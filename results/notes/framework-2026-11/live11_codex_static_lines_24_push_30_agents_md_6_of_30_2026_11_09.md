---
name: live11_codex_static_lines_24_push_30_agents_md_6_of_30_2026_11_09
description: "Partly (LIVE11): Codex three standing rule lines 24/30, push 30, AGENTS.md alone 6; push beats standing text for Codex"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T11:01:21+04:00
  status: provisional
  evidence: "private-repo brain_improvement/LIVE11_20261109 1bfcb739e6"
---

Partly (LIVE11, 9 Nov 11:0x): Codex gpt-6.1-sol high, every arm with the account AGENTS.md, LIVE6's items and hidden checker, 135 runs. Traps of 30: G (AGENTS.md only) 6, GS (plus LIVE10's three rule lines as developer_instructions) 24, GP (plus push v2 on the request) 30. GS vs G 18/0, p 7.6e-6 (rule 1 met). GS vs GP 0/6, p 0.031: rule 2 (within 3) NOT met. Controls 15/15 all.

Per task G/GS/GP: TYPO_MAP 5/5/5, TYPO_GUESS 1/2/5, MESH_A 0/2/5, MESH_B 0/5/5, MODEL_A 0/5/5, MODEL_B 0/5/5.

The difference from Claude: the same three lines took Claude to 30/30 ([[live10_claude_static_rule_lines_30_push_29_claude_md_alone_10_of_30_2026_11_09]]); Codex slips on the dictionary-guess typo (kept experimnet_results 3 of 5; the rule's keep-a-name clause seems to license it, while the push names the likely real word for this request) and on MESH_A (3 of 5 wrote the counter with no claim). For Codex the push beats standing text when the trigger is in the request. LIVE13 (Codex, trigger at step 03, where a request push cannot fire) decides whether Codex needs a tool-read hook.

Self-run claims on mesh traps: GS 9/10, GP 6/10, G 0/10 ([[live9_codex_agents_md_fixes_typos_6_of_10_never_claims_mesh_0_of_10_2026_11_09]]: AGENTS.md alone never claims).

Packaging scar: a GS run made its own .agent_mesh/agent_mesh.sqlite3 in the workspace; the secret scanner refuses NUL-heavy files, so redact_l6x.py now drops .agent_mesh as well as .mesh. And an outer pipeline without pipefail let the push script start after the pack failed; it aborted on the missing tar, nothing landed.

Evidence: private-repo 12_cognitive_architecture/brain_improvement/LIVE11_20261109 (PREREG 75697430f5, results 1bfcb739e6, 9 files read back). No brain arm. Leak check 10 memories, 3,736 shingles, none.

