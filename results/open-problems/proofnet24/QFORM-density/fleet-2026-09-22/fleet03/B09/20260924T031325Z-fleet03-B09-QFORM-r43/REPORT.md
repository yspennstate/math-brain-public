SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-24T03:13:25Z.
attacking: the heavy physical off-diagonal pair endpoint by combining exact pair-Schur algebra with aggregate original-coordinate linear anti-concentration on the Schur-null face, and by compiling the rank-two overlap currency into a literal disjoint two-row crossing before reciprocal minor selection.

# fleet03/B09 — Schur-null aggregate-star smoothing + literal disjoint E2 compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations  
Run: `20260924T031325Z-fleet03-B09-QFORM-r43`  
Status: **NEW SUPPORTING THEOREMS / EXACT SCHUR-NULL SUBBRANCH PAID / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted owner target remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence hypothesis is introduced. All probabilistic coordinates below are literal ORIGINAL coordinates. Arbitrary same-bank quadratic curvature, outside couplings and affine terms are retained. Nothing uses the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea bound, worst conditional projection-density moment, fiber-supremum reduction, or deletion of a small nonzero coefficient.

## 1. Fresh source boundary and the exact debt

The immediate same-slot predecessor is

`yspennstate/math-open-problems@1fe06352f0192b8b0110e6d86844daa785da8c93`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260924T024509Z-fleet03-B09-QFORM-r43/REPORT.md`.

It reduced the nonphysical-kernel grouped rank-two endpoint to a literal physical-pivot-or-heavy-physical-pair fork. In its difficult branch a physical pair has a quantitatively large off-diagonal coefficient, while the first scalar Schur pivot may vanish or be too small. Its named debt is

`QFORM-RANK2-HEAVY-OFFDIAGONAL-PAIR-THIRDRESOURCE-v1`.

The complementary fleet02/B09 source

`yspennstate/math-open-problems@d5d7bf292da3a593888913cc453ad0e604462cd6`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260924T021301Z-fleet02-B09-QFORM-r16/REPORT.md`

pays the **exact rank-one** physical-pair endpoint with arbitrary pair-to-leaf cross rank and arbitrary leaf curvature, but proves that a merely near-rank-one pair cannot be handled by taking a worst half-Riesz slice first. The third resource must be spent jointly.

Two completed analytic inputs are used below.

1. `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`, source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite literal physical pair `B`, putting

`D=|det B|`, `kappa=sigma_min(B)`,

if its exact physical Schur remainder `R` obeys

`sup_t P(|R-t|<rho) <= H0 sqrt(rho)`,

then

`||p_Q||_infinity <=4 sqrt(2 H0) (D kappa)^(-1/4)`.             (1.1)

This is a final linear interval bound, not a square-root decoupling conclusion.

2. `QFORM-ROW-MARGINAL-FREE-2VOLUME-COLLISION-v1`, source

`yspennstate/math-open-problems@588fa418bc29d4b889fcbbee2b61370234ceef37`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260923T175336Z-fleet01-B03-QFORM-r30/REPORT.md`.

For a literal two-row physical crossing matrix `M` with

`Z2=det(MM^T)>0`,

the arbitrary-curvature ambient form satisfies the half-Riesz estimate

`sup_t E|Q-t|^(-1/2) <=2^(11/4) Z2^(-1/8)`.                     (1.2)

The designated fleet04/B09 result is applied in Section 7.

## 2. Rank-two packet notation

Let `L={1,2,3}` be three literal original coordinates and `J` a disjoint original-coordinate bank. Condition on every coordinate outside `L union J`. Write

`Q=Y^T P Y+2Y^T C Z+G(Z)+ell^T Y+const`,                       (2.1)

where `P=A[L,L]`, `C=A[L,J]`, `G` is an arbitrary quadratic-affine polynomial on the entire right bank, and

`rank C=2`.                                                       (2.2)

Let `n` be a unit vector spanning `ker(C^T)`, put

`a=Pn`,                                                           (2.3)

and let

`s1>=s2>0`

be the two nonzero singular values of `C`, with

`Delta=s1 s2`.                                                    (2.4)

The grouped overlap currency from the preceding B09 work is

`V=Delta^2 ||a||_2^2`.                                           (2.5)

No random variable is rotated in what follows.

## 3. New theorem A: overlap-to-literal-disjoint E2 compiler

For each physical `j in L`, let

`H_j=L\{j}`

and move the literal coordinate `j` to the opposite side. The resulting **disjoint original-coordinate** cross block is

`M_j=A[H_j,J union {j}]
     =[ C[H_j,J] | P[H_j,j] ]`,                                  (3.1)

which has two physical rows. Put

`Z2_j=det(M_j M_j^T)`.                                           (3.2)

Let `G_C=CC^T`, let `p_j=P e_j` be the `j`-th physical column of `P`, and define

`r_j=e_j cross p_j`.                                              (3.3)

### Theorem 3.1 — `QFORM-RANK2-OVERLAP-TO-DISJOINT-E2-v1`

For every `j`,

`boxed:
 Z2_j = Delta^2 n_j^2 + r_j^T G_C r_j.
`                                                                    (3.4)

Moreover, with `D0=diag(P_11,P_22,P_33)`,

`boxed:
 sum_j Z2_j
 >= Delta^2 + s2^2 ||(P-D0)n||_2^2.
`                                                                    (3.5)

Consequently some literal disjoint cut satisfies

`boxed:
 Z2_j >= (1/3)[Delta^2+s2^2||(P-D0)n||_2^2].
`                                                                    (3.6)

This is a deterministic coefficient theorem. It compiles the off-diagonal action of `P` on the rank-two kernel into a genuine source-coordinate crossing before any individual minor is inverted.

### Proof

Fix `j` and abbreviate `H=H_j`, `v=P[H,j]`. Since

`M_jM_j^T=G_C[H,H]+vv^T`,                                        (3.7)

the two-dimensional determinant lemma gives

`Z2_j=det(G_C[H,H])+v^T adj(G_C[H,H])v`.                         (3.8)

Because `G_C` has rank two and kernel `span(n)`,

`adj(G_C)=Delta^2 n n^T`.                                        (3.9)

Hence the principal cofactor is

`det(G_C[H,H])=Delta^2 n_j^2`.                                   (3.10)

A direct two-by-two cofactor calculation identifies the second term as

`v^T adj(G_C[H,H])v=(e_j cross p_j)^T G_C(e_j cross p_j)`,       (3.11)

proving (3.4).

On `n^perp`, the two eigenvalues of `G_C` are `s1^2,s2^2`, so

`r_j^T G_C r_j >=s2^2 ||P_(n^perp)r_j||^2`.                     (3.12)

Since `n` is unit,

`||P_(n^perp)r_j||=||n cross r_j||`.                             (3.13)

The vector triple-product identity gives

`n cross (e_j cross p_j)
 =e_j(n^T p_j)-p_j n_j
 =e_j a_j-p_j n_j`.                                              (3.14)

Sum (3.4) and use `sum n_j^2=1`:

`sum_j Z2_j
 >=Delta^2+s2^2 sum_j ||e_j a_j-p_j n_j||^2`.                   (3.15)

The `j`-th component of the `j`-th vector in the last sum is

`a_j-P_jj n_j=[(P-D0)n]_j`.                                      (3.16)

Discarding all other nonnegative components gives (3.5), and averaging over the three indices gives (3.6). QED.

### Fractional consequence

Applying (1.2) to the winning literal cut in (3.6) gives

`sup_t E|Q-t|^(-1/2)
 <=2^(11/4) 3^(1/8)
   [Delta^2+s2^2||(P-D0)n||^2]^(-1/8)`                           (3.17)

with numerical prefactor

`2^(11/4)3^(1/8)=7.71742903968...`.                              (3.18)

Equation (3.17) is deliberately recorded as a **half-Riesz** conclusion, not a density theorem. A third smoothing credit is still required. Its value is that the high-off-diagonal branch is now represented by one actual disjoint source partition rather than an overlapping invariant.

## 4. Pair Schur algebra without a leafwise reciprocal

Choose a literal physical pair `H=L\{k}` and suppose its principal block

`B=P[H,H]`                                                        (4.1)

is invertible indefinite. Write

`p=P[H,k]`, `d=P_kk`, `C_H=C[H,J]`, `c=C[k,J]`.                  (4.2)

Completing the pair `H` exactly leaves a Schur remainder on `{k} union J`. Its scalar coefficient and whole cross row are

`s=d-p^T B^(-1)p`,                                               (4.3)

`m=c-p^T B^(-1)C_H`.                                            (4.4)

The right-bank self curvature after completion is arbitrary and is retained.

### Lemma 4.1 — exact scalar and aggregate-star identities

One has

`boxed: s=det(P)/det(B).`                                        (4.5)

Also

`boxed:
 n_k m^T = - C_H^T B^(-1) a_H,
`                                                                    (4.6)

where `a_H=(Pn)_H`.

If `n_k!=0`, then `C_H` has row rank two,

`det(C_H C_H^T)=Delta^2 n_k^2`,                                 (4.7)

and therefore

`boxed:
 ||m||_2 >= s2 ||B^(-1)a_H||_2
          >= s2 ||a_H||_2/||B||op.
`                                                                    (4.8)

### Proof

Equation (4.5) is the standard determinant identity for the scalar Schur complement. For (4.6), use

`C^T n=C_H^T n_H+c^T n_k=0`,                                    (4.9)

`a_H=Bn_H+p n_k`.                                                (4.10)

Thus

`C_H^T B^(-1)a_H
 =C_H^T n_H+C_H^T B^(-1)p n_k
 =-c^T n_k+C_H^T B^(-1)p n_k
 =-n_k m^T`.                                                      (4.11)

For (4.7), the left side is the `k,k` cofactor of `CC^T`, hence (3.9) gives exactly `Delta^2 n_k^2`. Therefore

`sigma_min(C_H)
 =Delta |n_k|/sigma_max(C_H)
 >=Delta |n_k|/s1
 =s2 |n_k|`.                                                      (4.12)

Taking norms in (4.6), applying (4.12), and using

`||B^(-1)a_H||>=||a_H||/||B||op`

gives (4.8). QED.

The important point is that `m` is the **whole** original-coordinate Schur-star row. No largest leaf coefficient is selected.

## 5. New theorem B: Schur-null aggregate-star smoothing

Assume now

`det(P)=0`,                                                       (5.1)

so by (4.5) the pair Schur scalar is **exactly**

`s=0`.                                                            (5.2)

The residual has the form

`R(X_k,Z)
 =2X_k m^T Z+beta X_k+G_1(Z)`,                                   (5.3)

where `G_1` is an arbitrary quadratic-affine polynomial on the entire right bank.

### Theorem 5.1 — `QFORM-INDEFINITEPAIR-SCHURNULL-AGGREGATE-STAR-v1`

Suppose

- `rank C=2`;
- `B=P[H,H]` is a literal invertible indefinite physical pair;
- `det P=0`;
- `n_k!=0`;
- `Pn!=0`.

Then `m!=0`, the full conditional and unconditional law has an essentially bounded density, and

`boxed:
 ||p_Q||_infinity
 <=2^(27/8)
   [ |det B| sigma_min(B) ||m||_2 ]^(-1/4).
`                                                                    (5.4)

Using only original rank-two packet quantities,

`boxed:
 ||p_Q||_infinity
 <=2^(27/8)
 [ |det B| sigma_min(B)
   s2(C) ||a_H||_2/||B||op ]^(-1/4).
`                                                                    (5.5)

Every interval `I` therefore satisfies the same coefficient times `|I|`.

If `i in H` is a heavy component with

`|a_i|>=||a||/sqrt(3)`,                                          (5.6)

then

`boxed:
 ||p_Q||_infinity
 <=11.902
 [ |det B| sigma_min(B) s2(C)||a||/||B||op ]^(-1/4).
`                                                                    (5.7)

### Proof: aggregate linear anti-concentration

Because `s=0`, condition on the entire right bank `Z`. For fixed `Z=z`, (5.3) is affine in the genuine original coordinate `X_k`, with slope

`T(z)=2m^Tz+beta`.                                                (5.8)

Hence

`P(|R-t|<rho | Z=z)
 <=min(1,2rho/|T(z)|)`.                                          (5.9)

The one-dimensional product-projection theorem gives

`||p_(m^T Z)||_infinity <=sqrt(2)/||m||`.                        (5.10)

After the factor two in (5.8),

`||p_T||_infinity <= M:=1/(sqrt(2)||m||)`.                       (5.11)

For any `eta>0`, average (5.9) and split according to `|T|<=eta`:

`P(|R-t|<rho)
 <=2M eta+2rho/eta`.                                             (5.12)

The optimum `eta=sqrt(rho/M)` gives

`boxed:
 sup_t P(|R-t|<rho)
 <=2^(7/4)||m||^(-1/2) sqrt(rho).
`                                                                    (5.13)

Thus the pair-log hypothesis (1.1) holds with

`H0=2^(7/4)||m||^(-1/2)`.                                       (5.14)

Insert (5.14) into (1.1):

`4 sqrt(2H0)
 =4 sqrt(2^(11/4)||m||^(-1/2))
 =2^(27/8)||m||^(-1/4)`,                                        (5.15)

which proves (5.4). Equation (5.5) follows from (4.8).

It remains only to check that the denominator is nonzero under the stated hypotheses. If `a_H=0`, then the scalar identity obtained from (4.3),

`a_k=p^T B^(-1)a_H+n_k s`,                                      (5.16)

would give `a_k=0` because `s=0`. Hence `Pn=a=0`, a contradiction. Therefore `a_H!=0`, so (4.8) gives `m!=0`. Finally (5.7) is (5.5) plus `||a_H||>=||a||/sqrt(3)` and

`2^(27/8)3^(1/8)=11.9019026093...`.                              (5.17)

QED.

### What this closes and what it does not

This pays the **exact Schur-null face** of the heavy indefinite physical-pair branch using the whole original-coordinate star before any leafwise reciprocal. The square-root estimate (5.13) is only an intermediate smoothing profile; the final conclusion is the required `O(|I|)` interval bound (5.4), so no square-root decoupling loss survives.

It does **not** prove a uniform collar for `det P !=0` but tiny. When `s` is nonzero, however small, the residual is quadratic in `X_k`; the fleet02/B09 near-rank-one obstruction shows that arbitrary same-bank curvature can align the critical value and defeat a naive perturbation of (5.13). The next step must interpolate at the pair-plus-star level rather than delete `sX_k^2` or take a worst half-Riesz slice.

Continuity is not asserted by the pair-log/small-ball proof above. Full-target continuity remains OPEN.

## 6. Target-valid regression

Take

`P=[[0,1,0],
    [1,0,1],
    [0,1,0]]`,                                                   (6.1)

`C=[[1,0],
    [0,1],
    [-1,-1]]`,                                                    (6.2)

and the full five-coordinate matrix

`A_*=[[P,C],[C^T,0_2]]`.                                         (6.3)

Then

`det P=0`,

`n=(1,1,1)/sqrt(3)`,

`(s1,s2)=(sqrt(3),1)`,

`Pn=(1,2,1)/sqrt(3)`.                                            (6.4)

Choose `H={1,2}`, `k=3`. Then

`B=[[0,1],[1,0]]`,

`|det B|=1`, `sigma_min(B)=1`,                                   (6.5)

and exact pair completion gives

`s=0`,

`m=(-2,-1)`, `||m||=sqrt(5)`.                                   (6.6)

Therefore Theorem 5.1 gives

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=2^(27/8) 5^(-1/8)
 =8.484084489464063... .
`                                                                    (6.7)

The spectrum of `A_*` is

`{-2.214319743...,-1.414213562...,0.539188873...,
   1.414213562...,1.675130871...}`,                              (6.8)

so four eigenvalues have modulus at least one. This is a genuine target-valid instance, not a subclass that drops the owner's spectral requirement.

For the same example, Theorem 3.1 gives literal disjoint two-row crossing currencies after moving each left coordinate to the opposite bank; the checker verifies (3.4) exactly to numerical precision.

## 7. Designated fleet04/B09 result applied to an actual inequality

The completed designated partner theorem is

`QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`,

source `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,

path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It proves that a literal invertible physical `3x3` cross block `K` gives

`||p_Q||_infinity <=3 |det K|^(-1/3)`                            (7.1)

with arbitrary dense same-side curvature and a continuous density.

Apply it to

`K=diag(1,1,4)`,

`A_partner=[[0,K],[K,0]]`.                                       (7.2)

The spectrum is

`{-4,-1,-1,1,1,4}`,                                              (7.3)

so the owner target holds, and `det K=4`. Hence the actual final-law inequality is

`boxed:
 ||p_(X^T A_partner X)||_infinity
 <=3*4^(-1/3)
 =1.889881574842310...,
`                                                                    (7.4)

with

`P{X^T A_partner X in I}
 <=1.889881574842310... |I|`                                     (7.5)

and a continuous density.

## 8. Exact remaining B09 debt

The new first obstruction is narrower than the predecessor's generic heavy-pair wording:

`QFORM-RANK2-HEAVY-PAIR-NEAR-SCHURNULL-INTERPOLATION-v1`:

> For a literal invertible indefinite physical pair in the rank-two packet, interpolate uniformly between the exact Schur-null aggregate-star theorem above and the nonzero scalar-Schur branch, spending the whole star and scalar curvature jointly before any worst half-Riesz slice. Equivalently, control the regime `s=det(P)/det(B) ->0` without treating `s X_k^2` as a deletable perturbation. Preserve arbitrary right-bank curvature and original product provenance.

A second structural issue is when the useful heavy pair has complement `k` with `n_k=0`; then `C_H` drops to rank one and the quantitative lower bound (4.8) does not apply. That case should be routed through physical-kernel / row-promotion machinery rather than silently divided by `n_k`.

Full unrestricted QFORM remains **OPEN**. Full-target continuity remains **OPEN**. No full-target counterexample was found.

## 9. Deterministic verification plan

The accompanying checker verifies on seeded random rank-two matrices and singular left blocks that

- `adj(CC^T)=Delta^2 n n^T`;
- the literal disjoint identity (3.4);
- the summed lower bound (3.5);
- `s=det(P)/det(B)`;
- `n_k m^T=-C_H^TB^(-1)a_H`;
- the target-valid spectrum and numerical bound (6.7);
- the partner constant (7.4).

The finite checks audit algebra and arithmetic only; they are not evidence for the universal theorem beyond the displayed proofs.
