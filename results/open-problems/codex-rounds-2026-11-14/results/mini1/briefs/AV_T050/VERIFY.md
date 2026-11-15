# Verification of T050

Checked 14 November 2026. Verdict: **PARTIAL-CLAIMED**. The whole row is not claimed by these candidates. “Claimed” below records what a manuscript states; it does not certify its proof.

## Our statement

“For first-passage percolation on Z^d, d ≥ 2, with iid continuous edge weights satisfying E min(t_1, …, t_{2d})^d < ∞ (so that the shape theorem holds), the limit shape (the asymptotic shape of the ball of passage time t, scaled by t) is strictly convex.”

The usual nonnegative edge-weight convention is understood. The comparison concerns the undirected nearest-neighbor edge model, not directed last-passage percolation.

## Candidate 1: strict convexity

**OpenAI, “Strict convexity and differentiability of the planar exponential first-passage limit shape,” September 24, 2026.**

Opened the actual [main TeX file](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/main.tex), [introduction](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex), and [manuscript README](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/README.md). The introduction is saved locally as [convexity-introduction.tex](convexity-introduction.tex); its GitHub blob SHA is ea108cac0994372ba5887e93df5afb1379ff7b40. The root PDF is named main.pdf. Browser PDF retrieval failed on content type; quotations are from the primary TeX, not from a title or an abstract.

Exact main theorem, Theorem 1.1 (including original TeX notation):

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

The relevant additional theorem, Theorem 1.2, exactly:

```tex
\begin{theorem}[Differentiability for Gamma weights]
\label{thm:gamma-differentiability}
For independent Gamma edge weights with any fixed shape $\kappa>0$
and rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable at
every nonzero vector, and $\partial\Bcal$ is a $C^1$ curve.
\end{theorem}
```

Here the paper defines T(x,y) as the minimum sum of edge weights along undirected nearest-neighbor paths, μ as its deterministic time-constant norm, and B as {v : μ(v) ≤ 1}. Thus its unit ball is exactly the asymptotic passage-time ball in our row.

| Clause of our row | What the paper claims | Coverage |
| --- | --- | --- |
| First-passage percolation on Z^d | Undirected nearest-neighbor edge FPP on Z² | Same model at d = 2; no d ≥ 3 claim |
| iid edge weights | Independent weights with one fixed exponential rate, or one fixed Gamma shape and rate | Same independence and common-law requirement |
| Every continuous distribution | Exponential for strict convexity; Gamma for differentiability | Exponential is a special continuous law; arbitrary continuous laws are not covered |
| E[min(t₁,…,t₂d)^d] < ∞ | Exponential/Gamma laws have finite moments of every positive order | The special cases satisfy our assumption; the theorem does not quantify over all laws satisfying it |
| Limit shape | Unit ball of the time-constant norm | Same quantity |
| Strictly convex | Strict convexity and differentiability for exponential weights, all positive rates | Same strict-convexity strength in this special case, plus a separate regularity assertion |
| Gamma extension | Differentiability and C¹ boundary | Does not assert strict convexity for nonexponential Gamma laws |

The conclusion is exact strict convexity of the limiting body, not a finite-time bound, a curvature lower bound, or an explicit formula for the shape. Differentiability means that each boundary point has a unique support; strict convexity means that each supporting face has at most one point. The former does not imply the latter, so the Gamma extension cannot enlarge the strict-convexity verdict.

## Candidate 2: no bigeodesics

**OpenAI, “No bigeodesics in planar first-passage percolation,” September 24, 2026.**

Opened the actual [main TeX file](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/main.tex), [introduction](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex), and [README](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/README.md). Exact source is saved in [bigeodesics-introduction.tex](bigeodesics-introduction.tex), blob SHA 731be208d4c934c87c6d2cd59022942cb863e9f0. Theorem 1.1 says exactly:

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

The preceding model definition is iid nonnegative weights of common Borel law G on unoriented nearest-neighbor edges of Z². “No atoms” includes singular continuous laws; it is not restricted to laws having a density. Its minimum-of-four second-moment hypothesis is exactly our moment assumption at d = 2, and does not require a finite second moment of an individual edge.

The model and planar moment class therefore agree with our row, but the quantity and conclusion differ: this rules out a doubly infinite path all of whose finite pieces minimize passage time. It does not state strict convexity of the limit shape. The introduction explicitly says that no differentiability, strict convexity, or curvature of the shape is assumed; it does not give a theorem deriving strict convexity from its conclusion. There is also no higher-dimensional assertion. **NOT-THIS for the requested conclusion**, despite its relevance to planar FPP.

## Candidate 3: univalent functions

**OpenAI, “A strict inverse-first-power bound for univalent functions,” September 24, 2026.**

Opened the actual [main TeX file](https://github.com/openai/math/blob/main/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/main.tex), [introduction](https://github.com/openai/math/blob/main/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/00-introduction.tex), and [README](https://github.com/openai/math/blob/main/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/README.md). The introduction is saved in [univalent-introduction.tex](univalent-introduction.tex), blob SHA 15cbd452de44374c2455d48200883208b9c5c208. Its Theorem 1.1 says exactly:

```tex
\begin{theorem}[Uniform inverse-first-power bound]\label{thm:main}
There exist constants \(0<\varepsilon<1/4\) and \(C<\infty\) such that
\begin{equation}\label{eq:uniform}
 M_{-1}[f'](r)\le C(1-r)^{-1/4+\varepsilon}
 \qquad\text{for every }f\in\SSS\text{ and every }1/2\le r<1.
\end{equation}
Consequently \(B_b(-1)<1/4\), and Kraetzer's conjectured identity
\eqref{eq:kraetzer} is false.
\end{theorem}
```

The class S consists of injective holomorphic maps from the complex unit disk to C with f(0) = 0 and f′(0) = 1. The quantity M_p is the normalized circular mean of |f′|^p; B_b(p) is the supremum of its limiting logarithmic growth exponent over bounded-image maps in S. The theorem is a uniform integral-means upper bound, with a strict improvement of its exponent.

There is no random edge model, no lattice dimension, no passage-time moment condition and no FPP limit shape. “Strict” refers to the integral-means exponent. **NOT-THIS**.

## Follow-ups and formalization

### Primary repository evidence opened

- [Repository README](https://github.com/openai/math/blob/main/README.md): the collection is described as model-produced research material at differing verification stages, with possible issues in unformalized results.
- [history.md](https://github.com/openai/math/blob/main/history.md), saved as [history.md](history.md): no entry lists a correction or withdrawal of these three manuscripts. The dated manuscript READMEs have no version-repair notice. This is a check of listed history, not a claim that every repository change was audited.
- [lean/docs/212.md](https://github.com/openai/math/blob/main/lean/docs/212.md), saved as [lean-docs-212.md](lean-docs-212.md): explicitly says that strict convexity is outside the selected differentiability statements. Its paper list links only the strict-convexity/differentiability paper, not the no-bigeodesics paper.
- [PlanarFirstPassage.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PlanarFirstPassage.lean) and [GammaPassage.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GammaPassage.lean), both saved here: the former specifies the rate-one exponential environment and differentiability/C¹ boundary/unique support; the latter quantifies over every positive Gamma shape and rate. Neither states strict convexity or absence of bigeodesics. Rate scaling covers other exponential rates for differentiability.
- The corresponding [PlanarFirstPassage.json](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PlanarFirstPassage.json) and [GammaPassage.json](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GammaPassage.json) point to separate solution modules, with only propext, Quot.sound, and Classical.choice permitted. The challenge files' “sorry” placeholders are not evidence that the separate solution files are missing proofs. The configured formalizations were not rebuilt in this verification.
- [lean/README.md](https://github.com/openai/math/blob/main/lean/README.md), [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md), and [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml) were opened. The manifest is saved as [lean-formalization.yaml](lean-formalization.yaml).
- For the unrelated third candidate, [lean/docs/072.md](https://github.com/openai/math/blob/main/lean/docs/072.md) and [StrictMeans.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/StrictMeans.lean) were opened and saved. They do specify the strict inverse-first-power estimate and B_b(−1) < 1/4. That formalization has no bearing on T050.

### External reports opened

- [MathVet fidelity table](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv), read through the GitHub connector at the linked commit. Family 212 has partial coverage and reports successful sandboxed Comparator checks of GammaPassage and PlanarFirstPassage. Its note identifies both strict convexity and no-bigeodesics as absent from the challenge statements. Saved relevant entries: [mathvet-excerpts.txt](mathvet-excerpts.txt).
- [Carlos Toledo's cert-machine statement audit](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json), read at the linked commit. Family 212 is classified NARROWER — UNLINKED, distinguishing stated differentiability from the omitted convexity and bigeodesic conclusions. Relevant primary records are saved in [cert-machine-excerpts.json](cert-machine-excerpts.json). This is a formal-statement scope audit, not a referee report on the strict-convexity proof.
- [Plectis Atlas's paper transcription](https://wcook04.github.io/plectis-atlas/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026.html) and [family 212 page](https://wcook04.github.io/plectis-atlas/families/212.html) were opened as discovery aids. Atlas identifies its text as a conversion of OpenAI's TeX and directs readers to the original paper; the exact quotations above were checked in the original TeX.
- Two Orply expositions were opened: [the exponential-shape exposition](https://orply.com/articles/perplexity/212-2-strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-4c374966) and [the no-bigeodesics exposition](https://orply.com/articles/perplexity/212-1-no-bigeodesics-in-planar-first-passage-percolation-23ca1170). They explain the claimed results; their existence does not establish refereeing or independent verification.
- A later research paper was located and opened at both its arXiv abstract and [full HTML text](https://arxiv.org/html/2610.42124v1): **Scott Armstrong and Ahmed Bou-Rabee, “Fluctuation bounds for rotationally invariant first-passage percolation,” arXiv:2610.42124v1, submitted October 30, 2026**. Its introduction, immediately after Theorem 1.1, acknowledges the announcement of planar exponential strict convexity and differentiability; reference [Ope26] identifies the September 24 OpenAI preprint. Its own model is rotationally invariant continuum FPP on R^d and its result concerns fluctuations. This is evidence of subsequent citation by named authors, not a proof audit or an extension of the lattice strict-convexity theorem.

### Search outcome and limits

Used web search for each exact title, title plus arXiv, and combinations with error, refutation, referee, expert, and review. Exact-title searches restricted to arxiv.org did not locate arXiv versions of the three candidates. The GitHub issue search `repo:openai/math "first-passage"` returned no results.

No opened source supplied a referee acceptance or a refutation of the strict-convexity theorem. The later Armstrong–Bou-Rabee paper acknowledges its announcement without assessing its proof; the other concrete follow-up evidence is the narrower Lean scope and the two outside formal-statement audits. Search silence is not proof that no later commentary exists.

## Recommended replacement for “Where it stands”

The general strict-convexity problem remains open: OpenAI's unrefereed preprint “Strict convexity and differentiability of the planar exponential first-passage limit shape” (September 24, 2026) claims strict convexity for iid exponential weights on Z². It does not cover arbitrary continuous laws or dimensions d ≥ 3, and its Gamma extension claims differentiability only. The repository's selected Lean formalizations cover differentiability and explicitly omit strict convexity.

## Spot check

**Target:** the central contraction proposition, “Contraction in the original road class” (source label `improvement:contraction-proposition`, Section 15.7). This is the decisive intermediate assertion in Part II: under a hypothetical flat face it gives fixed D and ρ < 1 with b(Dn) ≤ ρ b(n). Together with the positive lower bound on b, it supplies the strict-convexity contradiction. Opened its full proof in [the primary improvement section](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/improvement.tex), saved as [strict-improvement.tex](strict-improvement.tex), and its final use in [strict-conclusion.tex](strict-conclusion.tex). Also read its finite-range replacement lemma and the definitions of its cost estimates in that same section.

This check concerns cost bookkeeping and scale passage. It does not establish the earlier constructions summarized as inputs (G) and (L).

1. **Clipping to actual cost.** Put p = P(Z₀ > M), W₀ = clip_M(Z₀), and A_* = 2G_*C₀ + H_*C_V + 2K_δ. The replacement lemma gives
   `E Z₀(out) ≤ E W₀ + H_*Mp + 2C₀(L_*+1)δ + A_*p`.
   The matched cap supplies E W₀ ≤ C₁s + η and Mp ≤ η; the first-moment estimate supplies p ≤ C₀/M₀. The error is therefore at most
   `(H_*+1)η + 2C₀(L_*+1)δ + A_*C₀/M₀`.
   The stated choices make each term at most ε/3. This gives C₁s + ε. It bounds actual replacement pieces rather than treating clipped costs as physical path costs.

2. **Independence and signs in the replacement estimate.** An uncovered positive tail is charged to one of at most 2G_* remote flags, or one of at most 2(L_*+1) failed transition tests. Each possible witness is indexed more than R away and hence independent of Zᵢ under the hypotheses; the estimates precede selection of the cluster endpoints. For spare costs, the coverage indicator Oᵢ is bounded by a sum of at most H_* primary flags. Independence of the entire spare and primary fields then gives E[VᵢOᵢ] ≤ H_*C_Vp, without assuming that success itself is independent of Vᵢ. The retained-cost inequality
   `(1−Oᵢ)Zᵢ ≤ clip_M(Zᵢ) + MOᵢ + Zᵢ⁺ 1{Zᵢ>M}(1−Oᵢ)`
   also holds when Zᵢ < −M: on a covered slot the right side is nonnegative, and on an uncovered slot clipping can only increase a negative cost. These checks reproduce the displayed error budget from the stated field assumptions.

3. **Scale factor and choice order.** Costs remain in original lattice units. D old slots form one new period, giving D(C₁s + ε)β; the proof retains that factor D. It chooses D from asserted uniform structural bounds before choosing s and ε, then makes DC₁s < 1/4 and Dε < 1/4. Thus ρ < 1/2 if those uniform bounds and the claimed locality/tracking closure hold. Integer D preserves the mesh divisibility.

4. **Infimum and iteration.** The proof chooses β ≤ b(n)+t in a class having a common upper prefactor and a threshold asserted uniform over that class. Applying the construction and sending t down to zero does not require a minimizing road. Iteration gives c₀ ≤ b(D^k n₀) ≤ ρ^k b(n₀), contradictory for fixed finite b(n₀).

No algebraic error was isolated in these steps. The substantive inputs still unchecked here are the earlier local gauges, matched-cap crossing estimates, and physical path/locality constructions, including their parameter uniformity. This spot check does not settle the correctness of the strict-convexity proof.


