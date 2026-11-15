# Substantial claimed advance found; full T050 remains unresolved here

Reference: **OpenAI**, *Strict convexity and differentiability of the planar
exponential first-passage limit shape*, September 24, 2026, OpenAI Math Release
preprint.

- [Manuscript opened (95-page PDF)](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf)
- [Publisher's repository location](https://github.com/openai/math/tree/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026)
- [Landing page opened](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/)

**arXiv identifier:** not located. The opened landing page supplies a repository
preprint citation, not an arXiv identifier. Do not invent one.

## Exact scope of the manuscript's claims

Theorem 1.1, PDF page 3: undirected nearest-neighbor FPP on Z² with iid
exponential edge weights, of any rate λ > 0, has a strictly convex limit shape
with C¹ boundary; its time-constant norm is Fréchet differentiable away from zero.

Theorem 1.2, same page: for iid Gamma weights of any positive shape and rate,
the planar time-constant norm is Fréchet differentiable away from zero and its
unit sphere is C¹. This theorem does **not** assert strict convexity for general
Gamma laws. Neither theorem establishes the full continuous-law conjecture in
all dimensions.

## Verification limits

This is a located preprint claim, not an independently verified solution in this
session. The theorem statements and the concluding proof of Theorem 1.1 in
Section 16 were inspected; the intervening arguments were not fully audited.

The [author's formalization scope note, opened directly](https://raw.githubusercontent.com/openai/math/main/lean/docs/212.md)
explicitly excludes exponential strict convexity from its selected Lean
statements. It describes differentiability for positive Gamma laws, including
exponential weights. A formalization claim for differentiability cannot certify
the strict-convexity assertion. No Lean checks were run here.

The date predates the supplied November 2026 status check. Thus it is a missed
recent claim contradicting that status paragraph, rather than a result dated
after November 2026. The requested stop branch is taken because of its direct
relevance and substantial claimed scope; the filename does not certify acceptance
or correctness.
