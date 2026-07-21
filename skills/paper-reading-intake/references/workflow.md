# Workflow Reference

Read this reference for a full Obsidian intake, ambiguous classification, evidence-strength judgments, artifact placement, or cross-machine path handling.

## Contents

- [Data flow](#data-flow)
- [Output package](#output-package)
- [Reading and archive sequence](#reading-and-archive-sequence)
- [Recommended archive structure](#recommended-archive-structure)
- [Evidence-strength labels](#evidence-strength-labels)
- [Classification questions](#classification-questions)
- [Q&A writeback map](#qa-writeback-map)
- [Cross-machine portability](#cross-machine-portability)
- [Sync verification](#sync-verification)

## Data flow

```text
authoritative paper ───────────────┐
                                  v
workspace paper-notes ──> intake verification ──> canonical literature Markdown
          (optional)        ^                         │
                            │                         v
direct archive ─────────────┘                 self-contained HTML
```

Treat the authoritative paper as the technical fact source. Treat `paper-notes` as the source of corrected understanding, user insights, and critique. Generate the final HTML from the same conclusions and numbers as the canonical literature Markdown.

## Output package

Adapt logical roles to the vault's existing folders instead of forcing exact names:

| Artifact | Typical location | Persistence | Purpose |
|---|---|---|---|
| Work reading note | workspace-local Obsidian vault | durable upstream | Pre/companion/post reading trace owned by `paper-notes` |
| Literature Markdown | vault `20 Literature/<Paper>.md` | canonical | Editable formal archive and source of truth |
| HTML reference | vault `50 Outputs/HTML Format References/<slug>_REPORT.html` | canonical pair | Self-contained browser-readable report |
| Temporary draft/assets | task scratch directory | temporary | Extraction, conversion, and rendering inputs |
| Topic link | vault `10 Topics/...` | durable link | Mainline or side-branch placement |
| Literature index | vault literature index | durable link | Global discovery entry |

Do not retain a separate workspace `<slug>_REPORT.md` after the final literature Markdown is established. Do not keep a sibling `<slug>_figures/` directory beside the archived HTML. Avoid absolute image paths in archived HTML.

## Reading and archive sequence

1. Establish authoritative sources and a stable `paper_id`.
2. Locate and classify the matching `paper-notes` state using [notes-consumption.md](notes-consumption.md).
3. Resume incomplete active reading when required, or record a direct-archive decision.
4. Identify the paper type, changed layer, and research-line relationship.
5. Fetch authoritative text, figures, captions, code, and project links.
6. Extract corrected insights from the work note without copying raw self-test history.
7. Recheck exact numbers, captions, evidence strength, and version-sensitive claims against primary sources.
8. Write the canonical literature Markdown.
9. Produce a matching self-contained HTML report with base64 figures.
10. Patch useful follow-up corrections into the relevant sections of both artifacts.
11. Add the topic link, index entry, `source_note`, and allowed reciprocal link.
12. Render the HTML and verify applicable sync.

## Recommended archive structure

```markdown
---
type: paper-note
producer: paper-reading-intake
schema_version: 1
paper_id: "arxiv:YYMM.NNNNN"
status: read
reading_provenance: paper-notes
source_note: "[[<work-note>]]"
category: <mainline|side-branch|tech-report|method|benchmark>
topic: [<topic>]
source: <arxiv|publisher|project-page>
url: <authoritative-url>
read: YYYY-MM-DD
html: "<relative-html-path>"
---

# <Paper>: <one-line topic>

## 结论先说
State what the paper is, what it is not, and how it relates to the user's work.

## 图 1：<function>
Explain the setup, support, limits, and relevance. Keep the visual in the linked HTML.

### 机制辨析：X 是什么，不是什么
Write the corrected mechanism beside the evidence.

## 关键结果
Preserve exact metrics and comparison conditions after primary-source verification.

## Ablation / Evidence
Separate component evidence from probes, sanity checks, and qualitative examples.

## 和主线的关系
Classify direct competition, adjacent inspiration, or background value.

## 我的判断
Summarize strengths, risks, evidence gaps, and reuse value.
```

Set `reading_provenance: direct` and leave `source_note` empty when the workflow legitimately bypasses `paper-notes`.

## Evidence-strength labels

| Evidence | Supports | Does not automatically support |
|---|---|---|
| Independent benchmark | Relative task performance under the stated setup | General superiority outside that setup |
| Ablation | Contribution of a removed or changed component | Mechanistic explanation beyond the tested change |
| Representation probe | Whether information can be decoded from a representation | End-task causality or practical necessity |
| Internal sanity check | Whether an internal schema or target is learnable | External validity or fair comparison |
| Qualitative figure | Intuition and visible behavior | Reliable aggregate performance |
| Real-world demo | Feasibility on demonstrated tasks | Robustness without enough trials and controls |

Use precise language such as "supports", "is consistent with", or "suggests". Do not turn a preprint claim into an established fact.

## Classification questions

Answer all five before filing the note:

1. Is it mainline, a direct competitor, a side branch, background, or tooling?
2. Which layer does it change: data, representation, backbone, policy head, training, inference, RL, or system infrastructure?
3. Does it share the user's problem definition and evaluation target?
4. Can it contribute metrics, experimental design, terminology, or counterarguments?
5. Does it alter the current novelty judgment?

Prefer a compact comparison table when three or more approaches must be distinguished.

## Q&A writeback map

| User question or upstream content | Durable destination |
|---|---|
| Corrected mechanism answer | Corresponding mechanism or figure section |
| Exact experimental setup | Corresponding experiment or ablation |
| Dataset-rigor concern | Evidence caveat or limitation |
| Competitor relationship | Classification and project-relationship section |
| Raw blind answer or correction history | Keep only in the upstream work note |
| Unverified sharp insight | Keep upstream until verified or clearly label as interpretation |

Do not add a generic Q&A appendix unless the user explicitly requests a conversation log.

## Cross-machine portability

- Detect formal and workspace-local vault roots on every machine.
- Inspect project instructions and directories containing `.obsidian`; accept established names such as `notes/` or `obsidian/` instead of assuming one name.
- Keep repository files free of usernames, drive letters, credentials, and machine-specific remotes.
- Store machine-specific sync configuration outside the skill repository.
- Use relative links in final vault artifacts.
- Preserve Obsidian notes as the human-readable entry points and Git repositories as versioned skill sources.

## Sync verification

Choose the vault's existing sync mechanism. For rclone-style setups:

1. Verify the configured remote instead of trusting a remembered name.
2. Copy only the note and output directories in scope.
3. Run a directory-level check with narrow include patterns when appropriate.
4. Require a clean result such as `0 differences found` before claiming success.

Never commit sync credentials or local configuration to a skill repository.
