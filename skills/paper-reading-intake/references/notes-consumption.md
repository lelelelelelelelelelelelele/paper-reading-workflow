# Consuming paper-notes

Use this reference when `paper-reading-intake` must locate, resume, or consume a work reading note.

## Contents

- [Locate work-note vaults](#locate-work-note-vaults)
- [Match the same paper](#match-the-same-paper)
- [Interpret lifecycle state](#interpret-lifecycle-state)
- [Consume content safely](#consume-content-safely)
- [Handle legacy notes](#handle-legacy-notes)
- [Link both layers](#link-both-layers)

## Locate work-note vaults

1. Read applicable project instructions for an explicit notes or Obsidian path.
2. Inspect workspace children such as `notes/` and `obsidian/` only when they exist.
3. Confirm a candidate is an Obsidian vault by finding `.obsidian` in that directory or its resolved junction target.
4. Follow the candidate vault's existing paper-note filename and folder conventions.
5. Search broader personal vaults only when no workspace-local vault exists or the user identifies another source.

Do not assume that every directory named `notes` is an Obsidian vault. Do not assume that work notes belong in the formal `20 Literature` archive.

## Match the same paper

Use the following priority and confirm the title after every match:

1. Exact normalized `paper_id`:
   - `arxiv:YYMM.NNNNN` without a version suffix;
   - `doi:<lowercase-doi>`;
   - `zotero:<key>` when no publication identifier exists.
2. Exact `arxiv`, `doi`, or `zotero_key` fields.
3. Canonical paper URL after removing tracking parameters and arXiv version suffixes.
4. Normalized title as a legacy fallback only.

Require `producer: paper-notes` for contract-v1 work notes. Never treat a `producer: paper-reading-intake` archive as its own upstream source. Never select the first generic `type: paper-note` match.

When two candidates remain:

- prefer exact publication-ID matches over title matches;
- prefer `producer: paper-notes` over untyped legacy notes;
- prefer the note with the furthest valid `reading_stage`, but do not merge conflicting user insights silently;
- present unresolved candidates to the user.

## Interpret lifecycle state

| Work-note state | Intake action |
|---|---|
| `reading_stage: post`, `status: complete` | Consume the note, then verify evidence against primary sources |
| `reading_stage: pre`, `status: drafting` | Resume the same note with `paper-notes`; do not archive as if deeply read |
| `reading_stage: companion`, `status: drafting` | Continue the user's read/self-test loop before post archival |
| `review_status: ai-draft` | Preserve the provenance; do not imply user confirmation |
| `review_status: user-reviewed` | Treat user judgments as reviewed, while still verifying technical facts |
| no work note + deep-reading intent | Invoke or hand off to `paper-notes` |
| no work note + archive-only intent | Use direct mode and record `reading_provenance: direct` |
| `paper-notes` unavailable or user declines | Explain the downgrade and offer direct mode |

Companion state cannot be completed by inference. It depends on the user's own reading and answers.

## Consume content safely

### Required inputs

- paper identity, version, and source links;
- `## 一句话定位`;
- `## 核心逻辑链（problem → method → validation）`;
- `## 关键结果与证据锚点`;
- corrected `## 机制辨析` sections;
- project-line relationship and final judgment;
- unresolved items and evidence gaps.

### Optional inputs

- module 3.5 cross-paper positioning;
- venue/reviewer score;
- user insights that have enough context for a formal archive.

### Keep upstream only

- raw blind answers and wrong-answer history;
- lightweight correction markers whose only purpose is learning trace;
- uncorrected comments or contextless reactions;
- claims that cannot be tied to a primary-source anchor.

Rephrase consumed material for the formal archive. Do not copy the work note wholesale.

## Verify against primary evidence

Use the work note to decide what matters and where misunderstandings occurred. Use the paper, official supplement, project page, and repository to verify:

- exact metrics and comparison conditions;
- figure/table numbers and captions;
- equations, module names, and train/inference distinctions;
- paper version and later revisions;
- whether an apparent claim is author-stated, evidence-supported, or the user's interpretation.

When the work note conflicts with the paper, correct the formal archive and record the discrepancy or uncertainty. Do not silently preserve a known error.

## Handle legacy notes

Legacy notes may lack `producer`, `schema_version`, `paper_id`, or lifecycle fields.

1. Match by arXiv, DOI, Zotero key, canonical URL, or normalized title.
2. Inspect headings for evidence that the note is a work reading note rather than a formal archive.
3. Label the match as legacy in the working process.
4. Apply stronger primary-source verification.
5. Do not rewrite legacy frontmatter solely to satisfy intake unless the user authorizes that edit.

## Link both layers

Set the final archive frontmatter to:

```yaml
producer: paper-reading-intake
schema_version: 1
reading_provenance: paper-notes
source_note: "[[<work-note>]]"
```

When editing the workspace-local vault is permitted, add or update this field on the work note:

```yaml
archive_note: "[[<formal-literature-note>]]"
```

Do not move or delete the work note. In direct mode, set `reading_provenance: direct` and leave `source_note` empty.
