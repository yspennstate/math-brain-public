# Literature check, 14 November 2026

The search was limited to less than ten minutes. No complete solution of the
fixed four-corner problem was found. This is a search result, not a proof
that no solution exists.

The following primary sources were opened:

1. Caleb Marshall, *Improved Power Laws for the Favard Length Problem in All
   Dimensions*, [arXiv:2509.02882v2](https://arxiv.org/html/2509.02882v2),
   revised 12 August 2026. Corollary 8.2 proves the four-corner upper bound
   \(N^{-1/5+u}\) for every \(u>0\). This was already in the brief.
2. Damian Dąbrowski, *Survey on Favard length and rectifiability*,
   [arXiv:2610.35502v1](https://arxiv.org/html/2610.35502v1),
   26 October 2026. Section 2.5, Problem 2.33 explicitly asks for the rate.
   Equations (2.16) and (2.20) give the \(1/5-\varepsilon\) upper
   exponent and \(\log n/n\) lower bound, respectively.
3. Caleb Marshall, *Nearly Sharp Uniform Projection Bounds and Superlinear
   Vitushkin Inequalities for Deterministic Self-Similar Sets*,
   [arXiv:2610.22908v1](https://arxiv.org/html/2610.22908v1),
   16 October 2026. Constructs different self-similar systems, with rotations,
   for each prescribed exponent below one. The theorem does not apply to
   the fixed four-corner system.
4. Alan Chang, Pablo Shmerkin, Ville Suomala, *Sharp Favard Length of Random
   Cantor Sets*, Geometric and Functional Analysis 36 (2026), 786–830,
   [DOI:10.1007/s00039-026-00743-3](https://doi.org/10.1007/s00039-026-00743-3).
   Gives sharp rates for random models; its introduction distinguishes the
   deterministic four-corner lower bound.
5. Alan Chang, Damian Dąbrowski, Giacomo Del Nin, *Favard length of
   non-homogeneous random disc-like Cantor sets*,
   [arXiv:2609.33557](https://arxiv.org/abs/2609.33557), 27 September 2026.
   Gives sharp estimates for random non-homogeneous variants.

An additional primary software source was opened:
[CoolRmal/FavardLength README](https://github.com/CoolRmal/FavardLength).
It reports an upper bound with exponent 156307/625000 = 0.2500912 and
claims Lean kernel verification. Its provenance section attributes the
underlying unpublished manuscripts to Yongxi Lin, and says they have not
been externally refereed. No corresponding arXiv identifier is provided
there. The mathematical bridge and claimed kernel builds were not audited
in this session. This is an unverified lead for the next literature worker,
not an established improvement asserted here. Even if correct, it would
leave the exact rate unresolved.

The session's completed piece is the finite computation in `PROOF.md` and
`data/`; it is independent of all these asymptotic upper-bound claims.
