# Workflow Reference

Read this reference for a full Obsidian intake, ambiguous classification, evidence-strength judgments, artifact placement, or cross-machine path handling.

## Contents

- [Data flow](#data-flow)
- [Output package](#output-package)
- [Source-background metadata](#source-background-metadata)
- [Reading and archive sequence](#reading-and-archive-sequence)
- [Recommended archive structure](#recommended-archive-structure)
- [Evidence-strength labels](#evidence-strength-labels)
- [Classification questions](#classification-questions)
- [Locate the affected knowledge](#locate-the-affected-knowledge)
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

## Source-background metadata

Keep this information available without interrupting reading: use a default-collapsed Obsidian `> [!info]- Metadata` callout and an HTML `<details>` block without `open`. Do not change global vault settings. Optional frontmatter fields are `publication_status`, `publication_year`, `metadata_checked`, `source_screening` and `source_flags`; they describe sources, not reading completion.

- Verify the paper's publication status (preprint / accepted / published / unverified), version, venue identity (main conference / workshop / journal), authors and affiliations. An arXiv DOI alone is not proof of peer-reviewed publication.
- Summarize venue standing and relevant author/team track records with sources, not prestige scores. Identify confirmed editorial, identity or research-integrity concerns specifically. Unknown authors, limited track records, fees or absence from a ranking alone do not establish a poor venue or paper. Prestige does not validate the paper's experiments.
- Check selected load-bearing citations and the actual empirical baselines, not every reference. Use columns: object, role in this paper, cited version/status at the time, currently verified publication status, consequence for interpretation, source link. Keep historical and current status separate.
- Distinguish a preprint used as an algorithm reference from a preprint carrying an essential empirical or theoretical claim. Surface the dependency and any concrete uncertainty; preprint status alone is not a methodological defect or proof of an unfair baseline.
- Record checked date, scope and unresolved items. `source_screening: checked-selected` covers only the explicitly listed scope; use `partial` when that scope is unfinished. Preserve uncertainty during intake instead of silently upgrading it. A consequential confirmed concern may warrant one visible sentence while the details stay folded.

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
10. Synthesize the relevant multi-turn discussion into the note, rewriting affected explanations and their consequences in Markdown and HTML; follow [the synthesis rules](../SKILL.md#7-synthesize-discussion-into-reusable-knowledge).
11. Add the topic link, index entry, `source_note`, and allowed reciprocal link.
12. Render the HTML and verify applicable sync.

## Recommended archive structure

The outline below is one paper-note example. Choose headings and their order from the actual knowledge and intended use; omit, combine, rename, or rearrange sections as needed. Do not require every discussion note to cover the whole paper. Personal or critical evaluation is optional and on demand; retain established evidence limits without adding a review to fill a heading. Preserve the existing source metadata and the self-contained HTML visual surface when applicable.

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

### <A clarification needed by this mechanism>
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

## Locate the affected knowledge

These examples help find the material affected by a discussion. They do not prescribe the final headings, one section per question, or a fixed note structure. Apply the synthesis rules in SKILL.md to combine related explanations and propagate supported corrections through their consequences.

| User question or upstream content | Durable destination |
|---|---|
| Corrected mechanism answer | Corresponding mechanism or figure section |
| Exact experimental setup | Corresponding experiment or ablation |
| Dataset-rigor concern | Evidence caveat or limitation |
| Competitor relationship | Classification and project-relationship section |
| Raw blind answer or correction history | Keep only in the upstream work note |
| Unverified sharp insight | Keep upstream until verified or clearly label as interpretation |

Keep discussion chronology and update summaries out of the saved knowledge note. A completion recap belongs in the chat reply. A conversation log, when explicitly requested, is a different output from the synthesized note.

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
