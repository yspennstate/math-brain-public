# Attempt

## Exact statement and conventions

Let B be the continuous two-parameter R^d-valued Brownian sheet with independent coordinates and covariance Cov(B_i(s,t),B_j(u,v))=δ_ij min(s,u)min(t,v). Let Z={(s,t)∈(0,∞)²:B(s,t)=0}, and d∈{2,3}. Does an orthogonal projection onto a possibly B-dependent random line have image dimension different from 2−d/2?

**Answer: no, almost surely. This question is solved in the literature.** The exact theorem, source quotations, page numbers and bibliographic evidence are in LITERATURE.md. The dimensions are 1 for d=2 and 1/2 for d=3.

The source's Open Problem 4 omits a repeated dimension restriction, but page 3 identifies d=2,3 as the range where its target dimension is the zero-set dimension and can equal a line-image dimension. The deterministic zero axes are excluded. A literal interpretation with d=1 would give an impossible target of 3/2 for a subset of a line; a literal interpretation including the axes would also change the problem. These are convention checks, not counterexamples to the intended question.

## Complete application proof

Chen–Woessner, arXiv:2405.20019v2, Theorem 1.2 (page 2), provides an event Ω₁ of probability one such that, for every ω∈Ω₁ and every nonzero linear map p:R²→R, dim_H p(Z(ω))=dim_H Z(ω). Proposition 1.1 on the same page provides an event Ω₂ of probability one on which dim_H Z=2−d/2. These are published probabilistic results used as inputs, not new results claimed here.

Set Ω₀=Ω₁∩Ω₂. Fix ω∈Ω₀. For each line L choose a unit vector u∈L. Define p_u(x)=⟨x,u⟩ and J_u(r)=ru. Then p_u is a nonzero scalar linear map, J_u is an isometry onto L, and the orthogonal projection onto L is P_L=J_u∘p_u. Isometries preserve Hausdorff dimension, so

dim_H P_L(Z(ω)) = dim_H p_u(Z(ω)) = dim_H Z(ω) = 2−d/2.

This argument holds for every L on Ω₀. Consequently, for any random line L(ω), the same identity holds for every ω∈Ω₀. Dependence on the sheet is immaterial because the universal quantifier is already inside the common probability-one event. Orthogonal projections onto affine lines, if included, differ from these by an isometry and translation and have the same image dimension. This proves the requested negative answer directly from the source-matching theorem.

## Referee checks

1. **Objects:** identical Brownian-sheet law; same strictly positive parameter zero set. Later proof localizes to [a,b]² with 0<a<b (page 4). Both formulations exclude the deterministic zero axes for the nontrivial dimension statement.
2. **Dimension range:** Theorem 1.2 expressly covers N=2 and d=2,3. No extrapolation to unmentioned dimensions is used.
3. **Quantifier:** the theorem states “almost surely, for any” and the following paragraph explicitly explains the placement of this quantifier. It is stronger than “for each fixed p, almost surely.”
4. **Orthogonal versus scalar projection:** the isometry J_u gives the equality of image dimensions exactly; no additional geometric theorem is needed.
5. **Proof present:** full Section 2 is titled “Proof of Theorem 1.2” (pages 4–7), with the final Step 3 proving uniformity in p on page 7. This is not merely an abstract announcement.
6. **Publication:** Crossref confirms J. Theor. Probab. 38 (2025), article 33, DOI 10.1007/s10959-024-01399-1. Springer HTML/PDF requests returned a client challenge; the quoted full-text theorem is specifically from the accessible arXiv v2.
7. **Prior attempt:** the earlier fixed-direction argument was not used to justify the stronger simultaneous result.

No new theorem, numerical evidence, or Lean-verified Brownian-sheet proof is claimed. Step 1 of the requested workflow terminates the task once an exact stated-and-proved literature solution is confirmed; consequently, no further independent attack, numerical experiment or Lean formalization is needed. A tentative tube-moment approach was considered before the direct solution was verified, but was not completed or used in the verdict.

## Remaining gap

None for the intended D0019 question with positive parameters and d=2,3. This record verifies the theorem and its exact applicability; it does not claim to have independently formalized or reproduced every estimate in the authors' proof. Journal PDF pagination was not inspected; all theorem/proof page references here are to arXiv v2.
