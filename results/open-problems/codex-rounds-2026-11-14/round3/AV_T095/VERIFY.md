# T095 verification and continuation

Checked 15 November 2026 (Asia/Tbilisi). The release claims the Gamma special case; the full continuous-law statement is not claimed by the three candidates. The new work below conditionally checks the characteristic-length input to the earlier endpoint reduction. It does not judge any full preprint proof correct.

## Exact candidate statements

All three manuscripts name **OpenAI** as author in the actual TeX entry files. The two FPP manuscripts are dated September 24, 2026; the QAOA manuscript is dated September 25, 2026. The current default-branch snapshot returned by the read-only recent-commit tool is still `4eaee87548250b2682affda7d05d947c05554bae`, dated October 30, 2026, the snapshot used by the earlier worker.

### Strict convexity and differentiability of the planar exponential first-passage limit shape

Opened the [actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex) and entry file `build/main.tex`. Local source: [source-exponential-introduction.tex](source-exponential-introduction.tex). Exact theorem environments:

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

```tex
\begin{theorem}[Differentiability for Gamma weights]
\label{thm:gamma-differentiability}
For independent Gamma edge weights with any fixed shape $\kappa>0$
and rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable at
every nonzero vector, and $\partial\Bcal$ is a $C^1$ curve.
\end{theorem}
```

### No bigeodesics in planar first-passage percolation

Opened the [actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex) and entry file `build/main.tex`. Local source: [source-no-bigeodesics-introduction.tex](source-no-bigeodesics-introduction.tex). Exact main theorem:

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

### QAOA attains the SK ground-state energy in the thermodynamic-first limit

Opened the [actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/sections/01-introduction.tex) and entry file `build/main.tex`. Local source: [source-qaoa-introduction.tex](source-qaoa-introduction.tex). Exact main theorem:

```tex
\begin{theorem}\label{thm:main}
For the zero-field SK model~\eqref{eq:sk-model},
\begin{equation}\label{eq:main-result}
 \lim_{p\to\infty}Q_p=\Pstar.
\end{equation}
Equivalently, for every $\varepsilon>0$ there exist a finite integer $p$ and
deterministic real vectors $\gamma,\beta\in\R^p$, independent of $n$ and $J$,
such that $v_p(\gamma,\beta)\ge\Pstar-\varepsilon$.
\end{theorem}
```

## Comparison with our statement

Our claim concerns undirected nearest-neighbor edge FPP on Z², iid nonnegative weights of an arbitrary continuous (atomless) law with E[min(τ₁,…,τ₄)²] < ∞, and differentiability at every point of the deterministic limit-shape boundary.

| Clause | Shape preprint | No-bigeodesics preprint | QAOA preprint |
| --- | --- | --- | --- |
| Model | Same undirected nearest-neighbor edge FPP | Same FPP | Zero-field Sherrington–Kirkpatrick spin glass and QAOA |
| Dimension | Z², norm on R² | Z² | Number n of spins tends to infinity |
| iid nonnegative weights | Fixed positive Gamma law, including exponential | Common Borel law G on [0,∞) | Gaussian spin couplings, a different model |
| Continuous law | Gamma only; not every atomless law | G has no atoms, exactly as required | No corresponding FPP hypothesis |
| Minimum-of-four second moment | Holds since min(τ₁,…,τ₄)² ≤ τ₁² and Eτ₁² = κ(κ+1)/λ² | Exactly the same hypothesis | No corresponding condition |
| Quantity | Time-constant norm and its unit-ball boundary | Doubly infinite minimizing paths | Limiting optimized QAOA energy versus Parisi value |
| Strength | Everywhere Fréchet differentiability away from zero and C¹ boundary; exponential strict convexity additionally claimed | Almost-sure simultaneous exclusion of all bigeodesics, not boundary differentiability | Equality after the size limit and then the depth limit, not an FPP result |
| Universal law quantifier | Missing: covers only Gamma | Correct law class, different conclusion | Unrelated |

Uniform[1,2] is a concrete continuous nonnegative law in the target class: min(τ₁,…,τ₄)² ≤ 4, yet the law is not Gamma. Thus the first preprint does not claim the entire target statement. This is an example outside its scope, not a counterexample to differentiability. The second introduction explicitly assumes no shape differentiability and gives no general differentiability corollary; no implication from its stated conclusion to T095 is established here. Candidate verdicts remain PARTIAL-CLAIMED for the shape paper and NOT-THIS for the other two papers.

## Follow-ups opened and bounded update search

The continuation search was limited to five minutes as requested. Queries included the exact shape title with November/error, first-passage differentiability with continuous/OpenAI/2026, GammaPassage/error, first-passage differentiability after 2026-11-13, and the shape title with error. No newly located paper solves the full continuous-law question, and no new specific refutation was found in that pass. This is a search limit, not proof of absence.

| Opened in this session | Observation |
| --- | --- |
| Scott Armstrong and Ahmed Bou-Rabee, [*Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124](https://arxiv.org/abs/2610.42124), abstract and [full HTML v1](https://arxiv.org/html/2610.42124v1), submitted October 30, 2026 | Their theorem concerns continuum rotationally invariant FPP fluctuations. The introduction describes the exponential lattice shape result as recently announced; it neither proves general lattice differentiability nor certifies the announcement. |
| [OpenAI history.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/history.md) and recent-commit metadata | No FPP repair, revision, or withdrawal is recorded there. The current repository snapshot is unchanged from the earlier worker's snapshot. |
| [Official Lean scope note](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/212.md), saved as [source-lean-scope.md](source-lean-scope.md) | Specifies Gamma differentiability and excludes exponential strict convexity from the selected statements. It does not state a formalized all-continuous-law differentiability theorem. |
| [Actual Gamma Comparator target](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GammaPassage.lean), saved as [source-gamma-target.lean](source-gamma-target.lean) | Defines actual undirected paths and passage times; the law quantifier is Gamma with positive shape/rate. The challenge's `sorry` is a placeholder for the separate solution. |
| [Actual final Gamma solution](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/GammaPassage/Differentiability.lean), saved as [source-gamma-differentiability.lean](source-gamma-differentiability.lean) | Calls the Gamma no-corner and time-constant/boundary-chart results. No local compilation or audit of its full dependency chain was performed. |
| [MathVet primary fidelity table, family 212](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv) | Reports partial headline coverage and a sandboxed Comparator pass. The selected statements include Gamma differentiability, with strict convexity and no-bigeodesics absent from their conclusions. |
| [Carlos Toledo / cert-machine primary statement audit, family 212](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json) | Separately maps the Gamma differentiability clause to GammaPassage and records the other two family claims as outside the selected conclusions. It is a statement-scope audit, not a proof of full T095. |

The [earlier VERIFY.md](~/codex_op_1114/briefs/AV_T095/VERIFY.md) and [earlier LOG.md](~/codex_op_1114/briefs/AV_T095/LOG.md) were read in full. Their other follow-up records are historical observations by that worker and were not independently refreshed here; they include no same-title arXiv version or named specialist referee report. Only the sources in the table above are used for this session's follow-up claims. No SOLVED_ELSEWHERE.md is written because no full solution elsewhere was identified.

## Earlier result rechecked

The reopened actual theorem blocks match the earlier saved sources, so the Gamma-only claim-scope finding holds independently of the earlier summary.

The earlier arbitrary-endpoint spot check was also re-derived from its complete saved source. For fixed J, the exact attachment tail is

\[
 \sum_{j\ge J}j^2 2^{-j}
 =2^{1-J}(J^2+2J+3).
\]

This follows by writing j = J+h and using the three geometric sums Σ2⁻ʰ = 2, Σh2⁻ʰ = 2, and Σh²2⁻ʰ = 6. Two attachments therefore contribute at most 64C₁s2⁻ᴶ(J²+2J+3) + 2max|aσ|. Fixing sufficiently large J and then increasing k makes this smaller than εs/2. Nonnegative original path cost bounds its possible backward displacement by 2Rmax|aσ|s/m₀, while the attachments add at least 2lⱼ with j = J and lⱼ/s → ∞. The final span is consequently at least lⱼ eventually. The number of coarse-column pairs is O(2⁸ᴶ), fixed as k increases; the grid-event error is a convergent tail after multiplying exp(−cj²) by 2⁵ʲ. The same order of limits therefore supports the earlier conditional endpoint conclusion. Its earlier crossing inputs remain assumptions.

## Spot check

Chosen new piece: the entire **Characteristic lengths** section, [actual source](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/differentiability/scales.tex), comprising `df:gr:tilt`, `df:gr:characteristic-lengths`, and `df:gr:record-scales`. Local source: [source-scales.tex](source-scales.tex). This is precisely an input left conditional by the earlier endpoint check. Its two crossing inputs were opened in [source-crossings.tex](source-crossings.tex), with the supporting setup in [source-preliminaries.tex](source-preliminaries.tex).

The complete conditional derivation is in [PROOF.md](PROOF.md). Scaling M internal Gamma weights by 1−δ has likelihood second moment \((1-\delta^2)^{-\kappa M}\). The region has at most 144ns internal edges; choosing δ = η₀s/n makes the log of this second moment at most 288κη₀²s³/n, hence uniformly bounded at n = s³. The scaling turns a crossing with positive allowance Ks into a negative-defect crossing; Cauchy–Schwarz transfers the assumed rare-fast estimate back to the original law. A second derivation through the Laplace transform of the sum of all M modified coordinates gives the same identity.

The short-length proof covers both n → ∞ and bounded n, and the subsequence argument gives the required uniformity in 1 ≤ n ≤ Cs. The first-dyadic-threshold and record-minimum arguments require no monotonicity of crossing probabilities or of Lₖ. Their record comparison gives exactly the smaller-scale trial lengths needed in the endpoint grid, including its terminal mesh.

No flaw was found in this reduction conditional on rare-fast crossings and localized travel. This does not verify those two inputs or the full differentiability argument. The next check should target `df:cr:rare-fast`, particularly its crossing amplification, dependence radius, and high-density oriented-path lemma.

## Recommended replacement for “where it stands”

The general continuous-law statement remains open on the evidence checked here. OpenAI's unrefereed preprint *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026) claims differentiability everywhere for all Gamma laws with positive shape and rate, including exponential weights, and strict convexity for exponential weights. The supplied Lean targets cover Gamma differentiability, while the conditional checks here verify only reductions used in the manuscript and do not settle the full statement.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 00:52 Asia/Tbilisi.

