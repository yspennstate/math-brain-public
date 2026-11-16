---
name: live10_claude_static_rule_lines_30_push_29_claude_md_alone_10_of_30_2026_11_09
description: "Yes (LIVE10): three always-on rule lines take Claude to 30/30 traps, push 29, CLAUDE.md alone 10; equal when the trigger is in the request"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T10:38:19+04:00
  status: provisional
  evidence: "private-repo brain_improvement/LIVE10_20261109 9029205275"
---

Yes, all three rules met (LIVE10, 9 Nov 10:4x): headless Claude Opus 5.5 high, every arm with the global CLAUDE.md, LIVE6's items and hidden checker, 5 reps, 135 runs. Traps of 30: M (CLAUDE.md only) 10, S (plus three always-on rule lines, push v2's texts, via --append-system-prompt) 30, P (plus push v2 on the request) 29. S vs M 20/0, p 1.9e-6. S vs P 1/0. Controls 15/15 every arm. Cost flat (about $6.7 per 45 runs each arm).

Per task M/S/P: TYPO_MAP 5/5/5, TYPO_GUESS 5/5/5, MESH_A 0/5/5, MESH_B 0/5/5, MODEL_A 0/5/4 (P's miss left out the effort), MODEL_B 0/5/5.

So for triggers that sit in the request, three standing lines do what the push does, and CLAUDE.md as it stands misses the mesh and Codex rules every time ([[live8_claude_md_alone_5_vs_3_of_15_self_claims_6_of_10_scripts_0_2026_11_09]]). For Codex, AGENTS.md as it stands fixes only the typos ([[live9_codex_agents_md_fixes_typos_6_of_10_never_claims_mesh_0_of_10_2026_11_09]]); LIVE11 runs the same three arms on Codex.

Side effect: the rule arms ran a mesh claim themselves in 10/10 mesh-trap runs (M 6/10), and in 4 to 5 of 15 controls, mostly writing status.md, which others only read. That over-claiming is cheap and changes no score.

What it does not settle: a trigger met partway through a task, in a file read later. A request-time push sees nothing there (push v2 prints 0 chars on LIVE12's requests and fires on every step-03 file); standing text is still on. LIVE12 tests it. Owner decision this feeds: adding the three lines to CLAUDE.md/AGENTS.md versus wiring house_rules_hook ([[live6_claude_house_rules_push_25_pull_13_bare_7_of_30_2026_11_09]], [[live5_push_v2_traps_30_of_30_controls_15_of_15_2026_11_09]]).

Evidence: private-repo 12_cognitive_architecture/brain_improvement/LIVE10_20261109 (PREREG cf951ca475, results 9029205275, 9 files read back). No brain arm: rule text only. Leak check 8 memories, 3,117 shingles, no hits. Short tasks (median 24 s): a rule-compliance test, not a memory test.

