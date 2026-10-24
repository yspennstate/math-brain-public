# P0157 — four-hub exclusion and an exact three-hub witness count in the stress family

**Scope.** This is a self-contained HARD7-04 route result for the explicit finite-third-moment barely-subcritical configuration-model family introduced in `p0157_multihub_route_refutation.md`. It does **not** solve van der Hofstad's full crossover problem. It proves one half of the latest checkpoint's concrete boundary target: with high probability no connected component contains four of the designated hubs. It also replaces the heuristic three-hub first-moment calculation by an exact actual-configuration-model witness count whose expectation grows linearly. The remaining gap is a second-moment/overlap argument proving that at least one such three-hub witness exists with high probability.

## 1. The family and notation

Let `m` tend to infinity through even positive integers and put

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

\[
x=3m^{11}+\frac{m^5}{4}(m^2-1)^2,
\]

\[
N_d=M,\qquad N_3=2m^{12}-x,\qquad N_1=6m^{12}+x-M.
\]

The total number of half-edges is

\[
\ell
=\frac{m^5}{2}\left(24m^7-12m^6-m^4+4m^2-3\right)
\sim 12m^{12}.
\tag{1.1}
\]

Write

\[
\delta
=1-\frac{\sum_v d_v(d_v-1)}{\ell}
=\frac{12m^{11}}{\ell}
\sim \frac1m.
\tag{1.2}
\]

The `M` vertices of degree `d` are called **hubs**. All non-hub vertices have degree `1` or `3`.

A useful exact bulk continuation ratio is

\[
q:=\frac{6N_3}{\ell}.
\tag{1.3}
\]

Since

\[
\ell\delta
=\ell-\{6N_3+d(d-1)M\},
\]

we have the exact identity

\[
1-q=\delta+\frac{d(d-1)M}{\ell}.
\tag{1.4}
\]

Consequently

\[
q<1-\delta,\qquad m(1-q)\longrightarrow1.
\tag{1.5}
\]

Indeed the second term in (1.4) is \(O(m^{-3})\), whereas \(\delta\sim m^{-1}\).

The frozen HARD7-04 local fluctuation metric remains

\[
Q_m=\frac{\sigma_m^2}{d\delta}
=m^{-1}+O(m^{-2})\to0.
\tag{1.6}
\]

Nothing below changes this scalar.

---

## 2. B4: a complete weaker theorem — four hubs never merge whp

### Theorem 2.1

For the configuration model with degree sequence above,

\[
\boxed{
\mathbb P\{\exists\text{ a connected component containing at least four hubs}\}
=O(m^{-1})\longrightarrow0.
}
\tag{2.1}
\]

Thus the heuristic `k=4` boundary from the preceding rank-one surrogate is a genuine theorem in the actual configuration model.

### Proof

We separate unusually long hub explorations from short connecting trees.

### 2.1 A uniform hub-exploration truncation

Explore the component of a fixed hub `h` by pairing active half-edges. Let `A_s` be the number of active half-edges after `s` pairing steps, and let `tau_h` be the number of pairing steps until the active set is empty.

Before the stopping time, the conditional active-half-edge increment is at most the size-biased average of `d_v-2` over unseen vertices. The full degree sequence satisfies

\[
\sum_v d_v(d_v-2)
=\sum_v d_v(d_v-1)-\ell
=-\ell\delta.
\tag{2.2}
\]

After at most `s` vertices have been removed from the unseen set, this numerator can increase by at most `s`, because

\[
d(d-2)\ge-1
\]

for every nonnegative integer degree `d`. Hence for

\[
s\le \frac{\ell\delta}{4}
\]

the remaining numerator is at most \(-3\ell\delta/4\). Pairing to an already active half-edge only makes the increment more negative. Therefore, while \(s<\tau_h\wedge \ell\delta/4\),

\[
\mathbb E[A_{s+1}-A_s\mid\mathcal F_s]\le-\frac{\delta}{2}
\tag{2.3}
\]

for all sufficiently large `m`.

Set

\[
R=\left\lfloor\frac{\ell\delta}{64}\right\rfloor.
\tag{2.4}
\]

For large `m`, \(R\ge\ell\delta/128\) and \(R<\ell\delta/4\). Optional stopping at
\(\tau_h\wedge R\), starting from \(A_0=d\), gives

\[
0\le \mathbb E A_{\tau_h\wedge R}
\le d-\frac{\delta}{2}\mathbb E(\tau_h\wedge R),
\]

and therefore

\[
\mathbb E(\tau_h\wedge R)\le\frac{2d}{\delta}.
\tag{2.5}
\]

Markov's inequality yields

\[
\mathbb P(\tau_h>R)
\le
\frac{2d}{\delta R}
\le
\frac{256d}{\ell\delta^2}.
\tag{2.6}
\]

There are `M` hubs, so

\[
\mathbb P\{\exists h:\tau_h>R\}
\le
\frac{256Md}{\ell\delta^2}
=O(m^{-3}).
\tag{2.7}
\]

Call the complement of this event `G`.

### 2.2 Suppress degree-two vertices in a minimal four-hub tree

Assume `G` and suppose a component contains at least four hubs. Starting the component exploration at any one of its hubs exposes the whole component in at most `R` pairing steps. Choose a spanning tree of the component and then its minimal subtree containing **all** hubs of that component. Repeatedly delete one leaf hub and then prune any newly created **non-hub** leaves until every leaf is again a hub; stop as soon as four hub vertices remain. Each round removes exactly one hub, because the cleanup stops when it reaches another hub. The resulting connected tree has at most `R` edges, contains exactly four hubs, and has no omitted hub hidden in the interior.

It has no non-hub leaves. Every non-hub internal vertex has original degree `3` and tree degree either `2` or `3`. Suppress all non-hub tree-degree-two vertices. The resulting **core** is a tree with

- exactly four labeled hub vertices (some may be internal in the core);
- `t` labeled non-hub branch vertices, every one of core degree exactly `3`.

If the core has `L` edges then

\[
L=3+t.
\tag{2.8}
\]

The sum of the core degrees at the four hubs is

\[
2L-3t=6-t.
\tag{2.9}
\]

Since all four hubs have positive core degree, (2.9) forces

\[
t\le2.
\tag{2.10}
\]

The exact finite Prüfer enumeration archived with this result gives the number `C_t` of labeled core trees:

\[
\boxed{C_0=16,\qquad C_1=12,\qquad C_2=6,\qquad C_3=0.}
\tag{2.11}
\]

The checker is `p0157_core_topologies_exact.py`; its executed output ends `ALL_EXACT_CHECKS_PASS = True`.

### 2.3 Count short embedded trees

Fix `t in {0,1,2}` and a labeled core topology. Write \(s_e\ge0\) for the number of suppressed degree-three vertices placed on core edge `e`, and let

\[
s=\sum_{e=1}^{L}s_e.
\]

The full tree then has \(L+s\le R\) edges.

For a uniform perfect matching on `ell` half-edges, the probability that any fixed set of `r` disjoint prescribed pairs occurs is exactly

\[
\frac1{D_r},
\qquad
D_r:=(\ell-1)(\ell-3)\cdots(\ell-(2r-1)).
\tag{2.12}
\]

Since \(r\le R\),

\[
D_r\ge \{\ell(1-\delta/32)\}^{r}.
\tag{2.13}
\]

Put

\[
a:=1-\delta/32.
\]

For a fixed core and a fixed composition \((s_e)\), an upper bound for the number of stub embeddings is

\[
M^4\,d^{6-t}\,N_3^{t+s}\,6^{t+s}.
\tag{2.14}
\]

Here each branch or suppressed bulk vertex contributes at most `(3)_3=6` or `(3)_2=6`, while the total hub core degree is \(6-t\).

For a fixed total `s`, there are

\[
\binom{s+L-1}{L-1}
\]

compositions over the `L` core edges. Hence the expected number of short embedded connecting trees with `t` branch vertices is at most

\[
C_t
\frac{M^4d^{6-t}(6N_3)^t}{(\ell a)^{3+t}}
\sum_{s\ge0}
\binom{s+L-1}{L-1}
\left(\frac{6N_3}{\ell a}\right)^s.
\tag{2.15}
\]

We have extended the sum beyond the original cutoff \(L+s\le R\), which only enlarges it.

By (1.5),

\[
\frac{6N_3}{\ell a}
=\frac q a
\le
\frac{1-\delta}{1-\delta/32}
\le1-\frac{\delta}{2},
\tag{2.16}
\]

because

\[
(1-\delta/2)(1-\delta/32)-(1-\delta)
=\frac{15}{32}\delta+\frac1{64}\delta^2>0.
\]

The negative-binomial identity now gives

\[
\sum_{s\ge0}
\binom{s+L-1}{L-1}
\left(\frac q a\right)^s
=
(1-q/a)^{-L}
\le
(2/\delta)^L.
\tag{2.17}
\]

Also \((6N_3/(\ell a))^t\le1\). Thus (2.15) is bounded by

\[
C_t\,
\frac{M^4d^{6-t}}{(\ell a)^3}
\left(\frac2\delta\right)^{3+t}.
\tag{2.18}
\]

Using

\[
M=m^5,\qquad d=m^2,\qquad \ell\asymp m^{12},\qquad \delta\asymp m^{-1},
\]

the three cases have orders

\[
t=0:\ O(m^{-1}),\qquad
t=1:\ O(m^{-2}),\qquad
t=2:\ O(m^{-3}).
\tag{2.19}
\]

Therefore the probability, on `G`, that any component contains four hubs is \(O(m^{-1})\) by Markov. Adding the long-exploration probability (2.7) proves (2.1). `QED`

---

## 3. B10: remove the surrogate — an exact actual-CM three-hub witness family

The previous checkpoint predicted that three-hub trees should be abundant, but that calculation treated the marked-hub graph as an independent rank-one surrogate. We now replace it by a concrete family of source-model pairing events.

For distinct ordered hubs `(a,b,c)`, and integers

\[
m\le r,s\le2m,
\]

define a **V-witness** to be two internally vertex-disjoint simple paths:

- a path of length `r` from `a` to `b`;
- a path of length `s` from `a` to `c`;

whose internal vertices are all distinct degree-three vertices.

Let `Z_m` count all such ordered V-witnesses, with their actual half-edge embeddings.

### Proposition 3.1 — exact expectation and asymptotic

\[
\boxed{
\mathbb EZ_m
=(M)_3\,d^3(d-1)
\sum_{r=m}^{2m}\sum_{s=m}^{2m}
\frac{(N_3)_{r+s-2}\,6^{r+s-2}}
{D_{r+s}},
}
\tag{3.1}
\]

where `D_k` is defined in (2.12). Moreover

\[
\boxed{
\mathbb EZ_m
\sim
\frac{(e^{-1}-e^{-2})^2}{144}\,m
=0.0003755332\ldots\,m
\longrightarrow\infty.
}
\tag{3.2}
\]

### Proof

Choose the ordered central hub and two ordered leaf hubs in `(M)_3` ways. At the central hub choose two distinct half-edges, and at each leaf choose one, giving

\[
(d)_2d^2=d^3(d-1)
\]

choices. There are \(r+s-2\) internal degree-three vertices. Ordering distinct choices along the two paths gives \((N_3)_{r+s-2}\) possibilities, and each such internal vertex contributes `(3)_2=6` choices of incident half-edges. The union is a tree with exactly \(r+s\) prescribed matching pairs, whose probability is \(D_{r+s}^{-1}\). This proves the exact formula (3.1).

Uniformly for \(m\le r,s\le2m\),

\[
\frac{(N_3)_{r+s-2}}{N_3^{r+s-2}}
=1+O(m^2/N_3)=1+o(1),
\tag{3.3}
\]

and

\[
\frac{D_{r+s}}{\ell^{r+s}}
=1+O(m^2/\ell)=1+o(1).
\tag{3.4}
\]

Therefore, with \(q=6N_3/\ell\),

\[
\mathbb EZ_m
\sim
\frac{M^3d^4}{\ell^2}
\left(\sum_{r=m}^{2m}q^{r-1}\right)^2.
\tag{3.5}
\]

From (1.4), \(m(1-q)\to1\), so

\[
q^m\to e^{-1},
\qquad
q^{2m}\to e^{-2},
\]

and the geometric sum satisfies

\[
\sum_{r=m}^{2m}q^{r-1}
\sim
m(e^{-1}-e^{-2}).
\tag{3.6}
\]

Finally,

\[
\frac{M^3d^4}{\ell^2}
\sim
\frac{m^{15}m^8}{(12m^{12})^2}
=\frac1{144m}.
\tag{3.7}
\]

Combining (3.5)--(3.7) proves (3.2). `QED`

### What Proposition 3.1 does and does not prove

It proves in the **actual configuration model**, not in an independent surrogate, that a very explicit class of three-hub pairing witnesses has diverging first moment.

It does **not** prove

\[
\mathbb P(Z_m>0)\to1.
\]

A first moment is not an existence theorem. The remaining obligation is to classify overlaps of two V-witnesses and prove a second-moment estimate (or use a switching/Janson-type argument adapted to the perfect matching).

---

## 4. B16: compute the small core cases exactly

The four-hub proof needs only a finite family of suppressed core topologies. Instead of bounding those topologies by Cayley's formula, we enumerated them exactly through Prüfer words.

For four fixed labeled hub vertices and `t` fixed labeled bulk branch vertices, every branch vertex must have tree degree exactly three. In a Prüfer word on `4+t` vertices, this means each branch label occurs exactly twice. Hence:

- `t=0`: all \(4^{4-2}=16\) labeled trees;
- `t=1`: choose two of the three Prüfer positions for the branch label and one of four hub labels for the remaining position, giving \(3\cdot4=12\);
- `t=2`: the length-four Prüfer word consists of two copies of each branch label, giving \(\binom42=6\);
- `t=3`: impossible, because three branch labels would need six occurrences in a Prüfer word of length five.

The exhaustive exact checker independently returns

\[
(16,12,6,0).
\]

This small-case sequence does more than save constants: it exposes the degree-budget reason the four-hub obstruction has only three core types. Combined with the path-sum calculation, those types decay respectively as

\[
m^{-1},\quad m^{-2},\quad m^{-3}.
\]

At `k=3`, in contrast, the exact V-witness class has mean of order `m`. The `k=3/k=4` split predicted by the rank-one heuristic therefore survives two separate actual-CM calculations:

\[
\boxed{
\mathbb EZ_m^{(3)}\asymp m,
\qquad
\mathbb P(\text{some 4-hub component})=O(m^{-1}).
}
\tag{4.1}
\]

The missing implication is only the lower direction for `k=3`.

---

## 5. Result of this bounded iteration

The latest checkpoint asked for “three-hub lower bound plus four-hub exclusion” in the explicit stress family. This run settles the **four-hub exclusion** completely and turns the **three-hub lower route** into an exact actual-CM first-moment problem.

The sharp remaining local statement is now:

\[
\boxed{
\mathbb P(Z_m>0)\to1
\quad\text{for the V-witness count in (3.1).}
}
\tag{5.1}
\]

A successful proof of (5.1), together with Theorem 2.1 and the existing hub-component contraction law, would establish that the maximal number of hubs in a component is exactly three with high probability for this stress family. It would still be a structured special-family theorem, not the full van der Hofstad crossover problem.

The next useful route is not another first-moment calculation. It is an overlap taxonomy for pairs of V-witnesses (disjoint, one shared hub, shared path prefix, same three hubs, and cyclic union), followed by an exact factorial-moment or switching bound.
