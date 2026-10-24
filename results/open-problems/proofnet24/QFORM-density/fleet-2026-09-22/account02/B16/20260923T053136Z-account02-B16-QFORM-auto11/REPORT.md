SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T05:31:36Z.
attacking: the account03/B16 r26 near-coloop collar by testing the exact product-projection/Fresnel interface at the phase-sensitive `a=1-c -> 0` endpoint.

# account02/B16 — a strict-N3 near-coloop family with a logarithmically divergent absolute Fresnel certificate but uniformly bounded true density

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Method:** complementary construction / source-valid mechanism obstruction  
**Status:** `NEW SUPPORTING CONSTRUCTION + REFUTED INTERMEDIATE MECHANISM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** available on this constructed family from the completed mixed-hub Fresnel theorem; global continuity remains open.

## 1. Exact target and current boundary

The owner target remains the unrestricted statement: for every finite `n`, arbitrary independent real original-coordinate inputs with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential `L^infinity` density bound for `X^T A X`, or give a genuine counterexample. No moments, bounded support, log-concavity, identical laws, diagonal-basis independence, or post-rotation independence may be assumed.

Fresh owner control was read at the start of this invocation; QFORM remains the only active programme and the full conjecture remains open. The live corrections were reread. In particular this report does not use arbitrary-joint three-dimensional coarea, worst conditional projection-density heights or their positive moments, independence after spectral rotation, or law-uniform pointwise one-dimensional stationary phase.

The immediate designated-partner input is account03/B16 r26,

`yspennstate/math-open-problems@d6730c301e46e6337bc3b32e30eb3d04f07dc90b`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T045948Z-account03-B16-QFORM-r26/REPORT.md`.

Its theorem `QFORM-R23-ONE-COLOOP-REDUCTION-v1` reduces the exact-rank-three dominant-star residual chamber to the single geometric collar

`c>63/64`,                                                        (1.1)

where `c` is the leverage of one original physical row in a spectral direction `e`, and the residual longitudinal Parseval mass is

`a:=1-c<1/64`.                                                    (1.2)

The required bound must remain uniform as `a -> 0`; one may not replace the near-coloop by the exact coloop, delete the residual coefficient, or invoke a worst conditional projected density.

The purpose of this run is twofold. First, exhibit a many-direction, strict-N3 family lying genuinely inside that remaining collar and pay its true density uniformly while preserving product provenance. Second, prove that the natural endpoint extension of the absolute spectral Fresnel/duplicated-slice coefficient is impossible even on this harmless family: the exact absolute coefficient grows logarithmically as `a -> 0`.

## 2. Coefficient-space setup

Let

`Lambda=diag(1,1,-1)`                                                (2.1)

in the standard spectral basis and put

`e=(1,0,1)/sqrt(2)`,
`p=(1,0,-1)/sqrt(2)`,
`q=(0,1,0)`.                                                        (2.2)

The ordered triple `(e,p,q)` is orthonormal. In this deterministic coefficient basis the same quadratic form has matrix

`B=[[0,1,0],
    [1,0,0],
    [0,0,1]]`.                                                       (2.3)

Thus

`e^T Lambda e=0`, `e^T Lambda p=1`, `q^T Lambda q=1`,               (2.4)

and all other entries in (2.3) vanish. In particular

`det B=-1`, `B^(-1)=B`,                                             (2.5)

and the three nonzero eigenvalues remain exactly `{1,1,-1}`.

Fix

`0<a<1/128`, `c=1-a`.                                               (2.6)

For an integer `m>=3` put `theta_k=2 pi k/m` and define plane rows

`w_k=sqrt(2/m)(cos(theta_k) p+sin(theta_k) q)`, `1<=k<=m`.          (2.7)

The elementary trigonometric identities give

`sum_k w_k w_k^T=P_(e^perp)`.                                      (2.8)

Now take the physical spectral-frame rows

`r_0=sqrt(c)e`,
`r_1=sqrt(a)e`,
`r_(k+1)=w_k`, `1<=k<=m`.                                         (2.9)

Then

`sum_j r_j r_j^T=I_3`,                                             (2.10)

so if `R` is the matrix with rows (2.9), `R^T R=I_3`. Define

`A=R B R^T`.                                                        (2.11)

Because `R` is an isometry on coefficient space, the nonzero spectrum of `A` is the spectrum of `B`, namely

`boxed: spec_nonzero(A)={1,1,-1}.`                                 (2.12)

Hence every member of the family satisfies the exact three-large-eigenvalue hypothesis.

Relative to the partner notation, the dominant row has leverage `c>127/128>63/64`; its coefficient direction is exactly null by (2.4). The residual line row has `s_1^2=a`, transverse leverage zero. Every plane row has longitudinal coefficient zero and

`h_k=||w_k||^2=2/m`.                                                (2.13)

Thus for `m>128` all transverse leverages are below `1/64`. The duplicated-slice leverages from account03/B16 r24 are

`delta_1=0+a/(2a)=1/2`,
`delta_(k+1)=2/m`,                                                  (2.14)

so the source-valid duplicated-slice gate passes exactly at the endpoint row and strictly on the plane rows. Its published density estimate nevertheless carries the factor `[c(1-c)]^(-1/6)=[ca]^(-1/6)` and therefore is not uniform as `a -> 0`.

## 3. This is a genuine strict-N3 / low-disjoint-mass stress family

The construction can be made to satisfy every physical no-pivot threshold at once.

Write a plane row in coefficient coordinates as

`w_k=(0,alpha_k,beta_k)`,
`alpha_k=sqrt(2/m) cos(theta_k)`,
`beta_k=sqrt(2/m) sin(theta_k)`.                                    (3.1)

From (2.3), the physical matrix entries are

`A_00=A_11=0`,
`A_(k+1,k+1)=beta_k^2<=2/m`,                                      (3.2)

`A_(0,k+1)=sqrt(c) alpha_k`,
`A_(1,k+1)=sqrt(a) alpha_k`,                                      (3.3)

and among plane coordinates

`A_(k+1,l+1)=beta_k beta_l`.                                       (3.4)

Consequently every physical `2x2` principal determinant is either zero or, for one line row and one plane row,

`-c alpha_k^2` or `-a alpha_k^2`,                                  (3.5)

so

`max_i |A_ii|<=2/m`,
`max_(i<j) |det A_{ {i,j},{i,j} }|<=2/m`.                          (3.6)

Therefore for every prescribed no-pivot threshold `tau>0`, choosing

`m>2/tau`                                                          (3.7)

places the family in the strict N3 physical regime while preserving the exact spectrum `{1,1,-1}`.

The disjoint-Pluecker exit is also quantitatively absent. Every nonsingular physical basis contains exactly one of the two line rows `{0,1}` and two plane rows. Under the normalized Pluecker basis law, the line choice has probabilities `c` and `a`, because the plane-pair Cauchy--Binet weights sum to one. Two independently sampled bases can be disjoint only if their line choices differ. Hence the disjoint-basis mass `d` used by the partner satisfies

`d<=2ac<2a<1/64`.                                                   (3.8)

Thus, after taking `m>128`, this is not a family already removed by the partner's `d>=1/64` or transverse-leverage exits. It lies squarely in the r26 near-coloop collar.

## 4. The random variables: one genuine source bank and one dependent projected pair

Let all original coordinates be independent with arbitrary probability densities bounded by one. Define

`T=sqrt(c) X_0+sqrt(a) X_1`,                                       (4.1)

and from the disjoint plane bank

`C=sum_(k=1)^m alpha_k X_(k+1)`,
`D=sum_(k=1)^m beta_k X_(k+1)`.                                   (4.2)

Then the line bank `{X_0,X_1}` is genuinely independent of the **whole pair** `(C,D)`. No claim is made that `C` and `D` are independent; they reuse every plane source coordinate and are generally dependent.

The spectral coordinates in the basis `(e,p,q)` are exactly `(T,C,D)`. Hence by (2.3)

`boxed: Q=2 T C+D^2.`                                             (4.3)

This is the desired projection-product geometry: a genuinely independent source-bank scalar interacts nonlinearly with a dependent two-dimensional product projection.

The density of `sqrt(c)X_0` is bounded by `c^(-1/2)`. Convolution with the independent probability law of `sqrt(a)X_1` cannot increase the `L^infinity` norm, so

`||p_T||_infinity<=L:=c^(-1/2).`                                  (4.4)

The coefficient matrix in (4.2) has orthonormal columns by (2.8). The completed two-dimensional product-projection theorem therefore gives

`boxed: ||p_(C,D)||_infinity<=2.`                                 (4.5)

Again, (4.5) is a joint density cap, not independence of the two projected coordinates.

## 5. Uniform true-density payment: two source-valid derivations

### 5.1 Real-space dependent-pair kernel

The previously completed account02/B16 theorem `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1` states that if a scalar of density cap one is independent of an arbitrary pair with joint density cap `M`, then

`2 beta X C+alpha C^2+2 delta C D+gamma D^2`

has density at most

`3(2M)^(2/3)|beta^2 gamma|^(-1/3)`.                               (5.1)

For a scalar cap `L`, rescale `U=L T`; then `p_U<=1`, `T=U/L`, and (5.1) becomes

`||p_Q||_infinity
 <=3(2M)^(2/3)L^(2/3)|beta^2 gamma|^(-1/3).`                      (5.2)

Apply (5.2) to (4.3) with `M=2`, `beta=gamma=1`, and (4.4):

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3)c^(-1/3)
 <3*2^(4/3)(64/63)^(1/3)
 <7.60.`                                                          (5.3)

The only independence used here is between the line source bank and the entire plane bank.

### 5.2 Direct application of the required completed Claude mixed-hub theorem

The required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

proves Theorem H / mixed Fresnel. We apply it at equation level rather than merely citing it.

Set

`U=L T`, `L=c^(-1/2)`,                                             (5.4)

so `p_U<=1` and

`Q=2 L^(-1) U C+D^2`.                                             (5.5)

Treat `U` as the one heavy/hub coordinate. The original plane coordinates remain the light independent factors. Their light quadratic block is the single spread square `D^2`, so Theorem H has `|H|=1`, `r=1`, `lambda=1`. For plane coordinate `k` the augmented row is

`rho~_k=(beta_k, alpha_k/L)`.                                     (5.6)

Using the tight-frame identities,

`Gamma~=sum_k rho~_k rho~_k^T
       =diag(1,L^(-2))`,                                          (5.7)

so

`det Gamma~=L^(-2)`.                                              (5.8)

The normalized augmented leverage is exactly

`rho~_k^T Gamma~^(-1) rho~_k
 =beta_k^2+alpha_k^2
 =2/m<1/2`.                                                       (5.9)

Thus every hypothesis of the completed theorem is satisfied. Its explicit formula gives

`|phi_Q(t)|
 <=(2|t|)^(-1)(4 pi |t|)^(-1/2)(4 pi)^2 (det Gamma~)^(-1/2)
 =4 pi^(3/2) L |t|^(-3/2).`                                      (5.10)

Combining with `|phi_Q|<=1` and integrating the exact majorant,

`int_R min(1,K|t|^(-3/2))dt=6K^(2/3)`,                            (5.11)

Fourier inversion yields

`||p_Q||_infinity
 <=3*2^(4/3)L^(2/3)
 =3*2^(4/3)c^(-1/3)<7.60`.                                       (5.12)

The same argument supplies a continuous `C_0` density on this family.

This is an explicit application of the completed Claude result to the partner's near-coloop geometry. The theorem never treats `(C,D)` as independent: it factorizes the **original plane coordinates** before the curved pushforward.

## 6. A logarithmic obstruction to the absolute spectral Fresnel endpoint

The preceding true-density bound is uniform as `a -> 0`. The next calculation shows that the absolute spectral Fresnel coefficient itself is not.

Take every original input to be `Uniform[-1/2,1/2]`, whose characteristic function is

`psi(s)=sin(s/2)/(s/2)`.                                           (6.1)

The exact three-dimensional Fresnel representation underlying Claude Theorem F, applied in the coefficient basis `(e,p,q)`, has the oscillatory dual kernel

`exp[-i u^T B^(-1)u/(4t)]
 =exp[-i(2 xi eta+zeta^2)/(4t)]`,                                  (6.2)

because `B^(-1)=B`. After taking absolute values of that dual phase, the coefficient is

`J_(a,m)
 =int_(R^3) |psi(sqrt(c)xi) psi(sqrt(a)xi)|
   product_(k=1)^m |psi(alpha_k eta+beta_k zeta)|
   dxi deta dzeta.`                                                (6.3)

The separated source banks make this exact absolute coefficient factor as

`J_(a,m)=I(a,c) P_m`,                                              (6.4)

where

`I(a,c)=int_R |psi(sqrt(c)xi) psi(sqrt(a)xi)| dxi`,               (6.5)

`P_m=int_(R^2) product_k |psi(alpha_k eta+beta_k zeta)| deta dzeta`.(6.6)

The plane factor is bounded below uniformly in `m`. On the unit disk `v=(eta,zeta)`, `|w_k dot v|<=1` and

`psi(s)>=1-s^2/24` for `|s|<=1`.                                  (6.7)

Since

`sum_k (w_k dot v)^2=|v|^2`,                                     (6.8)

and `product(1-x_k)>=1-sum x_k` for `0<=x_k<=1`,

`product_k |psi(w_k dot v)|
 >=1-|v|^2/24
 >=23/24`                                                         (6.9)

on `|v|<=1`. Therefore

`boxed: P_m>=23 pi/24.`                                           (6.10)

Now put

`r=sqrt(a/c)`,                                                     (6.11)

and substitute `x=sqrt(c)xi/2`. Then

`I(a,c)
 =(2/sqrt(c)) int_R |sin x/x| |sin(r x)/(r x)| dx
 =(4/sqrt(c)) int_0^infinity |sin x|/x |sin(r x)/(r x)| dx.`       (6.12)

For `0<=r x<=1`,

`sin(r x)/(r x)>=sin(1)`.                                         (6.13)

Let

`N=floor(1/(pi r))-1`.                                             (6.14)

For sufficiently small `a` (in particular throughout a sequence `a -> 0`) `N>=1`, and for `1<=k<=N`, the interval `[k pi,(k+1)pi]` lies in `rx<=1`. On this interval,

`int_(k pi)^((k+1)pi) |sin x|/x dx
 >= [1/((k+1)pi)] int_(k pi)^((k+1)pi)|sin x|dx
 =2/((k+1)pi).`                                                    (6.15)

Combining (6.12)-(6.15),

`boxed:
 I(a,c)
 >= [8 sin(1)/(pi sqrt(c))] (H_(N+1)-1).`                          (6.16)

Since

`N+1=floor(sqrt(c/a)/pi)`,                                        (6.17)

(6.16) diverges logarithmically as `a -> 0`. Together with (6.10),

`boxed:
 J_(a,m)
 >=[23 sin(1)/(3 sqrt(c))](H_(N+1)-1)
 -> infinity.`                                                     (6.18)

In particular,

`J_(a,m) >= [23 sin(1)/(6 sqrt(c))] log(c/a)-O(1)`                (6.19)

as `a -> 0`.

The exact absolute-Fresnel majorant therefore has a genuinely divergent coefficient in the partner's near-coloop collar, even though the true density remains below `7.60` by (5.12).

### Corollary 6.1 — `QFORM-NEAR-COLOOP-ABS-FRESNEL-LOG-BARRIER-v1`

There is no universal constant bounding the **absolute spectral Fresnel coefficient**

`int_(R^3) product_j |hat f_j(r_j dot u)| du`                     (6.20)

throughout the exact-rank-three near-coloop collar, even after all transverse physical rows are individually diffuse and even on a strict-N3 family whose actual output density is uniformly bounded.

Equivalently, the `a -> 0` blowup in the account03/B16 r24 duplicated-slice absolute-value mechanism cannot be removed merely by sharpening its Brascamp--Lieb constant to a uniform number: on the family above the exact absolute quantity being bounded already grows at least logarithmically.

This is an intermediate-mechanism counterexample, **not** a counterexample to QFORM.

## 7. What cancellation is being lost

For this family the Fresnel dual phase is explicit:

`exp[-i(2 xi eta+zeta^2)/(4t)]`.                                  (7.1)

The near-coloop divergence comes from the long frequency window

`1 << |xi| << a^(-1/2)`,                                         (7.2)

on which `|psi(sqrt(a)xi)|` is still of order one while the hub factor contributes the nonintegrable envelope `|psi(sqrt(c)xi)|~|sin(sqrt(c)xi/2)|/|xi|`. The oscillatory factor `exp[-i xi eta/(2t)]` couples exactly this long hub frequency to the transverse source direction. Taking its absolute value destroys that cancellation and produces the harmonic sum (6.16).

The completed mixed-hub theorem avoids the loss by integrating the genuinely independent hub/source-bank variable before applying Hausdorff--Young and Brascamp--Lieb to the original light product factors. That is why (5.10) stays uniform while (6.18) diverges.

So the remaining partner-r26 implication cannot be closed by a uniformly bounded **absolute** three-dimensional spectral Fresnel integral. A successful overlap theorem must preserve either this hub/transverse modulation or an equivalent real-space source factor until after the curved payment.

## 8. Relation to the bounded two-dimensional projection

The construction also isolates the precise role of the two-dimensional product marginal. Equation (4.5) is genuinely useful only because the scalar `T` is independent of the **whole pair** `(C,D)`. The curved kernel then retains a `D^2` direction and the source scalar is integrated without an arbitrary pair-dependent nonlinear shear.

If one keeps merely the facts

`||p_(C,D)||_infinity<=2`,
`sup_(c,d)||p_(T|C=c,D=d)||_infinity<=L`,                          (8.1)

but discards how `T` is generated from a disjoint original-coordinate bank, the live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` correction shows that logarithmic cancellation counterexamples exist. Thus the usable invariant is not “bounded 2D projection + bounded conditional scalar”; it is the **product provenance of the scalar against the entire projected pair**, or a Fourier substitute that retains the same modulation.

## 9. First unpaid implication after this run

The designated partner has reduced its exact-rank-three residual geometry to `c>63/64`. This run shows:

1. a many-direction strict-N3 subfamily in that collar is uniformly paid (`<7.60`) by a legitimate product-bank compression followed by the completed Claude mixed-hub theorem;
2. the two-dimensional projected coordinates may remain dependent throughout;
3. the exact absolute spectral Fresnel coefficient nevertheless diverges like `log(1/a)`;
4. therefore the missing general near-coloop bridge must be **phase-sensitive / modulation-stable** and must handle the case where the residual longitudinal coefficient `s_j` and transverse coefficients `w_j` live on the same original coordinates.

A precise next target is:

`QFORM-NEAR-COLOOP-OVERLAP-MODULATION-v1` — for rows

`r_i=sqrt(c)e`, `r_j=s_j e+w_j`,

with `c>63/64`, `sum s_j^2=1-c`, `sum s_j w_j=0`, `sum w_jw_j^T=I_2`, and the strict-N3 near-null spectral block, prove a uniform curved-pushforward bound while retaining the common-source modulation between `s_j` and `w_j`. Any proof that first takes absolute value in the full spectral Fresnel variable is ruled out by Corollary 6.1.

Arbitrary additional spectrum remains a separate global interaction debt after exact rank three. No full-target solution is claimed.

## 10. Status

- `QFORM-NEAR-COLOOP-ABS-FRESNEL-LOG-BARRIER-v1`: **proved** as an intermediate-mechanism obstruction.
- Constructed stress family: **valid exact-rank-three / strict-N3 / many-direction / source-product family**.
- True-density bound on that family: **proved**, `||p_Q||_infinity<7.60`, with the required Claude Theorem H applied explicitly.
- Designated partner account03/B16 r26: **applied** to identify the exact remaining collar and verify the construction lies after its paid exits.
- Projected coordinates `(C,D)`: **not assumed independent**.
- Full QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**.
- Native learned-memory receiver use: **not verified; execution remains WITHOUT_VERIFIED_BRAIN**.
