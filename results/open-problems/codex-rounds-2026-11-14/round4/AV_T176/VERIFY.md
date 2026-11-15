# T176: verification and continuation

Verification date: 15 November 2026. The literature verdict remains PARTIAL-CLAIMED for powers of two only. The continuation result in REPORT.md is a local check of the remaining representation-theoretic completion, recorded in PROOF.md; it is not a judgment certifying the full proofs.

## Exact manuscript statements

All three manuscripts name the author **OpenAI** and the date **September 26, 2026**. Their current author/date main files and relevant theorem source files were opened directly through the read-only GitHub connector and saved here. Quotations below reproduce the theorem environments verbatim.

### Optimal-order mixing of the Thorp shuffle

Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex), saved as [optimal-source.tex](optimal-source.tex). Here n=2^d, q_d is one physical shuffle, U_n is uniform on S_n, and the mixing threshold is 1/4.

```latex
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

The theorem claims the full order Θ(log n) along powers of two, together with vanishing full-permutation TV error after 1600d physical shuffles. It does not give an asymptotic equivalent, an optimal leading constant, or cutoff. The introduction explicitly excludes the corresponding arbitrary-even question.

### Compatibility entropy and the spectrum of a Thorp sweep

Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/main.tex) and [sections/00-introduction.tex](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/sections/00-introduction.tex), saved as [compatibility-main-source.tex](compatibility-main-source.tex) and [compatibility-source.tex](compatibility-source.tex).

For weighted compatibility, R=(S_D)^A and C=(S_A)^D, n=AD, and U is the product of independent uniform row and column permutations. Compatibility means that the row-then-column permutation can also be written in column-then-row order, equivalently the indicated original-column images are distinct. For the moment theorem, n=2^d, T_n is one forward coordinate sweep, and Z_n(p) is its regular singular moment, including multiplicities: sum over λ of D_λ Tr[(T*_{n,λ}T_{n,λ})^p].

```latex
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

\begin{theorem}[A bounded regular moment]\label{tra:duality:moment}
There is an absolute finite $p_*>0$ such that, for every dyadic $n$,
\begin{equation}\label{tra:duality:eq7}
 Z_n(p_*)\le1+\frac1{16}.
\end{equation}
For every integer $M\ge p_*$, $M$ independent forward sweeps have worst-start total-variation distance at most $1/8$ from uniform.
\end{theorem}

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

The first theorem's balanced rectangles have auxiliary generality; they do not yield a mixing theorem for arbitrary even decks. The moment theorem and corollary explicitly claim full-deck, worst-start, physical Thorp mixing for dyadic sizes. A sweep costs d physical shuffles. Repetition of forward sweeps, rather than only a reflected chain, appears in the conclusion.

### Routing densities and representation contraction for Thorp sweeps

Opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/main.tex) and [sections/00-introduction.tex](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/sections/00-introduction.tex), saved as [routing-main-source.tex](routing-main-source.tex) and [routing-source.tex](routing-source.tex).

Here N=2^d, T_N averages a forward sweep, K_N=T_N* T_N is a sweep and its reflection with fresh coins, u_{N,k} is uniform on ordered k-injections, and R_x(y)=(N)_k Pr_{K_N}(x→y). D_λ is the irreducible degree. Exact main statement:

```latex
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

Its density assertion is an auxiliary reflected-pair estimate, but its final conclusion concerns full-permutation mixing by forward sweeps. Together with the support lower bound in the introduction it claims Θ(d) physical mixing for N=2^d, not just partial-card mixing. No arbitrary-even upper estimate is claimed.

## Clause-by-clause comparison with our row

| Our statement | Opened claims |
| --- | --- |
| “The Thorp shuffle” | Same physical cut-and-interleave model. In binary coordinates the map is (x_1,u) → (u,x_1+ξ_u). |
| “on a deck of n cards (n even)” | Full-deck mixing conclusions require n=2^d. Other even sizes are not covered. |
| “cuts the deck into two halves of n/2 cards” | The first bit selects the half; u selects the corresponding place within it. Exact match for dyadic decks. |
| “for each k=1,…,n/2” | There is exactly one corresponding pair for each binary word u of length d−1. |
| “drops the k-th cards … in an order decided by an independent fair coin” | Each ξ_u is independent and fair, with independent arrays at later steps. Exact match. |
| “Determine the order of magnitude” | Claimed upper O(d) plus lower Ω(d), hence Θ(log n) on powers of two. This is the requested strength on that subsequence. |
| “of its total-variation mixing time” | Full law on S_n, TV=half the absolute-mass sum, from the worst deterministic initial deck. Not merely a one-card or marginal metric. |
| “as n→∞” | The upper limit is restricted to n=2^d. No reduction covering all even n is supplied. |

For each fixed 0<ε<1, vanishing-TV upper bounds imply O_ε(log n), and the support count implies Ω_ε(log n), on the dyadic subsequence. Restriction to a subsequence prevents the claims from settling the entire row. Padding the deck or changing the switching network would need a separate argument preserving the stated chain.

## Follow-up search and opened record

The initial follow-up search was bounded to five minutes. Exact queries and outcomes are in LOG.md; absence findings are bounded search results.

- Opened the repository's [history.md](https://raw.githubusercontent.com/openai/math/main/history.md). Its latest listed entry is October 29, 2026; no Thorp correction or withdrawal is listed.
- Opened [Yunjiang Jiang, A subquadratic upper bound for the mixing time of the Thorp shuffle, arXiv:2610.18884](https://arxiv.org/abs/2610.18884). It still lists submission on October 3, 2026 and the dyadic subquadratic upper estimate from our row. This is a distinct paper, not an arXiv version of an OpenAI candidate.
- Opened the repository [issues page](https://github.com/openai/math/issues). No Thorp-specific correction surfaced in this pass; this is not an exhaustive issue-history audit.
- Reopened the repository's [family 238 Lean scope note](https://github.com/openai/math/blob/main/lean/docs/238.md), saved as [lean-scope-238.md](lean-scope-238.md). It claims formalization of the main dyadic 1600d conclusion and reciprocal-degree/eight-block support. For Compatibility it explicitly excludes the bounded regular-moment and moment/rank conclusions from that selected formalization. For Routing it describes nine earlier statements, requires J>2s for a conditional height estimate, and excludes changed later statements and six other blocks.
- Reopened [ThorpShuffle/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/Main.lean), saved as [lean-thorp-main.lean](lean-thorp-main.lean). It explicitly states convergence of distance d (1600*d) and a mixing-time order theorem. This session did not run Lean, inspect every imported definition, or audit all dependencies.

Read both earlier sessions' records. Their opened expositions, later citations, constant-improvement notes, statement audits and distinctions between challenges and solutions are preserved in the [first VERIFY.md](~/codex_op_1114/briefs/AV_T176/VERIFY.md) and [round 3 VERIFY.md](~/codex_op_1114r3/briefs/AV_T176/VERIFY.md). Those are inherited records, not papers newly opened in this session. No later all-even solution, arXiv version of an OpenAI candidate, named expert proof review, referee report or refutation was found in the brief current search.

## Recommended “where it stands” sentence

OpenAI's AI-generated preprint “Optimal-order mixing of the Thorp shuffle” (September 26, 2026), together with its same-date companions “Compatibility entropy and the spectrum of a Thorp sweep” and “Routing densities and representation contraction for Thorp sweeps”, claims total-variation mixing time Θ(log n) for n a power of two. The repository reports a Lean formalization of the main dyadic statement; this verification does not certify the complete proofs. These claims do not determine the order for arbitrary even n, so the full row remains open on the evidence checked here.

## Spot check

The single new check is the short paper's representation-theoretic completion, centered on Lemma 5.1. [PROOF.md](PROOF.md) gives an explicit finite-s majorant for the reciprocal-degree sum excluding the row and column, verifies the tableau constructions in each shape range, and takes the limits in a specified order. It then traces this bound through common trimming and the eight-block orbit estimate into the final eight-factor Fourier/sign comparison.

The explicit conditional estimate is
\[
\|q_d^{*(1600d)}-U\|_{\mathrm{TV}}
\le128\varepsilon_n+\tfrac12
\sqrt{(32C_1)^8R(n)
+\{16\varepsilon_n/(1-16\varepsilon_n)\}^{16}}\to0,
\]
for sufficiently large dyadic n, where R(n) is the reciprocal-degree sum excluding trivial and sign, and ε_n is Proposition 4.2's averaged-marginal bound. The previous calculation was independently rechecked first. No defect was found in these local steps, including the parity correction after trimming; no all-even argument, numerical value for C_1, complete formal check, or independent certification of the whole theorem is supplied.

Task: “Verify: has open problem T176 been settled by the OpenAI math release?” — 15 November 2026, approximately 04:24 Asia/Tbilisi at session start; exact receipt time unavailable.

