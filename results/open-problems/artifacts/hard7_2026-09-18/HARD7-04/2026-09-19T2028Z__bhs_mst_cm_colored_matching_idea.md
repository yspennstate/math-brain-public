# HARD7-04 idea checkpoint — edge-color first, then dualize the collar

Runtime: GPT-5.6 Sol; reasoning telemetry UNVERIFIED. This is not a closure claim.

## Why change the representation

The STUCK1 blocker was phrased in terms of an `available-degree` ratio after a marked lower-threshold component exploration. That representation exposes pairings before edge weights and therefore makes higher-threshold half-edges look as though they are consumed by boundary discoveries. For iid continuous edge weights there is another exact order of generation: first color the edges by threshold interval, then pair within color classes. In that representation the lower-threshold graph can be generated without revealing any future-color pairing.

This is not an approximation. It is a finite symmetry identity for a uniform perfect matching.

Let `H` be `L=2m` labeled half-edges. Draw a uniform perfect matching `M`, and independently color each matched edge in classes `A,B,C` with probabilities

`p`, `Delta`, `1-p-Delta`,

where `A` means weight `<=p` and `B` means `p<weight<=p+Delta`. Let `N_A,N_B,N_C` be the edge counts of the three colors and let `H_A,H_B,H_C` be the incident half-edge sets.

**Exact colored-matching decomposition.** Conditional on `(N_A,N_B,N_C)=(a,b,c)`, the ordered partition `(H_A,H_B,H_C)` is uniform among all partitions of `H` of sizes `(2a,2b,2c)`. Conditional on that partition, the three restrictions of `M` are independent uniform perfect matchings on `H_A,H_B,H_C`.

Proof is by a bijection: a colored perfect matching with fixed color counts is exactly a choice of the three half-edge sets followed by a perfect matching in each set. Every such colored matching has the same unconditional probability `(2m-1)!!^{-1} p^a Delta^b (1-p-Delta)^c`, hence the conditional law is uniform.

Consequences:

1. the lower graph `G_A` is a configuration model on the random lower-color degrees `X_v=|H_A cap H(v)|`;
2. its principal component `C_A` is measurable with respect to `(H_A,M_A)` alone;
3. conditional on all lower-color data, `H_B` is a uniform sample of size `2N_B` from `H\H_A`, and `M_B` is a fresh uniform perfect matching on `H_B`;
4. therefore the future collar does **not** require a lower-exploration stopping-time coupling. The dependence that remains is a static marked-degree problem.

This directly ports the useful part of the van der Hofstad--Janson--Luczak continuous-time configuration-model technique while avoiding the marked stopping-time that caused STUCK1.

## Ideal marked dual algebra

Write the original deterministic degrees as `d_v`, total half-edge count `L=sum_v d_v`, and

`h_n(s)=(1/L) sum_v d_v s^(d_v-1)`.

To identify the deterministic target, first use the independent-stub surrogate `X_v~Bin(d_v,p)`. Put `R_v=d_v-X_v`. The size-biased excess pgf of `X` is

`H_p(s)=h_n(1-p+ps)`.

Let `psi` be its extinction root and put

`q=1-p+p psi`,

so `psi=h_n(q)`. Weight a vertex by `psi^(X_v)`, the usual dual weight for lying outside the giant of the lower-color configuration model.

Elementary differentiation of `(1-p+p psi)^d=q^d` gives the exact ideal identities

`S_A := sum E[X psi^X] = p L psi^2`,

`Q_A := sum E[X(X-1) psi^X] = p^2 L psi^2 h_n'(q)`,

`S_R := sum E[R psi^X] = (1-p) L psi`,

`T_AR := sum E[X R psi^X] = p(1-p) L psi h_n'(q)`,

`Q_R := sum E[R(R-1) psi^X] = (1-p)^2 L h_n'(q)`.

In particular the lower dual reproduction mean is exactly

`Q_A/S_A = p h_n'(q)`.

Now let the collar half-edge sampling fraction among non-`A` stubs be

`theta=Delta/(1-p)`.

At first order the outside `B`-stub mass is

`S_B,out = theta S_R = Delta L psi`,

while the total `B`-stub mass is `Delta L`. Thus a `B` stub based outside pairs to another outside `B` stub with asymptotic probability `psi`; this is the missing factor that cancels a spurious `1/psi` in a naive two-type calculation.

Use edge type `A` or `B` as the type of a nonbacktracking particle. With rows indexed by incoming edge type and columns by outgoing edge type, the ideal outside reproduction matrix is

`M_dual = [[p h_n'(q), Delta h_n'(q)],
           [p h_n'(q), Delta h_n'(q)]] + negligible finite-population terms`.

Indeed:

- `A->A = Q_A/S_A = p h_n'(q)`;
- raw `A->B` stub count is `theta T_AR/S_A = Delta h_n'(q)/psi`; multiplying by the outside-pairing fraction `psi` gives `Delta h_n'(q)`;
- `B->A = theta T_AR/(theta S_R)=p h_n'(q)`;
- raw `B->B = theta^2 Q_R/(theta S_R)=Delta h_n'(q)/psi`; again the outside-pairing fraction gives `Delta h_n'(q)`.

Therefore

`rho(M_dual) = (p+Delta) h_n'(q)`.

This recovers the analytic collar coefficient from the previous runs without ever requiring the scalar stopped-process identity `R_n^av=h_n'(q_n)+o_P(epsilon_n)`.

For the retained mesoscopic choice

`p_n=(1+epsilon_n)/nu_n`,

`p_n^+=[1+(1+delta)epsilon_n]/nu_n`,

`Delta_n=delta epsilon_n/nu_n`,

and the already proved finite-`n` Pareto duality

`p_n h_n'(q_n)=1-(tau-3+o(1))epsilon_n`,

we get formally

`rho(M_dual,n)=1-(tau-3-delta+o(1))epsilon_n`.

Hence the sharp collar barrier `delta<tau-3` survives in the correct two-color operator.

## What remains, now statically formulated

The old stopping-time blocker can be replaced by the following marked-dual profile statement for the ordinary lower-color configuration model. Let `C_A` be its principal component and retain the original degree mark `d_v` alongside `X_v`. It is enough to prove, for the explicit Pareto-quantile subclass and `epsilon_n=(log n)^3 n^{-eta}`, the five simultaneous estimates

`sum_{v notin C_A} X_v                         = p_n L_n psi_n^2 + o_P(epsilon_n n)`,

`sum_{v notin C_A} X_v(X_v-1)                  = p_n^2 L_n psi_n^2 h_n'(q_n) + o_P(epsilon_n n)`,

`sum_{v notin C_A} (d_v-X_v)                   = (1-p_n)L_n psi_n + o_P(epsilon_n n)`,

`sum_{v notin C_A} X_v(d_v-X_v)                = p_n(1-p_n)L_n psi_n h_n'(q_n) + o_P(epsilon_n n)`,

`sum_{v notin C_A} (d_v-X_v)(d_v-X_v-1)        = (1-p_n)^2 L_n h_n'(q_n) + o_P(epsilon_n n)`.

Call this the **five-moment marked dual profile** (MD5). Once MD5 holds, the `B`-color hypergeometric sample and fresh uniform `B` matching are static. Standard without-replacement concentration should then transfer the displayed two-type matrix with `o_P(epsilon_n)` operator error; the finite matching correction is `O(1/(Delta_n n))=o(epsilon_n)` because `eta<1/3`.

The nearest solved engine is van der Hofstad--Janson--Luczak (Random Structures & Algorithms 55 (2019), 3--55, DOI 10.1002/rsa.20837): their Section 5 continuous-time exploration makes the deterministic-time sleeping-degree counts independent binomials, and Remark 2.7 extracts degree counts in the barely supercritical giant. The new task is not to control a marked bond-percolation stopping time. It is to extend that ordinary-CM dual profile to the five deterministic vertex marks above at the `o(epsilon_n n)` scale.

## Scale sanity check for MD5

For the explicit cumulative tail `A_n(k)~C n k^{-(tau-1)}`, write `r=tau-1 in (2,3)`, `a=1/r`, `beta=r-2`, `eta=beta/r`. The extinction tilt has

`1-q_n = y_n = n^{-a} z_n`,

with `z_n -> infinity` and `epsilon_n asymp y_n^beta`. For a second-factorial mark, the independent deterministic-time surrogate has variance at most the scale

`n y_n^(r-4)`.

Thus its standard deviation divided by the required error scale `epsilon_n n = n y_n^beta` is

`[n y_n^(r-4)]^(1/2) / [n y_n^beta]
 = (n y_n^r)^(-1/2)
 = z_n^(-r/2) -> 0`.

So the static weighted concentration has the correct fluctuation margin. The unresolved issue is the transfer from deterministic sleeping indicators to the actual principal-component complement uniformly for these growing marks, not an impossible variance scale.

## Counterexample pressure on this route

The obvious scalar shortcut is false: deleting/consuming a low-degree half-edge can increase `Q/S`. The earlier report already exhibited this. The colored representation shows something stronger: the very need to expose future-color boundary pairings during the lower exploration is representation-dependent. Under the exact colored-matching decomposition there are no such revelations. Therefore `R_n^av=h_n'(q_n)+o_P(epsilon_n)` is not a canonical invariant that must be proved; MD5 plus the two-type operator is a different and strictly more modular route.

No source statement is refuted here. No movement of the frozen MST exponent is claimed until MD5 is proved and the Kruskal collar ladder is closed.