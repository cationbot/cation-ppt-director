# Cation PPT Director

[中文介绍](#中文介绍) | [English Introduction](#english-introduction)

## 中文介绍

Cation PPT Director 是一个用于创建和优化商业汇报型 PowerPoint 的 Codex Skill，强调结论先行、管理者可读和业务判断清晰。

适用于经营复盘、业务汇报、年度规划、项目复盘、晋升述职，以及从过程稿到提交版的优化。

### 核心特点

- 先明确汇报目标、受众、重点与交付形态，再开始完整生成。
- 用有结论的标题和清晰主线组织内容。
- 强化数据、行动与业务判断之间的联系。
- 采用克制、专业的管理汇报视觉风格。
- 检查网格、字体、图表、表格、结构与整体审美。
- 明确区分事实、建议和待确认口径，不编造结论。

### 隐私说明

公开版不包含原始私人训练 PPT、截图、文件名、公司或员工名称、本地路径及原始业务内容。`references/` 中仅保留脱敏后的选择标准、聚合规律和可复用方法。

## English Introduction

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
git clone https://github.com/cationbot/cation-ppt-director.git \
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
