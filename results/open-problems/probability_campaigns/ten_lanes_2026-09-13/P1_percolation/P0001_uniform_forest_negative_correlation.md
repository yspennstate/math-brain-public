# P0001 — negative correlation of two edges in a uniform forest (Grimmett's Conjecture 4.2)

13 September 2026.

## The problem

Let `G` be a finite (multi)graph and let `F` be a uniformly chosen acyclic edge subset of `G`
(a "uniform forest"; all acyclic subsets, not only spanning trees, and all equally likely).
Conjecture: for distinct edges `e, f`,

    Cov( 1{e in F}, 1{f in F} )  <=  0.

Equivalently, with `N(G)` the number of acyclic subsets of `G` (`= T_G(2,1)`) and `G/e` the
contraction (loops deleted),

    N(G) * N(G/e/f)   <=   N(G/e) * N(G/f).                                     (C)

Ledger record: P0001, `grimmett_2022_selected`, Conjecture 4.2. Existing campaign attempt
P0001-A001 proves the statement for cactus graphs and stops at "overlapping cycle constraints do
not factor".

## Literature check (13 Sep 2026)

* G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected
  graphs*, Random Structures & Algorithms 24 (2004) 444–460; arXiv:math/0302185, abstract fetched.
  They verified the conjecture **computationally for all graphs with at most 8 vertices, and for
  9-vertex graphs with at most 18 edges** (their Theorem 1.5). The reported running times were
  about 40 minutes for the 8-vertex case and about 140 hours for the 9-vertex, 18-edge case on
  2003 hardware.
* Pengfei Tang and Zibo Zhang, *Pairwise Negative Correlation for Uniform Spanning Subgraphs of
  the Complete Graph*, arXiv:2603.10738 (11 Mar 2026), abstract fetched: pairwise negative
  correlation is proved for several uniform spanning-subgraph families **on K_n for n large**,
  including the first proof for uniform connected subgraphs. Not a general-graph resolution.
* No counterexample is reported. No computational verification beyond the 2004 range was found.
  Negative searches: "uniform forest conjecture counterexample"; "negative association uniform
  forest computer search 2026"; "Grimmett Winkler conjecture resolved".

Status as of today: **open** for general graphs.

## 1. An exact covariance identity (PROVED, machine-verified exactly)

Condition on `eta`, the restriction of `F` to `E \ {e,f}`. Set

    A_e = 1{ eta + e is acyclic },   A_f = 1{ eta + f is acyclic },
    B   = 1{ eta + e + f is acyclic },   Xi = A_e A_f - B.

`Xi = 1` exactly when each of `e, f` can be added to `eta` alone but not both together — i.e.
when `eta + e + f` contains a cycle through both. The number of allowed extensions is
`N(eta) = 1 + A_e + A_f + B`, and

**Proposition 1.** Conditionally on `eta`, `1{e in F}` and `1{f in F}` are *independent* unless
`Xi = 1`, in which case the conditional covariance is exactly `-1/9`, and

    E[ 1{e in F} | eta ] = (1/2) A_e - (1/6) Xi,   E[ 1{f in F} | eta ] = (1/2) A_f - (1/6) Xi.

*Proof.* The four conditional weights are `1, A_e, A_f, B` on `S = {}, {e}, {f}, {e,f}`. If
`B = A_e A_f` the table factorises as `(1 + A_e)(1 + A_f)/(1 + A_e)(1 + A_f)`-style, giving
independence (check the four cases: `A_e=A_f=B=1` gives `N=4` and covariance `1/4 - (2/4)(2/4) = 0`;
`A_e=1, A_f=0` gives `N=2` and covariance `0 - (1/2)(0) = 0`; `A_e=A_f=0` is deterministic). If
`Xi = 1` then `A_e = A_f = 1`, `B = 0`, `N = 3` and the covariance is `0 - (1/3)(1/3) = -1/9`. The
conditional means read off the same table. QED

**Corollary (the identity).** With every moment taken under the `eta`-marginal of the uniform
forest measure — which is the uniform measure on forests of `G - e - f` *tilted by* `N(eta)` —

    Cov( 1{e in F}, 1{f in F} )
        =  -(1/9) E[Xi]
         + (1/4) Cov(A_e, A_f)
         - (1/12) ( Cov(A_e, Xi) + Cov(A_f, Xi) )
         + (1/36) Var(Xi).                                                      (I)

**Machine check.** `code/uf_identity.py` computes both sides in exact rational arithmetic for
every connected graph up to isomorphism on 3 to 6 vertices with at most 8 edges and every pair of
distinct edges: **1,600 edge pairs, 0 failures**, and 0 positive covariances.

Identity (I) is the exact analogue of the decomposition obtained for the random-cluster model with
`q < 1` in the companion memo `C0091_fk_negative_correlation_q_below_one.md`, with the FK
coefficients replaced by absolute rational constants. The whole content of the conjecture is that
`(1/4) Cov(A_e, A_f)` — where `A_e`, `A_f` are two *decreasing* events on **overlapping** edge sets
— cannot beat `(1/9) E[Xi]` plus the two cross terms.

## 2. Two complete cases (PROVED)

**Corollary A (parallel pair).** If `e` and `f` join the same two vertices then `Cov <= 0` for
every host graph, with equality only when `E[A_e] = 0`.
*Proof.* `A_e = A_f = 1{u !~ v in eta}` and `B = 0` always (two parallel edges make a cycle), so
`Xi = A_e = A_f =: A`. Then (I) reads

    Cov = -(1/9) E[A] + (1/4) Var(A) - (2/12) Var(A) + (1/36) Var(A)
        = -(1/9) E[A] + (1/9) Var(A)
        = -(1/9) E[A]^2   <=  0,

using `Var(A) = E[A](1 - E[A])`. QED — and the value is exactly `-(1/9) E[A]^2`, a clean formula.

**Corollary B (series pair).** If `e = {a,v}`, `f = {v,b}` and `v` is incident to no other edge of
`G`, then `Cov <= 0` for every host graph.
*Proof.* In `eta` the vertex `v` is isolated, so `A_e = A_f = 1` identically and `B = 1{a !~ b}`,
`Xi = 1{a ~ b in eta}`. The two covariance terms involving `A_e, A_f` vanish (they are constants),
so with `t = E[Xi]`,

    Cov = -(1/9) t + (1/36) t(1-t) = - t (3 + t) / 36   <=  0,

strictly negative unless `t = 0`. QED

**Corollary C (bridges).** If `e` is a bridge of `G` then `1{e in F}` is independent of everything
else: `A_e = 1` identically and `Xi = 0`, so every term of (I) vanishes. (Directly: the forests of
`G` are the forests of `G - e` with or without `e`, so `e` is a fair coin independent of the rest.)

**Corollary D (strictness).** In general, `Xi` has positive probability iff `e` and `f` lie on a
common cycle of `G`, i.e. in a common block; otherwise the measure factorises across blocks and
`Cov = 0` exactly. So the negative term in (I) is present in every non-trivial instance, and any
counterexample must be quantitative.

These are elementary and I could not find them stated in the literature, but they may be folklore;
they are certainly not the conjecture. The point of recording them is that they are the exact
analogues of the FK statements, which is evidence that the identity (I) is the right frame.

## 3. Search beyond the Grimmett–Winkler range (NUMERICAL EVIDENCE ONLY)

The verified range in the literature is 8 vertices, or 9 vertices with at most 18 edges (2004).
I built an exact integer forest counter that avoids the `2^m` enumeration: for a multigraph on
vertex set `V`,

    N(G) = f(V),   f(S) = sum over blocks B of S containing min(S) of tau(G[B]) f(S - B),

with `tau` the spanning-tree count of the induced sub-multigraph by Kirchhoff's theorem, computed
with a fraction-free (Bareiss) integer determinant — so the whole computation is exact integer
arithmetic and costs `O(3^n)` rather than `O(2^m)`. Validated against brute-force enumeration on
all 109 connected graphs up to isomorphism on at most 6 vertices with at most 9 edges: 0 mismatches
(`code/forests.py`).

The search (`code/uf_search.py`) samples random connected graphs on 9 and 10 vertices at densities
0.25 to 0.85 — so including the 19-to-45-edge range the 2004 computation did not reach — and tests
`(C)` exactly on random edge pairs. Result: see `uf_search.log` in this directory. No
counterexample was found. Harness controls: the two-bridge path returns exactly 0 and three
parallel edges return a strictly negative value, as Corollaries A and C require.

This is a sample, not an exhaustive verification, so it is **evidence only**; it does not extend
the theorem of Grimmett and Winkler. What it does do is put the untested dense 9- and 10-vertex
regime under some pressure for the first time.

## Status

* Proposition 1 and identity (I): **proved**, machine-verified exactly on 1,600 edge pairs.
* Corollaries A–D: **proved**. Corollary A gives the exact value `-(1/9) E[A_e]^2` for a parallel
  pair, which is more than a sign.
* The conjecture: **no progress**. The remaining obligation is a bound on `Cov(A_e, A_f)`, the
  covariance of two decreasing connection-failure events on overlapping edge sets, under the
  tilted uniform-forest measure on `G - e - f`.
* Dense 9- and 10-vertex search: **numerical evidence only**, no counterexample.

## The strongest case that I am wrong, and the one check that settles it

The load-bearing claim is Proposition 1, and the way it fails is if the conditional table can take
a shape I did not enumerate — for instance if `B = 1` while `A_e = 0`. It cannot: `eta + e + f`
acyclic forces `eta + e` acyclic. The exact 1,600-pair check is what covers the rest, and it uses a
completely independent brute-force computation of the left-hand side, not a rearrangement of the
right.

The concrete next check: identity (I) makes `Cov(A_e, A_f)` the only quantity to bound. Test on
small graphs whether

    Cov(A_e, A_f)  <=  (4/9) E[Xi]  +  (1/3)( Cov(A_e,Xi) + Cov(A_f,Xi) )  -  (1/9) Var(Xi)

is ever tight, and where. If the slack is uniformly bounded away from zero except in a recognisable
family, that family is the theorem to prove.
