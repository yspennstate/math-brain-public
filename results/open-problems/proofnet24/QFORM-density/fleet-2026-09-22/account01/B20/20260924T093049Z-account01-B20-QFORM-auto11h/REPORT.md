SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-24T09:30:49Z.
attacking: account02/B20 r50's moderate-residual endpoint; convert same-bank curvature transverse to the actual top-two light crossing into a literal physical E3 cut, and test the new compiler on the partner's rank-three Walsh survivor.

# account01/B20 — mixed 2+1 incident-volume compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T093049Z-account01-B20-QFORM-auto11h`  
Status: `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem is NOT claimed proved or disproved. The continuity statement is also kept separate: only the physical-E3 branches paid below have a continuous C0 density.

No Gaussian, moment, iid, compact-support, log-concavity, conditional-cap, rotated-independence, fiber-supremum, or law-uniform pointwise quadratic oscillatory-decay assumption is used.

## 1. Pinned inputs

1. Fresh owner control: `yspennstate/math-research-brain@0aae39e792eb341d930934f748c48cc0325f14a8`, with owner revision `2026-09-22.15`; QFORM remains the sole research target and the full theorem remains open.

2. Designated completed partner: `yspennstate/math-open-problems@3482c3d93d336c0993f6aa85a7a0c78c9a07ffad`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260924T091256Z-account02-B20-QFORM-auto11-r50/REPORT.md`.
Its unpaid r50 chamber is a retained-tail rank-12/rank-11 moderate residual endpoint. It also records the explicit flat Walsh rank-three residual stress family used in Section 5 below.

3. The actual r52 light crossing used below is pinned at `yspennstate/math-open-problems@5ec1cc2bf208bc0249ea89d86fd7298b62ac324e`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T070220Z-account03-B19-QFORM-r52/REPORT.md`.
It supplies a literal original-coordinate crossing `N=A[R,C]` with

    tau = 2^-16,
    ||N-N0||_F < tau,
    sigma_2(N) > beta := 4089/458752,

where `N0` has rank at most two and its source-normalized left and right two-frames have every physical row leverage at most 1/2.

4. Analytic receiver: `yspennstate/math-open-problems@1439f3ecb30a49b8363552d780159306f4b9c56f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T184716Z-account02-B03-QFORM-auto11/REPORT.md`, theorem `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`:
for every literal original-coordinate cross block `M` with `Z3=e3(MM^T)>0`, the full ambient quadratic form has a continuous C0 density and

    ||p_Q||_infty <= C3 Z3^(-1/6),
    C3 = 3*2^(4/3)*e^(1/3) = 10.5501688311648... .

Same-side curvature, outside coordinates/couplings, affine terms, signs, extra spectrum, and nonzero coefficient tails are retained by that theorem.

## 2. New deterministic theorem: mixed 2+1 incident volume

Let `R,C` be disjoint literal original-coordinate sets and let

    N=A[R,C]=U Sigma V^T + N_tail

be the ACTUAL SVD split into its top two singular directions and the orthogonal remainder. Thus `U,V` have two orthonormal columns and `Sigma=diag(sigma_1,sigma_2)`, `sigma_2>0`. Let

    P=UU^T, Q=I-P,
    D=A[R,R]-diag(A[R,R]).

For each physical `j in R` define `y_j=D e_j`, `q_j=Qy_j`, `ell_j=P_jj`, and define the physical mixed incident volume

    Gamma_R := sum_{j in R} sum_{S subset R\{j}, |S|=3}
                 det([U_S,(D e_j)_S])^2.                         (2.1)

### Theorem 2.1 — `QFORM-MIXED-2PLUS1-INCIDENT-VOLUME-v1`

There exists a literal physical partition `R=I disjoint_union J` such that, for the literal full crossing

    M=A[I, C union J],

one has

    e3(MM^T) >= ((sigma_1 sigma_2)^2/16) Gamma_R
              >= (sigma_2^4/16) Gamma_R.                         (2.2)

Moreover the incident currency has the exact identity

    Gamma_R = sum_j [(1-ell_j)||q_j||_2^2 - |q_j(j)|^2].          (2.3)

In particular, if `h=max_j ell_j`, then

    Gamma_R >= (1-h)||Q D||_F^2 - h||P D||_F^2.                  (2.4)

### Proof of (2.2)

The SVD remainder is orthogonal on the right to the top-two part, hence after any row restriction

    N_I N_I^T
      = (U_I Sigma V^T)(U_I Sigma V^T)^T
        + (N_tail)_I (N_tail)_I^T
      >= (U_I Sigma V^T)(U_I Sigma V^T)^T.                       (2.5)

Also `A[I,J]=D[I,J]` because the diagonal never crosses the partition. Therefore

    MM^T = N_I N_I^T + D[I,J]D[I,J]^T

PSD-dominates the Gram matrix of `[U_I Sigma V^T, D[I,J]]`. Monotonicity of `e3` on the PSD cone and Cauchy-Binet allow us to keep only column triples containing two columns from the first block and one physical column `j in J` from the second block. For any fixed three-row set `S subset I` and `j in J`, Cauchy-Binet on the right two-frame gives

    sum_{T subset C, |T|=2}
      det([(U Sigma V^T)_{S,T}, (D e_j)_S])^2
      = (sigma_1 sigma_2)^2 det([U_S,(D e_j)_S])^2,              (2.6)

because `sum_{|T|=2} det(V_T)^2=det(V^T V)=1`.

Choose the partition of R by independent fair signs. For each pair `(S,j)` with `|S|=3` and `j notin S`, the event `S subset I, j in J` has probability `2^-4=1/16`. Hence the expected selected sum is exactly `(sigma_1 sigma_2)^2 Gamma_R/16`; some physical split realizes at least its expectation. This proves (2.2). No random variable is rotated.

### Proof of (2.3)-(2.4)

For fixed j, total Cauchy-Binet gives

    sum_{|S|=3} det([U_S,y_{j,S}])^2 = ||Qy_j||^2 = ||q_j||^2.    (2.7)

Replacing `y_j` by `q_j` does not change these determinants. The sum of the terms whose row set contains j is the row-j leverage contribution of the three-column matrix `[U,q_j]`. Since `U^T q_j=0`, it equals

    ell_j ||q_j||^2 + |q_j(j)|^2.                                (2.8)

Subtracting (2.8) from (2.7) proves (2.3). Since `D_jj=0`,

    q_j(j)=-(PDe_j)_j,
    |q_j(j)|^2 <= ell_j ||PDe_j||^2.                              (2.9)

Summing (2.3) and using `ell_j<=h` yields (2.4). QED.

## 3. Apply it to the retained r52 light crossing

Let `P0` be the left two-plane of the source rank-two approximant `N0`. Its physical row leverages are at most 1/2. Let P be the left top-two singular projection of the ACTUAL N. Since `||N-N0||_op<tau`, the top-two singular equation gives

    ||(I-P0)U||_op <= tau/sigma_2(N) < tau/beta = 7/4089.        (3.1)

For equal-dimensional two-planes this bounds `||P-P0||_op`, so every ACTUAL top-two leverage obeys

    P_jj < h := 1/2 + 7/4089 = 4103/8178
               = 0.5017119100024456... .                         (3.2)

The same argument applies on C to the ACTUAL right top-two singular plane.

Take the fixed incident-volume gate

    Gamma_* = 2^-20.                                               (3.3)

If `Gamma_R >= Gamma_*`, Theorem 2.1 yields a literal physical cut with

    e3(MM^T) > beta^4 2^-24
              = 3.76215482072658e-16.                              (3.4)

The marginal-free physical-E3 receiver therefore pays the full ambient law:

    ||p_Q||_infty
      < C3 (beta^4 2^-24)^(-1/6)
      = 3926.629866970723... < 3927.                               (3.5)

This branch has a continuous C0 density.

If it is not paid through this route, the exact structural obstruction is

    Gamma_R < 2^-20.                                                (3.6)

By (2.4) and (3.2), this implies the explicit one-sided alignment inequality

    ||Q D||_F^2
      < (4103/4075)||P D||_F^2
        + (8178/4075) 2^-20.                                       (3.7)

Applying the transposed theorem to the C bank gives the same alternative for its same-bank off-diagonal curvature. Thus any r50/r52 state still unpaid by this compiler must have BOTH mixed incident currencies below `2^-20`; this is stronger information than a bare rank bound.

## 4. What the new currency measures

Equation (2.3) is deliberately physical. `Gamma_R` vanishes exactly when every column of the same-bank off-diagonal curvature fails, after deleting its own physical coordinate, to create a third row-volume direction transverse to the actual top-two crossing plane. It therefore measures precisely the missing 2+1 geometry that the r50 retained-residual endpoint did not encode.

The construction does not discard the top-two SVD tail: (2.5) shows that the actual tail contributes a positive-semidefinite term. Nor does it discard diagonal or same-bank curvature: only the diagonal is absent from a literal cross cut by identity, while every off-diagonal coefficient is retained in D.

## 5. Actual equation-level consumption of account02/B20 r50

The completed partner r50 report exhibits a flat Walsh residual as a stress test. Let `m=1024`; choose flat orthonormal Walsh vectors `u1,...,u5` and `v1,v2`. Its crossing is

    N = c [u1 u2][v1 v2]^T,       c=1/64,                           (5.1)

and its same-bank residual is

    E = sum_{k=3}^5 u_k u_k^T.                                      (5.2)

This was correctly reported by account02/B20 as surviving the partner's `s5` and D5 gates; it is not a target counterexample. Apply the new theorem to the ACTUAL crossing. Here

    P=u1u1^T+u2u2^T,
    D=E-(3/m)I,
    Q=I-P,
    ell_j=2/m.                                                       (5.3)

Since E is orthogonal to P,

    PD=-(3/m)P,
    QD=E-(3/m)Q.                                                     (5.4)

Hence

    ||QD||_F^2
      = 3(1-3/m)^2 + (m-5)(3/m)^2,                                  (5.5)

and every physical diagonal entry of `QD` equals `6/m^2`. Substitution into the exact identity (2.3) gives

    Gamma_R = 3(m-5)/m.                                              (5.6)

At `m=1024`,

    Gamma_R = 3057/1024 = 2.9853515625.                              (5.7)

Because `sigma_1=sigma_2=c`, Theorem 2.1 gives a literal original-coordinate cut with

    e3(MM^T)
      >= c^4 Gamma_R/16
      = 3057/2^38
      = 1.1121301213279366e-8.                                      (5.8)

The physical-E3 receiver now gives

    ||p_Q||_infty
      <= C3 (3057/2^38)^(-1/6)
      = 223.3058714826806... < 224,                                 (5.9)

with continuous C0 density.

Thus the partner's explicit moderate rank-three Walsh survivor is paid directly by a physical E3 cut; Theorem H is not needed for this stress family. This is the required equation-level use of the completed account02/B20 result.

## 6. Scope and first remaining implication

New proved claim:

    QFORM-R50-MIXED-2PLUS1-INCIDENT-VOLUME-COMPILER-v1.

It closes every r52 light-crossing state for which either bank has mixed incident currency at least `2^-20`, and it closes the specific account02/B20 r50 rank-three Walsh survivor with density constant <224.

The full target remains OPEN. The first unresolved structural chamber is now

    QFORM-R50-TWOSIDED-MIXED-INCIDENT-VOLUME-COLLAPSE-
    PLUS-R12/R11-RETAINED-TAIL-ENDPOINT-v1,

namely the partner's retained-tail finite-rank endpoint together with `Gamma_R,Gamma_C<2^-20` relative to the ACTUAL top-two light crossing planes. A productive next step is to combine the exact identity (2.3) on both banks with the four-latent determinant/rank-collapse information, rather than recursively discarding residual singular directions.

Corrections respected: no law-uniform pointwise quadratic Fourier decay; no arbitrary-joint coarea shortcut; no fiber-supremum shortcut; no conditional projection-density cap; no post-rotation independence; no one-good-minor inference; no deletion of nonzero tails.
