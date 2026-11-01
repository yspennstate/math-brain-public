# Audit record: "Quadratic forms with nine large eigenvalues have bounded densities"

Source: `paper.tex` (15 pages), 24 September 2026. The hashes of the audited files are in `MANIFEST.txt`.

Result of the audit: every statement was re-derived from its hypotheses; no false statement and no gap was found
in the final text. Every numerical constant, every elementary inequality, the entropy inequality (Lemma 4.2), the
finite algebraic and combinatorial steps, the integral identities and the antiderivatives behind Lemmas 5.5 and 5.6
are proved in Lean 4 with Mathlib: 54 theorems in five files, each depending only on the axioms propext,
Classical.choice and Quot.sound. The analytic statements (Fourier inversion, the Brascamp-Lieb inequality, Theorem
4.1) are proved in the paper and tested numerically; they are not formalized.

Three kinds of evidence are attached to each statement below.

- Proof: the argument was reconstructed line by line from the hypotheses of the statement, and every invocation of
  an earlier statement was checked against that statement's exact hypotheses.
- Numerics: `checks/verify.py` (fixed seed 20260924). Constants in 50-digit arithmetic; integrals by adaptive
  quadrature; linear algebra on random and adversarial matrices; exact enumeration for the minor-sampling lemmas;
  Monte Carlo for densities, half potentials and characteristic functions, with explicit error allowances. The
  end-to-end test of Theorem 1.1 is `checks/t1_tight.py` and the example of Remark 8.3 is `checks/remark83.py`.
  Numerics are evidence, not proof; in particular the end-to-end test only shows that nothing is badly wrong, since
  the constant 400 is far from sharp.
- Lean: `lean/QformNine.lean` ... `lean/QformNine5.lean`, compiled with Lean 4.29.1 (leanprover/lean4:v4.29.1)
  against Mathlib commit 5e932f97dd25535344f80f9dd8da3aab83df0fe6; the `#print axioms` output of every theorem is in
  `lean/axioms_*.log`. A Lean theorem certifies the formal statement
  written there; the correspondence with the sentence of the paper was checked by reading both.

## Parameters

eta = 3/40 (diagonal pivots), zeta = 1/400 (pairs), kappa = 4/625 = (2/25)^2. Without a pivot, a_ij^2 <
eta^2 + zeta = 13/1600 < 1/121. The four cases of the proof of Theorem 1.1 give, at K = s = 1: no pivot
25 C_3 = 370.5; a diagonal pivot sqrt(40/3) * 82 = 299.4; a definite pair 20 pi = 62.8; an indefinite pair
20(6 + log 16 + L_0) + 1/e = 333.6 (below 337 with L_0 < 8). Every case is below 375, and the theorem states 400.

## Statement by statement

| Paper | Content | Proof | Numerics | Lean |
|---|---|---|---|---|
| Thm 1.1 | s_9(A) >= s gives density <= 400 K^2/s | assembled in Sec. 7 (four exhaustive cases), scaling checked | `checks/t1_tight.py`: 24 instances (diagonal, signed, paired, rotated, one heavy row, rank-9 factored with n = 200), every coordinate uniform so that K = 1, 2*10^6 samples each; largest density x s_9 = 1.84 | `main_constants`, `pivot_scales`, `log_le_two_div_e_mul_sqrt`, `log_div_sqrt_at_e_sq`, `logp_mul_le`, `logp_sixteen_sqrt` |
| Lem 2.1 | Plancherel, inversion, Gaussian identity | (a),(b) standard; (c) re-derived | I4 | - |
| Lem 2.2 | density from a power envelope | re-derived | - | `envelope_integral`, `envelope_tail` |
| Lem 2.3 | negative half moment via Fourier | re-derived (Gamma representation, substitution) | I1, I3 | `gamma_rep`, `halfmoment_constant`, `halfmoment_core`, `halfmoment_tail`, `halfmoment_total` |
| Lem 2.4 | domination by conditional densities | re-derived (Tonelli) | - | - |
| Lem 2.5 | Weyl and rank inequalities for singular values | standard (Eckart-Young-Mirsky) | L1 | - |
| Lem 2.6 | N_S(t) >= N_A(t) - k for Schur complements | re-derived (interlacing for the inverse; limit for singular A) | L2 (incl. singular) | - |
| Lem 2.7 | strict diagonal dominance gives invertibility | standard | L3 | used in `prop_volume_core` (Mathlib: `det_ne_zero_of_sum_row_lt_diag`) |
| Lem 2.8 | Cauchy-Binet; Gram factorization | re-derived | L4 | `gram_factor` |
| Thm 3.1 | geometric Brascamp-Lieb | re-derived (heat flow; the three limits) | B1 | - |
| Lem 3.2 | projections of product densities <= e^{d/2} | re-derived | B2, B3 | `mul_log_inv_le` |
| Lem 3.3 | integrated Fourier powers | re-derived | B4 | `fpower_floor` |
| Thm 4.1 | Fourier decay from the crossing volume | re-derived (promotion of heavy rows, Lemma 4.3) | D1, D2 | `omega_step` (monotonicity) |
| Lem 4.2 | entropy inequality | re-derived (Jensen, e_m <= (sum)^m/m!) | E1 | `entropy_lemma`, `factorial_mul_esymm_le` |
| Lem 4.3 | the bound with a hub | re-derived step by step (Plancherel, smoothing limit, Hoelder, joint projection) | D1, D2 | - |
| Cor 4.4 | density / half moment / decay constants | re-derived | C | `C3_lt`, `C2_lt` |
| Lem 5.1 | square profile | re-derived | P1 | `sqrt_add_sub_le` |
| Lem 5.2 | definite pair | re-derived (Jacobian) | P2 | - |
| Lem 5.3 | hyperbolic pair | re-derived (branches, tails, AM-GM) | P3 | `recip_sum_ge`, `hyperbola_cutoff`, `hyperbola_constants` |
| Lem 5.4 | concentration and logarithmic moment | re-derived | P4, P5, I2 | `concentration_constant_lt`, `L0_lt` |
| Lem 5.5 | J(d) <= pi + 4 log 2 + 2 log+(1/d); log kernel <= 8 | re-derived (exact formula for d <= 1 from three antiderivatives; monotonicity for d > 1; rearrangement) | I5, I6, I7 (exact formula against quadrature, relative error below 10^-8) | `antideriv_left`, `antideriv_right`, `kernel_product_le`, `kernel_log_bound`, `kernel_at_one`, `int_inv_sqrt` |
| Lem 5.6 | two coordinates: sup_a E\|q(W)-a\|^{-1/2} <= 16 D^{-1/4} | re-derived (bounded-density half potential (5.6); Lemma 5.3 rescaled; split at delta = 1/64; rearrangement) | P6 | `bounded_half_value`, `definite_pair_half`, `pair_half_constants`, `pair_antideriv` |
| (6.2) | entries without a pivot: \|a_ii\| < 3/40, \|a_ij\| < 1/11 | re-derived | - | `small_entry_bound` |
| Lem 6.2 | volume-sampled interpolation | re-derived; equality holds generically | M1 | `bordered_det` |
| Lem 6.3 | completion, rank 3r, restricted rank r | re-derived | M2 | `rank_three_r` (with `mrank_add_le`, `rank_indicator_le`) |
| Prop 6.4 | 4k-3 eigenvalues give V_k >= kappa^k, kappa = 4/625 | re-derived (dominance margin 137/200 against 2/3) | V1 | `telescoping`, `prop_volume_r0`, `prop_volume_margins`, `prop_volume_core`, `sqrt_kappa` |
| Lem 6.5 | random partition | re-derived | M3 (exact, all partitions) | `cut_count` |
| Prop 7.1 | no pivot: density < 375, half moment < 61 | re-derived | - | `volume_scales`, `nopivot_constants` |
| Prop 7.2 | s_5 >= 1 gives half moment <= 82 | re-derived (pair: Lemma 5.6; diagonal pivot: Lemmas 5.1, 2.4, 2.6, 5.4, 5.5; no pivot: Prop 7.1) | P7 | `halfpotential_constants`, `pivot_scales` |
| Rem 8.3 | E_2 alone does not bound the density: (X1+Y1)^2-(X2+Y2)^2, centred uniforms | computed (density of U^2 is (1-sqrt y)/sqrt y) | `checks/remark83.py`, 2*10^7 samples: density near 0 is 2.67, 4.78, 6.99, 9.22 for bins 10^-1..10^-4, against log(1/h) = 2.30, 4.61, 6.91, 9.21 | - |

## What is not formalized, and why

- Lemma 2.1 (Plancherel, inversion) and Lemma 2.4 (conditioning): standard measure theory, used in the form of any
  graduate text; not restated in Lean here.
- Lemma 2.5 (Weyl and rank inequalities for singular values) and Lemma 2.6 (interlacing for Schur complements):
  Mathlib has no singular values for rectangular real matrices in the form used; tested numerically (L1, L2).
- Theorem 3.1 (geometric Brascamp-Lieb) and everything built on it (Lemmas 3.2, 3.3, Theorem 4.1, Lemma 4.3):
  the heat-flow proof needs PDE and Fourier machinery beyond what can be assembled here; tested numerically (B1-B4,
  D1, D2). The finite parts inside them are formalized: the Gram factorization, the entropy inequality, the branch
  monotonicity, the logarithmic inequality of Lemma 3.2 and the floor bound of Lemma 3.3.
- Lemmas 5.1-5.3 (changes of variables for one and two coordinates) and Lemma 5.4: their constants and elementary
  inequalities are formalized; the change-of-variables formulas are tested numerically (P1-P5).
- Lemma 5.5: the two logarithmic antiderivatives of the exact formula for J(d) are formalized as derivative
  statements (`antideriv_left`, `antideriv_right`); the arcsine piece, which contributes exactly pi, and the passage
  to the improper integrals at the singular endpoints are checked against quadrature (I7, relative error 10^-25).
- Lemma 5.6: the probabilistic statement is tested by Monte Carlo (P6); every constant in it and the antiderivative
  of the near integral are formalized.
- Lemma 6.2 (the sampling expectation): the bordered determinant identity is formalized; the counting of
  (r+1)^2 extensions is checked by exact enumeration (M1).
- Proposition 6.4: the telescoping step, the numerical margins and the diagonal-dominance contradiction are
  formalized; the step "s_{r+1}(D) >= 1 - eps gives r+1 large diagonal entries" uses singular values and is tested (V1).

## Points that needed care

1. Theorem 4.1 needs Q to be a quadratic polynomial, not an arbitrary function of the two blocks: when a heavy row is
   set aside, its coupling to the other rows of the same block must be linear, which holds because that coupling is
   a block of A. The paper states the theorem for quadratic polynomials only.
2. In Lemma 4.3 the complex pushforward nu_x is bounded by the density of M_H X_J, so it lies in L^2 and the
   smoothing limit is a norm limit in L^2; no Fatou argument or weak compactness is needed.
3. The Hoelder step requires every marginal alpha_i to be at most 1/2, so that Lemma 3.3 applies with p = 1/alpha_i
   >= 2. Rows with alpha_i = 0 are dropped using |psi_i| <= 1. When a row exceeds 1/2 it becomes a hub, and the
   marginals of the remaining rows are ratios of the sums Theta_l(H), by the Gram factorization; each promotion
   loses at most a factor 2 in Theta_l.
4. The branch constants of Theorem 4.1 decrease along the promotion (ratio at most e^{-1/2}), so the bound without
   a hub is the worst case; `omega_step` is the integer inequality behind this.
5. In Lemma 3.2 the sum of (1 - beta_i) equals d only when the terms with beta_i = 0 are kept (reading
   0 log(1/0) as 0); the text says so.
6. Lemma 6.2 is an equality whenever every (r+1)-minor has all its r-subminors nonsingular; the enumeration (M1)
   hits ratio 1.0000, so the constant (r+1)^2 cannot be improved in general.
7. Proposition 6.4 uses singular values of the nonsymmetric matrices A - E and D only; symmetry of A enters only
   through the entry bounds (6.2).
8. The decoupling inequality (4.4) is close to sharp in some configurations: in test D2 the ratio of the two sides
   reached 0.985 on 150 cases. This is a check that the test can fail, not a problem with the inequality.
9. The two pivot thresholds enter in different places: eta through eta^{-1/2} in the diagonal-pivot case, zeta
   through zeta^{-1/2} in the indefinite pair case and through zeta^{-1/4} in Lemma 5.6. Without a pivot, two
   diagonal entries of the same sign and modulus above sqrt(zeta) = 1/20 force their off-diagonal entry to be large
   (a_ij^2 > a_ii a_jj - zeta); the test family of V1 (sign matrices with off-diagonal entries below 1/20, and a
   zero diagonal, a constant diagonal of about +-1/25, or a diagonal spread over [-1/50, 1/50], rescaled together
   with the matrix) stays inside the class without pivots, and every generated matrix is checked against the
   definition before it is used.
10. Proposition 7.2 needs the full negative half moment of the Schur complement R, not the truncated one: the
   diagonal-pivot case of Theorem 1.1 bounds p_Q(z) by |a_ii|^{-1/2} E|z - R|^{-1/2}, and the part |z - R| > 1
   contributes at most 1. Lemma 5.6 gives the full half moment for pairs directly.

## Relation to the 17-eigenvalue manuscript and to the fleet's constants

`../fixed-multiplicity-2026-09-24/manuscript.tex` proves the bound under s_17(A) >= s with constant 10^4, using a
regularized determinant estimate (|phi| <= det(I + t^2 M^T M/(pi e)^2)^{-1/8}) in place of Theorem 4.1. That estimate
decays like |t|^{-l/4} at order l, so a density bound needs order five and hence 4*5-3 = 17 eigenvalues. Theorem 4.1
decays like |t|^{-l/2}, so order three suffices (4*3-3 = 9). Sections 5 and 6 here follow the manuscript's Sections
5 and 6, with separate pivot thresholds eta = 3/40 and zeta = 1/400 and kappa = 4/625, restricted to orders k <= 3.
The threshold nine was first derived in `../fixed-multiplicity-2026-09-24/improvements/fleet03/B04/20260924T121940Z-fleet03-B04-fixedmult-audit-r1/REPORT.md`.
The same order-three and order-two estimates, with other constants, were reached independently in the reviews filed
under `../fixed-multiplicity-2026-09-24/improvements/` (fleet02/B04, fleet01/B07, fleet02/B09, fleet02/B10,
fleet02/B18, fleet03/B10) and in the check under `audits/fleet03/B08/.../GROUPED_COMPILER_CHECK.md`; all of them
pass the nine-eigenvalue argument. Constants recorded in the later files read for this audit: 2422 (fleet01/B10
r14), 2547 (fleet01/B11), 6010 (fleet02/B17); the release gate fleet03/B20 r4 records a common safe constant
5338. The separate thresholds 3/40 and 1/400, kappa = 4/625 and the two-coordinate half
potential 16 D^{-1/4} are those of `../fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/NINE_400_AND_OVERLAP.md`,
which reaches the constant 400 with a quarter-power logarithmic moment (L_0 = 4 + 4 log 5); with the half-power
Lemma 5.4 (L_0 < 8) every case here is below 375. A 20-page standalone write-up of that argument is in the same
folder (`paper.tex`, source commit eeb752c8, pointed to by the scheduled workers' objective). The present paper was
written separately and this audit is an independent end-to-end review of the same choice of parameters; a
step-by-step comparison of the two proofs is left to the scheduled reviews.

## What is not claimed

- The theorem for three large eigenvalues (the natural conjecture) is not claimed. Remark 8.2 of the paper
  explains where nine comes from: the case without pivots needs V_3(A) >= c, and the present rank count gives that
  only from nine large eigenvalues. The pivot cases need six and three.
- Continuity of the density is claimed only in the case without pivots.
- The constant 400 is not optimized.
