# T176 verification and continuation

The three candidates claim optimal full-permutation mixing for powers of two. None of their opened statements settles the row for every even deck size. The new result in this round is an independent proof and exact finite check of the tagged-flow identity in the short paper's Lean dependency chain; the continuation verdict is in [REPORT.md](REPORT.md).

## Exact theorem statements

All three author/date headers were opened in this session: author OpenAI, date September 26, 2026. The following are exact theorem/corollary environments from the freshly reopened TeX sources, including labels and notation.

### Optimal-order mixing of the Thorp shuffle

Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex), saved as [optimal.tex](sources/optimal.tex).

```tex
\begin{theorem}[Optimal-order mixing]\label{thm:mixing}
As $d\to\infty$,
\[
 \|q_d^{*(1600d)}-U_n\|_{\mathrm{TV}}\longrightarrow0.
\]
For every integer $t\ge0$,
\[
 \|q_d^{*t}-U_n\|_{\mathrm{TV}}
 \ge 1-\frac{2^{tn/2}}{n!}.
\]
Consequently the mixing time at distance $1/4$ satisfies
\[
 t_{\mathrm{mix}}(d)\ge
 \left\lceil\frac2n\log_2\frac{3n!}{4}\right\rceil
 =2d-O(1),
 \qquad t_{\mathrm{mix}}(d)=\Theta(d).
\]
\end{theorem}
```

The surrounding definitions set n=2^d and q_d to the ordinary physical shuffle. The displayed upper bound is asymptotic convergence at 1600d, not a guarantee of distance 1/4 at 1600d for every finite d. The lower bound and convergence determine Θ(d), without specifying a leading constant or cutoff.

### Compatibility entropy and the spectrum of a Thorp sweep

Opened [the introduction](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/sections/00-introduction.tex) and [author/date header](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/main.tex), saved as [compatibility.tex](sources/compatibility.tex) and [compatibility-header.tex](sources/compatibility-header.tex).

```tex
\begin{theorem}[Weighted compatibility]\label{tra:duality:weighted}\label{tra:duality:weighted-statement}
There are absolute constants $L,C_0>0$ such that the following holds. Put $m=\sqrt n$, assume $m/2\le A,D\le2m$, and take $m$ sufficiently large that $\theta=1-L/\log m>0$. For all nonnegative functions $w_i:S_D\to[0,\infty)$ and $v_k:S_A\to[0,\infty)$,
\begin{equation}\label{tra:duality:eq5}
 \frac{n!}{|R||C|}\,
 \mathbb E_U\!\left[\mathbf1_{\mathcal I}
       \prod_{i=1}^A w_i(r_i)\prod_{k=1}^D v_k(c_k)\right]
 \le e^{C_0n^{.54}}
       \prod_{i=1}^A(\mathbb E w_i^{1/\theta})^\theta
       \prod_{k=1}^D(\mathbb E v_k^{1/\theta})^\theta .
\end{equation}
The expectations on the right are uniform on the indicated symmetric groups, and logarithms are natural.
\end{theorem}
```

```tex
\begin{theorem}[A bounded regular moment]\label{tra:duality:moment}
There is an absolute finite $p_*>0$ such that, for every dyadic $n$,
\begin{equation}\label{tra:duality:eq7}
 Z_n(p_*)\le1+\frac1{16}.
\end{equation}
For every integer $M\ge p_*$, $M$ independent forward sweeps have worst-start total-variation distance at most $1/8$ from uniform.
\end{theorem}
```

```tex
\begin{corollary}[Singular ranks and full-deck mixing]\label{cor:intro-consequences}
For every nontrivial $\lambda\vdash n$ and $1\le r\le D_\lambda$,
\[
 s_r(T_{n,\lambda})\le(16D_\lambda r)^{-1/(2p_*)}.
\]
If $s_j(T_n)$ denotes the full regular singular list, including all multiplicities and zeros, then
\[
 s_j(T_n)\le j^{-1/(2p_*)}\qquad(1\le j\le n!).
\]
The constant singular value is the first value. The physical Thorp chain has worst-start $1/4$ mixing time $\Theta(d)$; more precisely its lower bound is $2d-O(1)$. For every fixed integer $M>p_*$, the worst-start total-variation distance after $Md$ physical shuffles tends to zero as $d\to\infty$.
\end{corollary}
```

The weighted-compatibility inequality is an auxiliary rectangle statement. The regular-moment theorem and final corollary are its full-deck mixing conclusions. The introduction defines n=2^d; a forward sweep has d coordinate layers and represents d physical shuffles in a rotating frame. The singular-value and moment assertions are stronger analytic quantities than TV, but their presence does not enlarge the deck-size range.

### Routing densities and representation contraction for Thorp sweeps

Opened [the introduction](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/sections/00-introduction.tex) and [author/date header](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/main.tex), saved as [routing.tex](sources/routing.tex) and [routing-header.tex](sources/routing-header.tex).

```tex
\begin{theorem}[Routing density and representation contraction]\label{fac:main}
There are absolute constants $\eta,c,C>0$ such that, with $a=1/1000$,
\[
 \log\E_{y\sim u_{N,k}}R_x(y)^{1+a}
 \le Ck(k/N)^\eta
 \qquad(1\le k\le N),
\]
uniformly over every starting injection $x$. For every sufficiently
large dyadic $N$ and every nontrivial irreducible representation,
\[
 T_N(\lambda)=0\quad\hbox{or}\quad
 \|T_N(\lambda)\|_{\op}\le D_\lambda^{-c}.
\]
Consequently an absolute number of forward sweeps has worst-start
total-variation distance from uniform tending to zero as $d\to\infty$.
\end{theorem}
```

Here N=2^d and u_(N,k) is uniform on ordered injections. R_x is the relative density for a forward/reflected pair, with \(K_N=T_N^*T_N\); T_N is the forward-sweep average operator. The final conclusion concerns independent forward sweeps and the full permutation law. The reflected density law and the forward law must not be identified. An absolute number of sweeps gives O(d) physical shuffles; the support lower bound then gives optimal order on the dyadic subsequence.

## Clause-by-clause comparison

| Our statement | What is covered | What is not covered |
| --- | --- | --- |
| Cut the n-card deck into two equal halves | The first-bit halves of n=2^d positions | Other even deck sizes are outside the definitions |
| For each corresponding pair, drop its cards in independent fair order | Physical map (b,u)→(u,b xor ξ_u), with independent pair and time coins | No change of model is needed within the dyadic range |
| Determine the order as n→∞ through even integers | Θ(log n) as n=2^d→∞ | No comparison reducing every even n to a dyadic deck is supplied |
| Total-variation mixing | Full labelled permutation against uniform on all n! orders, from every deterministic initial deck | This is more than a one-card or sparse-marginal statement |
| Determine an order of magnitude | Matching logarithmic upper/lower orders on powers of two | No exact leading asymptotic constant or cutoff; 1600d is an asymptotic sufficient clock |
| One unit is the stated physical shuffle | Each sweep costs d units | Counting a sweep as one shuffle would lose a factor d |

Thus the original literature verdict remains PARTIAL-CLAIMED: the dyadic subproblem is claimed solved; the whole all-even row is not claimed solved by these statements. The later continuation verdict in REPORT.md concerns the additional local audit, not a judgment that a complete preprint proof is correct.

## Follow-ups opened in this round

The initial follow-up search was limited to five minutes; its queries and timing are recorded in [LOG.md](LOG.md). It found no later all-even solution, Thorp-specific refutation, referee report, named expert validation, or separate arXiv version of these three OpenAI manuscripts. This is a bounded search result, not proof that none exists.

- [OpenAI repository history](https://github.com/openai/math/blob/main/history.md), also opened as raw text. Its last displayed entry is October 29, 2026; no Thorp correction or withdrawal is listed.
- [Yunjiang Jiang, A subquadratic upper bound for the mixing time of the Thorp shuffle, arXiv:2610.18884](https://arxiv.org/abs/2610.18884). Opened the arXiv page: v1 October 3, 2026, n=2^d, worst-start full-deck TV bound of order d^(5/3). It is the result already in the row, not a new all-even solution.
- [Yunjiang Jiang, Adhesive riffle shuffles: one-parameter models and mixing bounds, arXiv:2611.02092](https://arxiv.org/abs/2611.02092). Opened the arXiv page: v1 November 1, 2026. Its models are adhesive riffles and interpolation, rather than the unchanged Thorp chain. It predates the earlier reports.
- [Ilya Mironov, Mixing Time of the Random-Pair Monte Shuffle, arXiv:2611.03959](https://arxiv.org/abs/2611.03959). Opened the arXiv page: v1 November 2, 2026. It studies public random-pair schedules and expected conditional TV, a different transition model and quantity. It also predates the earlier reports.
- [Family 238 Lean scope note](https://github.com/openai/math/blob/main/lean/docs/238.md), opened through both web and read-only GitHub fetch; saved as [lean-scope-238.md](sources/lean-scope-238.md). It states that the headline dyadic result is formalized. For Compatibility, its selected scope excludes the bounded regular-moment and moment/rank conclusions; for Routing, it covers nine earlier statements and excludes changed later statements and six other result blocks.
- [Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/Main.lean), reopened and saved as [Main.lean](sources/Main.lean). Its full_mixing endpoint is 1600d, with a logarithmic-order theorem for the 2^d-card model. [ConditionalLaw](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/ConditionalLaw.lean) and [MaskedResampling](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/MaskedResampling.lean) were reopened and match round 5's saved bodies.

The exact import graph and other Lean bodies were read from round 5's snapshots, not newly fetched wholesale. A queue traversal and independent acyclicity check reproduce its 51-module Main closure and 55 saved modules in total. This is source inspection; no Lean kernel build, Comparator run, or compiler/dependency axiom audit was performed. Previous rounds' additional community and exposition reads remain recorded in their folders and are not presented as new opens here. Search snippets alone are not cited as papers read.

## Recommended replacement for “where it stands” (three sentences)

OpenAI's unrefereed preprint “Optimal-order mixing of the Thorp shuffle” (September 26, 2026) claims Θ(log n) full-deck TV mixing for n=2^d, with vanishing error after 1600d physical shuffles, and provides Lean sources for this dyadic result. The same release's “Compatibility entropy and the spectrum of a Thorp sweep” and “Routing densities and representation contraction for Thorp sweeps” (both September 26, 2026) also claim optimal order for powers of two. These claims do not settle the problem for all even n, and the complete proofs have not been certified by this verification.

## Spot check

The ONE extension chosen in this round is the tagged-flow link in MaskedResampling and ConditionalLaw, used to pass a centered flow-energy estimate to fixed-list marginal tests. [PROOF.md](PROOF.md) proves its one-step masked resampling identity, iteration for arbitrary signed raw weights, centering at a tag, and the bound by sqrt(N times expected energy). A second argument conditions on full exposed path cylinders when the exposed list fills the complement of the free set.

The resampling mask must be fixed by the past and must contain only pairs with two free inputs. Exposed points outside the free set then see exactly the same switch under original and resampled coins. The proof does not assert that the resampled array is independent of the original exposed endpoints.

[check_conditional.py](check_conditional.py) checks all basis weights and joint endpoint indicators for every free set on 2 and 4 cards at times 0–4, every free set on 8 cards at time 2, and eight specified sets on 8 cards at time 3. [check-output.json](check-output.json) reports 103,884 history/set cases and 2,536,256 exact equalities, with zero error; five independent full-path grouping tests also pass. Counterexamples to two invalid variants give expectations 1 versus 1/2 when an exposed point is free, and probability 1/4 for a supposedly fair coin when the mask depends on its current coin.

Round 5's balancing estimate, constants and import-graph result survive the independent recheck. This round finds no defect in the tagged-flow link. The rotating-half reindexing and its use in opposite-half factorization remain unchecked independently, as do the complete representation chain and a pinned Lean/Comparator build.
