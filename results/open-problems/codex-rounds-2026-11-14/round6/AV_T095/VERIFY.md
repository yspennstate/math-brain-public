# T095 verification, round 6

Literature verdict: PARTIAL-CLAIMED for positive Gamma laws, including exponential weights. No candidate claims the whole continuous-law differentiability statement. REPORT.md uses the later continuation verdict format; this round checks a further conditional reduction, without judging the full preprint correct.

## Exact main statements

The actual introduction source of each candidate was reopened this round, together with its build/main.tex author/date metadata. All three name OpenAI as author. The current repository snapshot returned by the latest-commit API is still `4eaee87548250b2682affda7d05d947c05554bae` (30 October 2026).

### Strict convexity and differentiability of the planar exponential first-passage limit shape — September 24, 2026

[Actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex), preserved as [source-exponential-introduction.tex](source-exponential-introduction.tex). Both headline theorems, verbatim:

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

[Actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex), preserved as [source-no-bigeodesics-introduction.tex](source-no-bigeodesics-introduction.tex). Verbatim:

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

[Actual introduction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/sections/01-introduction.tex), preserved as [source-qaoa-introduction.tex](source-qaoa-introduction.tex). Verbatim:

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

## Clause-by-clause comparison

| T095 requirement | Shape candidate | No-bigeodesics candidate | QAOA candidate |
| --- | --- | --- | --- |
| Undirected nearest-neighbor FPP | Same model | Same model | SK spin glass and quantum circuits |
| Z² | Same dimension | Same dimension | No lattice FPP limit shape |
| iid nonnegative edge weights | Common Gamma/exponential law; positive almost surely | Same general nonnegative iid setup | Different random inputs |
| Every continuous law | Only Gamma(κ,λ), κ,λ>0, including κ=1 exponential | Nonatomic law, matching this range | No corresponding law quantifier |
| E[min(τ₁,…,τ₄)²]<∞ | Automatic on the claimed subclass: min²≤τ₁² and E[τ₁²]=κ(κ+1)/λ² | Exactly the minimum-of-four condition | Not applicable |
| Boundary differentiable at every point | Claimed everywhere; Fréchet differentiability away from 0 and C¹ boundary have the required strength | Absence of doubly infinite geodesics, a different conclusion | An optimized energy limit as circuit depth tends to infinity |
| All qualifying laws | Not claimed | Matching laws, different quantity | Unrelated |

Uniform[1,2] is a concrete law inside T095 and outside the Gamma family: its minimum squared is at most 4 and its support is bounded. The shape statement is therefore a special case of the row, not its whole law quantifier. Exponential strict convexity is an additional claim, not asserted for all Gamma laws. No implication from the no-bigeodesics statement to universal differentiability was established here.

## Follow-ups actually opened

The first brief update search used the exact shape title, first-passage differentiability with OpenAI/2026/November/error, and the exact folder name with error. It found no later full-law resolution, same-title arXiv version, specific refutation, or expert/referee assessment changing the preceding record. This is a bounded negative search finding.

| Opened source | What it establishes and its limit |
| --- | --- |
| [Repository history](https://github.com/openai/math/blob/main/history.md) | No FPP withdrawal or repair notice in the page. This does not exclude criticism elsewhere. |
| [Latest-commit API](https://api.github.com/repos/openai/math/commits?per_page=1) | Still the October 30 snapshot named above. |
| Scott Armstrong and Ahmed Bou-Rabee, [*Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124](https://arxiv.org/abs/2610.42124) | Abstract reopened. It is a continuum fluctuation result, not the universal lattice differentiability theorem. No full-text recheck this round. |
| [Official Lean scope note](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/212.md), preserved as [source-lean-scope.md](source-lean-scope.md) | Describes positive-Gamma differentiability and excludes strict convexity from the selected statements. No local Lean compilation or full dependency check. |
| [Actual witness section](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/differentiability/witnesses.tex), preserved as [source-witnesses.tex](source-witnesses.tex) | Reopened for the new spot check below; unchanged mathematically from round 5. |
| J. van den Berg and H. Kesten, [*Inequalities with applications to percolation and reliability*](https://sites.math.northwestern.edu/~auffing/papers/vBK.pdf), Journal of Applied Probability 22 (1985), 556–569 | Original PDF opened, Section 3: the finite monotone Bernoulli BK input and its iteration. This is a prerequisite, not a post-preprint follow-up. |
| Richard Arratia, Skip Garibaldi and Alfred W. Hales, [*The van den Berg–Kesten–Reimer operator and inequality for infinite spaces*, arXiv:1508.05337](https://arxiv.org/html/1508.05337), Bernoulli 24 (2018), 433–448 | Abstract and full HTML opened, particularly Section 5 on multiple events. General nonmonotone BKR need not be treated as associative; the proof here supplies the monotone recursion directly. Also a prerequisite. |

Round 5's saved MathVet and Carlos Toledo/cert-machine records were read as inherited reports, not reopened or rerun. Their reported selected-statement acceptance is not new validation obtained this round. No conclusion about the full Lean dependency chain is added.

## Earlier result independently rechecked

The round 5 audit was rerun unchanged: `OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/AV_T095/audit.py`. It passes 723 paths, 3,222 chunks, 559,764 subpath intervals and independent greedy/DP packing checks. Runtime 6.335 seconds, peak RSS 17,743,872 bytes, actual nice 20.

A second derivation gives H(Q)≥−a−2aM_Q with a=ηs: each threshold-stopped prefix loses at most 2a and the suffix at most a. The cheap-full-chunk implication supplies H(Q)≥a when M_Q=0; for M_Q≥1, −a−2aM_Q≥a−4aM_Q. Summing full chunks and the remainder yields H(P)≥(N−1)a−4aM_tot, with disjoint edge witnesses even when indices repeat. The earlier claim holds within its stated hypotheses.

## Spot check

The single extension is the probabilistic link from those extracted witnesses to a uniform long-path lower bound: `df:wi:continuous-bk` and `df:wi:long-paths`. The all-case argument is in [PROOF.md](PROOF.md), with exact finite checks in [audit.py](audit.py).

Upper dyadic Gamma-quantile rounding decreases to the original weights. Strict path inequalities eventually hold at a common finite precision for any realizing finite witness list. Disjoint edge supports give disjoint bit certificates; complementing the bits and applying finite monotone BK bounds repeated lists by the product of their event probabilities. No spatial independence between the test boxes is used.

Low defect forces more than N/8−1/4 witnesses, so floor(N/16) can be retained for N≥16. At most 49^N deterministic itineraries and binom(N+t,t)≤4^N positional allocations cover every path-dependent list, including repeated labels. This gives P(B_N)≤196^N p^floor(N/16), with p=2q₀. The manuscript's scale condition implies 196p^(1/16)<49/200<1, so Borel–Cantelli yields the claimed simultaneous eventual lower bound. No failure was found in this reduction under the earlier rare-event and extraction inputs; this is not verification of the full preprint.

The finite audit result and resource measurements are recorded in [LOG.md](LOG.md). It checks actual path-support disjointness against a separate truth-table bit-certificate oracle; the latter may give a strictly larger event, so only containment is used. It also checks weak compositions independently by dynamic programming and the floor/exponent constants with rational arithmetic.

## Recommended replacement for “where it stands”

OpenAI's preprint *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026) claims differentiability everywhere for every Gamma law with positive shape and rate, including exponential weights. Its selected Lean statements cover Gamma differentiability, while exponential strict convexity is outside their scope. The general continuous-law statement under the Cox–Durrett minimum-of-four moment condition is outside these claims, and no later resolution was located in the bounded update search.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 09:52 Asia/Tbilisi.
