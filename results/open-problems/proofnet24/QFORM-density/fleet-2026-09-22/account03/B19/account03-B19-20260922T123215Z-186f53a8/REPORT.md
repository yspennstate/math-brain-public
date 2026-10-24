# account03/B19 — universal proof assembly: critical rank-two diffuse L3 bridge

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `account03-B19-20260922T123215Z-186f53a8`  
**Assignment:** Universal proof assembly  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Full target and current corrections

The full target remains: for every dimension, every independent real coordinates with one-dimensional densities `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the essential supremum of the density of `X^T A X`, or produce a valid counterexample. Continuity of a density representative is a separate stronger conclusion.

This run does not use the false law-uniform one-dimensional pointwise Fresnel decay, does not retain independence after a spectral rotation, does not take an unrestricted spectral-fiber supremum, and does not infer the theorem from one cross minor. It also respects the live correction that `C=pi` is false.

The designated partner `account04/B19` has now completed a compatible QFORM report. I apply its `QFORM-FINITE-UNION-CORE-v1`: the full concentration seminorm over arbitrary input densities is exactly the same as the supremum over product indicators of bounded finite unions of intervals of measure one. Thus every unresolved target-level branch below may, with no constant loss, be tested on compact finite-union product sets. This removes support/tail approximation as a possible hidden debt, but does not by itself prove the remaining trace or mixed-leverage estimate.

The new analytic step below combines two other completed results:

1. `account03/B08` proved a leverage-dependent Fourier--Brascamp--Lieb estimate for diffuse spectral frames. Its underlying Fourier estimate is valid already in rank two; only its final `L^1` integration required rank greater than two.
2. `account01/B11` proved a dependence-safe square-smoothing lemma from an `L^3` base density: if `R` has density `p` with `||p||_3=M` and the conditional density of `V|R=r` is at most one, then `R+dV^2` has density at most `4|d|^{-1/2}M^{3/4}`.

This run turns the critical rank-two Fourier estimate into exactly the `L^3` input required by (2), and inserts it into the spectral-Schur decomposition proved in the preceding B19 run.

## 2. Critical rank-two diffuse theorem

Let `S` be an `m x 2` real matrix with orthonormal columns. Write its rows as `s_j` and set the row leverage scores

`d_j=|s_j|^2`, so `sum_j d_j=2`.

Let `Gamma` be a real symmetric invertible `2 x 2` matrix. Let `X_1,...,X_m` be independent, each with probability density at most one. More generally allow arbitrary measurable one-coordinate potentials `V_j:R->R` and put

`Y=(S^T X)^T Gamma (S^T X)+sum_j V_j(X_j)`.

### Theorem 2.1 — `QFORM-DIFFUSE-RANK2-L3-v1`

If

`max_j d_j <= 1/2`,

then the law of `Y` is absolutely continuous with an `L^3` density and

`boxed( ||p_Y||_3 <= (3e)^(2/3) |det Gamma|^(-1/3). )`   (2.1)

The statement is sign-free: `Gamma` may be definite or indefinite. It is also stable under arbitrary coordinatewise phases `V_j`.

### Proof

For fixed nonzero `t`, define

`g_{j,t}(x)=f_j(x) exp(i t V_j(x))`.

Then `|g_{j,t}|<=1` and `||g_{j,t}||_1=1`. The account03/B08 complex high-power Hausdorff--Young lemma and geometric Brascamp--Lieb argument apply to every rank `r`, not only `r>=3`. For `r=2` they give

`int_{R^2} prod_j |hat g_{j,t}(<s_j,xi>)| dxi <= (2 pi sqrt(e))^2`.   (2.2)

The two-dimensional Fresnel identity for the invertible real symmetric matrix `Gamma`, with the same regularization used in B08, therefore gives

`|phi_Y(t)|
 <= (4 pi |t|)^(-1) |det Gamma|^(-1/2) (2 pi sqrt(e))^2
 = D/|t|`,

where

`D=pi e |det Gamma|^(-1/2)`.   (2.3)

Of course also `|phi_Y(t)|<=1`. Thus

`|phi_Y(t)| <= min(1,D/|t|)`.

Although the right side is not integrable, its `3/2` power is integrable. Indeed

`int_R |phi_Y(t)|^(3/2) dt
 <=2[ int_0^D 1 dt + int_D^infinity (D/t)^(3/2) dt ]
 =6D`.   (2.4)

Hence

`||phi_Y||_(3/2) <= (6D)^(2/3)`.   (2.5)

Use Hausdorff--Young for the inverse Fourier transform with the convention

`p(y)=(1/(2pi)) int exp(-ity) phi_Y(t) dt`.

The nonsharp norm-one Hausdorff--Young constant is sufficient and yields

`||p_Y||_3
 <=(2pi)^(-2/3)||phi_Y||_(3/2)
 <=(2pi)^(-2/3)(6 pi e |det Gamma|^(-1/2))^(2/3)
 =(3e)^(2/3)|det Gamma|^(-1/3)`.

For rigor, `phi_Y in L^(3/2)` implies through inverse Hausdorff--Young a function `p_Y in L^3`; equality with the original probability law follows in the sense of tempered distributions (equivalently by testing against Schwartz functions), so the law is absolutely continuous with this density. QED.

### Why this is the correct critical exponent

Rank two is exactly the threshold where the B08 Fourier envelope is `|t|^-1`, so `L^1` Fourier inversion is unavailable and an opposite-sign rank-two quadratic may indeed have a logarithmically unbounded density. But `|t|^-1` lies in `L^(3/2)` at infinity, which gives precisely an `L^3` density. This is the functional level needed for the third-square smoothing theorem. No false bounded-density conclusion is asserted for rank two.

## 3. New rank-three localized branch

Consider now a rank-exactly-three quadratic

`Q0=X^T R Lambda R^T X`,

where `R` is `n x 3` with `R^T R=I_3` and `Lambda` is invertible symmetric with all three eigenvalues of modulus at least one. Fix a physical coordinate `i`; let `v` be row `i` of `R`,

`c=|v|^2>0`,  `a=v^T Lambda v`.

Assume `a!=0`. The previous account03/B19 run proved the exact independent-coordinate spectral-Schur decomposition. With

`M=I-vv^T`, `W=R_L M^(-1/2)`, `Y=W^T X_L`,

one has

`Q0=a(X_i+m(Y))^2+Y^T T Y`,   (3.1)

where `W` has orthonormal columns, `T` is symmetric of rank two, and

`|pdet T| = c |det Lambda| / |a|`.   (3.2)

Let `U` be a `3 x 2` orthonormal basis for the range of `T`, put

`Gamma=U^T T U`,  `S=WU`.

Then `S` has orthonormal columns and

`Y^T T Y=(S^T X_L)^T Gamma(S^T X_L)`.   (3.3)

### Theorem 3.1 — `QFORM-LOCALIZED-DIFFUSE-RESIDUAL-v1`

If every row of the residual two-frame `S` has squared norm at most `1/2`, then `Q0` has an essentially bounded density satisfying

`boxed(
 ||p_Q0||_infinity
 <=4 sqrt(3e) ( |a| c |det Lambda| )^(-1/4).
)`   (3.4)

In particular, this closes the previously unpaid majority-sign localized branch whenever the rank-two indefinite Schur residual is diffuse in the remaining original coordinates and the displayed pivot invariant is quantitatively nonzero.

### Proof

Apply Theorem 2.1 to the residual variable

`R0=Y^T T Y`.

Since `|det Gamma|=|pdet T|`,

`||p_R0||_3
 <=(3e)^(2/3)|pdet T|^(-1/3).`   (3.5)

Set

`V=X_i+m(Y)`.

The original coordinate `X_i` is independent of all of `Y`. Conditional on `R0=r`, the shift `m(Y)` is random, but the law of `V` is only a mixture of translations of the density of `X_i`; consequently its conditional density remains at most one. This is exactly the dependence-safe hypothesis in account01/B11's `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1`.

Apply that theorem to (3.1):

`||p_Q0||_infinity
 <=4 |a|^(-1/2) ||p_R0||_3^(3/4)
 <=4 sqrt(3e) |a|^(-1/2)|pdet T|^(-1/4).`

Using (3.2),

`|a|^(-1/2)|pdet T|^(-1/4)
 =(|a|c|det Lambda|)^(-1/4)`,

which proves (3.4). QED.

### Sign interpretation

If `Lambda` has inertia `(2,1)` or `(1,2)` and the pivot `a` has the majority sign, the rank-two residual `T` is indefinite. This is exactly the sign branch not handled by the earlier definite-residual spectral-Schur theorem. The present result does not try to make that rank-two saddle bounded by itself; it proves an `L^3` bound at the critical diffuse level and lets the remaining square remove the logarithmic singularity.

For a minority-sign pivot the residual is definite and the earlier B19 theorem already gives the stronger constant `2 sqrt(2pi)` in place of `4 sqrt(3e)`. Thus the local sign obstruction has been replaced by a quantitative residual-localization obstruction.

## 4. Compact conditional assembly after this step

The strongest current rank-three assembly can now be stated as follows.

1. If the three-frame itself has every row leverage at most `1/2`, account03/B08 gives a continuous density bounded by `3e`.
2. If the rank-three form is definite and a row is localized, the previous B19 spectral-Schur theorem closes it; all rank-three definite forms therefore have density at most `3e`.
3. For an indefinite localized frame, choose a physical pivot. Minority-sign pivots with definite rank-two residual are controlled by the previous spectral-Schur theorem.
4. Majority-sign pivots with an indefinite residual are controlled by Theorem 3.1 whenever the whitened residual two-frame is diffuse.
5. Independently, account01/B11 and account02/B04 close every *fixed* invertible original-coordinate `3 x 3` principal block once its determinant and pivot data are quantitatively large, including the all-zero-diagonal pure-cross exception.
6. account04/B19's finite-union core shows that the remaining target-level branch can be tested, without loss of constant, on compact products of bounded finite unions of intervals.

These are real closed branches, but they do not yet imply a universal bound from the spectral hypothesis alone.

## 5. First unpaid implication

The first genuinely global remaining implication is now a two-level localization/aggregation statement rather than a local inertia statement:

### `QFORM-TWOLEVEL-MIXED-LEVERAGE-AGGREGATION-v1` — OPEN

For rank-exactly-three indefinite `A=R Lambda R^T`, prove a dimension-free dichotomy from only `|lambda_j|>=1`:

- either the original three-frame is diffuse and B08 applies;
- or a localized pivot has a quantitatively nonisotropic invariant `|a|c|det Lambda|` and its residual two-frame is diffuse, so Theorem 3.1 applies;
- or the second-level localization forces an original-coordinate block/cross-block configuration to which the proved Schur, pure-cross, or rank-three cross-block theorem applies with a universal quantitative parameter.

Near-isotropic localized pivots (`a` close to zero) and second-level residual localization are the precise unpaid subcases. The exact cross-energy identity from the preceding B19 run,

`sum_{j!=i} A_ij^2=|Lambda v|^2-a^2 >= c-a^2`,

shows that a near-isotropic high-leverage pivot carries substantial distributed cross coupling, but a dimension-free conversion of that aggregate energy into one of the paid mechanisms is still missing. A one-minor selection is known to lose dimension and is not an acceptable substitute.

The account04/B19 finite-union theorem sharpens this further: no noncompact-tail or density-extremizer issue remains in this unpaid implication. It is a finite product-geometry aggregation problem.

## 6. Scope and status

**Proved in this run**

- `QFORM-DIFFUSE-RANK2-L3-v1`, with explicit constant `(3e)^(2/3)|det Gamma|^(-1/3)` and arbitrary coordinatewise potentials;
- `QFORM-LOCALIZED-DIFFUSE-RESIDUAL-v1`, with explicit essential-density bound `4 sqrt(3e)(|a|c|det Lambda|)^(-1/4)`;
- replacement of the local majority-sign inertia obstruction by the narrower two-level mixed-leverage/near-isotropic aggregation obstruction.

**Applied completed partner mathematics**

- designated partner account04/B19: `QFORM-FINITE-UNION-CORE-v1`, used to reduce the remaining target-level concentration problem to bounded finite-union product inputs with no constant loss;
- account03/B08: the exact diffuse Fourier--Brascamp--Lieb estimate, extrapolated at its valid critical rank-two exponent;
- account01/B11: dependence-safe `L^3` square smoothing.

**Not proved**

- `QFORM-TWOLEVEL-MIXED-LEVERAGE-AGGREGATION-v1`;
- arbitrary additional spectral directions beyond rank exactly three;
- the full conjecture;
- a continuous representative in Theorem 3.1.

## 7. Source pins

- Live owner control: `yspennstate/math-research-brain`, revision `2026-09-22.5`; initial fresh control commit `054362207d28d2334a5c4eaee62ffbfa4a217ba6`, later prepublication main observed at `01885efdf6c679a379d87d67a5f0c973adc517bd` with unchanged control.
- Designated partner account04/B19 finite-union core: `yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T122030Z-account04-B19-QFORM-r1/REPORT.md`, blob `6c1e768322445d808cbf9d85aae456ec3240a663`.
- account03/B08 diffuse Fourier--Brascamp--Lieb theorem: `yspennstate/math-open-problems@9dcddd0bf3fbcb8e0b3396e0a4d883924d3f4ada`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T114830Z-account03-B08-qform-diffuse-v1/REPORT.md`, blob `022e24d4e6470665c48d7bfb1a3ad5c7963f664a`.
- account01/B11 binary-indefinite `L^3` and dependent square smoothing: `yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`, blob `17a44fbdfb6c987ed46e2e76833c60497b33f025`.
- Previous account03/B19 spectral-Schur report: path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T120353Z-account03-B19-qform-r11/REPORT.md`, blob `01012c049f3b3120c4b0c4972b72a0c736c778c4`.
- Live correction inbox at prepublication refresh: blob `1681679e291cfd73917b46a25dc5bc8584d40bec`.

No native brain retrieval was used. Repository transport and peer theorem application are recorded separately. Full conjecture remains open.
