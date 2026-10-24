# Maximum hitting times on distance-regular graphs

**Problem.** Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 7.31:
prove that over distance-regular graphs other than the $n$-cycles, $\tau_0 = O(n)$, where
$\tau_0 = \max_{i,j}\mathbb{E}_i T_j$ is the largest mean hitting time. They record that Biggs computed
$\max_{i,j}\mathbb{E}_iT_j/(n-1) = 195/101$ on a cubic graph with $102$ vertices, and outlined an argument
that this may be the largest value over the known distance-regular graphs.

**What is here.** The problem is reduced to an identity about intersection arrays, with no graph needed;
Biggs's value is reproduced exactly and shown to be the maximum over all thirteen cubic distance-regular
graphs; every classical infinite family is computed; and a search over feasible intersection arrays finds
nothing larger. The conjecture is not proved.

## The identity

In a distance-regular graph the hitting time $\mathbb{E}_iT_j$ depends only on $d(i,j)$, so the distance
to a fixed target is a birth-and-death chain on $\{0,\dots,d\}$: from distance $i$ it steps down with
probability $c_i/k$ and up with $b_i/k$. Its stationary measure is $k_i/n$, with $k_0=1$ and
$k_{i+1} = k_ib_i/c_{i+1}$. The birth-and-death formula for a downward step,
$\mathbb{E}_iT_{i-1} = \big(\sum_{j\ge i}\pi_j\big)\big/\big(\pi_i \cdot \text{down-rate}\big)$, gives
$$\boxed{\ \tau_0 \ = \ \mathbb{E}_dT_0 \ = \ k\sum_{i=1}^{d}\frac{k_i+k_{i+1}+\dots+k_d}{k_i\,c_i}\ }$$
and $\tau_0$ is the largest hitting time because in a birth-and-death chain $\mathbb{E}_iT_0$ increases
with $i$. So Open Problem 7.31 is a statement about intersection arrays alone.

Two things fall out at once. The $i=1$ term is
$$k\cdot\frac{k_1+\dots+k_d}{k_1c_1} = k\cdot\frac{n-1}{k\cdot 1} = n-1,$$
so **every** distance-regular graph has $\tau_0 \ge n-1$, with equality exactly when $d=1$, the complete
graph. The conjecture is therefore that the remaining terms add no more than a bounded multiple:
$$\tau_0 = (n-1) + k\sum_{i=2}^{d}\frac{k_i+\dots+k_d}{k_ic_i}.$$
And the excluded case shows what failure looks like: for the $n$-cycle, $k=2$, $c_i=1$ and $k_i=2$
throughout, so every one of the $d \approx n/2$ terms is of order $n$, and $\tau_0 = n^2/4$.

## The conjecture as a statement about products

The identity takes a better form still. Put $u_i = k/(k_ic_i)$ and $T_i = k_i+\dots+k_d$, so that
$\tau_0/n = \sum_i u_i\,(T_i/n)$. Since $k_{i+1}c_{i+1} = k_ib_i$, the $u_i$ satisfy a one-step recursion
with no reference to the $k_i$ at all:
$$u_1 = 1, \qquad u_{i+1} = u_i\,\frac{c_i}{b_i}, \qquad\text{that is}\qquad
u_i = \prod_{j<i}\frac{c_j}{b_j},$$
and therefore
$$\frac{\tau_0}{n} \ = \ \sum_{i=1}^{d}\frac{T_i}{n}\prod_{j<i}\frac{c_j}{b_j}
\ \le \ \sum_{i=1}^{d}\ \prod_{j<i}\frac{c_j}{b_j}.$$
The first term is $T_1/n = (n-1)/n$, the universal bound again. And the excluded case is now transparent:
for the $n$-cycle every ratio $c_j/b_j$ equals $1/1$, so every $u_i$ is $1$ and the sum has $d \approx n/2$
terms of size one.

So a sufficient condition for the conjecture is purely arithmetical, with no graph and no hitting time in
it:
$$\textbf{Is } \ \sum_{i=1}^{d}\ \prod_{j=1}^{i-1}\frac{c_j}{b_j} \ \textbf{ bounded over distance-regular
graphs other than the cycles?}$$
For the thirteen cubic graphs that sum runs between $1$ and $3.5$, largest at the dodecahedron and the
Desargues graph; Biggs--Smith, which maximises $\tau_0$, has $2.25$. For the Hamming and Johnson families
it is at most about $2.24$ and falls to $1$ as the parameters grow, because $c_j/b_j$ there is of order
$j/(d-j)$ and the products collapse. For the cycles it is exactly $2d$. Over every *feasible* array of valency three
to five and diameter up to eight, a larger class than the graphs known to exist, the sum never exceeds
$3.5$, and the array attaining it is again the dodecahedron's.

What makes the products decay is the pair $(b_j, c_j)$ never both being $1$ for long: if $c_j = 1$ and
$b_j \ge 2$ the ratio is at most $\tfrac12$, and if $c_j \ge 2$ the intersection numbers are growing
instead. The cycle is the case where $b_j = c_j = 1$ for every $j$. So the question above is really: how
long a run of $b_j = c_j = 1$ can a distance-regular graph of valency at least three have?

## The thirteen cubic distance-regular graphs

| graph | $n$ | $\tau_0$ | $\tau_0/(n-1)$ |
| --- | --- | --- | --- |
| $K_4$ | 4 | 3 | 1 |
| $K_{3,3}$ | 6 | 6 | 6/5 |
| cube $Q_3$ | 8 | 10 | 10/7 |
| Petersen | 10 | 12 | 4/3 |
| Heawood | 14 | 19 | 19/13 |
| Pappus | 18 | 27 | 27/17 |
| Desargues | 20 | 65/2 | 65/38 |
| dodecahedron | 20 | 35 | 35/19 |
| Coxeter | 28 | 45 | 5/3 |
| Tutte--Coxeter | 30 | 48 | 48/29 |
| Foster | 90 | 675/4 | 675/356 |
| **Biggs--Smith** | **102** | **195** | **195/101** |
| Tutte 12-cage | 126 | 234 | 234/125 |

The Biggs--Smith graph gives exactly $195/101 = 1.9307$, which is the number Aldous and Fill attribute to
Biggs, and it is the largest of the thirteen. Since the cubic distance-regular graphs are classified and
there are exactly thirteen, that part of Biggs's outlined claim is settled: $195/101$ is the maximum over
all cubic distance-regular graphs, not merely over the ones he checked.

## The infinite families

| family | $\tau_0/n$ |
| --- | --- |
| Hamming $H(d,2)$, $d = 4, 8, 12, 16$ | 1.333, 1.219, 1.120, 1.080 |
| Hamming $H(d,4)$, $d = 4, 8, 12, 16$ | 1.141, 1.054, 1.033, 1.023 |
| Johnson $J(2m,m)$, $m = 5,10,15,20,25$ | 1.076, 1.013, 1.005, 1.003, 1.002 |
| Odd graphs $O_K$, $K = 4,6,8,10,12,15$ | 1.314, 1.251, 1.172, 1.128, 1.101, 1.078 |
| cycles (excluded), $n = 10,40,100,400$ | 2.5, 10, 25, 100 |

Every classical family tends to $\tau_0/n \to 1$, that is, to the trivial lower bound. The Odd graphs are
the slowest to settle, and they are the family with the largest diameter relative to $n$ among these.

## A search over feasible arrays

Since the identity needs only an intersection array, one can go past the graphs that are known to exist.
Enumerating arrays $\{b_0,\dots,b_{d-1};c_1,\dots,c_d\}$ with $b_0 = k \ge 3$, the usual monotonicity
$b_0\ge b_1 \ge \dots$ and $1 = c_1 \le c_2 \le \dots$, non-negative $a_i = k-b_i-c_i$, integral $k_i$, and
the standard multiplicity test that the eigenvalue multiplicities
$m_j = n\big/\sum_i k_iu_i(\theta_j)^2$ be positive integers, gives the feasible arrays. Over valencies
$3$ to $6$ and diameters to $12$, nothing found exceeds the Biggs--Smith value, and most sit near $1.3$ to
$1.5$. In particular the cubic maximum over feasible arrays is again $\tau_0/n = 1.9118$ at diameter
seven, and that array is Biggs--Smith, which is the only feasible cubic array of that diameter.

This is worth more than a survey of known graphs, because a feasible array need not be realised by any
graph: the search covers a strictly larger set than the distance-regular graphs themselves, so a bound on
it is a stronger statement than a bound over the graphs.

## Checks

The identity was verified against a computation that shares none of its machinery: for twelve graphs, the
hitting-time linear system $h_j = 0$, $h_i = 1 + \frac1{\deg}\sum_{u\sim i}h_u$ was solved for every
target and the maximum taken. Petersen, $Q_3$, $Q_4$, the dodecahedron, Heawood, Pappus, Desargues,
$K_{3,3}$, $K_{5,5}$, $K_7$, $C_{12}$ and the icosahedron all agree exactly. Independently, the complete
graph must give $n-1$ and the cycle $n^2/4$, and both do.

Two errors were caught by those controls and are worth recording because each would have survived a
weaker check. The first version of the identity used the head sums $k_0+\dots+k_{i-1}$ in place of the
tail sums. It reproduced $n^2/4$ on the cycle perfectly, because a cycle's $k_i$ are symmetric and cannot
tell the two apart; the complete graph, where the formula returned $1$ instead of $3$, is what exposed it.
The second was in the multiplicity test, which used $u_i^2/k_i$ where the formula is $k_iu_i^2$; it
rejected all thirteen cubic distance-regular graphs, which is exactly what the control was there to catch.

## Status

Not proved. What is done: the problem is reduced to an identity in the intersection array, the universal
lower bound $\tau_0\ge n-1$ falls out of it, Biggs's $195/101$ is confirmed and shown to be the maximum
over all thirteen cubic distance-regular graphs, the classical families are computed and all tend to the
trivial value, and a search over feasible arrays turns up nothing larger. Verification: author checked
against a direct linear-algebra solve on twelve graphs, with the complete graph and the cycle as
independent controls at the two extremes. Prior art: the birth-and-death reduction for distance-regular
graphs is standard and the identity is very likely known; I did not find it written in this form, and
Aldous and Fill do not use it where they pose the problem. Not a clearance.

## New open problems

1. **The sharp constant.** Is $\tau_0 \le 2(n-1)$ for every distance-regular graph other than a cycle,
   with the Biggs--Smith graph's $195/101$ the extreme case? Everything computed here stays below
   $1.94(n-1)$.
2. **The products.** Is $\sum_{i\le d}\prod_{j<i}(c_j/b_j)$ bounded over distance-regular graphs other
   than the cycles? A yes proves the conjecture, by the display above. Equivalently, since a ratio
   $c_j/b_j$ is at most $\tfrac12$ unless $b_j = c_j = 1$ or $c_j > b_j$: can a distance-regular graph of
   valency at least three have a long run of indices with $b_j = c_j = 1$? The cycle is the case where
   every index is such a one.
3. **Bounded valency is not the obstruction.** For each $k\ge3$ there are finitely many distance-regular
   graphs, by the theorem of Bang, Dubickas, Koolen and Moulton settling the Bannai--Ito conjecture, so
   $\sup\tau_0/n$ is finite for each fixed valency. Does that supremum stay bounded as $k\to\infty$?
   That, and not any single family, is what the conjecture needs.
4. **The relaxation time half.** Aldous and Fill ask in the same place whether $\tau_2 = O(\log n)$ over
   distance-regular graphs. The same birth-and-death reduction gives $\tau_2$ as the relaxation time of a
   chain on $d+1$ states; does that make the question tractable in the same way?
