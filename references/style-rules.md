# Cation PPT Style Rules

## Core Positioning

This skill should produce Cation-style PPT materials: restrained, conclusion-led, business-analysis oriented, and suitable for management-facing operating reviews.

Priority scenarios:

1. Operating review / business review
2. Business report
3. Project retrospective

Secondary scenarios:

- Annual planning
- Promotion presentation
- Monthly review
- Quarterly review

Primary audiences:

- Management review meetings
- Product or business leadership
- Cross-functional teams
- Executive stakeholders

## Storyline Preferences

Default to result-driven logic. Present the result first, then connect actions and data to that result.

For existing progress:

- Title presents key conclusion.
- Body puts result first.
- Then explain actions and data.

For planning:

- Title presents key path.
- Body includes background, problem, and planned actions.

Avoid:

- 流水账.
- Simple ideas split into unnecessary 1/2/3 points.
- Data dumps.
- Similar dimensions repeated across multiple tables on one page.
- Claims where the data and result do not match.

Important caution:

If an action only helped a specific segment, do not claim it improved the whole business unless the deck provides a strong causal argument and supporting big-picture data.

## Scenario Structures

### Operating Review / Business Review

Use this default order:

1. KPI completion overview
2. Core metric movement
3. Key projects
4. Stage summary
5. Next-stage targets and risks
6. Key actions

### Annual Planning

Use a structure close to an operating review, but start with target situation and actual metric movement:

1. Target situation and actual metric movement
2. Current-state judgment
3. Annual target
4. Key path
5. Growth projects and rhythm
6. Risks and resource asks

### Project Retrospective

Answer:

- What was the background?
- What problem needed to be solved?
- What was done, and when?
- How did the solution perform after launch?
- What issues remain?
- How should it improve?
- What comes next?

### Promotion Presentation

Main line:

- Business result breakdown
- Concrete actions behind each result
- Reusable method
- Problems solved
- Future team plan
- Future business plan

## Title And Copy Rules

Every slide title needs a conclusion. There are no normal exceptions.

- Completed progress: title should show data performance or result judgment.
- Future plan: title should show method or key path.
- Neutral labels such as "Project Background", "Data Analysis", or "Problem Statement" are allowed only when needed, but titles must not become too long.

Numerical title rules:

- Prefer absolute values where available.
- Avoid exaggerated claims, especially revenue claims.
- Growth above 100% usually needs verification.
- Do not overload the title with too many numbers.

Body copy:

- Prefer short phrases.
- Avoid wordy paragraphs.
- Keep text simple and readable.
- Use large enough fonts.
- Use a tone that is judgmental but restrained.
- Avoid overclaiming.

Common business terms can be used when they carry meaning; do not mechanically ban them.

## Data Rules

Default data-page logic: `result + number`.

Metric handling:

- Preserve source-defined metric formulas.
- If a metric definition is missing, ask before calculating or state the assumption explicitly.
- Use the source's reporting currency, region, cohort, and denominator unless the user asks to normalize.

Common dimensions:

- Month-over-month change
- Target completion rate

Use year-over-year change, region, user segment, and project contribution when they directly support the slide's claim.

When performance is poor:

- Expose the issue.
- Emphasize follow-up actions.

When performance is good:

- Highlight business contribution.
- Explain the link between action and contribution.
- Avoid excessive self-credit.

Chart preferences:

- Use line charts and bar charts often.
- Avoid too many numbers inside charts.
- Reduce font size or hide excessive axis labels where visual clarity benefits.
- Use at most two core charts or tables per page.
- Split the page if more than two core charts/tables are needed.

Data notes:

- Add small, light-colored notes for segment scope or date scope when ambiguity is likely.

## Layout Rules

Default visual identity:

- Light or white background.
- Business-analysis material, not decorative presentation material.
- Avoid dark page backgrounds.
- Use deep blue for emphasis.
- Use red and green only when the local business convention is clear.
- Avoid too many colors on one page.

Font hierarchy:

- Main title: around 24pt.
- Page conclusion / target line directly under the main title: 12-14pt. In operating-review materials, this line is usually the page's key conclusion, target, or reporting scope, not a footnote.
- Subheaders: 12-14pt.
- Body text: at least 10pt.

Preferred layouts:

- Top-conclusion-bottom-breakdown
- Three parallel cards
- Left/right split
- Left-conclusion-right-chart

Information density:

- Maintain meaningful density.
- Data pages can be less dense.
- Method and planning pages should include product visuals or process visuals where helpful.

Avoid:

- Too much text.
- Too many colors.
- Misalignment.
- Vague titles.
- Unhighlighted key content.
- Overly decorative backgrounds.
- Tables whose rows/columns are not aligned.

Template use:

- If the user provides a template, use it as the visual baseline.
- If no template is provided, use a clean light-background management-report style.

## Submit-Ready Layout Gate

This gate turns the style preference into concrete page constraints. Apply it whenever creating or revising PPTX pages, especially for operating reviews and management-facing submissions.

### Grid And Spacing

- Use a clear grid before placing content. For operating-review materials, output exact Office 16:9 by default and verify PPTX XML `p:sldSz` is `12192000 x 6858000`; do not rely only on visual aspect ratio or PowerPoint labels.
- For 16:9 slides, keep outer margins around 0.5-0.6 inch unless following a source template.
- Keep module gaps at least 0.25 inch and card inner padding at least 0.20-0.25 inch.
- Align repeated cards, headers, timelines, tables, and diagrams to the same x/y coordinates. Avoid hand-placing each module independently.
- Content pages should normally use the available page area. If there is wide empty space and the page is not a cover/transition/data-breathing page, enlarge the content or spread modules more deliberately.
- Treat module grouping as part of the grid. Notes, legends, and scope notes belong visually to the module they explain.
- For parallel modules on the same page, keep title-to-content distance, content-card start position, card height, and internal padding consistent.

### Font Scale

- Main title: 22-25pt.
- Subtitle / page conclusion line: 12-14pt, with 12pt as the minimum for operating-review pages.
- Section header bars: 14-16pt.
- Card titles / subheaders: 11-12pt.
- Body text: generally 10pt or above.
- Notes, captions, source notes, and non-critical labels: 8-9pt.
- Do not use text below 8pt. If text would need to go below 8pt, reduce words, change layout, or split the page.

### Density And Fit

- If content feels cramped, first shorten wording and combine points; do not solve it by shrinking the font.
- If there is available space, increase line spacing before shrinking text. Key conclusion boxes and card body copy should look relaxed; two-line key conclusions should use roughly 1.5 line spacing.
- If line spacing cannot be controlled by the PPT generation API, split text into multiple text boxes and place them on fixed y coordinates to simulate consistent line height.
- Avoid awkward text wrapping, especially a single leftover character on a line. Shorten copy or manually split lines before reducing font size.
- When using fixed line spacing, ensure every line is short enough to avoid automatic wrapping; otherwise lines can overlap or look cramped.
- If a page has too much content for readable 10pt body text, split modules or split the page.
- One content page should usually carry no more than two main modules, or three clean parallel cards. Four or more dense blocks require a deliberate reason.
- Prefer fewer, stronger proof objects over many small decorative visuals.

### Diagrams And Visual Objects

- Every flowchart, arrow, timeline, dot, and KPI card must have a business meaning and readable labels.
- Do not leave unlabeled decorative circles, arrows, or icons in management-report pages.
- Do not leave orphaned bottom strips, floating notes, or standalone capability labels.
- Use process tables or milestone grids instead of small timelines when actions and dates both matter.
- Use red primarily for risk, warning, or key negative constraints. If red is also used for business uplift, make the semantic distinction obvious or use navy/black for positive business figures.
- KPI cards must establish a clear numeric hierarchy: the primary number is largest and visually dominant; the unit and change percentage are smaller, secondary, and spaced far enough from the number to avoid crowding.
- In action cards, icon, time label, title, and body text should align around a shared visual center. Avoid top-heavy or bottom-heavy cards where the text sits too close to either card edge.

### Visual QA

- Render final slides as images before delivery.
- Check each slide for alignment, clipping, awkward wrapping, inconsistent font scale, too-small text, low contrast, excessive empty space, unclear module grouping, and chart/diagram labels that do not explain the logic.
- Check PPTX structural integrity, not only rendered appearance: run `unzip -t`, unpack the PPTX, scan slide XML for negative dimensions like `cx="-` / `cy="-`, and scan for `NaN`, `Infinity`, `undefined`, `placeholder`, `xxxx`, `lorem`, or other invalid/leftover tokens.
- For operating-review materials, also verify exact 16:9 `p:sldSz` and that title-area conclusion/target lines are at least 12pt.
- Avoid generation patterns that create negative OOXML extents, especially diagonal lines produced by subtracting endpoint coordinates. Use safe connectors, positive-width/height lines, or milestone/table layouts instead.
- When any visible issue appears, fix and rerender at least once before calling the page final.
- Every complete PPT produced through this skill must receive an independent aesthetic review before final delivery. Prefer an independent sub-agent when the environment supports it; otherwise use a separate presentation tool, an isolated second visual-review pass, or another independent review mechanism.
- After that review, perform any necessary format correction, alignment cleanup, spacing adjustment, and visual polish. State which independent review method was used; do not rely only on the original generation pass.

## Draft-To-Submit Rules

Most common transformation types:

- Reorder pages.
- Strengthen titles.
- Adjust font sizes and formatting.
- Reduce text.
- Mark key progress.

Delete or recommend deleting pages when:

- Data support is weak.
- There is no conclusion.
- Information repeats.
- Information density is too high.

Merge pages when:

- They have similar nature.
- Content repeats.

Improve submitted-style pages by:

- Moving conclusions into titles.
- Unifying font and formatting.
- Reducing colors.
- Aligning table rows and columns.
- Reducing words.

When process materials are abundant but conclusion is unclear:

- Create a new revised page based on the process draft.
- State the proposed conclusion.
- Ask for confirmation before changing the user's underlying point of view.

When data is useful but expression is weak:

- Create a new revised page based on the process draft.
- Strengthen the title and action-result linkage.

## Observed High-Weight Deck Patterns

The anonymized training pass covered 8 high-weight submitted decks, 144 total pages, and 138 content pages.

Observed title pattern counts:

- Result-number title: 57
- Theme-conclusion title: 50
- Judgment-conclusion title: 16
- Path-planning title: 12
- Stage-description title: 3

Implications:

- Default to titles that carry results, numbers, path, or judgment rather than neutral labels.
- Use neutral labels only as section dividers or when the page's function is navigation.
- For operating reviews, a strong title often combines scope + result, such as a business area plus completion, trend, or target pressure.
- For project pages, a strong title often combines mechanism + business outcome.
- For planning pages, a strong title often combines user segment + key path.

Observed process-draft transformation:

- Annual planning had very large draft pools; the submitted deck compressed and selected only high-claim pages.
- Operating reviews often preserved some titles but rewrote others to make the business claim more direct.
- Quarterly and special-topic materials showed heavy replacement: rough materials were reduced into a smaller set of trend, progress, and scenario pages.
- Submitted pages tend to move the strongest conclusion into the title and move explanation, data scope, or operational detail into body text or notes.

## Output Rules

Default flow:

1. First output slide thumbnails for layout confirmation.
2. After confirmation, output editable PPTX.

Page-level outline:

- Provide it when it can improve the structure.
- It is not mandatory for every task.

Page ranges:

- Operating review / business review: within 15 pages.
- Annual planning: within 20 pages.
- Promotion presentation: within 20 pages.

Include:

- Speaker notes when useful.
- Text-only modification advice for draft optimization.

Do not include by default:

- Formal review-risk lists, unless the user asks.

Allowed source use:

- Excel source data.
- Historical PPT materials provided by the user.
- Local knowledge-base materials when relevant.

Default delivery folder:

- Use the current workspace or user-specified output folder.

## Approval And Safety Rules

Pause and ask before:

- Rewriting the user's original point of view.
- Deleting substantive content.
- Adding industry, competitor, or management judgments.
- Inferring data or conclusions from weak evidence.

When asking, state:

- What will be changed.
- Why it should change.
- What evidence supports the change.

Quality standard for "ready to submit":

- Font size and alignment are adjusted.
- No obvious logic errors.
- Same expression is consistent across the deck.
- No typos.
- No format disorder.

Most unacceptable AI PPT problems:

- Generic template feeling.
- Misaligned formatting.
- 流水账.
- Vague titles.
- Fabricated data.
- Logic jumps.

Pre-output self-check:

- Obvious grammar errors.
- Typos.
- Context confusion.
- Wrong or inconsistent formatting.
- Whether fonts and hierarchy are correct.
