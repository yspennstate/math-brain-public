---
name: c0034_lyons_orthogonal_union_coupling_open_rank_one_lyons_2003_codex_288_certs_2026_11_13
description: "C0034 (Lyons ICM 2014 arXiv 1406.2707, Question 2.8: for H = H_1 (+) H_2 orthogonal in l^2(E), is there a coupling of P_{H_1} and P_{H_2} whose union has law P_H?) is open on 13 Nov 2026; arXiv has nothing new. Known: dim H_1 = 1 is Lyons 2003 Lemma 10.4 / Prop 10.3 (also Moller-O'Reilly 1806.07347 Lemma 1), and complement duality settles every case with min(dim H_1, dim H_2, |E| - dim H) <= 1, so all |E| <= 5. First open rank triple (2,2,2) at |E| = 6. Codex C0034A (13 Nov, PARTIAL, unrefereed): explicit max-flow construction for rank one, 288 exact rational coupling certificates for |E| <= 7, and an exact 4-point Hadamard example where composing two valid couplings gives the wrong first marginal, so induction on dim H_1 does not work by composition"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T19:06:53.117Z
---

C0034, rank 60 on the 200 list. Source: Russell Lyons, "Determinantal probability: basic properties and conjectures",
ICM 2014, arXiv 1406.2707, Question 2.8, p.6 (right after the stochastic domination theorem 2.7). Given orthogonal closed
subspaces H_1, H_2 of l^2(E) with H = H_1 (+) H_2, is there a coupling of P_{H_1} and P_{H_2} whose union has law P_H?
For finite E the sizes force X_1 and X_2 to be disjoint, so the question is whether a three-marginal transportation
polytope is nonempty. Equivalently (complement duality) a random partition (X_1, X_2, X_3) of E with X_i ~ P_{H_i},
H_3 = H perp, which makes the question symmetric in the three spaces.

Status 13 Nov 2026: open.
- Known in print:
  - dim H_1 = 1: Lyons 2003 (Publ. IHES), Lemma 10.4, extended to infinite-dimensional nested spaces in Proposition 10.3.
    Moller and O'Reilly, arXiv 1806.07347, Lemma 1, restate the singleton-difference law for finite-rank kernels.
  - By complement duality, every case with min(dim H_1, dim H_2, |E| - dim H) <= 1. Lyons 2003 notes this covers all
    |E| <= 5. The first rank triple not covered is (2,2,2) at |E| = 6, then (2,2,3) at |E| = 7.
  - Coordinate-block sums: independent block couplings combine.
- Not answers, though they sound close: Lyons-Thom 1402.0969 (invariant monotone couplings on sofic groups), Kassel-Levy
  AIHPD 2022 Prop 5.15 (monotone coupling of determinantal linear processes), Pemantle-Peres 1108.0687 (stochastic
  covering), Bufetov-Qiu-Shamov JEMS 2021 (Lyons-Peres completeness), Poinas EJP 2026 (2406.03360, marked couplings by
  pointwise thinning), Decreusefond-Moroz (transport distances). Lyons' ICM errata of 30 Dec 2025 gives no resolution.
- My arXiv check on 13 Nov (determinantal with coupling and orthogonal; determinantal with union and coupling; "Question
  2.8" with Lyons; "projection determinantal" with coupling; strongly Rayleigh with coupling and union): nothing.
- Ours:
  - 7 Sep intake A001/A002: double-precision LP feasibility (HiGHS, zero violation) on 1360 random orthogonal pairs,
    |E| = 3..8, Fourier subspaces on cycles, K_4 star-space splits. Numerical only. Conditioning X_2 on X_1 fails.
  - R7-01 (17 Sep, open-problems-repo research7_2026-09-17): PARTIAL / source open.
  - Codex C0034A, referee_reports/2026-11-13/C0034A (13 Nov, gpt-6.1-sol, PARTIAL, unrefereed):
    - rank one by an explicit max-flow on the minors: weighted Hall from the interior product i_u (norm <= 1, i_u z = w),
      code/rank_one_flow.py in exact Fractions. A new proof of a known case, not a new result.
    - 288 exact rational certificates (286 distinct instances), every split p + q <= n for n = 2..7 on Cayley and Givens
      rational orthogonal matrices, plus the exceptional (2,2,2) and (2,2,3) triples. Evidence, not a proof.
    - Obstruction to induction: on the 4x4 Hadamard matrix, two valid successive couplings compose to a first colour with
      masses 1/2, 1/2 instead of the required four masses 1/4. Adding one vector at a time does not keep the marginal.
- Where an attempt could start: the (2,2,2) case at |E| = 6 is the smallest open shape. A proof there needs a Hall-type
  inequality for pairs of 2-vectors, not the rank-one interior-product bound; or an exact Farkas search on the
  Grassmannian Gr(2,6) x Gr(2,4) for a counterexample.

Related: [[c0033_lyons_determinantal_entropy_concavity_open_two_point_posted_codex_abc_partial_2026_11_13]] (same
survey, previous item in this loop); [[c0035_trig_determinantal_block_factor_open_m_ge_2_broman_m1_2026_11_13]] (same
survey).
