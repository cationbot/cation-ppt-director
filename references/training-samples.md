# Training Samples

This file describes how to use training examples without exposing personal paths, company names, employee names, or raw business content.

## Material Categories

Use user-provided examples in these anonymized categories:

- **High-weight submitted decks**: final meeting materials that the user considers submit-ready.
- **Process draft pools**: rough or intermediate versions used to learn how raw content becomes a submitted deck.
- **Scenario-matched references**: examples matching the current task type, such as operating reviews, annual planning, project retrospectives, promotion presentations, monthly reviews, or quarterly reviews.

Do not assume any local private path. If examples are needed, ask the user for the relevant folder or deck files, or use files already attached/provided in the current task.

## Learning Strategy

When creating or revising a deck:

1. Load the highest-weight examples matching the user's current scenario.
2. Extract slide titles and page order from submitted decks.
3. If process drafts exist for the same topic, compare process titles/order/content with the submitted deck.
4. Learn transformations rather than copying content:
   - Which pages were removed.
   - Which content was merged.
   - How titles became more conclusion-led.
   - How text was compressed.
   - How charts/tables were simplified.
   - How colors and alignment were standardized.
5. Use submitted decks as style and structure references, not as factual evidence for new claims unless the user asks to reuse their content.

For anonymized page-level examples and the first training summary, read `training-report.md`. It includes:

- Title pattern counts.
- Page-level structure patterns.
- Process-draft title pool comparison patterns.
- Reusable learnings from submitted decks.

## Suggested Matching

For operating reviews / business reviews:

- Start with final submitted operating-review decks from the same business area or metric type.
- Prefer recent decks if the user provides multiple periods.

For annual planning:

- Start with annual or half-year planning decks.
- Compare target-setting pages with current-state diagnosis pages.

For promotion presentations:

- Start with promotion or personal-impact decks only if the user provides them for this task.
- Preserve the user's current privacy boundary and do not reuse personal biography content unless explicitly requested.

For project retrospectives:

- Start with folders containing explicit retrospective materials and any matching process drafts.

For business reports to non-local teams:

- Prefer externally polished or cross-functional communication decks, if provided.

## Useful Extraction Script

Use `scripts/extract_pptx_text.py` to extract page-level text from PPTX files:

```bash
python3 scripts/extract_pptx_text.py "/path/to/deck.pptx"
```

For a folder:

```bash
python3 scripts/extract_pptx_text.py "/path/to/folder"
```

Use the extracted titles to study structure before making recommendations.
