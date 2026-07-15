#!/usr/bin/env python3
"""Generate a Cation PPT training report from submitted decks and drafts."""

from __future__ import annotations

import argparse
import difflib
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


PARA_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}p"
TEXT_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}t"

HIGH_WEIGHT_DECKS: list[str] = []



@dataclass
class Slide:
    number: int
    title: str
    text: list[str]


@dataclass
class Deck:
    path: Path
    slides: list[Slide]


def slide_number(path: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", path)
    return int(match.group(1)) if match else 0


def natural_key(path: Path) -> list[object]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", path.name)]


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace(" . ", ".").replace(" / ", "/")
    return text


def extract_deck(path: Path) -> Deck:
    slides: list[Slide] = []
    with zipfile.ZipFile(path) as zf:
        slide_names = sorted(
            [name for name in zf.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", name)],
            key=slide_number,
        )
        for slide_name in slide_names:
            xml = zf.read(slide_name)
            root = ET.fromstring(xml)
            paragraphs: list[str] = []
            for paragraph in root.iter(PARA_NS):
                parts = [(node.text or "") for node in paragraph.iter(TEXT_NS)]
                text = clean_text("".join(parts))
                if text:
                    paragraphs.append(text)
            title = paragraphs[0] if paragraphs else ""
            slides.append(Slide(slide_number(slide_name), title, paragraphs[1:]))
    return Deck(path, slides)


def find_drafts(submitted: Path) -> list[Path]:
    draft_dir = submitted.parent / "过程稿"
    if not draft_dir.exists():
        return []
    return sorted(
        [
            path
            for path in draft_dir.rglob("*.pptx")
            if not path.name.startswith("~$") and "自动保存" not in path.name
        ],
        key=natural_key,
    )


def is_content_slide(title: str) -> bool:
    normalized = title.strip().lower()
    if not normalized:
        return False
    if normalized in {"thank you", "thanks"}:
        return False
    if normalized.startswith("完成进度"):
        return False
    if len(normalized) <= 4 and re.search(r"\d", normalized):
        return False
    return True


def classify_title(title: str) -> str:
    if re.search(r"\d|%|万|亿|\+", title):
        return "结果数字型"
    if any(word in title for word in ["关键路径", "重点", "规划", "计划", "下半年", "后续"]):
        return "路径规划型"
    if any(word in title for word in ["趋势", "承压", "问题", "稳定", "增长", "达标"]):
        return "判断结论型"
    if any(word in title for word in ["背景", "进展", "复盘"]):
        return "阶段说明型"
    return "主题结论型"


def short_body(slide: Slide, limit: int = 110) -> str:
    body = "；".join(slide.text[:3])
    body = re.sub(r"\s+", " ", body)
    return body[:limit] + ("..." if len(body) > limit else "")


def compare_titles(submitted: Deck, drafts: list[Deck]) -> list[str]:
    if not drafts:
        return ["未找到同目录过程稿，无法进行过程稿对比。"]
    submitted_titles = [s.title for s in submitted.slides if is_content_slide(s.title)]
    draft_titles: list[str] = []
    for draft in drafts:
        draft_titles.extend([s.title for s in draft.slides if is_content_slide(s.title)])

    matcher = difflib.SequenceMatcher(None, draft_titles, submitted_titles)
    inserts = 0
    deletes = 0
    replaces = 0
    equals = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "insert":
            inserts += j2 - j1
        elif tag == "delete":
            deletes += i2 - i1
        elif tag == "replace":
            replaces += max(i2 - i1, j2 - j1)
        elif tag == "equal":
            equals += j2 - j1

    similar_examples: list[str] = []
    for title in submitted_titles:
        close = difflib.get_close_matches(title, draft_titles, n=1, cutoff=0.45)
        if close and close[0] != title:
            similar_examples.append(f"过程稿「{close[0]}」-> 提交版「{title}」")
        if len(similar_examples) >= 4:
            break

    result = [
        f"过程稿标题池 {len(draft_titles)} 页，提交版内容页 {len(submitted_titles)} 页；匹配保留 {equals} 页，疑似新增/强化 {inserts} 页，疑似删除 {deletes} 页，疑似替换 {replaces} 页。",
    ]
    if similar_examples:
        result.append("标题变化样例：")
        result.extend([f"- {item}" for item in similar_examples])
    return result


def write_report(decks: list[Path], output: Path) -> None:
    lines: list[str] = [
        "# Personal PPT Training Report",
        "",
        "本报告从用户提供的提交版和同目录 `过程稿/` 中抽取页序、标题、正文摘要和标题变化，用于更新或验证 `cation-ppt-director` skill。",
        "",
        "## Summary",
        "",
    ]

    extracted: list[Deck] = []
    for deck_path in decks:
        if deck_path.exists():
            extracted.append(extract_deck(deck_path))
        else:
            lines.append(f"- 缺失：`{deck_path}`")

    total_slides = sum(len(deck.slides) for deck in extracted)
    total_content_slides = sum(1 for deck in extracted for slide in deck.slides if is_content_slide(slide.title))
    lines.extend(
        [
            f"- 高权重提交版：{len(extracted)} 份",
            f"- 总页数：{total_slides} 页",
            f"- 内容页：{total_content_slides} 页",
            "",
            "## Title Pattern Counts",
            "",
        ]
    )

    pattern_counts: dict[str, int] = {}
    for deck in extracted:
        for slide in deck.slides:
            if is_content_slide(slide.title):
                pattern_counts[classify_title(slide.title)] = pattern_counts.get(classify_title(slide.title), 0) + 1
    for pattern, count in sorted(pattern_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {pattern}: {count}")

    lines.extend(["", "## Deck Notes", ""])

    for deck in extracted:
        lines.append(f"### {deck.path}")
        lines.append("")
        content_slides = [slide for slide in deck.slides if is_content_slide(slide.title)]
        lines.append(f"- 页数：{len(deck.slides)}，内容页：{len(content_slides)}")
        lines.append("- 页级结构：")
        for slide in deck.slides:
            if not is_content_slide(slide.title):
                continue
            lines.append(
                f"  - P{slide.number}: {slide.title} [{classify_title(slide.title)}]"
            )
            summary = short_body(slide)
            if summary:
                lines.append(f"    - 摘要：{summary}")

        drafts = [extract_deck(path) for path in find_drafts(deck.path)]
        lines.append("- 过程稿对比：")
        for item in compare_titles(deck, drafts):
            lines.append(f"  {item}" if not item.startswith("- ") else f"  {item}")
        lines.append("")

    lines.extend(
        [
            "## Reusable Learnings",
            "",
            "1. 提交版标题多数不是中性模块名，而是带结果、路径或阶段判断的短句。",
            "2. Operating-review pages often connect KPI completion, core changes, key projects, and next steps; each page carries one clear judgment.",
            "3. 项目页常用“关键结果/背景/逻辑/路径/阶段复盘/后续计划”压缩过程稿信息。",
            "4. 数据页更重视与大盘、目标完成率、环比变化的关系，而不是展示所有细节数据。",
            "5. 提交版倾向把有效结论上移到标题，把解释性材料压到正文或小字注释。",
        ]
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="Markdown report output path")
    parser.add_argument("decks", nargs="*", help="Submitted PPTX decks to analyze. Pass explicit files; this script does not include private default paths.")
    args = parser.parse_args()

    if not args.decks:
        parser.error("provide at least one submitted PPTX deck; no private default deck paths are bundled")
    decks = [Path(item) for item in args.decks]
    write_report(decks, Path(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
