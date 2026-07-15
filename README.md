# Cation PPT Director

> 把“信息很多，但讲不清楚”的材料，整理成管理者一眼能抓住重点的 PPT。

这是我把自己长期使用的商业汇报方法整理成的一个 Codex Skill。

它不只是帮你把文字放进幻灯片，而是先弄清楚：**为什么汇报、讲给谁听、最重要的判断是什么**，再把零散材料组织成结论清楚、逻辑连贯、视觉克制的提交版。

适合经营复盘、业务汇报、年度规划、项目总结、晋升述职，以及那些“内容基本都有，但离正式提交还差一口气”的 PPT。

## ✨ 它会帮你做什么

- 在完整生成前，先校准汇报目标、受众、重点和交付形态。
- 从材料中提炼真正值得放进标题的结论，而不是堆满描述。
- 串起数据、行动和业务判断，让每一页都服务于主线。
- 控制信息密度和视觉层级，保持专业、克制、管理者可读。
- 分别检查内容质量和文件质量，避免“技术上没问题，实际上不好讲”。
- 明确区分已有事实、补充建议和待确认口径，不替你编造结论。

## 它更适合这些场景

- 手里有 Word、Excel、旧 PPT 或一堆零散材料，不知道如何组织。
- 过程稿内容很多，但主线不够清楚，标题也没有结论。
- 想把业务汇报做得更像正式提交版，而不是套模板拼页面。
- 已经有一份 PPT，希望得到逐页诊断、修改建议或直接优化。
- 希望保留个人表达和业务判断，而不是生成一份“AI 味”很重的通用稿。

## 它不会做什么

- 不会为了显得完整而擅自扩写一整套新交付物。
- 不会用不存在的数据填满页面。
- 不会把视觉华丽误认为内容有说服力。
- 在目标还不清楚时，不会直接投入完整 PPT 制作。

## 🚀 快速开始

把仓库克隆到 Codex 的 Skill 目录：

```bash
git clone https://github.com/cationbot/cation-ppt-director.git \
  ~/.codex/skills/cation-ppt-director
```

安装后重新启动 Codex，或新建一个任务，让 Skill 列表重新加载。

它支持根据任务语义自动触发，也可以明确调用：

```text
使用 $cation-ppt-director，把我的材料整理成一份面向管理层的业务汇报 PPT。
```

为了得到更好的结果，建议同时提供：汇报对象、汇报目的、原始材料、期望产物，以及必须沿用的模板或限制。

## 隐私与公开范围

这个仓库是从我的私人版本中生成的公开脱敏版。

它**不包含**原始训练 PPT、截图、真实文件名、公司或员工名称、本地路径及原始业务内容。`references/` 中只保留脱敏后的选择标准、聚合规律和可复用方法；脚本也只会分析使用者明确提供的文件。

## 工具脚本

提取单个 PPTX 或文件夹中的文字：

```bash
python3 scripts/extract_pptx_text.py "/path/to/deck-or-folder"
```

根据明确提供的提交版 PPT 生成本地分析报告：

```bash
python3 scripts/analyze_training_decks.py \
  --output "/path/to/report.md" \
  "/path/to/submitted-deck.pptx"
```

脚本不包含私人默认路径，也不会主动上传文件。

<details>
<summary>查看仓库结构</summary>

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

</details>

## English

Cation PPT Director is a Codex skill for turning scattered business materials into conclusion-led, management-readable presentations.

It clarifies the audience, purpose, key judgment, and expected output before building a complete deck. It is designed for operating reviews, business reports, planning decks, project retrospectives, promotion presentations, and draft-to-submit optimization.

The public package contains no original private training decks, screenshots, company information, local paths, or raw business content.

## License

MIT License. See `LICENSE`.
