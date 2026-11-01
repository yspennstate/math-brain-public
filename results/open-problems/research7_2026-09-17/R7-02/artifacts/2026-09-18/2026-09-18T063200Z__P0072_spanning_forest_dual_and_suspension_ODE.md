# P0072 — spanning-forest duality and global mean-ODE stability on two-terminal suspensions

## Scope

This artifact continues canonical outside target `P0072` (Aletti et al., *Open Problems in Stochastic Reinforcement Models*, Section 2; parent formulation Kious–Mailler–Schapira, *Finding geodesics on graphs using reinforcement learning*, Conjecture 1.1).

It does **not** claim the full stochastic source conjecture. It proves a general exact dual identity for loop-erased reinforcement and then a complete deterministic theorem for the stochastic-approximation mean ODE on a broad non-series-parallel graph class. The remaining stochastic boundary-avoidance step is stated explicitly at the end.

Methods used in this research iteration are B11 (dualize), B25 (count the same object twice / forest decomposition), and B30 (localize the first gluing failure).

---

## 1. Weighted spanning-tree representation of one loop-erased ant

Let `G=(V,E)` be a finite connected undirected graph with distinguished vertices `s` (nest) and `t` (food), and positive conductances `c_e`.

A conductance-biased random walk from `s` stopped on first hitting `t`, after chronological loop erasure, has the same law as the unique `s`–`t` path in a weighted random spanning tree `T`, where

\[
\Pr(T)=\frac{\prod_{e\in T}c_e}{\tau(c)},
\qquad
\tau(c):=\sum_{T\text{ tree}}\prod_{e\in T}c_e.
\]

Write `p_e(c)` for the probability that the loop-erased path reinforces edge `e`.

Let `F_{s,t}` be the family of spanning two-forests with exactly two components, one containing `s` and one containing `t`, and write

\[
\Phi_{s,t}(c):=\sum_{F\in\mathcal F_{s,t}}\prod_{f\in F}c_f.
\]

For `e=uv`, define

\[
\Phi_e^\times(c)
:=
\sum_{\substack{F\in\mathcal F_{s,t}\\u,v\text{ in different components of }F}}
\prod_{f\in F}c_f.
\]

### Lemma 1 (exact deletion duality)

For every edge `e=uv`,

\[
\boxed{
\frac{p_e(c)}{c_e}=\frac{\Phi_e^\times(c)}{\tau(c)}.
}
\]

Equivalently, if `R_{s,t}(c)` is the effective resistance and `\mathbb F_{s,t}` is the probability measure on `s`–`t` separating two-forests proportional to their weights, then

\[
\boxed{
\frac{p_e(c)}{c_e}
=R_{s,t}(c)\,
\mathbb P_{\mathbb F_{s,t}}(u,v\text{ separated}).
}
\]

#### Proof

An edge `e` lies on the unique `s`–`t` path of a spanning tree `T` if and only if deleting `e` from `T` produces an `s`–`t` separating spanning two-forest whose two components contain `u` and `v` on opposite sides. The map

\[
T\longmapsto F=T\setminus\{e\}
\]

is a bijection between trees whose `s`–`t` path contains `e` and forests counted by `\Phi_e^\times`. Under this bijection

\[
\prod_{f\in T}c_f=c_e\prod_{f\in F}c_f.
\]

Summing and dividing by `\tau(c)` proves the first identity. Kirchhoff's two-forest formula gives

\[
R_{s,t}(c)=\frac{\Phi_{s,t}(c)}{\tau(c)},
\]

which gives the second identity. ∎

This duality is the useful exact replacement for direct random-walk path enumeration.

---

## 2. A general terminal-pair identity and exact harmonic-number martingales

Suppose an interior vertex `i` is joined to both terminals by edges `si` and `it`. Under an `s`–`t` separating two-forest, `i` lies on exactly one of the two sides. Hence Lemma 1 gives

\[
\boxed{
\frac{p_{si}}{c_{si}}+\frac{p_{it}}{c_{it}}=R_{s,t}(c).
}
\]

The right side is independent of `i`.

Consequently, in the actual loop-erased ant process, if `W_e(n)` denotes the raw edge weight before ant `n+1`, then for every two such interior vertices `i,j`,

\[
M_{ij}(n)
:=
H_{W_{si}(n)-1}+H_{W_{it}(n)-1}
-H_{W_{sj}(n)-1}-H_{W_{jt}(n)-1}
\]

is an **exact martingale**. Indeed, reinforcing an edge of current weight `W` increases `H_{W-1}` by exactly `1/W`, and therefore

\[
\mathbb E[\Delta M_{ij}(n)\mid\mathcal F_n]
=
\frac{p_{si}}{W_{si}}+\frac{p_{it}}{W_{it}}
-rac{p_{sj}}{W_{sj}}-\frac{p_{jt}}{W_{jt}}
=0.
\]

The five-edge losange martingale recovered in the preceding R7-02 run is the two-interior-vertex special case of this general identity.

---

## 3. Two-terminal suspension graphs

Let `I={1,...,m}` be a finite set of interior vertices. Consider the graph obtained by:

1. joining every `i\in I` to `s` and to `t`;
2. adding an arbitrary finite internal graph `H` on `I`.

The source-to-food geodesics all have length two, `s-i-t`. Every edge of `H` is therefore non-geodesic.

Write the normalized conductances as

\[
l_i=c_{si},\qquad r_i=c_{it},\qquad h_e=c_e\ (e\in E(H)),
\]

with

\[
\sum_i l_i=\sum_i r_i=1.
\]

For the loop-erased mean field define

\[
\dot c_e=p_e(c)-c_e.
\]

The two terminal sums are invariant because every simple `s`–`t` path uses exactly one edge incident to `s` and exactly one edge incident to `t`.

---

## 4. B25 forest factorization on the balanced terminal manifold

Assume temporarily that

\[
l_i=r_i=a_i>0,
\qquad
\sum_i a_i=1.
\]

### Lemma 2 (effective resistance is exactly two)

For every choice of the internal conductances `h`,

\[
\boxed{R_{s,t}=2.}
\]

#### Proof

Put electric potential `0` at `s`, `1` at `t`, and `1/2` at every interior vertex. Every internal edge has zero voltage drop. The total current entering from `t` is

\[
\sum_i a_i(1-1/2)=1/2.
\]

Thus the effective conductance is `1/2`, hence the resistance is `2`. ∎

There is also a useful combinatorial explanation. Restrict an `s`–`t` separating spanning two-forest to the internal graph `H`. If its internal components are `C_1,...,C_k`, then each `C_j` must have exactly one terminal attachment edge: two attachments to the same root would create a cycle, while attachments to both roots would join `s` and `t`. For a component `C`, the total weight of choosing its unique attachment to `s` is

\[
A(C):=\sum_{i\in C}a_i,
\]

and the total weight of choosing its unique attachment to `t` is the same `A(C)`.

Therefore, conditional on the internal forest, the root labels of its connected components are independent fair `s/t` coins.

Let `\mathbb Q_h` denote the induced probability law on internal forests; up to normalization its weight is

\[
\boxed{
\Big(\prod_{e\in F_H}h_e\Big)
\prod_{C\in\operatorname{Comp}(F_H)}2A(C).
}
\]

### Lemma 3 (strict negative drift of every positive non-geodesic edge on the balanced manifold)

For an internal edge `e=ij` with `h_e>0`,

\[
\boxed{
\frac{p_e}{h_e}
=
\mathbb Q_h(i,j\text{ lie in different internal-forest components})
<1.
}
\]

Hence

\[
\boxed{p_e-h_e<0.}
\]

#### Proof

By Lemma 1 and Lemma 2,

\[
\frac{p_e}{h_e}=2\theta_e,
\]

where `\theta_e` is the probability that `i` and `j` are on opposite root sides in the `s`–`t` separating two-forest.

Condition on the internal forest. If `i,j` are in the same internal component, they necessarily have the same root label. If they are in different internal components, their independent fair root labels differ with probability `1/2`. Thus

\[
\theta_e=\frac12\mathbb Q_h(i,j\text{ in different internal components}),
\]

which proves the displayed identity.

Strict inequality follows because `h_e>0` gives positive `\mathbb Q_h`-weight to an internal forest containing `e` (for example, take `e` together with no other internal edge and then attach each resulting component to one terminal). On that event `i,j` are in the same component. ∎

By terminal symmetry and Lemma 1,

\[
p_{si}=p_{it}=a_i
\]

on this balanced manifold. Thus the deterministic mean field leaves the geodesic terminal coordinates fixed while strictly decreasing every positive non-geodesic internal coordinate.

---

## 5. B11 global theorem for the deterministic mean ODE

### Theorem 4 (global mean-ODE convergence on every finite suspension graph)

Assume all terminal conductances are initially positive:

\[
l_i(0)>0,\qquad r_i(0)>0,
\]

and normalize their two sums to one. Internal conductances are nonnegative and finite. Then the loop-erased stochastic-approximation ODE

\[
\dot c_e=p_e(c)-c_e
\]

has the following global limit.

Set

\[
q_i:=l_i(0)r_i(0),
\qquad
S:=\sum_j\sqrt{q_j},
\qquad
\boxed{a_i:=\frac{\sqrt{q_i}}{S}}.
\]

Then

\[
\boxed{
l_i(t)\to a_i,
\qquad
r_i(t)\to a_i
}
\]

for every interior vertex `i`, and

\[
\boxed{h_e(t)\to0}
\]

for every internal edge `e`.

Thus the full mean ODE converges to the geodesic face, even when `H` is arbitrary and highly non-series-parallel.

#### Proof

For every `i`, the terminal-pair identity gives

\[
\frac{d}{dt}\log(l_i r_i)
=
\frac{p_{si}-l_i}{l_i}
+
\frac{p_{it}-r_i}{r_i}
=R_{s,t}-2.
\]

The right side is independent of `i`; hence all product ratios are conserved. There exists a scalar `\lambda(t)>0` such that

\[
\boxed{l_i(t)r_i(t)=\lambda(t)q_i\quad\text{for all }i.}
\]

Next, `R_{s,t}\ge2`. To see this, use Thomson's principle. Any unit `s`–`t` flow has energy on the cut incident to `s`

\[
\sum_i\frac{f_{si}^2}{l_i}
\ge
\frac{(\sum_i f_{si})^2}{\sum_i l_i}=1,
\]

and likewise has energy at least `1` on the disjoint cut incident to `t`. Internal edges contribute nonnegative energy. Therefore the minimum unit-flow energy satisfies

\[
\boxed{R_{s,t}\ge2.}
\]

Consequently `\lambda(t)` is nondecreasing because

\[
\frac{d}{dt}\log\lambda=R_{s,t}-2\ge0.
\]

On the other hand Cauchy–Schwarz gives

\[
\sqrt{\lambda(t)}S
=
\sum_i\sqrt{l_i(t)r_i(t)}
\le
\sqrt{\sum_i l_i(t)}\sqrt{\sum_i r_i(t)}=1,
\]

so

\[
\lambda(t)\le S^{-2}.
\]

Thus `\lambda(t)` has a finite limit `\lambda_\infty\le S^{-2}`.

We claim equality. If `\lambda_\infty<S^{-2}`, then for all large `t`

\[
\sum_i\sqrt{l_i r_i}\le1-\eta
\]

for some `\eta>0`. Since `\lambda` is nondecreasing and every `q_i>0`, all terminal coordinates remain uniformly bounded away from zero. Also each internal coordinate is uniformly bounded, because `p_e\le1` implies

\[
\dot h_e\le1-h_e.
\]

Hence the trajectory lies eventually in a compact set on which the Hellinger gap above is positive.

Equality `R_{s,t}=2` can occur only when `l_i=r_i` for every `i`: equality in both cut Cauchy–Schwarz inequalities forces the minimizing flow to satisfy `f_{si}=l_i` and `f_{it}=r_i`, while total energy `2` leaves zero energy for every internal edge, and flow conservation at each interior vertex then gives `l_i=r_i`. Therefore `R_{s,t}-2` has a strictly positive minimum on the above compact Hellinger-gap set. This would force `\log\lambda` to increase at a positive linear rate, contradicting boundedness. Hence

\[
\boxed{\lambda_\infty=S^{-2}.}
\]

It follows that

\[
\sum_i\sqrt{l_i r_i}\to1.
\]

Since

\[
\sum_i(\sqrt{l_i}-\sqrt{r_i})^2
=2-2\sum_i\sqrt{l_i r_i},
\]

we get `l_i-r_i\to0` for every `i`. Together with

\[
l_i r_i\to S^{-2}q_i=a_i^2
\]

this yields

\[
l_i,r_i\to a_i.
\]

It remains to eliminate internal conductances. Fix one internal edge `e` and `\varepsilon>0`. All internal coordinates stay in a compact box. At the limiting balanced terminal vector `(a,a)`, Lemma 3 gives

\[
\rho_e(h):=\frac{p_e(a,a,h)}{h_e}<1
\]

for every `h` with `h_e>0`. On the compact set `h_e\ge\varepsilon`, continuity gives a uniform `\delta(\varepsilon)>0` such that

\[
\rho_e(h)\le1-\delta(\varepsilon).
\]

Since `(l(t),r(t))\to(a,a)`, the same strict bound (with, say, `\delta/2`) holds for all sufficiently large `t` whenever `h_e(t)\ge\varepsilon`. Therefore

\[
\dot h_e
=h_e\left(\frac{p_e}{h_e}-1\right)
\le-\frac{\delta}{2}h_e
\]

throughout that region. After sufficiently large time the trajectory cannot cross upward through the level `\varepsilon`; hence `\limsup h_e\le\varepsilon`. Because `\varepsilon>0` was arbitrary,

\[
h_e(t)\to0.
\]

This completes the proof. ∎

---

## 6. B30 exact minimal two-chord specialization

Take three interior vertices `a,b,c`, terminal-pair conductances

\[
(sa,at)=a,
\quad
(sb,bt)=b,
\quad
(sc,ct)=c,
\qquad a+b+c=1,
\]

and internal non-geodesic chords `ab=x`, `bc=y`.

Exact spanning-tree enumeration gives 45 trees and

\[
p_{sa}=p_{at}=a,
\quad
p_{sb}=p_{bt}=b,
\quad
p_{sc}=p_{ct}=c.
\]

Let

\[
A=2bc+(b+c)y,
\qquad
K=2c(a+b)+y,
\qquad
D=2aA+xK.
\]

Then

\[
\boxed{
p_{ab}=\frac{2axA}{D},
\qquad
p_{ab}-x=-\frac{x^2K}{D}<0.
}
\]

Likewise, with

\[
C=2ab+(a+b)x,
\qquad
L=2a(b+c)+x,
\]

one has the same denominator `D=2cC+yL` and

\[
\boxed{
p_{bc}=\frac{2cyC}{D},
\qquad
p_{bc}-y=-\frac{y^2L}{D}<0.
}
\]

The exact checker is

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T062700Z__P0072_two_chord_exact_checker.py`

with archived output

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T062700Z__P0072_two_chord_exact_checker.out`.

It exhausts all 45 spanning trees symbolically and ends with `ALL_EXACT_CHECKS_PASS`.

---

## 7. Exact remaining stochastic gluing failure

The source conjecture concerns the **random reinforced process**, not only its deterministic mean ODE.

The theorem above shows that for every suspension graph and every deterministic ODE trajectory whose terminal coordinates start positive, the non-geodesic internal weights are driven to zero and the terminal pairs balance. Thus no interior mean-field obstruction remains in this graph class.

However, the stochastic normalized process can in principle approach boundary faces where one or more terminal coordinates vanish. Those boundary faces contain genuine non-geodesic ODE equilibria. For example, after normalized geodesic edges disappear, a single longer simple path can itself be an ODE equilibrium because every loop-erased ant then follows it with probability one. The source theorem requires proving that the reinforced stochastic dynamics almost surely avoids such boundary traps.

The exact harmonic-number martingales in Section 2 are the new tool for that step, but this artifact does **not** yet prove the required almost-sure boundary nonconvergence. Standard stochastic-approximation language alone is insufficient unless the boundary is excluded rigorously.

Thus the current source status remains `PARTIAL / SOURCE OPEN`.

---

## 8. Literature positioning checked 2026-09-18

- Kious–Mailler–Schapira, *Finding geodesics on graphs using reinforcement learning*, Ann. Appl. Probab. 32(5) (2022), DOI `10.1214/21-AAP1777`, arXiv `2010.04820`: proves the loop-erased conjecture on series-parallel graphs, but explicitly says convergence was not proved on the five-edge non-series-parallel losange.
- Aletti et al., *Open Problems in Stochastic Reinforcement Models*, Section 2: retains the universal finite-graph endpoint as an open problem.
- Kassel–Kenyon–Wu, *Random two-component spanning forests*, Ann. Inst. H. Poincaré Probab. Statist. 51(4) (2015), arXiv `1203.4858`: provides standard two-forest, Green-function, and edge-separation formulas that support the spanning-forest language used here.
- A bounded search on 2026-09-18 for later work explicitly solving the loop-erased finite-graph conjecture, the losange convergence problem, or the suspension-graph stochastic problem did not reveal an exact source-level resolution. This is negative evidence only, not a novelty certificate.

Publication novelty of the new ODE theorem and martingale generalization is therefore **UNVERIFIED** pending a deeper prior-art review.
