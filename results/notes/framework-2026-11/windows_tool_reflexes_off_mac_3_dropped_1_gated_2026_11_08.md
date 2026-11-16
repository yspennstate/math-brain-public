---
name: windows_tool_reflexes_off_mac_3_dropped_1_gated_2026_11_08
description: "[VERIFIED] 8 Nov: grep_for_a_cr_byte, ps_w_hides, ssh_backslash now dropped at load off Windows (24 Mac fires, 0 on-domain); windowless_parent ship-gated (18, gate keeps 0); process_presence left for Mac judgments"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:07:48+04:00
  status: verified
  evidence: "mac_fire_sample.py and mac_platform_gate_replay.py output 8 Nov over instinct_fires.tsv since 1 Nov; live probe 1794110823 in instinct_suppressed.tsv (platform); instinct_prime._load() 364 ids"
---

Do the Windows-tool reflexes still fire on the second machine? Not since 8 Nov 08:1x for four of the five that [[mac_reflex_guts_named_windows_paths_mac_line_past_clip_fixed_2_2026_11_08]] left unguarded.

Measured on the second machine's fires 1-8 Nov (mac_fire_sample.py prints each reflex's gut beside its fires; mac_platform_gate_replay.py runs them through instinct_prime's ship gate):
- grep_for_a_cr_byte_is_not_a_line_ending_test: 12 fires, 0 on-domain. The bug is Git Bash's grep; the second machine's grep counts a CR byte correctly.
- ps_w_hides_the_command_line: 5 fires, 0 on-domain. Git Bash ps -W; the second machine's ps -axww shows the full command line.
- ssh_backslash_escape_eater: 7 fires, 0 on-domain. None of the 7 was an ssh command; the trigger found "ssh" somewhere in up to 3,000 characters of text.
These three now sit in WINDOWS_ONLY beside heavy_compute_remote, so they are dropped at load off Windows.
- windowless_parent_pops_its_children: 18 fires; the ship gate keeps 0. It joined _SHIP_GATED rather than WINDOWS_ONLY, because code written here into brain-framework launches children on Windows too. At most 1 fire was arguably on-domain (a relative-path sed on wt-parity's creationflags, which the gate cannot see either way).

The ship gate's path pattern does not count wt-parity (a brain-framework worktree) as shipped code. Adding it would have kept 2 more windowless fires (edits to wt-parity/bootstrap/install.py), and neither was about a launch. Not changed.

Live check: a probe command matching both triggers produced no fire. instinct_suppressed.tsv logged windowless_parent as 'platform', and ps_w left no row because it is no longer loaded. 364 reflexes load; the process_presence_is_not_life control still loads. Backup: instinct_prime.py.before_20261108_platform. Only the second machine's live copy changed; the brain-framework copy already differed before this edit and is untouched. The change is harmless on Windows, since both lists only act when os.name != 'nt'.

Left on purpose: process_presence_is_not_life (131 Mac fires). Its lesson, that a listed process is not proof of a live one, may hold here, so it needs Mac judgments before any gate.

