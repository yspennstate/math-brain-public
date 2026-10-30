# fleet02/B05 — fixed-multiplicity full audit, fresh master pass

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin

Fresh `yspennstate/math-open-problems` master observed at the start of the package audit: `af01fc9240762f709dd21d725c2527c74b6167f7`.

The delivered baseline package pins the theorem source at:

- baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- `manuscript.tex` git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- 790 source lines.

I read the complete package `README.md`, `SOURCE_MANIFEST.json`, `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The support files advertised by the README are present on this master. `checks.json` reports the finite diagnostic suite PASS. The finite checker is reproducibility evidence only; the verdict below is from a line-by-line mathematical audit.

## Verdict

**Baseline theorem: PASS, with two nonfatal presentation/notation GAPs and no mathematical FALSE.**

The written theorem is the fixed-multiplicity statement

`independent densities <= K, s_17(A)>=s>0 => ||p_(X^TAX+b^TX+c)||_infinity <= 10^4 K^2/s`.

All signs, affine terms, dimensions and rough coordinate laws allowed by the statement are retained. The proof does not establish the unrestricted three-eigenvalue conjecture.

Neither gap below breaks a proof implication:

1. **GAP-PRESENTATION-PROJECTION** (`manuscript.tex` 258–282, final entropy line). After the factors with `b_i=0` are dropped, the text writes the retained sum as `sum_i(1-b_i)=d`. If the displayed sum is interpreted only over retained indices, equality need not hold. The correct statement is
   `sum_{b_i>0}(1-b_i) <= sum_all_i(1-b_i)=d`,
   which gives the same claimed cap `exp(d/2)`. Impact: none on the theorem; repair is one symbol (`<=`).
2. **GAP-NOTATION-SCHUR** (`manuscript.tex` 726–749, indefinite-pair branch). The phrase `||A/B||>=1` uses notation not defined elsewhere in the manuscript. The intended object is the Schur complement of the chosen pair; Lemma `lem:schur` gives that its quadratic matrix has operator norm at least one. Replacing `A/B` by the explicitly named Schur complement repairs the line. Impact: none on the theorem.

## Exhaustive source ledger

The ranges below partition the 790-line manuscript into front matter/prose and every proof-map object. `PASS*` means mathematically correct with one of the two presentation repairs above.

| Source lines | Object / obligation | Status | Audit reason / next obligation |
|---|---|---|---|
| 1–46 | preamble, conventions, abstract/introduction and normalization declarations | PASS | Definitions and quantifiers are compatible with the later proof; no hidden moments/support/smoothness assumption. |
| 47–57 | main fixed-multiplicity theorem | PASS | Quantifiers match the final scaling argument. |
| 59–61 | 33-direction corollary | PASS | Monotonicity `s_17>=s_33`. |
| 62–90 | Fourier convention, notation, proof architecture | PASS | Consistent with subsequent transform constants. |
| 91–120 | Fourier inversion / Gaussian regularization lemma and proof | PASS | Approximate-identity argument establishes density from integrable characteristic function. |
| 122–130 | power-envelope integral lemma | PASS | Split at the crossover; constants and exponents correct. |
| 132–160 | half-Riesz inequality and proof | PASS | Gaussian regularization + positive kernel/Tonelli; no pre-existing density required. |
| 161–168 | spectral-count notation / preliminaries | PASS | Symmetric singular values are eigenvalue moduli as used later. |
| 169–181 | singular-value rank perturbation lemma | PASS | Standard min-max/rank shift used in correct direction. |
| 183–207 | Schur spectral-count lemma | PASS | Invertible case via inverse compression; singular case moving-threshold limit is valid by ordered singular-value continuity. |
| 209–217 | strict diagonal-dominance lemma | PASS | Correct nonsingularity criterion. |
| 218–220 | BL section setup | PASS | Deterministic coefficient geometry only. |
| 221–255 | geometric rank-one Brascamp–Lieb theorem | PASS | Heat-flow proof closes; no probabilistic rotation is introduced. |
| 256–257 | projection section setup | PASS | — |
| 258–282 | product-projection density lemma | PASS* | Full Fubini + BL reconstruction checked; only retained-index equality typo described above. |
| 283 | Fourier-decay section setup | PASS | — |
| 284–301 | scalar Fourier powers | PASS | Plancherel/interpolation constants valid for cap-one densities. |
| 302–309 | decoupling setup | PASS | Product banks remain literal original-coordinate sets. |
| 310–324 | decoupling lemma | PASS | Independent copy/sign symmetrization valid. |
| 326–373 | determinant Fourier theorem | PASS | Frame normalization, BL exponents, scalar powers and entropy step all checked. |
| 374–385 | crossing-volume definitions | PASS | Cauchy–Binet normalization and dimensions consistent. |
| 386–400 | volume/Fourier corollary | PASS | Correct retention of determinant polynomial term and Fourier/Riesz thresholds. |
| 401–403 | pivot section setup | PASS | — |
| 404–414 | scalar-square profile | PASS | Density formula and interval-preimage length bound correct; singularity is genuine and intentionally retained. |
| 415–422 | conditional square domination formula | PASS | Correctly formulated at measure/test-function level and averaged by Tonelli, not by conditional independence. |
| 423–434 | definite two-coordinate pivot | PASS | Orthogonal change is deterministic integration only; joint cap, not independence, is used. |
| 435–436 | hyperbolic section setup | PASS | — |
| 437–482 | indefinite/hyperbolic pair lemma | PASS | Coarea parametrization, Jacobian, tail rearrangement and logarithmic envelope checked. Critical level is handled only a.e./measure-theoretically. |
| 483–484 | quarter-power section setup | PASS | — |
| 485–525 | quarter-power concentration/log-potential lemma | PASS | Diagonal branch and signed off-diagonal decoupling checked; Fourier/Gaussian small-ball estimate excludes atoms. |
| 526–527 | disjoint-minor section setup | PASS | — |
| 528–535 | pivot/volume definition | PASS | Ordered disjoint-set convention used consistently. |
| 536–544 | no-pivot entry estimates / sampling setup | PASS | `|a_ij|<1/7` follows from chosen constants. |
| 545–564 | volume-sampled interpolation | PASS | Bordered determinant identity and multiplicity `(r+1)^2` correct; singular seeds only strengthen inequality. |
| 566–580 | diagonal + interpolation completion | PASS | `rank R<=3r`, and crucial restricted `rank R_LL<=r`, both valid for nonsymmetric `R`. |
| 582–619 | no-pivot spectral-to-volume proposition | PASS | Telescoping ratio, singular-value rank shift, and diagonal-dominance contradiction checked for `k<=5`. |
| 621–630 | random coordinate cut | PASS | Every ordered disjoint `(S,T)` survives with probability `4^-k`. |
| 632–645 | no-pivot analytic consequences | PASS | `k=3` gives full half potential; `k=5` gives integrable Fourier density. Constants conservative. |
| 646–653 | final-pivot setup / truncated half potential | PASS | Atom convention compatible with later exclusion. |
| 654–674 | two singular-kernel estimates | PASS | Region split and centered-interval rearrangement/Tonelli bounds checked. |
| 676–714 | pivot controls truncated half potential | PASS | Scalar, definite and indefinite alternatives exhaustive; all conditional estimates uniform in affine terms and averaged at measure level. |
| 716–724 | nine-eigenvalue half-potential proposition | PASS | Pivot/no-pivot split plus outside-unit tail gives 601. |
| 726–749 | proof of main theorem | PASS* | All branches and scaling correct; undefined `A/B` notation repaired as Schur complement. |
| 750–778 | threshold accounting / dependency table / limitations | PASS | Correctly distinguishes order-three half-potential from order-five density and does not claim optimality. |
| 779–785 | no-continuity/no-independence remark | PASS | Accurately reflects proof interfaces. |
| 786–790 | acknowledgment/bibliography/end | PASS | No proof obligation. |

No mathematical source line is `UNCHECKED` in this audit. There is no `FALSE` entry.

## B05 reconstruction: product projection

Let `U` have orthonormal columns and complete it by `W` to an orthogonal matrix. With `w_i^T` the rows of `W`, put `b_i=||w_i||^2=1-||U^Te_i||^2`. Fubini writes the marginal density of `U^T X` as an integral in the complementary variable. For `b_i>0`, the vectors `v_i=w_i/sqrt(b_i)` satisfy

`sum_i b_i v_i v_i^T = I`.

Apply geometric BL to

`h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^(1/b_i)`.

Because `0<=f_i<=1`, `f_i^(1/b_i)<=f_i`, so `int h_i<=b_i^-1/2`. Therefore

`p_(U^T X)(y) <= product_{b_i>0} b_i^(-b_i/2)`.

Using `-b log b<=1-b` and the repaired retained-index inequality gives

`||p_(U^T X)||_infinity <= exp(d/2)`.

For any full-row-rank `L:R^n->R^d`, polar factorization then yields the form used by the nine-direction replacement:

`||p_(LX)||_infinity <= exp(d/2)/sqrt(det(LL^T))`.

At no point is independence of the projected/rotated coordinates asserted.

## B05 exceptional-slice stress tests

These are counterexamples to tempting shortcuts, not to the theorem.

1. Let `X_1,X_2` be independent uniform variables on `[-1/2,1/2]`, and set
   `Y=(X_1+X_2)/sqrt(2)`, `Z=(X_1-X_2)/sqrt(2)`.
   Then `p_Y(y)=sqrt(2)-2|y|` on its support, while conditional on `Y=y`, `Z` is uniform on an interval of exactly that length. Hence
   `||p_(Z|Y=y)||_infinity = 1/(sqrt(2)-2|y|)`,
   which diverges near the support boundary. An unconditional projection cap cannot be recycled after conditioning on another rotated coordinate.
2. If `X_1,X_2` are as above, `R=2X_1X_2` has
   `p_R(t)=log(1/(2|t|))`, `0<|t|<1/2`.
   The indefinite critical fiber has a real logarithmic singularity. A proof that replaces the manuscript's Tonelli-averaged logarithmic envelope by a uniform pointwise conditional density cap is false.
3. For `X` uniform on `[-1/2,1/2]`, `X^2` has density `t^(-1/2)` on `(0,1/4)`. The scalar-square singular profile likewise cannot be replaced by a bounded conditional density.

The manuscript survives all three tests because it uses domination of measures against nonnegative test functions and Tonelli before taking any a.e. density representative.

## Complete threshold reduction certified in this audit: 17 -> 9

I rechecked the existing fleet02/B05 grouped product-Fourier replacement rather than merely inheriting its PASS label. The complete theorem certified here is

`boxed: s_9(A)>=s>0 => ||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s.`

Dependency map:

1. baseline geometric BL + product-projection/full-row-rank corollary;
2. baseline scalar Fourier powers, Fourier inversion and half-Riesz inequality;
3. baseline Schur count, square/definite/hyperbolic pivots and quarter-power log potential;
4. baseline no-pivot spectral-to-volume proposition and random cut at orders two and three;
5. grouped product-Fourier compiler: hub Plancherel + mollified rough conditional pushforward + original-coordinate Fourier averaging + weighted subset Holder/entropy;
6. literal-original-coordinate heavy-row promotion trees, giving marginal-free `E_3` density and `E_2` half-potential receivers.

Key constants in normalized scale:

- marginal-free `E_3` receiver: `C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`;
- no-pivot `s_9` branch: `E_3^-1/6<=160`, hence `<2371<2400`;
- marginal-free `E_2` half-potential receiver: `C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`;
- scalar-pivot child with a pivot: full half potential `<=201+120 log16`; without a child pivot the order-two receiver is smaller (`~152.992`);
- outer scalar pivot costs `eta^-1/2=10`, giving `2010+1200 log16=5337.106466...<5338`;
- definite pair `<32`; indefinite pair `<251`.

The rough-law step was rechecked specifically for B05: the complex conditional pushforward is mollified before the `L^2` expansion; the expansion uses an independent copy of the original `J` bank; the `I`-bank expectation is taken in the original independent physical coordinates before absolute values; and Fourier-side Fatou removes the mollifier. Heavy promotions always move literal original coordinates into the hub. No post-rotation independence or exceptional-slice conditional cap is used.

A newer constant-only artifact on current master claims `<2514 K^2/s` at the same threshold nine. I did not promote that sharper constant to this B05 certificate because this run did not independently reconstruct its entire alternate scalar-pivot dependency chain. The complete B05-certified replacement constant remains 5338.

## Multiplicity eight frontier: OPEN, now sharply localized

Fresh master contains two compatible supporting results, neither a complete `L^infinity` theorem at `s_8`:

- the two-anchor Schur/log fusion cancels the logarithmic dependence on a small indefinite pair determinant, but leaves a nonlogarithmic `6 D^(-1/2)` term;
- the source-disjoint three-color/split-row collar gives the critical Fourier endpoint
  `|phi_Q(t)| <= min(1,U_*/|t|)`, `U_*<=197.494`, hence every finite `L^r` norm and `epsilon log(1/epsilon)` small-ball control, but not `L^infinity`.

The rank-two saddle counterexample above proves that this critical endpoint alone cannot imply a bounded density: `2X_1X_2` has the same logarithmic endpoint class and an unbounded density. Therefore the next valid `s_8` step must spend additional overlap-one / rank-saturation / source-disjoint curvature **before** reducing to the `1/|t|` envelope or to a local reciprocal small pair determinant.

### Next obligation

Prove a product-preserving endpoint receiver for the `s_8` two-sided collar that uses the surviving `Omega_1`/overlap-one currency to obtain either

- an integrable improvement `|phi_Q(t)| <= C |t|^(-1-epsilon)` for some universal `epsilon>0`, or
- a direct linear small-ball bound `P{Q in I}<=C|I|`,

without conditioning on a rotated projection, selecting a dimension-dependent tiny local minor, or replacing the curved exceptional slice by an unrestricted fiber supremum.

Multiplicity 8 remains OPEN. The unrestricted three-eigenvalue QFORM conjecture remains OPEN.
