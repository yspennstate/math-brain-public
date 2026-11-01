# PROB10-07 idea before checker: complete split graphs beyond the current split-5 frontier

Runtime request: GPT-6 maximum. Authenticated model/effort telemetry is unavailable, so runtime model/effort are **UNVERIFIED** and no selector change is claimed.

Parent target: Grimmett-Winkler pairwise negative edge correlation for the uniform measure on **all forests** of a finite graph. Parent status remains OPEN/PARTIAL.

## Nonoverlap and inherited state

Read before choosing scope:

- `operations/PROB10_2026-09-20.md`;
- current `POSTED.md`;
- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- own preceding `runs/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2.md`;
- current NM13-04 split-family follow-ups, including the already-owned `K_3 join I_n`, `K_4 join I_n`, and stronger one-port-field `K_5 join I_n` results.

Therefore this run does **not** claim `m=3,4,5`, does not repeat P14/HARD10 graph-order enumeration, and does not seize NM13's split-5/PF claim. The precise fresh scope is the unit-weight all-forest sign problem for

`K_m join I_n`, with `m=6,7,8,9` and arbitrary `n>=1`.

## Three materially different routes

### A. Port-field continuation from NM13 split-5

Try to extend the stronger one-port-field theorem from `m=5` to `m>=6`. This would be stronger than the unit target, but the stabilizer-orbit count and field-quadratic sign analysis grow sharply and there is no reason coefficientwise positivity should persist. This route is valuable but is not the bounded target here.

### B. Symmetry quotient aimed at all clique widths

Use `S_m` symmetry on terminal partitions, refined only by the at most four clique vertices touched by a marked edge pair. This could potentially yield an all-`m` theorem, but it requires proving simultaneous strong lumpability for the unmarked and every forced-spoke operator. That proof is not assumed.

### C. Cayley core vectors + exact full Bell transfer

This is the bounded route attempted now. For `G_{m,n}=K_m join I_n`, process the independent-side vertices through the partition lattice of the clique terminals. The fresh-vertex operator is

`M=(m+1)I+N`, with `N^m=0`,

because the empty spoke set and the `m` singleton spoke choices preserve the current partition, while every other legal spoke set strictly coarsens it.

The key improvement over brute core enumeration is an exact Cayley formula. For a terminal partition `pi` and a required acyclic set `R` of clique edges, the number of clique forests realizing `pi` and containing `R` factors over blocks `B` of `pi`. If `R_B` has component sizes `s_1,...,s_c` inside a block of size `q`, then the number of spanning trees of `K_q` containing `R_B` is

`q^(c-2) * product_i s_i`.

This is the standard contraction form of Cayley's formula. Thus all initial marked vectors are exact without iterating `2^(m choose 2)` clique subsets. That makes widths 8 and 9 accessible in a bounded exact run.

Under `S_m x S_n`, every distinct edge pair lies in exactly one of seven orbits: adjacent clique/clique; disjoint clique/clique; clique/spoke incident; clique/spoke nonincident; two spokes at one independent vertex; two spokes at different independent vertices with the same clique endpoint; two spokes at different independent vertices with different clique endpoints.

If an orbit touches `k=0,1,2` independent vertices, expose those vertices first and put `x=n-k`. Each marked count is `(m+1)^x` times a polynomial in `x` of degree at most `m-1`, hence each Rayleigh difference is `(m+1)^(2x)` times a polynomial of degree at most `2m-2`. The exact sign certificate sought is nonnegative monomial coefficients plus strict positivity at the first physical `x`.

No universal claim is made unless all arbitrary graphs are covered. A successful result here is a new infinite structural class only.