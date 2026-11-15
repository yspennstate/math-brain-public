# Verification of T050

Updated 15 November 2026. Literature verdict: PARTIAL-CLAIMED. The strict-convexity preprint claims only the planar exponential special case of our row. The continuation result in [PROOF.md](PROOF.md) proves a conditional local-envelope input, not strict convexity or the correctness of the manuscript as a whole.

## Our statement

For first-passage percolation on Z^d, d >= 2, with iid continuous edge weights satisfying E[min(t_1,...,t_(2d))^d] < infinity, the limit shape is strictly convex. The usual nonnegative weights and undirected nearest-neighbor edge model are understood.

## 1. The strict-convexity candidate

OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape*, September 24, 2026. Reopened its actual [introduction TeX](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex), saved as [convexity-introduction.tex](convexity-introduction.tex). Its main theorem is quoted exactly, retaining the TeX:

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

The additional Gamma theorem is also exact:

```tex
\begin{theorem}[Differentiability for Gamma weights]
\label{thm:gamma-differentiability}
For independent Gamma edge weights with any fixed shape $\kappa>0$
and rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable at
every nonzero vector, and $\partial\Bcal$ is a $C^1$ curve.
\end{theorem}
```

| Our clause | Actual theorem and model definition | What is covered |
| --- | --- | --- |
| First-passage percolation | Minimum sum of weights along undirected nearest-neighbor lattice paths | Same model |
| Z^d, every d >= 2 | Z² | Only d=2; no higher-dimensional claim |
| iid | Independent weights of one fixed exponential rate | Same iid requirement |
| Continuous weights, with no specified law | Exponential weights, all positive rates | One family of continuous laws |
| Minimum-of-2d d-th moment finite | Exponential laws have all positive moments | Satisfies our hypothesis in this special case; no theorem for the full moment class |
| Limit shape | Unit ball of the time-constant norm | Same asymptotic body |
| Strictly convex | Exact strict convexity, plus differentiability and C¹ boundary | Same strict-convexity conclusion in the special case; no explicit shape or curvature bound |
| Broader laws | Gamma differentiability theorem | Does not assert strict convexity for nonexponential Gamma laws |

Independent scale check: dividing rate-one exponential weights by lambda gives rate-lambda weights, so `mu_lambda=mu_1/lambda` and the ball scales by lambda. The minimum of four rate-lambda exponentials is rate 4lambda, with second moment `2/(4lambda)^2=1/(8lambda²)`. Thus every rate in the main theorem is a special case of the row. Differentiability does not imply strict convexity; it cannot supply the missing Gamma or general-law conclusion.

## 2. The no-bigeodesics candidate

OpenAI, *No bigeodesics in planar first-passage percolation*, September 24, 2026. Reopened the actual [introduction TeX](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex), saved as [bigeodesics-introduction.tex](bigeodesics-introduction.tex). Main theorem, exactly:

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

The preceding definition specifies iid nonnegative weights on unoriented nearest-neighbor edges of Z². Its nonatomic law and minimum-of-four second moment match our assumptions at d=2, including singular continuous laws and laws without a finite individual-edge second moment. Its conclusion is absence of doubly infinite geodesics, rather than strict convexity of the shape. It supplies no theorem deriving our conclusion from that absence and no higher-dimensional statement: NOT-THIS for the requested conclusion.

## 3. The univalent-functions candidate

OpenAI, *A strict inverse-first-power bound for univalent functions*, September 24, 2026. Reopened the actual [introduction TeX](https://github.com/openai/math/blob/main/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/00-introduction.tex), saved as [univalent-introduction.tex](univalent-introduction.tex). Main theorem, exactly:

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

Here S is the class of injective holomorphic maps of the unit disk with f(0)=0 and f'(0)=1, M is an integral mean of a derivative power, and B_b is its bounded-image universal growth spectrum. This is an exponent bound in complex analysis. There is no edge-weight model, lattice dimension, passage-time moment condition, or limit shape: NOT-THIS.

## Follow-ups actually opened in this session

The bounded update search began at 09:46 +04 and ended before 09:51 on 15 November 2026. It used exact-title/error/refutation/review/November queries, `openai/math` first-passage error queries, and arXiv-restricted strict-convexity queries. No new general solution, exact-title arXiv version, substantive proof assessment, or error report was located. This is a bounded search result, not a claim that all commentary has been exhausted.

* Opened [history.md](https://github.com/openai/math/blob/main/history.md), saved as [source-history.md](source-history.md). No listed repair or withdrawal concerns these candidates. The latest entry in that file is dated October 29, 2026.
* Opened [lean/docs/212.md](https://github.com/openai/math/blob/main/lean/docs/212.md), saved as [source-lean-scope.md](source-lean-scope.md). It explicitly excludes strict convexity from the selected differentiability statements.
* Reopened [PlanarFirstPassage.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PlanarFirstPassage.lean) and [GammaPassage.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GammaPassage.lean), saved as [PlanarFirstPassage.lean](PlanarFirstPassage.lean) and [GammaPassage.lean](GammaPassage.lean). Their conclusions concern differentiability, C¹ boundary and supporting lines; neither concludes strict convexity or no bigeodesics. These are challenge statements; their placeholders do not by themselves assess the separate solution files. No Lean build or solution audit was performed.
* Opened [Scott Armstrong and Ahmed Bou-Rabee, *Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124](https://arxiv.org/abs/2610.42124), submitted October 30, 2026. The abstract concerns fluctuation bounds in rotationally invariant continuum FPP on R^d. It does not state a solution of our iid lattice strict-convexity problem. Earlier workers inspected the paper's citation of the announcement; this session refreshed its arXiv abstract, not that citation's full context.
* Opened the read-only [repository issue search](https://api.github.com/search/issues?q=repo%3Aopenai%2Fmath%20is%3Aissue%20%22first-passage%22): zero issues, with incomplete_results=false. This does not search every possible synonym or external discussion.
* Reopened the actual [strict-convexity foundations](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex) and [improvement source](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/improvement.tex), saved as [source-foundations.tex](source-foundations.tex) and [source-improvement.tex](source-improvement.tex). Both, the three introductions, and the two Lean challenge statements agree with round 5 after terminal-whitespace normalization.

The older workers' external statement audits and expositions were read through their reports. They were not independently reopened in this continuation and are not used as fresh proof evidence here.

## Recommended replacement for “where it stands”

OpenAI's “Strict convexity and differentiability of the planar exponential first-passage limit shape” (September 24, 2026) claims strict convexity for iid exponential weights on Z². These manuscripts do not settle the statement for arbitrary continuous laws or higher dimensions. Strict convexity is outside the release's selected Lean statements, and the bounded follow-up search found no independent proof assessment or later general solution.

## Spot check

Read rounds 3–5 REPORT.md, LOG.md, PROOF.md and their unique scripts before extending them. Their results concern the finite-cell gauge, common incoming-road gauge, and comparison-network estimates under their hypotheses. The round 5 network constant was independently rederived as `4*4+5*(4ceil(D)+5)=20ceil(D)+41`; the support bound `ceil(D)+30` follows from `D+5+20+2`. Rerunning its exact check script passed all prior cases. The earlier conditional result holds.

The selected extension is `found:lem-envelope`, especially the simultaneous physical-competitor lower bound that round 5 left open. The detailed proof is in [PROOF.md](PROOF.md). For a finite connected comparison list with M edges of expected anchor error at most kappa beta and N prescribed periods, let A be the sum of absolute anchor-error increments and D the total period defect. Interpolation gives

`e(x)=(1-theta)e_i+theta e_(i+1)+D(i,x)-theta D_i`, where `e=g-P`.

Thus every attachment-error difference is at most `A+2D` in absolute value. Every physical endpoint-corrected competitor is bounded below by `-(A+2D)`, simultaneously over all paths and endpoint occurrences. Defining its envelope from the local minimum gives a local U' with mean at most `(M kappa+2N) beta`, although the analytic dominator itself may be nonlocal. Two signed center adjustments give mean at most `(M kappa+4N) beta`, improved to 2N when both centers are marked anchors. A fixed number of corrected signed road trips and switches has an analogous local envelope; no microscopic-vertex counting is needed.

[check_envelope.py](check_envelope.py), run as `OMP_NUM_THREADS=1 nice -n 15 python3 -B check_envelope.py`, passed 2187 interpolation configurations, 54675 signed occurrence pairs, 441 independently computed shortest-path distances, 5808 physical-endpoint checks, 17424 center-adjusted checks and 480 switch coincidences. The final run took 1.002 seconds and 15.06 MiB peak RSS. The fixture's total defect `517/91` was independently counted on its unsubdivided edges as `8/7+59/13`; it is a toy value, not an FPP estimate.

Attempted failure cases included integer pauses, repeated vertices, partial-edge centers, reversed signed arms, common gauge offsets, disconnected/empty feasible families, unrestricted selected-label maxima and switches between different calibration worlds. The proof states the needed restrictions. No mathematical check failed. The manuscript's dominated calibration, gauge-tail and phase estimates, link bounds and improved-road closure remain outside this envelope result; no assessment of the full strict-convexity proof follows.

Next check: `found:lem-gauge-tail`, especially the integrated lower-concentration maximum over all vertex pairs in a box and the deterministic centering for phase-conditioned anchors.
