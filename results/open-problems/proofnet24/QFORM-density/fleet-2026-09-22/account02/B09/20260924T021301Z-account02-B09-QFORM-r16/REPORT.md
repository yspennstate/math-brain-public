SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-24T02:13:01Z.
attacking: the exact rank-one physical-pair collar with arbitrary pair-to-leaf cross rank and completely arbitrary same-leaf curvature; then identify the obstruction to carrying the same half-Riesz interface through a merely near-rank-one pair.

# account02/B09 r16 — exact singular pair, arbitrary cross rank, arbitrary leaf curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid obstructions  
Status: **ESSENTIAL STEP APPLIED / NEW SCOPE EXTENSION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The owner target is unchanged: arbitrary independent real original-coordinate inputs with probability densities bounded by one; arbitrary symmetric `A` with at least three eigenvalues of modulus at least one; universal essential density bound or a target-valid counterexample. No moments, support, log-concavity, diagonal-basis hypothesis, post-rotation independence, or deletion of a small coefficient is used below.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-NEARRANKONE-PAIR-THIRDRESOURCE-BEFORE-HALFRIESZ-v1`:

> At an **exact** nonzero rank-one physical pair, every nonzero physical kernel-star is now paid at linear interval scale with completely arbitrary pair-to-leaf cross rank and completely arbitrary same-leaf curvature. The remaining singular collar is the genuinely **near**-rank-one case `det B !=0 ->0`, where the residual small hub square can combine with leaf curvature into a perfect square and make the conditional half-Riesz interface infinite. A successful interpolation must spend a third spectral/smoothing resource jointly before a worst-slice half-Riesz step; it cannot merely perturb the exact-rank-one proof.

Section 7 gives a target-valid family proving this method obstruction exactly.

## 2. Source boundary and duplicate-work audit

Fresh owner control remained QFORM-only, OWNER CONTROL revision `2026-09-22.15`, with no later stop or B09 reassignment found before this report. The live correction inbox was reread. In particular this run does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint three-dimensional coarea, conditional projection caps after rotation, a fiber supremum, or a uniformly good single physical minor.

Required historical source, read at the owner-pinned commit:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed ingredients used here are the one-dimensional product-projection density bound (in its reviewed Rogozin--Ball form in the current source line), the scalar-square / half-Riesz interface, and Theorem H, which is applied to an actual source-coordinate star in Section 6. The pinned counterexample search reports no valid full-target counterexample.

The latest designated partner account03/B09 result is

`yspennstate/math-open-problems@4ddad6fe460658dd00ffa73da5bb6da181065a26`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T014456Z-account03-B09-QFORM-auto11/REPORT.md`.

It proves a Schur/E2 receiver for an exact rank-one physical pair **under rank-one pair-to-leaf cross** and arbitrary leaf curvature, with a positive transverse-defect currency. It is applied quantitatively in Section 5.

A duplicate-work audit also found the newer account01/B09 run `20260924T015544Z-account01-B09-QFORM-auto11`, which proves the direct arbitrary-leaf-curvature estimate for an exact rank-one pair when the **whole pair-to-leaf cross block has rank one**. The present theorem removes that cross-rank assumption entirely. The elementary one-sided bathtub mechanism is therefore not claimed as new; the new content is its source-preserving arbitrary-cross compiler and its overlap-two consequence.

## 3. Exact rank-one pair: no pair-to-leaf rank assumption is needed

Let `H={h_1,h_2}` be two literal original coordinates and `L=H^c` after conditioning any further disjoint source bank. Suppose

`B=A[H,H]=tau ell ell^T`, `tau!=0`, `||ell||_2=1`,                 (3.1)

so the physical pair core is nonzero rank one. Let `k` be a unit vector perpendicular to `ell`. The leaf block

`D=A[L,L]`                                                        (3.2)

is completely arbitrary symmetric, and the cross block

`C=A[L,H]`                                                        (3.3)

is now also completely arbitrary: **no rank-one assumption on `C`**.

Define the physical kernel-star vector and its size

`q=C k`, `s=||q||_2`.                                             (3.4)

Assume `s>0`.

Relabel the two physical hub coordinates, if necessary, so that

`|ell_1|>=|ell_2|`, hence `|ell_1|>=1/sqrt(2)`.                  (3.5)

Write the two columns of `C` as `u=A[L,h_1]`, `v=A[L,h_2]`, and put

`a=tau ell_1^2`, `b=tau ell_1 ell_2`.                             (3.6)

Because `B` has rank one, its second diagonal is `b^2/a`. Complete the square in the **literal original coordinate** `X_{h_1}`. With arbitrary affine terms retained, one gets exactly

`Q=a U^2 + K(X_L) X_{h_2} + R(X_L)`,                              (3.7)

where

`U=X_{h_1}+(b/a)X_{h_2}+a^(-1)<u,X_L>+constant`,

`K(X_L)=2<c,X_L>+eta`,

`c=v-(b/a)u`,                                                     (3.8)

and `R` is an arbitrary measurable quadratic-plus-affine function of the leaf variables. No part of `D` has been removed.

The key exact identity is

`c = q/ell_1`.                                                     (3.9)

Indeed with orientation `k=(-ell_2,ell_1)`, `q=-ell_2 u+ell_1 v`.

### Conditional one-sided square estimate

Fix `X_L=z`. The shear `(X_{h_1},X_{h_2})->(U,X_{h_2})` has unit Jacobian, and the conditional joint density is

`f_{h_1}(U-(b/a)X_{h_2}-a^(-1)<u,z>-constant) f_{h_2}(X_{h_2})`.

Resolve `aU^2=t-R(z)-K(z)X_{h_2}`. Summing the two possible square roots and using `f_{h_1}<=1` gives a one-sided square kernel. For every `K!=0`, the cap-one bathtub estimate on the remaining physical coordinate gives

`||p_(Q|X_L=z)||_infinity
 <= 2 |a|^(-1/2)|K(z)|^(-1/2).`                                  (3.10)

The exceptional set `K=0` is null after averaging because `s>0` and the linear form below has a density.

The reviewed one-dimensional product-projection theorem gives

`||p_(<c,X_L>)||_infinity <= sqrt(2)/||c||_2`.                    (3.11)

Hence `K=2<c,X_L>+eta` has density cap at most

`1/(sqrt(2)||c||_2)`.                                             (3.12)

For any probability density bounded by `M`, the symmetric inverse-half bathtub estimate is

`E|Y|^(-1/2) <=2 sqrt(2M)`.                                       (3.13)

Therefore

`E|K|^(-1/2) <=2^(5/4)||c||_2^(-1/2)`.                           (3.14)

Averaging (3.10) gives the sharper physical-pivot form

`boxed:
 ||p_Q||_infinity
 <=2^(9/4)|a|^(-1/2)||c||_2^(-1/2).`                             (3.15)

The identical coefficient multiplies every interval length. Continuity is not claimed by this argument.

Using `a=tau ell_1^2`, `||c||=s/|ell_1|`, and (3.5), we obtain the invariant theorem.

### Theorem — `QFORM-RANKONEPAIR-ARBITRARY-CROSS-ARBITRARY-LEAFCURVATURE-v1`

For a literal nonzero rank-one physical pair, arbitrary pair-to-leaf cross matrix `C`, arbitrary symmetric leaf block `D`, arbitrary affine terms, and nonzero kernel-star `q=Ck`,

`boxed:
 ||p_Q||_infinity
 <=2^(5/2) (|tau| s)^(-1/2).`                                    (3.16)

Thus

`boxed:
 P{Q in J}
 <=2^(5/2)(|tau|s)^(-1/2)|J|.`                                  (3.17)

No probability is squared, so there is no square-root small-ball loss. The proof never rotates random coordinates and never takes a conditional density of a rotated projection.

## 4. Overlap-two compiler with arbitrary cross rank

The previous account02/B09 exact singular-pair ledger proved, without any assumption on the leaf block, that for each outside physical coordinate `i`, if

`u_i=A[H,i]`, `q_i=k^T u_i`,

then for distinct `i,j`

`det A[H union {i},H union {j}] = -tau q_i q_j`.                  (4.1)

Therefore the fixed-pair overlap-two currency is

`Omega_(2,H)
 =tau^2[(sum_i q_i^2)^2-sum_i q_i^4]`.                           (4.2)

This identity also does **not** require the pair-to-leaf cross to have rank one. Since

`Omega_(2,H) <= tau^2 s^4`,                                      (4.3)

Theorem (3.16) yields the source-coordinate overlap consequence

`boxed:
 ||p_Q||_infinity
 <=2^(5/2)|tau|^(-1/4) Omega_(2,H)^(-1/8).`                       (4.4)

In particular, on the macroscopic overlap collar `Omega_(2,H)>=1/4`,

`boxed:
 ||p_Q||_infinity
 <=2^(11/4)|tau|^(-1/4)
 =6.7271713221... |tau|^(-1/4).`                                 (4.5)

This removes the previous *analytic* arbitrary-leaf-curvature obstruction at the exact singular pair even when the physical pair-to-leaf cross has rank two. What remains quantitative is the tiny-`|tau|` collar, not entangled same-leaf curvature by itself.

## 5. Latest designated partner applied, then strictly enlarged

Use the partner stress family with even `m`,

`B=diag(1,0)`,
`A[L,H]=r e_2^T`,
`r=m^(-1/2)(1,...,1)`,
`D=t vv^T`,                                                       (5.1)

where `v` is a flat Walsh vector perpendicular to `r`. Its nonzero spectrum is

`{1,+1,-1,t}`                                                     (5.2)

(with `t=0` omitted), so the owner target holds for **every real `t`** because `{1,+1,-1}` remain.

For the partner theorem,

`Xi_h=t^2(m-2)/m`,                                                 (5.3)

so at `m=64,t=1` its completed Schur/E2 receiver gives

`||p_Q||_infinity <=15.5706812238`.                               (5.4)

The present theorem has `tau=1`, `s=1`, and the favorable physical pivot has `|ell_1|=1`. The sharper form (3.15) therefore gives, **uniformly for every real `t`**,

`boxed:
 ||p_Q||_infinity <=2^(9/4)=4.7568284601... .`                    (5.5)

Thus the same target-valid dense leaf-curvature family is paid continuously in the coefficient parameter `t` at the level of the essential-height estimate, including the partner's `Xi_h->0` endpoint. This does not assert continuity of the output density.

More importantly, (3.16) continues to hold if the rank-one cross in (5.1) is replaced by an arbitrary physical two-column cross block having the same nonzero kernel-star `q`; the partner theorem's rank-one-cross setup is not needed for this exact-pair payment.

## 6. Required pinned mixed-hub theorem applied to an actual source-coordinate star

Let `m>=8` be a Walsh size and choose flat orthonormal physical-coordinate vectors `c,v_1,v_2 in R^m`. Let `X_0` be one literal physical hub, `Y` the `m` original leaf coordinates, and `Z` any further disjoint original-coordinate bank. Consider

`F = 2 X_0 <c,Y>
    + <v_1,Y>^2 + <v_2,Y>^2
    +2 X_0 u^T Z +2 Y^T M Z + Z^T T Z + affine`,                 (6.1)

where `u,M,T` are completely arbitrary and `T` may be dense, indefinite and large.

Condition on `Z`. The active leaf block is exactly

`v_1 v_1^T+v_2 v_2^T`,                                           (6.2)

and the mixed physical rows are

`rho_i=((v_1)_i,(v_2)_i,c_i)`.                                   (6.3)

Their Gram is `I_3`, while every physical leverage is `3/m<=1/2`. The pinned completed Theorem H therefore gives

`|phi_F(t)| <=8 pi^2 |t|^(-2)`.                                  (6.4)

Exact integration of `min(1,8 pi^2 |t|^(-2))` and Fourier inversion yields

`boxed:
 ||p_F||_infinity <=4 sqrt(2)=5.6568542495... ,`                  (6.5)

and

`boxed: P{F in J}<=4sqrt(2)|J|.`                                  (6.6)

The fixed principal coefficient block on `span{X_0,c,v_1,v_2}` has spectrum

`{1,-1,1,1}`,                                                     (6.7)

so it already satisfies the exact target. Arbitrary extension by the `Z` block preserves at least three eigenvalues `>=1` by interlacing. The dense same-side rank-two leaf curvature is retained in the original source coordinates, and all arbitrary `Z`-side curvature/couplings remain inside the conditioned phase. There is no decoupling square root.

This is the required completed pinned result applied to a real target inequality.

## 7. Why the exact-pair proof cannot simply be perturbed to `det B !=0`

There is a sharp method obstruction. Let `0<delta<=1` and let `X,Y,Z,W` be independent unit-uniform cap-one variables. Define

`Q_delta = X^2 + delta (Y+Z/delta)^2 + W^2
         = X^2 + delta Y^2 +2YZ + delta^(-1)Z^2 +W^2.`            (7.1)

Its coefficient matrix has spectrum exactly

`{1,1,delta+delta^(-1),0}`,                                      (7.2)

so it is target-valid for every `delta>0`. The literal physical pair `H={X,Y}` has core

`B_delta=diag(1,delta)`, `det B_delta=delta ->0`.                 (7.3)

After completing the physical square `X^2`, condition on the third large-square coordinate `W=w`. The residual is

`R_w=delta(Y+Z/delta)^2+w^2`.                                    (7.4)

At the output level `s=w^2`,

`E|R_w-s|^(-1/2)
 =delta^(-1/2) E|Y+Z/delta|^(-1)
 =infinity.`                                                       (7.5)

Indeed the density of `Y+Z/delta` is positive in a neighborhood of zero (for these uniforms it equals `delta` near zero), so the `|x|^(-1)` integral diverges logarithmically.

Thus the exact-rank-one half-Riesz interface does **not** admit a uniform perturbative extension merely because the residual hub-square coefficient `delta` is small. In this target-valid family the failure is specifically caused by conditioning away the third large square before the half-Riesz step. The full law is not a counterexample: writing `U=sqrt(delta)Y+Z/sqrt(delta)`, `U` is independent of `(X,W)` and has density cap at most one, so `Q_delta=X^2+U^2+W^2` is itself a paid positive three-square form.

This is why the next implication must spend the third resource jointly before worst slicing.

## 8. Counterexample status and exact remaining gap

The required pinned counterexample search still reports no valid counterexample to unrestricted QFORM, and this run found none. The family (7.1) is a counterexample only to the **methodological shortcut** “small nonzero residual hub square can be treated as a perturbation of the exact-zero half-Riesz receiver.”

The exact singular-pair overlap-two branch is now analytically cleaner:

- exact rank-one physical pair + nonzero kernel-star: paid by (3.16) for arbitrary cross rank and arbitrary leaf curvature;
- macroscopic overlap-two mass: paid by (4.4), with deterioration only through a tiny nonzero pair eigenvalue `|tau|`;
- genuinely near-rank-one pair: must retain a third spectral resource jointly, because the half-Riesz worst-slice interface can be infinite even in a target-valid family.

The first unpaid implication remains `QFORM-NEARRANKONE-PAIR-THIRDRESOURCE-BEFORE-HALFRIESZ-v1`. Full QFORM and full-target continuity remain OPEN.
