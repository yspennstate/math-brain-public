---
name: codex_blind_brief_override_in_first_message_hooks_off_0_outside_paths_2026_11_08
description: "How do I keep a Codex worker blind despite the AGENTS.md wake ritual? Brief line blind: yes (8 Nov): launcher sends the override as the first message, hooks off; 2 of 2 runs clean vs 0 of 3"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T10:37:17+04:00
  status: verified
  evidence: "launcher.py BLIND_PROMPT; BLINDT1 and RECALL4b audits"
---

How do I start a Codex worker that stays blind, given that its AGENTS.md runs the wake ritual? Put `blind: yes` on a line of the brief. Since 8 Nov 10:20 launcher.py then sends BLIND_PROMPT as the first message and runs Codex with `--disable hooks`. BLIND_PROMPT says the ritual does not apply, forbids reads outside the folder, says the log is audited, and names the first command exactly (cat ../../RULES.md ./BRIEF.md). The backup is launcher.py.pre_blind_20261108.

Why: RECALL2, RECALL3 and RECALL4 each had the override only inside BRIEF.md. Each ran the ritual in its first command (the compute-state read, and RECALL4's `rg --files .claude -g MEMORY.md -g '*startup*'`), because the model plans that call before it reads the brief.

Measured after the change, by RECALL1b/audit_recall3_log.py:
- BLINDT1 smoke task: 4 commands, 0 outside paths.
- RECALL4b, the real 24-description job: 10 commands; the only outside path is ../../RULES.md, and the forbidden-name hits are its own report text.

That is two of two clean runs against zero of three before. Ritual-free does not mean leak-free: the auditor still has to run on every blind log.

Related: [[codex_agents_md_wake_ritual_breaks_blinded_briefs_2026_11_08]] - the failure this fixes. [[recall4_randomized_question_lead_desc_top1_6_to_10_hold_flat_p0p11_2026_11_08]] - the first test run on it.

