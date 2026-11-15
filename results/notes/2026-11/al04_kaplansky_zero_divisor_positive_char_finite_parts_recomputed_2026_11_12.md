---
name: al04_kaplansky_zero_divisor_positive_char_finite_parts_recomputed_2026_11_12
description: "Kaplansky zero-divisor conjecture: is positive characteristic settled? Three preprints say false (OpenAI p=2, Ivanov odd p, Mghirbi-Douglas with Lean); Ivanov's finite arithmetic recomputed and holds; char 0 open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T00:55:36+02:00
  status: provisional
  evidence: "al04_check.out, commit 6f7e751ec4bd; geometric part and Lean build not checked"
---

Row AL04 (Kaplansky's zero-divisor conjecture), 12 Nov 2026.

Positive characteristic is reported disproved by three preprints: OpenAI (p = 2, GitHub preprint of 23 Sep 2026, not on arXiv, not read here), Ivanov arXiv 2610.17662 (every odd p), Mghirbi and Douglas arXiv 2611.04599 (torsion-free hyperbolic groups, all four Kaplansky conjectures, existence for every prime formalized in Lean 4 per their Appendix C; their zero-divisor Section 6 is not formalized apart from Lemma 6.1). All are probabilistic existence proofs: no explicit group or elements.

Recomputed here from Ivanov's definitions (al04_check.py, 5 s): the Perron test vector inequality of Proposition 5.3 exactly for the 167 odd primes below 1000 and q = p^3, p^4, p^5; PG(2,27), letter frequencies, cross-intersections 1, 4, 28, 31, turn weights 1/28, 28/757, 1, exact lumping of the 760 x 760 matrix to the 3 x 3 one, spectral radius 0.976461; Table 2; the signed cancellation of Lemma 2.2 on random instances at p = q = 3 (every step-graph component has signed count divisible by 3), with two controls that fail as they should (non-bipartite first graph; one extra letter instead of three).

Not checked: the geometric part (torsion-free, aspherical, root separation), which rests on the OpenAI preprint's Sections 3 to 5. The Lean development was not built.

What stays open: characteristic zero. A counterexample over Q would contradict the strong Atiyah conjecture for the group; the mechanism needs constant cross-intersections over Z, and the line-line matrix qI + J has rank one only modulo p.

Method note: when a reported disproof is a probabilistic existence proof there is no finite certificate of the theorem to check; what can be checked in minutes is the paper's own finite arithmetic (design, certificate vector, appendix computations) plus controls showing each hypothesis is needed. Say plainly that this is not a check of the theorem.

Files: 06_math_research/al04_kaplansky_agent_2026_11_12/ (AL04_CHECK.md, al04_check.py, al04_check.out), commit 6f7e751ec4bd. Related: [[an09_fuglede_dim2_finite_sets_in_z60xz12_check_out_2026_11_12]], [[t283_polytime_low_degree_conjecture_refuted_small_noise_only_2026_11_12]].

