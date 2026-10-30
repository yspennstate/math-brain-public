SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-23T10:39:40Z.
attacking: kappa-free gradient/coarea payment for the near-double-zero grouped packet, preserving the dependent (S,R) product projection.

# fleet03/B05 r23 — Schur-gradient density and the exact ambient-to-level coarea gap

**Programme:** QFORM-DENSITY-3EIG-20260922.  
**Assignment:** Quadratic coarea bound.  
**Status:** new supporting geometric theorem proved; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** not proved by this theorem.  
**Execution:** WITHOUT_VERIFIED_BRAIN. Repository retrieval and native learned-memory ingestion remain separate facts.

## 1. Why this is the first unpaid implication

The preceding fleet03/B05 r22 report reduced the difficult two-sheet packet to the regime where the physical scalar pair can become nearly singular (`kappa -> 0`), exact-slope atoms may be absent, and the normalized residual coupling can vanish. Its pair-log density receiver is independent of the ratio residual but still pays a reciprocal power of `kappa`; its exact-double-zero null-scalar receiver avoids `kappa` only when the residual coupling is quantitatively nonzero.

The present run changes the mechanism. Instead of estimating the output density first, it studies **three original-coordinate directional derivatives simultaneously**. The main point is that the Schur cancellation produces one derivative combination depending only on `S`, while the other two derivatives are the scalar-pair gradients. A shear has determinant one, so the scalar-pair condition number disappears exactly rather than perturbatively.

The result is a `kappa`-free three-dimensional density bound for the relevant gradient triple and, consequently, a dimension-free reciprocal-gradient expectation. This pays the whole grouped packet before any reciprocal local minor. It does **not** yet provide the missing uniform level trace; Section 6 identifies that factor precisely.

## 2. Exact grouped normal form

Let `(S,R)` be the two coordinates of the normalized product projection from the first original-coordinate packet. For the nonzero-residual packet it has a joint density `h(s,r)`; only the marginal cap

    ||p_S||_infinity <= L_S

will be used. In the QFORM packet one has `L_S <= sqrt(2)` by the one-dimensional product-projection bound.

Let `W=(Y,Z)` come from two disjoint original-coordinate banks, independent of `(S,R)`, with density caps

    ||p_Y||_infinity <= L_Y,
    ||p_Z||_infinity <= L_Z.

The active conditional quadratic-plus-affine form is

    Q(V,W)
      = V^T C V + 2 V^T P W + W^T B W
        + ell_V^T V + ell_W^T W + c0,                     (2.1)

where `V=(S,R)`, `B` is a real symmetric invertible `2x2` matrix, and

    C - P B^{-1} P^T = [[a,0],[0,0]],    a != 0.           (2.2)

For the ratio packet from fleet01/B05 r26,

    a = lambda m,
    D = |det B|,
    mu = D |lambda|,
    D |a| = mu m.                                          (2.3)

All affine coefficients may depend on the conditioned outside original coordinates. The estimate below is uniform in them.

## 3. Main theorem: Schur-gradient density

### Theorem 3.1 — QFORM-SCHUR-GRADIENT-DENSITY-v1

Under (2.1)-(2.2), write

    g_S = partial_S Q,
    g_W = (partial_Y Q, partial_Z Q).

Then `(g_S,g_Y,g_Z)` has a density satisfying

    ||p_(g_S,g_Y,g_Z)||_infinity
       <= L_S L_Y L_Z / (8 |a det B|).                    (3.1)

Equivalently, for every `tau>0`,

    P(max(|g_S|,|g_Y|,|g_Z|) <= tau)
       <= (L_S L_Y L_Z / |a det B|) tau^3.                (3.2)

No lower bound on `sigma_min(B)` occurs. No cap for the conditional law `S|R=r` is used. The residual coordinate `R` may be arbitrarily dependent on `S`.

### Proof

Set

    v = e_1^T P B^{-1}                                  (3.3)

and form the Schur-combined derivative

    H = g_S - v g_W.                                     (3.4)

From (2.1),

    g_S = 2 e_1^T C V + 2 e_1^T P W + ell_S,
    g_W = 2 P^T V + 2 B W + ell_W.

Therefore

    H
      = 2 e_1^T(C-PB^{-1}P^T)V
        + ell_S - e_1^T P B^{-1} ell_W
      = 2 a S + beta,                                    (3.5)

where `beta` is a scalar independent of `S,R,Y,Z`. In particular `H` is independent of `R` as a function of the live variables.

Fix `R=r`. The affine map

    (s,y,z) -> (H,g_Y,g_Z)                               (3.6)

has derivative matrix of block-triangular form

       [ 2a            0      0 ]
       [   *                 ]
       [   *          2 B       ]

and hence Jacobian determinant

    |J| = 8 |a det B|.                                   (3.7)

Let `(s(h),w(h,g,r))` denote its inverse for fixed `r`. By change of variables, the joint density of `(H,g_W,R)` is

    rho_(H,g_W,R)(h,g,r)
      = h_SR(s(h),r)
        p_Y(w_1(h,g,r)) p_Z(w_2(h,g,r))
        / (8 |a det B|).                                 (3.8)

Integrate in `r`, use `p_Y<=L_Y`, `p_Z<=L_Z`, and then use the **marginal**, not conditional, cap of `S`:

    rho_(H,g_W)(h,g)
      <= [L_Y L_Z/(8|a det B|)]
         integral h_SR(s(h),r) dr
      =  [L_Y L_Z/(8|a det B|)] p_S(s(h))
      <= L_S L_Y L_Z/(8|a det B|).                       (3.9)

Finally `(H,g_W) -> (g_S,g_W)` is the shear

    g_S = H + v g_W,                                     (3.10)

whose determinant is one. Thus the same density cap holds for the raw gradient triple. This proves (3.1). Integrating this density over the cube `[-tau,tau]^3`, of volume `8 tau^3`, proves (3.2). QED.

### Remarks

1. The potentially huge factor `||PB^{-1}||` never appears. Bounding `|H|` by `(1+||PB^{-1}||)|grad Q|` would lose exactly the near-singular pair scale. The determinant-one shear is the correct operation.
2. The proof never conditions on `R`, so it does not invoke the refuted conditional-density-cap interface.
3. The proof uses the original-coordinate product structure only through the genuine independence of the three disjoint banks and the marginal cap for the normalized projection `S`.

## 4. Reciprocal-gradient coarea budget

Let

    G = max(|g_S|,|g_Y|,|g_Z|),
    K = L_S L_Y L_Z / |a det B|.                          (4.1)

Then (3.2) gives

    P(G <= tau) <= min(1, K tau^3).                       (4.2)

Layer cake yields

    E G^{-1}
      = integral_0^infinity P(G < 1/t) dt
      <= K^{1/3} + K integral_(K^{1/3})^infinity t^{-3} dt
      = (3/2) K^{1/3}.                                    (4.3)

Because the directions `S,Y,Z` are unit original-coordinate directions with disjoint bank provenance, the full original-coordinate Euclidean gradient obeys

    ||grad Q||_2 >= G.                                    (4.4)

Therefore

    boxed(
    E ||grad Q||_2^{-1}
       <= (3/2) [L_S L_Y L_Z / |a det B|]^{1/3}.
    )                                                      (4.5)

This is an ambient coarea estimate, uniform in the dimension, the pair condition number, all affine terms, and the dependence between `S` and `R`.

For the ratio packet, `L_S,L_Y,L_Z <= sqrt(2)` and `|a det B|=mu m`, so

    boxed(
    P(G <= tau) <= [2 sqrt(2)/(mu m)] tau^3,
    E ||grad Q||_2^{-1} <= (3/sqrt(2)) (mu m)^(-1/3).
    )                                                      (4.6)

Using fleet01/B05 r26's constant-mass packet `m>=3/20`,

    P(G <= tau)
       <= [40 sqrt(2)/(3 mu)] tau^3
       < 18.857 mu^{-1} tau^3,                             (4.7)

and

    boxed(
    E ||grad Q||_2^{-1}
       <= (3/sqrt(2))(20/3)^{1/3} mu^{-1/3}
       < 3.993 mu^{-1/3}.
    )                                                      (4.8)

Thus the `kappa -> 0` singularity is **not present in the ambient reciprocal-gradient budget**.

## 5. Coarea interpretation

Let `f` denote the active original-coordinate product density after fixing the outside coordinates. The coarea formula, first with `(epsilon+||grad Q||)^{-1}` and then by monotone convergence, gives

    integral_R T_2(t) dt
       = E ||grad Q||_2^{-1},                              (5.1)

where

    T_2(t)
      = integral_{Q=t} f(x) / ||grad Q(x)||_2^2
          d H^{d-1}(x).                                   (5.2)

Hence (4.8) proves the quantitative integrated trace estimate

    integral_R T_2(t) dt < 3.993 mu^{-1/3}.               (5.3)

The desired output density, however, is

    p_Q(t)
      = integral_{Q=t} f(x) / ||grad Q(x)||_2
          d H^{d-1}(x).                                   (5.4)

So this run removes the near-singular-pair loss **before level localization**. The remaining issue is not a reciprocal-gradient blow-up in ambient product measure.

## 6. The precise missing factor: ambient-to-level trace

A formal Cauchy-Schwarz inequality on a level gives

    p_Q(t)^2 <= T_2(t) S_0(t),                             (6.1)

where

    S_0(t) = integral_{Q=t} f(x) d H^{d-1}(x).             (6.2)

Neither (5.3) nor product-density caps alone give a uniform bound for `S_0(t)` or for `T_2(t)` pointwise in `t`. This is exactly where the refuted arbitrary-joint shell/coarea interfaces would enter if one discarded product provenance.

The obstruction is structural, not merely a constant loss: the live correction stream contains bounded-density three-dimensional shell measures concentrated along a thin quadratic level whose quadratic pushforward density is arbitrarily large. Since the gradient map of a nondegenerate quadratic is linear and invertible, a bounded joint density for the gradient by itself cannot replace the missing level-product structure.

Therefore the next B05 implication is now sharpened to:

**QFORM-GRADIENT-TO-LEVEL-PRODUCT-TRACE-v1.** In the grouped packet normal form, use the original product provenance to upgrade the kappa-free gradient-density estimate (3.1) / integrated trace (5.3) to

    sup_t integral_{Q=t} f/||grad Q|| dH <= C mu^{-1/3},    (6.3)

without conditioning `S` on `R` and without replacing the active law by an arbitrary bounded joint density.

Any successful next argument should spend the determinant-one Schur shear before taking a level supremum. Paying `||PB^{-1}||`, `kappa^{-1}`, or a conditional cap is now known to be avoidable at the ambient-gradient stage.

## 7. Designated partner applied to an actual inequality

The completed designated partner result is fleet04/B05 r2:

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B05/20260923T041255Z-fleet04-B05-dominant-slope-r2/REPORT.md`.

For exact-slope mass `m_*>0` it proves

    ||p_Q||_infinity < 51.6 (mu m_*)^{-1/3}.               (7.1)

Applying it at the concrete threshold `mu>=1`, `m_*>=1/4` gives

    boxed(||p_Q||_infinity < 51.6 * 4^{1/3} < 81.91).      (7.2)

Thus the exact-slope branch has a genuine full density bound. In the complementary near-parallel/no-large-atom packet, (4.8) gives the new kappa-free ambient estimate on exactly the same determinant scale `mu^{-1/3}`. The remaining distinction is therefore level localization, not the scalar-pair condition number.

## 8. Dependencies and checks

Consumed mathematical sources:

1. fleet03/B05 r22, canonical commit `2d50abfc12e46bb37e72db66f5a6f0e23aca5c1a`, for the previous two-sheet state and the definitions of `mu,kappa,m`;
2. fleet01/B05 r26, canonical commit `b0299facc04ea0c03276dddb1a12c027aed5a946`, for the ratio-variance packet, `m>=3h/20`, the orthonormal `(S,R)` construction, and the exact Schur remainder `lambda diag(m,0)`;
3. fleet04/B05 r2, canonical commit `59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`, applied in (7.2).

A finite diagnostic check on 873 random invertible symmetric `B`, random `P`, and nonzero `a` verified

    det D_(s,y,z)(H,g_Y,g_Z) = 8 a det B

with maximum floating-point absolute error `5.7e-14`. This is only a regression check; equations (3.5)-(3.9) are the proof.

## 9. Scope and status

**Proved this run:**

- `QFORM-SCHUR-GRADIENT-DENSITY-v1`, equation (3.1);
- the kappa-free cubic gradient small-ball estimate (3.2)/(4.6);
- the reciprocal-gradient expectation (4.5)/(4.8);
- the integrated squared-Jacobian coarea trace (5.3).

**Not proved:**

- a pointwise bound for `T_2(t)`;
- the desired full level trace (6.3);
- the unrestricted QFORM theorem;
- the full continuity conclusion.

The theorem retains arbitrary fragmented input supports, arbitrary affine terms, indefinite `B`, arbitrary pair condition number, and the dependence of `S` and `R`. No Gaussian, log-concavity, moment, compact-support, connected-support, or rotated-coordinate independence assumption is used.
