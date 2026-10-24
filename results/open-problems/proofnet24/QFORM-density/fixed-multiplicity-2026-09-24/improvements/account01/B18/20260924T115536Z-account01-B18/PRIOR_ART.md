# Primary-source prior-art audit and suggested attribution patch

Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Source-valid matches

### Bennett–Carbery–Christ–Tao

J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp–Lieb inequalities: finiteness, structure, and extremals*, arXiv:math/0505065 (published in GAFA).

Scope match: classical Brascamp–Lieb structure and heat-flow monotonicity. The manuscript proves its geometric rank-one specialization internally, so this is attribution rather than an imported theorem.

### Rudelson–Vershynin

M. Rudelson, R. Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492.

Scope match: independent real coordinates with bounded densities; orthogonal projections and, in dimension one, the sharp `sqrt(2)K` density bound for normalized linear combinations. No iid or moment assumptions are needed for that density theorem. The manuscript's projection estimate is weaker but self-contained.

### Livshyts–Paouris–Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949.

This is relevant omitted prior art. For product densities with one-dimensional caps one, the paper gives the sharp `2^{k/2}` marginal-density scale in the stated range. It is closer to the manuscript's Lemma `lem:projection` than the general-constant RV theorem and should be cited. It does not create any independence after projection.

### Banks–Garza Vargas–Kulkarni–Srivastava

J. Banks, J. Garza Vargas, A. Kulkarni, N. Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, arXiv:2005.08930; Ann. IHP Probab. Stat. 60 (2024).

Theorem 2.1 is explicitly titled “Density of Quadratic Forms” and treats bilinear-affine maps of two independent bounded-density banks. Corollary 2.4 gives an improved scalar-output estimate using a geometric mean of leading singular values. This is direct prior art for cross-block anticoncentration.

It does **not** subsume the manuscript's regularized determinant theorem as stated: the manuscript permits arbitrary measurable same-bank phases `F(X_I)+G(X_J)`, including unrestricted within-bank quadratic terms. Thus Banks et al. is relevant related work, not an exact prior solution of the fixed-multiplicity theorem.

### Herry–Malicet–Poly

R. Herry, D. Malicet, G. Poly, *Regularity of laws via Dirichlet forms — Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488.

Scope mismatch for the present theorem: their inputs are iid and the common law is assumed representable as a sufficiently smooth function of a Gaussian field. This is much narrower than arbitrary non-iid bounded densities.

## Suggested manuscript wording

A publication version could replace the current brief antecedent sentence by something like:

> Geometric Brascamp–Lieb and bounded-density projection inequalities have classical antecedents in Bennett–Carbery–Christ–Tao and Rudelson–Vershynin; sharp product-marginal constants were obtained by Livshyts–Paouris–Pivovarov. Bilinear-affine quadratic-form density estimates in terms of singular values also appear in Banks–Garza Vargas–Kulkarni–Srivastava. Our specialized inequalities are proved here at the constants used below; in particular, the crossing determinant estimate retains arbitrary same-bank measurable phases arising from the two within-bank parts of a quadratic polynomial.

Add bibliography entries for LPP and Banks et al. Herry–Malicet–Poly may be cited in a broader related-work paragraph if desired.

## Novelty caution

A targeted current primary-source search found no exact theorem matching all arbitrary-law, arbitrary-sign, arbitrary-affine hypotheses of the 17-direction statement. This is **not** evidence of novelty or priority by itself, and this file makes no such claim.
