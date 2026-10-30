# fleet03/B20 — two-level square cascade and proof-closure update

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner revision: `2026-09-22.5`  
Run: `20260922T131539Z-fleet03-B20-qform-r11`  
Status: `SUPPORTING_THEOREM_APPLIED / FULL_CONJECTURE_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction-aware scope

The target is: for every dimension, every product law on `R^n` with independent one-dimensional densities bounded by one, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite bound. Continuity of a representative is tracked separately.

This report keeps original-coordinate independence. It does not use independence after spectral rotation, moments, compact support, log-concavity, the refuted law-uniform pointwise quadratic-phase decay, a dimension-free fiber-supremum estimate, a single uniformly good principal block, or a generic conditional-cap-as-independence substitution.

Fresh corrections consumed include the failure of the single-Schur rank-two extraction, conditional-cap-as-independence, bounded-diameter localization, and the local-cross-rank-three dichotomy. The result below is therefore deliberately a theorem **inside the genuine spectral-Schur two-level localized branch**, not a claim that every target matrix admits that branch.

## 2. Current compatible proof state

I source-read the current fleet03/B19 proof assembly
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/fleet03-B19-20260922T123215Z-186f53a8/REPORT.md`.
It proves a rank-two diffuse `L^3` theorem and a rank-three localized-pivot theorem, and leaves two linked debts in the rank-exactly-three indefinite core: second-level residual localization and near-isotropic scalar pivots.

I also source-read the completed named partner result fleet04/B20
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T132134Z-fleet04-B20-QFORM-r1/REPORT.md`.
Its theorem `QFORM-AGGREGATE-HYPERBOLIC-SQUARE-v1` gives, for disjoint original-coordinate blocks,

`||p_T||_infty <= 4 M_Z sqrt(M_U M_V) / sqrt(|ab|)`.

Applied exactly to the hard bank family with `U=X_0`, `V=Y_m`, `Z=Z_m`, `a=b=1`, `M_U<=1`, `M_V,M_Z<=sqrt(2)`, this gives

`||p_Q||_infty <= 2^(11/4)`.

Thus the newly recorded local-cross-rank-three counterfamily is not a target counterexample: its aggregate-bank branch is uniformly bounded by the partner theorem. The remaining structural debt is extraction/aggregation for arbitrary matrices.

## 3. Three dependent-square lemmas

The following lemmas are useful because square completion in original coordinates produces **dependent** successive squares, but each newly exposed pivot variable still enters as fresh independent additive noise.

### Lemma 3.1 — one square is uniformly `L^(3/2)`

Let `Y` have density `h` with `||h||_infty <= M`, and let `d != 0`. Then `R=dY^2` has a density and

`||p_R||_(3/2) <= 2 M^(2/3) |d|^(-1/3)`.

**Proof.** It suffices first to take `d=1`. Put `H(r)=h(r)+h(-r)` for `r>0`; then `0<=H<=2M` and `int_0^infty H(r)dr=1`. For `z=r^2>0`,

`p_R(r^2)=H(r)/(2r)`.

Hence

`||p_R||_(3/2)^(3/2) = 2^(-1/2) int_0^infty H(r)^(3/2) r^(-1/2) dr`.

Among functions of mass one bounded by `2M`, the decreasing weight `r^(-1/2)` and convex integrand make the right side maximal for `H=2M` on `[0,(2M)^(-1)]`. Its value is at most `2 sqrt(2) M`. Raising to power `2/3` gives `2M^(2/3)`. Scaling by `d` contributes `|d|^(-1/3)`. QED.

In particular, the sharp one-dimensional product-marginal cap `M<=sqrt(2)` for a normalized linear projection of independent density-`<=1` coordinates yields

`||p_(d(s dot W)^2)||_(3/2) <= 2^(4/3)|d|^(-1/3)`.

### Lemma 3.2 — a fresh dependent square raises `L^(3/2)` to `L^6`

Let `R` have density `p_R in L^(3/2)`. Let `V` be any real random variable such that a regular conditional density of `V` given `R=r` exists and is bounded by one for almost every `r`. For `b!=0`, put `T=R+bV^2`. Then

`||p_T||_6 <= C_HLS |b|^(-1/2) ||p_R||_(3/2)`,

where `C_HLS` is the universal one-dimensional Hardy-Littlewood-Sobolev constant for the kernel `|u|^(-1/2)`.

**Proof.** Given `R=r`, the density of `bV^2` at a point of the appropriate sign is at most `|b|^(-1/2)u^(-1/2)`. Therefore

`p_T(t) <= |b|^(-1/2) int_0^infty p_R(t-sgn(b)u)u^(-1/2)du`.

The one-dimensional HLS inequality maps `L^(3/2)` to `L^6`. QED.

This lemma does **not** assert that a generic bounded conditional density is equivalent to independence. It proves only this one-sided square-smoothing inequality. In the application below the conditional cap is itself derived from an untouched independent original coordinate.

### Lemma 3.3 — an `L^q` input plus a fresh square gives `L^infty`

Let `q>2`, let `R` be a probability density in `L^q`, and suppose again that `V|R=r` has density at most one almost surely. For `a!=0`, `T=R+aV^2` satisfies

`||p_T||_infty <= C_q |a|^(-1/2) ||p_R||_q^(q/[2(q-1)])`,

where, with `alpha=(q-2)/q`,

`C_q=(1+alpha) alpha^(-alpha/(1+alpha)) [2(q-1)/(q-2)]^((q-1)/(q(1+alpha)))`.

For `q=6` this simplifies to

`C_6=(5/3)(3/2)^(2/5)sqrt(5/2)`.

**Proof.** The conditional square bound gives

`p_T(t) <= int_R p_R(t-av^2)dv`.

Split at `|v|=R_0`. On the inner part, after `u=|a|v^2` and Holder,

`I_inner <= K_q ||p_R||_q |a|^(-1/q) R_0^(1-2/q)`,

with `K_q=[2(q-1)/(q-2)]^((q-1)/q)`. On the outer part, use total mass one and `u^(-1/2) <= (|a|R_0^2)^(-1/2)` to get

`I_outer <= 1/(|a|R_0)`.

Optimizing `R_0` gives the displayed expression. QED.

## 4. New theorem: two-level localized square cascade

### Theorem `QFORM-TWOLEVEL-LOCALIZED-SQUARE-CASCADE-v1`

Let

`A_0=R Lambda R^T`, `R^T R=I_3`,

be a rank-exactly-three real symmetric quadratic form in original coordinates. Assume its three nonzero eigenvalues are the diagonal entries of invertible `Lambda` and satisfy the target normalization when this theorem is inserted into the full problem.

Choose a physical coordinate `i` with leverage `c=||R_{i,*}||_2^2>0` and nonzero scalar pivot

`a=(A_0)_{ii}`.

Let `T` be the rank-two Schur complement after eliminating coordinate `i`. Choose a remaining physical coordinate `j` whose leverage in the rank-two range is `c_2>0` and whose scalar pivot in `T` is nonzero,

`b=T_{jj}`.

Let the final rank-one Schur complement have nonzero eigenvalue `d`. Then the quadratic form admits an exact original-coordinate representation

`Q = a V_1^2 + b V_2^2 + d(s dot W)^2`,

where `W` consists of untouched original coordinates,

`V_2 = X_j + m(W)`,

`V_1 = X_i + alpha X_j + ell(W)`,

and `s` is a unit vector. Moreover

`|a b d| = c c_2 |det Lambda|`.

For arbitrary independent original-coordinate input densities bounded by one,

`||p_Q||_infty <= C_* |a|^(-1/2)|b|^(-3/10)|d|^(-1/5)`,

where

`C_* = C_6 C_HLS^(3/5) 2^(4/5)`.

Equivalently, using the pseudodeterminant identity,

`||p_Q||_infty <= C_* |a|^(-3/10)|b|^(-1/10)(c c_2 |det Lambda|)^(-1/5)`.

**Proof.** The two scalar Schur completions give the displayed representation and the source-proved pseudodeterminant identities

`|pdet T| = c |det Lambda|/|a|`,

`|d| = c_2 |pdet T|/|b|`,

hence `|abd|=c c_2|det Lambda|`.

The normalized linear projection `Y=s dot W` has density at most `sqrt(2)`. By Lemma 3.1,

`||p_(dY^2)||_(3/2) <= 2^(4/3)|d|^(-1/3)`.

Now condition on `R_0=dY^2`. Since `X_j` is independent of `W` and has density at most one, the conditional law of `V_2=X_j+m(W)` given `R_0` is a mixture of translates of the density of `X_j`, so it is still bounded by one. Lemma 3.2 gives

`||p_(R_0+bV_2^2)||_6 <= C_HLS 2^(4/3)|b|^(-1/2)|d|^(-1/3)`.

Next `R_1=R_0+bV_2^2` is a function only of `(X_j,W)`. Since `X_i` is independent of `(X_j,W)`, the conditional law of `V_1=X_i+alpha X_j+ell(W)` given `R_1` is likewise a mixture of translates of the density of `X_i`, hence bounded by one. Applying Lemma 3.3 with `q=6` gives

`||p_Q||_infty <= C_6 |a|^(-1/2) [C_HLS 2^(4/3)|b|^(-1/2)|d|^(-1/3)]^(3/5)`,

which is exactly the claimed constant and exponents. QED.

### Consequence for the B19 two-level localized branch

If the first and second localized leverages obey `c>1/2` and `c_2>1/2`, and the full target core has `|det Lambda|>=1`, then

`||p_Q||_infty <= C_* 4^(1/5)|a|^(-3/10)|b|^(-1/10)`.

Hence for every fixed `eta>0`, the entire double-localized branch with

`|a|>=eta` and `|b|>=eta`

has a universal bound

`||p_Q||_infty <= C_* 4^(1/5) eta^(-2/5)`.

So **second-level residual localization is no longer an independent obstruction away from isotropic scalar pivots**. In this branch any sequence capable of escaping this theorem must have at least one of the first two scalar pivots tending to zero.

## 5. Exact rational calibration of the Schur bookkeeping

Take the rank-three projection

`P=I_4-(1/4)11^T`,

whose nonzero eigenvalues are all one. Every original row has leverage `3/4`. Eliminating the first coordinate gives a rank-two residual with row leverage `2/3`; eliminating one of those coordinates leaves rank one. The exact scalar pivots/eigenvalue are

`a=3/4`, `b=2/3`, `d=1`,

so

`|abd|=(3/4)(2/3)=1/2=(3/4)(2/3)|det Lambda|=c c_2 |det Lambda|`.

This is only an algebra calibration; the theorem above is analytic and holds for arbitrary signs.

## 6. Application of the named fleet04/B20 result

The newly completed fleet04/B20 theorem is compatible and was applied rather than merely cited. On the disjoint-bank hard family described in its report,

`Q=2X_0Y_m+Z_m^2`,

with normalized aggregate coefficient vectors, the product-marginal caps are

`M_U<=1`, `M_V<=sqrt(2)`, `M_Z<=sqrt(2)`.

Putting these values into its exact theorem

`4 M_Z sqrt(M_U M_V)/sqrt(|ab|)`

with `a=b=1` yields

`||p_Q||_infty <= 2^(11/4)`.

This directly handles the family now used in the correction ledger to refute a naive local-cross-rank-three structural dichotomy. It also shows why the replacement structural proof must allow original-coordinate **bank aggregation**, not just fixed principal blocks.

## 7. What remains unpaid

The full target remains open. This run removes a concrete portion of the B19 two-level localization debt and imports the fleet04/B20 aggregate-bank closure. The first remaining proof obligations are now sharper:

1. **Near-isotropic pivot closure.** In the genuine two-level Schur branch, control the regimes `|a|` or `|b|` small by using off-diagonal energy / aggregate-bank structure before paying reciprocal pivot factors.
2. **Aggregate normal-form extraction.** In leverage-heavy near-isotropic branches not captured by the scalar-pivot cascade, either extract disjoint original-coordinate blocks with the fleet04/B20 hyperbolic-square structure and a dimension-free coefficient product, or control the residual `U^2/UZ` couplings by a different product-preserving aggregate argument.
3. **Higher-rank/additional-eigenvalue interaction.** A rank-three core cannot simply be separated from the rest after spectral rotation; that dependency debt remains.
4. **Continuity.** The result here proves absolute continuity and an `L^infty` bound on its stated branch. It does not prove that the density has a continuous representative.

Suggested next claim: `QFORM-NEAR-ISOTROPIC-BANK-EXTRACTION-v1`: show that a rank-three leverage-heavy configuration with a small physical scalar pivot either admits a quantitatively nondegenerate disjoint-bank hyperbolic-square normal form or has enough diffuse off-diagonal energy for a direct product-preserving smoothing bound.

## 8. Integrity

No full-solution claim is made. The theorem is source-compatible and branch-scoped. It preserves original-coordinate independence and all signs through absolute-value coefficient factors. No native mathematical-memory receiver was used, so `full_brain_connected=false` and the run remains `WITHOUT_VERIFIED_BRAIN`.
