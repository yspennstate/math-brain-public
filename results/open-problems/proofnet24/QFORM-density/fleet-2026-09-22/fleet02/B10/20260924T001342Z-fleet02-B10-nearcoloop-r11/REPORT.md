# fleet02/B10 — conditional hyperbolic-square receiver and a genuine mixed-row null-hub chamber

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** rank-three coupled case / complementary constructions and source-valid counterexamples  
**Status:** `PROVED_SUPPORTING_LEMMA / EXACT-NULL-MIXED-ROW-SUBCHAMBER-CLOSED / FULL_QFORM_OPEN`  
**Target:** independent physical coordinates with densities at most one; symmetric quadratic form with at least three eigenvalues of modulus at least one. No moment, support, log-concavity, diagonal-basis, or post-rotation-independence assumptions are used. Continuity is not claimed.

## 1. First unpaid implication

The live partner reduction leaves an exact-rank-three near-coloop state

`Q = alpha Z^2 + 2 Z (m dot P) + P^T N P`,

where `Z=sqrt(c)H+T`, `c>63/64`, `H` is one ORIGINAL physical coordinate, and `(T,P)` is an original-leaf linear image. The partner's adapted-hub theorem gives a uniform conditional cap for `Z` given `P`, but the generic two-bank receiver is still unpaid because the two transverse bank outputs can each share original coordinates with longitudinal leakage.

The first unpaid implication at the start of this run was therefore the endpoint-stable mixed-row receiver, without paying `rho^{-gamma}`, a fiber supremum, or a single tiny minor. This report proves the receiver when the contamination is one-sided: all longitudinal leakage is allowed to be arbitrarily entangled with the hub-coupling transverse scalar, while the second transverse scalar comes from a disjoint clean original bank. The remaining debt is precisely the bidirectional-contamination case.

## 2. Source results actually consumed

The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its ruled-level-set theorem says that for exact rank three of signature `(+,+,-)`, with all three spectral magnitudes at least one, the majority-sign levels satisfy

`p_Q(s) <= pi*sqrt(2),  s>=0`,

and this is source-valid because the proof controls line integrals of the projected density by two-dimensional marginals of the ORIGINAL product law, not by declaring spectral coordinates independent.

The latest compatible named partner result read before this proof was fleet03/B10

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T221626Z-fleet03-B10-QFORM-r25/REPORT.md`

at the then-current source head `6fc3fd9ab1c296c1590d76991577dbfa22f04a76`. Its adapted-hub cap is used below at an actual inequality: in the near-coloop state, the joint law of `(Z,P)` is dominated by `c^(-1/2)` times the law of `P`; hence every marginal conditional cap obtained by forgetting components of `P` is also at most `c^(-1/2)`.

The standard scalar Ball--Rogozin projection fact, also recorded in earlier fleet03/B10 work, is used in the form

`||p_{sum a_i X_i}||_infinity <= sqrt(2)` whenever `sum a_i^2=1` and the `X_i` are independent with density caps one.

## 3. A conditional-cap hyperbolic-square receiver

### Theorem 3.1 — `QFORM-CONDITIONAL-HYPERBOLIC-SQUARE-RECEIVER-v1`

Let `(Z,Y)` have a joint density satisfying

`p_{Z,Y}(z,y) <= K_Z p_Y(y)` a.e.,          (3.1)

and assume `||p_Y||_infinity <= K_Y`. Let `W` be independent of the pair `(Z,Y)` with `||p_W||_infinity <= K_W`. For real `b,c0` and nonzero real `s,d`, put

`Q0 = 2s ZY + bY^2 + 2c0 YW + dW^2`.         (3.2)

Then `Q0` has an essentially bounded density and

`||p_Q0||_infinity <= 4 sqrt(2) K_W sqrt(K_Z K_Y) / sqrt(|s d|)`.       (3.3)

No independence between `Z` and `Y` is assumed.

#### Proof

Complete the `W` square and absorb the resulting `Y^2` term by a `Y`-dependent translation of `Z`:

`W' = W + (c0/d)Y`,

`beta = b - c0^2/d`,

`Z' = Z + beta Y/(2s)`.

Then

`Q0 = 2s Z'Y + d(W')^2`.                      (3.4)

For each fixed `Y=y`, the conditional law of `Z'` is a translate of the conditional law of `Z`, hence still has density at most `K_Z`. Because the original `W` is independent of `(Z,Y)`, conditional on `Y=y` the variables `Z'` and `W'` are independent, and the conditional density of `W'` is a translate of `p_W`, hence has cap `K_W`.

For a scalar random variable `V` with density cap `K`, decreasing rearrangement gives the sharp elementary half-potential estimate

`sup_a E |V-a|^(-1/2) <= 2 sqrt(2K)`.          (3.5)

Indeed the maximizing cap-`K` density occupies an interval of length `1/K` centered at the singularity.

Fix `y != 0`. The variable `U=2s y Z'` has conditional density cap

`K_U <= K_Z/(2|s y|)`.                       (3.6)

Also the conditional density of `d(W')^2` is bounded, on its natural half-line, by

`K_W / (sqrt(|d|) sqrt(|v|))`.                (3.7)

Therefore, using conditional independence and (3.5), for every output value `q`,

`p_{Q0|Y=y}(q)`

` <= K_W/sqrt(|d|) * E[|q-U|^(-1/2) | Y=y]`

` <= 2 K_W sqrt(K_Z) / (sqrt(|s d|) sqrt(|y|))`.                       (3.8)

A second use of (3.5), now with the marginal cap `K_Y`, gives

`E |Y|^(-1/2) <= 2 sqrt(2K_Y)`.                (3.9)

Integrating (3.8) in `y` yields (3.3). The null set `y=0` is irrelevant because `Y` has a density. This also supplies absolute continuity. QED.

### Why this is stronger than the independent-three-scalar receiver

The proof spends only a **conditional cap** for the hyperbolic factor `Z` given `Y`. Thus `Z` and `Y` may be strongly dependent because they share the same original coordinate bank. Independence is required only for the square-smoothing bank `W`, and that independence will be supplied below by disjoint ORIGINAL coordinates.

This is exactly the kind of dependence permitted by the current near-coloop geometry and forbidden from being simplified by spectral rotation.

## 4. Exact-null near-coloop geometry with one genuinely mixed bank

Work in exact rank three. Write

`A = R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`.

Choose a unit spectral direction `e` carrying one physical hub row

`u_0 = sqrt(c) e`, `c>63/64`,

and assume the hub spectral pivot is exactly null:

`e^T M e = 0`.                                (4.1)

Let `m = (I-ee^T)Me`, put `r=||m||`, and choose the transverse orthonormal basis

`u=m/r`, `v perpendicular to both e and u`.

Suppose the remaining ORIGINAL physical coordinates split into disjoint banks `B` and `C` with rows

`u_i = t_i e + y_i u`,       `i in B`,

`u_j = w_j v`,               `j in C`.          (4.2)

Thus all longitudinal leakage may share original variables with the `u`-transverse bank, while the `v`-bank is clean. Parseval `R^T R=I` gives

`sum_B t_i^2 = 1-c =: rho`,

`sum_B y_i^2 = 1`,

`sum_B t_i y_i = 0`,

`sum_C w_j^2 = 1`.                             (4.3)

For the corresponding independent source coordinates define

`H=X_0`,

`T=sum_B t_i X_i`,

`Y=sum_B y_i X_i`,

`W=sum_C w_j X_j`,

`Z=sqrt(c)H+T`.                                (4.4)

Crucially, `T` and `Y` are **not** assumed independent. They are two linear observables of the same original bank. The variable `W`, however, is genuinely independent of the entire pair `(Z,Y)` because bank `C` is disjoint from the hub and bank `B`.

In the spectral basis `(e,u,v)`, symmetry and the definition of `u` give

`M = [[0,r,0],[r,a,b],[0,b,d]]`.               (4.5)

Consequently

`Q = 2r ZY + aY^2 + 2bYW + dW^2`.             (4.6)

Two spectral-gap consequences are quantitative and require no norm upper bound:

1. `r=||Me||>=1`, because `sigma_min(M)>=1`.
2. `|d|>=1`. Indeed `det M=-r^2 d`, and direct inversion of (4.5) gives `(M^{-1})_{vv}=1/d`. Since `||M^{-1}||<=1`, one has `|1/d|<=1`.

Hence

`|r d|>=1`.                                    (4.7)

The partner's adapted-hub result applies to the actual inequality

`p_{Z,P}(z,p) <= c^(-1/2) p_P(p)`,             (4.8)

with `P=(Y,W)`. Marginalizing `W` yields

`p_{Z,Y}(z,y) <= c^(-1/2) p_Y(y)`.             (4.9)

This is also evident directly by conditioning the original bank `B`: `sqrt(c)H` is an independent cap-`c^(-1/2)` additive component of `Z`, but (4.8) records that this is exactly the partner mechanism used in the live near-coloop reduction.

Ball--Rogozin and (4.3) give

`K_Y<=sqrt(2)`, `K_W<=sqrt(2)`.                (4.10)

Apply Theorem 3.1 to (4.6), with `K_Z=c^(-1/2)`, `s=r`, and square coefficient `d`. By (4.7),

`||p_Q||_infinity`

` <= 4sqrt(2)*sqrt(2)*sqrt(c^(-1/2)*sqrt(2))`

` = 8*2^(1/4)c^(-1/4)`

` < 8*(128/63)^(1/4)`

` < 9.552`.                                     (4.11)

This bound is uniform in the leakage mass `rho=1-c`, including the endpoint `rho=0`. It contains no `rho^(-gamma)`, no component-count/BV/layer-cake functional of the hub density, no conditional profile supremum, and no selected physical minor.

### Theorem 4.1 — `QFORM-EXACT-NULL-ONE-MIXED-BANK-CLOSURE-v1`

Under (4.1)--(4.3), for arbitrary independent cap-one physical source densities,

`||p_Q||_infinity < 9.552`.                    (4.12)

The theorem is an essential-density statement only; continuity remains separate.

## 5. A concrete diffuse-leaf target family inside the live survivor

The preceding theorem is not a formal edge case. It contains a family satisfying the diffuse-leaf numerical chamber used by the partner.

Fix `0<rho<1/64`, `c=1-rho`. Take the hub row `sqrt(c)e_1`. In bank `B`, take 128 rows

`u_i = epsilon_i sqrt(rho/128) e_1 + (1/sqrt(128)) e_2`,

with 64 signs `epsilon_i=+1` and 64 signs `epsilon_i=-1`. In bank `C`, take 64 rows

`u_j = (1/8)e_3`.                              (5.1)

Then (4.3) holds exactly. Every transverse leaf leverage is at most `1/64<1/61`; the `B` leaves have leverage `1/128`. Let

`M = [[0,1,0],[1,0,0],[0,0,1]]`.               (5.2)

The exact nonzero spectrum is `{-1,1,1}`. Writing

`T=sqrt(rho/128) sum_i epsilon_i X_i`,

`Y=(1/sqrt(128)) sum_i X_i`,

`W=(1/8)sum_j X_j`,                             (5.3)

one gets

`Q=2(sqrt(c)H+T)Y+W^2`.                        (5.4)

The pair `(T,Y)` uses the SAME 128 original coordinates and is not declared independent; only `W` is separated by original-coordinate support. Theorem 4.1 gives

`||p_Q||_infinity < 9.552`                      (5.5)

for arbitrary independent cap-one source laws.

This is a genuine mixed-row endpoint closure beyond the previous pure-longitudinal test family, where leakage came from a bank disjoint from the hyperbolic transverse scalar.

## 6. Required ruled-side theorem applied to the same family

For the concrete family (5.1)--(5.4), the exact spectrum has signature `(+,+,-)`. Therefore the completed ruled theorem at the required source pin gives the sharper one-sided inequality

`p_Q(s) <= pi sqrt(2) < 4.443,  for every s>=0`.                       (6.1)

Thus the pinned source theorem pays the majority-sign side directly. The new receiver supplies, in this mixed-bank chamber, the two-sheet side that the ruled theorem intentionally does not cover, and does so without any post-rotation independence assumption.

## 7. Exact boundary of the new argument

The proof breaks for a mathematically meaningful reason, not a bookkeeping gap. If the second transverse bank also carries longitudinal leakage, write

`Z=sqrt(c)H+T_B+T_C`,

where `(T_B,Y)` share bank `B` and `(T_C,W)` share bank `C`. Parseval only forces the coefficient vectors of `T_C` and `W` to be orthogonal; for arbitrary non-Gaussian cap-one product input this does **not** make the projected variables independent. Then `W` is no longer independent of `(Z,Y)`, so Theorem 3.1 cannot be invoked.

A concrete diffuse frame realizing exactly this obstruction is obtained by using 128 signed leakage rows in each of the two transverse banks, with half the total leakage energy in each bank and balanced signs so every longitudinal/transverse coefficient inner product is zero. All transverse leverages can remain below `1/61`. Hence the obstruction is present inside the live near-coloop chamber and cannot be removed by a scalar-pivot or leverage threshold.

The next implication is therefore

`QFORM-EXACT-NULL-BIDIRECTIONAL-MIXED-BANK-RECEIVER-v1`:

prove a uniform density bound for the exact-null normal form when **both** transverse banks carry longitudinal leakage, retaining each bank as an original-coordinate product-linear object. Equivalently, extend Theorem 3.1 so that the square-smoothing observable may share its original bank with an orthogonal leakage observable, without replacing orthogonality by independence and without paying the leakage scale.

This is a strict refinement of the partner's generic `QFORM-TWOBANK-MIXEDROW-TRIANGULAR-RECEIVER-v1`: one-sided contamination is now paid; bidirectional same-bank contamination is the remaining endpoint debt.

## 8. Scope

The full arbitrary-orientation / at-least-three-large-eigenvalue QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The report proves a dependence-tolerant analytic receiver and closes an exact-null near-coloop subchamber. It does not establish a law-uniform perturbation from `alpha=0` to `alpha!=0`; such a step would be invalid if justified only by small coefficient size, because the target assumes no moments or support bounds. It does not assert continuity of the output density.
