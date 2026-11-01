SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B04, 2026-09-22T18:54:16Z.
attacking: aggregate-before-inversion for a square plus a rank-one cross-bank packet, using hyperbolic-product decreasing rearrangement in L^3 and a square L^(3/2) endpoint to obtain a dimension-free continuous-density bound.

# fleet03/B04 — L^3 hyperbolic rearrangement and square-plus-cross-bank closure

**Run:** `B04-20260922T185416Z-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Product Fourier rearrangement  
**Control observed at start:** owner revision `2026-09-22.11`; QFORM remains the sole target.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL_TARGET_OPEN`

## 1. Target, source status, and first unpaid implication

The unrestricted target remains open: for independent real physical coordinates with densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free density cap for `X^TAX`, or give a true target-level counterexample. Continuity is tracked separately.

The previous B04 run refuted the unweighted scalar-conditioning supremum gate. The live proof-first request instead prioritizes aggregate-before-inversion mechanisms that preserve original-coordinate product structure. This run attacks that branch directly. The new result below pays an entire rank-one cross bank at its aggregate singular scale `sigma=||u||_2||v||_2`, even when every individual physical coefficient tends to zero, and couples it to one independent quadratic square using a conjugate `L^3`/`L^(3/2)` smoothing argument.

This is not the full theorem. It closes an exact rank-three rotated family with eigenvalues `{a,+sigma,-sigma}` and supplies a quantitative packet that can be inserted into a larger exhaustive reduction.

## 2. Completed mathematics actually consumed

### 2.1 Hyperbolic-product envelope and rearrangement source

The completed fleet01/B04 report

`yspennstate/math-open-problems@efe730532ded82011b532f5ac8b443768f04a086`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260922T181620Z-fleet01-B04-QFORM-r15/REPORT.md`

proves, from the fleet02/B04 translated hyperbolic-product envelope, that for independent cap-one `U,V`, any `c!=0`, and arbitrary deterministic translations, the density `g_c` of `2cUV` obeys

`g_c(s) <= |c|^(-1)[1+log_+(2|c|/|s|)]`.                    (2.1)

It then uses probability-mass rearrangement to derive an `L^2` bound. The present run applies the same source-valid envelope but changes exponent to `3`; the resulting exact constant is computed below.

### 2.2 Rank-one original-coordinate bank lift

The completed fleet02/B04 report

`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T181702Z-dac07509/REPORT.md`

records the one-dimensional product-projection estimate: for disjoint original-coordinate banks `I,J`,

`U=u^T X_I`, `V=v^T X_J`, `s=||u||_2`, `t=||v||_2`,

one has

`||p_U||_infinity <= sqrt(2)/s`, `||p_V||_infinity <= sqrt(2)/t`.  (2.2)

Because the banks are disjoint, `U,V` are independent. The same report rescales these bank variables to cap-one scalar variables and pays the aggregate scale `sigma=st`, not a single entry `u_i v_j`. Equation (2.2) is applied quantitatively in Theorem 5.1 below.

### 2.3 Designated partner status

The designated partner is `fleet04/B04`. A fresh repository search before publication found no completed QFORM report or handoff from that slot; its visible B04 commits were older FEI/BT4 work. I therefore did not fabricate a partner result or wait for it. The compatible completed same-role results above are the mathematics actually consumed.

## 3. New `L^3` rearrangement for a hyperbolic product

Let `z>2` be the unique root

`4 z exp(-(z-2)) = 1`.                                       (3.1)

Numerically,

`z = 4.994664629781440392391150218754047...`.                (3.2)

Define

`K_3 := z^2 + 3 + 2/z
      = 28.347102049552591121354462869450197...`.            (3.3)

### Lemma 3.1 — `QFORM-HYPERBOLIC-PRODUCT-L3-v1`

Let `U,V` be independent real random variables with densities bounded by one, let `c!=0`, and allow arbitrary deterministic translations of either input. If `g_c` is the density of the translated product term `2cUV`, then

`||g_c||_3^3 <= K_3 |c|^(-2)`,                              (3.4)

hence

`||g_c||_3 <= K_3^(1/3)|c|^(-2/3)`,                         (3.5)

with

`K_3^(1/3)=3.0490851703865357279962999027569665...`.

#### Proof

From the completed envelope (2.1),

`0 <= g_c(s) <= k_c(s):=|c|^(-1)[1+log_+(2|c|/|s|)]`,
`integral g_c = 1`.                                          (3.6)

Write `L=z-2` and `a=e^(-L)`. By (3.1),

`4a(L+2)=1`.                                                  (3.7)

Set `r=2|c|a`. Direct integration on the high-cap region gives

`integral_{|s|<=r} k_c(s) ds = 4a(L+2)=1`.                  (3.8)

Let `g_c^*` and `k_c^*` denote decreasing rearrangements. Pointwise domination implies `g_c^*<=k_c^*`. Let `h` be the rearrangement obtained by filling the highest-cap part of `k_c^*` until exactly one unit of mass is used, equivalently the rearrangement of `k_c 1_{[-r,r]}`. Then for every `x>=0`,

`integral_0^x g_c^* <= min(1, integral_0^x k_c^*)
                     = integral_0^x h`.                     (3.9)

Thus `h` majorizes `g_c^*`. Since `u -> u^3` is convex, the standard convex rearrangement/Karamata inequality yields

`integral g_c^3 <= integral h^3
                 = integral_{|s|<=r} k_c(s)^3 ds`.           (3.10)

Substitute `s=2|c|u`. Since the integrand is even,

`integral_{|s|<=r} k_c(s)^3 ds
 = 4|c|^(-2) integral_0^a (1+log(1/u))^3 du`.                (3.11)

With `v=log(1/u)`,

`integral_0^a (1+log(1/u))^3 du
 = integral_L^infinity (1+v)^3 e^(-v) dv
 = a(L^3+6L^2+15L+16)`.                                    (3.12)

Using (3.7),

`4a(L^3+6L^2+15L+16)
 = (L^3+6L^2+15L+16)/(L+2)`.                                (3.13)

With `z=L+2`, the numerator is

`L^3+6L^2+15L+16 = z^3+3z+2`,                               (3.14)

so (3.13) equals

`z^2+3+2/z = K_3`.                                           (3.15)

Equations (3.10)--(3.15) prove (3.4). QED.

The key point is that no pointwise Fourier decay is asserted. This is a physical-density decreasing-rearrangement estimate using the exact logarithmic product envelope plus probability mass one.

## 4. A sharp-enough `L^(3/2)` square endpoint

### Lemma 4.1 — `QFORM-SQUARE-L32-v1`

Let `Z` be a real random variable with density at most one, let `a!=0`, and allow an arbitrary deterministic translation `d`. If `h_{a,d}` is the density of

`a(Z+d)^2`,

then

`||h_{a,d}||_(3/2) <= 2 |a|^(-1/3)`.                        (4.1)

#### Proof

Reflection of the output reduces to `a>0`. For `y>0`, the change-of-variables formula gives

`h_{a,d}(y)
 = [f_Z(-d+sqrt(y/a))+f_Z(-d-sqrt(y/a))]/[2 sqrt(a y)]
 <= (a y)^(-1/2)`.                                           (4.2)

Also `integral h_{a,d}=1`. Let `k(y)=(ay)^(-1/2)1_{y>0}`. The highest-cap initial interval whose `k`-mass is one is `[0,a/4]`, since

`integral_0^(a/4) (ay)^(-1/2) dy =1`.                        (4.3)

The same mass-filling rearrangement argument as above, now with the convex function `u^(3/2)`, gives

`integral h_{a,d}(y)^(3/2)dy
 <= integral_0^(a/4) a^(-3/4)y^(-3/4)dy
 = 2 sqrt(2) a^(-1/2)`.                                     (4.4)

Taking the `2/3` power yields

`||h_{a,d}||_(3/2)
 <= (2sqrt(2))^(2/3) a^(-1/3)
 =2a^(-1/3)`.                                                (4.5)

QED.

## 5. Main new aggregate theorem: one square plus one rank-one cross bank

Let `I,J,{0},W` be mutually disjoint original-coordinate groups. The inputs in all groups are independent and each scalar physical coordinate has density at most one. Put

`U=u^T X_I`, `V=v^T X_J`,
`s=||u||_2`, `t=||v||_2`, `sigma=st>0`.                      (5.1)

Allow arbitrary measurable functions `alpha(W), beta(W), d(W), R(W)` and define

`Q = a(Z+d(W))^2
    +2(U+alpha(W))(V+beta(W))
    +R(W)`,                                                   (5.2)

where `a!=0`. In an actual quadratic form these functions arise from aligned affine contamination after conditioning; the theorem is stated measurably because no additional regularity is needed.

### Theorem 5.1 — `QFORM-SQUARE-RANK1-BANK-LP-CLOSURE-v1`

Under (5.1)--(5.2), `Q` has a continuous density and

`boxed: ||p_Q||_infinity
 <= C_* (|a| sigma^2)^(-1/3)`,                               (5.3)

where

`C_* = 2^(5/3) K_3^(1/3)
     = 9.680242014024447102623670750953914...`.              (5.4)

In particular, if `|a|>=1` and `sigma>=1`, then

`boxed: ||p_Q||_infinity <= 9.681`.                          (5.5)

#### Proof

Condition on `W=w`. Because `I,J,{0},W` are disjoint original-coordinate groups, `U,V,Z` remain independent under this conditioning.

By the completed bank projection estimate (2.2),

`||p_U||_infinity <= sqrt(2)/s`,
`||p_V||_infinity <= sqrt(2)/t`.                              (5.6)

Rescale

`U'=(sqrt(2)/s)U`, `V'=(sqrt(2)/t)V`.                         (5.7)

Then `U',V'` are independent and have density caps at most one. The translated hyperbolic term becomes

`2(U+alpha)(V+beta)
 =2c(U'+alpha')(V'+beta')`,
`c=sigma/2`,                                                  (5.8)

for deterministic translated values `alpha',beta'` depending on `w`. Lemma 3.1 therefore gives its conditional density `g_w` the bound

`||g_w||_3
 <= K_3^(1/3)(sigma/2)^(-2/3)
 =2^(2/3)K_3^(1/3)sigma^(-2/3)`.                             (5.9)

Independently, Lemma 4.1 gives the translated square density `h_w` the bound

`||h_w||_(3/2) <=2|a|^(-1/3)`.                              (5.10)

The two random terms are independent conditionally on `w`, so their sum has density `h_w*g_w`, up to the deterministic translation `R(w)`. Young's convolution inequality at conjugate exponents `3/2` and `3` gives

`||h_w*g_w||_infinity
 <= ||h_w||_(3/2)||g_w||_3
 <= 2^(5/3)K_3^(1/3)(|a|sigma^2)^(-1/3)`.                   (5.11)

This bound is uniform in `w` and in all translations.

For each fixed `w`, convolution of an `L^(3/2)` function and an `L^3` function lies in `C_0(R)`: approximate either factor by compactly supported continuous functions, or use translation continuity in the conjugate norm. Thus the conditional density is continuous. Averaging these conditional densities over `W` produces a density for `Q`; the uniform bound (5.11) gives dominated convergence in `w`, so the averaged density is continuous as well. Equations (5.3)--(5.4) follow. QED.

### Why this is an aggregate-before-inversion result

The constant depends on `sigma=||u||_2||v||_2`, the singular value of the rank-one cross block `uv^T`, and not on any individual coefficient `u_i v_j`. Therefore it remains useful when every physical cross entry is arbitrarily small.

## 6. Explicit genuinely rotated indefinite exact-rank-three target family

For any integer `m>=2`, use coordinates

`(Z, X_1,...,X_m, Y_1,...,Y_m)`

with arbitrary independent densities bounded by one. Let

`u=v=m^(-1/2)(1,...,1)`,
`U=u^T X`, `V=v^T Y`.                                        (6.1)

Consider the symmetric matrix

`A_m = [1] direct_sum [[0, u v^T],[v u^T, 0]]`.              (6.2)

Equivalently,

`Q_m = Z^2 + 2UV`.                                           (6.3)

The cross block `uv^T` has singular value one. Hence the nonzero spectrum of `A_m` is exactly

`{1,1,-1}`                                                     (6.4)

and all remaining eigenvalues are zero. Thus this is an exact instance of the owner target with exactly three eigenvalues of modulus one and an indefinite genuinely rotated rank-three form.

Every individual physical cross coefficient equals `1/m`, so any reduction demanding one uniformly large original-coordinate mixed coefficient fails as `m->infinity`. Nevertheless Theorem 5.1 pays the whole bank before inversion and gives, for every admissible product input law,

`boxed: ||p_(Q_m)||_infinity <= 9.680242014024448`,           (6.5)

and the density is continuous, uniformly in `m`.

This is a target-facing branch, not a diagonal or eigen-coordinate-independence argument. The eigenvectors for `+1` and `-1` are proportional to `(0,u,+v)` and `(0,u,-v)`, so for `m>=2` they mix many original independent coordinates.

## 7. Companion two-bank-pair corollary

The completed fleet01/B04 `L^2` theorem and the same bank rescaling also give a useful four-eigenvalue packet. Suppose four disjoint original-coordinate banks yield independent rank-one cross packets with aggregate scales `sigma_1,sigma_2>0`. Conditional aligned translations are allowed as above. The scalar hyperbolic `L^2` theorem gives, after bank rescaling,

`||g_i||_2^2 <= 2K_2/sigma_i`,                               (7.1)

where

`K_2=5.1948782725628494447...`.                              (7.2)

Therefore the sum of the two packets has a continuous density with

`boxed: ||p||_infinity
 <= 2K_2/sqrt(sigma_1 sigma_2)
 = 10.389756545125699/sqrt(sigma_1 sigma_2)`.                 (7.3)

Again this pays aggregate bank singular scales rather than individual entries. This corollary is not needed for Theorem 5.1 but is useful in a future bank-routing trichotomy.

## 8. Relation to the full conjecture and first unpaid implication

The theorem above proves a dimension-free continuous-density bound for an exact rank-three rotated indefinite family with vanishing local coefficients. It therefore removes one concrete failure mode of local minor selection. It does **not** imply that every matrix with three large eigenvalues contains a square-plus-rank-one-cross-bank packet of uniformly large aggregate scale. Small or nonzero in-bank quadratic leakage also cannot be discarded under the owner hypotheses because the inputs have no moments or bounded support.

The next unpaid implication for B04 is:

`QFORM-SQUARE-CROSSBANK-ROUTING-v1` — starting from an arbitrary three-large-eigenvalue matrix in the high-leverage/near-isotropic branch, either (i) extract disjoint original-coordinate groups that realize Theorem 5.1 with `|a|sigma^2` uniformly bounded below after exact completion, or (ii) route quantitatively to the existing ridge-window, full-matrix pair, diffuse-rank-two, or multi-bank hyperbolic mechanisms, without discarding quadratic leakage or selecting a vanishing local minor.

A useful structural target is a product-preserving grouped-coordinate decomposition in which the cross part is paid in `L^p` before any reciprocal coefficient is introduced. The present theorem shows that a single square plus an aggregate rank-one cross singular value is already enough at the analytic endpoint; the remaining obstruction is structural extraction, not smoothing of this packet.

## 9. Corrections and scope checks

This run does not use:

- uniform pointwise van-der-Corput/Fresnel decay for arbitrary cap-one densities;
- independence after spectral rotation;
- the false arbitrary-joint 3D coarea bound;
- the false positive conditional-projection-density moment;
- the false scalar conditional-supremum gate from the preceding B04 run;
- a universal good principal triple/pair;
- a one-Schur-rank-two extraction theorem;
- fiberwise trace supremum bounds;
- moments, centering, log-concavity, compact support, or connected support.

The input product structure is used only on disjoint original-coordinate groups. All constants are explicit. Theorem 5.1 proves both essential boundedness and continuity in its stated scope. The unrestricted QFORM conjecture remains OPEN.

## 10. Constant verification

The numerical constants were independently evaluated at high precision from the defining equation (3.1):

`z  = 4.9946646297814403923911502187540471797135199936320`

`K2 = 5.1948782725628494447150983798124766000788416634314`

`K3 = 28.347102049552591121354462869450197463656387923190`

`K3^(1/3) = 3.0490851703865357279962999027569665066867959726881`

`C_* = 2^(5/3)K3^(1/3)
     = 9.6802420140244471026236707509539137300504219128763`.

A short checker is saved beside this report. The finite computation verifies arithmetic only; the inequalities above are the proof.
