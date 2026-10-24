SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-24T07:06:24Z.
attacking: spend the full third-compound inequality rather than only s3, split the unpaid rank-two crossing into a two-channel cancellation branch or a Frobenius-thin rank-two branch, and intersect the result with the newest account03/B08 punctured double-alignment router.

# account02/B08 r35 — full third-compound double-cancellation / thin-rank-two router

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING HYBRID ROUTER + EXACT TARGET-VALID DOUBLE-CANCELLATION STRESS FAMILY / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.

Throughout, `X=(X_i)` has independent coordinates with arbitrary densities bounded by one. No moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is used. Every cut below is a cut of the original physical coordinates. Continuity is asserted only on branches paid by an integrable Fourier envelope.

## 1. First unpaid implication

`QFORM-TWOCHANNEL-CANCELLATION-OR-FROBENIUS-R2-CARRIER-COMPILER-v1`.

In the diffuse-top-three chamber from r34, let

`A_3=U Lambda U^T`, `B=A[S,T]`, `B_0=A_3[S,T]`, `C=(A-A_3)[S,T]`,

where the physical balanced cut satisfies

`U_S^T U_S >= (3/8) I_3`, `U_T^T U_T >= (3/8) I_3`.

Write

`C_* = 197.7780678260685`,
`C_3 = 6^(4/3) = 10.902723556992836...`,
`theta = C_3/C_* = 0.05512604949999305...`.

The completed marginal-free third-compound receiver gives

`||p_Q||_infinity <= C_3 e_3(BB^T)^(-1/6)`.

Hence failure of the benchmark `C_*/L` forces

`e_3(BB^T)^(1/6) < theta L`.                                      (1.1)

The new point is to retain all of (1.1), not only its consequence `s_3(B)<theta L`.

## 2. Full-compound Frobenius identity

Let `s_1>=s_2>=...` be the singular values of `B`. By the elementary-symmetric expansion,

`e_3(BB^T)=sum_{i<j<k} s_i^2 s_j^2 s_k^2`

and therefore

`e_3(BB^T) >= s_1^2 s_2^2 sum_{k>=3} s_k^2`.                     (2.1)

Since

`dist_F(B,{rank<=2})^2 = sum_{k>=3}s_k^2`,

(1.1)-(2.1) imply the scale-invariant estimate

`boxed: s_1(B)s_2(B) dist_F(B,rank<=2) < theta^3 L^3.`            (2.2)

This is strictly stronger than the previous operator-norm rank-two tube whenever the first two crossing directions have target-scale size.

## 3. Main dichotomy at alpha=1/8

Set `alpha=1/8`.

### Branch A — near-rank-one literal crossing gives two signed cancellation channels

Assume

`s_2(B)<L/8`.                                                       (3.1)

Let `v_1` be a top right singular vector of `B`. Since `range(U_T)` has dimension three,

`E := range(U_T) intersect v_1^perp`

has dimension at least two. For every unit `x in E`,

`||Bx|| <= s_2(B) < L/8`.                                         (3.2)

The nonzero singular values of

`B_0=U_S Lambda U_T^T`

are at least `(3/8)L`, because both restricted Gram matrices dominate `(3/8)I_3` and the three selected eigenvalues have modulus at least `L`. Thus for every unit `x in range(U_T)`,

`||B_0x|| >= (3/8)L`.                                             (3.3)

Since `C=B-B_0`, (3.2)-(3.3) give

`boxed: ||Cx|| > L/4 for every unit x in E.`                      (3.4)

Equivalently, by the min-max principle,

`boxed: s_2(C) > L/4.`                                            (3.5)

Moreover, choosing any orthonormal `x_1,x_2 in E` and

`y_j=B_0x_j/||B_0x_j||`,

one has the signed inequalities

`boxed: y_j^T C x_j < -L/4, j=1,2.`                               (3.6)

Finally, a best rank-one approximation `B_1` satisfies `||B-B_1||op=s_2(B)<L/8`, while `rank(B_1-B_0)<=4`; hence

`boxed: dist_op(C,{rank<=4}) < L/8.`                              (3.7)

Thus an unpaid near-rank-one literal crossing is not merely cancelled in one top-three direction: complementary curvature must carry two target-scale signed cancellation channels.

### Branch B — two target-scale literal crossing directions force a very thin Frobenius rank-two tube

Assume instead

`s_2(B)>=L/8`.                                                      (3.8)

Then `s_1(B)>=s_2(B)>=L/8`, so (2.2) yields

`dist_F(B,{rank<=2}) < 64 theta^3 L`

with

`delta_F := 64 theta^3 = 0.010721377460082268...`.                (3.9)

Hence

`boxed: dist_F(B,{rank<=2}) < 0.010722 L.`                         (3.10)

If `B_2` is a best rank-two approximation, then

`C=(B_2-B_0)+(B-B_2)`

and `rank(B_2-B_0)<=5`, so

`boxed: dist_F(C,{rank<=5}) < 0.010722 L.`                         (3.11)

This is more than five times thinner than the previous operator-norm error `theta L=0.055126...L`, and it is already below the `L/64` alignment scale used by the newest designated partner.

The previous signed one-channel certificate remains available in this branch: there exist unit
`x in range(U_T)`, `y in range(U_S)` with

`boxed: y^T C x < -(3/8-theta)L`
`                 = -0.31987395050000694... L.`                   (3.12)

## 4. Actual spectral/localized gates retained

Nothing in Sections 2-3 weakens the actual gates inherited from the newest localized/diffuse router. Therefore failure of the `197.779/L` payment still implies simultaneously

`boxed: s_4(A) > 0.31987395050000694 L`,                           (4.1)

and for

`P_*=1_{|A|>=0.0049980304765626085 L}`,

`boxed: max_i (P_*)_ii > 1/32`,                                   (4.2)

and some original physical coordinate `k` satisfies

`boxed: max{|A_kk|, ||A[k,-k]||_2}`
`       >0.0006247538095703261 L.`                                (4.3)

Thus the live diffuse hybrid is now split into two explicit packets:

1. a near-rank-one literal crossing with **two** signed target-scale complementary cancellation directions and a rank-four complementary tube; or
2. a literal crossing with two target-scale singular directions but Frobenius tail below `0.010722L`, together with a Frobenius-thin rank-five complementary tube and a signed `0.31987L` cancellation.

Both packets still carry (4.1)-(4.3).

## 5. Newest designated partner: punctured double alignment

The newest completed compatible `account03/B08` theorem is

`QFORM-PUNCTURED-CROSSSTAR-DOUBLEALIGN-ROUTER-v1`,

canonical mathematics `yspennstate/math-open-problems@19c12072f7e67266ce894042034bcabb9c376bea`.

On its inherited one-hub, diffuse-top-two-child aligned-star collar it proves the following product-safe original-coordinate router. If the child puncture `r=s_3(C_child)` satisfies `r>=L/4096`, then either

`||p_Q||_infinity<262144/L`, `p_Q in C_0`,

or an original child row obeys

`max{|(C_child)_kk|,||(C_child)[k,-k]||_2}>L/2^21`.

If instead `0<r<L/4096`, a physical child half-cut has

`s_2(D)>=0.31959453358755213 L`.

The partner's exterior-algebra lemma says, for a physical star half `z`,

`e_3([z^T;D][z^T;D]^T) >= s_1(D)^2 s_2(D)^2 dist(z,R_2(D))^2`.

Consequently any star-half distance at least `L/64` gives

`||p_Q||_infinity < 93.296/L`, `p_Q in C_0`; otherwise both hub-augmented literal crossings lie within `0.015626908L` in operator norm of rank at most two.

This consumes the designated partner at its exact scope. Intersected with Branch B above, the crossing tail `0.010722L` is already below the partner's `1/64` alignment scale. Hence any overlapping unpaid one-hub realization is forced into the partner's **double-aligned rank-two tube**, or returns a second localized child row. Branch A supplies a distinct two-channel cancellation packet that the partner theorem does not subsume.

## 6. Exact target-valid double-cancellation stress family

The two-channel packet is nonempty and cannot be replaced by a claim that a localized row must interact with the crossing.

Let `m=2^q>=512` and work on `G=F_2^q`. Let `u_g` denote the normalized Walsh character

`u_g(x)=m^(-1/2)(-1)^{g dot x}`.

Choose independent labels `e_1,e_2,e_3` and define

`u_1=u_0`, `u_2=u_{e_1}`, `u_3=u_{e_2}`,
`chi(x)=(-1)^{e_3 dot x}`,
`v_2=chi .* u_2=u_{e_1+e_3}`,
`v_3=chi .* u_3=u_{e_2+e_3}`.

The five normalized Walsh vectors `u_1,u_2,u_3,v_2,v_3` are orthonormal. Add a separate physical coordinate `z` and set

`A_m = L(u_1u_1^T+u_2u_2^T+u_3u_3^T+v_2v_2^T+v_3v_3^T)
       +(L/2)e_z e_z^T`.                                          (6.1)

Its nonzero spectrum is exactly

`boxed: {L,L,L,L,L,L/2}.`                                        (6.2)

In particular it satisfies the exact target. The chosen leading-three frame has physical leverage `3/m` on every Walsh coordinate and zero at `z`, hence is diffuse.

Take the physical half-cut

`S={x:chi(x)=+1}`, `T={x:chi(x)=-1}`.

On `S x T`, multiplication by `chi` changes sign, so the `v_2v_2^T` crossing cancels the `u_2u_2^T` crossing exactly, and `v_3v_3^T` cancels `u_3u_3^T` exactly. Therefore

`B=A_m[S,T]=L u_{1,S}u_{1,T}^T`,

so the literal crossing has singular values

`boxed: {L/2,0,0,...}.`                                           (6.3)

Meanwhile the selected top-three crossing has singular values

`{L/2,L/2,L/2}`,

and the complementary crossing equals

`C=L(v_{2,S}v_{2,T}^T+v_{3,S}v_{3,T}^T)`

with singular values

`boxed: {L/2,L/2,0,...}.`                                         (6.4)

Thus the two signed cancellation channels have magnitude exactly `L/2`, stronger than the universal `L/4` certificate. The separate coordinate `z` has `A_zz=L/2` and is completely disconnected from the crossing, so the localized row need not help resolve the two-channel cancellation.

Every physical `2 x 2` principal block is weak. For two Walsh coordinates, each diagonal entry is `5L/m`, hence the smaller singular value is at most `5L/m`; for a block containing `z`, the smaller singular value is again `5L/m`. Therefore for `m>=512`,

`boxed: sigma_min(A_m[{i,j},{i,j}]) <= 5L/m < L/64`               (6.5)

for every physical pair.

This family is a proof-mechanism obstruction, not a QFORM counterexample.

## 7. Required fixed-source theorem applied to the obstruction

The required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was read in `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed generalized rank-`r` Fresnel--Brascamp--Lieb theorem states that for

`A=D+R Lambda R^T`

with physical leverage of the rank-`r` frame at most `1/2`, arbitrary diagonal twist `D`, arbitrary affine terms, and arbitrary independent cap-one product sources,

`|phi_Q(t)| <= (4 pi)^(r/2)|t|^(-r/2) prod_k |lambda_k|^(-1/2)`

and, for `r>2`,

`||p_Q||_infinity <= [4r/(r-2)] prod_k |lambda_k|^(-1/r)`.

Apply it to the **five** Walsh eigenvectors in (6.1). Their physical leverage is exactly `5/m<=1/2`, all five coefficients equal `L`, and the separate `z` term is an allowed physical diagonal twist. Hence

`|phi_Q(t)| <= min{1,(4 pi)^(5/2)(L|t|)^(-5/2)}`                 (7.1)

and exact integration gives

`boxed: ||p_Q||_infinity <= (20/3)/L = 6.6666666667.../L,`        (7.2)

with `p_Q in C_0(R)`.

So whole-frame aggregation pays precisely the target-valid family in which the literal crossing has rank one, two top-three cut directions are cancelled by complementary curvature, every physical pair is poorly conditioned, and the available localized row is disconnected.

## 8. What remains

The unrestricted QFORM conjecture remains OPEN. The next compiler should not try to select a uniformly conditioned physical pair. It must consume one of the two concrete packets from Section 4:

* **two-channel packet:** near-rank-one literal crossing plus two signed complementary cancellation channels, a rank-four complementary tube, and an actual localized row; or
* **thin-rank-two packet:** two target-scale literal crossing directions with Frobenius tail `<0.010722L`, complementary rank-five Frobenius tail of the same size, a signed `0.31987L` cancellation, and the actual localized row.

On the one-hub overlap, the newest partner further reduces the second packet to double rank-two alignment or a second localized child row. A successful receiver should aggregate the low-rank cancellation carrier in original coordinates before any reciprocal pivot, and must remain valid for the Walsh family above and for arbitrary same-bank curvature/affine terms permitted by the target.