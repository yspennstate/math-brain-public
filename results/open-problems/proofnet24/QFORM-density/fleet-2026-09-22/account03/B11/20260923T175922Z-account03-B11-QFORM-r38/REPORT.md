SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T17:59:22Z.
attacking: rank-two crossing plus one internal square curvature as an integrated-Fourier third-direction receiver; apply it to the exact-graph near-coloop boundary and isolate the null-ruling survivor.

# account03/B11 r38 — rank-two crossing + internal square curvature

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner continuation acknowledged:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
**Status:** `NEW SUPPORTING THEOREM / ACTUAL NEAR-COLOOP APPLICATION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new Fourier branch proves a bounded **continuous** density. It does not prove continuity for the full target.

The unrestricted conjecture remains OPEN. No Gaussianity, log-concavity, moment, support, connectedness, spectral-coordinate independence, or pointwise van-der-Corput decay is used.

## 1. Why this mechanism is needed

The exact opposite-sign rank-two control remains

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,

for independent centered unit uniforms. At Fourier level a rank-two bilinear crossing gives the endpoint decay `|t|^-1`, which is not integrable. The live correction forbids replacing the missing half power by a law-uniform pointwise quadratic-phase estimate.

The first new theorem below instead uses an **integrated** square-phase estimate. A third square curvature on one side of a rank-two crossing produces a mixed `L^4(dt;L^2)` gain. Hölder against the rank-two `|t|^-1` factor is then integrable. This is exactly the kind of averaged Fourier mechanism still allowed by the current corrections.

## 2. New analytic theorem

### Theorem `QFORM-RANK2-CROSS-INTERNAL-SQUARE-L4-v1`

Let `X` and `Y` be independent random vectors. Let

`u=U^T X in R^2`, `z=w^T X in R`, `v=V^T Y in R^2`,

where `[U,w]` has three orthonormal columns in the `X` source space and `V` has two orthonormal columns in the `Y` source space. Assume `(u,z)` has a joint density `rho` satisfying

`||rho||_infinity <= M_X`,

and `v` has density `p_v` satisfying

`||p_v||_infinity <= M_Y`.

Let `S=diag(sigma_1,sigma_2)` with `sigma_1,sigma_2>0`. Suppose

`Q = [u;z]^T C [u;z] + 2 u^T S v + G(Y)`,                    (2.1)

where `C` is a real symmetric `3 x 3` matrix, `G` is arbitrary measurable real-valued, and the `z^2` coefficient

`alpha := C_33`

is nonzero. Then `Q` has a bounded continuous density and

`boxed:
 ||p_Q||_infinity
 <= C_* (M_X M_Y)^(2/5)
          (sigma_1 sigma_2)^(-2/5) |alpha|^(-1/5),`              (2.2)

where one may take

`C_* = [10/(2 pi 8^(4/5))]
       [pi 6^(3/4) (16 pi)^(1/4)]^(4/5)
     = 4.8329551124... < 4.833.`                                 (2.3)

The signs of the eigenvalues of `C` are irrelevant. In particular the theorem is compatible with both target signatures `(+,+,-)` and `(+,-,-)`.

### Proof

Write

`C = [[C_0,d],[d^T,alpha]]`.

Completing the square only inside the already dependent three-dimensional projection gives

`[u;z]^T C [u;z]
 = alpha (z+alpha^(-1)d^T u)^2
   + u^T(C_0-alpha^(-1)dd^T)u`.                                 (2.4)

For each `t`, push the `Y`-side complex measure `exp(it G(Y)) dP_Y` onto `v`. Its density `b_t(v)` satisfies

`|b_t(v)| <= p_v(v)`,

hence

`||b_t||_2 <= M_Y^(1/2)`.                                       (2.5)

On the `X` side define

`a_t(u)=exp(it u^T(C_0-alpha^(-1)dd^T)u)
        integral exp(it alpha y^2)
        rho(u,y-alpha^(-1)d^T u) dy`.                            (2.6)

The translation in the last argument depends on `u`, but for each fixed `u` it preserves both the vertical mass

`m(u)=integral rho(u,z) dz`                                      (2.7)

and the cap `M_X`.

We first prove the square-phase mixed norm

`boxed: integral_R ||a_t||_2^4 dt <=16 pi M_X^2/|alpha|.`         (2.8)

Fix `u`, abbreviate the translated vertical density by `f(z)`, and let `m=int f`. For `alpha=1`, let `h` be the density of `Z^2` under the sub-probability density `f`. For `r>0`,

`h(r)=[f(sqrt(r))+f(-sqrt(r))]/[2 sqrt(r)] <= M_X/sqrt(r)`.       (2.9)

Therefore

`int h(r)^(3/2) dr
 <= M_X^(1/2) int h(r) r^(-1/4) dr
 =  M_X^(1/2) int f(z)|z|^(-1/2) dz`.                            (2.10)

Among densities bounded by `M_X` with mass `m`, the final weighted integral is maximized by filling the centered interval of length `m/M_X`. Hence

`int f(z)|z|^(-1/2) dz <=2 sqrt(2 M_X m)`,                        (2.11)

and so

`||h||_(3/2)^(3/2) <=2 sqrt(2) M_X sqrt(m)`.                      (2.12)

With the Fourier convention used by the current QFORM package, Hausdorff--Young gives

`int_R |int exp(it z^2) f(z) dz|^3 dt
 <=2 pi [int h^(3/2)]^2
 <=16 pi M_X^2 m`.                                               (2.13)

Replacing `t` by `alpha t` gives the additional factor `|alpha|^-1`. Integrating (2.13) over `u` and using `int m(u)du=1` gives

`int_R ||a_t||_3^3 dt <=16 pi M_X^2/|alpha|`.                    (2.14)

Also `||a_t||_1<=1`. Interpolation in `u` yields

`||a_t||_2^4 <=||a_t||_1 ||a_t||_3^3 <=||a_t||_3^3`,             (2.15)

which proves (2.8).

Now use the exact rank-two crossing. Fourier inversion of the bilinear phase and Plancherel, exactly as in the current projected-crossing theorem, give for `t !=0`

`|phi_Q(t)|
 <= [pi/|t|] (sigma_1 sigma_2)^(-1/2)
     ||a_t||_2 ||b_t||_2`                                       (2.16)

and hence, by (2.5),

`|phi_Q(t)|
 <= A |t|^-1 F(t)`,                                              (2.17)

where

`A=pi M_Y^(1/2)(sigma_1 sigma_2)^(-1/2)`,
`F(t)=||a_t||_2`,

and by (2.8)

`||F||_4 <=(16 pi)^(1/4) M_X^(1/2)|alpha|^(-1/4)`.               (2.18)

For every `T>0`, use `|phi_Q|<=1` on `|t|<T`, and Holder on the complement:

`int_|t|>=T |t|^-1 F(t) dt
 <=[int_|t|>=T |t|^(-4/3)dt]^(3/4)||F||_4
 =6^(3/4) T^(-1/4)||F||_4`.                                     (2.19)

Thus

`int_R |phi_Q(t)|dt <=2T+B T^(-1/4)`,                            (2.20)

with

`B=pi 6^(3/4)(16 pi)^(1/4)
    (M_X M_Y)^(1/2)(sigma_1 sigma_2)^(-1/2)|alpha|^(-1/4)`.      (2.21)

The minimizing choice is `T=(B/8)^(4/5)`, and then

`int |phi_Q|
 <=10 8^(-4/5) B^(4/5)`.                                       (2.22)

Fourier inversion gives (2.2)--(2.3). Since `phi_Q in L^1`, the resulting density has a bounded continuous representative. QED.

### Scope note

This theorem is **not** a disguised pointwise van-der-Corput statement. The square phase can still be phase-aligned at individual frequencies. The only square gain used is the integrated estimate (2.8), and the rank-two crossing contributes its separate Plancherel factor.

The theorem also does not claim that a small third singular value of a rank-three cross block can simply be discarded. It applies when the relevant physical cut has an exact rank-two crossing and the missing direction survives as nonzero internal square curvature.

## 3. Application to the B11 exact-graph near-coloop boundary

Use the exact-rank-three state from account03/B11 r37:

`A=R M R^T`, `R^T R=I_3`, `s=min|eig M|>=1`,

with a physical hub row

`r_0=sqrt(c)e`, `c>63/64`,

and residual rows `r_j=s_j e+w_j`, `w_j in e^perp`.

The designated account04/B11 theorem is first used at an actual inequality. If some residual row satisfies

`||w_j||^2 >=1/36`,

then

`g_0j=||r_0 wedge r_j||^2=c||w_j||^2
    >(63/64)(1/36)=7/256`.                                      (3.1)

Account04/B11, commit `50b07997bec888ff7cc6820cd42be8e34d0ffc48`, proves

`||p_Q||_infinity <=128 sqrt(2)/(s sqrt(g_0j))`,                  (3.2)

so (3.1) gives the concrete full-line estimate

`boxed: ||p_Q||_infinity
 <2048 sqrt(2/7)/s
 =1094.7020469.../s.`                                            (3.3)

This is the required completed partner result applied at an actual target inequality.

Hence the surviving r37 chamber may assume every transverse leaf leverage is `<1/36`. The determinant-pair coloring argument already proved that there is a literal original-coordinate partition `S sqcup T` of the residual leaves such that, with

`G_B=sum_(j in B) w_j w_j^T`,

`det(G_S)det(G_T)>17/288`,
`lambda_min(G_S),lambda_min(G_T)>17/288`.                         (3.4)

Put

`tau_B=sum_(j in B)s_j^2`,
`h_B=sum_(j in B)s_jw_j`,
`rho_B=tau_B-h_B^T G_B^(-1)h_B`.                                 (3.5)

The r37 theorem already pays the exact graph boundary `rho_B=0` in essential `L^infinity`, but did not prove continuity. The new theorem yields a continuous-density subbranch and identifies the remaining tangent geometry.

Assume, after relabeling, that

`rho_T=0`.                                                        (3.6)

Let `H={0} union S` and consider the physical crossing

`B=A[H,T]=R_H M R_T^T`.                                         (3.7)

Because (3.6) says the full spectral rows of `T` lie on a two-dimensional graph plane, `R_T` has rank two; `R_H` has rank three because it contains the hub and `G_S>0`. Thus `B` has exact rank two. Let its nonzero singular values be `sigma_1>=sigma_2>0`.

### Uniform lower bound on the rank-two crossing product

The full spectral Gram on `T` is

`Gamma_T=R_T^T R_T=J_T G_T J_T^T`,
`J_T y=(a_T^T y)e+y`, `a_T=G_T^(-1)h_T`.                         (3.8)

Therefore

`pdet(Gamma_T)=det(G_T)(1+||a_T||^2)>17/288`.                    (3.9)

The full Gram on `H` is

`Gamma_H=R_H^T R_H
 =[[c+tau_S,h_S^T],[h_S,G_S]]`.                                  (3.10)

Writing `a_S=G_S^(-1)h_S`, it factors as

`Gamma_H=L_S diag(c+rho_S,G_S)L_S^T`,
`L_S=[[1,a_S^T],[0,I_2]]`.                                       (3.11)

Since `tau_S<=1-c<1/64` and `lambda_min(G_S)>17/288`,

`||a_S||^2 <=tau_S/lambda_min(G_S)<9/34`.                         (3.12)

Hence

`sigma_min(L_S)^2
 >=||L_S^(-1)||_F^(-2)
 >34/111`,                                                       (3.13)

and therefore

`lambda_min(Gamma_H)
 >(17/288)(34/111).`                                             (3.14)

Since `sigma_min(R_H M)>=s sqrt(lambda_min(Gamma_H))`, the two-dimensional determinant inequality on the rank-two map `R_T^T` gives

`sigma_1 sigma_2
 >=s^2 lambda_min(Gamma_H) sqrt(pdet(Gamma_T))`

and thus

`boxed:
 sigma_1 sigma_2
 > kappa_0 s^2,
 kappa_0=(34/111)(17/288)^(3/2)
        =0.00439279148... .`                                    (3.15)

### The internal-square invariant

Choose an SVD `B=U diag(sigma_1,sigma_2)V^T`. Inside the three-dimensional physical range `range(R_H)`, let `w` be the unique unit vector orthogonal to `range(U)`. The full `H`-side quadratic block has range in `range(R_H)`, so after projecting `X_H` onto

`u=U^T X_H`, `z=w^T X_H`,                                       (3.16)

it is an exact three-variable quadratic form. Define its cross-null internal curvature

`alpha_H := w^T A[H,H] w`.                                      (3.17)

The variables `(u,z)` are a three-dimensional orthogonal projection of the original product law on `H`, while `v=V^T X_T` is a two-dimensional orthogonal projection of the disjoint original product law on `T`. The product-projection theorem used in the current projected-crossing source gives

`M_X<=2^(3/2)`, `M_Y<=2`.                                       (3.18)

If for some `theta>0`

`|alpha_H| >=theta s`,                                          (3.19)

then Theorem 2.1, (3.15), and (3.18) give

`||p_Q||_infinity
 < 4.833 (2^(3/2)*2)^(2/5)
       kappa_0^(-2/5) theta^(-1/5) s^(-1)`

and the projection constants simplify exactly because

`(2^(3/2)*2)^(2/5)=2`.                                          (3.20)

Numerically,

`boxed:
 ||p_Q||_infinity
 <84.752 theta^(-1/5)/s.`                                       (3.21)

For the concrete non-null-ruling threshold `theta=1/100`,

`boxed:
 ||p_Q||_infinity <212.886/s,`                                  (3.22)

and this branch has a **continuous density**.

### What remains on the exact graph boundary

The r37 theorem already gives essential boundedness `<128/s` when `rho_T=0`, with no lower bound on `alpha_H`; therefore (3.21) is not advertised as a better `L^infinity` constant. Its new content is analytic mechanism and regularity: it proves continuity whenever the cross-null direction has quantitative internal square curvature.

The only exact-graph portion not covered by this continuous-density argument is the **null-ruling/tangent collar**

`|alpha_H|/s ->0`.                                                (3.23)

In indefinite signature this is a genuine geometric possibility: the missing cross direction may approach a null direction of the restricted quadratic form. There one must exploit the remaining internal bilinear curvature rather than pretend that an arbitrarily small `alpha_H` is a perturbative square.

## 4. How the third direction removes the logarithmic singularity

This theorem gives a quantitative answer in the non-null-ruling exact-graph chamber.

* Rank-two crossing alone contributes `|t|^-1`, exactly the Fourier endpoint compatible with the logarithmic density of `2XY`.
* The third square direction is **not** assigned a false pointwise `|t|^-1/2` estimate.
* Instead the selector/product geometry yields

  `integral ||a_t||_2^4 dt < infinity`.                           (4.1)

* Holder then makes

  `integral_1^infinity |t|^-1 ||a_t||_2 dt < infinity`.          (4.2)

Thus the third direction removes the logarithmic endpoint by an integrated time estimate. This mechanism respects fragmented/unbounded cap-one inputs and does not diagonalize the random variables.

Reflection `Q -> -Q` leaves the proof unchanged, so the same mechanism applies to both `(+,+,-)` and `(+,-,-)`.

## 5. Current gap after this run

The full exact-rank-three problem is still not closed by this report, and arbitrary additional nonseparable spectrum remains a separate bridge.

The sharpened B11 analytic gap is:

`QFORM-RANK2-CROSS-NULLRULING-INTERNAL-BILINEAR-v1`:

> In the exact-graph near-coloop boundary, when the rank-two crossing product is uniformly paid but the cross-null self coefficient `alpha_H` is arbitrarily small or zero, exploit the necessarily surviving internal `z-u` bilinear curvature by an integrated estimate analogous to Theorem 2.1. Do not replace it by pointwise phase decay or by conditional density caps.

For the punctured collar `0<rho_S,rho_T<<1`, the account02/B11 projected-crossing theorem remains valid but deteriorates as a negative power of the graph defect. A future uniform interpolation must combine that nonzero crossing currency with the rank-two/internal-curvature mechanism without treating a small operator coefficient as a small random quadratic error.

The unrestricted owner target remains OPEN. Global continuity remains OPEN.

## 6. Sources actually used

2. account03/B11 r37 exact graph boundary: `yspennstate/math-open-problems@60366e6dcbf3a321423e2ff1b0f4ecb9a78776f6`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T171407Z-account03-B11-QFORM-r37/BOUNDARY_CHECKPOINT.md`.
3. designated partner account04/B11 disjoint-volume/pair-area compiler: `yspennstate/math-open-problems@50b07997bec888ff7cc6820cd42be8e34d0ffc48`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T111608Z-account04-B11-disjoint-volume-compiler-r5/REPORT.md`.
4. projected-crossing Fourier normalization and product-projection caps: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
5. rank-two logarithmic control and current corrections are retained from the shared QFORM state; no refuted arbitrary-joint coarea or conditional-cap shortcut is used.

No public release, workflow execution, paid API/model call, installation, scheduler mutation, cross-account authentication, notification change, or email action was performed.
