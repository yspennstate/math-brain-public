# QFORM-PAIRLOG-SCHUR-CENTER-v1

Run: `20260922T204204Z-account02-B09-QFORM-r9`  
Worker: `account02/B09` — Bilinear block mechanism  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Control observed at start: brain main `2010e67fe8c43f12a3925927ab6d4a8145c18731`, OWNER CONTROL revision `2026-09-22.15`; protected controls were unchanged in the pre-write comparison through `831d0901bc5ca9931fae3e59161029b424fba0bc`.  
Status: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED; full conjecture remains OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The current B09 bottleneck is

`QFORM-THREEBANK-CYCLE-OR-SCHURCENTER-ROUTING-v1`:

starting only from `s_3(A)>=1`, in the high-leverage / low-ridge residual, aggregate disjoint ORIGINAL-coordinate banks before paying any reciprocal physical minor and force at least one of:

1. a three-bank zero-self cycle to which account03/B09 `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1` applies at universal scale;
2. a three-scalar compression having an indefinite endpoint pair `E` and a quantitatively nonzero Schur-center coefficient `delta=det(G)/det(E)` at universal scale, so the theorem below applies;
3. an already-paid ridge, scalar-pivot, zero-self Frobenius, definite-pair, or grouped hyperbolic/square branch;

or else isolate the genuine remaining curved-bank operator and prove a product-preserving estimate for it. The theorem below pays item 2 exactly; the structural routing from the bare spectral hypothesis remains open.

## 2. Source-pinned dependencies and corrections

Fresh programme state and corrections were read from `yspennstate/math-research-brain@2010e67fe8c43f12a3925927ab6d4a8145c18731`, including `CURRENT_RESEARCH.md`, `CLAIMS.json`, `DELTAS.json`, `CORRECTION_INBOX.json`, `PATHWAYS.md`, `MEMORY_PROTOCOL.md`, and the exact account02/B09 assignment card.

The mathematical inputs used positively are:

* the complete two-coordinate logarithmic envelope `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1`, full proof `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`;
* account02/B09 `QFORM-ZERODIAG-TRIANGLE-LOGSMOOTH-v1`, specifically its scalar quadratic log-averaging Lemma 4.1, full proof `yspennstate/math-open-problems@1abb65eef22eb44be26d8b21dd5c7174fba4aa1:proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T171216Z-account02-B09-QFORM-r5/REPORT.md`;
* named partner account03/B09 `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1`, canonical mathematics `yspennstate/math-open-problems@5e92c0aa0681b3d24630451076ab511f92dc718c`.

Consumed corrections include failure of law-uniform pointwise quadratic Fourier decay, loss from naive spectral-fiber suprema, loss of independence after rotation, failure of a universal single rank-two Schur extraction, failure of the local rank-three-cross-cut dichotomy, failure of conditional-cap-as-independence substitutions, and B09's same-square heavy-row counterexample. None is used as a positive premise.

## 3. Main theorem: an indefinite physical pair is paid by a scalar Schur center

### Theorem 3.1 — QFORM-PAIRLOG-SCHUR-CENTER-v1

Let `X,Y,Z` be independent real random variables with densities bounded by one. Let

`G = [[E, v], [v^T, beta]]`

be a real symmetric `3 x 3` coefficient matrix after ordering the two endpoint variables first and the center variable last. Assume the `2 x 2` endpoint block `E` is invertible and indefinite. Put

`D = |det E|`, `kappa = sigma_min(E)`, `Delta = |det G|`,

and assume `Delta>0`. Then for every affine perturbation `ell^T (X,Z,Y)+c`, the quadratic form has an essentially bounded density satisfying

`||p_Q||_infinity <= 8 sqrt(2) sqrt( D/(kappa Delta) ) + 2/sqrt(D)`.    (3.1)

The same estimate holds inside an arbitrary larger product input after conditioning all original coordinates outside these three; hence arbitrary outside quadratic terms and outside-to-selected couplings are allowed. Consequently every interval `L` obeys

`P(Q in L) <= [8 sqrt(2) sqrt(D/(kappa Delta)) + 2/sqrt(D)] |L|`.        (3.2)

No square-root small-ball conversion or resampling enters.

### Proof

Condition on all variables except the three selected original coordinates; this only changes affine coefficients and an additive constant. Write the endpoint vector as `w=(X,Z)^T`. The conditional form is

`w^T E w + 2Y v^T w + beta Y^2 + affine`.

For fixed `Y=y`, complete the endpoint pair. Its matrix is always the same indefinite `E`; only its affine shift varies with `y`. The source-pinned pair-log theorem therefore gives, for every `r>0`,

`p_(Q|Y=y)(t) <= 2 sqrt(2)/r`
` + D^(-1/2) log_+( 2r^2/(kappa |t-t0(y)|) )`,                 (3.3)

where `t0(y)` is the critical value after completing the pair.

Completing the pair explicitly shows that the quadratic coefficient of `t0(y)` is

`delta = beta - v^T E^(-1) v`.                                (3.4)

The block determinant identity is

`det G = det E * delta`,                                      (3.5)

so `|delta|=Delta/D>0`. The linear and constant coefficients of `t0` are irrelevant.

Average (3.3) in the cap-one variable `Y`. Apply account02/B09 Lemma 4.1 to the quadratic `t0(y)` with

`L0 = 2r^2/kappa`.

It gives

`E log_+(L0/|t-t0(Y)|)`
` <= 2 + log_+( 8L0/|delta| )`
` = 2 + log_+( 16r^2/(kappa |delta|) )`.                      (3.6)

Choose

`r^2 = kappa |delta|/16`.                                     (3.7)

Then the logarithm in (3.6) vanishes, and (3.3)-(3.7) give

`p_Q(t) <= 8 sqrt(2)/sqrt(kappa |delta|) + 2/sqrt(D)`
`        = 8 sqrt(2) sqrt(D/(kappa Delta)) + 2/sqrt(D)`.       (3.8)

The bound is uniform in the outside conditioning, so averaging preserves it. This proves (3.1)-(3.2). QED.

### Definite endpoint companion

If the same physical endpoint block `E` is definite instead, the completed pair has density at most `pi/sqrt(|det E|)` for every affine perturbation, by the definite-pair part of the pair-log source. Conditioning and averaging therefore give

`||p_Q||_infinity <= pi/sqrt(|det E|)`.                        (3.9)

Thus the Schur-center payment is needed only for the indefinite endpoint logarithm.

## 4. Three-bank scalar-compression corollary

Let `I,J,K` be disjoint original-coordinate banks and

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`.

The three projections are independent because the banks are disjoint. Suppose all active quadratic dependence on these banks factors through `z=(U,V,W)` with scalar coefficient matrix `G`; arbitrary outside variables may add affine shifts after conditioning. If the projection density caps are `M_U,M_V,M_W`, rescale by `U'=M_U U`, etc. The rescaled variables have density caps one and coefficient matrix

`Gbar = diag(M_U,M_V,M_W)^(-1) G diag(M_U,M_V,M_W)^(-1)`.      (4.1)

In particular, for unit vectors `u,v,w`, the standard product-marginal cap `sqrt(2)` allows `M_U=M_V=M_W=sqrt(2)`, hence `Gbar=G/2`. If an endpoint pair `E` of `G` is indefinite, Theorem 3.1 becomes

`||p_Q||_infinity <= 16 sqrt(2) sqrt(D/(kappa Delta)) + 4/sqrt(D)`,     (4.2)

where again `D=|det E|`, `kappa=sigma_min(E)`, `Delta=|det G|` are computed before this uniform `sqrt(2)` rescaling.

This is a bank-first estimate: the whole independent bank is compressed before reciprocal determinant payment, rather than choosing one tiny physical coefficient.

## 5. Target-valid diffuse curved-chain family

Take three disjoint banks of size `m`, with normalized constant vectors `u,v,w`, and scalar projections `U,V,W`. Consider the scalar coefficient matrix

`G0 = [[2,1,0], [1,2,1], [0,1,-2]]`.                         (5.1)

Its characteristic polynomial is

`p(lambda)=lambda^3-2lambda^2-6lambda+8`.                     (5.2)

The sign brackets are exact:

`p(-3)=-19`, `p(-2)=4`; `p(1)=1`, `p(2)=-4`; `p(3)=-1`, `p(4)=16`.

Thus its three eigenvalues lie respectively in `(-3,-2)`, `(1,2)`, `(3,4)`, so all have absolute value greater than one: this is a genuine target matrix after embedding in the three banks.

Choose endpoint variables `U,W`. Then

`E=diag(2,-2)`, `D=4`, `kappa=2`, `Delta=|det G0|=8`.           (5.3)

The cap-one scalar theorem would give

`||p_Q||_infinity <= 1+4sqrt(2)`.                             (5.4)

For actual unit bank projections the `sqrt(2)` marginal-cap version (4.2) gives the still universal

`||p_Q||_infinity <= 2+8sqrt(2) < 13.314`.                    (5.5)

Every physical coefficient inside the rank-one bank blocks or cross blocks is `O(1/m)`. A one-coordinate-from-each-bank principal compression is `G0/m`, so reciprocal local-minor payment deteriorates with `m`, whereas (5.5) is independent of `m`. This is a direct aggregate-before-inversion gain on a curved, non-zero-self target family.

## 6. Named partner result applied to an actual inequality

Apply account03/B09 `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1` to the same three disjoint unit-projection banks and

`F = 2(UV+UW-VW)`.                                            (6.1)

The scalar coefficient matrix has zero diagonal and off-diagonal signs `(1,1,-1)`, hence nonzero spectrum `{1,1,-2}`. The three aggregate cross strengths are exactly one. Therefore the partner theorem gives the target-valid bound

`||p_F||_infinity <= 2(3+log 8) < 10.159`.                   (6.2)

Again every individual physical cross coefficient is only `1/m`. Equations (5.5) and (6.2) are complementary: the partner pays a coherent zero-self cycle, while Theorem 3.1 pays a genuinely curved scalar compression through its nonzero Schur center.

## 7. Exact source-valid falsifier to dropping the Schur-center tax

The condition `Delta>0`, equivalently `delta!=0`, cannot simply be removed from this mechanism. Let independent

`X,Y,Z ~ Uniform[-1/2,1/2]`

and

`Q=(X+Y)^2-Z^2`.                                              (7.1)

Its coefficient matrix is

`Gdeg = [[1,1,0],[1,1,0],[0,0,-1]]`,                          (7.2)

which contains the perfectly conditioned indefinite endpoint pair `diag(1,-1)` after taking endpoints `X,Z`, but `det Gdeg=0`; its spectrum is `{2,-1,0}`.

Put `S=X+Y`. Near zero the triangular density of `S` is `p_S(s)=1-|s|`, so the density of `S^2` is asymptotic to `t^(-1/2)` as `t downarrow0`. For `Z^2`, the density is exactly `t^(-1/2)` on `0<t<1/4`. Therefore the density of the difference at zero contains

`integral_0^epsilon p_(S^2)(u) p_(Z^2)(u) du`,                (7.3)

which diverges logarithmically like `integral_0^epsilon du/u`. Hence (7.1) has unbounded density at zero.

This does **not** refute QFORM: (7.2) has only two nonzero, hence only two large, eigenvalues. It refutes the tempting intermediate claim that one uniformly conditioned indefinite pair plus an arbitrary center is sufficient without a quantitative third Schur-center curvature. The determinant ratio `|delta|=Delta/D` in Theorem 3.1 is therefore a genuine third-direction payment, not an artifact of the proof.

## 8. Conditional end-to-end route

A compact conditional full proof now has the following shape.

* The completed spectral-window/ridge theorem pays the low-leverage high-spectrum branch.
* Existing scalar-pivot, zero-self Frobenius, definite-pair, grouped square/hyperbolic, and rank-two-half-Riesz results pay their exact branches.
* Account03/B09 pays a coherent zero-self three-bank cycle by (6.2).
* The present theorem pays any three-bank scalar compression with a controlled indefinite endpoint pair and controlled nonzero Schur-center determinant by (4.2).

Thus the first missing implication is purely structural/product-preserving: prove `QFORM-THREEBANK-CYCLE-OR-SCHURCENTER-ROUTING-v1`, or construct a source-valid target counterexample to that routing and isolate its curved-bank operator. Arbitrary within-bank curvature orthogonal to the selected scalar projections remains an explicit unpaid residual; it is not discarded or replaced by a bistochastic/spectral surrogate.

## 9. Integrity

No numerical experiment is used as mathematical evidence. The root brackets in Section 5 and all constants follow from displayed exact algebra. No moments, bounded support, identical laws, centering, log-concavity, or post-rotation independence assumptions are used. The result establishes essential boundedness in its exact scope and a direct `O(|L|)` interval estimate; continuity is not claimed. The full conjecture remains open.
