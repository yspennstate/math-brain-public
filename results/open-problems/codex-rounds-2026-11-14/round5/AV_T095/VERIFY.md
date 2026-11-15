# T095 verification, round 5

Checked 15 November 2026. Literature verdict: **PARTIAL-CLAIMED**, for every Gamma law with positive shape and rate, including exponential weights. None of the three candidate main statements claims differentiability for every continuous law in T095. REPORT.md uses the continuation task's later required verdict format.

## Exact main statements

All three preprints name **OpenAI** as author in their actual `build/main.tex` files, reopened this session. Dates below are copied from those entry files. The following theorem environments are verbatim from the actual introduction sources, also reopened this session. The repository's latest commit API still returns `4eaee87548250b2682affda7d05d947c05554bae` (October 30, 2026); no later version was located.

### Strict convexity and differentiability of the planar exponential first-passage limit shape — September 24, 2026

Author: OpenAI. Opened [the actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex); local source: [source-exponential-introduction.tex](source-exponential-introduction.tex).

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

### No bigeodesics in planar first-passage percolation — September 24, 2026

Author: OpenAI. Opened [the actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex); local source: [source-no-bigeodesics-introduction.tex](source-no-bigeodesics-introduction.tex).

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

### QAOA attains the SK ground-state energy in the thermodynamic-first limit — September 25, 2026

Author: OpenAI. Opened [the actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/sections/01-introduction.tex); local source: [source-qaoa-introduction.tex](source-qaoa-introduction.tex).

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

| Exact requirement in T095 | Shape preprint | No-bigeodesics preprint | QAOA preprint |
| --- | --- | --- | --- |
| Undirected nearest-neighbor first-passage percolation | Same path metric on unoriented edges | Same model | Different: zero-field SK spin glass and quantum circuits |
| On Z² | Same dimension | Same dimension | No lattice limit-shape statement |
| iid nonnegative edge weights | Independent common exponential/Gamma law; positive almost surely | Same general nonnegative iid setting | Different random quantities |
| A continuous law | Only Gamma(shape κ, rate λ), κ,λ>0, including exponential κ=1 | General nonatomic law, matching the row | No matching distributional quantifier |
| E[min(τ₁,…,τ₄)²]<∞ | Automatic on its subclass because min²≤τ₁² and Eτ₁²=κ(κ+1)/λ² | Exactly the same minimum-of-four condition | Not applicable |
| Boundary differentiable at every point | Claimed everywhere; Fréchet differentiability off zero and C¹ boundary have the requested strength | Conclusion excludes doubly infinite geodesics; no boundary-differentiability conclusion | Conclusion is an asymptotic optimized energy limit |
| All qualifying continuous laws | Not claimed | Law range matches, but quantity and conclusion do not | Unrelated |

For example, Uniform[1,2] meets T095 (min²≤4), but has bounded support and is not Gamma. This shows a strict scope restriction, not a counterexample to T095. The exponential theorem additionally claims strict convexity, whereas the general Gamma theorem states differentiability only. No implication from the no-bigeodesics conclusion to the full row was established in this verification.

The shape candidate is PARTIAL-CLAIMED; the other two are NOT-THIS for T095. The original note's assertion that no continuous example is known should now distinguish an announced Gamma result from a verified resolution of the universal statement. Neither a title match nor a Lean badge changes the law quantifier.

## Follow-ups and records actually opened

The bounded update search used the exact shape title with error/refutation/review/arxiv; first-passage differentiability with OpenAI/2026 and November 2026; GammaPassage with error/review/issue; and openai/math with transverse. It found no new full continuous-law solution, same-title arXiv version, specific refutation, or named referee/expert assessment changing the earlier reports. This is a bounded negative finding.

| Opened source | Finding and limit |
| --- | --- |
| Scott Armstrong and Ahmed Bou-Rabee, [*Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124](https://arxiv.org/abs/2610.42124) | Abstract page reopened: submitted October 30, 2026; proves a continuum fluctuation bound in Rᵈ, d≥2. It is not an arXiv version of the lattice differentiability preprint or a solution to T095. Full text was not reopened this round. |
| [Official Lean scope note](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/212.md), saved as [source-lean-scope.md](source-lean-scope.md) | Explicitly describes differentiability for all positive Gamma shape/rate; excludes strict convexity from the selected statements. No universal continuous-law target. |
| [Gamma Comparator challenge](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GammaPassage.lean), saved as [source-gamma-target.lean](source-gamma-target.lean) | The actual target quantifies over Gamma laws and actual time constants. Its sorry is a challenge placeholder; this is not the final proof file. |
| [Final Gamma differentiability proof](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/GammaPassage/Differentiability.lean), saved as [source-gamma-differentiability.lean](source-gamma-differentiability.lean) | Calls the earlier no-corner and time-constant results. No local Lean build or complete dependency audit was performed. |
| [MathVet primary fidelity table, pinned revision](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv), family 212 | Reopened row reports partial coverage and comparator-sandboxed-pass. It distinguishes Gamma differentiability from no-bigeodesics and exponential strict convexity. This reports selected-statement checking, not a referee judgment of all manuscript arguments. |
| Carlos Toledo / cert-machine [statement audit](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json) and [kernel record](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-kernel.json), both reopened | Family 212 distinguishes the narrower Gamma/exponential differentiability targets. The GammaPassage and PlanarFirstPassage kernel rows report Comparator exit 0 and acceptance by Lean and nanoda on October 10, 2026. These are reported external runs for selected statements, not local reruns or certification of the full manuscript; the recorded peak memory exceeds this task’s ceiling. Relevant rows saved in [external-kernel-records.json](external-kernel-records.json). |
| [Repository history](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/history.md), saved as [source-history.md](source-history.md) | No FPP repair or withdrawal notice in this file. |
| [Repository issues](https://github.com/openai/math/issues) | Default open-issue view shows zero open issues. This does not exclude criticism elsewhere or establish anything about closed issues. |
| [Latest commit API](https://api.github.com/repos/openai/math/commits?per_page=1) | Returned the same October 30 snapshot as the earlier sessions. |
| Actual manuscript [endpoint source](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/differentiability/endpoints.tex), [witness source](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/differentiability/witnesses.tex), and conclusion source | Reopened and saved locally. The endpoint text differs from the original worker's local file only by a trailing blank line. |

Other follow-ups described in the earlier reports remain inherited leads unless explicitly recorded here as reopened. No later source was treated as independent validation merely because it cited the announcement.

## Independent recheck of round 4

Read REPORT.md, LOG.md, PROOF.md and scripts in all three specified earlier folders; the original folder has no PROOF.md or scripts. Re-ran the round 4 audit unchanged, from this folder, with `OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/AV_T095/audit.py`. All checks pass: 2,307 contour sets, 1,536 strip placements, 1,734 dependence-coordinate cases, the source/theorem checks, and the exact union bound 181/48000. Actual nice is 20, runtime 0.292 seconds, measured peak RSS 15,384,576 bytes; the old script catches its rejected data-limit setter.

Independently re-derived the contour exponent: m/2 boundary edges face forward neighbors, so at least m/8 distinct sites must be bad; greedy spacing leaves at least m/[8(2k+1)²] independent bad tests. The previous threshold ζ=2^(−48(2k+1)²) turns their union bound into 9Σₘ≥₄(m+1)²16^(−m). Summing after m=j+4 gives 9·16^(−4)[a(1+a)/(1−a)³+10a/(1−a)²+25/(1−a)] at a=1/16, equal to 181/48000. The previous result holds within its stated fixed-Gamma shape-theorem input.

## Spot check

The single extension is the deterministic chunk-to-disjoint-witness reduction, `df:wi:chunk-witness` and its negative-defect multiplicity estimate `df:wi:chunk-defect`. The complete all-case derivation is in [PROOF.md](PROOF.md); [audit.py](audit.py) supplies an independent finite subpath oracle.

The corner gap c gives min Hσ=H−c|Δr|, so any cheap transverse exit witnesses a negative extreme-support defect. A backward exit cannot be cheap by nonnegative costs. A forward exit yields either a negative-defect outer piece or a strict E(s,L) crossing. The shifted center's fractional phase is handled directly, including negative slopes and coordinates. For very negative chunks, threshold splitting supplies disjoint negative-defect witnesses; simplicity makes witnesses from distinct chunks disjoint even when coarse indices repeat. This proves H(Q)≥−ηs−2ηsM_Q and H(P)≥(N−1)ηs−4ηsM_tot under the stated scale assumptions.

The endpoint interface uses the arbitrary-endpoint estimate with A=R=4, ε=η and the characteristic-length bound P(E(s,L))≤q₀. Translation invariance gives P(Aᵢ,ₕ)≤q₀+o(1), uniformly at one fixed chosen scale, without independence between the two defining alternatives. No gap was found in this reduction under its explicit inputs. This finding is not an endorsement of the whole proof; the remaining BK and itinerary step was not verified this round.

The final command `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py` passes 723 deterministic paths, 3,222 chunks and 559,764 candidate subpath intervals. Greedy interval packing and dynamic programming agree in every chunk. Coverage includes 1,800 cheap full chunks, 889 negative-defect chunks, 129 cheap chunks requiring the crossing alternative, 48 paths revisiting coarse indices, 1,056 shifted-center phases, one tied exit, two cheap forward exits with an empty final outer piece, and 29 exact-threshold equalities. All local and total defect bounds hold. The run took 6.132 seconds at nice 20, with peak RSS 18,219,008 bytes. These finite checks test deterministic bookkeeping; the all-case proof is in PROOF.md and no Gamma probability estimate is inferred from the fixtures.

## Recommended replacement for “where it stands”

OpenAI's preprint *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026) claims differentiability everywhere for every Gamma law with positive shape and rate, including exponential weights. The repository's selected Lean statements cover Gamma differentiability, while exponential strict convexity is outside those selected statements. The general continuous-law statement under the Cox–Durrett minimum-of-four moment condition is outside these claims, and no later resolution was located in this bounded search.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 07:31 Asia/Tbilisi.
