# P0253 — is the antivoter variance maximised by the complete graph? (Aldous–Fill, Chapter 14)

**Status: NOT settled. Three exact identities PROVED (one of them a strict generalisation of
the monograph's Corollary 14.24), a spectral upper bound PROVED and shown to be tight exactly
at $K_n$ and therefore incapable of settling the question by itself, and the conjecture
VERIFIED EXHAUSTIVELY over every admissible regular graph on $n \le 9$ vertices plus
high-degree families up to $n = 16$. No counterexample. The problem stays open.**

## The problem, from the source

Aldous and Fill, Chapter 14 §14.4, verbatim from
`https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch14.S4.html`:

> Implicit in the proof are a corollary and an open problem. The open problem is to show that
> var $S$ is in fact maximized on the complete graph. This might perhaps be provable by
> sharpening the inequality in (14.22).
>
> **Corollary 14.24** On an edge-transitive graph, write
> $c_{\text{edge}} = c(v,w) = E\eta_v\eta_w$ for an arbitrary edge $(v,w)$. Then
> var $S = n(1+c_{\text{edge}})/2$, $c_{\text{edge}} < 0$.

The antivoter chain (Matloff 1977; Donnelly and Welsh 1984): on an $n$-vertex $r$-regular
graph, each vertex $i$ carries a spin $\eta_i \in \{\pm1\}$; at each step choose a vertex $i$
uniformly and a neighbour $j$ of $i$ uniformly and set $\eta_i \leftarrow -\eta_j$. Assuming
$G$ is neither bipartite nor an $n$-cycle, the $2^n - 2$ non-constant configurations form one
irreducible class and carry the unique stationary law. $S = \sum_i \eta_i$; $E_\pi S = 0$ by
the global flip symmetry, so var $S = E_\pi S^2$. The definition is quoted verbatim in Rinott
and Rotar, *Ann. Appl. Probab.* 7 (1997) 1080–1105, §1.3.

## Machinery, and the controls it passed

`code/antivoter.py` computes everything exactly over the rationals by two independent routes.

**Route A, brute force.** Build the $2^n-2$ state transition matrix, solve $\pi P = \pi$
exactly, read off var $S$ and every $E_\pi[\eta_i\eta_j]$.

**Route B, duality.** $E_\pi[\eta_i\eta_j] = E[(-1)^{\tau_{ij}}]$, where $\tau_{ij}$ is the
number of steps taken by the annihilating pair walk started with particles at $i$ and $j$
(each step: pick one of the two particles uniformly, move it to a uniform neighbour; annihilate
on collision). This is a special case of Donnelly and Welsh (1984), Theorem 1. It gives a
linear system in $\binom{n}{2}$ unknowns,

$$g(i,j) = -\frac{1}{2r}\Big[\sum_{k \sim i} g(k,j) + \sum_{l \sim j} g(i,l)\Big], \qquad g(x,x) := 1,$$

which is what makes $n$ up to 20 or so computable at all.

Controls, all exact: on $K_4$, $K_5$, $C_5$, the prism and $K_6$, routes A and B agree on
**every** pair correlation and on var $S$, and $E_\pi S = 0$ exactly. And $K_n$ returns
$n(n-2)/(2n-3)$: $8/5$, $15/7$, $8/3$, $35/11$, $48/13$, $21/5$ for $n = 4,\dots,9$.

## Three identities

Write $\bar c$ for the mean of $E_\pi[\eta_i\eta_j]$ over directed edges, $\bar p$ for the mean
of $P_\pi(\eta_i = \eta_j)$ over directed edges, and $\bar q$ for the mean of
$P_\pi(\eta_j = \eta_k)$ over ordered pairs $(j,k)$, $j \ne k$, with a common neighbour
(weighted by the number of common neighbours — i.e. over the $nr(r-1)$ "cherries").

**(I) Corollary 14.24 without edge-transitivity.**
$$\operatorname{var} S \;=\; \frac n2\,(1+\bar c) \;=\; n\,\bar p .$$

*Proof.* One step of the chain replaces $\eta_i$ by $-\eta_j$ for a uniform directed edge
$(i,j)$ independent of the current configuration, so $S' = S - \eta_i - \eta_j$ and
$S'^2 = S^2 - 2S(\eta_i+\eta_j) + (\eta_i+\eta_j)^2$. In stationarity $E S'^2 = E S^2$, so
$$0 = -2E[S(\eta_i+\eta_j)] + E[(\eta_i+\eta_j)^2].$$
Now $E[(\eta_i+\eta_j)^2] = 2 + 2\bar c$, and summing over the directed edges,
$\sum_{i}\sum_{j\sim i} E[S\eta_i] = r\,E[S^2]$ and likewise
$\sum_{i}\sum_{j \sim i} E[S\eta_j] = \sum_j \deg(j) E[S\eta_j] = r E[S^2]$, so
$E[S(\eta_i+\eta_j)] = 2E[S^2]/n$. Hence $4E[S^2]/n = 2+2\bar c$. $\square$

Aldous and Fill state this only for edge-transitive graphs, where $\bar c = c_{\text{edge}}$.
The averaged form holds for every regular graph and is what makes the extremal problem a
question about one number, $\bar c$. (Rinott and Rotar quote the equivalent
var $U = (EQ + rn)/(2r)$ "from Aldous and Fill (1994)"; the derivation above is independent.)

**(II) The cherry identity.**
$$\bar p \;=\; \Big(1-\frac1r\Big)\,\big(1-\bar q\big), \qquad\text{so}\qquad
\operatorname{var} S = n\Big(1-\frac1r\Big)(1-\bar q).$$

*Proof.* $\bar p = P(\tau \text{ even})$ for the annihilating pair walk from a uniform directed
edge. From an adjacent pair the first step annihilates with probability exactly $1/r$; if it
does not, the new pair is $\{k,j\}$ with $k \sim i$, $k \ne j$ (or the mirror image), and since
$j \sim i$ too, the new pair is a cherry pair, distributed exactly as the cherry average. And
$\tau$ is even iff the first step does not annihilate and the remaining time is odd. $\square$

Both identities were checked as assertions inside every single graph computed in the searches
below — every admissible regular graph on $n \le 9$ vertices — and never failed.

**(III) A spectral upper bound.** Let $\lambda_2$ be the second largest adjacency eigenvalue.
Then
$$\boxed{\ \operatorname{var} S \;\le\; \frac{n^2(r+\lambda_2)}{2rn - r + \lambda_2}\ }$$
with equality of the *bound* and the complete-graph value exactly when $G = K_n$.

*Proof.* Let $G_{\mathrm{corr}} = E_\pi[\eta\eta^{\mathsf T}] \succeq 0$, with unit diagonal, and
$V = \mathbf 1^{\mathsf T} G_{\mathrm{corr}} \mathbf 1 = \operatorname{var} S$. Then
$\operatorname{tr}(AG_{\mathrm{corr}}) = nr\bar c = r(2V-n)$ by (I). Split
$A = r uu^{\mathsf T} + A'$ with $u = \mathbf 1/\sqrt n$, so $A' = PAP$ for $P = I - uu^{\mathsf T}$
and $A'$ has eigenvalues $\lambda_2 \ge \dots \ge \lambda_n$ on $\mathbf 1^\perp$. Then
$\operatorname{tr}(A G_{\mathrm{corr}}) = rV/n + \operatorname{tr}(A\,PG_{\mathrm{corr}}P) \le
rV/n + \lambda_2(n - V/n)$, because $PG_{\mathrm{corr}}P \succeq 0$ and
$\operatorname{tr} PG_{\mathrm{corr}}P = n - V/n$. Rearranging gives the bound (the denominator
is positive since $\lambda_2 \ge -r$ and $2rn - 2r > 0$). $\square$

For $K_n$ ($r = n-1$, $\lambda_2 = -1$) the bound is $n(n-2)/(2n-3)$: exactly the true value.

**And that is why this bound cannot settle the problem.** Subtracting, the bound exceeds
$n(n-2)/(2n-3)$ by a positive multiple of $r + (n-1)\lambda_2$; and for a connected regular
graph $\sum_{k \ge 2}\lambda_k = -r$ forces $\lambda_2 \ge -r/(n-1)$, with equality only when
the graph has two distinct eigenvalues, i.e. only for $K_n$. So the spectral bound is $\ge$ the
conjectured maximum for *every* graph, with equality only at the conjectured maximiser. It is
tight where you want it and useless everywhere else: a natural first relaxation of this
problem is provably not strong enough.

## What the exhaustive search says

`code/anti_search.py` enumerates **all labelled $r$-regular graphs** on $n$ vertices by
recursive degree-constrained edge assignment, filters to connected, non-bipartite, $r \ge 3$
(the source's admissibility convention), reduces to isomorphism classes by bucketing on
(adjacency spectrum, triangle count) and then running VF2 *within* each bucket — so two
non-isomorphic graphs are never merged — and computes var $S$ exactly for each class.

| $n$ | admissible classes | max var $S$ | $K_n$ value | verdict |
|---|---|---|---|---|
| 5 | 1 | 15/7 | 15/7 | $K_n$ |
| 6 | 3 | 8/3 | 8/3 | $K_n$ strictly |
| 7 | 3 | 35/11 | 35/11 | $K_n$ strictly |
| 8 | 14 | 48/13 | 48/13 | $K_n$ strictly |
| 9 | 21 | 21/5 | 21/5 | $K_n$ strictly |

(Validation of the enumerator: it finds 16 connected 4-regular graphs on 9 vertices, the known
count.) The runner-up is always $r = n-2$, the cocktail-party graph $K_{n \times 2}$, and the
ordering of the top few is monotone in $r$ — larger degree, larger variance.

Two closed forms fall out and match the search exactly. For complete multipartite
$K_{m \times k}$ ($n = mk$, $r = n-k$), the distance chain of the pair walk is a three-state
birth-and-death chain and

$$c_{\text{edge}} = -\frac{1}{2n-4k+1}, \qquad
\operatorname{var} S = \frac n2\Big(1 - \frac{1}{2n-4k+1}\Big),$$

which is decreasing in $k$: $k=1$ is $K_n$ with $-1/(2n-3)$, $k=2$ is the cocktail-party graph
with $-1/(2n-7)$. So within this family $K_n$ wins, for the reason that a larger $r$ dilutes
the edge anticorrelation.

Targeted high-degree search (`code/anti_highdeg.py`), complements of $d$-regular graphs for
$d = 1,2,3$ at $n$ up to 16 — the only regime where the margin is small — found no graph above
$K_n$; the closest competitor at $n = 12$ falls short by 0.067 against $K_{12}$'s $5.714$.

## A parity reformulation

Combining (I) with the duality: with $\tau$ the annihilation time of the pair walk started from
a **uniform directed edge**, and $\varphi(z) = E[z^\tau]$ its probability generating function,

$$\bar c = \varphi(-1), \qquad \operatorname{var} S = \frac n2\big(1+\varphi(-1)\big),$$

so **P0253 is exactly the statement**
$$\varphi_G(-1) \;\le\; -\frac{1}{2n-3}\quad\text{for every admissible } r\text{-regular } G,
\ \text{with equality iff } G = K_n .$$

On $K_n$ the pair walk annihilates at each step with probability exactly $1/(n-1)$, so
$\tau \sim \mathrm{Geom}(1/(n-1))$, $\varphi(z) = pz/(1-qz)$ and $\varphi(-1) = -p/(1+q) =
-1/(2n-3)$ — the extremal value is the generating function of a geometric law at $-1$. In
operator form, $\varphi(-1) = -\langle u, (I+K)^{-1}a\rangle$ with $K$ the substochastic kernel
of the pair walk on ordered distinct pairs, $a$ its one-step absorption vector and $u$ the
uniform directed-edge law; the conjecture is
$\langle u, (I+K)^{-1}a\rangle \ge 1/(2n-3)$.

This is a parity statement about an absorbing walk, with no reference to the $2^n$-state spin
chain. It is the form in which the $K_n$ value is transparent, and the natural starting point
for a proof.

The monograph's own suggestion is to sharpen its inequality (14.22),
$\sum_{l\ge2}\frac{(-1)^l}{l-1}P(Z+Z^-=l) = \int_{-1}^0 \varphi^2(z)z^{-2}\,dz > 0$. Cauchy–Schwarz
on the unit-length interval gives $\int_{-1}^0 (\varphi(z)/z)^2 dz \ge \big(E[(-1)^{Z+1}/Z]\big)^2$,
which on a geometric law of mean $\sim n$ is $\approx (\log 2)^2/n^2 = 0.48/n^2$ against the
$\approx 0.5/n^2$ the conjecture needs — within four percent, but on the wrong side. The book's $Z$ is not pinned down here precisely
enough to claim this as a measurement of its route; the reformulation above is the verified
statement.

## Literature check (2026-09-13)

Searched: "antivoter model stationary variance regular graph complete graph maximize Aldous
Fill"; "antivoter model Donnelly Welsh variance d-regular stationary". Found: Matloff (1977),
Donnelly and Welsh (1984), Rinott and Rotar (1997) — which addresses the *other* half of the
same passage, the asymptotic normality of $S$, and quotes the variance identity from Aldous and
Fill without addressing which graph maximises it — and Aldous and Fill's own text. Rinott (2004,
IMS Lecture Notes, *The stationary distribution in the antivoter model: exact sampling and
approximations*) treats sampling, not the extremal problem. **No source found that settles or
even states progress on "var $S$ is maximised on the complete graph".** Recorded as a negative
search.

## Remaining obligation

Everything. What is established here is: the identity that reduces the problem to one scalar
$\bar c$ for all regular graphs (not only edge-transitive ones); a cherry recursion for that
scalar; a spectral certificate that is tight at the conjectured optimum and provably slack
everywhere else; an exhaustive verification to $n = 9$; and a parity reformulation. What is
missing is any argument that rules out a large sparse graph with anomalously weak edge
anticorrelation. The cherry identity localises what such a graph would need:
$\bar q \le 1 - \frac{r}{r-1}\cdot\frac{n-2}{2n-3}$, so a cubic counterexample would need mean
agreement probability below about $1/4$ at cherry distance, i.e. mean correlation below $-1/2$
between vertices two steps apart. Every graph computed here has $\bar q$ between $0.43$ and
$0.53$. A proof that $\bar q \ge \frac12 - O(1/r)$ for all admissible graphs would finish the
problem; no such proof is known.
