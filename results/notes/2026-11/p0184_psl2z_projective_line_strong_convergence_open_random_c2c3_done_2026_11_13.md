---
name: p0184_psl2z_projective_line_strong_convergence_open_random_c2c3_done_2026_11_13
description: "P0184 (van Handel strong-convergence survey arXiv 2507.00346 Sec 6.4: does the deterministic PSL_2(Z) action on P^1(F_q), on constants-orthogonal vectors, converge strongly to the regular representation?) is open on 13 Nov 2026. Weak convergence is elementary (a nonscalar word fixes at most two points of P^1(F_q); our 6 Sep pass P0184-A001). The RANDOM analogue is now done: Barbieri-Jezernik arXiv 2602.11905 (Feb 2026) prove strong convergence of uniformly random homomorphisms from free products of finite groups, C2*C3 = PSL_2(Z) included, by a fractional-power polynomial method. The source says the random model is a different question, so it does not settle P0184"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T16:45:27.537Z
---

P0184, rank 43 on the 200 list. Source: van Handel, "The strong convergence phenomenon" (2025 survey), arXiv
2507.00346, Section 6.4, p.67. PSL_2(Z) acts on the projective line P^1(F_q). On the vectors orthogonal to the
constants, does this permutation action converge strongly to the left regular representation, that is, do the norms
of every fixed polynomial in the generators with matrix coefficients converge to their regular-representation values?
The survey's diffusion-operator and polynomial forms are equivalent and counted once.

Status 13 Nov 2026: open.
- Weak convergence (traces) is elementary and recorded in our 6 Sep pass P0184-A001 (codex_20h). A nonscalar
  X = (a b; c d) fixes the roots of c z^2 + (d - a) z - b = 0 on P^1(F_q), at most two points except for the finitely
  many primes where X reduces to a scalar. So the normalized trace on the q-dimensional constants-orthogonal space is
  (fix(X) - 1)/q -> 0. The open part is the norm upper bound, where sparse exceptional eigenvalues are the obstruction.
- Random analogue, now proved by an outside group: Barbieri and Jezernik, "Strong convergence of random representations
  of free products of finite groups", arXiv 2602.11905 (12 Feb 2026). They extend the polynomial method of
  Chen-Garza-Vargas-Tropp-van Handel and Magee-Puder-van Handel to groups with torsion, where the trace expansions run in
  fractional powers of N. Uniformly random homomorphisms from G_1 * ... * G_m into Sym(N) converge strongly, and
  PSL_2(Z) = C2*C3 is such a group. The source's caveat says random homomorphisms from C2*C3 are a different model. The
  deterministic arithmetic action on P^1(F_q) has no randomness for the method to average over.
- Also nearby: Gao, Kunnawalkam Elayavalli, Manzoor and Patchell, arXiv 2603.24502 (Mar 2026, v5), new purely finite
  field (PFF) groups. PFF asks for SOME sequence of finite-image homomorphisms that converges strongly. That is weaker
  than strong convergence of this particular congruence sequence.
- My arXiv check on 13 Nov: strong convergence with projective line, modular group, arithmetic, PSL, finite field, and
  with congruence, Schreier or deterministic. Nothing addresses the P^1(F_q) family. My reading, not checked against
  the survey's text: a positive answer would make the
  (2,3)-generated Schreier graphs of PSL_2(Z) on P^1(F_p) asymptotically optimal expanders in the free-product sense,
  a Ramanujan-type statement well beyond the Selberg-type spectral gap. That is a measure of how hard it is.
- There is no Codex report for P0184 in referee_reports/2026-11-13.
- Earlier brain-vs-no-brain test OP16 (06_math_research/op16_strong_2026_10_12/OP16_PARTIAL_RESULT.md, 12 Oct): both arms
  graded PARTIAL on P0184, one referee put the brain arm ahead; coarse grades, a direction only.

Related: [[d0082_meander_walk_conjecture_superseded_bgs_meandric_permuton_open_2026_11_13]] (previous item in this loop).
