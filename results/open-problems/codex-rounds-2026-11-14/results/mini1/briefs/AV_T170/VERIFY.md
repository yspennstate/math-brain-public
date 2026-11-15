# T170: Eden non-ball conjecture

Checked 14 November 2026. Verdict: NOT-THIS. None of the three candidate preprints claims the non-ball conclusion, even just for dimension two. This is a comparison of statements, not a judgment that any proof is correct.

## Sources and exact theorem statements

All three manuscripts name **OpenAI** as author. The paper sources were opened through the read-only GitHub connector, including each build/main.tex and introduction; exact local copies are in sources/. The repository main branch resolved to commit `4eaee87548250b2682affda7d05d947c05554bae`; the links below pin that revision. TeX blocks below reproduce the theorem environments verbatim, including labels and macro names; their meanings are given immediately afterward.

### 1. Strict convexity and differentiability of the planar exponential first-passage limit shape — September 24, 2026

Opened [paper source](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/main.tex), [introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex), and the manuscript README. The PDF linked by that README is [main.pdf](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf).

Theorem 1.1:

```tex
\begin{theorem}[The exponential limit shape]
\label{thm:exponential-shape}
For independent exponential edge weights of any rate $\lambda>0$,
the norm $\mu$ is Fr\'echet differentiable on $\R^2\setminus\{0\}$,
and its unit ball is strictly convex. In particular,
\[
 \mu((1-t)x+ty)<1
 \quad\text{if }x,y\in\partial\Bcal,\ x\ne y,\ 0<t<1,
\]
and $\partial\Bcal$ is a $C^1$ curve with a unique supporting line
at every point.
\end{theorem}
```

Theorem 1.2, the other main statement:

```tex
\begin{theorem}[Differentiability for Gamma weights]
\label{thm:gamma-differentiability}
For independent Gamma edge weights with any fixed shape $\kappa>0$
and rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable at
every nonzero vector, and $\partial\Bcal$ is a $C^1$ curve.
\end{theorem}
```

Here the source defines μ by the almost-sure passage-time limit and defines Bcal = {v: μ(v) ≤ 1}. The graph is the unoriented nearest-neighbor lattice Z². The author does not identify this ball with, or distinguish it from, a Euclidean disk.

### 2. Symplectic Ball Packings in Higher Dimensions — September 23, 2026

Opened [paper source](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/build/main.tex), [introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/build/sections/introduction.tex), [completion](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/build/sections/conclusion.tex), and the manuscript README. The PDF is [paper.pdf](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/paper.pdf).

Theorem 1.1:

```tex
\begin{theorem}\label{intro:main}
Let \(n\ge3\) and \(k\ge1\) be integers. For positive real numbers
\(R,R_1,\ldots,R_k\), there exists a symplectic embedding
\[
 \bigsqcup_{i=1}^k B^{2n}(R_i)
 \hookrightarrow \Int B^{2n}(R)
\]
if and only if
\begin{equation}\label{intro:inequalities}
 \sum_{i=1}^k R_i^n<R^n,
 \qquad
 R_i+R_j<R\quad (1\le i<j\le k).
\end{equation}
\end{theorem}
```

The definition immediately preceding it is B^{2n}(R) = {z ∈ C^n: πΣ|z_j|² ≤ R}; R is capacity, and the Euclidean radius is √(R/π). A closed-source embedding must extend to an open neighborhood, with pairwise disjoint compact images inside the open target.

### 3. No bigeodesics in planar first-passage percolation — September 24, 2026

Opened [paper source](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/main.tex), [introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex), and the manuscript README. The PDF is [main.pdf](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf).

Theorem 1.1:

```tex
\begin{theorem}\label{thm:main}
Suppose that \(G\) has no atoms and that, for independent
\(X_1,X_2,X_3,X_4\) with law \(G\),
\begin{equation}\label{eq:minimum-moment}
 \EE\!\left[\min\{X_1,X_2,X_3,X_4\}^{\,2}\right]<\infty.
\end{equation}
Then, with probability one, there is no sequence
\((v_i)_{i\in\Z}\) of pairwise distinct vertices with consecutive
vertices adjacent and
\[
 \sum_{k=i}^{j-1}t_{\{v_k,v_{k+1}\}}=T(v_i,v_j)
 \qquad\text{for every }i<j.
\]
\end{theorem}
```

The preceding definitions fix the unoriented nearest-neighbor edges of Z², iid weights with Borel law G on [0,∞), and T as the infimum of finite-walk passage times. EE denotes expectation. The theorem excludes every doubly infinite minimizing path on a single event of probability one, including paths whose directions depend on the environment.

## Comparison with our statement, clause by clause

Our target is: for iid mean-one exponential weights on the edges of Z^d, the deterministic shape B of t⁻¹ times the reached set is not a Euclidean ball, for **every integer d ≥ 2**. Equivalently, in each such dimension its time-constant norm is not c times the Euclidean norm for any constant c > 0.

| Clause in our row | Planar strict-convexity paper | Symplectic packing paper | No-bigeodesics paper |
| --- | --- | --- | --- |
| First-passage percolation on unoriented nearest-neighbor edges | Same model in Z² | No random metric, growth process, or lattice | Same model in Z² |
| Independent exponential weights of mean 1 | Included by rate λ = 1; other rates only rescale the shape | No edge-weight law | Included: exponential weights are nonatomic and meet the moment assumption |
| Dimension: every d ≥ 2 | Only d = 2; no statement for d = 3,…,22 or higher | Real symplectic dimension 2n ≥ 6, unrelated to lattice d | Only d = 2 |
| Quantity: deterministic shape B | Exactly the same limit-shape object in dimension two | Embeddability of already specified standard balls | Random infinite minimizing paths, not B's rotational symmetry |
| Conclusion: B is not Euclidean | Strict convexity and C¹ boundary only | Exact packing criterion, with strict capacity inequalities | Almost-sure nonexistence of bigeodesics |
| A new dimensional case of our conclusion? | None | None | None |

A Euclidean disk has a strictly convex C¹ boundary, a differentiable norm away from the origin, and a unique supporting line at every boundary point. Thus every geometric conclusion in the first theorem is compatible with the excluded possibility in our problem; this is not a weaker estimate for non-ballness or a solution of its planar special case. The strict inequality in that theorem tests convex combinations of different boundary points, not whether equal-length directions have different time constants.

For the third paper, if X_i are mean-one exponentials then their minimum is exponential with rate 4, so its second moment is 2/4² = 1/8 < ∞. Its model therefore includes our planar model without an extra hypothesis, but its conclusion supplies no inequality between directional time constants and no implication from nonexistence of bigeodesics to non-ballness. The second paper's use of “ball” is a match of words only.

## Follow-ups and formalization

The search covered the exact titles, variants with “OpenAI”, “arxiv”, “error”, “gap”, “review”, “correction”, and “refutation”, and the Eden conjecture with 2026. A search returning nothing relevant is not evidence that no unpublished review exists. No direct arXiv version of any of these three OpenAI manuscripts, nor a targeted refutation or referee report establishing their correctness, was located in the material opened.

1. **Later research citation to the first paper.** Opened the [arXiv abstract](https://arxiv.org/abs/2610.42124) and [full HTML](https://arxiv.org/html/2610.42124v1) of *Fluctuation bounds for rotationally invariant first-passage percolation*, **Scott Armstrong and Ahmed Bou-Rabee**, submitted 30 October 2026. Its introduction and reference [Ope26] acknowledge the planar regularity announcement; they do not certify it or assert Eden non-ballness. Its own theorem treats rotationally invariant continuum FPP on R^d, whose rotational invariance makes its limit shape a ball, and studies passage-time fluctuations. It is not an arXiv version of the OpenAI paper.

2. **Later symplectic work.** Opened the original 45-page [PDF](https://aixiv.online/pdf/2611.00466v1), *Explicit Hamiltonian ball packings in every dimension*, **Liang Song**, aiXiv identifier 2611.00466v1 (November 2026; aiXiv is a different service from arXiv). The abstract, introduction §1.3, and [Ope26] explicitly build on the symplectic manuscript. It concerns Hamiltonian packing constructions, not Eden growth; its disclosure says the mathematics, formalization and text were produced by AI systems. Its existence is not independent expert validation.

3. **Expositions.** Opened [Closed Form, family 212](https://closedform.nishachay.tech/e/openai-math-2026-212/) and [Latent Seminar, family 343](https://lowrank.github.io/latent-seminar/OpenAI-Math/343-symplectic-ball-packings), the latter dated 7 October 2026. These restate the relevant claims and distinguish them from full independent verification; Closed Form is explicitly an AI explanation. They do not claim the Eden non-ball result. They are recorded as follow-up pages, not as mathematical evidence for proof correctness.

4. **Public audit.** Opened [Carlos Toledo, OpenAI's math release: what it claims beyond what it checks](https://carlostoledo.co/reports/openai-math.html), an audit dated 10 October 2026 pinned to fd4aeeb2. Its family-212 scope comparison lists strict convexity and the no-bigeodesics claim among conclusions beyond the checked statements. This is a statement-scope audit, not a refutation of either manuscript. Our own inspection of the repository's scope note agrees about the restricted formal scope.

5. **Lean material actually inspected.** Opened [lean/README.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/README.md), [formalization.yaml](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/formalization.yaml), [docs/212.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/212.md), [PlanarFirstPassage.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarFirstPassage.lean), [GammaPassage.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GammaPassage.lean), [PlanarFirstPassage.json](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarFirstPassage.json), and the actual solution file [BoundaryCurve.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/FirstPassage/BoundaryCurve.lean). The scope note describes differentiability for all positive Gamma parameters and explicitly excludes strict convexity. The exponential comparator is for mean-one edges and its solution theorem asserts existence of the actual time-constant norm, differentiability and C¹ boundary/support properties; it contains no non-Euclidean conclusion. Comparator files contain deliberate `sorry` challenge placeholders; this alone is not a defect of the corresponding solution. No kernel build or dependency audit was run, and the Gamma solution dependency chain was not independently checked. No formalization of non-ballness or of the no-bigeodesics theorem was identified in these records.

   Also opened [docs/343.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/343.md) and [BallPacking.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BallPacking.lean): their claimed formal scope is the symplectic capacity criterion, not random growth. An initial search hit led to docs/087.md; opening it showed that it concerns Mahler and polar products, so it was excluded as irrelevant.

6. **Revision status.** Opened the repository [README](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/README.md), all three manuscript READMEs and [history.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/history.md). None of those three manuscript READMEs carries a withdrawal or correction notice. The history records other withdrawals and revisions, but no entry naming these candidates. This does not establish that their proofs are valid.

## Existing dimensional result

Opened the original arXiv pages for *Dimension improvement in Dhar's refutation of the Eden conjecture*, **Quentin Bertrand and Jules Pertinand**, [arXiv:1705.08143v2](https://arxiv.org/abs/1705.08143), revised 31 January 2018, and *Construction of a short path in high dimensional First Passage Percolation*, **Olivier Couronné, Nathanaël Enriquez, Lucas Gerin**, [arXiv:1008.5069v2](https://arxiv.org/abs/1008.5069), revised 23 February 2011. Bertrand–Pertinand explicitly state a non-ball result for dimension greater than 22. The older paper's abstract says “larger than 35”, while our supplied note says d ≥ 35; that intermediate endpoint was not rederived and is unnecessary for the current frontier. The older Kesten threshold and Dhar asymptotic in the supplied note were not independently rechecked here.

## Recommended “where it stands” sentence

Open in dimensions 2 through 22; Bertrand and Pertinand proved non-ballness for d > 22. OpenAI's unrefereed preprint *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026) claims planar strict convexity and a C¹ boundary, which are compatible with a Euclidean disk and do not settle this question. Neither of the other two candidates claims the missing non-ball result.

## Spot check

After saving REPORT.md, checked the proposition **“Contraction in the original road class”**, source label `improvement:contraction-proposition`, in [strict/improvement.tex](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/improvement.tex). It is the decisive scale-improvement step: a fixed D and ρ < 1 must give b(Dn) ≤ ρ b(n) in the same road class. Read its proof, the whole replacement lemma and endpoint/locality accounting immediately before it, the road definitions and random-cut identity in [foundations.tex](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex), and the final iteration in [conclusion.tex](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/conclusion.tex). These source snapshots are saved locally.

The following checks are conditional on the earlier gauge and link inputs (G) and (L), and on their stated uniformity; they do not verify those inputs.

- Recomputed the replacement error. With p = P(Z₀ > M), the displayed estimate is E Z₀(out) ≤ E clip_M(Z₀) + H Mp + C₀[2Gp + 2(L+1)δ] + (H C_V + 2Kδ)p. Using the matched-cap bounds and A = 2G C₀ + H C_V + 2Kδ, this becomes at most C₁s + (H+1)η + 2C₀(L+1)δ + Ap. The choices in the proposition bound each of the last three terms by ε/3, including Ap ≤ A C₀/M₀ ≤ ε/3. Thus its (C₁s+ε)β estimate has the stated sign and factors.

- Checked the rare-event accounting used in that bound. With B = R+1, G = 4B and L = 8B, a replaced interval has at most L+2B+1 = 10B+1 = H slots. The finite cluster tests look only within 13B slots. For an uncovered flag in a long cluster, the first flag farther than R has distance at most R+G, giving at most 2G deterministic witnesses; for a short rejected cluster, each possible failed endpoint test has index farther than R. Thus the independence being used is from a deterministic remote variable before selecting an extreme, rather than independence conditioned on a selected cluster. Bounding coverage by nearby primary flags also justifies the spare-cost estimate despite possible dependence of transition success on the spare field.

- Rechecked scale and quantifiers. Dividing old positions by D turns the mesh 1/n into 1/(Dn), tracking error C_tr s into C_tr s/D ≤ s/1000, and dependence radius R_out into R_out/D ≤ 10. D old periods have centered physical cost using (Dn)h(A), exactly the new Q_(Dn) convention, so the cost bound is multiplied by D; it is not divided by D. Uniform thresholds over near-minimizing input roads are needed to pass β ↓ b(n), and the proof explicitly invokes that uniformity. Its choices yield ρ = D(C₁s+ε) < 1/2. Fixed rational denominators remain admissible under multiplication by D.

These calculations reveal no error in this final contraction deduction **assuming** the earlier uniform gauge, link, support and coupling assertions. The important remaining burden is precisely those inputs: in particular the fixed support bounds independent of small s, cap tolerances and the chosen input rule, and the matched-cap link estimate. They were not established by this spot check, and the manuscript's proof has not been certified. Even a valid contraction proves absence of a flat face, which remains compatible with a Euclidean disk and does not change the T170 verdict.
