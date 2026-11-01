# P0150 structural lemma: degree-two corridors are logarithmic

This note isolates one source-specific obstruction to upgrading the heavy-tailed critical configuration-model scaling limit from Gromov-weak to Gromov–Hausdorff–Prokhorov convergence.

## Setup

Let `CM_n(d)` be the configuration model with deterministic degree sequence `d=(d_v)_{v in [n]}` and even total number of half-edges

`ell_n := sum_v d_v`.

Let

`N_2(n) := #{v : d_v=2}`

and let `L_n` denote the maximum number of consecutive degree-two vertices occurring on a simple path in the resulting multigraph. Assume

`N_2(n)/n -> p_2`,  `ell_n/n -> mu in (0,infinity)`

and set

`q := 2p_2/mu < 1`.

In the heavy-tailed critical source regime the limiting degree law is not concentrated at degree two, so `q<1`. If `q=0`, use the convention `1/(-log q)=0` below.

## Theorem 1 — exact geometric tail from pairing exposure

For all sufficiently large `n`, put

`q_n := 2N_2(n)/(ell_n-1) < 1`.

Then for every integer `r>=1`,

`P(L_n >= r) <= ell_n q_n^(r-1)`.

Consequently, for every

`c > 1/(-log q)`

when `q in (0,1)`,

`P(L_n > c log n) -> 0`.

If `q=0`, the same conclusion holds for every `c>0`. Thus, for

`C_2^+ := inf{c>0 : P(L_n <= c log n) -> 1}`,

we have

`C_2^+ <= 1/(-log q)`

with the convention above.

### Proof

Fix an oriented half-edge `h` incident to a degree-two vertex and expose the random perfect matching by following the degree-two corridor beginning in the direction `h`. Whenever the current active half-edge is paired to a half-edge at a previously unvisited degree-two vertex, continue through the other half-edge of that vertex. Stop as soon as the mate is not at a fresh degree-two vertex or the walk would fail to remain simple.

Suppose `j` successful pairings to fresh degree-two vertices have already occurred. Before the next pairing there are `ell_n-2j-1` possible mates for the current active half-edge. The number of eligible half-edges belonging to as-yet unvisited degree-two vertices is at most

`2N_2(n)-2j`.

Therefore the conditional probability of one further successful degree-two step is at most

`(2N_2-2j)/(ell_n-2j-1)`.

For all sufficiently large `n`, `2N_2 <= ell_n-1` because `q_n->q<1`. Under this inequality,

`(2N_2-2j)/(ell_n-2j-1) <= 2N_2/(ell_n-1) = q_n`.

Indeed, after cross-multiplication the difference between the right and left products is

`2j(ell_n-1-2N_2) >= 0`.

Hence, for a fixed oriented degree-two starting half-edge, the probability that the exploration traverses at least `r` consecutive degree-two vertices is at most `q_n^(r-1)`. Any simple path containing `r` consecutive degree-two vertices supplies at least one such oriented starting half-edge. There are at most `2N_2 <= ell_n` possible starts, so the union bound gives

`P(L_n >= r) <= ell_n q_n^(r-1)`.

Because `N_2/n->p_2` and `ell_n/n->mu`, we have `q_n->q`. If `q in (0,1)` and `c>1/(-log q)`, choose `qbar in (q,1)` close enough to `q` that

`c(-log qbar)>1`.

Eventually `q_n<=qbar` and `ell_n=O(n)`. With `r=ceil(c log n)`,

`P(L_n>=r) <= O(n) qbar^(c log n-1) = O(n^(1-c(-log qbar))) -> 0`.

If `q=0`, then for each fixed `c>0` choose `qbar>0` so small that `c(-log qbar)>1`; eventually `q_n<=qbar`, and the same argument applies. This proves the theorem. QED.

## Corollary 2 — degree-two pipes disappear on the heavy-tailed metric scale

Let

`eta := (tau-3)/(tau-1) > 0`,  `tau in (3,4)`.

Then

`n^(-eta) L_n -> 0`

in probability.

### Proof

Theorem 1 gives `L_n=O_P(log n)`, while `log n=o(n^eta)`. QED.

## Lemma 3 — deterministic suppression is GHP-small

Let `C` be a finite connected multigraph. If every vertex of `C` has degree two, set `S(C)=C`. Otherwise suppress each maximal chain of degree-two vertices to a weighted edge whose length equals the number of original graph edges in that chain. Let `S(C)` have vertex set consisting of the unsuppressed vertices and shortest-path metric induced by these edge lengths. Let `pi:C->S(C)` map each unsuppressed vertex to itself and every suppressed degree-two vertex to a nearest endpoint of its chain. For any finite measure `mu_C` on the vertices, give `S(C)` the push-forward measure `pi_*mu_C`.

If `L(C)` is the largest number of consecutive degree-two vertices on a simple path of `C`, then, under the usual max-type GHP convention,

`d_GHP((C,d_C,mu_C),(S(C),d_S,pi_*mu_C)) <= L(C)`.

Under conventions that sum Hausdorff and Prokhorov errors, the conservative bound `<=2L(C)` holds.

### Proof

Distances between unsuppressed vertices in `S(C)` equal their distances in `C`: suppressing a degree-two chain replaces it by an edge of exactly the same length, and paths expand/collapse without changing length. Thus `(S(C),d_S)` can be isometrically identified with the subset of unsuppressed vertices in `(C,d_C)`.

Every suppressed vertex lies on a degree-two chain with at most `L(C)` degree-two vertices, so

`d_C(x,pi(x)) <= L(C)`.

Therefore the Hausdorff distance from `C` to the embedded `S(C)` is at most `L(C)`. Coupling the mass at each `x` with its image `pi(x)` transports every unit of mass by distance at most `L(C)`, so the Prokhorov distance between `mu_C` and `pi_*mu_C` in the same ambient space is at most `L(C)`. The stated GHP bounds follow. QED.

Combined with Corollary 2, suppressing all degree-two corridors changes each rescaled component by `o_P(1)` in GHP distance at the source scale `n^(-eta)`.

## Corollary 4 — any macroscopic path must contain many non-degree-two vertices

Let `P` be a simple path and let `B(P)` denote the number of vertices on `P` whose degree is not two. The degree-two vertices of `P` form at most `B(P)+1` consecutive blocks, each of size at most `L_n`. Hence

`|V(P)| <= B(P) + (B(P)+1)L_n`.

Therefore, on an event where `L_n<=c log n`, any path with at least `delta n^eta` edges satisfies

`B(P) >= (delta n^eta - c log n)/(c log n+1)`

up to the harmless endpoint `+1` convention. In particular every macroscopic path contains `Omega(n^eta/log n)` non-degree-two vertices with high probability.

This rules out a canonical Gromov-weak/GHP failure mechanism: a critical component cannot carry an `n^eta`-scale thin tentacle consisting almost entirely of degree-two vertices. The unresolved obstruction is genuinely branching: long low-mass fringes with many non-degree-two vertices, matching the survival-tail bottleneck identified in the current source discussion.