Runtime identification: **GPT-5.6 Sol; reasoning telemetry UNVERIFIED — not GPT-6 maximum.**

# HARD7-04 idea checkpoint — from MD5 to an actual one-collar diameter bound

Fresh moves remain **B9 RANDOMIZE, B12 FIND WHAT IS CONSERVED, B28 REPLACE FOR ALL WITH TYPICAL** for this bounded run. This checkpoint extends the already committed five-mark early-awakening route. It is not a closure claim.

## Setup carried from the MD5 checkpoint

Work in the explicit Pareto-quantile configuration-model subclass already fixed by HARD7-04. Write

- `r=tau-1 in (2,3)`, `beta=r-2=tau-3`, `eta=beta/r`;
- `epsilon_n=lambda_n n^{-eta}` with `lambda_n=(log n)^3`;
- `p_n=(1+epsilon_n)/nu_n`;
- `p_n^+=[1+(1+delta)epsilon_n]/nu_n`, where `0<delta<beta`;
- `Delta_n=p_n^+-p_n=delta epsilon_n/nu_n`.

The 20:30Z colored-matching checkpoint showed that after splitting edges into colors `A` (weight `<=p_n`), `B` (`p_n<weight<=p_n^+`), and `C`, the lower `A`-graph and future `B` matching can be generated in the order that makes the `B` matching fresh after the `A` principal component is known. The 21:30Z checkpoint proves the five marked outside-giant moment estimates MD5 at error `o_P(epsilon_n n)`.

Consequently, on an event of probability `1-o(1)`, the actual two-type nonbacktracking reproduction matrix for the `(A,B)` collar outside the lower `A` principal component is entrywise

`Mhat_n = h_n'(q_n) [[p_n, Delta_n],[p_n, Delta_n]] + o(epsilon_n)`.

The finite-`n` duality calculation from 18:30Z gives

`p_n h_n'(q_n)=1-(beta+o(1))epsilon_n`,

while `Delta_n h_n'(q_n)=(delta+o(1))epsilon_n`. Hence for some fixed `c_0>0`, for example any `c_0<(beta-delta)/2`,

`max_i sum_j Mhat_n(i,j) <= 1-c_0 epsilon_n`                                      (1)

with probability tending to one.

This checkpoint turns (1) into an actual geometric statement.

## Counterexample pressure first

A spectral-radius calculation alone does not rule out a long thin component: a rare sequence of pairings could in principle create a path much longer than the reciprocal drift scale. The relevant negation is therefore

> even though the collar is subcritical on average, there exists with non-vanishing probability a vertex-simple outside-collar path of length much larger than `epsilon_n^{-1} log n`.

The uniform-matching structure defeats this route by an exact path count. This is stronger and safer than inferring diameter directly from a branching-process heuristic.

## Conditional multitype path count

Condition on the complete colored half-edge profile and on the lower principal component, restricted to a good event on which MD5 and (1) hold. Let `L_A^out,L_B^out` be the outside half-edge totals of colors `A,B`. Their scales are

`L_A^out=Theta(n)`,

`L_B^out=Theta(Delta_n n)=Theta(epsilon_n n)`.

Conditional on the colored half-edge sets, the `A` and `B` restrictions are independent uniform perfect matchings. Let `N_ell` be the number of oriented vertex-simple paths of length `ell` contained entirely in the outside `(A,B)` collar graph.

For a fixed candidate path whose edge-color word uses `m_A` edges of color `A` and `m_B` of color `B`, the probability that all its required disjoint pairings occur is exactly

`prod_{j=0}^{m_A-1}(L_A^out-(2j+1))^{-1} * prod_{j=0}^{m_B-1}(L_B^out-(2j+1))^{-1}`.      (2)

The denominator correction relative to sampling with replacement is harmless on the logarithmic subcritical scale. Take

`ell_n=ceil(K epsilon_n^{-1} log n)`.

Then

`ell_n^2/L_A^out -> 0`,

and, crucially,

`ell_n^2/L_B^out
 = O(epsilon_n^{-3} (log n)^2/n)
 = O(n^{3 eta-1}/(log n)^7)
 -> 0`,                                                         (3)

because `eta=(tau-3)/(tau-1)<1/3` and `epsilon_n=(log n)^3 n^{-eta}`.

Thus the exact factors in (2), uniformly over all color words of length at most `ell_n`, differ from the corresponding with-replacement products by a multiplicative `1+o(1)`.

Now sum over candidate paths. Dropping the distinct-vertex restriction only increases the count. The resulting unrestricted first-moment recursion is precisely multiplication by the two-type mean matrix `Mhat_n`. Since the total number of possible oriented starting half-edges is `O(n)`, (1)--(3) give

`E[N_ell | good profile]
 <= C n (1+o(1)) (1-c_0 epsilon_n)^(ell-1)`                    (4)

uniformly for `ell<=ell_n`.

Choose `K>3/c_0`. Then at `ell=ell_n`,

`E[N_ell_n | good profile]
 <= C n exp[-c_0 epsilon_n ell_n+o(1)]
 <= n^{-1-o(1)}`                                               (5)

(after increasing `K` if needed). Markov's inequality therefore gives

`P(N_ell_n>0 | good profile)=o(1)`.

Any component of graph diameter at least `ell_n` contains a shortest path of length `ell_n`, hence a vertex-simple path counted by `N_ell_n`. Therefore

`Delta_max(outside one-collar graph)
 = O_P(epsilon_n^{-1} log n)`.                                 (6)

For the retained mesoscopic scale,

`epsilon_n^{-1} log n
 = n^eta/(log n)^2
 = o(n^eta)`.                                                   (7)

So one genuine postcritical collar contributes only `o_P(n^eta)` graph-distance diameter outside the lower giant.

## What has actually been removed

The previous immediate obstruction was: even after MD5, does a subcritical two-type spectral margin really imply a geometric diameter bound in the finite colored configuration model? Equations (2)--(7) answer yes for this one collar, without treating the matrix as an independent Galton--Watson process and without replacing the finite matching by a simulation.

No finite exhaustive claim is made, so no checker is warranted. The proof is analytic and is written on the page.

## New exact blocker

The remaining source-level obstacle is no longer MD5 or a one-collar diameter estimate. It is the configuration-model analogue of the rank-one upper-MST approximation theorem: one needs control that is uniform across the Kruskal levels, in the source order of limits. A clean target is

`lim_{lambda->infinity} limsup_{n->infinity}
 P(n^{-eta} d_H(M_{n,lambda},M_n)>varepsilon)=0`               (8)

for every `varepsilon>0`, where `M_{n,lambda}` is the MST structure captured up to a fixed critical-window level `lambda` under the source normalization.

The present result treats a single mesoscopic collar with `lambda_n=(log n)^3`; it does not justify passing from every fixed large `lambda` through an entire geometric ladder to the full MST. That uniform attachment/Hausdorff step is the remaining source-style obstruction.
