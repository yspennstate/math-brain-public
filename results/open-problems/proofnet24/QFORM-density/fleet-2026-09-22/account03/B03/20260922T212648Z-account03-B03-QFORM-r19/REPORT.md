# QFORM-COLLISION-L2-HOMOGENEITY-REPAIR-v1

## Status

**CORRECTION + SUPPORTING LEMMA / FULL QFORM OPEN.**  Essential boundedness for the unrestricted target is not proved here, and continuity is not proved.  The designated partner `account04/B03` was consumed at its completed handoff/report, but its advertised two-square unweighted `L^2` compiler is false as stated.  This report gives a decisive scaling counterexample, identifies the missing factor in its displayed Cauchy--Schwarz step, and replaces it with a correctly homogeneous collision theorem that still yields linear independent-copy small-ball scaling.

Control source at startup: `yspennstate/math-research-brain@be06d2190c1485a3a76635f2635b24c995a378b3`, OWNER CONTROL revision `2026-09-22.15`.  Prepublication refresh: `yspennstate/math-research-brain@288dc19339f1f24f73b8b9a75417e17d46bf5352`, same revision.  Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and assignment

The full target is: for every dimension, every independent real input vector with coordinate densities at most one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a target-valid counterexample.  No moments, compact support, log-concavity, Gaussianity or independence after rotation is assumed.

B03's assignment is the decoupled time integral: use independent-copy identities without falsely separating the dependent sum/difference pair `(X-X',X+X')`, and recover linear small-ball scaling from an integrated estimate.

## 2. Exact partner result consumed, and the defect

The designated partner handoff is

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260922T193150Z-account04-B03-collision-l2-r1/REPORT.md`.

For `Y=aZ^2+bW^2`, with `Z,W` independent and density caps `M_Z,M_W`, it claims

`int |phi_Y(t)|^2 dt <= sqrt(2*pi) C_sq sqrt(M_Z M_W) |ab|^(-1/4)`

and hence

`||p_Y||_2^2 <= (C_sq/sqrt(2*pi)) sqrt(M_Z M_W) |ab|^(-1/4)`,

where `C_sq=14.2950242690...`.

The displayed proof writes

`int |psi_a psi_b| = int (|t|^(-1/2)|psi_a|^2)^(1/2)(|t|^(-1/2)|psi_b|^2)^(1/2) dt`.

That equality is false.  The right-hand integrand equals

`|t|^(-1/2)|psi_a(t) psi_b(t)|`,

so the correct identity has an additional factor `|t|^(1/2)` on the right.  The account01/B03 *weighted* half-Riesz estimate remains valid; only the partner's removal of that weight is invalid.

There is also an unavoidable homogeneity contradiction.  If both coefficients are multiplied by `c>0`, then `Y_c=cY` and

`||p_(Y_c)||_2^2 = c^(-1)||p_Y||_2^2`.

The partner right side scales only like `c^(-1/2)`.

### Concrete cap-one counterexample

Take `Z,W` iid Uniform[0,1] and `a=b=c=10^(-4)`.  Then `Y_c=c(Z^2+W^2)` is supported on an interval of length `2c`.  Any probability density supported on a set of measure at most `2c` satisfies by Cauchy--Schwarz

`||p_(Y_c)||_2^2 >= 1/(2c) = 5000`.

The claimed partner bound gives only

`(C_sq/sqrt(2*pi)) c^(-1/2) = 570.2889580...`.

Thus `QFORM-COLLISION-L2-COMPILER-v1` is false as stated.  This is a correction of an intermediate theorem, not a counterexample to the QFORM conjecture.

## 3. A correctly homogeneous square-density `L^p` lemma

Let `X` have density `f` with `0<=f<=M`, let `a!=0`, and let `G=aX^2`.  Write `g` for its density on the appropriate half-line.  For `s>0` after reflection if necessary,

`g(s) <= M / sqrt(|a| s) =: c s^(-1/2)`,

and `int g=1`.

For every `1<=p<2`, the bathtub principle for the decreasing envelope `c s^(-1/2)` gives

`int g(s)^p ds <= [2^(p-1)/(2-p)] M^(2p-2) |a|^(1-p)`.      (3.1)

Indeed, among `0<=g<=c s^(-1/2)` with unit mass, the convex functional `int g^p` is maximized by filling the largest values of the envelope first.  The saturation interval is `[0,R]` with

`2c sqrt(R)=1`, hence `R=1/(4c^2)`, and direct integration gives (3.1).

At `p=4/3`,

`||g||_(4/3) <= (3^(3/4)/sqrt(2)) M^(1/2)|a|^(-1/4)`.       (3.2)

This estimate is invariant under reflection, so it applies to either sign of `a`.

## 4. Corrected two-square `L^2` collision compiler

Let `Z,W` be independent with density caps `M_Z,M_W`, and set

`Y=aZ^2+bW^2`, `ab!=0`.

The density of `Y` is the convolution of the two reflected square densities.  Ordinary Young plus (3.2) already gives

`||p_Y||_2 <= (3^(3/2)/2) sqrt(M_ZM_W)|ab|^(-1/4)`

and therefore

`||p_Y||_2^2 <= (27/4) M_ZM_W |ab|^(-1/2)`.                 (4.1)

Using the sharp one-dimensional Young constant improves this.  With

`A_p=(p^(1/p)/(p'^(1/p')))^(1/2)`, `A_2=1`,

one has

`||f*g||_2 <= A_(4/3)^2 ||f||_(4/3)||g||_(4/3)`,

and

`A_(4/3)^2 = 2/3^(3/4)`.

Combining with (3.2) yields

`boxed( ||p_Y||_2 <= 3^(3/4) sqrt(M_ZM_W)|ab|^(-1/4) )`,

hence

`boxed( ||p_Y||_2^2 <= 3sqrt(3) M_ZM_W |ab|^(-1/2) )`.       (4.2)

This has the only possible common coefficient homogeneity: multiplying `(a,b)` by `c` multiplies both sides of (4.2) by `c^(-1)`.

By Plancherel for `phi_Y(t)=E exp(itY)`, (4.2) is the full-time estimate

`boxed( int_R |phi_Y(t)|^2 dt <= 6*pi*sqrt(3) M_ZM_W |ab|^(-1/2) )`.   (4.3)

No pointwise oscillatory decay is used.

## 5. Linear independent-copy small-ball scaling, with the partner's valid step

Let `Y'` be an independent copy.  The *valid* collision step from the account04/B03 report is

`P(|Y-Y'|<=epsilon) <= 2 epsilon ||p_Y||_2^2`.

Applying that partner inequality to the repaired bound (4.2) gives the actual inequality-level partner consumption

`boxed( P(|Y-Y'|<=epsilon) <= 6sqrt(3) M_ZM_W |ab|^(-1/2) epsilon )`.   (5.1)

Numerically `6sqrt(3)=10.3923048454...`.

This is a dependence-safe independent-copy conclusion.  Nothing in the proof asserts that `Z-Z'` and `Z+Z'` are independent.  The separate account01/B03 weighted identity

`int |t|^(-1/2)|psi_a(t)|^2 dt < infinity`

also remains valid precisely because it treats `|Z^2-Z'^2|=|(Z-Z')(Z+Z')|` jointly.  The present correction says only that one may not erase the half-Riesz weight by the partner's displayed Cauchy--Schwarz step.

## 6. `L^r` ladder: where a third genuinely independent smoother can close

The same argument gives more than `r=2`.  For any finite `r>1`, choose

`p=2r/(r+1)`.

Then `1+1/r=2/p`, and ordinary Young with (3.1) gives

`||p_Y||_r <= C_r (M_ZM_W)^(1-1/r)|ab|^(-(1-1/r)/2)`,

where

`C_r=(r+1)^((r+1)/r) 2^(-2/r)`.                              (6.1)

For example `r=3` gives

`||p_Y||_3 <= 4 (M_ZM_W)^(2/3)|ab|^(-1/3)`.                  (6.2)

A third *independent* square `dV^2`, with density cap `M_V`, satisfies

`||p_(dV^2)||_(3/2) <= 2 M_V^(2/3)|d|^(-1/3)`.

Therefore ordinary Young gives

`||p_(aZ^2+bW^2+dV^2)||_infinity
 <= 8 (M_ZM_WM_V)^(2/3)|abd|^(-1/3)`.                         (6.3)

This corollary is useful for disjoint original-coordinate bank projections whose scalar projected laws have bounded densities.  It does **not** solve the rotated full target because a general quadratic form does not decompose into three independent square summands after diagonalizing its large spectral subspace.

## 7. What this changes for the full target

The partner's useful diagnosis survives: a linear collision estimate is fundamentally an `L^2` certificate, not by itself an `L^infinity` certificate.  The corrected compiler now has the right scaling and a stronger explicit cap-one/unit-coefficient collision constant, but it does not pay the genuinely rotated third-direction dependence.

The first unpaid B03 implication is therefore sharper:

> Construct a product-preserving bank-level `L^(2+delta)` or translation-uniform fractional-potential estimate from the third large spectral direction **without** conditioning on a sum/difference variable with an exploding cap and without replacing the dependent `(X-X',X+X')` geometry by separate positive factors.

The current correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` also forbids pretending that an almost-zero Schur diagonal plus cross-row norm automatically supplies this upgrade.

Full QFORM remains **OPEN**.  Continuity remains **OPEN**.

## 8. Provenance and no-claim boundary

- Designated partner consumed: `account04/B03`, report commit `28681f9af7c2307f80968df86010084019599e38`.
- Underlying valid weighted collision theorem re-read: `account01/B03`, report commit `cd628bcb117fb633c47261a3fbb9d1504a8b1b1b`.
- Corrections consumed before publication include `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, and `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`.
- No Gaussian, moment, support, log-concavity, rotated-independence, pointwise van-der-Corput, or Monte Carlo premise is used.
- No native learned-memory receiver use occurred; status remains `WITHOUT_VERIFIED_BRAIN`.
