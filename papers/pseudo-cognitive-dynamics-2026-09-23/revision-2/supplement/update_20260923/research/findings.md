# Research update findings — 23 September 2026

## Snapshot and scope

The refreshed `yspennstate/math-open-problems` snapshot is **24597f0dcc3cc32d81fd8f22b13903f636460396**, committed at **2026-09-23 20:04:37 UTC**. The default branch is `master`. Comparing with the previous paper's source `b4745ece98fa3839cf7afe35d829d08384c815b4` reports 271 additional commits and 269 changed paths, all below `proofnet24/QFORM-density/`. The eight intake queues and the prior catalogue counts (1,391 rows, 1,168 distinct identifiers, 87 top-level ProofNet directories) did not change in this comparison. This is a focused review, not a full audit of all 269 changed files.

The broad-memory review uses `<private-repo>@9c754d786b3a0ea4943da0585d1490c13cd9ef99` (19:52:16 UTC). Its cards are claim summaries; the underlying source paper, theorem statements, and proof interfaces were read where material. The separate Math Brain snapshot supplied by the parent is `96705ab32952783ed63bc4d3f9ea3ff9ed5bf222`. No schedules, live repositories, or existing paper files were changed by this review.

## 1. QFORM: improve the fixed-dimension statement without inventing new progress

The updated QFORM manuscript is entitled *Density Bounds for Quadratic Forms under Product Measures*. It foregrounds the arbitrary-real-matrix formulation: for a real matrix B, only A=(B+Bᵀ)/2 enters XᵀBX. The spectral hypothesis must concern s₃(A), not s₃(B). A nonzero skew-symmetric B can have full rank while its quadratic form vanishes identically.

For independent coordinate densities bounded by one and arbitrary affine terms, the source states

**||p_Q||∞ ≤ 2√(6πn)/s₃(A)**.

This is uniform over all matrices A of the specified dimension and spectral scale, over the entire remaining spectrum, over b,c, and over the input laws. It is therefore stronger than merely saying that each fixed matrix has some bounded density. It remains dimension dependent. The separate result that each fixed rank-at-least-three matrix gives a continuous density vanishing at infinity is a different regularity statement.

**Crucial delta classification:** the exact √n theorem and its projected-gradient proof already occur, unchanged, in the old frozen source. The new manuscript changes emphasis and adds the symmetric-part clarification. Our paper currently mentions only an O(√n) bound; replace that abbreviated wording by the exact formula and its quantifiers, but do not describe this as a theorem proved since the previous snapshot.

### Focused proof review

The source proof (`structure.tex`, `thm:projected-gradient-slicing` and `thm:finite-dimension`) is coherent under the cited standard two-dimensional projection-density bound. Choose a three-dimensional invariant subspace E with |λ|≥σ. The projected gradient is g=2(A|E)(P_EX−z₀), so |g|≥2σ|P_EX−z₀|. The identity ∇Q·g=|g|² gives a sum of nonnegative coordinate contributions after taking absolute values. For coordinate i, choose a two-plane E_i⊂E∩e_i⊥. Its projection depends only on the remaining independent original coordinates. Coordinate change of variables has at most two roots, giving a bound proportional to √ℓ_i E|P_{E_i}X−z|⁻¹/σ. The unconditional planar density cap 2 implies E|Y−z|⁻¹≤2√(2π). Summing √ℓ_i and using Σℓ_i=3 gives √(3n).

This does **not** apply an unconditional projection bound to a conditional rotated law. It conditions only on original coordinates and deliberately chooses a plane that excludes the integration coordinate. This makes it a useful constructive counterpart to the earlier invalid conditional-projection route.

The semidefinite 17100/s₃(A) and Gaussian-mixture <3 bounds remain the same scoped results. The general dimension-free indefinite conjecture remains explicitly **OPEN**. The source's lower bound C≥3√2 is also already present in the prior snapshot: normalized sums of unit uniforms converge to N(0,1/12), whose (2,1)-signature quadratic density at zero is 3√2. This is consistent with the <3 mixture bound because the mixture theorem imposes an additional average component-peak hypothesis.

Cite `CaseQFORMCurrentMain2026` and `CaseQFORMCurrentStructure2026`.

## 2. Newly added, checked supporting results

### Shift-stable joint L² estimate

The new note `20260923T200500Z-shift-stable-product-l2/REPORT.md` proves the following. H is independent of an arbitrary triple (L,V,P), H has a density ≤1, and (L,V) has joint density g≤M. For **any** measurable u(L,P), let Z=L[H+u(L,P)]. Then (Z,V) has a joint density k with

**||k||²₂ ≤ 4M**.

The constant 4 is sharp at M=1 (independent centered unit uniforms, u=0). In particular u=βL/2+εP retains both βL² and dependent leakage εLP.

I checked the analytic proof. At fixed v, the density collision integral is bounded by
∫g(l,v)g(l′,v)/max(|l|,|l′|) dl dl′,
because the overlap of two shifted, rescaled cap-one hub densities is at most min(|l|,|l′|), uniformly in the shifts. With m(v)=∫g(l,v)dl and F_v(r)≤min(m(v),2Mr), layer cake gives ∫F_v(r)²r⁻²dr≤4Mm(v). Integrating over v gives 4M.

The same source proves finite-p bounds ||k||p≤p(2M)^(1−1/p), but it correctly leaves the next step open: for Q=2Z+V², the density is a restriction of k to a parabola, and an L² bound in the plane does not control that restriction. Even bounds for every finite p do not imply the needed endpoint trace bound. This is a particularly clear mathematical example for the paper: an invariant can survive arbitrary dependent shifts while still failing to pay for the target theorem's final operation.

Cite `CaseQFORMShiftL2_2026`.

### Independent hub with a dependent planar light law

The newly added `20260923T203100Z-beta-uniform-one-hub-square/REPORT.md` proves

**||p_{2tHL+βL²+λV²}||∞ ≤ 1/2 + 4√2 M/(|t|√|λ|)**,

where tλ≠0, β is arbitrary, H is independent of (L,V), H has density ≤1, and (L,V) has any joint density ≤M. All deterministic affine terms are covered by a translation of the invertible active three-variable core.

The proof is a valid elementary split. On |L|>1/|t|, hub conditioning costs ≤1/2. On the complement, square-map change of variables in V followed by a cap-one one-sided inverse-square-root bound in H costs √(2/(|tL|)); its integral over the short L interval is 4√2/|t|. The bound is uniform in β. The statement **excludes** an additional dependent third projection 2εLP. The arbitrary joint planar law here does not contradict the old three-dimensional dependent-shell counterexample, because the independent hub is an essential extra hypothesis.

Cite `CaseQFORMBetaHub2026`.

### Avoid false stronger-result credit

The newly added exact-rank-three affine note gives 51(n−2)/σ. It is weaker than the existing arbitrary-rank 2√(6πn)/σ theorem and should not be presented as an improved upper bound. Its physical-triple proof can still be a useful alternative argument.

The new curved dyadic tube note proves an independent-axis O(ar²) bound and a physical-triple extension; it explicitly leaves the diffuse rotated-product version unproved. It also gives a genuine counterexample to extending the same ar² rate uniformly under an affine shear dL (a logarithmic factor appears). This refutes an auxiliary estimate, not QFORM itself. These details can remain in the supplement.

## 3. The QFORM broad card: useful correction with exact scope

The card `qform_bounded_density_state_after_the_second_wave_2026_09_23.md` adds Proposition 5.5/5.6 results supported by the committed `single_hub_core/REPORT.md`.

For a hub whose conditional density is bounded by one and depends on the light inputs only through P, Proposition 5.5 has a maximal-density bound
1/2 + 2ρ* [1+log₊(cM*/ρ*)].
A bounded-support hypothesis on the physical coordinates that carry the partner gives logarithmic dependence on support length. Unit-window mixture laws U[0,1]*ν on those coordinates give the stated **13.9** bound for |λ|≥1, within the displayed single-hub form and absence of the excluded light diagonal terms. The proof's integration of min(ρ_{L,P}, c a√|t|) over p and then t is valid; the support condition is used in the separate tilt estimate. This does not cover every rough bounded density: a subunit comb does not inherit a unit-window representation or a uniform cap after conditioning.

The updated card corrects a claimed numerical leveling-off after a larger sample range. Ratios continue to increase in the tested N≤20 cases while absolute density estimates decrease. The source's sentence suggesting an “unbounded factor” is stronger than finite samples establish; do not adopt it as a theorem. Likewise, values obtained by putting a **measured** ρ* into a proved inequality remain partially numerical evaluations of that bound.

Cite `CaseQFORMHubPartner2026` if this case is used.

## 4. FEI: substantive previously omitted claims, new memory, and source mismatch

The changed broad read-k FEI card adds an evening paragraph explicitly headed “numerics and partial proofs, NO new theorem.” The separate new near-dictator card is a provisional summary of the mechanism used in an earlier theorem claim. The math-open-problems compare contains no new FEI paths. These are memory publication/continuation changes, not evidence that a new FEI theorem appeared after the old frozen mathematical source.

The underlying `proofnet24/P03-fei/continuations/2026-09-23-readk-dnf/paper/fei_readk_regular.tex` does contain substantial claims that the earlier Pseudo-Cognitive Dynamics research section did not summarize:

- read-k DNF/CNF: H≤min(2.89+9.9k,30+5.6 log₂k)I;
- regular/2-monotone functions, including LTFs **under the uniform measure**: H≤15.1I;
- read-k unions/intersections of regular functions: logarithmic dependence on k;
- strengthened **biased** FEI+ for **unweighted symmetric threshold gates** T_{t,r} under arbitrary product measures, with 760 bits as the displayed constant; O'Donnell–Tan composition then gives H≤760I for read-once formulas over these threshold gates (and XOR), with arbitrary fan-in and depth.

These should be described as source manuscript claims with complete written arguments, internally reviewed and not independently refereed by this update. I inspected the critical theorem statement, weak-form dependencies, near-dictator proof, and composition interface. I did not independently verify every lemma or novelty claim in the 30-page FEI paper.

The near-dictator split is precisely scoped: if every pivotal probability ρ_j≤0.9, J≥I/10 lets the weak inequality pay. If max ρ_j=1−ε>0.9, lattice anti-concentration forces the *other inputs of an unweighted threshold* to be nearly deterministic; the proof then controls second-order spectral mass family by family. This implication does not hold for general weighted LTFs: a heavy pivotal input can coexist with many random light inputs. Full FEI and biased FEI+ for general weighted LTFs stay **OPEN**.

The Lean source `lean/FEISubadd.lean` proves the scalar inequality for φ_s(x)=x ln(s/x):
φ_s((a+b)²)≤2φ_s(a²)+2φ_s(b²)+2a²+2b²,
under s>0, a²≤s, b²≤s. It is an algebraic analytic helper used in the near-dictator case, not a formalization of the full FEI theorem. Source inspection found the explicit assumptions and no sorry/admit. The current card reports successful Lean 4.33.1/Mathlib compilation and only standard axioms; this update did not replay the build.

**Source mismatch to preserve:** the broad card cites a Section 29 with further slice-regime constants and a proposed smaller bound. At the pinned math-open-problems head, the underlying REPORT ends at Section 28 and the committed paper does not contain those later Section 29 statements. Do not promote those card-only constants (7.04, 7.35, 15.6 bits) into paper theorem claims. The new near-dictator card also says its Lean compile was pending, while the later changed read-k card reports it succeeded: this is a concrete example of memory-version order mattering.

Cite `CaseFEIReadKManuscript2026`, `CaseFEIReadKReport2026`, `CaseFEISubadd2026`, and `CaseFEINearDictatorCard2026`.

## Recommended paper changes

1. Replace the QFORM subsection's vague O(√n) sentence with the exact arbitrary-symmetric-matrix, fixed-dimension bound and the symmetric-part qualification for a general real matrix.
2. Keep unrestricted dimension-free QFORM explicitly open. Add a compact paragraph on the shift-stable L² result and its unpaid parabola restriction; optionally pair it with the independent-hub theorem.
3. Add a source-qualified FEI paragraph describing the read-k and unweighted-threshold manuscript, preserving the distinction from full FEI and from biased weighted-LTF FEI+.
4. Use the revised cards as evidence of correction/version propagation, not as a new independent proof or controlled measurement of Math Brain efficacy.
5. Keep old catalogue rows frozen and preserve original snapshot provenance. The update adds a delta dossier; it does not silently relabel all 1,168 IDs at the new head.

No literature novelty claim was added in this focused review. QFORM's only bibliography diff corrects a title and adds the DOI for an already cited Friedland–Sodin source; it does not change the paper's mathematical comparison. Exact source and local hash records are in `source_manifest.json`.

