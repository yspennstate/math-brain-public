# C0054 independent route, recorded before reading w603/w604 proof drafts

Date: 2026-10-10. Source: Bourgade, *Random band matrices*, arXiv:1807.03031, (0.1), (0.2), section 2.2. The source predicts two-dimensional bulk localization for fixed W on length scale exp(W^2), plus Poisson-side statistics. These are conjectural and separate targets. Current openness: UNKNOWN after a bounded primary-source search.

## Proposed route

For a regular-entry subfamily, try a finite-volume multiscale analysis on square boxes. Prove a base-scale Green-function decay estimate for every bulk E on a box with side L_0(W) comparable to exp(cW^2), with a small failure probability. Then control resonant boxes at each scale, using conditional independence only after spelling out which matrix entries each box event uses. A completed localization result would still need a separate Minami-type input or replacement to obtain Poisson statistics.

The single hardest open piece is the **bulk base-scale decay estimate at exp(cW^2)** for arbitrary fixed W. A small failure probability or spectral averaging alone does not give that estimate. The 2018 survey's conductance/Gaussian-free-field discussion is heuristic, not the needed initial-scale theorem.

## Immediate obstruction in the full source class

This route cannot invoke a universal interval-length Wegner estimate under the source hypotheses. For N>2W let q_W be the number of sites within periodic L1 distance W of each vertex, including itself, and put H_xy=q_W^{-1/2} eps_{\{x,y\}} for allowed pairs, zero otherwise, with independent fair signs eps. The model is real symmetric, centered, row-variance normalized, of comparable nonzero variance, and uniformly subgaussian after multiplying entries by W. It is therefore inside the survey's class.

For every sign configuration Tr(H^2)=|Lambda|, so at least one eigenvalue lies in [-1,1]. Fix a configuration H_0 and one such eigenvalue E_0. The event H=H_0 has probability 2^{-m}>0, where m is the number of independent allowed unordered pairs. Every interval I containing E_0 has E Tr 1_I(H) >= 2^{-m}. As |I| tends to zero, no finite constant C_{N,W} can make E Tr 1_I(H) <= C_{N,W}|I||Lambda| hold for all intervals I. In particular a uniform Wegner estimate, and any Minami argument requiring continuous spectral averaging, needs extra entry regularity or a different method. This does not refute the localization conjecture.

Next: send this narrow obstruction to w608 for independent audit; inspect w603 and w604 only after this approach is saved; rederive their hardest claim from definitions.
