# Cation PPT Director

Cation PPT Director is a Codex skill for creating and improving conclusion-led, management-readable business presentations.

It is designed for operating reviews, business reports, planning decks, project retrospectives, promotion presentations, and draft-to-submit optimization.

## What It Emphasizes

- Result-driven storylines.
- Conclusion-bearing slide titles.
- Strong links between data, action, and business judgment.
- Restrained management-report design.
- Readable grids, typography, charts, tables, and diagrams.
- Structural validation and independent aesthetic review.
- Explicit uncertainty instead of fabricated conclusions.

## Privacy

This public package does not include the original private training decks, screenshots, filenames, company names, employee names, local paths, or raw business content.

The files under `references/` contain only anonymized selection guidance, aggregate pattern counts, and reusable presentation methods.

The scripts analyze only files explicitly provided by the person running them.

## Structure

```text
cation-ppt-director/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── style-rules.md
│   ├── training-samples.md
│   └── training-report.md
└── scripts/
    ├── analyze_training_decks.py
    └── extract_pptx_text.py
```

## Installation

Clone the repository into the Codex skills directory:

```bash
git clone https://github.com/<your-github-username>/cation-ppt-director.git \
  ~/.codex/skills/cation-ppt-director
```

Restart Codex or start a new task after installation so the skill catalog is refreshed.

## Usage

The skill supports automatic invocation when its description matches the task. It can also be invoked explicitly:

```text
Use $cation-ppt-director to turn my materials into a Cation-style business presentation.
```

Before generating a complete deck, provide the intended audience, reporting purpose, source materials, expected output, and any required template when possible.

## Utility Scripts

Extract text from a PPTX file or folder:

```bash
python3 scripts/extract_pptx_text.py "/path/to/deck-or-folder"
```

Generate a local training report from explicitly provided submitted decks:

```bash
python3 scripts/analyze_training_decks.py \
  --output "/path/to/report.md" \
  "/path/to/submitted-deck.pptx"
```

The scripts do not bundle private default paths or upload files.

## License

MIT License. See `LICENSE`.
