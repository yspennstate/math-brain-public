# B13 FEI creative run — block/profile Booleanity route

**Status: PARTIAL. Full FEI remains OPEN.**

Primary route: APPROACH 2/13. No read-once certificate rerun and no FEI audit was performed.

## Movement this run

The previous exact `n<=4` experiment had shown that every *fully product* Boolean spectral law it found had marginals only in `{0,1/2,1}`. This run upgrades that observation to a dimension-free theorem and weakens the hypothesis from full product structure to independence of just one spectral membership bit from the rest.

For a Boolean `f` with spectral sample `X`, if `X_i` is independent of `X_{-i}`, then

`Inf_i(f)=P(X_i=1) in {0,1/2,1}`.

The proof is in `PRODUCT_SPECTRAL_RIGIDITY.md`. It combines exact independence of squared Walsh coefficients with Boolean Fourier inversion. If `0<q_i<1`, independence makes the ratio of paired squared Walsh coefficients constant. Since Walsh coefficients are integers, the square root of that ratio is rational, say `u/v`. Boolean inversion splits the `(n-1)`-cube into unchanged and flipped `i`-edges of sizes `a,b`, with `b/a=u^2/v^2` and `a+b=2^{n-1}`. Thus `u^2+v^2` divides a power of two; coprimality and parity force `u=v=1`, hence `q_i=1/2`.

A corollary classifies exact product spectral laws: after removing irrelevant coordinates and multiplying by a character, they are exactly flat-spectrum (bent) Boolean functions on an even number of active coordinates. This explains the prior `n<=4` product-law counts exactly.

## New decisive finite calculation

An independent exact integer enumeration checked the stronger one-coordinate theorem on all Boolean functions up to global negation for `n<=4`:

- `n=1`: 2 independent coordinate cases, 0 bad marginals;
- `n=2`: 16 independent coordinate cases, 0 bad marginals;
- `n=3`: 120 independent coordinate cases, 0 bad marginals;
- `n=4`: 6848 independent coordinate cases, 0 bad marginals.

Every independent coordinate had `q_i` equal to `0`, `1/2`, or `1`. The exact checker and output are saved beside this report. The finite calculation is supportive only; the theorem itself is analytic and dimension-free.

## FEI consequence and remaining gap

This rules out the most obvious entropy/mean-size obstruction: a product random subset with tiny independent marginals cannot be the exact spectral sample of a Boolean function. In information language, Booleanity forces

`q_i notin {0,1/2,1}  =>  I(X_i;X_{-i})>0`.

What FEI still needs is a *quantitative* correlation tax. Total correlation obeys

`TC(X)=sum_i h(q_i)-H(X)`.

To convert the rigidity theorem into FEI one needs a dimension-free lower bound on `TC(X)` when many `q_i` are small. A concrete stronger target is an ordering `pi` and universal `C` for which

`sum_k I(X_{pi(k)}; X_{pi(<k)}) >= sum_k [h(q_{pi(k)})-C q_{pi(k)}]_+`.

The left side is exactly total correlation. The present theorem proves only the zero-defect endpoint. Its divisibility argument is not robust under approximate independence, so no universal modulus is claimed.

## Next creative move

Robustify the paired-Walsh-ratio argument. For fixed `i`, let the conditional odds of `X_i` given `X_{-i}=R` be the ratios `W_{R,1}^2/W_{R,0}^2`. Their information-theoretic dispersion around the global odds is `I(X_i;X_{-i})`. Seek a Boolean inverse-transform inequality that lower-bounds this dispersion when `q_i` is far from `{0,1/2,1}`, and then seek an ordering/charging rule that sums the coordinate taxes without replacing total correlation by the generally larger `sum_i I(X_i;X_{-i})`.

Prior-art novelty for the rigidity theorem is **UNVERIFIED**; no novelty claim is made here.
