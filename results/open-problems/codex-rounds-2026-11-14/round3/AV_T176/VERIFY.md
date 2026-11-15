# T176 continuation verification

Checked 15 November 2026 (Asia/Tbilisi). The earlier worker's report was dated 14 November. This record distinguishes manuscript claims from the local calculation checked in this session.

## Outcome

The earlier scope verdict holds: PARTIAL-CLAIMED for n = 2^d. All three candidates claim optimal-order full-permutation total-variation mixing in physical shuffles for that subsequence. None of their quoted conclusions covers all even n.

The new check is the conditional-flow input to the short paper's Fourier transfer, through its averaged ordered-marginal proposition. Its complete local derivation is in [PROOF.md](PROOF.md). No defect was found there; this is not a judgment that the complete preprint or its formalization is correct.

## 1. Optimal-order mixing of the Thorp shuffle

Author on the paper: OpenAI. Date: September 26, 2026. Opened the actual [build/main.tex](https://github.com/openai/math/blob/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex) through read-only GitHub fetch; saved as [optimal-main.tex](optimal-main.tex).

Exact main theorem:

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

The preceding definitions set n = 2^d, q_d to the law of a complete physical shuffle, U_n to uniform on S_n, and the mixing threshold to 1/4. Its model maps (x_1,u) to (u,x_1+xi_u), with independent fair bits for corresponding pairs. Thus this is exactly our cut-and-interleave model on dyadic decks, and the quantity is the full permutation law, rather than a one-card law.

The upper statement is vanishing TV at 1600d; together with the support bound it claims order Θ(log n). It does not give an asymptotic equivalent, leading constant, or cutoff. Our question asks only for order, so these finer issues do not limit coverage on powers of two. The text explicitly says that the corresponding optimal-order question for arbitrary even deck sizes is not addressed by its cube argument.

## 2. Compatibility entropy and the spectrum of a Thorp sweep

Author: OpenAI. Date: September 26, 2026, checked in the opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/main.tex). Opened the actual [introduction source](https://github.com/openai/math/blob/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/build/sections/00-introduction.tex), saved as [compatibility-introduction.tex](compatibility-introduction.tex).

Exact main results and mixing corollary:

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
```

```latex
\begin{theorem}[A bounded regular moment]\label{tra:duality:moment}
There is an absolute finite $p_*>0$ such that, for every dyadic $n$,
\begin{equation}\label{tra:duality:eq7}
 Z_n(p_*)\le1+\frac1{16}.
\end{equation}
For every integer $M\ge p_*$, $M$ independent forward sweeps have worst-start total-variation distance at most $1/8$ from uniform.
\end{theorem}
```

```latex
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

Here n = 2^d for the physical shuffle, T_n is a forward coordinate sweep, and one sweep costs d physical shuffles. Z_n(p) is the ordinary regular trace of (T_n* T_n)^p, including the irreducible multiplicity D_lambda. The weighted compatibility theorem concerns balanced rectangles with n=AD, R=(S_D)^A and C=(S_A)^D; compatibility means that row-then-column routing admits the opposite-order factorization. Its broader rectangular range is an auxiliary combinatorial statement, not an arbitrary-even physical mixing theorem.

The corollary explicitly returns to full-deck worst-start TV and physical time, with Θ(d) mixing for powers of two. The intermediate reflected operator does not change the stated final chain into a different shuffle. Neither the statement nor the definition supplies the all-even extension.

## 3. Routing densities and representation contraction for Thorp sweeps

Author: OpenAI. Date: September 26, 2026, checked in the opened [build/main.tex](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/main.tex). Opened its actual [introduction source](https://github.com/openai/math/blob/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/build/sections/00-introduction.tex), saved as [routing-introduction.tex](routing-introduction.tex).

Exact main theorem:

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

The introduction sets N=2^d. T_N is a forward sweep, K_N=T_N* T_N a sweep followed by reflection with fresh coins, and R_x(y)=(N)_k Pr_K(x -> y) is the density for an ordered k-card injection relative to its uniform law. D_lambda is an irreducible dimension.

The first estimate concerns a reflected pair and possibly partial-card laws. The final sentence nevertheless claims full-permutation worst-start TV mixing in an absolute number of forward sweeps. Because one sweep is d physical shuffles, the introduction combines this with the support lower bound to claim Θ(log N) physical mixing. This covers the same dyadic part of our row, without covering arbitrary even N.

## Clause-by-clause comparison

| Our statement | Scope actually claimed |
| --- | --- |
| “The Thorp shuffle” | Same independent corresponding-pair cut-and-interleave chain. The deterministic coordinate rotation is a change of frame. |
| “on a deck of n cards (n even)” | Physical mixing conclusions only for n=2^d. |
| “cuts the deck into two halves of n/2 cards” | The first bit selects the half and u identifies the corresponding position. |
| “for each k = 1, …, n/2” | One switch per u, with 2^(d-1)=n/2 such switches. |
| “order decided by an independent fair coin” | Independent fair switches, refreshed every step. |
| “order of magnitude” | A matching upper and lower order Θ(log n), not merely an improved polylogarithmic upper bound, along powers of two. |
| “total-variation mixing time” | Full permutation law, worst deterministic start, threshold 1/4; vanishing-TV upper claims imply the corresponding bound for each fixed positive error. |
| “as n → ∞” | The limit is restricted to n=2^d. No all-even reduction is stated. |

The upper estimate on one subsequence does not bound other even deck sizes. No padding or monotonicity reduction preserving the ordinary full-deck chain is provided.

## Follow-ups opened in this continuation

The brief search was limited to the initial literature pass. Queries and failed fetches are recorded in LOG.md. No follow-up found in that pass postdated the earlier report or changed its verdict; this is a bounded search result, not a proof that no other discussion exists.

- Opened the repository's [history.md](https://github.com/openai/math/blob/main/history.md). Its latest listed entry is October 29, 2026. No Thorp-specific withdrawal, repair, or extension appears there.
- Opened [Ilya Mironov, Mixing Time of the Random-Pair Monte Shuffle, arXiv:2611.03959](https://arxiv.org/abs/2611.03959). The page still lists v1, submitted November 2, 2026. Its theorem concerns a public random-pair schedule and expected conditional TV, with leading time 2n log n; it does not solve the all-even Thorp question. The earlier worker had already opened this item.
- Opened [Yunjiang Jiang, Adhesive riffle shuffles: one-parameter models and mixing bounds, arXiv:2611.02092](https://arxiv.org/abs/2611.02092). The page lists v1, submitted November 1, 2026. Its abstract treats adhesive riffle, interpolation and correlated-label models, not optimal mixing of the ordinary Thorp chain. This additional bibliographic lead does not change the picture.
- Reopened [family 238 Lean scope](https://github.com/openai/math/blob/main/lean/docs/238.md), saved as [lean-scope-238.md](lean-scope-238.md). It reports the main dyadic 1600d statement and the support lower bound as formalized. For Compatibility it explicitly excludes the bounded regular-moment and other moment/rank conclusions. For Routing it identifies nine earlier statements, requires J>2s for one high-height estimate, and excludes changed later statements and six other blocks.
- Reopened [ThorpShuffle/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/ThorpShuffle/Main.lean) and [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml). The former explicitly states convergence of distance d (1600*d); the catalogue has a document-level review status of unchecked. This is not a separate review judgment on each entry. No Lean build, dependency audit or Comparator run was performed.

The earlier worker's additional opened expositions, constant-improvement notes, community pages and statement audit are documented in its [VERIFY.md](~/codex_op_1114/briefs/AV_T176/VERIFY.md). They were read as previous-session records, not represented here as newly opened web papers. No arXiv version of the three OpenAI candidates, named expert proof review, referee report, or refutation of their mixing conclusion was found in the continuation search.

## Recommended replacement for “where it stands”

OpenAI's AI-generated preprint “Optimal-order mixing of the Thorp shuffle” (September 26, 2026), and its same-date companions “Compatibility entropy and the spectrum of a Thorp sweep” and “Routing densities and representation contraction for Thorp sweeps”, claim total-variation mixing time Θ(log n) for n a power of two. The repository reports a Lean formalization of the main dyadic statement, but this record does not certify the complete proofs. The claims do not determine the order for arbitrary even n, so they do not settle our full row.

## Spot check

New beyond the earlier report: checked Sections 3–4 of the short paper through Proposition 4.2. The detailed check in [PROOF.md](PROOF.md) derives the path-cylinder conditioning law, the energy identity E_t=sum_(j=1)^d 2^(-j)b_(t-j), the opposite-half factorization, and b_s <= (15/16)E_s+2exp(-n/256). It then derives E_t <= (31/32)^(t-2d)+32exp(-n/256), and hence the displayed averaged ordered-marginal bound at 200d.

Load-bearing constants were derived twice where possible: the noise norm by direct spreading and repeated norm halving; the decay base from the geometric sum and its characteristic equation; and the power-of-n decay by an integral logarithm bound and an exact binomial inequality. The argument survives checks of future conditioning, both exposed endpoints sharing an edge, arbitrary bad-event/energy correlation, m=n, m=1, d=1 and t=2d+1. The random-list averaging cannot be dropped.

The earlier Fourier-transfer calculation was also re-derived independently: each isotypic orbit has dimension at most (dim pi)^2 even with multiplicity; the exponent is (3/8-1)/2=-5/16 and the squared constant is 4*8*C_1=32C_1. Neither that recheck nor the present flow check establishes Lemma 5.1, the complete group comparison, any companion theorem, or an all-even extension.

