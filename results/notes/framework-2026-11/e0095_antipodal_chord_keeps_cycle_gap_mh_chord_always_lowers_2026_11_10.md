---
name: e0095_antipodal_chord_keeps_cycle_gap_mh_chord_always_lowers_2026_11_10
description: "E0095 Diaconis graph augmentation (OPEN2 Codex, 10 Nov): one chord on even cycle - antipodal keeps gap 1-cos(2pi/n) at any weight, others strictly lower; MH-restored uniform: every chord lowers; matchings open; full math store recall OOMs at 900 MiB"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T03:49:27+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-10T18:40:48.136Z
---

The OPEN2 Codex worker (launched 10 Nov 03:27 laptop, brief codex_local_1108/briefs/OPEN2, gpt-6.1-sol high, normal speed) chose E0095, Diaconis's graph-augmentation problem, not Lyons' conjecture as its first log line suggested. Result is partial: the general problem (best perfect matching, or best stationary-preserving kernel) is not solved.

Proved on paper, with two exact computation paths (Fraction polynomials, n = 4..16 even, weights 1/2, 1, 5) and a float sweep (n to 40, weights 0.01 to 1000):
1. On an even cycle C_n with one added chord of any positive weight, ordinary weighted random walk: the antipodal chord keeps the spectral gap exactly at the cycle's 1 - cos(2 pi/n); every other chord gives a strictly smaller gap. This closes the equality the September E0095 memo had only numerically.
2. If the chord is added and Metropolis-Hastings restores the uniform law, every single chord strictly lowers the gap.
Controls: C6 with a unit antipodal chord gives ordinary gap 1/2, half-lazy 1/4, uniform-target MH 1/3. A whole antipodal matching on C8 gives 2/3 at weight 1 and 1/6 at weight 10, against 1 - sqrt(2)/2 before. So the one-chord result does not extend to matchings.

Checked independently by an agent on 10 Nov (numpy, symmetric normalisation D^-1/2 W D^-1/2): n = 8, 10, 14 at weights 0.5 and 5. The antipodal gap equals 1 - cos(2 pi/n) to 6 places and the distance-2 and distance n/2-1 chords are lower.

Recall lesson: the full math_recall store raised MemoryError under the worker's 900 MiB cap after 208 s. A bounded SQL subset (13 seed cards plus neighbours, 24 cards and 36 links, 40 s) worked. Full-store recall costs more than 900 MiB, which bears on the recall-10x work.

Next, per the report: which chord loses least under MH, and optimising a whole matching. Before any publication claim it needs an external proof review and a fuller priority search. Files: briefs/OPEN2/REPORT.md, SOLUTION.md, evidence/ (PROOF_REVIEW.md, SEARCH.md, exact_matrix.json).


Independent audit 10 Nov ~20:2x by an agent (briefs/OPEN2/audit_agent/AUDIT.md): both claims hold on all 1,520 cases (even n 4..40, every chord distance, weights 0.01..1000); claim 2 (MH: every chord lowers) had not been checked before; smallest MH drop 3.7e-7 at w=0.01, 1.9e-5 for w>=0.5. Numerical support, not a proof review.

Proof review 10 Nov ~20:4x by an agent (briefs/OPEN2/audit_agent/PROOF_REFEREE_2026_11_10.md): both proofs in SOLUTION.md are correct line by line (half-rotation split; the even sector has slack 2, so the gap is set by the odd sector, whose extremal function sin(pi i/m) is zero at both chord ends; the MH edge weights 1/2, 1/(2+w), w/(2+w) and the trig sum 4[a^2cos^2 al + sin^2 th sin^2 al] were re-derived by hand). The explicit bounds themselves (not only the strict inequalities) were checked on 5,220 cases, n=4..60, w=0.01..1e4: ALL PASS. Still owed before posting: a priority search for the normalized one-chord equality.
- Lean (an agent, 10 Nov 22:1x): edge_sum identity and chord_energy bound compile rc=0, axioms propext/Classical.choice/Quot.sound only; OPEN2/audit_agent/E0095_MHIdentity.lean (fcb620e97eb6). The gap statement itself is not formalized.
