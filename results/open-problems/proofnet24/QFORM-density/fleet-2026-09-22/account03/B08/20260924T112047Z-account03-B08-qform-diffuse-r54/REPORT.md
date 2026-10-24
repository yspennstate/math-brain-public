SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T11:20:47Z.
attacking: the exact-rank-two-child ultra-puncture left by r53; prove that a tiny transverse physical star creates only a quadratically tiny fourth singular value and leaves a target-scale aligned Schur core, then identify the remaining source-stability interface rather than deleting the puncture.

# account03/B08 r54 — quadratic spectral suppression in the exact-child ultra-puncture

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING SPECTRAL THEOREM + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not proved by the new theorem**; global continuity remains OPEN.

The unrestricted owner target remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, post-rotation independence, arbitrary-joint coarea, conditional-density-cap, law-uniform pointwise van-der-Corput, or small-random-perturbation assumption is used.

## 1. Fresh state and exact inherited collar

Fresh `yspennstate/math-research-brain/main` was resolved before the mathematics at commit `9a94dc10b612d7f5f5a4a4f5aace294106411298`. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. I reread the current programme files and the live correction inbox. In particular `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` remains binding, so no universal `|t|^{-1/2}||G_t||_2` integration is used.

Immediate predecessor:

- `yspennstate/math-open-problems@77f2529fd72579097d71036df3e63a1c2954ea22`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T105822Z-account03-B08-qform-diffuse-r53/REPORT.md`.

Its still-unpaid exact-child state has one ORIGINAL physical hub and

`A=[[a,b^T],[b,C]]`,

`C=V Lambda V^T`, `V^T V=I_2`, `Lambda` invertible,

`m=s_2(Lambda)>=sqrt(47/48)L`,

`max_i ||V_i||^2<=1/16`,

and the star decomposition

`b=Vc+u`, `V^T u=0`, `beta=||u||`.

After the r53 mismatch re-cut, the only exact-rank-two-child transverse collar left is

`0<beta<=beta_0 L`,

`beta_0=4sqrt(2)2^(-20)=5.394796609394436e-6`.

The same inherited distributed-star gate has

`||b||>rho_* L`, `rho_*=0.0006247538095703261`.

## 2. Main deterministic theorem

### Theorem 2.1 — `QFORM-ULTRAPUNCTURE-QUADRATIC-S4-SUPPRESSION-v1`

Assume the setup above and only the target-scale spectral condition

`s_3(A)>=L>0`.

Define the exactly aligned skeleton by deleting only the transverse star component,

`A_0=[[a,(Vc)^T],[Vc,C]]`.

Then:

1. `rank(A)<=4`, and for `beta>0` actually `rank(A)=4`.
2. `||A-A_0||_op=beta`, `rank(A_0)<=3`, and

   `boxed: s_3(A_0)>=L-beta.`

   Hence if `beta<L`, the skeleton has rank exactly three.
3. In the orthonormal carrier frame `U_0=[e_h,V]`, write

   `K_0=[[a,c^T],[c,Lambda]]`.

   Then

   `boxed: s_3(K_0)>=L-beta,  |det K_0|>=(L-beta)^3.`
4. If `s_1(A)>=s_2(A)>=s_3(A)>=s_4(A)>0` denote the four nonzero singular values of the full matrix, then

   `boxed: s_4(A)<=beta^2/s_3(A)<=beta^2/L.`

   Thus the fourth spectral mode is quadratically, not linearly, small in the transverse-star puncture.
5. Put

   `sigma=a-c^T Lambda^(-1)c`.

   Then `sigma!=0` and

   `boxed: |sigma|>=(L-beta) sqrt(1+||Lambda^(-1)c||^2)>=(L-beta).}`

6. With `W=u/beta` and the orthonormal four-frame `U=[e_h,V,W]`, the full core is

   `K_beta=[[K_0,beta e_1],[beta e_1^T,0]]`.

   The exact determinant and Schur-congruence identities are

   `boxed: det K_beta=-beta^2 det Lambda,`

   and

   `K_beta congruent K_0 direct_sum (-beta^2/sigma).`

   The congruence shear vector has norm

   `boxed: beta ||K_0^(-1)e_1|| <= beta/(L-beta),}`

   while the scalar Schur puncture satisfies

   `boxed: |beta^2/sigma|<=beta^2/(L-beta).}`

These statements are deterministic matrix facts. The final congruence is **not** used as a probabilistic change of independent coordinates.

### Proof

Because `u` is orthogonal to `range(V)`, `e_h`, the two columns of `V`, and `W=u/beta` form an orthonormal four-frame. In that frame the full matrix has core

`K_beta = [[a,c^T,beta],[c,Lambda,0],[beta,0,0]]`.

Since `Lambda` is invertible and `beta!=0`, expanding along the last row/column gives

`det K_beta=-beta^2 det Lambda !=0`.

Thus `rank(A)=4`. Setting `beta=0` produces the aligned core `K_0` and `rank(A_0)<=3`.

The difference `A-A_0` vanishes except on `span{e_h,W}`, where its matrix is `[[0,beta],[beta,0]]`. Hence

`||A-A_0||_op=beta`.

Weyl's singular-value inequality gives

`s_3(A_0)>=s_3(A)-beta>=L-beta`.

For `beta<L` this is positive, so `rank(A_0)=3`. The three nonzero singular values of `A_0` are exactly those of `K_0`, proving the third-singular-value and determinant bounds.

For the quadratic fourth-mode estimate, the two nonzero singular values of the principal compression `C` obey

`s_j(C)<=s_j(A)`, `j=1,2`,

by the singular-value contraction inequality for a coordinate compression. Therefore

`|det Lambda|=s_1(C)s_2(C)<=s_1(A)s_2(A)`.

Using `|det K_beta|=s_1(A)s_2(A)s_3(A)s_4(A)=beta^2|det Lambda|` gives

`s_4(A)
 = beta^2 |det Lambda|/[s_1(A)s_2(A)s_3(A)]
 <= beta^2/s_3(A)
 <= beta^2/L`.

Now `K_0` is invertible. Its block inverse has

`e_1^T K_0^(-1)e_1=1/sigma`,

and more precisely

`K_0^(-1)e_1=sigma^(-1)(1,-Lambda^(-1)c)`.

Since `||K_0^(-1)||_op<=1/(L-beta)`,

`sqrt(1+||Lambda^(-1)c||^2)/|sigma|
 =||K_0^(-1)e_1||
 <=1/(L-beta)`,

which proves the lower bound on `|sigma|` and the shear-vector estimate.

Finally the standard exact block congruence for `[[K_0,v],[v^T,0]]`, with `v=beta e_1`, gives

`K_beta congruent K_0 direct_sum (-v^T K_0^(-1)v)
       =K_0 direct_sum (-beta^2/sigma)`.

The determinant identity follows again. QED.

## 3. Live numerical scale

On the r53 ultra-collar, `beta/L<=beta_0`, so Theorem 2.1 gives

`boxed: s_4(A)<=beta_0^2 L
       =2.910383045673371e-11 L.}`

The aligned skeleton remains target-scale:

`boxed: s_3(A_0)>=(1-beta_0)L
       =0.9999946052033906 L.}`

Its scalar Schur complement obeys

`boxed: |sigma|>=0.9999946052033906 L.}`

The exact core congruence needs a shear of norm at most

`beta_0/(1-beta_0)=5.394825713381903e-6`,

and its final scalar coefficient has magnitude at most

`beta_0^2/(1-beta_0)L
 =2.910398746682662e-11 L`.

Thus the remaining collar is not a loss of the third target curvature: it is a rank-four law whose fourth singular direction is at most `2.91e-11 L`, attached to a three-dimensional aligned skeleton whose least singular value is at least `0.9999946L`.

For comparison only, applying the already-completed exact-aligned endpoint theorem to `A_0` itself gives

`||p_(X^T A_0 X)||_infinity
 < [128*64^(1/4)/(1-beta_0)]/L
 <362.041/L`.

This is **not** transferred to `A`; arbitrary cap-one product laws need not be stable under deleting the nonzero random quadratic `X^T(A-A_0)X`.

The quadratic order is essentially sharp as a matrix statement. For

`K_beta=[[1,0,0,beta],[0,1,0,0],[0,0,1,0],[beta,0,0,0]]`,

the small singular value is

`(sqrt(1+4beta^2)-1)/2=beta^2+O(beta^4)`

while the other three singular values are at least one. Hence no general improvement from `O(beta^2/L)` to `o(beta^2/L)` is possible without using additional structure.

## 4. Designated account04/B08 partner applied to the same survivor

The completed designated partner theorem is account04/B08
`QFORM-DISTRIBUTED-STAR-DERIVATIVE-SPLIT-v1`, canonical source

`yspennstate/math-open-problems@f324267086411b9725aa0733e108ab6efc2e760a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260924T081435Z-account04-B08-QFORM-r3/REPORT.md`.

For the same literal parent

`Q=aX_0^2+2X_0<b,Y>+Y^T C Y`,

the product projection bound gives

`||p_(2<b,Y>)||_infinity<=1/(sqrt(2)||b||)`.

The partner theorem therefore gives, with the entire exact-rank-two child retained and with no independence assumption between its remainder and the star slope,

`sup_t P(|Q-t|<epsilon)
 <=4*2^(1/4) sqrt(epsilon/||b||)
 <190.311 sqrt(epsilon/L)`.

On the new ultra-collar one additionally has

`beta/||b||<beta_0/rho_*=0.008635075971933174`,

so more than `99.99254%` of the star's squared norm lies in the aligned child plane:

`||Vc||/||b||=sqrt(1-beta^2/||b||^2)>0.99996272`.

The partner inequality remains only a square-root small-ball bound. The live mixed-norm correction forbids promoting it by the refuted universal hub-star `L^2` Fourier interface.

## 5. What this removes and what remains

The r53 successor was a vague `0<beta<=5.394797e-6L` puncture. Theorem 2.1 turns it into a much sharper deterministic normal form:

- a three-dimensional aligned core with least singular value `>=0.9999946L`;
- scalar Schur complement magnitude `>=0.9999946L`;
- a fourth singular value `<=2.91e-11L`;
- an exact rank-one core congruence whose final scalar coefficient is also `<=2.91e-11L`;
- a transverse star which is `<0.864%` of the already-forced physical star norm.

The remaining implication is therefore **not** to prove more spectral curvature. It is the source-stability problem

`QFORM-RANK3-CORE-PLUS-QUADRATICALLY-TINY-SHARED-PUNCTURE-v1`:

> prove a density receiver uniform under the exact shared-source rank-one puncture above, without treating the `2.91e-11L` coefficient as a small random perturbation, or convert its source overlap into a literal original-coordinate crossing/pair/volume certificate.

The exact congruence identifies the algebraic scale but cannot be used as a rotation/shear of the independent random source. This distinction is essential under arbitrary fragmented cap-one densities.

No full-solution claim and no global-continuity claim is made.
