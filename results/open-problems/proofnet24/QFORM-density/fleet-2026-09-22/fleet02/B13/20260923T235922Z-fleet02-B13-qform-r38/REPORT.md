# fleet02/B13 r38 — tau-clean intrinsic pair mass -> actual physical e2 crossing

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: supporting theorem only. The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED; continuity is separate. No moment, support, log-concavity, diagonal-basis, post-rotation independence, or attained-extremizer assumption is used.

## First unpaid implication

`QFORM-TAUCLEAN-E2-2TO4MODE-RECEIVER-v1`: pay an original-coordinate physical cross bank carrying a rho^{-4}-scale aggregate **tau-clean** two-volume, while every actual physical cross bank has fifth singular scale O(rho^{-1}) by the pinned unconditional D5 theorem. The receiver must preserve the partner's physical finite-center/diffuse-bank information and may not select/invert one tiny minor, delete retained curvature, or rotate the product variables. Otherwise construct a genuine bounded-finite-union product-indicator counterexample.

## Inputs actually used

Use the latest completed compatible designated-partner result fleet03/B13 r38, commit `ff2b04c19ca6cf8bebe0cbd03981bc4711d6d3f0`, `QFORM-RANK2-DPP-FOURIER-DISJOINTNESS-v1`, `QFORM-DPP-WEIGHTED-TRANSVERSE-L1-SHARPENED-v1`, and `QFORM-MU-FINITECENTER-OR-DIFFUSE-BANK-v1`.

In its diffuse exact-rank-two chamber

    A = D + U Lambda U^T,   U^T U = I_2,   max_i ||u_i||^2 <= 1/3,

with slab ratio rho, the partner selects a physical coordinate k with |d_k| >= 1. For physical pairs E={r,s} disjoint from k put

    q_E = det(U_E)^2,
    Delta_E = sum_{F: |F|=2, F cap (E union {k})=empty} q_F,
    W_k = sum_E q_E Delta_E,
    mu_k(E)=q_E Delta_E/W_k.

The partner proves

    W_k >= 1/12.

In its hard non-rank-one branch,

    |det Lambda| > H_0 rho^{-2},
    H_0 = sqrt(1536 e^2) = sqrt(1536) e = 106.53445530886934...,
    |A_kk| <= H_0 rho^{-2},

and, for

    tau_E = d_k q_rs + d_r q_ks + d_s q_kr,

    E_{mu_k}|tau_E| < 267.630809135 rho^{-1},

hence

    mu_k{ |tau_E| <= T rho^{-1} } >= 1/2,
    T = 535.261618270.

The exact identity H_0^2/384 = 4 e^2 will be used below.

The owner-pinned source `e5f71d79eff325201dd0274053d20268ce65b837` was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed unconditional D5 theorem says for every actual original-coordinate disjoint cross block B=A[I,J],

    ||p_Q||_infty <= 5 sqrt(2e) e_5(B^T B)^(-1/10).

The pinned counterexample search reports no valid counterexample in its tested families; no numerical observation is used as proof here.

## Theorem 1 — QFORM-TAUCLEAN-PHYSICAL-E2-CROSSING-v1

Assume the partner r38 hard non-rank-one chamber above. Define the good physical pair set

    G = { E: |E|=2, k notin E, |tau_E| <= T rho^{-1} }.

Then there is an original-coordinate physical partition C sqcup C^c = [n]\{k} such that, with the actual physical cross block

    B_C = A[C,C^c],

and the tau-clean two-volume subsum

    Z_G(C)
      := sum_{E subset C, |E|=2, E in G}
         sum_{F subset C^c, |F|=2} det A[E,F]^2,

one has

    Z_G(C) >= (det Lambda)^2 / 384
           > 4 e^2 rho^{-4}.                              (1)

In particular

    e_2(B_C^T B_C) >= Z_G(C) > 4 e^2 rho^{-4}.             (2)

Every row pair E counted in Z_G(C) is a genuine original-coordinate pair and obeys

    |tau_E| <= 535.261618270 rho^{-1}.                      (3)

### Proof

Because D is diagonal and E,F are disjoint physical two-sets away from k,

    A[E,F] = U_E Lambda U_F^T,

so

    det A[E,F]^2 = (det Lambda)^2 q_E q_F.                  (4)

Choose C by independently coloring every coordinate in [n]\{k} red/blue with probability 1/2. For each ordered disjoint physical pair (E,F), the event E subset C and F subset C^c has probability 2^{-4}=1/16. Therefore

    E_C Z_G(C)
      = (det Lambda)^2/16 * sum_{E in G} q_E Delta_E
      = (det Lambda)^2 W_k mu_k(G)/16
      >= (det Lambda)^2 / (16*12*2)
      = (det Lambda)^2/384.                                (5)

Hence some deterministic physical cut C satisfies the same lower bound. Cauchy-Binet gives

    e_2(B_C^T B_C)
      = sum_{E subset C, F subset C^c, |E|=|F|=2} det B_C[E,F]^2,

so the restricted nonnegative subsum Z_G(C) is at most e_2(B_C^T B_C). Finally the hard branch gives

    (det Lambda)^2 > 1536 e^2 rho^{-4},

and dividing by 384 proves (1). No random-coordinate transformation is performed: the random coloring is only a deterministic existence argument over original coordinates. QED.

## Corollary 2 — partner finite-center/diffuse fork also crosses physically

The same cut averaging localizes the two branches of partner r38 rather than merely the global good set.

### Finite-center branch

For any R>=1, suppose the partner provides a physical center h with

    mu_k{E: h in E} >= 1/(48R)

and star-conditional mean

    E(|tau_E| | h in E) < 12846.2788385 R rho^{-1}.

By Markov, the star-good set

    G_h={E: h in E, |tau_E|<25692.5576770 R rho^{-1}}

has mu_k-mass at least 1/(96R). The same Bernoulli-cut calculation gives some physical cut C with

    Z_h(C)
      := sum_{E subset C, E in G_h}
         sum_{F subset C^c, |F|=2} det A[E,F]^2
      >= (det Lambda)^2/(18432 R)
      > e^2/(12R) rho^{-4}.                                (6)

Thus a finite intrinsic center produces an actual cross-bank two-volume star: every contributing physical row pair contains the same h.

### Diffuse-bank branch

Suppose the partner provides L_R with

    det(U_{L_R}^T U_{L_R}) >= 1/24,
    s_i/S_R <= 1/R for i in L_R,
    mu_k{E subset L_R}>1/2,

and

    E(|tau_E| | E subset L_R)<535.261618270 rho^{-1}.

Then

    G_L={E subset L_R: |tau_E|<1070.52323654 rho^{-1}}

has mu_k-mass >1/4. Hence some physical cut C satisfies

    Z_L(C)
      := sum_{E subset C, E in G_L}
         sum_{F subset C^c, |F|=2} det A[E,F]^2
      > (det Lambda)^2/768
      > 2 e^2 rho^{-4}.                                    (7)

So the genuinely diffuse intrinsic bank also has a genuine original-coordinate crossing certificate, without choosing one favorable minor.

## Corollary 3 — pinned D5 supplies the general 2-to-4-mode obstruction

For every arbitrary target-class high-density witness, not merely the exact rank-two chamber, apply the pinned D5 theorem to every actual physical cut B=A[I,J]:

    e_5(B^T B) <= (5 sqrt(2e)/rho)^10,                       (8)
    s_5(B) <= 5 sqrt(2e)/rho
           = 11.6582199079856... rho^{-1}.                  (9)

Thus any future robust receiver that promotes the tau-clean crossing certificate to an actual cross block in a general survivor only needs to cope with at most four singular directions above the explicit O(rho^{-1}) scale; any fifth transverse physical mode is already paid by the pinned Fourier theorem. This is an actual coefficient inequality on every original-coordinate cut, with no leverage or moment hypothesis.

In the exact rank-two chamber of Theorem 1, e_5=0 identically; the point of (8)-(9) is the robust general obstruction needed by the unpaid glue problem, not an artificial use of D5 inside a block where rank already kills it.

## Why this is progress

Partner r38's strongest information was an intrinsic pair law mu_k weighted by q_E Delta_E. That law is excellent for aggregate arguments but is not itself a physical product-coordinate bank to which one may blindly apply conditioning or Fourier receivers. Theorem 1 converts half of its tau-clean mass into a single **actual physical cross block** while preserving the whole pair-volume sum. It therefore removes one provenance gap: no latent rotation, post-rotation independence, or single-minor denominator is needed.

The finite-center/diffuse corollary does the same conversion branchwise. The remaining difficulty is analytic rather than measure-theoretic: e_2 alone is a borderline two-direction Fourier currency, so the next receiver must use the tau cancellation / physical center-bank structure to gain the missing integrability while D5 prevents a fifth uncontrolled transverse direction.

## Extremal-product interface

No attained global bathtub optimizer is used. The valid reduction is approximation: every probability density f with 0<=f<=1 can be approximated in L1 by finite convex mixtures of indicators of bounded finite unions of intervals of total measure one. For products,

    || prod_i f_i - prod_i g_i ||_1 <= sum_i ||f_i-g_i||_1.

Therefore any strict slab violation transfers with arbitrarily small loss to a finite mixture and hence to at least one bounded-finite-union product-indicator component. There is no centered-interval conclusion, no common support-diameter bound, and no uniform fragment-count bound. Fragmented and originally unbounded supports remain admissible.

## Counterexample status

No valid counterexample was produced. The pinned numerical search found none, but those experiments are not proof and are not used in any implication above.

## Next mathematical move

Prove `QFORM-TAUCLEAN-E2-2TO4MODE-RECEIVER-v1`. The promising split is:

1. finite-center: use (6) to convert a shared physical row h plus tau cancellation into a one-hub/two-form Fourier estimate before any reciprocal minor is taken;
2. diffuse bank: use (7), the partner's normalized transverse-mass cap, and a geometric BL/half-Riesz estimate on the whole bank;
3. robust/general survivor: invoke (9) first to isolate at most four physical singular directions above rho^{-1}, and keep the low singular tail inside the actual phase rather than deleting it.

Any proof must remain uniform in fragmented finite-union supports and cannot use support diameter to make coefficient-small remainders probabilistically small.
