# R01 G0012 proof correction — global versus per-plan deviation averaging

This memo corrects one quantifier overstatement discovered during the post-commit self-audit of
`runs/R01/20260917T0802Z_g0012_biregular_heatbath_7b4e2c19.md`.

The run report states Lemma 5.1 and the first paragraph of Section 7 as though the `1/4` bad-deviation conclusion held **for every individual simple base plan**. The non-returning and final-endpoint estimates are per-plan, but Dozier's middle-returning excursion-reversal involution pairs deviations across the global set of simple base plans. Therefore the correct statement is an **average/global** one. The theorem and constants remain unchanged because, on a bipartite `(a,b)`-biregular graph, every `k`-simple base path has exactly the same raw deviation count `W`.

## Corrected Lemma 5.1

Let `S` be the set of `k`-simple plans with the fixed starting edge. For each `rho in S`, let `D(rho)` be its `W` raw deviation classes `(i,c)`. If

\[
k\ge 96,\qquad L\ge 48n/k,
\]

then among the disjoint union

\[
\mathcal D=\bigsqcup_{\rho\in S}D(\rho)
\]

at least one quarter of all raw deviation classes are not `L`-simple.

### Proof

For each fixed `rho`, the non-returning `L`-simple classes are at most `2m/L`, hence by the report's (4.3) at most `W/8`. Thus globally they contribute at most `|S|W/8`.

For each fixed `rho`, the final-endpoint exceptional classes are at most `d(v_k)-1`, hence by the report's (5.3) at most `W/8`. Thus globally they contribute at most `|S|W/8`.

The remaining returning classes are the middle-returning classes plus classes that return to the base path at or before the departure point. The latter are automatically non-`L`-simple. On the set of middle-returning classes over **all** `rho in S`, Dozier's excursion-reversal construction is an involution. It remains valid at variable degrees because every altered local map is a derangement on the same incident-edge set and inversion preserves that set. In each reversal pair, at most one member is `L`-simple. Therefore at most half of all middle-returning classes are `L`-simple.

Consequently the total number of `L`-simple raw classes is at most

\[
\frac18|S|W+\frac18|S|W+\frac12|S|W
=\frac34|S|W,
\]

so at least one quarter of `\mathcal D` is bad. QED.

## Corrected early restriction

Removing the last `L` departure indices deletes at most `W/8` raw classes **from each base plan** when `L<=k/96`, hence at most `|S|W/8` globally. The corrected global Lemma 5.1 therefore leaves at least

\[
\frac18|S|W
\]

early bad raw classes.

Under the report's heat-bath proposal, each raw class carries total proposal mass exactly `1/W`, because after the raw class `(i,c)` is selected the conditional resampling probabilities over all target derangements sum to one. Hence the **total** early-bad proposal mass out of the uniform counting measure on `S` is at least

\[
\frac18|S|.
\]

This is exactly the lower bound used in Section 7's double count. No per-source lower bound is needed.

The incoming bound for a fixed non-simple target plan is unchanged: at a candidate index `i`, summing over all possible source local derangements cancels `R'_{d_i}` and gives at most `(d_i-2)/W`; summing over the at most `L+1` candidate indices gives at most `12(L+1)/k`. Therefore

\[
\frac{|S|}{8}
\le
|T\setminus S|\frac{12(L+1)}k,
\]

and all subsequent inequalities, including

\[
P(\text{simple})\le 4800\,\frac{n}{k^2}
\quad\text{for }k^2\ge4704n,
\]

remain unchanged.

**Verdict after correction:** the report's theorem statement and constants survive; only the per-plan wording of the bad-deviation lemma is replaced by the correct global averaging statement.