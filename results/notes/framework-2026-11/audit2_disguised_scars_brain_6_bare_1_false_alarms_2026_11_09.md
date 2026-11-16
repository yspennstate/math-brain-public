---
name: audit2_disguised_scars_brain_6_bare_1_false_alarms_2026_11_09
description: "Does the brain help catch a bug that undoes a recorded fix and reads like a tidy edit? Partly (AUDIT2): fixed 6 vs 1 of 12 (p 0.0625) but 6 vs 3 clean false alarms; frozen primary score -1.00 vs -0.92"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:56:28+04:00
  status: verified
  evidence: "the private repository, 12_cognitive_architecture/brain_improvement/audit2_scar_disguised_2026_11_09 (00dd7e8580)"
---

Mixed (AUDIT2, Codex gpt-6.1-sol high, 9 Nov). On 12 disguised SCAR plants, each undoing a recorded fix and reading like a tidy edit, BRAIN found and fixed 6 and BARE 1. Paired: 5 brain-only, 0 bare-only, 1 both, 6 neither; sign test p = 0.0625 two-sided. BRAIN also flagged 6 of 12 CLEAN originals, against BARE's 3. On DECOY (safe tidy edits) the false alarms were 0 against 1. The pre-registered primary score, (fixed - 3 x false alarms)/12, came out BRAIN -1.00, BARE -0.92, so no win under the frozen rule. Balanced group accuracy was 0.67 against 0.58. The deleted-memory control showed no advantage, as intended.

BRAIN called the brain in 36 of 36 reviews (20 of 36 in AUDIT1). All 5 brain-only fixes and all 6 of its false alarms came in reviews that called it. Median per review: 5 commands and 70.6 s, against BARE's 2 commands and 41.8 s. The calibration worked: BARE fixed 1 of 12 here, against 8 of 12 on AUDIT1's visible plants.

Reading: the brain supplies the recorded fix, but it also makes the reviewer suspicious of clean code. The next arm needs the same evidence bar for "broken" as BARE (cite the memory AND show the failing line), and the next bank needs more pairs (12 per group is a pilot).

Interrupted at 53/72 by live-sidecar drift. Resumed under amendment 01 ([[freezing_live_sidecar_digest_stops_long_brain_tests_audit2_2026_11_09]]). On the 26 items finished before the drift: 4 to 0 and false alarms 5 to 3, the same direction.

Graph brain-graph-full-2026-11-07, 376,111 nodes and 16,811,666 edges; sidecar 243,298 links at the freeze. The easier predecessor: [[audit1_script_audit_brain_ties_bare_2026_11_09]].

