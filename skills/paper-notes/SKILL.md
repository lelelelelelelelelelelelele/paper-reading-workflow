---
name: paper-notes
description: Create and evolve workspace-local Obsidian work notes for active academic-paper reading, especially ML, robotics, VLA, VLM, and embodied-AI papers. Use when the user asks for a pre-read map, companion reading, section-by-section self-tests, answer correction, a critical post-read review, or group-meeting reading notes, and when paper-reading-intake delegates its upstream reading stage. Keep learning traces and user insights here. Do not use this skill to create the final literature archive or self-contained HTML; use paper-reading-intake for that.
---

# Paper Notes

Create structured, reviewable, critical work notes for active paper reading. Keep the learning trace here; let `paper-reading-intake` create the clean formal archive later.

## Apply the user's reading style

- Focus on VLA / VLM / world-action-model / embodied-AI research when relevant.
- Support a technically strong reader who reads English carefully and tests paper logic through questions.
- Prefer a plain-spoken Chinese voice with English terms inline, limited bolding, and no deck slogans.
- Judge papers by role and controlled evidence, not leaderboard rank alone.
- Keep learning-oriented observations separate from reviewer criticism.

## Build one growing work note

Use these stable sections and the detailed structure in [references/note-template.md](references/note-template.md):

| Section | Purpose |
|---|---|
| Paper identity + one-line position + logic chain | Stable foundation and paper identity |
| Motivation Map | What to learn from the paper |
| Key results and evidence anchors | Exact figure/table/section pointers for later verification |
| Mechanism clarifications | Corrected explanations of common misunderstandings |
| Guided Q&A | Self-tests, corrected answers, and interaction insights |
| Personal judgment | Sharp insight, research-line use, and advisor questions |
| Cross-paper positioning | Neighbors, tensions, combinations, and idea ammunition |
| Reviewer score | Venue-specific critical assessment |

Keep pre, companion, and post work in one file. Do not open a new note for each stage.

## Choose the reading stage

| Stage | Trigger | Output and frontmatter |
|---|---|---|
| `pre` | "我要读 X", "读前地图" | Identity, tentative logic chain, Motivation Map, open questions; `status: drafting` |
| `companion` | "陪我读", "边读边问", self-test request | Add guided Q&A and corrected checkpoints; `status: drafting` |
| `post` | "我看完了", critical review request | Add judgment, positioning, reviewer score, and unresolved evidence; `status: complete` when structurally finished |

Set `review_status: ai-draft` until the user has reviewed the conclusions. Set `review_status: user-reviewed` only after explicit user confirmation.

### Run companion reading as interaction

1. Start with a pre-read map, then move one section at a time: Intro → Method → Experiments → Ablation.
2. Ask 2–3 anchored self-test questions after each section.
3. Let the user answer 1–3 questions at a time before correcting.
4. Correct the concept before writing the durable answer. Keep only lightweight states such as "已订正", "方向对但需补全", or "仍待确认".
5. Use questions to guide a stuck reader before giving a direct explanation.
6. Provide objective text, figures, and numbers when the document is hard to read, but leave interpretation to the user when possible.
7. Preserve the user's useful insight after removing conversational noise and adding enough context.
8. End each section with a one-line checkpoint.
9. Move to post only after the paper has actually been read and discussed.

Never fabricate the user's blind answers or silently mark companion reading complete.

## Execute the work-note workflow

1. **Establish identity**: resolve title, version, source links, and a stable `paper_id`. Prefer `arxiv:YYMM.NNNNN`, then lowercase DOI, then `zotero:<key>`; use title matching only for legacy notes.
2. **Find the existing note**: search the active workspace-local Obsidian vault by stable ID before creating a file. Resume the same note when it exists.
3. **Collect sources**: use authoritative paper text and available fulltext tools. Do not invent details from the abstract.
4. **Position the paper**: write `## 一句话定位` and `## 核心逻辑链（problem → method → validation）` first.
5. **Judge by role**: classify VLM, VLA, data method, training paradigm, inference method, benchmark, or system before comparing it.
6. **Fill the current stage**: use [references/note-template.md](references/note-template.md) and update lifecycle frontmatter.
7. **Critique evidence**: read [references/critique-checklist.md](references/critique-checklist.md) for modules 3 and 4. Verify a supposedly missing baseline before criticizing it.
8. **Score the right venue**: read [references/venue-scoring.md](references/venue-scoring.md) before module 4.
9. **Link the research graph**: add `[[wikilink]]` connections to related notes and ideas.
10. **Return a handoff**: when invoked by intake, report the work-note path, `paper_id`, reading stage, review status, and unresolved items. Do not create the formal archive or HTML.

## Store the work note in Obsidian

### Discover the workspace-local vault

1. Read applicable project instructions for an explicit notes or Obsidian path.
2. Inspect existing workspace children such as `notes/` and `obsidian/`.
3. Confirm a candidate vault by locating `.obsidian` in the directory or resolved junction target.
4. Follow the vault's existing paper-note filename and folder conventions, including a flat root when that is the established style.
5. Ask about placement only when inspection leaves multiple materially different vaults.

Do not hardcode a username, drive letter, or personal vault root in this repository. Do not assume every `notes/` directory is an Obsidian vault.

### Keep work notes separate from formal archives

- Keep the work note in the workspace-local vault through pre, companion, and post.
- Do not automatically move or copy it to `20 Literature` after post.
- Let `paper-reading-intake` create the clean literature Markdown and self-contained HTML when formal archival is requested.
- Keep `archive_note` empty until that archive exists, then add a reciprocal wikilink only when editing the work vault is allowed.
- Treat vault operations as add/update only by default. Never delete or move an existing note without explicit authorization.

### Use frontmatter contract v1

```yaml
---
type: paper-note
producer: paper-notes
schema_version: 1
paper_id: "arxiv:YYMM.NNNNN"
reading_stage: pre
status: drafting
review_status: ai-draft
owner: ai
source: ai-draft
tags: [论文阅读, <方向>, <简称>]
related:
  - "[[相关笔记]]"
zotero_key: <key>
arxiv: <id>
doi: <doi>
venue: <venue>
created: YYYY-MM-DD
archive_note: ""
---
```

Use absolute dates. Preserve existing user-authored fields when upgrading a note. Do not rewrite a legacy note merely to satisfy this contract unless the current task requires editing it.

## Keep Obsidian-native structure

- Use `[[wikilink]]` in frontmatter and prose.
- Follow the vault's established Chinese tags.
- Use MathJax for formulas.
- Use callouts or folds for long self-test sections.
- Anchor claims to figures, tables, equations, sections, or appendices.
- Use vault-relative paths for any local images.

## Avoid these failures

- Do not copy the abstract as a note.
- Do not preserve an incorrect blind answer as the final technical conclusion.
- Do not judge a data or method paper only by absolute leaderboard rank; use controlled gain.
- Do not invent method details when the paper text is unavailable.
- Do not create the formal `20 Literature` note or HTML from this skill.
- Do not create a second file when the same paper already has a pre or companion note.
