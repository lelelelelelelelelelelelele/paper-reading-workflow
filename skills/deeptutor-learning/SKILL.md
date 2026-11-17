---
name: deeptutor-learning
description: Use DeepTutor from Codex to study a course handout or paper, continue questions in the same DeepTutor session, and turn the discussion into a standalone Notebook note. Use for requests such as “用 DeepTutor 带我读”, “继续这节课”, “整理一下”, or “把刚才的订正改进同一篇笔记” in a DeepTutor learning conversation. Pass supported paper drafts and primary-source locations to paper-reading-intake when the user requests a formal archive.
---

# DeepTutor learning in Codex

Use the existing DeepTutor installation. Follow [CLI usage](references/cli.md) to resolve the runtime, workspace, session and Notebook. Keep the source, workspace and session IDs in the Codex conversation. When saving a note, also keep its Notebook ID, record ID and durable Markdown path. Reuse these values across turns. For a resumed task, read the matching DeepTutor session and Notebook before writing. Ask only if multiple plausible targets remain.

## Read and continue

- Resolve the actual file or canonical source URL and the page, section or figure requested. Give DeepTutor the relevant source content with page anchors. For a PDF or slide deck, inspect the original page or figure where extraction loses layout, values or formulas and describe the relevant visuals in the prompt. Keep the original source separate from any generated explanation.
- Start one DeepTutor chat for the material and give it a title that includes the source or topic. Send follow-up questions with the same workspace and session. Use the completed DeepTutor answer in Codex. Keep the actual sections discussed and the learner's confirmed progress distinct.
- Wait for a terminal event and a usable response. For a failed or interrupted turn, report the actual outcome and recover its session from the event log or workspace history before retrying. Resume in that session once the prior turn has stopped.

## Organize or revise

- Ask DeepTutor in the same session for Markdown with the helper's `--draft` option. Supply the useful source anchors and request the full note in its reply. Organize around the concepts, methods or tasks that matter. Preserve meaningful formulas, source figures or figure links, useful tables, assumptions, examples and limitations. Check that the result answers a practical question from the original material.
- For a correction, read back the existing note and give DeepTutor its text along with the correction and relevant evidence. Request a complete revision with the supported correction integrated wherever it changes the reasoning. Keep a clean note body and put the completion recap in chat.
- Save only after a complete usable response. Write the Markdown to a writable, durable learning location and check material links. Use the same Notebook and the original record ID on revision. Read back the saved record and confirm its body. If saving was interrupted, inspect the scoped Notebook or replay the same save with the same draft and IDs. Use the existing draft rather than generating another note for a save retry.

## Hand off a paper for formal archival

When the user asks to archive, give `paper-reading-intake` the readable draft path, the actual primary PDF or URL, the paper identity if known, the sections or figures covered, and the learner's explicitly confirmed progress. Include figure file paths or page anchors when relevant. Identify the draft as DeepTutor context and leave the intake skill to resolve the reading route. If the user has asked for direct archival, the draft can inform it as supplemental context. Verify evidence, obtain paper-native figures, and produce the formal Markdown and HTML through intake. A generated explanation or a saved Notebook record alone establishes no reading completion.
