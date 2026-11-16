---
name: t014_d7_percolation_tail_exponent_0p496_mean_field_2026_11_02
description: T014 bond percolation at p_c, d 3-7, BFS on infinite lattice: tail exponent of P(|C|>=s) d7 0.496 +- 0.002 (mean field 1/2), d6 0.476 with log-correction creep, d3 0.190; PREREG93 4/4; evidence not proof
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:58:01+04:00
  status: provisional
  evidence: "rows/T014/moves.jsonl 9c934759"
---

T014 (mean-field bond percolation, proved d >= 11, open for d 7-10), first frontier move, 2 Nov 2026, an agent. m014a is in rows/T014/moves.jsonl (9c934759); the code is t014_perc.c and t014_tail.py in 06_math_research/frontier/rows/T014.

- Setup: BFS clusters on the infinite lattice at literature p_c, d 3-7, 4e6 clusters each, capped at 65,536 sites.
- The tail exponent of P(|C| >= s) over s 1024-65536 is d3 0.190, d4 0.315, d5 0.417, d6 0.476 and d7 0.496 +- 0.002. Mean field gives 1/2.
- At d7, sqrt(s) P is flat at 1.03 over the last four doublings.
- At d6 (the upper critical dimension) the local exponent creeps 0.469 -> 0.479, which fits log corrections.
- PREREG93 4/4. This is numerical evidence for mean field at d7, not a proof, and it rests on p_c values that were not re-measured.
- Harness note: push_row.sh died on a gh PUT error after all six blobs had landed identical. Checking each blob with git hash-object against origin, then running append.py alone under the row claim, recovered the move without re-uploading.
- Related: [[t024_sl2_cayley_cutoff_window_flat_76_tmix_7logn_2026_11_02]].

