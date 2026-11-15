# T176: literature verification and Lean source audit

The opened claims cover the ordinary Thorp shuffle on n=2^d cards. They do not determine the order for every even n. This continuation independently rechecks round 4 and audits the dyadic Lean model and completion; it does not assess the complete preprint as correct.

The continuation verdict required by the latest instructions is in REPORT.md. Under the original literature-verification vocabulary, the scope result remains PARTIAL-CLAIMED: optimal order on powers of two only.

## Exact manuscript statements

All three manuscripts name their author as **OpenAI** and their date as **September 26, 2026**. The following are exact TeX environments from the newly opened sources, including labels and notation; the companion theorem environments do not by themselves define their notation, so the model and quantity are described afterward.

### Optimal-order mixing of the Thorp shuffle

Opened [the manuscript source](https://github.com/openai/math/blob/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex); saved as [optimal.tex](sources/optimal.tex).

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

The surrounding definitions set n=2^d and q_d equal to one physical shuffle, with positions represented by binary strings and the map (b,u) → (u,b xor ξ_u). The invariant law U_n is uniform on all n! permutations. The introduction explicitly says that the arbitrary-even question is not addressed. The upper assertion is convergence at 1600d as d tends to infinity, not a numerical guarantee for every finite d; combined with the lower bound it determines an order, not a leading asymptotic constant or cutoff.

### Compatibility entropy and the spectrum of a Thorp sweep

Opened [the introduction and theorem statements](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/sections/00-introduction.tex) and its [author/date source](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/main.tex); saved as [compatibility.tex](sources/compatibility.tex) and [compatibility-header.tex](sources/compatibility-header.tex).

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

The weighted-compatibility theorem is an auxiliary inequality for balanced rectangles, not the shuffle-mixing statement by itself. The regular-moment theorem and corollary apply to the dyadic deck n=2^d defined in the introduction. A forward sweep consists of d coordinate matching layers; at a sweep endpoint it is d physical shuffles, with the deterministic frame restored. Thus the corollary claims full-deck worst-start TV mixing of order d, and vanishing error after any fixed integer M>p_* sweeps. Its singular-value and moment estimates are stronger quantities than TV, but do not extend the range of n.

### Routing densities and representation contraction for Thorp sweeps

Opened [the introduction and theorem](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/sections/00-introduction.tex) and its [author/date source](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/main.tex); saved as [routing.tex](sources/routing.tex) and [routing-header.tex](sources/routing-header.tex).

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

Here N=2^d; x is a starting injection, u_(N,k) is the uniform ordered-injection law, and R_x is the density of the reflected-pair routing law defined in the introduction. T_N is the forward-sweep Fourier operator. The density statement and forward-sweep statement concern different laws, connected by the paper's claimed argument; the last sentence is the full-deck mixing consequence. An absolute number of sweeps means O(d) physical steps. This is again an optimal-order dyadic claim after the support lower bound, not a result for arbitrary even N.

## Comparison with our statement

| Our clause | What the three candidates claim | Remaining difference |
| --- | --- | --- |
| Cut the deck into equal halves | Binary first-bit halves of a dyadic deck | Same physical operation in the covered range |
| Independently decide each corresponding pair's order by a fair coin | One fresh bit ξ_u for every pair and time | Same model; no card-by-card single-position substitute |
| n even, tending to infinity | n=2^d (or N=2^d), with d tending to infinity | Non-powers of two are absent |
| Total-variation mixing time | Full permutation, uniform law, every initial deck | Same quantity; companions also state stronger spectral or moment bounds |
| Determine its order of magnitude | Upper O(d), lower 2d-O(1), hence Θ(d)=Θ(log n) | Determines the order on the dyadic subsequence only |
| General asymptotic statement | The upper constant works asymptotically, with finite-d mixing existence separately | No leading constant, cutoff, or universal finite-d 1600d assertion is implied |

No implication from dyadic decks to arbitrary even decks is supplied by the opened statements. Padding a deck or taking a subsequence would require an additional comparison of transition laws and errors; it cannot be assumed.

## Follow-ups actually opened

The bounded later-literature search used the web search tool before the source audit. It found no solution of the all-even problem or Thorp-specific refutation. This is a limited search outcome, not a proof of absence. It found no development after round 4 that changes the scope verdict.

1. [Yunjiang Jiang, A subquadratic upper bound for the mixing time of the Thorp shuffle, arXiv:2610.18884](https://arxiv.org/abs/2610.18884). Opened the arXiv page, which lists v1 submitted 3 October 2026. Its full-deck bound is the dyadic d^(5/3) bound already in our row; it does not supply an all-even result.
2. [OpenAI repository history](https://github.com/openai/math/blob/main/history.md). Opened; the displayed history has no Thorp-specific correction or withdrawal. General corrections to other families do not validate this one.
3. [OpenAI repository issues page](https://github.com/openai/math/issues). Opened. This page and the bounded search supplied no Thorp error report; the landing page is not an exhaustive issue-by-issue review.
4. [Community manuscript entry, updated November 4](https://mathcommunity.github.io/oai-math-revised/papers/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/). Opened as a discovery record. Its human notes section is empty and its collected notes are expressly unreviewed and AI-generated. It lists constant-improvement remarks, a cutoff agenda and expositions; none is adopted here as validation.
5. The community links to [acprk's R5 directory](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R5-thorp-24d) and [R25 directory](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R25-swapornot-cu-constants) failed to open in this session (robots/cache errors). These failures are recorded; the remarks' proofs and constants are not cited as checked. The earlier session did open resolved files, as its LOG.md records.
6. [cert-machine statement audit at its linked pinned revision](https://raw.githubusercontent.com/carlostoledo1891/cert-machine/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json). Opened. It describes its activity as statement reading, not a proof certificate. This session does not convert that description into expert or referee approval.
7. [OpenAI's family 238 Lean scope note](https://github.com/openai/math/blob/main/lean/docs/238.md). Opened and saved as [lean-scope-238.md](sources/lean-scope-238.md). It states dyadic full-deck convergence at 1600d. Its selected Compatibility formalization excludes bounded regular moments and moment/rank conclusions; its Routing formalization covers nine earlier statements and excludes changed later statements and six other result blocks.
8. [Lean README](https://github.com/openai/math/blob/main/lean/README.md) and the two challenge files [ThorpRemaining](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpRemaining.lean) and [ThorpFirstReciprocal](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThorpFirstReciprocal.lean). Opened. Challenge theorem placeholders are intentional and distinct from the proof sources. The guessed root formalization.yaml did not exist; no inference is made from that failure.
9. The actual solution [ThorpShuffle/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/Main.lean), its 51-module OAI dependency closure, and four additional FirstMain modules were fetched and saved. The [manifest](sources/MANIFEST.md) records every module and direct import. No local Lean or Comparator run was performed, and Mathlib/compiler/tactic internals were not audited.

Earlier sessions opened further papers and expositions. They remain documented in their folders; this list distinguishes what was opened again here. No referee report, named expert endorsement, or independently run formal certificate was obtained in this session.

## New source-audit result

Main imports EightBlocks and states convergence of distance(d,1600d) to zero and an IsTheta(log(2^d)) mixing-time theorem. Model defines full permutations, uniform independent time/pair coins, the physical map of the question and ordinary TV. The complete OAI import closure contains 51 modules, with Mathlib as its only outside import; there is no import cycle. A lexical scan found no literal sorry, admit, axiom or unsafe in the 55 fetched solution modules. This is source inspection, not kernel certification.

The route to Main differs from a literal transcription of the short paper. It uses inverse-square reciprocal degrees and an operator contraction of order D^(-1/4), enough for eight factors, whereas the separate FirstMain branch proves the paper's first-power reciprocal and D^(-5/16) estimate. It also uses a fixed-list marginal estimate; the paper's checked Proposition 4.2 averages over a random input list. These differences are compatible with the scalar completion, and the fixed-list branch has a separate initial balancing step; neither should be silently substituted for the other.

The detailed conditional derivation, constants 98, 3136 and 96^8, parity treatment, clock conversion and boundaries are in [PROOF.md](PROOF.md). The full chain of representation and conditional-flow proofs has not been independently re-proved here.

## Recommended replacement for “where it stands” (three sentences)

OpenAI's unrefereed preprint “Optimal-order mixing of the Thorp shuffle” (September 26, 2026) claims that the full shuffle on n=2^d cards mixes in Θ(log n) physical shuffles, with vanishing total-variation error after 1600d steps, and supplies Lean sources for this dyadic result. The same release's “Compatibility entropy and the spectrum of a Thorp sweep” and “Routing densities and representation contraction for Thorp sweeps” (both September 26, 2026) also claim optimal-order mixing for powers of two. These claims do not cover all even deck sizes, so the row as stated remains open in the sources checked here; the complete preprint proofs have not been certified by this verification.

## Spot check

The load-bearing preparation lemma pair_both_half_balance in FreshCoins is checked in PROOF.md, Section 6. For any deterministic set of m free positions, one shuffle puts at least m/4 free positions in each prepared half except with probability at most 2(9/10)^m. The local generating-function factors are exactly 1, 881/1000 and 16/25 for empty, singly free and doubly free pairs; an independent centered-binomial tail bound confirms the result.

This explains why the actual Lean endpoint can use a fixed input list without supposing its initial free set is uniform. It is a local source-level check, with the remaining conditional-flow and representation dependencies explicitly left outside the certification claim.

