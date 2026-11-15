# Verification of T050

Literature check refreshed 15 November 2026. Verdict for T050: **PARTIAL-CLAIMED**. The whole row is not claimed by these candidates. “Claimed” below records what a manuscript states; it does not certify its proof.

The earlier verification and rounds 3–4 are preserved below with their historical source records. Round 5 reopened all three primary theorem sources and audited the additional-anchor comparison network; its spot check is appended below, and PROOF.md gives the detailed argument. REPORT.md uses the continuation instructions’ PROVED label for this conditional network estimate alone; the literature verdict remains PARTIAL-CLAIMED.

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

The general strict-convexity problem is not settled by these papers: OpenAI's unrefereed preprint “Strict convexity and differentiability of the planar exponential first-passage limit shape” (September 24, 2026) claims strict convexity for iid exponential weights on Z². It does not cover arbitrary continuous laws or dimensions d ≥ 3, and its Gamma extension claims differentiability only. The repository's selected Lean formalizations cover differentiability and explicitly omit strict convexity.

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

### Continuation, 15 November 2026: the abstract local-potential lemma

The scope verdict was independently re-derived from the current primary introduction. If `tau_e^(lambda)=tau_e^(1)/lambda`, then `T_lambda=T_1/lambda`, `mu_lambda=mu_1/lambda`, and `B_lambda=lambda B_1`; dilation preserves strict convexity. Also `min(tau_1,...,tau_4)` has exponential rate `4lambda`, with second moment `2/(4lambda)^2=1/(8lambda^2)`. Thus all positive exponential rates really satisfy our planar moment condition, while varying the rate supplies neither other continuous distribution families nor higher dimensions. Differentiability in the Gamma theorem is still a different assertion from strict convexity.

**Selected next check:** `found:lem-finite-cell`, “Local increments admit a local potential”, in the current [foundations section](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex), saved as [strict-foundations-current.tex](strict-foundations-current.tex). This is a component of input (G), which the earlier contraction check took as an assumption. The current foundations file is byte-identical to the earlier saved source. The three current theorem quotations, scope note and history also agree with their earlier source files, apart from a terminal blank line in the connector responses; [current-source-audit.json](current-source-audit.json) records the fresh responses and URLs.

[round3-finite-cell-proof.md](round3-finite-cell-proof.md) verifies this abstract lemma under its stated independent-cell hypotheses using the manuscript's gauge construction. It supplies the explicit bound

`C_H = 2 + 2 N_H B_H 2^m`,

where `R=8H+20`, `m=(2H+1)^2`, `N_H=(2R+1)^2 2^((4H+1)^2)` and `B_H=4R+4H+11`. The boundary detour has at most `4R+4H+10` steps; one additional same-index label change accounts for the last 1. The proof writes out the finite conditional-expectation identities, the cutoff errors and the recovery of a neighboring increment, without an L2 or infinite-series assumption. Constants do not depend on the number of labels or the number of variables inside a cell.

The accompanying [check_local_potential.py](check_local_potential.py), run with `OMP_NUM_THREADS=1 nice -n 15 python3 check_local_potential.py`, confirms the detour length by breadth-first search for H=2,3,5,10,20 and checks the projection identities by exact rational arithmetic on a nonuniform four-cell Bernoulli product. All checks passed, including 2,800 support-cancellation checks. At H=2, two computations agree on `C_2=2+1737254*2^106=140942788854329116202736232342545760258`. The run took 4.279 seconds and peaked at 15.09 MiB RSS. These finite checks accompany the general proof; they do not replace it.

Attempts to find a missed case included same-index label changes, nonlocal individual potentials, common random additive offsets, nonzero label means, arbitrary cell contents, boundary corners, and the sign of the centered error. None breaks the stated abstract lemma. In particular, the result bounds increments of `g-V`; it does not claim an absolute L1 bound on `g-V` itself.

This verifies one auxiliary lemma, not the FPP application or the full proof. The comparison network, the common-world gauge lemma, matched-cap links and road-class closure remain unchecked here. The next check should be `found:lem-common-gauge` and the use of one fixed baseline in several exterior completions.

### Follow-up search in this continuation

Within the initial five-minute check, reopened [repository history](https://github.com/openai/math/blob/main/history.md), the [manuscript README](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/README.md), [lean/docs/212.md](https://github.com/openai/math/blob/main/lean/docs/212.md), and both the [arXiv abstract](https://arxiv.org/abs/2610.42124) and [HTML](https://arxiv.org/html/2610.42124v1) of Scott Armstrong and Ahmed Bou-Rabee, *Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124v1. The history and README contain no listed repair or withdrawal for this theorem. The scope note still excludes strict convexity. The later paper remains a citation of the announcement, not a verification or a solution of the general lattice problem.

Web searches used the exact strict-convexity title, error/correction/refutation/November variants, arXiv-restricted variants, and general first-passage strict-convexity queries for November 2026. Read-only GitHub issue search `repo:openai/math "first-passage"` returned no issues. No new solution, named proof assessment or error report was located in this bounded check. No claim is made that all later commentary has been exhausted. The other external audits and expositions in the earlier follow-up section are inherited records from the previous worker, not freshly rebuilt checks.




### Round 4, 15 November 2026: common incoming-road gauge

The next step named by round 3 was `found:lem-common-gauge`, especially the insertion of a fixed privately completed baseline into different worlds. Reopened the current primary foundations source, whose SHA256 remains `2b4099ac2502613172cba97cd1cd8c842f7ffab33678fa9fee7fa1e013792ba4`. Its exact lemma statement is:

```tex
\begin{lemma}[A gauge from the preserved incoming road]
\label{found:lem-common-gauge}
Fix deterministic tubes and a baseline road contained in one of them.
Write $\eta=(\eta_0,\eta_{\rm other})$ for all preserved tube weights,
where $\eta_0$ consists exactly of the weights in the baseline's own
tube and $\eta_{\rm other}$ contains the remaining preserved edges.
Let $\xi$ contain the baseline's private road seeds and a private
completion of the entire complement of its own tube.  Construct the
baseline once, using the actual weights in its own tube and these
private inputs everywhere else.  The resulting road is a function of
$(\eta_0,\xi)$ alone.

In each world $j$, retain all prescribed tube weights and use an iid
completion $\zeta^j$ elsewhere.  For every $j$, the private input
$\xi$ is independent of the joint tuple $(\eta,\zeta^j)$; different
worlds may share coordinates with one another.  Assume that every world
has the correct product weight law, uses the same measurable
calibration map, and supplies the local comparison network above with
period bound $\beta$.  Assume also that the shared baseline is
admissible in every world and has expected defect at most $\beta$ on
each marked period there.  The latter condition follows from the
random-cut period identity when the shared baseline rule has period
excess at most $\beta$.

Let $g_x^j$ be the gauge given by \eqref{found:eq-gauge-formula} at a
marked baseline anchor.  There is a local function $g_x^{\rm in}$ of
$(\eta_0,\xi)$ alone such that, in every world,
\begin{equation}
 \E |g_x^j-g_x^{\rm in}|\leq C\beta.
                                                        \label{found:eq-common-gauge}
\end{equation}
Its support radius and the constant $C$ are uniform in the number of
worlds.  After interpolation along any bounded baseline interval,
the same assertion holds with an expected supremum bound of order
$\beta$.  No identification of the calibrations in different worlds
is asserted.  In particular, incoming gauges for disjoint baseline
tubes with independent private completions and seeds are independent.
\end{lemma}
```

[round4-common-gauge-proof.md](round4-common-gauge-proof.md) supplies a detailed conditional proof and checks the private-completion insertion described in [strict-improvement.tex](strict-improvement.tex), lines 108–176. It first independently re-derives round 3's finite-cell projection bound and coefficient, which hold. It then verifies five parts of the new step: a signed network detour avoiding every projected cell set; common conditional expectations of the preserved baseline cost; equality of random-anchor means; admissibility and period defects of the inserted baseline; and interpolation and independence of disjoint incoming gauges.

With network comparison error at most `K beta`, the explicit anchor error bound is

`C_common beta`, where `C_common=N 2^m (L+JK)`,

`R=8H+20`, `m=(2H+1)^2`, `N=(2R+1)^2 2^((4H+1)^2)`,

`L=2R+4H+22`, `J=L+4R+4H+11`.

For H=2 this is `5329(102+265K)2^106 beta`. A prescribed interval meeting p periods has expected supremum discrepancy at most `(p+1)C_common beta`. These constants are independent of the number of worlds, labels and microscopic scale once H and K are fixed. The comparison-network hypothesis remains an input, so this is not a check of all hypotheses of the strict-convexity contraction.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_common_gauge.py`. All checks passed in 0.071 seconds, with peak RSS 15.70 MiB and inherited nice 20. A different tensor-integration implementation reproduced the earlier projection identities and constant. The script exhaustively checks the new detours at H=2,3,5 for both baseline directions and checks exact conditional projections in three worlds with shared exterior coordinates. The toy random-anchor means agree at -1/135; deliberate exterior dependence yields unequal projections with L1 distance 40/81, confirming that the own-input restriction matters. The distance and rational-number outputs are also re-derived algebraically in round4-common-gauge-proof.md.

The proof requires the private collections to be jointly independent of both actual tube weights and world complements, and requires the baseline tube to contain every traveled edge and preserve the baseline period shift. The manuscript's deterministic straight tubes and independently chosen baseline arrays meet these particular restrictions as stated. Uniform local-comparison estimates for all inserted baseline labels, and the downstream link/phase/road-closure arguments, remain unchecked. No counterexample to the conditional common-gauge lemma was isolated; this spot check does not certify strict convexity.

#### Update check opened in this round

The initial bounded web search found no new settlement, withdrawal, substantive error report or referee assessment. Opened all three primary introductions through the GitHub read-only connector, the strict-convexity README, the current foundations, [repository history](https://github.com/openai/math/blob/main/history.md), [Lean scope 212](https://github.com/openai/math/blob/main/lean/docs/212.md), and the [PlanarFirstPassage](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PlanarFirstPassage.lean) and [GammaPassage](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GammaPassage.lean) challenge statements. The theorem environments and those challenge files match the saved earlier evidence; machine-readable reopened contents are in [reopened-sources.json](reopened-sources.json). The challenges still omit strict convexity; no Lean build was run.

Also opened the [arXiv abstract](https://arxiv.org/abs/2610.42124) and [full HTML](https://arxiv.org/html/2610.42124v1) of Scott Armstrong and Ahmed Bou-Rabee, *Fluctuation bounds for rotationally invariant first-passage percolation*, submitted October 30, 2026. Its introduction still describes planar exponential strict convexity as an announcement; its own continuum fluctuation theorem does not settle T050. Earlier external scope audits and expositions listed above are retained as earlier-session evidence, not represented as new discoveries in this round. The recommended three-sentence replacement status above remains unchanged.


### Round 5, 15 November 2026: local comparison network and extra anchors

Literature result remains **PARTIAL-CLAIMED**. In the bounded initial update search no later resolution, refutation, or substantive specialist assessment was located. This is a search outcome, not a universal absence claim. The recommended three-sentence replacement above remains unchanged.

Reopened primary sources in this round:

- OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape*, September 24, 2026: [main TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/main.tex), [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex), [foundations](https://raw.githubusercontent.com/openai/math/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex), and [improvement](https://raw.githubusercontent.com/openai/math/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/improvement.tex). Fresh local copies are [introduction](fresh-convexity-introduction.tex), [foundations](fresh-strict-foundations.tex), and [improvement](fresh-strict-improvement.tex).
- OpenAI, *No bigeodesics in planar first-passage percolation*, September 24, 2026: [primary introduction](https://raw.githubusercontent.com/openai/math/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex), saved as [fresh-bigeodesics-introduction.tex](fresh-bigeodesics-introduction.tex). A guessed unnumbered introduction path returned 404 before the correct path was opened.
- OpenAI, *A strict inverse-first-power bound for univalent functions*, September 24, 2026: [primary introduction](https://raw.githubusercontent.com/openai/math/main/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/00-introduction.tex), saved as [fresh-univalent-introduction.tex](fresh-univalent-introduction.tex).
- [Lean scope note 212](https://raw.githubusercontent.com/openai/math/main/lean/docs/212.md), [PlanarFirstPassage.lean](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/PlanarFirstPassage.lean), [GammaPassage.lean](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/GammaPassage.lean), [scope note 072](https://raw.githubusercontent.com/openai/math/main/lean/docs/072.md), and [history](https://raw.githubusercontent.com/openai/math/main/history.md). Fresh copies are [scope 212](fresh-lean-docs-212.md), [exponential statement](fresh-PlanarFirstPassage.lean), [Gamma statement](fresh-GammaPassage.lean), [scope 072](fresh-lean-docs-072.md), and [history](fresh-history.md). Strict convexity is still explicitly outside the selected statements. No relevant repair or withdrawal appears in the listed history. No Lean build was run.
- Scott Armstrong and Ahmed Bou-Rabee, *Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124v1, submitted October 30, 2026: reopened its [arXiv abstract](https://arxiv.org/abs/2610.42124) and [full HTML](https://arxiv.org/html/2610.42124v1). Introduction paragraph preceding the discussion of the planar continuum case calls exponential lattice strict convexity and differentiability an announcement and cites OpenAI; it does not validate that proof. Its own theorem concerns a rotationally invariant continuum model, so it is not a solution of our lattice row.

The exact four theorem environments quoted above occur verbatim in the freshly reopened introductions. All three introductions agree with the earlier saved sources after terminal whitespace normalization; foundations and improvement also agree. The earlier external audit/exposition records above are inherited evidence, not new openings in round 5. New searches used exact titles with error/refutation/referee, arXiv-domain strict-convexity queries, and GitHub issue search `repo:openai/math "first-passage"` (no issues returned).

**Earlier result rechecked.** The common-gauge estimate follows by splitting each projected calibration difference into an L-period baseline error and J local comparisons avoiding the projected cells. The projection norm is at most 2^m and there are at most N terms, giving `N 2^m(L+JK) beta`. Exterior independence makes each incoming-cost projection common; identical joint laws give the same deterministic mean at the random anchor. Interpolation cancels the common raw costs. This reproduces the conditional result in the [round 4 proof](round4-common-gauge-proof.md). Rerunning [recheck_common_gauge.py](recheck_common_gauge.py) passed in 0.084 seconds, peak RSS 16.45 MiB.

**New check.** [PROOF.md](PROOF.md) verifies `found:lem-network` for prescribed translated road labels satisfying the manuscript's tracking, spatial locality, domination, and period-defect assumptions. If an added marked anchor's nominal center is within coordinate distance D of its assigned grid index, admissible uniform constants are

`H=ceil(D)+30`, `K_D=20ceil(D)+41`.

The construction attaches each endpoint to the nearest grid intersection with two signed intervals, each controlled by four deterministic full periods. A grid edge costs at most five periods. A Manhattan route has at most `4ceil(D)+5` edges, so its total comparison error is at most `[16+5(4ceil(D)+5)] beta`. All queried nominal locations lie within D+5, the dependence radius contributes at most 20 in oblique coordinates, and cell assignment fits within H. Substituting private exterior weights at their original spatial locations preserves this support radius for inserted baselines. This discharges the network comparison hypothesis used in the prior common-gauge check, under the road and calibration assumptions just stated.

**Attempts to break it.** [check_network.py](check_network.py) passed 131225 exact rounding/route checks, 243 rational period-containment checks, all 35721 pairs of finite strip crossings, repeated-occurrence checks, and 230 signed-telescoping checks. Runtime was 0.275 seconds and peak RSS 13.97 MiB, with inherited nice 20 and one thread. Constants were counted a second way as four attachment intervals at 4 beta and at most `4ceil(D)+5` grid intervals at 5 beta. Negative controls confirm that physical reverse costs cannot replace signed comparisons, and that a maximum over many selected labels need not inherit a per-label expectation bound.

No counterexample was found under these hypotheses. The estimate is pairwise for prescribed labels, not a maximum over an arbitrary family. The dominated calibration, local envelope lemma, phases and conditioned period estimates, link estimates, and closure of improved roads are not established by this check. The next check should be `found:lem-envelope`, especially its simultaneous endpoint lower bound U' and its use for physical competitors; phase conditioning remains a separate issue. No correctness judgment of the full strict-convexity proof follows.
