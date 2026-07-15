#!/usr/bin/env python3
"""Extract page-level text from PPTX files for style learning."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


PARA_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}p"
TEXT_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}t"


def natural_key(path: Path) -> list[object]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", path.name)]


def slide_number(path: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", path)
    return int(match.group(1)) if match else 0


def extract_pptx(path: Path) -> list[tuple[int, list[str]]]:
    slides: list[tuple[int, list[str]]] = []
    with zipfile.ZipFile(path) as zf:
        slide_names = sorted(
            [name for name in zf.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", name)],
            key=slide_number,
        )
        for slide_name in slide_names:
            xml = zf.read(slide_name)
            root = ET.fromstring(xml)
            texts = []
            for paragraph in root.iter(PARA_NS):
                parts = [(node.text or "") for node in paragraph.iter(TEXT_NS)]
                text = "".join(parts).strip()
                if text:
                    texts.append(re.sub(r"\s+", " ", text))
            slides.append((slide_number(slide_name), texts))
    return slides


def iter_pptx(target: Path) -> list[Path]:
    if target.is_file() and target.suffix.lower() == ".pptx" and not target.name.startswith("~$"):
        return [target]
    if target.is_dir():
        return sorted(
            [
                path
                for path in target.rglob("*.pptx")
                if not path.name.startswith("~$") and "/过程稿/" not in path.as_posix()
            ],
            key=natural_key,
        )
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="PPTX file or folder")
    parser.add_argument("--include-drafts", action="store_true", help="Include files under 过程稿/")
    args = parser.parse_args()

    target = Path(args.target).expanduser()
    if not target.exists():
        print(f"Not found: {target}", file=sys.stderr)
        return 2

    paths = iter_pptx(target)
    if args.include_drafts and target.is_dir():
        paths = sorted(
            [path for path in target.rglob("*.pptx") if not path.name.startswith("~$")],
            key=natural_key,
        )

    if not paths:
        print(f"No pptx files found: {target}", file=sys.stderr)
        return 1

    for deck_index, pptx in enumerate(paths):
        if deck_index:
            print()
        print(f"# {pptx}")
        try:
            slides = extract_pptx(pptx)
        except Exception as exc:  # noqa: BLE001 - diagnostic script
            print(f"ERROR: {exc}", file=sys.stderr)
            continue
        for number, texts in slides:
            title = texts[0] if texts else ""
            print(f"\n## Slide {number}: {title}")
            if texts[1:]:
                for text in texts[1:]:
                    print(f"- {text}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
