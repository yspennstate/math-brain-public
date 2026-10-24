# VDH-8.3-DUALITY — exact fixed-set conditional duality and the true conditioning obstruction

**Status.** R14 theorem-sized self-check / **PARTIAL** progress on van der Hofstad's barely-supercritical finite-third-moment configuration-model question “Does the discrete duality principle still hold?” This note does **not** solve the source problem and does **not** claim novelty. It gives an exact conditional-law identity for a prescribed candidate giant vertex set and isolates the only extra bias introduced by requiring that candidate to be the unique largest component.

The purpose is to stress-test the negation before trying to prove asymptotic duality. The obvious possible failure mechanism is that conditioning a prescribed set to be the giant might seriously bias the pairing on its complement. For the configuration model, the bias can be written exactly and is much smaller in conceptual scope than that: after conditioning away cross-edges and requiring connectivity inside the prescribed giant, the complement is **exactly** a fresh configuration model. Requiring the prescribed component to be the **unique largest** only conditions that fresh complement on the event that its own largest component is smaller than the giant.

## 1. Setup

Let `d=(d_v)_{v in V}` be a deterministic graphical half-edge sequence with even total half-edge count. Work with the configuration-model multigraph `CM(d)`, i.e. a uniformly random perfect matching of all half-edges.

Fix a deterministic subset `S subset V`, put `T=V\S`, and assume the half-edge totals

\[
L_S:=\sum_{v\in S}d_v,
\qquad
L_T:=\sum_{v\in T}d_v
\]

are even. Let

- `X_S` be the restriction of the pairing to half-edges incident to `S`;
- `X_T` be the restriction to half-edges incident to `T`;
- `N_S` be the event that there are **no** pairs joining `S` to `T`;
- `C_S` be the event that the multigraph induced by `X_S` is connected;
- `M_T(s)` be the event that every component of the multigraph induced by `X_T` has fewer than `s` vertices.

Thus, for `s=|S|`, the event

\[
G_S:=N_S\cap C_S\cap M_T(|S|)
\tag{1.1}
\]

is exactly the event that `S` is the vertex set of the **unique largest component** (with strict inequality ruling out ties).

## 2. Exact factorization under no cross-edges

### Proposition 2.1

Conditional on `N_S`, the pairings `X_S` and `X_T` are independent uniform perfect matchings of the half-edges in `S` and `T`, respectively. Equivalently,

\[
\boxed{
\mathcal L(X_S,X_T\mid N_S)
=
\mathrm{UnifPM}(S)\otimes\mathrm{UnifPM}(T).
}
\tag{2.1}
\]

### Proof

Every perfect matching with no `S`--`T` pair is uniquely a pair `(m_S,m_T)`, where `m_S` is a perfect matching of the `L_S` half-edges in `S` and `m_T` is a perfect matching of the `L_T` half-edges in `T`. Conversely every such ordered pair gives one global matching with no cross-edge.

The number of allowed global matchings is therefore

\[
(L_S-1)!!\,(L_T-1)!!,
\]

and every ordered pair `(m_S,m_T)` occurs with the same conditional probability

\[
\frac1{(L_S-1)!!(L_T-1)!!}.
\]

This is exactly the product of the two uniform perfect-matching laws. `square`

This is the “count the same thing twice” step: global no-cross matchings and ordered pairs of internal matchings are literally in bijection.

## 3. Connectivity of the candidate giant does not bias the complement

### Corollary 3.1

Conditional on `N_S cap C_S`, the complement pairing `X_T` is still an **unconditioned** configuration-model pairing with degree sequence `d|_T`:

\[
\boxed{
\mathcal L(X_T\mid N_S,C_S)=CM(d|_T).
}
\tag{3.1}
\]

### Proof

Under Proposition 2.1, `X_S` and `X_T` are independent. The event `C_S` is measurable with respect to `X_S` only. Conditioning on it cannot alter the law of `X_T`. `square`

So merely forcing `S` to be a connected component does **not** create a mysterious Radon--Nikodym tilt on the rest of the graph.

## 4. Requiring `S` to be the unique largest component: exact law

### Theorem 4.1 — fixed-set conditional duality identity

Conditional on `G_S`, the complement pairing is exactly a configuration model on `d|_T` conditioned only on having no component as large as `S`:

\[
\boxed{
\mathcal L(X_T\mid G_S)
=
\mathcal L\bigl(CM(d|_T)\mid L_1(CM(d|_T))<|S|\bigr).
}
\tag{4.1}
\]

Moreover, writing

\[
p_S:=\mathbb P_{CM(d|_T)}\bigl(L_1<|S|\bigr),
\]

the Radon--Nikodym derivative relative to the unconditioned complement law is

\[
\boxed{
\frac{d\mathcal L(X_T\mid G_S)}{d\mathcal L(CM(d|_T))}(x)
=
\frac{\mathbf 1\{L_1(x)<|S|\}}{p_S}.
}
\tag{4.2}
\]

Consequently,

\[
\boxed{
 d_{\rm TV}\!\left(
 \mathcal L(X_T\mid G_S),
 \mathcal L(CM(d|_T))
 \right)
 =1-p_S
 =\mathbb P_{CM(d|_T)}(L_1\ge |S|).
}
\tag{4.3}
\]

### Proof

By Corollary 3.1, conditional on `N_S cap C_S`, `X_T` is a fresh uniform configuration-model pairing on `T`. The remaining factor in `G_S` is exactly the event `M_T(|S|)`, which is measurable with respect to `X_T` and is identical to `{L_1(CM(d|_T))<|S|}`. This proves (4.1) and (4.2).

For any probability law `P` and event `E` of positive probability,

\[
d_{TV}(P(\cdot\mid E),P)=P(E^c).
\]

Indeed the density is `1_E/P(E)`, so

\[
\frac12 E_P\left|\frac{1_E}{P(E)}-1\right|
=\frac12\{P(E)(P(E)^{-1}-1)+P(E^c)\}
=P(E^c).
\]

Take `P=CM(d|_T)` and `E={L_1<|S|}`. `square`

## 5. Counterexample-first stress test

The obvious negation route was:

> Perhaps conditioning a prescribed connected set `S` to be the giant introduces a complicated global bias in the complement, so literal duality fails before one even reaches asymptotics.

Theorem 4.1 kills that mechanism completely for a fixed candidate set. There is only one possible bias:

\[
\boxed{
\text{the fresh complement CM is conditioned on }L_1<|S|.
}
\tag{5.1}
\]

This also identifies exactly when the mechanism *can* matter. If the candidate giant scale is comparable with the natural largest-component scale of the complement, then the conditioning probability in (4.3) need not tend to zero and exact unconditional duality is false in total variation. Thus a proof must use the scale separation of the barely-supercritical source regime; it cannot be a purely combinatorial statement valid at criticality.

Conversely, if one can prove uniformly over likely candidate giant sets `S` that

\[
\mathbb P_{CM(d|_T)}(L_1\ge |S|)=o(1),
\tag{5.2}
\]

then

\[
\mathcal L(X_T\mid G_S)
\quad\text{and}\quad
CM(d|_T)
\]

are asymptotically equivalent in **total variation**, not merely contiguous.

## 6. Why the source regime should make the conditioning negligible

In the finite-third-moment barely-supercritical regime, the giant has order `n epsilon_n`, whereas the candidate dual barely-subcritical largest-component scale carried by the preceding HARD7-04 work is of order

\[
\varepsilon_n^{-2}\log(n\varepsilon_n^3).
\]

Their ratio is

\[
\frac{n\varepsilon_n}{\varepsilon_n^{-2}\log(n\varepsilon_n^3)}
=
\frac{n\varepsilon_n^3}{\log(n\varepsilon_n^3)}
\longrightarrow\infty
\tag{6.1}
\]

whenever `n epsilon_n^3 -> infinity`. Therefore the exact conditioning obstruction (4.3) should disappear once one has a **uniform** subcritical upper tail for the random outside degree sequence.

This section is a route implication, not a new source theorem: the required uniform tail estimate for the random post-giant degree sequence still has to be checked under the exact source hypotheses and with the random-set conditioning handled correctly.

## 7. How this interfaces with the inherited HARD7-04 results

HARD7-04 already established, as partial proof checkpoints, a simultaneous weighted degree-profile approximation

\[
\sum_d(1+d)\left|N^{out}_{n,d}-n_d\xi_n^d\right|
=o_p(n\varepsilon_n)
\tag{7.1}
\]

and a candidate sharp second-component scale under earlier reductions. Those results attack the **random degree sequence** and **size** parts of duality.

Theorem 4.1 attacks a different issue: the conditional law of the pairing once the outside vertex set/degree sequence is specified. It says there is no additional unknown pairing tilt except the explicit event `{L_1<|S|}`.

A promising route to a source theorem is therefore:

1. show that, with high probability, the random outside degree sequence lies in a deterministic “good” class controlled by (7.1);
2. prove a subcritical largest-component upper tail uniformly on that good class at a scale `o(n epsilon_n)`;
3. apply (4.3) conditionally on the realized candidate giant set to erase the unique-largest conditioning;
4. replace the random outside degree sequence by the extinction-tilted dual degree sequence at whatever notion of graph observable the source requires.

Step 3 is now exact. Steps 1, 2 and 4 remain the genuine work.

## 8. Section-B method accounting

### #2 ATTACK THE NEGATION FIRST

Tried to construct a failure of duality caused solely by conditioning the prescribed candidate set to be the giant. The attack failed in the strongest useful way: the complement-law bias is exactly the one event in (5.1), with total-variation cost exactly its failure probability.

### #18 SAY IT IN ANOTHER LANGUAGE

Rewrote “discrete duality” as a conditional-law / Radon--Nikodym identity for perfect matchings. This turns a qualitative graph heuristic into the exact formula (4.2).

### #25 COUNT THE SAME THING TWICE

Counted no-cross global perfect matchings directly and as pairs of internal perfect matchings, yielding the exact product law (2.1).

## 9. Remaining obligation and status

This note does **not** prove the source's full discrete duality principle. It isolates a clean next target:

\[
\boxed{
\sup_{d^{out}\in\mathcal G_n}
\mathbb P_{CM(d^{out})}\!\left(
L_1\ge c\,n\varepsilon_n
\right)
\longrightarrow0
}
\tag{9.1}
\]

for a high-probability class `G_n` of post-giant degree sequences generated by the source exploration, with the constants/normalization aligned to the actual giant-size asymptotic. Once (9.1) is in hand, the “largest-component conditioning” disappears in total variation by an exact identity rather than a heuristic.

- Source: **OPEN** in the bounded current-source/literature screen used by R14.
- Result here: **PARTIAL**.
- Independent audits: **0**.
- Finite checker: none needed; this is an exact combinatorial/probabilistic theorem with proof on the page.
- Novelty: **not claimed**. Conditional factorization of uniform matchings is elementary/folklore; the contribution here is the exact reduction of the VDH source obstruction to the complement-largest tail in the current proof program.
