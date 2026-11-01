# R11 / I0054 idea before code — direct path coupling and fresh perfect-match dependence

Runtime model identifies as GPT-5.6 Sol; reasoning level is UNVERIFIED, not GPT-6 maximum.

This note records the mathematical idea before any new checker is written. Current source/ownership/literature screens were completed first: Aldous–Janson arXiv:2303.02529v3 still states Open Problem 18 on printed page 58; `operations/claims/I0054.md` still gives R11 the provisional exclusive reservation with `PENDING_ADMISSION, not READY`; P13 excludes I0054 as R11-owned; current bounded literature searches recovered Part III and 2026 beta-splitting followups but no checked primary-source resolution of exact Open Problem 18. External priority remains UNVERIFIED.

Methods for this run: #4 PROVE SOMETHING WEAKER, COMPLETELY; #14 FIND THE GROUP ACTING; #23 DO WHAT THE PROPOSER DID NOT EXPECT.

## U061 route: remove the exponential `2^k` loss

U060 bounded every split coordinate and then multiplied by the number of possible splits. The stronger structure is that both the fresh-dependence hierarchy and CTCS are exchangeable fragmentations. Couple the whole coloring proposal directly rather than union-bounding coordinates.

Let `Xi_N` be any fresh exchangeable random partition of `[N]` at each harmonic-grid proposal and let

`c_N = P(1 ~_{Xi_N} 2)`.

For a visible block of size `m`, couple its `Xi_N`-block coloring to iid Bernoulli(x) colors by sharing the color of one representative per `Xi_N` block and resampling only the nonrepresentatives independently in the iid comparator. Conditional on the restricted partition, the probability that the two color vectors differ is at most

`2 x(1-x) * sum_B (|B|-1)`.

Since `|B|-1 <= C(|B|,2)` and exchangeability gives expected colliding pairs `C(m,2)c_N`, the mismatch probability at mark x is at most

`2 x(1-x) C(m,2)c_N`.

The harmonic-grid clock rate is `1/(2N x(1-x))`, so the singular factor cancels. Summing over the `N-1` marks gives mismatch hazard at most

`C(m,2)c_N (N-1)/N`.

Across all current visible blocks, `sum C(m_b,2) <= C(k,2)`. Hence the path-TV cost of replacing the fresh exchangeable-dependence model by the iid harmonic-grid model is at most

`T C(k,2)c_N (N-1)/N`.

Next compare the iid harmonic-grid model directly to CTCS without counting coordinates crudely. For an oriented red set A of size i in an m-block, with j=m-i,

`r_N(A) = (1/(2N)) sum_{s=1}^{N-1} x_s^(i-1)(1-x_s)^(j-1)`,

whereas CTCS has `r(A)=B(i,j)/2`.

For `h_{i,j}(x)=x^(i-1)(1-x)^(j-1)`, the rectangle-rule error for a bounded-variation function gives

`|N^{-1} sum_{s=1}^{N-1} h(s/N) - integral_0^1 h| <= 2 sup h / N`.

Also

`sup h_{i,j} <= 1 / C(m-2,i-1)`

because `C(m-2,i-1) h_{i,j}(x)` is a binomial probability mass. Therefore the total oriented jump-measure error on one m-block is bounded by

`(1/N) sum_{i=1}^{m-1} C(m,i)/C(m-2,i-1)`
`= 2(m-1) H_{m-1}/N`.

Summing over all current blocks yields at most `2(k-1)H_{k-1}/N`.

The resulting target theorem is

`TV(path laws on [0,T]) <= min(1, T[ C(k,2)c_N (N-1)/N + 2(k-1)H_{k-1}/N ]).`

Thus growing visible restrictions converge whenever

`k_N^2 c_N + k_N log(k_N)/N -> 0`,

removing U060's exponential `2^k` penalty.

## C081 route: fresh uniform perfect matching dependence

At each proposal sample a fresh exchangeable partition whose blocks are pairs (and, for odd N, one singleton): equivalently a uniformly random perfect matching for even N and uniformly random near-perfect matching for odd N. Color each pair-block independently Bernoulli(x) and split the active clade by inherited colors.

Then

- even N: `c_N=1/(N-1)`;
- odd N: `c_N=1/N`.

Hence U061 would imply whole-path TV convergence for every `k_N=o(sqrt(N))`, much stronger than the previous logarithmic growing-k statement.

At N=4 the model has two random pairs, so every nontrivial four-label split is 2|2 and the balanced-root probability is 1, versus CTCS(4)'s 3/11. Thus it is not a relabeling or global time-rescaling of the source.

To separate C081 from C079 as a sequence/model class, use N=9. C081 has dependence-block profile 2+2+2+2+1, while C079 has 3+3+3. Their pair rates and four-label total split rates yield different scale-free ratios. The exact target values to verify are:

- C081: pair rate `64/81`; four-label total rate `7240/5103`; ratio `905/504`.
- C079: pair rate `2/3`; four-label total rate `74/63`; ratio `37/21`.

Since `905/504 != 37/21`, no global time rescaling or relabeling identifies the two classes.

If the exact checker confirms these formulas, the frozen class metric should move `80 -> 81`, still with source/campaign status PARTIAL until the required two outside audits and admission conditions are met.
