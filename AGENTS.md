# Development and installation

This independent GitHub-backed repository is the producer. Edit, test and commit here; CC Switch, Codex and Claude skill directories are consumers. Never develop in installed directories or import whole consumer working trees as trusted baselines.

Preserve the paired workflow: paper-notes owns active reading, intake owns formal archives. Keep paper identity, truthful reading provenance, source_note/archive_note links, and incomplete-reading handoffs. PAPER-001 changes only intake; leave skills/paper-notes and intake/references/notes-consumption.md unchanged. Preserve self-contained HTML figures. Source-background checks and discussion synthesis belong in separate commits. Completion recaps belong in chat, not saved knowledge notes; templates remain optional and critique on demand.

The canonical record is .workblock/items/PAPER-001/WORKITEM.md. Records have an independent Git repository and are ignored by code Git; do not stage or commit them. Retired-producer and consumer records are not separate execution entries. Human-facing reports use matching Markdown and static HTML.

For accepted landed changes, synchronize the configured GitHub main branch before installation. Use project-installer with the local .workblock/actions/install.json registration. The script exports only skills/paper-reading-intake/{SKILL.md,agents/,assets/,references/}, preserves consumer Git, Block records, unrelated files and root links, and emits its receipt to stdout. PAPER-001 targets only intake; do not overwrite installed paper-notes. Temporary fixtures belong in .workblock/runtime/PAPER-001 and must be removed at closeout; permanent verification evidence belongs under the Item.
