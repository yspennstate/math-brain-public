---
name: t013_two_ghost_limit_sqrt2_minus_1_round_rl_rectangle_not_self_dual_2026_11_03
description: [VERIFIED] T013 m013f (Codex m5f-T013b): two wired arcs give f/(f+sqrt2(1-f)), square q=2 limit sqrt2-1 not 0.5; L=128 sits +1.0 to +2.7 se above; W=round(rL) rectangle is not self-dual (q=1 8 se off), use W+1
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T02:45:41+04:00
  status: verified
  evidence: "codex_fleet/20261102/workers/m5f-T013b/REPORT.md; rows/T013 moves.jsonl 66b7ff00"
---

T013 (FK crossing, rectangle vs disk), Codex worker m5f-T013b, harvested by an agent as move m013f on
brain-repo 06_math_research/frontier/rows/T013 (moves.jsonl 66b7ff00; files t013b_REPORT.md, t013b_RESULTS.md,
t013b_combined.json, t013b_boundary_convention.md, fk_alt.c, t013b_formula_check.py/.json).

What it settled:
- The predecessor compared two independently wired FK arcs with the Chelkak-Smirnov open-interface loop probability.
  Those are different events. If CS print f, the two-ghost connection probability is f / (f + sqrt(2)(1 - f)), so the
  square (r = 1) limit at q = 2 is sqrt(2) - 1 = 0.41421, not 0.5. Source: Chelkak-Smirnov arXiv 0910.2045v2 Thm 6.1,
  Rem 6.2 (PDF p.43); weights confirmed by Feng-Peltola-Wu arXiv 2205.08800v3 Eq. 1.9-1.10, Thm 1.8.
- Swendsen-Wang q = 2, L = 128, two seeds x 20,000 sweeps: r 1/2 0.850475 +/- 0.003590 vs 0.840896 (+2.67 se);
  r 1 0.419375 +/- 0.005339 vs 0.414214 (+0.97 se); r 2 0.092825 +/- 0.002608 vs 0.086427 (+2.45 se). All three sit
  above the limit and rose from L = 64 to 128: consistent with approach, no controlled extrapolation, no theorem.
- Geometry scar: the inherited rectangle W = round(rL), H = L is not self-dual. Its q = 1 control gives
  0.508980 +/- 0.001121, 8.0 se off 0.5. W = round(rL) + 1 (rect_medial) gives 0.499975 +/- 0.001118 at L = 64 and passes.
  Any rectangle crossing run on this row must use the +1 width or carry the offset.
- Exact 4x4 enumeration (16.8M configurations) checks the sampler: q 1/2/3 = 0.630363, 0.570472, 0.538223; the
  million-sweep estimates are within 1.3 se.

Next: brief m5f-T013c (self-dual rect_medial q = 2 to L = 256 with extrapolation; rectangle vs disk at q 2/3) waits on
the Codex launcher's disk gate. Earlier history of the row: [[t013_fk_crossing_rect_vs_disk_q2_q3_fail_unmatched_scale_2026_11_02]].

