# Uniform condensation windows: continuation of Janson 18.40

Date: 17 September 2026. This contribution continues the full-path proof at `runs/2026-09-17/direct_janson1840_full_path_11-47-17Z/`, final predecessor commit `c867a507d155314bff77e0ba2768de0daccd0c1c`.

**Status: FULL-SCOPE COMPLETE PROOF CANDIDATE, WITH STRENGTHENINGS. Independent end-to-end audits: 0/2. Publication novelty: UNVERIFIED.** This is a further derivation by the same assistant, not an independent audit. No shared ledger, prior proof, peer file, or scheduled task was changed.

## Stronger conclusion

For every fixed nonnegative zero-radius weight sequence with `w_0 > 0`, every `epsilon in (0,1)`, and every compact density interval `0 < alpha < beta < infinity`, the candidate theorem gives `delta > 0` and supported sizes `k_r -> infinity` such that

```text
sup P(Y_max(m,n) <= (1-epsilon)m) -> 0,
```

where the supremum ranges over every admissible integer pair satisfying

```text
(1+3 delta) k_r <= m <= (1+5 delta) k_r,
alpha <= m/n <= beta.
```

Thus condensation is uniform over a whole interval of total masses and over all box counts in the density range. The same windows work for all those pairs; they are not selected separately for each mass path. The density interval and desired accuracy are fixed before taking the limit.

The previous full-path conclusion follows: for every prescribed admissible path `m_n/n -> lambda in (0,infinity)`, with arbitrary jumps, some subsequence has `Y_max/m_n -> 1` in probability. For every fixed accuracy, there are also intervals containing a number of consecutive sizes proportional to their location on which the failure probability tends to zero uniformly. This does not assert condensation at every size, regularly spaced good windows, or a rate uniform in the weights.

## What the recheck changed

The occupation-count insertion inequality was rederived using both count-vector factorials and labelled weighted double counting. This yields the sharper finite inequality

```text
Z(m,n) >= w_k W_r Z_u(t,n) (n-t)_[Q]
          / product_j (min(n,floor(m/j)))_[r_j],
```

where `r_j` are multiplicities in a fixed supported residual representation, `Q=1+sum r_j`, `u<k`, and `t+Q<=n`. Falling factorials are denoted by `_[.]`. The earlier coarser bound is a consequence. The condition `m<2k` is unnecessary for this finite insertion lemma, since every image has exactly one size-k box by construction.

The geometric record argument is now deterministic. Define

```text
G_J = k_J (B_J-B_{J-1}) - b log(k_J) - E_J,
```

with the residual energy bound `E_J` given explicitly in the paper. The proof shows `limsup G_J = infinity`, independently of any allocation probability. Whenever the finite mean and size conditions hold, every pair in the corresponding mass window satisfies

```text
P(Y_max <= u_J) <= min(1, C exp(-G_J)).
```

A finite-prefix lower bound for the weighted sum of `G_J/k_J` is also proved with explicit geometric constants. It makes the finite-prefix absorption and the once-per-plateau accounting checkable without supposing a lower bound on an unknown probability.

The standalone greedy lemma now explicitly requires `J >= i_0+D`. All applications in the predecessor already met that condition; this clarifies its domain, not a restriction on the main theorem. The other reviewed steps were the image injectivity, repeated-size multiplicities, the cancellation of the identical small-box factor `A^n`, the geometric-kernel coefficient, plateau charging, span reduction, and the order of fixed parameters followed by diagonal selection. No additional unresolved mathematical step was identified in this self-review. That statement is not independent certification.

## Sharpness and a tree consequence

For an infinite sampled index set `N_1<N_2<...`, the condition `N_{j+1}/N_j -> 1` is necessary and sufficient for a near-total-condensation subsequence theorem valid for every such weight sequence and every admissible positive-density path on that set.

Necessity is constructive. If infinitely many gaps have ratio at least `theta>1`, put the large support points at their left endpoints, add weights at zero and one, and set `w_k=exp(k^2)` at the large support points. Along the tree path `m=n-1` sampled on the given set, every available supported size is at most `n/theta` (apart from the harmless unit size). Thus near-total condensation is impossible throughout that sampled set. With unbounded gap ratios, one can force `Y_max/n -> 0` deterministically on the entire sampled set. This is not a claim that every weight sequence fails on a nondense index set.

For simply generated plane trees, the candidate also gives a subsequence on which the root has `(1-o_P(1))n` children, is the unique maximum-degree vertex with probability tending to one, and only `o_P(n)` vertices lie at depth at least two. This application uses the known size-biased root identity in Janson's Lemma 14.7 / equation (19.1). That identity is explicitly attributed, not claimed as a new result.

## Executed exact checks

Run in this directory:

```bash
python3 check_uniform_windows.py > checks.reproduced.json
cmp checks.json checks.reproduced.json
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The standard-library-only checker uses the bundled predecessor script, or the sibling repository file pinned by SHA-256. The downloadable ZIP contains that dependency and is self-contained.

Results: **ALL_EXACT_CHECKS_PASS**, reproduced byte-for-byte in a second execution. The new checks include all 97 integer pairs with `20<=m<=22` and `1/2<=m/n<=2` for one explicit fixed sparse law; 97 span-three coefficient checks; 412 exact finite-prefix inequalities; deterministic sampled-support checks; and enumeration of all 6,917 plane trees of sizes 2 through 10, checking 283 conditional root-degree identities across 96 degree-count classes. The predecessor's 12 occupation-count, 16 kernel, 36 plateau and 391 greedy checks were reexecuted.

For the explicit law, `w_0=1`, the positive support below 120 is `{2,3,5,17}`, and `w_j=2^(j^2)` there. Adding factorial support points `j=l!`, `l>=5`, with the same weights defines one fixed infinite zero-radius sequence. Across the entire tested mass/density window, the sharp insertion bound certifies

```text
P(Y_max <= 3m/4) <= 2^(-189).
```

The largest actual probability is approximately `1.5098622004476568e-58`; its exact rational is saved in `checks.json`. The predecessor's coarser insertion inequality gives the weaker but still exact uniform bound `2^(-183)`.

During checker development, an expected list of large sample gaps omitted the boundary gap `2 -> 3` at threshold `3/2`. The expected list was corrected to include it; the mathematical inequality already allows equality and was unchanged. All final assertions, including that boundary case, pass. These finite tests are not a formal proof of the asymptotic theorem and are not independent audits.

## Source and delivery scope

Primary source: S. Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), 103-252, DOI 10.1214/11-PS188, arXiv:1112.0510, Section 18.6, Problem 18.40. The question and neighboring example were visually rechecked on PDF page 122; Lemma 14.7 and equation (19.1) were recovered for the root consequence. The positive-boundary-mean Problem 18.39 is not solved here. Bounded current-literature searches did not establish publication novelty; no priority clearance is asserted.

The ten-page PDF compiles without undefined references or overfull-box warnings and was inspected in a PDF renderer. The repository contains the mathematical source and exact checker/output; the conversation package also includes the compiled PDF. Prior candidate files remain unchanged. Source-registry promotion is deferred pending independent verification.
