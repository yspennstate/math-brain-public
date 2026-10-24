# account02/B11 — overlap-safe logarithmic pair smoothing by the exact third Schur square

Programme `QFORM-DENSITY-3EIG-20260922`. Worker `account02/B11`, indefinite signatures. Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / EXACT TARGET-VALID INTERPOLATION FAMILY / PARTNER_RESULT_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

The full conjecture remains open. The new theorem below is for the exact-rank-three indefinite branch with a quantitative ORIGINAL-coordinate indefinite pair. It does not handle arbitrary additional spectrum, and it does not assert a uniformly good pair exists. Its point is to close the overlap defect left by the preceding disjoint-bank argument: the same residual coordinates may translate the pair and carry the third square.

## 1. First unpaid implication and source map

The first unpaid implication entering this run was the genuinely overlapping third-direction problem. After Schur completion of a physical indefinite pair, the rank-one third direction lives on the remaining original coordinates, but those same coordinates also translate the two pair variables. One may not declare the translated pair independent of the third scalar.

Sources actually used at equations:

* Pair logarithmic envelope and moving-centre framework: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`, especially (3.1) and Section 4.
* Required pinned Claude package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C (ruled one-sheet estimate). `RESULTS.md` and `FOURIER_ROUTE_REPORT.md` were also read at that snapshot.
* Designated partner, latest compatible account03/B11 result read in full from `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T061800Z-account03-B11-QFORM-r24/REPORT.md`: balanced defect STAR/CROSS-2VOL dichotomy and pure-star mixed-Fresnel receiver.
* Standard product-projection input used throughout the current programme: a normalized linear form of independent cap-one coordinates has density at most `sqrt(2)` (Rogozin/Ball product-marginal bound).

No arbitrary-joint coarea estimate, conditional projection-density cap, moment assumption, support bound, or independence after spectral rotation is used.

## 2. Main theorem: overlapping rank-one Schur square

### Theorem `QFORM-OVERLAP-PAIR-SQUARE-v1`

Let `X=(U,Z)` have independent real coordinates with densities at most one, where `U=(X_i,X_j)` are two ORIGINAL coordinates. Suppose

`A = [[B,C],[C^T,D0]]`

is real symmetric and `B` is invertible indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Assume the Schur complement has exact rank one,

`S=D0-C^T B^{-1} C = sigma v v^T`, `||v||_2=1`, `sigma != 0`.

Let `W=v.Z`, and more generally suppose only that `W` has density cap `L`. Then the pure quadratic form `Q=X^TAX` has an essentially bounded density and

`||p_Q||_infinity <= 2^(13/4) L^(1/2) (D kappa |sigma|)^(-1/4)`.          (2.1)

For product inputs, `L<=sqrt(2)`, hence

`boxed(||p_Q||_infinity <= 8 sqrt(2) (D kappa |sigma|)^(-1/4)).`          (2.2)

The pair shift may depend arbitrarily on the same residual scalar `W`; no independence between the pair after completion and the third square is assumed.

### Proof

Schur completion is an identity in the ORIGINAL variables:

`Q=(U+B^{-1}CZ)^T B (U+B^{-1}CZ)+sigma(v.Z)^2`.             (2.3)

Fix `Z=z`. The two coordinates of `U` remain independent and have density caps one; their deterministic translations by the two entries of `B^{-1}Cz` preserve those caps. The source-pinned physical-pair envelope therefore gives, for every cutoff `r>0`,

`p_(Q|Z=z)(t)`
` <= 2 sqrt(2)/r`
`    +D^(-1/2) log_+(2r^2/[kappa |t-sigma(v.z)^2|]).`       (2.4)

The critical value in (2.4) is exactly the Schur remainder. This is where the overlap is retained: `B^{-1}Cz` may depend on `v.z`, but the envelope is uniform in the pair translation.

Set `Y=sigma W^2`. For every `t` and `rho>0`, the preimage

`{w: |sigma w^2-t|<rho}`

has Lebesgue measure at most

`2 sqrt(2rho/|sigma|)`.                                      (2.5)

Indeed for the sign-reduced case `sigma>0`, if `0<=t<=rho` the set is contained in the interval of radius `sqrt((t+rho)/sigma)<=sqrt(2rho/sigma)`; if `t>rho`, it is the union of the positive and negative intervals between `sqrt((t-rho)/sigma)` and `sqrt((t+rho)/sigma)`, whose total length is maximized at `t=rho` and again equals `2sqrt(2rho/sigma)`. For `t<0` or `sigma<0`, reflection can only shorten the preimage or reduces to the same calculation.

Therefore the density cap on `W` gives the uniform square small-ball estimate

`P(|Y-t|<rho) <= H sqrt(rho)`,
`H=2 sqrt(2) L / sqrt(|sigma|)`.                            (2.6)

For any `a>0`, layer cake yields

`E log_+(a/|t-Y|)`
` = integral_0^infinity P(|t-Y|<a e^{-u}) du`
` <= integral_0^infinity H sqrt(a) e^{-u/2} du`
` = 2H sqrt(a)`.                                             (2.7)

Average (2.4) over `Z`, insert `a=2r^2/kappa` into (2.7), and obtain

`p_Q(t) <= 2sqrt(2)/r + 2sqrt(2) H r / sqrt(D kappa)`.       (2.8)

The minimum of `a0/r+b0 r` is `2sqrt(a0 b0)`. Optimizing (2.8) gives

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`
` = 2^(13/4) L^(1/2) (D kappa |sigma|)^(-1/4)`,

which is (2.1). The normalized product-projection cap `L<=sqrt(2)` gives (2.2). QED.

### What is and is not new here

The source pair theorem already permits arbitrary moving pair shifts and proves the more general `8sqrt(5)(D kappa s)^(-1/4)` exact-rank-three bound by feeding the pair logarithm a rank-one **affine** small-ball estimate with constant `10/sqrt(s)`. The present step specializes the exact pure-quadratic rank-three Schur remainder to its literal square, computes its sharp geometric `sqrt(rho)` small-ball constant from the product projection, improves the constant, and makes the previously unpaid overlap mechanism explicit. It is a supporting sharpening, not a claim that the full physical-pair route is new.

## 3. Exact-rank-three corollary and sign tracking

Assume now that the full matrix has exact rank three, with three nonzero eigenvalue magnitudes at least `s>0`, and signature `(+,+,-)` or `(+,-,-)`. Let `B` be any invertible indefinite original-coordinate principal pair.

By Sylvester inertia under Schur congruence, `S` has rank one and its sign is the sign left over after removing one positive and one negative direction. Thus in signature `(+,+,-)`, `S=sigma vv^T` with `sigma>0`; in signature `(+,-,-)`, `sigma<0`.

The exact-rank-three Schur inverse identity from the source pair proof gives

`|sigma|>=s`.                                               (3.1)

Consequently

`boxed(||p_Q||_infinity <= 8sqrt(2)(D kappa s)^(-1/4)).`     (3.2)

This is uniform over arbitrary fragmented/unbounded cap-one input laws. Essential boundedness is claimed; continuity is not added by this proof.

The sign-specific splice with the pinned Claude ruled theorem is now explicit. For signature `(+,+,-)`, Theorem C at the pinned `e5f71d...` source gives

`p_Q(t) <= pi sqrt(2),   t>=0`,                              (3.3)

on the one-sheet/cone side. Equation (3.2) pays the complementary two-sheet side `t<0` whenever the quantitative physical pair exists (indeed it pays both sides). For signature `(+,-,-)`, apply (3.3) to `-Q`: the ruled bound pays `t<=0`, while (3.2) pays the opposite side. This is a genuine use of the pinned result at the remaining sign-specific inequality, not a bibliography-only citation.

## 4. A target-valid overlapping interpolation family

The overlap in Theorem 2 is not cosmetic. Consider, for `sigma>=0`,

`A_sigma = [[0,2,1],
            [2,0,1],
            [1,1,1+sigma]]`.                              (4.1)

Take the physical pair `B=[[0,2],[2,0]]`. Then

`D=4`, `kappa=2`, `B^{-1}(1,1)^T=(1/2,1/2)^T`,

and its Schur complement is the scalar `sigma`. Hence

`Q_sigma`
` =4(X_1+X_3/2)(X_2+X_3/2)+sigma X_3^2`.                  (4.2)

The third scalar `X_3` both translates the two saddle variables and supplies the smoothing square. Treating those two effects as independent would be invalid; (2.4)-(2.8) do not do so.

One eigenvector is `(1,-1,0)` with eigenvalue `-2`. On the orthogonal span of `(1,1,0)/sqrt(2)` and `e_3`, the matrix is

`[[2,sqrt(2)],[sqrt(2),1+sigma]]`,

whose eigenvalues are

`lambda_± = (3+sigma ± sqrt(sigma^2-2sigma+9))/2`.          (4.3)

The smaller one satisfies `lambda_- >=1` exactly when `sigma>=2`. Thus every `sigma>=2` gives a valid exact target matrix with three eigenvalues of absolute value at least one. At the threshold `sigma=2`,

`spec(A_2)={-2,1,4}`.                                      (4.4)

Because here `W=X_3` itself has density cap `L<=1`, (2.1) gives at `sigma=2`

`||p_(Q_2)||_infinity <= 2^(13/4) (4*2*2)^(-1/4)`
`                      = 2^(9/4) < 4.757`.                 (4.5)

The pinned Claude ruled theorem independently gives the sharper one-sheet value

`p_(Q_2)(t) <= pi sqrt(2) <4.443,  t>=0`.                  (4.6)

Therefore the concrete genuinely overlapping target family at `sigma=2` is paid by

`p_(Q_2)(t) <= pi sqrt(2)` for `t>=0`,
`p_(Q_2)(t) <= 2^(9/4)` for `t<0`,

and hence `||p_(Q_2)||_infinity <=2^(9/4)`.

### The rank-two logarithm survives at the endpoint

Set `sigma=0`. Then

`Q_0=4Y_1Y_2`,
`Y_1=X_1+X_3/2`, `Y_2=X_2+X_3/2`.                          (4.7)

For iid `X_k~Unif[-1/2,1/2]`, the joint density of `(Y_1,Y_2)` is exactly one on the square `[-1/4,1/4]^2`: for every point in that square, every `x_3 in[-1/2,1/2]` leaves both reconstructed `x_1=y_1-x_3/2` and `x_2=y_2-x_3/2` inside `[-1/2,1/2]`.

For `0<t<1/4`, the product pushforward formula therefore gives

`p_(Q_0)(t)`
` >= 2 integral_t^(1/4) [1/(4y)] dy`
` = (1/2) log(1/(4t)) -> infinity`.                         (4.8)

Thus even with three original independent variables and a genuinely overlapping translation, the rank-two endpoint keeps a logarithmic singularity. Overlap alone does not smooth it. The nonzero third Schur square is exactly what supplies the `sqrt(rho)` factor in (2.6), making the logarithm integrable. This is the requested sign-specific explanation of how the third direction removes the rank-two failure without post-rotation independence.

## 5. Applying the designated partner result to the complement

The theorem above pays the quantitative indefinite-pair branch; it does not force such a pair. The latest compatible account03/B11 report supplies a structural alternative in a complementary chamber.

Assume the surviving physical coordinates have positive diagonals, every physical pair is PSD, and the off-diagonal signs admit the global gauge used by the partner. After the original-coordinate sign gauge, write

`A=uu^T-F`, `F_ii=0`, `F_ij>=0`.

For `s_3(A)>=1`, partner Theorem 1 gives the real dichotomy

* **STAR:** some original coordinate `i` obeys `sum_(j!=i) F_ij^2 >=1/4`; or
* **CROSS-2VOL:** some disjoint cut `S,T` obeys `e_2(F_ST^T F_ST)>=1/32`.

This is applied here as the exact next structural implication after the local indefinite-pair exit. It prevents the proof map from leaving the balanced pair-PSD chamber as an amorphous remainder. The partner also pays the pure-star endpoint under its genuine mixed-Fresnel leverage gate. It does **not** yet pay arbitrary collective STAR geometry or automatically lift every CROSS-2VOL certificate to a leverage-admissible rank-three actual cross block; I do not infer those converses.

## 6. First unpaid implication after this run

`QFORM-BALANCED-STAR-CROSS-TWOSHEET-v1`.

In the exact-rank-three `(+,+,-)` / `(+,-,-)` no-quantitative-pair chamber, and after any already-paid sign-frustrated exit, convert the partner's dimension-free STAR/CROSS-2VOL certificate into a dimension-free two-sheet density estimate while retaining:

1. original-coordinate product provenance;
2. arbitrary within-bank quadratic curvature;
3. no moment or support assumptions;
4. no claim that a small matrix error is a small random quadratic perturbation;
5. no assertion that one physical minor or one cross block is uniformly well conditioned.

A viable next split is: either the partner rank-one-lift lemma creates an actual third cross singular value at fixed scale and the volume-stability receiver applies with its marginal gate checked, or one side is quantitatively aligned with the defect 2-plane and should be compiled as an aggregate star/hub without paying a local reciprocal determinant. The exact rank-two interpolation (4.7)-(4.8) is the control that any proposed compiler must preserve.

## 7. Scope and review status

* Full arbitrary-dimensional QFORM: **OPEN / NOT PROVED**.
* New theorem (2.1)-(2.2): proved here, pending independent review.
* Exact-rank-three pair corollary (3.2): proved from the new theorem plus the source-pinned Schur scale identity.
* Pinned Claude Theorem C: used only at its one-sheet scope.
* Partner STAR/CROSS-2VOL result: used only at its pair-PSD, sign-balanced scope.
* Arbitrary extra nonzero spectrum remains a separate debt because the Schur remainder is then not a pure rank-one square.
* Continuity is not claimed from this logarithmic-envelope argument.
