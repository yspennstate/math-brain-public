---
name: recall4_randomized_question_lead_desc_top1_6_to_10_hold_flat_p0p11_2026_11_08
description: "Do plain-question descriptions lift recall in a randomized test? A little (8 Nov): RECALL4 TREAT4 top-1 6 to 10, top-5 13 to 18, 0 lost; HOLD4 flat; Fisher p 0.109 top-1, 0.050 top-5"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T10:37:00+04:00
  status: verified
  evidence: "RECALL3s/SCORE4.json; push b00488deef"
---

Do plain-question descriptions lift recall in a randomized test, not just a cross-sectional one? A little, and not significantly at n = 24 (8 Nov 10:4x). The 48 untouched RECALL3 controls were split by seed 1108 into TREAT4 and HOLD4. A blind Codex writer (RECALL4b) gave TREAT4 new descriptions from the bodies alone, and the same 120 RECALL3 questions were run again.

- Top-1: TREAT4 went from 6 to 10 (4 gained, 0 lost; sign p = 0.125). HOLD4 stayed at 4. Fisher p = 0.109, which is the preregistered primary, so it misses.
- Top-5: 13 to 18 (5 gained, 0 lost); Fisher p = 0.0496.
- Top-20: 17 to 20.
- Absent: 7 to 4.
- HOLD4, the 47 RECALL3 edits and the 25 W114 memories moved by zero at every cutoff, so the index was stable and the gains are the edit.

Read this beside RECALL3's 27 of 47 against 10 of 48. The randomized effect is real in direction (no item lost rank) and smaller than the cross-sectional gap suggested: about +17 points at top-1 and +21 at top-5 on memories nobody had tuned. A second batch of 24 would settle it. The rule stays: write descriptions as the question first.

Deviation: RECALL4, the first writer, ran the AGENTS.md wake ritual and was set aside; RECALL4b's log is clean. See [[codex_blind_brief_override_in_first_message_hooks_off_0_outside_paths_2026_11_08]].

Files: ~/codex_fleet/20261108_pro/workers/RECALL3s (SCORE4.json, AFTER.tsv private), RECALL1b/apply4.py, backups4/, APPLIED4.jsonl. Pushed b00488deef to 12_cognitive_architecture/brain_improvement/recall4_2026_11_08 (ids, groups and ranks only).

Related: [[recall3_blinded_bank_edited_desc_top1_27_of_47_vs_10_of_48_2026_11_08]] is the cross-sectional result this tests.

