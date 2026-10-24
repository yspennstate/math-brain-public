# PROB10-07 idea checkpoint — matched-biclique width 6

Parent target: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests**. Parent status remains OPEN/PARTIAL. This file is an idea-before-code checkpoint only; it does not claim a theorem.

Nonoverlap: P14/HARD10-01 own the complete-graph-order history and the 3-connected / three-separator obstruction. This route does not enumerate arbitrary graphs and does not modify their claims. It continues the complementary structural-family line after `runs/prob10_2026-09-20/PROB10-07/20260920T1308Z_matched-biclique-m4-m5-two-nilpotent.md`.

## Frozen candidate family

For terminal width `m=6`, let

`G_6(k,r)=K_{6,2k+r}+M_k`, `k>=1`, `r>=0`,

where `M_k` is a matching on `2k` right-side vertices and there are no other right-right edges. The exact target is `Delta_G(e,f)=Z_e Z_f-Z Z_ef >=0` for every distinct present edge pair, where all counts range over all forests.

## Three materially different unexhausted approaches

1. **Two-nilpotent exact response, width 6.** Keep the exact terminal-partition algebra from the preceding width-4/5 proof: `S=7I+N` for one ordinary right vertex, `P=62I+Q` for one matched pair, `NQ=QN`, and every word of total nilpotent degree at least 6 vanishes. Reduce the 14 edge-pair orbit types to exact bivariate Rayleigh polynomials in the numbers of unmarked matched-pair and singleton layers. This is the main route. It is a new width, not a graph-order census.

2. **Deletion–contraction on a matching edge.** For a nonmarked matching edge `g`, write the forest counts in the deletion and contraction environments and use the exact mixture identity for the Rayleigh difference. This would give an induction in `k` if the environmental response product had the right sign or a sharp domination by endpoint Rayleigh gaps. The preceding P14 history warns that endpoint Rayleigh signs alone do not control this term, so this route is used as a falsification test rather than an assumption.

3. **Counterexample-first exact arithmetic inside the same family.** Before promoting coefficient positivity, directly enumerate small source-valid graphs `G_6(1,0)` and, if feasible, `G_6(1,1)` in the original edge-subset model and compare every actual edge pair with the transfer certificate. A verified negative Rayleigh numerator in this family would be a genuine counterexample to the original conjecture and would take precedence over proving the family.

## Critical claim to falsify

The width-4/5 proof used positivity of every coefficient of each normalized orbit polynomial. There is no a priori theorem that this coefficientwise positivity survives at width 6. The checker must therefore reconstruct the terminal transfers from forest edge subsets, verify the nilpotent identities exactly, generate all 14 orbit polynomials with rational arithmetic, and reject the route immediately if any physical parameter point gives a negative Rayleigh value.

No scheduler, claim, ledger, email, Drive, or public-posting state is changed by this checkpoint.