---
name: paper-reading-intake
description: Archive technical papers into a durable Obsidian knowledge base as one canonical Markdown note plus one self-contained HTML report, using paper-native figures, evidence checks, topic/index updates, and an upstream paper-notes work note when available. Use when the user asks to put a paper in Obsidian, "看完放 OB", produce a figure-rich HTML archive, update a reading list, or preserve a paper discussion as a formal record. Hand active read-along, self-test, and pre/post reading-note work to paper-notes. Do not use for manuscript writing, rebuttals, or chat-only fact lookups.
---

# Paper Reading Intake

Turn a paper-reading session into a clean, durable archive. Treat the final literature Markdown as the editable source of truth and the self-contained HTML as its reading surface. Keep upstream reading traces in `paper-notes`; do not merge raw self-test history into the formal archive.

## Resolve the environment

1. Locate the active formal Obsidian vault and its literature, topic, output, and index conventions.
2. Distinguish the formal archive vault from any workspace-local Obsidian vault used for active reading notes.
3. Inspect existing notes before choosing a destination. Prefer semantic placement over the first convenient folder.
4. Detect paths and sync targets on the current machine. Never assume a username, drive letter, vault root, or rclone remote.
5. Read [references/workflow.md](references/workflow.md) for a full archive. Read [references/notes-consumption.md](references/notes-consumption.md) before matching, resuming, or consuming `paper-notes` artifacts.

## Execute the workflow

### 1. Establish the source and identity

- Resolve the authoritative paper HTML or PDF, title, authors, version, project page, and code repository when available.
- Assign a stable `paper_id`: prefer normalized arXiv ID, then DOI, then Zotero key; use a normalized title only as a legacy fallback.
- Prefer primary sources for technical claims.
- Record the paper version and access URL in both final artifacts.
- Keep the source-background check in default-collapsed metadata: an Obsidian `[!info]-` callout and HTML `<details>` without `open`. Follow [references/workflow.md](references/workflow.md#source-background-metadata) for publication, venue/author context and selected key-reference/baseline checks. Preserve the same findings, scope and checked date in both outputs.

### 2. Resolve the upstream reading state

Search workspace-local Obsidian vaults for the same paper, following the matching rules in `references/notes-consumption.md`.

- If a matching `producer: paper-notes` note is `reading_stage: post` and `status: complete`, consume it as upstream context.
- If a matching note is at pre or companion stage, resume that same note with `paper-notes`; do not create a duplicate.
- If no note exists and the user wants deep reading, explanation, or companion reading, hand off to `paper-notes` before archival.
- If the user explicitly wants archive-only work, declines deep reading, or `paper-notes` is unavailable, continue in direct mode and set `reading_provenance: direct`.
- If multiple candidates remain ambiguous after stable-ID matching, present the candidates instead of choosing the first file.

Never fabricate companion completion. Companion reading requires the user's own reading, answers, and corrections.

### 3. Classify before drafting

State:

- the paper type: method, system or tech report, benchmark, representation bridge, data paper, or tooling;
- the layer it changes: data, representation, backbone, policy or action head, training, inference, or system infrastructure;
- whether it is mainline, direct competitor, side branch, background, or unrelated to the user's project;
- what evidence could change that classification.

Use this classification to choose the topic hub, note headings, and reading-list placement.

### 4. Collect and verify paper-native evidence

- Fetch the paper's original figures and captions before making explanatory visuals.
- Keep stable figure filenames and preserve figure numbers.
- Recheck exact numbers, captions, paper version, and technical claims against primary sources even when a `paper-notes` note exists.
- Separate benchmark evidence, ablation, representation probes, internal sanity checks, qualitative figures, and demos. Do not describe them as equally strong.
- Use custom diagrams only when the user explicitly requests one or the paper lacks an adequate visual.

### 5. Build the final pair

Produce exactly two durable archive artifacts:

- `20 Literature/<Paper>.md`: the canonical editable source, adapted to the vault's established literature path;
- `50 Outputs/HTML Format References/<slug>_REPORT.html`: the matching browser-readable report.

Choose the note's structure from the knowledge to retain and its intended use: concepts and their dependencies, mechanisms, methods, evidence, or the requested task result. Use only the helpful parts of [assets/paper-note-template.md](assets/paper-note-template.md) and [assets/paper-report-template.html](assets/paper-report-template.html); headings and order are examples, not a required outline. Omit empty or irrelevant sections. Organize the editable Markdown first, then generate or update HTML from the same content.

Use scratch Markdown or extracted figures only as temporary generation inputs. Do not preserve a third workspace `<slug>_REPORT.md` as another knowledge-base truth. Embed figures directly in HTML as base64 `data:` URIs; do not keep a sibling figures directory for the archived report.

### 6. Explain figures by function

For each core figure included in the requested note, explain as relevant:

1. What experiment, component, or claim is shown?
2. What is the setup?
3. What does the figure actually support?
4. What does it not prove?
5. Why does it matter to the user's research line?

Lead with the supported conclusion, then explain the mechanism. Preserve important caveats beside the figure that creates them. These questions guide the explanation; they do not require fixed subheadings or a new critical review. Add further critical evaluation only when requested, and retain valid critique already established in the discussion.

### 7. Synthesize discussion into reusable knowledge

When asked to organize or update a note, combine the relevant multi-turn discussion with the existing note in the requested scope. Rewrite it as independently understandable knowledge, organized by the relationships between ideas and their use. Several questions may become one explanation; one clarification may require changes across several sections. Do not preserve the order of chat turns or make each question its own note section.

- Carry over corrected conclusions, evidence anchors, mechanism clarifications, project relationships, final judgments, and useful user insights. Keep raw blind answers, wrong-answer history, and uncorrected discussion in the upstream work note.
- Merge repeated and synonymous explanations. Integrate supported corrections into the affected prose and revise dependent reasoning, examples, figure explanations, metrics, and conclusions. Do not leave an obsolete explanation beside a later correction for the reader to reconcile.
- Judge corrections by their evidence and conditions, not by recency alone. Preserve genuinely unresolved questions, conflicts, and unknowns beside the relevant claim without presenting them as settled.
- Retain the background, definitions, conditions, examples, key reasoning, and sources needed to understand and reuse the content without reopening the chat. Familiarity or use in only one course is not a reason to discard useful knowledge.
- Keep original figures, formulas, metrics, and source anchors where they support the explanation. Preserve the self-contained HTML figure handling and the text-focused vault note's link to that visual reading surface.
- Update existing related prose within the requested scope, retaining still-valid content. Reflect substantive changes in structure, explanation, facts, or conclusions in both Markdown and HTML.
- Keep completion recaps in the chat reply only. Saved notes contain the integrated knowledge, not update logs, modification summaries, or a chronology of the discussion. Unresolved knowledge and material limitations still belong in the relevant prose.

This changes note synthesis, not the companion-reading method, reader questions, or self-test rhythm. Keep critical evaluation independent and on demand. Do not introduce a fixed note template, compulsory review, score, or new learning routine.

### 8. Archive and link

Follow the vault's conventions. A typical archive contains:

- one canonical literature Markdown with `producer: paper-reading-intake`;
- one self-contained HTML report;
- a `source_note` link to the upstream work note when present;
- a reading-list or topic-hub link;
- a literature-index entry.

Do not move or delete the upstream work note. Add a reciprocal `archive_note` link only when the active vault policy allows editing it. Do not duplicate full reports across folders or create a separate assets directory for report figures.

### 9. Verify the result

- Open or render the HTML and confirm that all images load offline.
- Check that Markdown and HTML agree on conclusions and key numbers.
- Read the note without the chat: check that essential context and reasoning remain, repeated explanations are integrated, supported corrections reach all affected claims, and unknowns remain clear. Check that no Q&A chronology or completion recap has been inserted into the note.
- Confirm that `paper_id`, `reading_provenance`, and `source_note` reflect the actual route.
- Confirm that raw reading traces remain only in the work note.
- Confirm that topic placement reflects the conceptual relationship.
- Run the smallest real sync verification supported by the vault.
- Report every unverified source, missing figure, legacy match, direct-mode downgrade, or sync gap.

## Completion criteria

Finish only when:

- the paper identity and classification are stable;
- the upstream reading state or direct-mode decision is explicit;
- core paper-native evidence has been rechecked;
- one canonical Markdown and one self-contained HTML exist and agree;
- relevant discussion has been synthesized into reusable prose, with supported corrections integrated and necessary context, evidence, and unknowns preserved; raw self-test history remains upstream;
- vault links, topic placement, and indexes are updated when requested;
- HTML rendering and applicable sync have been checked.
