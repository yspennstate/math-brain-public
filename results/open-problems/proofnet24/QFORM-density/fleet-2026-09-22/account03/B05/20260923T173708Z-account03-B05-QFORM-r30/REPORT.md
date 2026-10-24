# account03 / B05 / QFORM r30

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T17:37:08Z.
attacking: QFORM-PARTIAL-BILINEAR-TRANSVERSE-U-COAREA-v1 — determine whether the r29 half-Riesz trace can be spliced with the two scalar banks without throwing away the third curvature.

## Status

Full QFORM is OPEN: this report is not a proof or counterexample to the conjecture. Full-target continuity is also not proved here. The useful output is (i) a sharp product-kernel half-Riesz lemma, and (ii) an exact obstruction showing why completing both scalar directions before averaging can erase the third curvature even on a target-valid matrix.

Control source refreshed before publication: yspennstate/math-research-brain@fd833b8e184d76d66929db61837a07f3ca3c7574, OWNER CONTROL revision 2026-09-22.15. Execution context remains WITHOUT_VERIFIED_BRAIN.

## 1. A universal product-kernel half-Riesz lemma

Let Y,Z be independent real random variables with probability densities f,g satisfying 0<=f,g<=1. For W=YZ, the usual product-density formula gives, for w!=0,

p_W(w) = int_R f(y) g(w/y) dy/|y|.

By Cauchy-Schwarz,

p_W(w)^2 <= A(w) B(w),

where

A(w)=int f(y)g(w/y)dy <= int f(y)dy = 1,

and

B(w)=int f(y)g(w/y)dy/y^2.

With z=w/y (using absolute Jacobians),

B(w)=|w|^{-1} int g(z) f(w/z) dz <= |w|^{-1}.

Hence

**QFORM-PRODUCT-KERNEL-HALFRIESZ-SPLICE-v1**

> p_{YZ}(w) <= |w|^{-1/2} for a.e. w!=0.

Translations do not alter the density caps, and scaling gives, for fixed y0,z0,q0 and c!=0,

p_{c(Y-y0)(Z-z0)+q0}(t) <= |c|^{-1/2}|t-q0|^{-1/2}.

Consequently, if T is independent of (Y,Z) and

sup_t E |T-t|^{-1/2} <= M,

then convolution with the product kernel yields the genuine density estimate

||p_{T+c(Y-y0)(Z-z0)}||_infty <= |c|^{-1/2} M.

This is exactly the kind of half-order smoothing that would close r29 if the residual half-Riesz variable remained independent of a fixed-shift bilinear product.

## 2. Why full scalar completion does not give that independent splice in the live Schur packet

Work first at the exact double-zero endpoint

B = [[0,c],[c,0]], c!=0,

and write V=(S,R), W=(Y,Z), with

Q = V^T C V + 2 Y p^T V + 2 Z q^T V + 2cYZ + affine terms.

Completing the Y,Z product exactly gives

Q = 2c (Y + q^T V/c)(Z + p^T V/c) + T(V),

where the V-quadratic part of T is

C - P B^{-1} P^T.

In the live ratio-packet normal form this Schur complement is exactly

C - P B^{-1}P^T = lambda [[m,0],[0,0]],

so full completion of both scalar directions removes the rank-two C-curvature used by the r29 same-bank half-Riesz estimate and leaves only a rank-one quadratic residual.

Conditionally on V, the product-kernel lemma gives only

p_{Q|V}(t) <= |2c|^{-1/2} |t-T(V)|^{-1/2}.

If T(V) has a one-dimensional square critical point, averaging this envelope can diverge logarithmically: |t-T|^{-1/2} becomes 1/|S| at the critical level. Therefore the implication

"same-bank half-Riesz + complete both independent scalars + average"

is not valid as a universal proof interface. The failure is not in the product-kernel lemma; it is caused by completing away the transverse mixed curvature before the final reciprocal trace is paid.

## 3. Exact target-valid stress test for that proof-interface failure

The unscaled four-variable form

q0(S,R,Y,Z) = S^2 + 2SR + 2SY + 2RZ + 2YZ

has symmetric matrix

H0 =
[[1,1,1,0],
 [1,0,0,1],
 [1,0,0,1],
 [0,1,1,0]].

Its characteristic polynomial is

x (x^3 - x^2 - 4x + 2).

The cubic has one root in (-2,-1), one in (1/3,1), and one in (2,3): indeed its values at -2,-1,1/3,1,2,3 are respectively -2,4,16/27,-2,-2,8. Therefore the three nonzero eigenvalues of 3H0 all have absolute value strictly larger than 1. Thus

Q = 3 q0

is an exact instance of the owner's target for independent original coordinates S,R,Y,Z with arbitrary cap-one densities.

But q0 factorizes after completing the two scalar directions as

q0 = S^2 + 2(Y+R)(Z+S).

The fixed-V product-kernel envelope is therefore

p_{q0|S,R}(t) <= 2^{-1/2}|t-S^2|^{-1/2}.

At t=0 its average over any cap-one S density positive near zero contains the divergent majorant

int_{|S|<eta} dS/|S| = infinity.

So the complete-both-scalars-first proof literally produces an infinite upper bound on a matrix satisfying the full three-large-eigenvalue hypothesis (after the harmless factor 3). This is a counterexample to that proof interface, NOT to QFORM.

As a consistency check, this same example can be regrouped without rotating dependent coordinates. Set A=Y+R. Since Y and R are independent cap-one variables, A has density f_Y*f_R with ||p_A||_infty<=1, and A is independent of S,Z. Then

q0 = S^2 + 2A(S+Z)

is a rank-three quadratic form in the three independent cap-one variables (S,A,Z), with coefficient matrix

M = [[1,1,0],[1,0,1],[0,1,0]], det M=-1.

Thus the completed rank-exactly-three theorem in the programme controls this stress family after scaling; the logarithmic divergence above is solely a loss in the conditional envelope, not evidence against the conjecture.

## 4. Precise missing factor

The r29 quantity

U = (-r,alpha)^T C (-s,beta)

and identity

T_Y T_Z - U^2 = tau^2 det C

now have a sharper interpretation. A proof must keep at least one mixed/transverse U-type resource alive while smoothing with the independent Y,Z banks. If one fully completes both scalar variables first, the Schur cancellation can collapse the V-quadratic part to rank one and the last half-Riesz integral is at the logarithmic threshold.

Accordingly the next implication is

**QFORM-PARTIAL-BILINEAR-TRANSVERSE-U-COAREA-v1**:

derive an interval/coarea inequality that completes or integrates only one scalar direction at a time, so that the second scalar bank is paid jointly with the transverse minor U (or an equivalent original-coordinate aggregate) before taking a reciprocal or fiber supremum. In the branch where tau^2 det C collapses, switch to the already identified escaped-curvature structural route rather than applying the same envelope again.

This is more precise than the previous generic statement "splice the half-Riesz trace with two scalar banks": the independent product-kernel splice itself is valid, but its required independence is destroyed exactly when the two scalar shifts carry the third curvature.

## 5. Partner result applied to an actual branch

The completed account04/B05 dominant-slope theorem states

||p_Q||_infty < 51.6 (mu m_*)^{-1/3}.

Hence on the concrete exact-slope branch mu>=1 and m_*>=1/8,

||p_Q||_infty < 51.6 * 2 = 103.2.

This closes that branch independently of the partial-completion issue above and leaves the non-atomic/mixed transverse regime as the B05 coarea problem.

## 6. Checks and scope

- The product-kernel proof uses only independence, probability normalization, and the density caps <=1.
- The target-valid stress matrix check is exact: the characteristic polynomial and sign brackets above suffice; no Monte Carlo or floating-point spectral claim is used.
- No post-rotation independence is assumed.
- No moments, support bounds, log-concavity, connected support, or smoothness assumptions are introduced.
- The new product-kernel theorem gives an L-infinity density bound in its stated independent-convolution scope; it does not prove continuity. The stress test proves a proof-interface failure only. Full QFORM and full-target continuity remain open.
