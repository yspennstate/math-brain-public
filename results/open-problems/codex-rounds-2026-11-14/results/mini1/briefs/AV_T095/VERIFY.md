# T095: differentiability of the planar FPP limit shape

Checked 14 November 2026. **PARTIAL-CLAIMED:** all positive Gamma laws, including exponential weights; the universal continuous-law statement is not claimed by these candidates. This records the scope of the claims, not a judgment that the proofs are correct.

## Our statement

For undirected nearest-neighbor first-passage percolation on Z², with iid nonnegative edge weights of any continuous law satisfying E[min(τ₁,τ₂,τ₃,τ₄)²] < ∞, the boundary of the deterministic limit shape is differentiable at every point. Here “continuous” means atomless; it does not require a density or finite individual-edge second moment.

## 1. Strict convexity and differentiability of the planar exponential first-passage limit shape

Author: **OpenAI**, exactly as in the paper. Date: **September 24, 2026**. Opened the actual LaTeX entry file `build/main.tex` and the [introduction containing Theorems 1.1 and 1.2](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex). Local verbatim source: [source-exponential-introduction.tex](source-exponential-introduction.tex).

The following are exact theorem environments copied from the source, including its TeX notation and labels:

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

\begin{theorem}[Differentiability for Gamma weights]
\label{thm:gamma-differentiability}
For independent Gamma edge weights with any fixed shape $\kappa>0$
and rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable at
every nonzero vector, and $\partial\Bcal$ is a $C^1$ curve.
\end{theorem}
```

The surrounding model definition assigns weights to unoriented nearest-neighbor edges of Z², defines passage time as the infimum of sums over undirected paths, and defines B = {v : μ(v) ≤ 1} using the almost-sure time constant. Thus the model and geometric quantity agree with T095.

| Phrase in T095 | What these theorems claim | Coverage |
| --- | --- | --- |
| First-passage percolation | Undirected nearest-neighbor edge FPP, with costs added along paths and minimized | Same model |
| On Z² | On Z², with a norm on R² | Same dimension |
| iid nonnegative edge weights | Independent weights of one fixed exponential or Gamma law, positive almost surely | A subclass of the same iid nonnegative models |
| Whose law is continuous | Every Gamma(shape κ > 0, rate λ > 0) law, including exponential (κ = 1) | These laws are continuous; arbitrary other continuous laws are not covered |
| E[min(τ₁,…,τ₄)²] < ∞ | Gamma weights have finite second moment, so satisfy the condition | The moment hypothesis holds on the claimed subclass; the theorem is not stated for every law satisfying only that hypothesis |
| Boundary differentiable at every point | μ Fréchet differentiable at every nonzero vector and boundary C¹; exponential also has a unique supporting line at every boundary point | At least the requested strength, at every boundary point, for the claimed subclass |
| All qualifying continuous laws | No universal continuous-law theorem appears in either main statement | Not covered |

The moment inclusion can be checked directly: min(τ₁,…,τ₄)² ≤ τ₁² and E[τ₁²] = κ(κ+1)/λ² < ∞ for these Gamma laws. For example, iid Uniform[1,2] weights satisfy every hypothesis of T095 but are not a Gamma law, so neither of these theorem statements applies to them. This is a scope example, not a counterexample to differentiability. Strict convexity is additionally claimed for the exponential model; it is not claimed for all Gamma laws, and should not be conflated with differentiability.

## 2. No bigeodesics in planar first-passage percolation

Author: **OpenAI**. Date: **September 24, 2026**. Opened `build/main.tex` and the [actual introduction containing Theorem 1.1](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex). Local verbatim source: [source-no-bigeodesics-introduction.tex](source-no-bigeodesics-introduction.tex).

Exact main theorem environment:

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

The preceding paragraph specifies unoriented nearest-neighbor edges of Z² and a common Borel law G on [0,∞). Thus the model, dimension, iid assumption, nonnegativity, atomlessness, and minimum-of-four second-moment condition match T095 exactly. The conclusion differs: it excludes all doubly infinite minimizing paths simultaneously, rather than asserting differentiability of the limit shape. The introduction explicitly makes no differentiability, strict-convexity, or curvature assumption; it does not state a general differentiability corollary. Therefore this is **NOT-THIS** as a proposed solution to T095, although it is relevant FPP work under the same distributional hypotheses. No implication from its conclusion to T095 has been established in this verification.

## 3. QAOA attains the SK ground-state energy in the thermodynamic-first limit

Author: **OpenAI**. Date: **September 25, 2026**. Opened `build/main.tex` and the [actual introduction containing Theorem 1.1](https://github.com/openai/math/blob/main/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/sections/01-introduction.tex). Local verbatim source: [source-qaoa-introduction.tex](source-qaoa-introduction.tex).

Exact main theorem environment:

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

Its definitions are hₙ,J(σ) = n^(−1/2) Σᵢ<ⱼ Jᵢⱼ σᵢσⱼ with independent standard Gaussian Jᵢⱼ, P_* = limₙ n^(−1) E maxσ hₙ,J(σ), vₚ(γ,β) = the n→∞ expected QAOA energy per spin at fixed depth and deterministic angles, and Qₚ = supγ,β vₚ(γ,β). The theorem then takes p→∞. It is an asymptotic energy-attainment statement for a mean-field spin glass, with no lattice Z² FPP, nonnegative passage times, limit-shape boundary, or differentiability assertion. It is **NOT-THIS** for T095.

## Follow-ups and formalization

The repository's [family-212 Lean scope note](https://github.com/openai/math/blob/main/lean/docs/212.md) was opened. It describes differentiability for every positive Gamma shape/rate, including the exponential case, and explicitly places exponential strict convexity outside the selected statements. The actual selected statement files [PlanarFirstPassage.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PlanarFirstPassage.lean) and [GammaPassage.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GammaPassage.lean) were also opened: their conclusions are differentiability, a genuine passage-time limit norm, and boundary regularity. The exponential challenge normalizes the rate to 1; the Gamma challenge quantifies over all positive shapes and rates. The `sorry` in a Comparator challenge is a placeholder for a separately supplied proof, not itself evidence of an unproved claim in the supplied solution. The actual proof files and outside checking reports are recorded below.

The [family-281 Lean note](https://github.com/openai/math/blob/main/lean/docs/281.md) was opened. It limits the selected formalizations to SK value identities and full support of minimizers, rather than QAOA circuit convergence; none concerns FPP. The [repository history](https://github.com/openai/math/blob/main/history.md) was opened; its entries through October 29 record no revision or withdrawal of either family-212 manuscript. The three manuscript README files also contain no revision or withdrawal notice.

## Recommended replacement for “where it stands”

The general continuous-law statement remains open on the evidence checked here. OpenAI's unrefereed preprint *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026) claims differentiability everywhere for every Gamma law with positive shape and rate, including exponential weights, and strict convexity for exponential weights. The release supplies Lean material for the Gamma differentiability claim, but these claims do not cover all continuous weight laws satisfying the Cox–Durrett condition.

## Follow-up record and limits of verification

Repository snapshot: [4eaee87548250b2682affda7d05d947c05554bae](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae), whose commit metadata is dated October 30, 2026. Files were fetched from main; the snapshot identifier was then checked through GitHub's read-only API. All literature searches below were made on November 14, 2026.

| Opened source | What it adds |
| --- | --- |
| [Actual exponential Lean solution, BoundaryCurve.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/FirstPassage/BoundaryCurve.lean) | Supplies `manuscriptMain` from the actual time constant and differentiability/boundary-chart inputs. |
| [Actual Gamma Lean solution, Differentiability.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/GammaPassage/Differentiability.lean), [Gamma import catalogue](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/GammaPassage/Main.lean) | Supplies `gamma_differentiability` from no-corner and actual-time-constant results. The target quantifies over positive shape and rate, not over all continuous laws. |
| [Exponential Comparator configuration](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarFirstPassage.json), [Gamma configuration](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GammaPassage.json), [formalization catalogue](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/formalization.yaml), [Lean README](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/README.md) and [Comparator instructions](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/README.md) | Configurations select those two theorems, list no definition holes, and permit only propext, Quot.sound, and Classical.choice. |
| [MathVet primary fidelity table, family 212](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv) | Reports a sandboxed Comparator pass and partial coverage of the family headline: Gamma differentiability is stated, whereas strict convexity and no-bigeodesics are not selected conclusions. This is a scope audit and reported machine check, not a referee report on both papers. |
| [Carlos Toledo / cert-machine primary statement audit, family 212](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json) and [primary kernel-check record](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-kernel.json) | Statement audit distinguishes Gamma differentiability from the two uncovered conclusions. Kernel records for GammaPassage and PlanarFirstPassage report exit 0 and acceptance by Lean and nanoda on October 10, 2026. These are external reported runs, not runs repeated here; acceptance of selected statements does not certify the entire papers. |
| Scott Armstrong and Ahmed Bou-Rabee, [*Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124v1](https://arxiv.org/html/2610.42124v1), submitted October 30, 2026; abstract and full HTML opened | Its introduction cites the exponential shape preprint as an announcement. Its own result concerns continuum rotationally invariant FPP fluctuations; it does not establish general lattice-shape differentiability or independently validate the announced proof. |
| Dylan Herman, Shouvanik Chakrabarti, Junhyung Lyle Kim, Guneykan Ozgul, [*A Fully Polynomial Approximation Algorithm for the Sherrington-Kirkpatrick Model*, arXiv:2611.05446v1](https://arxiv.org/html/2611.05446v1), submitted November 3, 2026; abstract and full HTML opened | Section 1.3 cites the QAOA claim, explaining its order of limits and lack of quantitative depth and finite-size guarantees. It is a separate SK algorithm paper, not an arXiv version or validation of the supplied QAOA proof, and has no T095 implication. |
| Chris Kapulkin and Nathan Kershaw (names as on the arXiv page), [*Reasoning is topologically simple*, arXiv:2611.03739v1](https://arxiv.org/abs/2611.03739), submitted November 2, 2026; abstract and full HTML opened | Appendix B.3 includes the no-bigeodesics manuscript in a text-comparison corpus. This is a study of text topology, not an FPP proof review or an error report. |
| Myeongjin Kang, [*Removing the moment assumption from a stipulated planar no-bigeodesics theorem*, Zenodo record](https://zenodo.org/records/23647122), October 25, 2026; author-deposited record and [MathDB abstract](https://mathdb.com/abs/2610.00759) opened | The deposited abstract explicitly assumes the OpenAI source and specified proof inputs. It proposes a conditional no-bigeodesics extension beyond the minimum-of-four moment class; it supplies no general differentiability statement and is not independent validation of its source. PDF access details are recorded in LOG.md. |

The [Plectis Atlas family-212 page](https://wcook04.github.io/plectis-atlas/families/212.html) was opened to locate the primary scope/checking reports above. Its own catalogue was not substituted for the theorem source or the primary audit data. The [MathDB bigeodesics page](https://mathdb.com/p/331958/furstenberg-kesten-conjecture-on-bigeodesics-in-two-dimensio) was opened to locate Kang's author-deposited record; its historical summary was not used as authority for T095.

Searches used each candidate's exact title, the exact titles restricted to arxiv.org, and combinations with error, gap, refutation, review, Damron, Hoffman, and GammaPassage. A read-only GitHub issue search for `repo:openai/math "first-passage"` returned no issues. No same-title arXiv version, named specialist refutation, referee report, or independently checked proof of the full continuous-law differentiability statement was located in these searches. This is a bounded search result, not a claim that no such material exists.

No Lean build or full proof audit was performed. The supplied source statements and external checking records support recording a Gamma special-case claim and its formalization; they do not justify changing T095 to solved.

## Spot check

Selected lemma: **“Arbitrary endpoints”**, source label `df:gr:variable-endpoints`, in [the shape paper's endpoint section](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/differentiability/endpoints.tex). This is the crucial upgrade from prescribed-column crossing estimates to environment-dependent path endpoints, which the subsequent path-witness argument needs. Local complete source: [source-differentiability-endpoints.tex](source-differentiability-endpoints.tex).

The lemma says that, along the chosen scales s = 2^k and L = L_k with L/s → ∞, the probability of any path in {|x| ≤ AL, |r| ≤ Rs} having H₊ < −εs or H₋ < −εs tends to zero, uniformly under lattice translation. Here r(z) = z₂ − bz₁, m₀ = μ(1,b), fσ(z) = m₀x(z) + aσr(z), and Hσ(P) = τ(P) − fσ(ΔP).

The complete proof and its simultaneous-grid connection argument were read. The following checks concern this reduction, taking the earlier rare-fast-crossing and characteristic-scale lemmas as inputs.

1. **Endpoints chosen from the environment.** The grid event covers whole endpoint intervals before a path is selected. With meshes lⱼ = 2^max(0,m−4j−1) and wⱼ = 2^(k−j), a greedy decomposition uses at most 16 intervals per level. Thus each endpoint attachment has excess cost at most 16C₁s Σⱼ≥J j²2^(−j) + |aσ|. Rounding the target height changes the displacement of the whole attachment by less than one; no per-level rounding error needs to be added.
2. **The grid-event probability.** At level j there are O(2^(5j)) interval/bin pairs. The proof uses j² disjoint-strip trials, with failure at most (1−q₀)^(j²), and coordinate-path tail errors at most 2exp(−c₀j²wⱼ). Their union bound is a tail of a convergent series O(Σⱼ≥J 2^(5j)(exp(−q₀j²) + 2exp(−c₀j²))), which tends to zero as J grows. No independence between successful crossings and their attachments is required for this union bound.
3. **Possibly backward original endpoints.** Nonnegative path cost and Hσ < −εs imply Δx ≥ −(2R max|aσ|/m₀)s. Both attachments extend by at least l_J, so the final span is at least 2l_J − C₃s ≥ l_J for large k at fixed J. Since l_J/s → ∞, the extended path qualifies for the earlier long-crossing estimate even if the original path went slightly backward.
4. **Signs, constants, and limits.** The two attachment errors together are bounded by 32C₁s Σⱼ≥J j²2^(−j) + 2max|aσ|. The choices in the text make this at most εs/2, leaving defect below −εs/2. At fixed J only O((L/l_J)²) = O(2^(8J)) coarse-column pairs remain, independent of k. One first sends k to infinity, then J to infinity; there is no union over a growing number of endpoint pairs at fixed J.

No gap was identified in these endpoint-extension estimates conditional on their stated earlier inputs. This spot check does not verify those inputs, the rest of the differentiability argument, the strict-convexity proof, or the no-bigeodesics proof. It does not change the claim-scope verdict.

Task: “Verify: has open problem T095 been settled by the OpenAI math release?” — November 14, 2026, approximately 21:04 Asia/Tbilisi.


