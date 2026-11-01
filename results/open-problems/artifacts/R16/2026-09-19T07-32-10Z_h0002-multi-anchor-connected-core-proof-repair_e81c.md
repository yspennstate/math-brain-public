# R16 H0002 — connected-core proof repair for the multi-anchor theorem

This is a substantive proof repair for the immutable run report

`runs/R16/2026-09-19T07-29-30Z_h0002-multi-anchor-layercake-absorption_e81c.md`.

It does **not** change the theorem statement, the constants, or the ledger movement `G_multi >= G_2A > G_pad`. It repairs one conditioning sentence in Section 5 of that report.

## The issue

The report conditioned on a connected round-one/two seed component `A_*` satisfying

`|A_*| >= (a(d3)-o(1))n`

and then wrote

`|A_*\A_i|/n <= d3-e_i+o(1)`.

That inequality does not follow from a **lower** bound on `|A_*|`; the actual connected component may be larger. A larger component should help, but the proof must account for it rather than reverse the inequality.

## Correct conditioning: trim to a connected core of controlled size

Fix the same finite anchor set

`d1=e1<e2<...<ek<d3<dP`.

On the established gluing event, let `C_big` be the connected seed component with

`|C_big| >= (a(d3)-o(1))n`.

Choose a deterministic sequence `eta_n -> 0` large enough to dominate the gluing `o(1)` loss, and put

`N3:=floor((a(d3)-eta_n)n)`.

For all large `n`, `N3<=|C_big|`. Every finite connected graph contains a connected vertex subset of every cardinality between `1` and its order: take a spanning tree and delete leaves one at a time. Hence choose a connected core

`C subset C_big`, `|C|=N3`.

Because each `a(e_i)<a(d3)` by a fixed amount, choose nested anchor subsets

`A_1 subset A_2 subset ... subset A_k subset C`

with

`|A_i|=a(e_i)n+o(n)`.

Now the needed size comparison is exact in the correct direction:

`|C\A_i|/n = d3-e_i+o(1)`.

For each anchor, let `H_i` be the degree-quantile set from Lemma 1 of the report, so

`|H_i| >= (s-o(1))n`.

Define

`T_i:=H_i\C`.

Then

`|T_i|/n >= [s-(d3-e_i)]_+-o(1)=m_i(d3)-o(1)`.

This recovers exactly the mass lower bound used by the layer-cake argument.

## Why vertices in `C_big\C` do not create a new problem

The sets `T_i` may contain vertices of the already-connected excess `C_big\C`. Such vertices are **better** than prospective round-three attachments: they are already connected to `C` before the absorption round.

For every vertex `v outside C` define

`Y_v:=1` if `v in C_big\C`,

and otherwise let `Y_v` be the indicator that the independent absorption round opens an edge from `v` into `C`.

For `v in T_i`:

- if `v in C_big\C`, then `Y_v=1` deterministically;
- if `v notin C_big`, its anchor-degree lower bound into `A_i subset C` gives the same attachment-probability lower bound `r_i` as in the report.

Thus in every case

`P(Y_v=1 | rounds 1 and 2) >= max{r_i: v in T_i}`.

The nonconstant variables `Y_v` use disjoint absorption-round edge sets for distinct outside vertices; the variables equal to `1` are deterministic. Therefore the same Poisson-binomial Chernoff estimate applies.

The layer-cake identity now gives

`sum_{v outside C} P_lower(v)
 >= n * integral_0^1 max_{i:r_i>=t} m_i(d3) dt-o(n)`.

Since `C` itself is connected and every successful `Y_v` vertex is in the final component containing `C`, the final connected mass is at least

`a(d3)
 + integral_0^1 max_{i:r_i>=t} m_i(d3) dt
 - o(1)`

after absorbing the vanishing `eta_n` into the final `o(1)`.

This is exactly the lower bound claimed in Sections 7-8 of the immutable report.

## Consequence

The proof of the multi-anchor theorem is repaired without changing any definition:

`G_multi := a(dP) + sup_D integral_0^1 max_{d in D:R(d)>=t} m(d) dt`,

and every fixed `g<G_multi` still satisfies

`P(L1(G_p)>=g n) -> 1`.

The explicit two-anchor choice in Section 9 is unaffected, so

`G_multi >= G_2A > G_pad`.

The stray display typo `a(e_i)n+o(n` in Section 5 of the immutable report should be read as `a(e_i)n+o(n)`; it has no mathematical effect.

This repair is analytic; there is no finite claim requiring an exact-arithmetic checker.