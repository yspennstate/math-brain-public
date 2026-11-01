# fleet02/B16 QFORM r36 — fresh-hub divisible-twist absorption

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T20:31:40Z.
attacking: the true near-coloop punctured endpoint by separating the genuinely dangerous nonzero fresh-hub square from every light term that is merely divisible by the hub-partner projection.

**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Role:** projection-product interaction; preserve original-coordinate product provenance and never infer independence after projection.  
**Continuity:** separate. The main theorem below proves absolute continuity and an essential density bound; it does not by itself assert continuity.

## First unpaid implication

`QFORM-PUNCTURED-FRESH-HUB-SQUARE-STABILITY-v1`.

After the theorem below, every light term of the form `2 L T`, with `T` an arbitrary measurable function of the light source vector, can be absorbed into an untouched independent physical hub without any conditional projection-density estimate. Thus in fleet03/B16's true-near-coloop equation the zero-hub-diagonal endpoint is completely stable under arbitrary longitudinal leakage of this divisible type. The first unpaid step is specifically the addition of the small nonzero **fresh physical hub square** `alpha H^2`; fleet03/B16's caps-only counterexample shows that this step cannot be justified from a scalar conditional cap and a two-dimensional marginal cap alone. The source product structure must be retained through that square.

## Theorem — `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1`

Let `H` be a real random variable with density `f_H<=1`, independent of an arbitrary light random object `W`. Let `L=L(W)`, `V=V(W)`, and `T=T(W)` be real measurable functions. Assume only that `(L,V)` has a joint density with

`||p_(L,V)||_infinity <= M`.

Let `gamma*kappa != 0`, and let `alpha,delta` be arbitrary real numbers. Define

`Q = 2 gamma H L + 2 L T + alpha L^2 + 2 delta L V + kappa V^2`,       (2.1)

with arbitrary additional affine terms in the three displayed receiver variables allowed. Then `Q` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <= 3*2^(2/3) M^(2/3) |gamma^2 kappa|^(-1/3).
)`                                                                    (2.2)

There is no hypothesis on the law of `T`, no independence between `T,L,V`, no moment/support/log-concavity assumption, and no projected-independence assertion.

### Proof

Set

`Y = H + T/gamma`.                                                    (2.3)

Conditional on `(L,V)=(l,v)`, let `mu_(l,v)` be a regular conditional law of `T`. Since the untouched physical source `H` is independent of the entire light object `W`, the conditional density of `Y` is

`p_(Y | L,V)(y | l,v)
 = integral f_H(y-t/gamma) mu_(l,v)(dt)
 <= 1`                                                               (2.4)

for almost every `(l,v)`. This is the key provenance statement: it is an average of translates of one fixed original-source density, not a conditional density inferred from a projected joint cap.

Equation (2.1) becomes

`Q = 2 gamma Y L + alpha L^2 + 2 delta L V + kappa V^2`.              (2.5)

Its quadratic coefficient matrix in `(Y,L,V)` is

`B = [[0,gamma,0],[gamma,alpha,delta],[0,delta,kappa]]`,               (2.6)

and therefore

`det B = -gamma^2 kappa`.                                             (2.7)

Apply the completed `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1` theorem (`math-open-problems@1bbe7c7c194bc92e10fc9c3cb3eb548d65e7043d`): if the first variable has conditional density cap `K`, the remaining pair has joint density cap `M`, and `B_11=0`, then

`||p||_infinity <= 3*2^(2/3)(K M)^(2/3)|det B|^(-1/3)`.

Use `K=1` from (2.4) and (2.7). This proves (2.2). The cited theorem also gives absolute continuity. QED.

## Fresh application: the current two-bank Fourier receiver loses no logarithm in essential height

A fresh source resolved during this run is `math-open-problems@190455b1b9773b2afb4ef5551cd86885e523a9ee`, `proofnet24/QFORM-density/interactive/20260923T204100Z-two-bank-central-holder/REPORT.md`. It studies

`Q_epsilon = 2 H L + beta L^2 + V^2 + 2 epsilon L P`,                 (3.1)

with `H` independent of the light vector and proves a useful Hoelder modulus in a central negative strip, plus an all-target essential-density estimate with a `sqrt(log(1/|epsilon|))` loss.

For essential height, (3.1) is directly in Theorem (2.2): take

`gamma=1`, `kappa=1`, `T=epsilon P`, `alpha=beta`, `delta=0`.          (3.2)

Hence, as soon as `(L,V)` has joint density cap `M`,

`boxed(
 ||p_(Q_epsilon)||_infinity <= 3*2^(2/3) M^(2/3),
)`                                                                    (3.3)

uniformly in **all** real `epsilon` and `beta`, at every target level.

Under the two-bank hypotheses of that report, `(L,V)=(L_A,V_A)+(L_B,V_B)` is a sum of independent pairs with density caps `M_{2,A},M_{2,B}`. Convolution gives

`M <= min(M_{2,A},M_{2,B})`,                                         (3.4)

so (3.3) needs neither the 3D bank caps nor the logarithmic all-target loss. This does **not** invalidate the report's Hoelder/continuity estimate for its inner contribution; it only shows that its logarithmic companion bound is unnecessary for the main essential-`L^infinity` objective when the fresh-hub hypothesis is present.

## Required pinned-result application and an exact target family

The owner-pinned package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed two-dimensional product-projection input says that an orthonormal two-dimensional projection of independent cap-one originals has joint density at most `2`. Insert that actual result into (2.2): for `M<=2`,

`boxed(
 ||p_Q||_infinity
 <= 3*2^(4/3)|gamma^2 kappa|^(-1/3).
)`                                                                    (4.1)

In particular the normalized case `gamma=kappa=1` gives

`3*2^(4/3) = 7.559526299369239... < 7.56`.                            (4.2)

This is a direct product-marginal-to-curved-integral application; no independence of the two projected coordinates is inferred.

For a strict target-valid stress family, take one fresh original coordinate `H=X_0` and, on the disjoint leaf source bank, choose three orthonormal coefficient vectors `ell,v,p`. Put

`L=<ell,X'>`, `V=<v,X'>`, `P=<p,X'>`,

and for arbitrary real `epsilon` set

`Q_epsilon = 2 X_0 L + V^2 + 2 epsilon L P`.                         (4.3)

In the orthonormal carrier basis `(X_0,L,V,P)` the physical matrix is

`A_epsilon = [[0,1,0,0],[1,0,0,epsilon],[0,0,1,0],[0,epsilon,0,0]]`.

Its characteristic polynomial is

`-lambda (lambda-1)(1+epsilon^2-lambda^2)`,                         (4.4)

so its nonzero spectrum is exactly

`{1, +sqrt(1+epsilon^2), -sqrt(1+epsilon^2)}`.                       (4.5)

Thus every member has exactly three eigenvalues of modulus at least one. The pinned two-dimensional projection theorem gives `||p_(L,V)||_infinity<=2`, and (4.2) yields for arbitrary independent cap-one source laws

`boxed(
 ||p_(Q_epsilon)||_infinity < 7.56
)`                                                                    (4.6)

uniformly for all `epsilon`, including `epsilon -> 0` and `|epsilon| -> infinity`.

A second completed result from the same pinned package applies to a real side of this family: `COUNTEREXAMPLE_SEARCH.md`, Theorem C (ruled one-sheet rank-three estimate), gives because (4.5) has signature `(+,+,-)` and no out-of-range affine term,

`p_(Q_epsilon)(s) <= pi*sqrt(2) = 4.442882938158366...`               (4.7)

for almost every `s>=0`. Thus the zero-pivot absorption supplies the uniform global/negative-side control, while the pinned ruled estimate is sharper on the one-sheet side.

## Designated partner fleet03/B16 applied exactly

The latest completed compatible partner handoff is fleet03/B16 run `20260923T190206Z-fleet03-B16-QFORM-auto11b`, canonical mathematics `math-open-problems@bdbe6e38a3ee3d586e8e6119e518c573310253fb`. In its true-near-coloop coordinates,

`Q = a(sqrt(c)X_0+S)^2 + 2b(sqrt(c)X_0+S)U
     + uU^2+2vUV+wV^2`,                                             (5.1)

with `c>63/64`, `D=|det Lambda|>=1`, and `(U,V)` an orthonormal two-dimensional product projection.

At the endpoint `a=0`, (5.1) is precisely (2.1) with

`H=X_0`, `L=U`, `T=bS`, `gamma=b*sqrt(c)`,
`alpha=u`, `delta=v`, `kappa=w`.                                    (5.2)

The original physical coordinate `X_0` is independent of the full leaf source, while the pinned projection theorem gives `M<=2`. Since at `a=0`

`det Lambda = -b^2 w`,

we have

`|gamma^2 kappa| = c D`.                                            (5.3)

Therefore (2.2) gives exactly

`||p_Q||_infinity
 <= 3*2^(4/3)(cD)^(-1/3)
 < 7.6`,                                                             (5.4)

recovering the partner endpoint by a general source-translation principle. The point is structural: **all** light leakage multiplying the hub partner `U` can be absorbed into the fresh source before the nonlinear trace is paid.

For `a!=0`, however, (5.1) contains the genuinely new term `ac X_0^2`. It cannot be absorbed by (2.3). The same partner proved a caps-only counterexample for nonzero pivot and paid the outer collar `|a|D>=2^-12`; its exact remaining chamber is

`0 < |a|D < 2^-12`.                                                 (5.5)

Thus the next B16 problem is no longer generic projected dependence or generic `LP` leakage. It is specifically **stability of the fresh-hub zero-pivot trace under the nonzero physical square `acX_0^2`, while keeping the original leaf product provenance**. A proof that replaces the leaves by only a marginal/conditional cap is ruled out by the partner's counterexample.

## Status

`QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1`: **PROVED SUPPORTING THEOREM**.  
Current two-bank all-target logarithmic essential-height loss: **REMOVED under its stated fresh-hub assumptions**; its continuity/Hoelder conclusion remains separate.  
Exact target family (4.3): **UNIFORMLY CONTROLLED by <7.56 for arbitrary cap-one product laws**.  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Next exact implication: `QFORM-PUNCTURED-FRESH-HUB-SQUARE-STABILITY-v1` in the partner collar (5.5).
