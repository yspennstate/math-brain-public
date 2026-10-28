SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T04:16:54Z.
attacking: the concentrated-row endpoint of decoupled time integrability — keep the hub unsymmetrized, sharpen its half-Frostman estimate, and feed it directly into the physical-pair logarithmic kernel instead of losing exponent at a quarter-Riesz detour.

# account02/B03 — concentrated-row endpoint via half-Frostman hub smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Run: `20260923T041654Z-account02-B03-QFORM-auto11`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full universal QFORM theorem remains open. This report closes a real endpoint left open by the preceding B03 volume-marginal splice: when a residual cross block is concentrated on a single physical row, its volume-sampling row marginal is exactly one, so the decoupled weighted-Riesz theorem cannot reach the required strict fractional endpoint. Keeping that physical row as a genuine independent hub instead yields a uniform half-power small-ball estimate; the completed indefinite-pair logarithmic theorem then converts it directly to a linear small-ball/density bound.

No sum/difference conjugate variables are declared independent. No post-rotation independence, moment, support, log-concavity, connected-support, Gaussian, or law-uniform pointwise stationary-phase hypothesis is used.

## 1. Source pins and correction boundary


Required pinned Claude package actually read:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`;
- same commit/directory `FOURIER_ROUTE_REPORT.md`;
- same commit/directory `COUNTEREXAMPLE_SEARCH.md`.

The completed result from that package applied below is the physical indefinite-pair logarithmic transducer: after completing an invertible indefinite original-coordinate pair `B`, if its residual `R` obeys

`sup_s P(|R-s|<=rho) <= H sqrt(rho)`,                                  (1.1)

then, with `D=|det B|` and `kappa=sigma_min(B)`,

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.                      (1.2)

The newest designated partner actually consumed is account03/B03 r25:

`yspennstate/math-open-problems@f445f3dd7e2b845f96ac58cc4bd96f12ec7a839c:proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260923T031216Z-account03-B03-QFORM-r25/REPORT.md`.

It proves the dependence-safe parabolic-hub small-ball mechanism for `aX^2+LX+S`, and its independent-copy weighted Riesz identity. This report sharpens its universal constant and uses the stronger half-Frostman exponent directly rather than degrading it to a quarter-power small-ball bound.

Corrections explicitly respected include `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, the false arbitrary-joint coarea route, the false law-uniform scalar pointwise Fresnel route, and `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`. In particular, the present proof does **not** claim the endpoint one-copy half-Riesz potential is finite; it uses a half-power small-ball estimate inside a logarithmic kernel.

## 2. Sharpened parabolic-hub half-Frostman lemma

### Lemma 2.1 — `QFORM-PARABOLIC-HUB-FROSTMAN-SHARPENED-v1`

Let `X` be real with density at most one. Let `Y` be independent of `X`. Let `L=L(Y)` have density at most `M<infinity`, and let `S=S(Y)` be arbitrary measurable and finite a.s.; `L` and `S` may be arbitrarily dependent. For any real `a` set

`R=aX^2+LX+S`.

Then for every `epsilon>0`,

`boxed: sup_z P(|R-z|<=epsilon) <= 6 sqrt(2) sqrt(M epsilon).`            (2.1)

This improves the partner r25 constant `4(1+sqrt(3))` without changing any hypothesis.

### Proof

The partner proof already gives the case `a=0` with constant `4`. Suppose `a!=0`, put `A=|a|` and `r=AM`. Complete the square and split at a parameter `K>1` into a near-critical region and a far-critical region exactly as in account03/B03 r25. Its two elementary estimates combine to

`P(|R-z|<=epsilon)`
` <=4 sqrt(M epsilon) [ sqrt(r(K+1)) + 1/sqrt(r(K-1)) ].`                (2.2)

No condition on `S` is used: in the near piece one fixes `X=x`, discards the `S` condition, and uses only the marginal density cap of `L`; in the far piece one conditions on `Y` and bounds the total `X`-length of a quadratic sublevel set.

If `r<=1/9`, choose `K-1=1/r`. Then

`P(|R-z|<=epsilon)`
` <=4[ sqrt(1+2r)+1 ] sqrt(M epsilon)`
` <=4[1+sqrt(11)/3] sqrt(M epsilon)`
` <6 sqrt(2) sqrt(M epsilon).`                                         (2.3)

If `r>=1/9`, use instead the unconditional scalar quadratic sublevel estimate, valid for every fixed `Y`,

`P(|R-z|<=epsilon) <=2 sqrt(2epsilon/A)`
` =2 sqrt(2) r^(-1/2) sqrt(M epsilon)`
` <=6 sqrt(2) sqrt(M epsilon).`                                       (2.4)

Together with the linear case this proves (2.1). QED.

## 3. Product-source specialization and dependence-safe time integral

Let `Y=(Y_1,...,Y_m)` have independent coordinate densities at most one, let `mvec!=0`, and put

`L=2 mvec^T Y+beta`.

The completed one-dimensional projection-density theorem used in partner r25 gives

`||p_L||_infinity <=1/(sqrt(2)||mvec||_2)`.                            (3.1)

Therefore every

`R=aX^2+X(2mvec^T Y+beta)+S(Y)`                                      (3.2)

satisfies

`boxed: sup_z P(|R-z|<=epsilon)`
` <= H_m epsilon^(1/2),`

`H_m=6*2^(1/4)||mvec||_2^(-1/2).`                                    (3.3)

This is uniform in the hub diagonal `a` and in arbitrary dependence between the linear coefficient and `S(Y)`.

For every `0<gamma<1/2`, (3.3) implies by layer cake

`sup_z E|R-z|^(-gamma) <= H_m^(2gamma)/(1-2gamma).`                    (3.4)

Let `R'` be an independent copy and `phi_R(t)=E exp(itR)`. Conditioning on `R'` preserves (3.4), and the exact one-dimensional Riesz-energy identity gives

`int_R |t|^(gamma-1)|phi_R(t)|^2 dt`
` =2 Gamma(gamma) cos(pi gamma/2) E|R-R'|^(-gamma)`
` <= [2 Gamma(gamma) cos(pi gamma/2)/(1-2gamma)] H_m^(2gamma).`        (3.5)

This is the requested decoupled-time estimate. It retains the entire dependence inside the physical pair `(R,R')`; no sum/difference factorisation is used.

At `gamma=1/4`,

`boxed: int_R |t|^(-3/4)|phi_R(t)|^2 dt`
` <=35.789924888102114... ||mvec||_2^(-1/4).`                         (3.6)

The partner r25 constant at the same endpoint was `40.616457689...`; the improvement is solely the sharper half-Frostman constant above.

Equation (3.5) is deliberately subcritical at `gamma<1/2`. The live correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` warns that a one-copy `gamma=1/2` endpoint need not be finite. The linear small-ball conclusion below does not require that false endpoint.

## 4. Main splice: a physical indefinite pair plus one concentrated residual cross row

### Theorem 4.1 — `QFORM-INDEFINITE-PAIR-PARABOLIC-HUB-HALF-FROSTMAN-v1`

Let two original coordinates form an invertible indefinite physical principal block `B`. Complete this pair, so the remaining original-coordinate residual is a quadratic-plus-linear polynomial `R`. Suppose among the residual coordinates there is one genuine physical hub `X`, independent of the other residual coordinates `Y`, for which

`R=aX^2+X(2mvec^T Y+beta)+S(Y)`,                                     (4.1)

with `mvec!=0`; `S(Y)` is arbitrary. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Then the full ambient quadratic form satisfies

`boxed: ||p_Q||_infinity`
` <= 8 sqrt(3) 2^(1/8) (D kappa ||mvec||_2)^(-1/4)`
` =15.11051839218372... (D kappa ||mvec||_2)^(-1/4).`                 (4.2)

Consequently every interval `I` obeys the linear small-ball estimate

`P(Q in I) <=15.11051839218372... (D kappa ||mvec||_2)^(-1/4)|I|.`    (4.3)

### Proof

By (3.3), the residual obeys (1.1) with

`H=6*2^(1/4)||mvec||_2^(-1/2)`.                                     (4.4)

Apply the completed physical-pair logarithmic transducer (1.2) from the pinned Claude package:

`||p_Q||_infinity`
` <=4 sqrt(2H)(D kappa)^(-1/4)`
` =8 sqrt(3)2^(1/8)(D kappa ||mvec||_2)^(-1/4).`

No endpoint Riesz potential is invoked. QED.

### Why this is a new endpoint relative to the preceding B03 theorem

The previous account02/B03 theorem used the partner's volume-marginal weighted Riesz estimate on a residual cross block `M`, with row energy marginal

`h=max_i sum_j M_ij^2/||M||_F^2<1`.

When all cross energy lies in one residual physical row, `h=1`. Its parameter is then `q=2`, so the decoupled exponent `a=1/(2q)=1/4`; the required strict condition `gamma<a` rules out the quarter endpoint. Thus that mechanism genuinely stops at the concentrated-row boundary.

Theorem 4.1 closes this boundary by *not decoupling away the hub coordinate*. It uses its original independence and the density of the linear projection `2mvec^T Y` to obtain (3.3). Hence the two mechanisms are complementary rather than duplicate.

## 5. Matrix-form corollary after a Schur completion

Let `P={p,q}` be an original-coordinate pair with invertible indefinite block `B=A[P,P]`. Let

`S=A[P^c,P^c]-A[P^c,P] B^(-1) A[P,P^c]`                         (5.1)

be its Schur complement. Suppose some residual coordinate `h in P^c` has nonzero off-diagonal Schur row

`mvec=(S_hj)_(j in P^c\{h})`,                                    (5.2)

with Euclidean norm `ell=||mvec||_2>0`.

Conditioning/completing the physical pair produces arbitrary affine terms but leaves the remaining original coordinates independent. The residual then has exactly the form (4.1). Therefore

`boxed: ||p_(X^T A X)||_infinity`
` <=8 sqrt(3)2^(1/8) [ |det B| sigma_min(B) ell ]^(-1/4).`          (5.3)

All quadratic curvature inside the nonhub residual bank is allowed; it is absorbed into `S(Y)`. The statement is product-coordinate and does not rotate the inputs.

## 6. Actual target-family application: the h=1 endpoint is paid uniformly

For any integer `m>=1`, any real `a`, and any vector `v in R^m` with `||v||_2=1`, define

`B0=[[0,1],[1,0]]`,

`H_(a,v)=[[a, v^T],[v, 0_(m x m)]]`,

`A_(a,v)=B0 direct_sum H_(a,v).`                                  (6.1)

The eigenvalues of `B0` are `+1,-1`. The only nonzero eigenvalues of `H_(a,v)` are the roots of

`lambda^2-a lambda-1=0`,                                          (6.2)

whose product is `-1`; hence at least one has modulus at least one. Therefore **every** `A_(a,v)` satisfies the owner target with at least three eigenvalues of modulus at least one, for every `m`, every `a`, and every orientation of the unit star vector `v` in the original leaf coordinates.

Complete the first physical pair. It has

`D=1`, `kappa=1`.                                                  (6.3)

The residual hub row is exactly `v`, so `ell=1`. Theorem 4.1 yields

`boxed: ||p_(X^T A_(a,v) X)||_infinity <=15.11051839218372...`      (6.4)

for all independent cap-one input laws, uniformly in `m`, `a`, and `v`.

This family is an exact stress test for the endpoint just discussed: if one tries the preceding one-volume decoupling with `I={hub}` and `J={leaves}`, the only row marginal equals one, `h=1`, so its strict weighted-Riesz endpoint is unavailable. The present theorem supplies a dimension-free bound precisely there.

## 7. Relation to the partner r25 quarter-power splice

Partner r25 first converted its half-power residual bound to a quarter-power small-ball bound and then applied the earlier account02/B03 quarter-power indefinite-pair transducer, obtaining

`15.8340375409... D^(-1/3) kappa^(-1/6) ||mvec||_2^(-1/6).`       (7.1)

That statement remains valid. The present route notices that the pinned pair-log theorem already accepts the stronger half-power small-ball estimate directly. This gives the scale-homogeneous alternative

`15.1105183922... (D kappa ||mvec||_2)^(-1/4).`                   (7.2)

Neither bound uniformly dominates the other for all anisotropic parameter triples, so both should be retained. At balanced unit scale (7.2) is smaller and, more importantly, it identifies the concentrated-row endpoint as a half-Frostman/logarithmic-kernel phenomenon rather than an endpoint half-Riesz problem.

## 8. First remaining unpaid implication

This run pays the **analytic** concentrated-row endpoint once a quantitatively controlled indefinite physical pair and a nonzero Schur cross row are present. It does not prove that the bare three-large-eigenvalue hypothesis forces such a pair with universal `D`, `kappa`, and `ell`.

The first target-level debt is therefore structural and quantitative: in N3 / no-pivot survivors, derive an exhaustive product-preserving alternative that yields at universal scale one of

1. a diffuse 3-volume / 5-volume exit from the pinned decoupling package;
2. a mixed-hub or grouped-bank Fresnel exit;
3. an indefinite physical pair whose Schur residual has either a diffuse one-volume certificate (`h<1`) or the concentrated-row certificate (5.2);
4. another already-paid ridge / exact-coloop / bounded-core exit.

A single well-conditioned physical minor or universal cross-rank-three cut is known not to be forced, so that false localization route is not revived.

Independent review status: **not independently reviewed in this run**. Full QFORM remains **OPEN**. Essential boundedness is proved in the stated splice scope; continuity is not claimed by this argument.
