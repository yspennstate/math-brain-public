# R06 / I0056 closure audit request — edge-to-outer-vertex theorem

Requested independent auditors under `operations/RFLEET_2026-09-16.md` and the fleet closure contract:

1. **R05**, the directed R-series auditor for R06; and
2. **P26**, the shared independent audit/ledger track.

No audit is claimed by this file. The earlier R05 audit
`R05-AUDIT-R06-I0056-LOWER-20260916T141505Z: PASS_SCOPED`
covered only the old Haslegrave--Panagiotis lower bound for the pre-closure
`H_{5,5}` interval and does **not** audit the theorem below.

## Source scope

Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:
determine the outer vertex-isoperimetric constant for regular, co-regular plane
graphs. Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, compute the triangular
and quadrangular cases (face degree/codegree 3 and 4). The R06 frozen unresolved
test case was the regular pentagonal tessellation `H_{5,5}`.

The source outer vertex boundary is
\[
\partial_V K=\{x\notin K:\exists y\in K,\ x\sim y\},\qquad
\Phi_V(G)=\inf_{\varnothing\ne K\subset V,\ K\ {\rm finite}}
\frac{|\partial_VK|}{|K|}.
\]
The edge boundary is
\[
\partial_EK=\{xy:x\in K,\ y\notin K\},\qquad
\Phi_E(G)=\inf_K\frac{|\partial_EK|}{|K|}.
\]

## Candidate theorem to audit

**R06-I0056-CLOSURE-01.**
Let `G` be an infinite simple `d`-regular graph. If
\[
\Phi_E(G)\ge d-3,
\]
then
\[
\Phi_V(G)=\Phi_E(G).
\]

No planarity or transitivity is used in this theorem.

### Full proof

Write `h=Phi_E(G)`. Always `Phi_V(G)<=h`, because every outer boundary
vertex supports at least one crossing edge.

Fix an arbitrary finite nonempty `K_0`, write `n=|K_0|`, and perform the
following closure operation. If some `v notin K_j` has
\[
r_j:=|N(v)\cap K_j|\ge2,
\]
set `K_{j+1}=K_j union {v}`. Let
\[
b_j=|\partial_VK_j|,\qquad e_j=|\partial_EK_j|.
\]

Because `G` is simple and `d`-regular, exactly `r_j` old crossing edges at `v`
become internal and exactly `d-r_j` formerly external edges become crossing.
Thus
\[
e_{j+1}=e_j+d-2r_j\le e_j+d-4. \tag{1}
\]
For the outer vertex boundary, `v` itself leaves the old boundary, every old
boundary vertex other than `v` remains a boundary vertex because the set only
grows, and at most the `d-r_j` outside neighbours of `v` can be newly exposed.
Hence
\[
b_{j+1}\le b_j-1+(d-r_j)\le b_j+d-3. \tag{2}
\]

The process must terminate. Indeed, after `m` additions,
\[
e_m\le e_0+m(d-4)\le dn+m(d-4),
\]
whereas the definition of `h` gives
\[
e_m\ge h(n+m).
\]
Consequently
\[
(h-d+4)m\le(d-h)n.
\]
Since `h>=d-3`, the coefficient `h-d+4` is at least `1`, so an infinite
sequence of additions is impossible.

At the terminal set `K_m`, every outer boundary vertex has exactly one
neighbour in `K_m`: it has at least one by definition and cannot have two,
otherwise the closure step would still apply. Simplicity then gives a
bijection between outer boundary vertices and crossing edges, so
\[
b_m=e_m.
\]
Iterating (2) backwards and using edge expansion,
\[
\begin{aligned}
b_0
&\ge b_m-(d-3)m\\
&=e_m-(d-3)m\\
&\ge h(n+m)-(d-3)m\\
&=hn+(h-d+3)m\\
&\ge hn.
\end{aligned}
\]
Since `K_0` was arbitrary, `Phi_V(G)>=h`. Combined with `Phi_V(G)<=h`,
this proves equality. QED.

## Source corollary to audit

Byung-Geun Oh's sharp edge-isoperimetric theorem for a `(d,f)`-regular plane
tessellation gives
\[
\Phi_E(d,f)
=(d-2)\sqrt{1-\frac4{(d-2)(f-2)}}.
\]
For `f>=5` and `d>=4`,
\[
\Phi_E(d,f)^2-(d-3)^2
=2d-5-\frac{4(d-2)}{f-2}
\ge\frac{2d-7}{3}>0.
\]
For `d=3`, every admissible infinite plane pair with `f>=5` has
`Phi_E>=0=d-3` (the Euclidean equality pair is `(3,6)`).
Therefore CLOSURE-01 yields
\[
\Phi_V(d,f)=\Phi_E(d,f)
=(d-2)\sqrt{1-\frac4{(d-2)(f-2)}}
\quad (f\ge5)
\]
throughout the regular/co-regular tessellation branch not covered by the
Haslegrave--Panagiotis face-degree 3 and 4 formulas.

For the frozen pair
\[
H_{5,5}:\qquad \Phi_V=\Phi_E=\sqrt5.
\]
Thus the certified interval width is exactly zero.

## Required adversarial checks

1. **Quadrangular non-extension.** For `f=4`,
   \[
   \Phi_E(d,4)^2-(d-3)^2=-1,
   \]
   so CLOSURE-01 does not apply. This is essential: the known quadrangular
   vertex constant is not the edge constant.
2. **Simple-graph dependence.** Terminal `b_m=e_m` uses absence of parallel
   crossing edges. Verify that the Lyons--Peres / Haslegrave--Panagiotis /
   Oh regular plane tessellation scope is the usual simple tessellation
   edge graph, or flag any mismatch.
3. **Infinite-set convention.** The proof uses the infinite-graph constants
   with the infimum over all finite nonempty vertex sets, with no finite-graph
   `|K|<=|V|/2` restriction.
4. **Oh normalization.** Verify that Oh's `Phi(p,q)` is the unnormalized
   crossing-edge count divided by vertex count, matching `Phi_E` here.

## Exact evidence

Original closure checker:
- `artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.py`
- `artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.out`

Hardening checker from the present run:
- `artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.py`
- `artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.out`

The hardening checker exhaustively verifies the local boundary moves on every
simple graph with at most six vertices (2,331,910 admissible closure moves),
checks 533,158 terminal multiplicity-one instances, and checks the exact
regular/co-regular threshold over all admissible `3<=d<=500`, `5<=f<=500`.

## Prior-art status

As of 2026-09-16, a bounded search found:
- Haslegrave--Panagiotis (2021): exact outer vertex constants only for
  triangular and quadrangular hyperbolic lattices;
- Panagiotis (2024), *Self-avoiding walks and polygons on hyperbolic graphs*:
  explicitly remarks that the vertex Cheeger constant has been computed for
  `k=3` or `4`;
- Oh, arXiv:2009.04394 (current arXiv metadata checked 2026-09-16):
  exact **edge** isoperimetry for plane tessellations;
- D'Achille--Jacquier--Ruszel (2026): perimeter/edge isoperimetry on regular
  hyperbolic lattices.

No exact prior source for CLOSURE-01 or an `f>=5` outer-vertex formula was
found in the bounded search. This is **not** a proof of novelty.

## Audit decision requested

Please return one of:
- `PASS` — theorem, normalization, and source corollary all verified;
- `PASS_SCOPED` — theorem valid but source application needs a stated scope
  restriction;
- `FAIL` — with the first invalid step or a concrete counterexample.

Do not count the old R05 lower-bound audit as this audit.
