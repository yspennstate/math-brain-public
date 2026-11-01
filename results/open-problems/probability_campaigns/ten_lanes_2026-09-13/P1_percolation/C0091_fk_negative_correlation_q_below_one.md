# C0091 — pairwise negative correlation in the random-cluster model with cluster weight q < 1

13 September 2026.

## The problem

Let `G = (V,E)` be a finite (multi)graph, let `p = (p_e)` be edge parameters in `(0,1)` and let
`q > 0`. The random-cluster (FK) measure is

    mu(omega)  =  Z^{-1} * prod_e p_e^{omega_e} (1-p_e)^{1-omega_e} * q^{k(omega)},

`k(omega)` the number of connected components of `(V, omega)`, isolated vertices counted.
For `q >= 1` the measure satisfies the FKG lattice condition and distinct edges are positively
correlated. For `0 < q < 1` the model is expected to be negatively dependent, and the weakest
form of that expectation — `Cov(omega_e, omega_f) <= 0` for `e != f` — is open on general graphs.

Ledger record: C0091, source `heydenreich_hofstad_highd_2017`, "Open Problem 16.9". The exact
book numbering could not be confirmed by fetch; what *was* confirmed (below) is that the
statement is open as of September 2026.

## Literature check (searches run 13 Sep 2026; every arXiv id below was fetched, not recalled)

* Heehyun Park, *The q<1 Random-Cluster Model on Wired Trees: Uniqueness and Negative
  Dependence*, arXiv:2608.08565 (9 Aug 2026). Abstract, fetched and quoted: "The random-cluster
  model with cluster weight 0<q<1 is expected to exhibit negative dependence, but without FKG
  even pairwise negative correlation remains open on general graphs." The paper proves a
  conditional negative-association statement on Delta-regular trees only.
* Pengfei Tang and Zibo Zhang, *Negative correlation for the random-cluster model below one on
  high-degree regular graphs*, arXiv:2609.11578 (10 Sep 2026). Abstract, fetched and quoted:
  "...even pairwise negative correlation between distinct edges remains open on general finite
  graphs." They prove it for high-degree regular graph sequences satisfying a two-scale
  edge-isoperimetric condition.
* No counterexample is reported anywhere in the searched literature, and no exhaustive
  small-graph computer search for one is reported. Negative searches: "random cluster q<1
  counterexample negative correlation"; "FK model q less than 1 positive correlation example";
  "computer search negative association random cluster" — nothing found.
* Grimmett's *The Random-Cluster Model* and Heydenreich–van der Hofstad could not be fetched as
  text (the PDFs came back as binary), so the attribution of the conjecture to a numbered item in
  either book is left unverified here.

So the problem is live, and the two 2026 papers are the frontier.

## 1. The conditional structure (PROVED, and machine-verified exactly)

Fix distinct edges `e = {a,b}` and `f = {c,d}` and write `H = G \ {e,f}`. Condition on the
configuration `eta` of `H`. Put

    delta_e  = k(eta) - k(eta + e),   delta_f = k(eta) - k(eta + f),
    delta_ef = k(eta) - k(eta + e + f),

each the number of components destroyed by inserting the edge(s); `delta_e, delta_f` lie in `{0,1}`.

**Proposition 1.** Exactly five triples `(delta_e, delta_f, delta_ef)` are realisable, namely
`(0,0,0)`, `(0,1,1)`, `(1,0,1)`, `(1,1,2)` and `(1,1,1)`. Conditionally on `eta`, the pair
`(omega_e, omega_f)` is *independent* in the first four cases. In the fifth — call it type E, the
case in which `e` and `f` together with `eta` close a cycle through both — the conditional law has
weights proportional to

    (1-x)(1-y),   x(1-y) r,   (1-x) y r,   x y r        with r = 1/q, x = p_e, y = p_f,

and, writing `Z_E = (1-x)(1-y) + r( x(1-y) + (1-x)y + xy )`,

    Cov( omega_e, omega_f | eta )  =  x y r (1-x)(1-y) (1-r) / Z_E^2 .

In particular the conditional covariance is strictly negative for `q < 1`, zero for `q = 1` and
strictly positive for `q > 1`.

*Proof.* The conditional weight of `S` contained in `{e,f}` is
`prod_{g in S} p_g * prod_{g not in S} (1-p_g) * q^{k(eta + S)}`, and `k(eta + S) = k(eta) - delta_S`;
dividing by `q^{k(eta)}` gives, in the four non-E cases,
`(1-x)(1-y)`, `x(1-y) r^{delta_e}`, `(1-x) y r^{delta_f}`, `x y r^{delta_e + delta_f}`, so the
table factorises as `((1-x) + x r^{delta_e}) * ((1-y) + y r^{delta_f})` and the two coordinates
are conditionally independent. In type E, `delta_e = delta_f = delta_ef = 1`, the table does not
factorise, and

    Cov = x y r / Z_E - x y r^2 / Z_E^2 = (x y r / Z_E^2)( Z_E - r ),
    Z_E - r = (1-x)(1-y) + r( 1 - (1-x)(1-y) ) - r = (1-x)(1-y)(1-r),

using `x(1-y) + (1-x)y + xy = 1 - (1-x)(1-y)`. For realisability: `max(delta_e, delta_f) <= delta_ef
<= delta_e + delta_f` is immediate, and `(0,0,1)` is impossible because if neither edge alone merges
components then neither does the pair. `(1,1,1)` occurs exactly when, in `eta`, `a !~ b` and
`c !~ d` but the two pairs are cross-connected (`a ~ c` and `b ~ d`, or `a ~ d` and `b ~ c`),
i.e. when `e` and `f` close a common cycle. QED

**Machine check.** `code/types_check.py` recomputes the conditional law by brute force in exact
rational arithmetic for every connected graph on at most 5 vertices with at most 8 edges, every
ordered pair of distinct edges, every configuration of the remaining edges, and
`q in {1/5, 1/2, 4/5, 3/2, 5}`: **83,310 conditional laws, 0 mismatches**, and exactly the five
predicted types observed. Nothing was checked in floating point.

## 2. The exact decomposition

Write `beta_x = x r / (1 - x + x r)` and `gamma_x = x r / Z_E` (and the same with `y`). Since
`Z_E - r = (1-x)(1-y)(1-r) < 0` and `Z_E - (1-x) - x r = y(1-x)(r-1) > 0`,

    x  <  gamma_x  <  beta_x        for every q < 1.

Let `U = 1{a !~ b in eta}`, `V = 1{c !~ d in eta}`, `Xi = 1{type E}` (so `Xi <= U V`). The
conditional mean of `omega_e` is `x` on `{U=0}`, `beta_x` on `{U=1, Xi=0}` and `gamma_x` on
`{Xi=1}`, hence

    g_e = x + (beta_x - x) U - (beta_x - gamma_x) Xi,
    g_f = y + (beta_y - y) V - (beta_y - gamma_y) Xi,

and by the conditional variance decomposition, with all moments under the `eta`-marginal of `mu`
(which is a *tilted* random-cluster measure on `H`, not the plain one),

    Cov(omega_e, omega_f)
      =  E[Xi] * x y r (1-x)(1-y)(1-r) / Z_E^2
       + (beta_x - x)(beta_y - y)         Cov(U,V)
       - (beta_x - x)(beta_y - gamma_y)   Cov(U,Xi)
       - (beta_x - gamma_x)(beta_y - y)   Cov(Xi,V)
       + (beta_x - gamma_x)(beta_y - gamma_y) Var(Xi).                       (*)

Every coefficient in (*) is explicit; the first line is strictly negative for `q<1` and is the
only negative term. **This is the whole content of the conjecture**: what remains is that the
four `eta`-moments cannot beat `E[Xi]` by the margin the coefficients allow.

Why this is not self-improving: `U` and `V` are both *decreasing* functions of `eta` on
**overlapping** coordinate sets, so negative association — even if it were known — says nothing
about the sign of `Cov(U,V)`.

## 3. Three complete cases (PROVED, exactly machine-verified)

**Corollary A (bridges).** If `e` is a bridge of `G` then `omega_e` is independent of everything
else, with odds `p_e / (q(1-p_e))`. *Proof.* `k(omega) = k(omega - e) - omega_e` for every
`omega`, so the weight is `q^{k(omega - e)} (w_e/q)^{omega_e}` and factorises. QED

**Corollary B (parallel pair).** If `e` and `f` join the same two vertices `u,v`, then for every
host graph, all edge weights and all `q < 1`, `Cov(omega_e, omega_f) <= 0`.
*Proof.* Only types `(0,0,0)` (when `u ~ v` in `eta`) and E (when `u !~ v`) occur, so with
`alpha = P(u ~ v in eta)` we have `U = V = Xi = 1 - 1{u~v}` and (*) collapses to

    Cov = ( (1-alpha) x y (1-x)(1-y)(1-r) / Z_E^2 ) * [ r + alpha (1-x)(1-y)(1-r) ].

The prefactor is `<= 0` because `1 - r < 0`. The bracket equals `r - alpha (1-x)(1-y)(r-1) > 0`
because `alpha <= 1`, `(1-x)(1-y) < 1` and `r - 1 < r`. QED

**Corollary C (series pair).** If `e = {a,v}`, `f = {v,b}` and `v` is incident to no other edge of
`G`, then for every host graph, all edge weights and all `q < 1`, `Cov(omega_e, omega_f) <= 0`.
*Proof.* In `eta` the vertex `v` is isolated, so `delta_e = delta_f = 1` always; type E occurs
exactly when `a ~ b` in `eta`, and otherwise the type is `(1,1,2)`. With `alpha = P(a !~ b)`,
(*) collapses to a two-state computation and `Cov <= 0` is equivalent to

    alpha * x y r (r-1)  <=  (1 - x + x r)(1 - y + y r),

whose right side is at least `x r * y r = x y r^2 > x y r (r-1) >= alpha x y r (r-1)`. QED

**Corollary D (strictness).** In B and C the inequality is strict exactly when `e` and `f` lie in
a common block of `G` (equivalently, some cycle of `G` contains both); otherwise the covariance is
exactly zero. Type E has positive probability iff `e` and `f` lie on a common cycle; when it has
probability zero the two edges are conditionally independent given `eta` and the whole measure
factorises across blocks.

**Machine check.** `code/corollary_check.py`: 152 parallel-pair and 160 series-pair instances on
random multigraphs with up to 7 vertices and 12 edges, random rational weights from
`{1/10, ..., 9/10}`, `q in {1/10, 1/3, 3/4, 9/10}`, all in exact rational arithmetic. Every case
has `Cov <= 0`; every case with `Cov = 0` has `e,f` in different blocks (28 of 312) and every case
with `Cov < 0` has them in the same block (284 of 312). No anomalies.

A structural consequence worth recording: **type E has positive probability whenever `e` and `f`
lie in a common block**, so the negative term in (*) is never absent in a non-trivial instance.
Any counterexample must be a quantitative one; there is no configuration in which the positive
terms act alone.

## 4. Counterexample search (NUMERICAL EVIDENCE ONLY — none found)

Three searches, each with a positive control.

*(a) Uniform-parameter grid.* All connected graphs up to isomorphism on at most 6 vertices with at
most 10 edges (124 graphs), all edge pairs, `p` on an 11-point grid in `(0,1)`, `q` on a 13-point
grid in `(0,1)` down to `q = 0.001`. Largest covariance found: `2.2e-16`, i.e. zero to machine
precision. (`code/scan_mono.py`.)

*(b) Arbitrary edge weights.* For every connected graph up to isomorphism on at most 6 vertices
with at most 9 edges (109 graphs) and every one of the 2,356 edge pairs, the covariance was
*maximised* over all `m`-parameter weight vectors and over `q in (0,1)` by multi-start coordinate
hill-climbing (6 restarts, 200 sweeps). Largest covariance over the whole search: `8.9e-16`.
(`code/wsearch_np.py`.)

*Positive control for (b).* The identical optimiser with `q > 1` allowed finds `Cov = +0.1588` on
a 5-vertex, 7-edge graph. The search has room to fail, so the null result is informative — but it
is a local search, so it is evidence, not proof, even on those graphs.

*(c) Theory-guided gadget.* Section 2 says a counterexample needs `Cov(U,V) > 0` with `Xi` rare —
the two connection events `{a <-> b}` and `{c <-> d}` positively correlated in `eta` while the
cross-connections `a ~ c`, `b ~ d` stay unlikely. The natural construction makes the two
connections share a single edge: `H` = the tree `a-u, u-v, v-b, c-u, v-d`, with `e = {a,b}` and
`f = {c,d}`; under a product measure `Cov(U,V) > 0` strictly. Maximising over all seven weights and
`q` gives `5.6e-16` — no violation. The reason is visible in the construction: in a tree, if the
`a-b` path and the `c-d` path share an edge `g`, then the configuration in which only `g` is shut
has `a ~ c` and `b ~ d`, so type E is forced to be *likely* exactly when the connection events are
most strongly coupled. That tension looks structural, and it is the best heuristic reason I have
for believing the conjecture.

## 5. A certificate that FAILS, and why that is worth recording

The cheapest possible proof for a fixed graph over the whole parameter range would be a
coefficient certificate: substituting `w_e = p_e/(1-p_e)` in `(0,inf)` and `s = 1-q` in `(0,1)`,
`Cov * Z^2` is a polynomial in `(w_1,...,w_m, s)` with integer coefficients, and all coefficients
`<= 0` would give the result for all weights and all `q < 1` at once.

Machine result (`code/exact_cert.py`, sympy, exact): **the certificate fails already on the
triangle.** For two edges of `K_3` the polynomial has exactly three positive coefficients (at
`w_e w_f w_g^2 s^2`, `w_e w_f w_g s^4`, `w_e w_f w_g s^2`, with coefficients 2, 1, 3); on `K_4`
each edge pair has 87 positive coefficients. So the inequality is genuinely cancellative in these
variables and any proof must use a pairing or an injection, not term-by-term positivity. This is
the first thing anyone would try, and it does not work.

The natural pairing comes out of the two-copy identity

    2 Cov * Z^2 = sum over (omega1, omega2) with f in omega1, f not in omega2 of
        ( 1{e in omega1} - 1{e in omega2} ) ( W(omega1)W(omega2) - W(omega1 - f)W(omega2 + f) ),

where swapping `f` between the two copies changes the weight by exactly `q^{d1 - d2}` with
`d1 = 1{f is a cut edge of omega1}` and `d2 = 1{f joins two components of omega2}`. The swap is
weight-increasing for `q < 1` precisely when `d1 <= d2`, so the conjecture would follow from an
injection repairing the pairs with `d1 = 1, d2 = 0`. That is the Feder–Mihail-shaped obligation,
and it is where I stopped.

## Status

* Proposition 1 and the decomposition (*): **proved**, machine-verified exactly (83,310 cases).
* Corollaries A, B, C, D: **proved**, machine-verified exactly (312 random instances). These are
  elementary; I could not find them stated anywhere, but they may well be folklore. They are not
  the conjecture.
* No counterexample on any graph with at most 6 vertices and at most 9–10 edges, for arbitrary
  edge weights and arbitrary `q < 1`: **numerical evidence only**.
* The coefficient certificate: **refuted** (exact symbolic computation).
* The conjecture itself: **no progress** — the remaining obligation is the bound on the four
  `eta`-moments in (*), equivalently the injection repairing the `d1 = 1, d2 = 0` pairs.

## The strongest case that I am wrong

The corollaries are the load-bearing claims. The way they could be wrong is that the
`eta`-marginal is a *tilted* measure, not the random-cluster measure on `H`, and I used only
`0 <= alpha <= 1` about it — if I had silently used more, the proofs would be circular. They do
not: read the two displayed inequalities, neither mentions `eta` beyond `alpha`. The other risk is
that Proposition 1's case list is incomplete, which would invalidate the collapse in B and C; the
83,310-case exact check is what covers that, and it found exactly five types and no sixth.

The concrete check that would settle the remaining step: establish a lower bound on `P(type E)` in
terms of `Cov(U,V)` under the tilted measure. That is a finite statement about four marked
vertices in a random-cluster measure, so it can be tested by machine on small graphs before it is
attempted by hand.
