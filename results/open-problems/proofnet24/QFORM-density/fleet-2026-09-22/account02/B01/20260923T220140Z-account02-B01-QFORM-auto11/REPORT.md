# account02/B01 — rank-one latent crossing: transverse same-bank curvature can be re-cut into rank two

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T220140Z-account02-B01-qform-auto11`  
Role: oscillatory replacement / complementary constructions / source-valid obstructions  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN**

## 1. Control and correction boundary


The exact target remains the universal bounded-density conjecture for `X^T A X` under independent real cap-one densities and `s_3(A)>=1`.

## 2. Source-pinned inputs actually spent

1. Required source package at
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
   I use its proved square peel
   `D(Q) <= |a|^{-1/2} H_{1/2}(R)`
   after a literal original-coordinate completion, and its fractional-potential philosophy. The same source records that the three-/five-volume routes require positive `Z_3`/`Z_5` and explicitly preserves the phase-aligned obstruction to scalar pointwise Fresnel decay.

2. Previous account02/B01 state pinned at
   `yspennstate/math-open-problems@1760a61be07cc456da3f69e703d025e74c3877eb`.
   The already proved bilateral rank-two projected-Plancherel receiver is used in the form
   `H_{1/2}(R) <= 8 Delta^{-1/4}`
   whenever an original-coordinate physical cross block has rank two and singular-value product `Delta=s_1 s_2>0`; arbitrary same-bank quadratic curvature and affine terms remain present.

3. Newest designated partner account03/B01 state available at sign-in:
   `yspennstate/math-open-problems@b028a41e2e0b653c75740c740351aeef537e313f`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T212842Z-auto11/REPORT.md`.
   Its high-diagonal theorem pays every second scalar-Schur pivot `>=1/64` by `<3444.312`; otherwise it produces a fixed-energy original-coordinate scalar-Schur cross packet `N` with `||N||_F^2>3969/8192`. The preceding account02/B01 run showed that exact `W_2=0` forces this `N` to have rank at most two and paid the branch `s_2(N)>=1/256`, leaving the rank-one-dominant endpoint.

## 3. Structural lemma: an exact rank-one cross in diagonal-plus-rank-two geometry

Let

`H = D + U C U^T`,

where `D` is diagonal, `U` has two columns, and `C` is a real symmetric invertible `2x2` matrix. Let `I,J` be disjoint original-coordinate banks and suppose

`N=H[I,J]=U_I C U_J^T`

is nonzero of exact rank one.

If both `U_I` and `U_J` had column rank two, then, because `C` is invertible, the product `U_I C U_J^T` would have rank two. Hence at least one side has latent rank one. After swapping `I,J` if needed, assume `rank U_I=1`.

Make only an algebraic change of basis in the two-dimensional latent coefficient space (no random-variable rotation). Then

`U_I=[u,0]`,  `U_J=[v,w]`,

and

`C=[[alpha,beta],[beta,gamma]]`,  `det C !=0`.

All vectors here are coefficient vectors on literal original-coordinate banks.

## 4. New theorem — `QFORM-RANK1-LATENT-TRANSVERSE-WEDGE-v1`

Partition the original coordinates of `J` as `J=J_1 disjoint_union J_2`. Put

`T(J_1,J_2)
 = |det C| ||u||_2 ||w_{J_1}||_2 ||v_{J_2} wedge w_{J_2}||`,

where

`||v_{J_2} wedge w_{J_2}||^2
 = sum_{j<k in J_2} (v_j w_k-v_k w_j)^2`.

### Theorem 4.1

Assume a literal outer original coordinate has already been completed as

`Q=a(X_0+h)^2+R`,  `a!=0`,

and the quadratic coefficient of `R` is `H` above. If `T(J_1,J_2)>0` for one partition, then

`H_{1/2}(R) <= 8 T(J_1,J_2)^(-1/4)`

and therefore

`boxed: ||p_Q||_infinity
 <= 8 |a|^(-1/2) T(J_1,J_2)^(-1/4).`

No continuity claim is attached to this theorem.

### Proof

On the re-cut

`(I union J_1) | J_2`,

the diagonal matrix `D` contributes no cross term. The low-rank cross matrix is exactly

`M = A_1 B_1^T + A_2 B_2^T`,

with

`A_1=[u;v_{J_1}]`,
`A_2=[0;w_{J_1}]`,
`B_1=alpha v_{J_2}+beta w_{J_2}`,
`B_2=beta v_{J_2}+gamma w_{J_2}`.

For any rank-at-most-two matrix `ab^T+cd^T`, Cauchy-Binet gives

`e_2(M^T M)=||a wedge c||^2 ||b wedge d||^2`.

Here

`||A_1 wedge A_2|| >= ||u|| ||w_{J_1}||`,

because the `u` coordinates and `w_{J_1}` coordinates are disjoint, while bilinearity of the exterior product gives the exact identity

`B_1 wedge B_2 = (det C) (v_{J_2} wedge w_{J_2})`.

Thus the singular-value product of the physical cross block satisfies

`Delta(M)=s_1(M)s_2(M)=sqrt(e_2(M^T M)) >= T(J_1,J_2)`.

The completed bilateral projected-Plancherel theorem therefore gives

`H_{1/2}(R) <=8 Delta(M)^(-1/4) <=8 T(J_1,J_2)^(-1/4)`.

Finally, the square-peel theorem from the required 20260922T211500Z Fourier report gives

`||p_Q||_infinity <= |a|^(-1/2) H_{1/2}(R)`.

This proves the result. Every probabilistic operation is on literal original-coordinate banks. QED.

## 5. Averaged partition currency and the exact obstruction

Define the original-coordinate triple currency

`Zeta_3(v,w)
 = sum_{l,j,k distinct, j<k}
     w_l^2 (v_j w_k-v_k w_j)^2.`

Color each coordinate of `J` independently into `J_1,J_2` with probability `1/2`. Then

`E[ ||w_{J_1}||^2 ||v_{J_2} wedge w_{J_2}||^2 ]
 = Zeta_3(v,w)/8`,

because a term indexed by three distinct coordinates survives exactly when `l in J_1` and `j,k in J_2`, an event of probability `1/8`.

Hence some deterministic partition satisfies

`T(J_1,J_2)
 >= |det C| ||u|| (Zeta_3/8)^(1/2)`.

Theorem 4.1 therefore yields the averaged-frequency/rearrangement estimate

`boxed:
||p_Q||_infinity
 <= 8*8^(1/8) |a|^(-1/2)
    (|det C| ||u||)^(-1/4) Zeta_3(v,w)^(-1/8).`

Numerically `8*8^(1/8)=10.3747164372...`. In the newest partner's high-diagonal branch, `|a|>=1/64`, so this becomes

`boxed:
||p_Q||_infinity
 <=82.997732
   (|det C| ||u||)^(-1/4) Zeta_3(v,w)^(-1/8).`

This is a genuine new payment inside the exact-rank-one endpoint; it does not pay any tiny pair determinant or tiny second singular value.

The zero set of this currency is sharply localized. If `rank U_J=2`, so that `v,w` are linearly independent, and `Zeta_3(v,w)=0`, then `w` is supported on at most two original coordinates. Indeed, if `w` had at least three nonzero coordinates, for every pair `j!=k` one could choose a third support coordinate `l` distinct from both. The vanishing of the corresponding summand forces `v_j w_k-v_k w_j=0` for every pair, making `v,w` collinear, contradiction.

Thus for an exact rank-one cross with genuinely two-dimensional latent geometry on the opposite bank, diffuse transverse same-bank leakage is no longer a survivor: it can be re-cut into a physical rank-two packet and paid by half-Riesz. Failure forces the transverse latent direction onto at most two literal coordinates.

## 6. Concrete exact-W2 target family: same-bank leakage paid at 9.514

This is not merely an abstract compiler. Let `m` be even and let `w=(1/sqrt(m),...,1/sqrt(m))` on original coordinates `Y_1,...,Y_m`. Use original coordinates

`p_1,p_2,x_0,x,y,Y_1,...,Y_m`.

Let `D` be diagonal with

`D_{x_0}=1`, `D_x=D_y=-1`,

and all other diagonal entries zero. Let `U` have two columns with rows

`U_{p_1}=(1,0)`, `U_{p_2}=(0,1)`,
`U_x=U_y=(1,0)`,
`U_{Y_r}=(0,w_r)`,
`U_{x_0}=0`,

and set

`A=D+UU^T`.

The physical pair `P={p_1,p_2}` has `A_PP=I_2`. Its exact pair Schur complement is

`A/P = D_{P^c}`,

which is diagonal. Hence this family has **exact `W_2(P)=0`**.

Its spectrum contains, independently of `m`,

`{-1, 1-sqrt(2), 1, 2, 1+sqrt(2)}`

plus zeros, so at least four eigenvalues have absolute value at least one. It is an actual owner-target family.

Condition on `p_1,p_2`; their contributions become affine terms. The remaining quadratic part is

`Q_cond = x_0^2 + 2xy + (w dot Y)^2`.

The natural cut `I={x}`, `J={y,Y_1,...,Y_m}` has exact rank-one cross, so every third- and fifth-volume currency on that cut is zero. Split the `Y` bank evenly, take

`J_1={Y_1,...,Y_{m/2}}`,
`J_2={y,Y_{m/2+1},...,Y_m}`.

Then the re-cut cross block has singular values `1` and `1/2`, hence

`Delta=1/2`.

The rank-two half-Riesz receiver plus the required square peel gives the explicit full-target bound

`boxed:
||p_{X^T A X}||_infinity
 <=8 (1/2)^(-1/4)
 =8*2^(1/4)
 =9.513656921... .`

All affine terms generated by conditioning are harmless in the cited receiver. This family also gives a concrete obstruction to trying to finish the branch with D/D'/D5 alone: the natural packet is rank one and the successful re-cut is rank two, so `Z_3=Z_5=0` in both places. The payment is genuinely fractional-potential/rank-two, not a volume theorem in disguise.

## 7. Application to the newest account03/B01 routing theorem

The newest partner theorem says that from `s_3(A)>=1` and an outer physical diagonal `|a|>=1/64`, either a non-small second scalar-Schur pivot is already paid by

`||p_Q||_infinity <3444.312`,

or one reaches a fixed-energy original-coordinate Schur cross packet. In exact `W_2=0`, the preceding account02/B01 closure lemma makes that packet rank at most two; the previous run paid `s_2>=1/256` and isolated the rank-one-dominant tube.

Theorem 4.1 now pays the **exact-rank-one** subcase whenever the second latent direction has positive triple currency `Zeta_3`. Quantitatively, with `|a|>=1/64`,

`||p_Q||_infinity
 <=82.997732 (|det C| ||u||)^(-1/4) Zeta_3^(-1/8).`

Therefore, in the exact-rank-one limit of the partner's survivor, a genuinely two-dimensional opposite-bank latent geometry can remain unpaid only if its transverse latent coefficient vector is supported on at most two original coordinates. This is a strict structural reduction of the first unpaid implication.

On the concrete family in Section 6, the partner's theorem is also valid (there are large second pivots), giving its universal `<3444.312` branch, while the new re-cut estimate gives `9.514`; thus the partner result was applied to an actual target inequality, not only summarized.

## 8. What is still unpaid

The first unpaid implication is now

`QFORM-W2ZERO-RANK1-FINITELEAK-OR-QUANTITATIVE-ROUTING-v1`.

Starting from the rank-one-dominant scalar-Schur tube, extend the exact theorem above quantitatively to `0<s_2<1/256`, or route the exact-rank-one zero-triple-currency cases. After the new theorem, those exact cases are confined to:

1. global latent rank one (`rank C=1`);
2. both bank restrictions latent-rank one;
3. an invertible latent rank-two geometry whose transverse direction is supported on at most two literal original coordinates (up to swapping the banks).

These are finite-coordinate / two-aggregate obstructions, not diffuse same-bank leakage. They should be tested against the required source's proved bounded-dimensional zero-diagonal core and the existing rank-one-bilinear-plus-square / physical-pair receivers before any tiny determinant is inverted.

Full QFORM is not proved or disproved here.

## 9. Execution facts

Authenticated repository retrieval was active. A receiver-memory query was attempted but supplied no QFORM-specific state used in the proof, so execution remains `WITHOUT_VERIFIED_BRAIN`. Model self-report: `GPT-5.6 Sol`. Configured/self-reported thinking level: `UNKNOWN`. Provider reasoning-token and thinking-time telemetry: `null/not exposed`. Elapsed work is recorded separately and includes tool/network/publication/readback overhead; it is not pure thinking.
