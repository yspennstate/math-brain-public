SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T09:23:39Z.
attacking: r30's three-packet mixed-range survivor by a quantitative Hall/mixed-discriminant stability theorem, followed by a heavy-row delete-or-isolate reduction on the large mixed-discriminant side.

# account03/B20 r31 — quantitative three-packet Hall stability and heavy-row reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: proof closure and keeper  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `ESSENTIAL_STEP_APPLIED / NEW QUANTITATIVE STRUCTURAL THEOREM / FULL QFORM OPEN`.

The unrestricted conjecture remains OPEN. No Gaussian, log-concave, moment, compact-support, connected-support, diagonal-basis, or post-rotation-independence assumption is introduced. Every packet below is a set of ORIGINAL coordinates. Continuity is stated only on branches where an existing Fourier/Brascamp--Lieb receiver genuinely proves it.

## 1. Fresh incoming state

The immediate predecessor is account03/B20 r30,

`yspennstate/math-open-problems@2c0131b6830892a77a8faaf3521388d3a51e7514`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T084738Z-account03-B20-QFORM-r30/REPORT.md`.

In its still-unpaid exact-rank-three branch,

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `sigma_min(M)>=1`,                 (1.1)

there is an ORIGINAL-coordinate partition

`[n]=B_1 disjoint_union B_2 disjoint_union B_3`                      (1.2)

and orthonormal spectral directions `e_1,e_2,e_3` such that

`sum_(i in B_k) <r_i,e_k>^2 >= c_*`,
`c_*:=453/4096`, `k=1,2,3`.                                          (1.3)

Here `r_i^T` denotes the `i`th row of `R`. Also every still-unpaid state contains a physical row `h` with

`c_h:=||r_h||^2>1/2`.                                                (1.4)

The r30 counterexample shows that (1.3) alone does not imply one nonzero rainbow triple: two packet ranges can coincide. The open implication was explicitly a quantitative Hall/mixed-discriminant dichotomy.

For each packet define its deterministic packet Gram

`G_k:=sum_(i in B_k) r_i r_i^T`.                                    (1.5)

Then

`G_1+G_2+G_3=I_3`, `0<=G_k<=I_3`, and `lambda_1(G_k)>=c_*`.          (1.6)

Define the rainbow squared-volume

`T:=sum_(i in B_1,j in B_2,k in B_3) det(r_i,r_j,r_k)^2`.           (1.7)

By Cauchy--Binet, `T` is exactly the coefficient of `x_1x_2x_3` in

`p(x_1,x_2,x_3):=det(x_1G_1+x_2G_2+x_3G_3)`.                       (1.8)

## 2. Quantitative Hall stability theorem

### Theorem 2.1 — `QFORM-THREEPACKET-HALL-STABILITY-v1`

Let `G_1,G_2,G_3>=0`, `G_1+G_2+G_3=I_3`, and suppose

`lambda_1(G_k)>=alpha` for `k=1,2,3`.                               (2.1)

Fix `0<beta<=1`. Then at least one of the following holds.

**RAINBOW VOLUME:**

`boxed: T >= (2/9) alpha beta^2`.                                  (2.2)

**TWO-PACKET NEAR LINE:** for some distinct `a,b`,

`lambda_2(G_a+G_b)<beta`.                                          (2.3)

If `ell` is a unit top eigenvector of `H:=G_a+G_b`, then

`boxed:
 sum_(i in B_a union B_b) ||P_(ell^perp) r_i||^2 <2 beta.}`         (2.4)

Moreover on `ell^perp`, the complementary packet Gram `G_c=I-H` obeys

`boxed: G_c|_(ell^perp) >(1-beta) I_(ell^perp).}`                   (2.5)

### Proof

Assume (2.3) fails for every pair, so

`lambda_2(G_a+G_b)>=beta` for all `a!=b`.                           (2.6)

We prove a capacity lower bound for the determinant polynomial (1.8). Take arbitrary `x_1,x_2,x_3>0` and relabel the packet indices so that

`x_i<=x_j<=x_k`.                                                     (2.7)

Put

`H:=G_j+G_k=I-G_i`, `K:=G_k`.                                      (2.8)

Then `0<=H<=I`, `lambda_2(H)>=beta`, and `lambda_1(K)>=alpha`. Write

`x_iG_i+x_jG_j+x_kG_k
 = A_0 +(x_k-x_j)K`,                                                (2.9)

where

`A_0:=x_i I +(x_j-x_i)H`.                                          (2.10)

Because the second and first eigenvalues of `H` are at least `beta`,

`det A_0
 >= x_i [x_i+beta(x_j-x_i)]^2`.                                 (2.11)

Also `H<=I` gives `A_0<=x_j I`, hence

`A_0^{-1} >= x_j^{-1}I`.                                           (2.12)

Choose a unit top eigenvector `u` of `K`. Since `lambda_1(K)>=alpha`,

`K>=alpha u u^T`.                                                   (2.13)

Monotonicity of determinant on positive definite matrices and the matrix determinant lemma give

`det(A_0+(x_k-x_j)K)
 >=det(A_0+(x_k-x_j)alpha u u^T)`
`=det A_0 [1+alpha(x_k-x_j) u^T A_0^{-1}u]`
`>=det A_0 [1+alpha(x_k-x_j)/x_j]`.                                (2.14)

Divide by `x_i x_j x_k`. Using (2.11),

`p(x)/(x_1x_2x_3)
 >= [beta+(1-beta)x_i/x_j]^2
    [alpha+(1-alpha)x_j/x_k]`
`>=alpha beta^2`.                                                   (2.15)

Therefore the capacity

`Cap(p):=inf_(x_1,x_2,x_3>0) p(x)/(x_1x_2x_3)`                     (2.16)

satisfies

`Cap(p)>=alpha beta^2`.                                             (2.17)

The polynomial `p` is homogeneous of degree three, has nonnegative coefficients by Cauchy--Binet, and is real stable: if every `Im z_k>0`, then

`Im(sum_k z_kG_k)=sum_k (Im z_k)G_k`                               (2.18)

is positive definite because `sum_kG_k=I`; hence the matrix is nonsingular. We now use Gurvits's coefficient/capacity inequality for homogeneous real-stable polynomials with nonnegative coefficients:

`[x_1x_2x_3]p >= (3!/3^3) Cap(p)=(2/9)Cap(p)`.                    (2.19)

This is a published theorem, not a new fleet claim. It is the `n=3` instance of the stable-polynomial van-der-Waerden/Gurvits inequality; see Leonid Gurvits, *Van der Waerden Conjecture for Mixed Discriminants*, arXiv:math/0406420, and the real-stable coefficient formulation discussed by Nima Anari and Shayan Oveis Gharan, arXiv:1702.02937.

Equations (2.17)-(2.19) prove (2.2).

If instead (2.3) holds, diagonalize `H` with eigenvalues `h_1>=h_2>=h_3>=0` and take `ell` along the `h_1` eigendirection. Then

`sum_(i in B_a union B_b)||P_(ell^perp)r_i||^2
 =h_2+h_3<2beta`,                                                   (2.20)

which is (2.4). Since `G_c=I-H`, its eigenvalues on `ell^perp` are `1-h_2,1-h_3`, both strictly larger than `1-beta`, proving (2.5). QED.

### Source-matching note on Gurvits

The only imported published statement is the coefficient/capacity implication (2.19). The packet-to-capacity estimate (2.15), the exact coefficient identity (1.8), and the near-line conclusion are proved here. No conclusion about random-variable independence is taken from spectral coordinates.

## 3. Exact constants in the live r30 packet

Take

`alpha=c_*=453/4096`, `beta=1/64`.                                  (3.1)

Theorem 2.1 gives the exhaustive alternative

`boxed: T >= zeta:=151/25165824
                 =6.000200907389... x 10^(-6)}`                    (3.2)

or, for some pair of physical packets and some deterministic spectral line `ell`,

`boxed:
 sum_(i in B_a union B_b)||P_(ell^perp)r_i||^2 <1/32,`             (3.3)

while the complementary packet has

`boxed: G_c|_(ell^perp) >(63/64)I_(ell^perp).}`                    (3.4)

Thus the exact r30 counterexample is not an uncontrolled obstruction: it is captured quantitatively by the second branch.

If the heavy physical row `h` from (1.4) belongs to the near-line pair, then

`||P_(ell^perp)r_h||^2<1/32`,                                     (3.5)

and with `e_h=r_h/||r_h||`,

`boxed: sin^2 angle(e_h,ell)<(1/32)/(1/2)=1/16.`                   (3.6)

If instead `h` lies in the complementary packet, then the two non-heavy packets jointly have transverse trace below `1/32`, while the packet containing the heavy row alone carries more than `63/64` Gram mass in each of two directions orthogonal to `ell`. This is a fixed, product-preserving two-dimensional receiver geometry.

## 4. Large-rainbow branch: heavy-row delete or isolate at a fixed scale

The rainbow branch (3.2) can be sharpened immediately using the heavy row. Rename packets so `h in B_1`, and write

`L:=||r_h||^2>1/2`.                                                  (4.1)

Split the rainbow packet as

`T=T_h+T_rest`,                                                      (4.2)

where

`T_h:=sum_(j in B_2,k in B_3)det(r_h,r_j,r_k)^2`                    (4.3)

and `T_rest` is the rainbow mass avoiding `h`.

Cauchy--Binet for the residual Parseval frame gives

`T_rest <= det(I-r_hr_h^T)=1-L`.                                   (4.4)

Set

`eta_0:=zeta/2=151/50331648
       =3.000100453694... x 10^(-6)`.                              (4.5)

### Theorem 4.1 — `QFORM-RAINBOW-HEAVY-DELETE-OR-ISOLATE-v1`

On the rainbow branch, one of the following holds.

**DELETE.** `1-L>=eta_0`. Condition on the ORIGINAL coordinate `X_h`. The residual row Gram is

`H=I-r_hr_h^T`,                                                     (4.6)

with `lambda_min(H)=1-L>=eta_0`. After deterministic coefficient whitening, the same residual quadratic block has spectral matrix

`N_-=H^(1/2) M H^(1/2)`                                            (4.7)

satisfying

`boxed: sigma_min(N_-)>=eta_0, |det N_-|>=eta_0.`                  (4.8)

**ISOLATE.** `1-L<eta_0`. Then by (4.2)-(4.4),

`T_h>T-(1-L)>zeta/2=eta_0`.                                       (4.9)

Put

`K=r_hr_h^T+G_2+G_3`.                                               (4.10)

Cauchy--Binet contains all fixed-hub `B_2-B_3` minors as nonnegative terms, so

`det K>=T_h>eta_0`.                                                  (4.11)

Since `0<K<=I`,

`lambda_min(K)>=det K>eta_0`.                                      (4.12)

Condition on all ORIGINAL coordinates in `B_1\{h}`. The active independent sources are the singleton hub together with the two untouched original-coordinate banks `B_2,B_3`. After coefficient whitening their exact-rank-three spectral matrix

`N_h=K^(1/2) M K^(1/2)`                                            (4.13)

satisfies

`boxed: sigma_min(N_h)>eta_0, |det N_h|>eta_0.`                    (4.14)

### Proof

For DELETE, `H` has eigenvalues `1,1,1-L`. Conditioning an original coordinate preserves independence among the residual physical coordinates; its couplings become an arbitrary affine term. From `sigma_min(M)>=1` and `|det M|>=1`,

`sigma_min(H^(1/2)MH^(1/2))>=lambda_min(H)>=eta_0`,                 (4.15)

and

`|det N_-|=det(H)|det M|=(1-L)|det M|>=eta_0`.                     (4.16)

For ISOLATE, (4.9)-(4.12) hold as stated. Conditioning on the rest of `B_1` again preserves original-coordinate independence in the active set. Equations (4.13)-(4.14) follow from `sigma_min(M)>=1`, `|det M|>=1`, `lambda_min(K)>eta_0`, and `det K>eta_0`. QED.

### Diffuse child is already paid

In either DELETE or ISOLATE, normalize the active row Gram to `I_3`. If every normalized active physical leverage is at most `1/2`, the completed exact-rank-three Fresnel--Brascamp--Lieb diffuse-core theorem used in account03/B10 r20 applies uniformly in the conditioned affine term:

`||p_Q||_infinity <=12 |det N_active|^(-1/3)
                   <=12 eta_0^(-1/3)
                   <833.`                                         (4.17)

The cited theorem gives a continuous density on this branch. Hence every still-unpaid large-rainbow state reduces to a **uniformly conditioned active exact-rank-three block with another normalized physical leverage `>1/2`**; in the isolate child the active product provenance has the particularly sharp form `singleton hub + two original-coordinate banks`, and its fixed-hub rainbow packet is `>eta_0`.

This is not claimed to close the heavy active child. Existing B10 work shows why arbitrary repeated heavy-row deletion is not by itself a dimension-free proof.

## 5. Designated account04/B20 theorem applied at an actual inequality

The designated partner theorem is account04/B20

`QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1`,

canonical source

`yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T011956Z-account04-B20-QFORM-r4/REPORT.md`.

At its exact scope, write the heavy physical row as

`r_h=sqrt(c_h)e`, `c_h>1/2`,                                      (5.1)

and suppose every residual physical row is exactly longitudinal to `e` or transverse to `e`. Put

`a=e^T M e`.                                                        (5.2)

If `|a|<=1/2`, the partner theorem gives the actual full-law inequality

`boxed:
 ||p_Q||_infinity
 <=103680^(1/3) 2^(7/6)|det M|^(-1/3)
 <105.463,`                                                         (5.3)

and the density is continuous. If `|a|>1/2`, then the genuine physical diagonal satisfies

`|A_hh|=c_h |a|>1/4`,                                               (5.4)

which is already in the completed scalar-pivot branch. Thus the exact longitudinal/transverse overlap of the r31 state is paid. I do not apply the partner theorem to approximately partitioned rows.

Consequently every unpaid r31 survivor still contains genuinely mixed physical rows relative to the leverage-`>1/2` direction. On the near-line branch, if the heavy row belongs to the near-line pair, (3.6) says that the Hall line is already within squared sine `<1/16` of that heavy direction; the remaining debt is therefore quantitative mixed leakage, not an uncontrolled range orientation.

## 6. Why this advances the first implication

r30 left the qualitative statement: large mixed discriminant should feed a third-volume mechanism; small mixed discriminant should force two packet ranges close to a common line. Theorem 2.1 makes that statement dimension-free and quantitative at explicit constants.

The large side is additionally compiled by Theorem 4.1 into a fixed-scale active exact-rank-three child, with its diffuse part completely paid by `<833`. The small side is no longer merely `T` small: two entire ORIGINAL-coordinate packets have total transverse squared mass `<1/32`, and the remaining packet carries `>63/64` in both transverse directions.

No physical coordinate is deleted as an approximation, no good individual determinant is selected, and no spectral coordinate is declared independent.

## 7. First unpaid implication after r31

The earliest remaining synthesis debt is now

`QFORM-THREEPACKET-NEARLINE-OR-HEAVY-ACTIVE-PAYMENT-v1`:

1. **near-line child:** pay the state (3.3)-(3.4), using the existing genuine mixed row and distinguishing whether the leverage-`>1/2` row lies inside or outside the near-line pair; or
2. **large-rainbow heavy child:** after Theorem 4.1, pay the uniformly conditioned active exact-rank-three block when its normalized frame still has a leverage-`>1/2` row, with the isolate branch retaining an aggregate fixed-hub packet `>eta_0` across two independent physical banks.

A valid payment must remain aggregate before reciprocal minors. The known target-valid B10 spread-bank families prevent replacing either child by one uniformly large physical scalar pivot, pair determinant, or principal triple.

The unrestricted QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN. Continuity is proved here only on the diffuse active branch (4.17) and the designated partner overlap (5.3).

## 8. Exact arithmetic checks

The constants are exact:

`(2/9)*(453/4096)*(1/64)^2 =151/25165824`,

`2*(1/64)=1/32`,

`(1/32)/(1/2)=1/16`,

`eta_0=(1/2)*(151/25165824)=151/50331648`.

The decimal `<833` in (4.17) is only a display check; the analytic bound is the exact expression `12*(50331648/151)^(1/3)`.
