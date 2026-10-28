# FOREST separator transfer / induced-weight adversary report

Run: `20260922T004255Z-b03-forest`  
Account/slot: `account02/B03`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent FOREST conjecture: `OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Control and scope


The superseded brain-installation/benchmark role was not continued. Historical M1-M6/F01-F20 evidence is preserved unchanged and is not re-evaluated or promoted by this research run.

## 2. Exact inherited state consumed

The latest complete lead handoff consumed is account01/B01 `FOREST-SIMPSON-MATCHING-v1`, Git blob `498b6154449ed3028685e6c174cb5563b0478bde`. In a lexicographically minimal counterexample, a violating pair `{e,f}` has positive covariance, every third edge is strictly negatively correlated with both marked edges, positive-covariance pairs form a matching, and the lead obtains the quantitative Pearson bound recorded there. Its first requested bridge is to combine this geometry with the exact overlap/reconnection state.

Three exact separator/overlap dependencies were also consumed:
- account01/B03 blob `b49c6b896238cd62508b98549526dd12a469ceb3`: with `K=G-{e,f}`, forest cells `n_ij`, total `N`, and overlap reservoir `q`, the Rayleigh numerator is
  `Delta = n10*n01 - n00*n11 + N*q`;
- account01/B02 blob `4cc43cbb0b87369e550e4c3e0a5d7622181f109f`: marked 1-separation switching and exact 3-edge-cut injection, leaving a nontrivial 2-separator/fibre problem;
- account03/B03 blob `0358d8ad988f3abe17d3a80d4dd51befc5222fbb`: the `K_{3,m}` q-essential adversary and additive three-terminal coordinate `eta`, showing that triangle-only three-terminal compression loses information.

Named partner account03/B01 completed during this invocation. Its source-bound receipt is blob `c624439e9f684ea2d9ba8f4424511151c8e3abf5`. I consumed and apply its exact reported bridge: uniform unrooted forests admit an internal-activity-cube decomposition with basis weight `2^{i(T)}`, and its remaining obligation is an activity-weighted one-edge exchange inequality. The partner's referenced full report object was not reachable through the current connector snapshot, so I use only the receipt-level statement and do not claim to have reviewed its unavailable proof text.

## 3. Conditional end-to-end route

Combine the inherited overlap identity with separator recursion as follows.

1. Account01/B03 reduces the target for a marked pair to `n00*n11 <= n10*n01 + N*q`.
2. Account01/B02 handles marked 1-separations and cuts of size at most three by exact involution/injection.
3. The theorem below handles every proper vertex 2-separation exactly. Cross-side marked pairs factor into two smaller local Rayleigh numerators. Same-side marked pairs compress the opposite side to one boundary edge with an exact induced positive weight `lambda=C/D`; if the boundary edge already exists, that virtual edge is a parallel copy and must be merged by ADDING its weight, not by simplifying to one unit edge.
4. Thus a separator induction would be complete if one proves the one-boundary-edge weighted Rayleigh implication for the exact induced response values and then proves the eta-aware overlap inequality on the remaining 3-connected core. The first missing implication is now the weighted boundary-edge step, stated precisely in Section 8.

This is a conditional route, not a proof of the parent conjecture.

## 4. Exact two-separator factorization: cross-side marks

Let `G=A union B`, edge-disjoint, with `V(A) intersect V(B)={s,t}` and no other shared vertices. Put a marked edge `e` in `A` and a distinct marked edge `f` in `B`.

For side `A`, let `d_i^A` be the number of forests of `A` with `1_{e in F}=i` and with `s,t` disconnected, and `c_i^A` the corresponding number with `s,t` connected. Put `t_i^A=d_i^A+c_i^A`; define the analogous quantities for `B`.

A pair `(F_A,F_B)` has acyclic union iff it is not the case that both sides connect `s` to `t`. Therefore the global inclusion cells are exactly

`M_ij = d_i^A t_j^B + c_i^A d_j^B
      = t_i^A t_j^B - c_i^A c_j^B`.

Taking the 2-by-2 determinant gives the exact factorization

`R_G(e,f) := M_10 M_01 - M_00 M_11
           = delta_A(e;s,t) delta_B(f;s,t)`

with

`delta_A = d_0^A c_1^A - d_1^A c_0^A`,
`delta_B = d_0^B c_1^B - d_1^B c_0^B`.

If `st` is absent from `A`, then after adding a unit boundary edge `g=st`,

`delta_A = R_{A+g}(e,g)`.

If `st` already belongs to `A` and `e != st`, then

`delta_A = R_A(e,st)`.

If `e=st`, then `d_1^A=0`, so `delta_A=d_0^A c_1^A >= 0` automatically. The same statements hold for `B`.

Consequently, in a vertex-minimal simple-graph counterexample, a proper 2-separation cannot have the violating marked edges on opposite sides: each nondegenerate completed side has fewer vertices, and its local unit Rayleigh numerator is nonnegative by minimality (or is automatic in the boundary-mark case), so their product is nonnegative.

This closes the cross-side 2-separator case exactly.

## 5. Exact same-side compression and the induced parallel edge

Now let both marked edges `e,f` lie in `A`, initially assume neither is the actual boundary edge `st`. Let

`D_B = # {forests of B disconnecting s,t}`,
`C_B = # {forests of B connecting s,t}`,
`lambda_B = C_B / D_B`.

`D_B>0` because the empty forest is counted.

For a forest `F_A`, there are `D_B+C_B` compatible forests of `B` when `F_A` disconnects `s,t`, and only `D_B` when `F_A` connects them. Hence, cell by cell, the contribution of `B` is exactly the same as a virtual boundary edge `g=st` of weight `lambda_B`, multiplied by `D_B`:
- if `st` is absent from `A`, adjoin `g` with weight `lambda_B`;
- if `st` is already an unmarked edge of `A`, the virtual edge is parallel to it. Since a forest cannot contain both parallel copies and the marked events do not distinguish them, merge the copies into the existing boundary edge with total weight `1+lambda_B`.

Thus

`R_G(e,f) = D_B^2 R_{A_hat,lambda_B}(e,f)`,

where `A_hat` is the completed/weight-adjusted side just described.

There is also no hidden exceptional obstruction when one mark is the actual boundary edge. If `e=st` and `f` is another edge of `A`, write `D_j,C_j` for the disconnected/connected `s,t` counts in `A-st` with `f`-state `j`. Direct enumeration gives

`M_0j = D_B(D_j+C_j)+C_B D_j`,
`M_1j = D_B D_j`,

and the `C_B` terms cancel in the determinant:

`R_G(st,f) = D_B^2 R_A(st,f)`.

So a proper 2-separation can only remain difficult for a same-side pair not equal to the boundary edge, and then the only information the opposite side contributes is its exact scalar response `lambda_B`.

## 6. Exact response calculus and why unit-edge simplification is false

The two-terminal response `lambda=C/D` has exact series/parallel rules.

For parallel composition of edge-disjoint two-terminal pieces sharing only `{s,t}`, a forest can connect `s,t` through at most one piece. Therefore

`D_parallel = product_r D_r`,
`lambda_parallel = sum_r lambda_r`.

For series composition `B=B_1 o B_2` at a single articulation, every pair of side forests is compatible and the whole network connects iff both pieces connect. Hence

`lambda_series = lambda_1 lambda_2 / (1+lambda_1+lambda_2)`.

A single unit edge has `lambda=1`. A two-edge path has `D=3,C=1`, hence `lambda=1/3`. Therefore `k` internally-disjoint two-edge `s-t` paths in a simple graph have

`D=3^k`, `C=k 3^(k-1)`, `lambda=k/3`.

The induced boundary weight is therefore unbounded even inside finite simple graphs. Replacing a separator side by one UNIT edge is not an exact operation.

An even smaller parallel-edge warning comes from contraction. In a triangle with marked edge `e`, contracting `e` turns the other two edges into two parallel copies. Exactly three forests contain `e` in the original triangle (`{e}`, `{e,g}`, `{e,h}`), matching the three forests of the two-parallel-edge contraction (`empty`, first copy, second copy). Simplifying those copies to one unit edge leaves only two forests and destroys the count. The correct simple-edge representation, when the copies are unmarked, is one edge carrying the SUM of their weights.

## 7. Diamond / overlapping-cycle adversary

Take vertices `s,t,a,b` and edges

`st, sa, at, sb, bt`.

This is two triangles sharing the separator edge/path structure.

For cross marks `e=sa`, `f=sb`, the exact global inclusion cells are

`M = [[8,6],[6,4]]`, so `R_G(e,f)=4`.

The two side determinants are both `2`, giving `4=2*2`. Naively multiplying the side forest totals gives `7*4=28`, but the graph has only `24` forests: exactly four pairs connect `s,t` on both sides and their union contains a cycle.

In the account01/B03 overlap coordinates for the same marked pair,

`(N,n_00,n_10,n_01,n_11,q) = (8,1,1,1,5,1)`,

and indeed

`Delta = 1*1 - 1*5 + 8*1 = 4`.

So the overlap reservoir is already essential in this four-vertex separator.

For same-side marks `e=sa`, `f=at`, the opposite two-edge path has `(D,C,lambda)=(3,1,1/3)`. The triangle side already contains `st`, so its boundary weight becomes `1+lambda=4/3`. Exact values are

`R_G(e,f)=28`,
`R_triangle(weight(st)=4/3)=28/9`,
`D^2 R_triangle = 9*(28/9)=28`.

If one incorrectly collapses the opposite side to a unit boundary edge instead, the scaled value is only `9*2=18`. The sign happens to remain positive here, but the separator count is quantitatively wrong.

The family with `k` parallel length-two paths amplifies this: the exact boundary weight is `1+k/3`, and with the two non-boundary triangle edges marked,

`R_G = 9^(k-1) (k+3)(k+6)`.

The unit-collapse surrogate is `2*9^k`; their ratio is unbounded in `k`. Thus multiplicity/weight cannot be treated as a bounded perturbation.

## 8. Named-partner application: activity tilt and the first missing implication

The current account03/B01 receipt reports an internal-activity-cube representation of uniform unrooted forests with basis weight `2^{i(T)}` and reduces the remaining proof to a basis-exchange inequality.

The separator response above produces a precise one-parameter deformation of that representation. By the standard activity-interval partition of independent sets,

`Z(y) = sum_T [ product_{h in T\IA(T)} y_h ] [ product_{h in IA(T)} (1+y_h) ]`.

With all original weights equal to one and only the boundary edge `g` assigned weight `w>0`, the unit basis factor `2^{i(T)}` is multiplied by exactly

`r_w(T,g) = 1` if `g notin T`,
`r_w(T,g) = w` if `g in T\IA(T)`,
`r_w(T,g) = (1+w)/2` if `g in IA(T)`.

Thus the separator problem does not require an arbitrary new measure: it requires controlling the partner's activity-weighted exchange inequality under this explicit three-level tilt, at the induced `w=lambda_B` (or `w=1+lambda_B` when an existing unmarked boundary edge absorbs the parallel copy).

**First essential missing implication.** Prove that the needed edge-pair Rayleigh/exchange inequality survives every such separator-induced boundary tilt, or derive from a failure of that tilted inequality a third edge with positive covariance to one marked edge, contradicting the lead's matching/strict-external-negative geometry. This is the exact point at which the present argument stops.

The `K_{3,m}`/`eta` obstruction from account03/B03 remains mandatory after two-separator elimination: this report does not compress a genuine three-terminal separator to `lambda` and does not delete the `q` reservoir.

## 9. Exact computation and regression

The committed standard-library checker is `forest_separator_checker.py`, Git blob `bddc6ee61d7c85137cfe0d325fa00fd0d2aa812c`; local source byte count 6,644 and SHA-256 `3a7da5ef97191fb7ad833d9b58fec6f3da31859e0a47129569a960e4bde027e7`.

Its committed exact output is `forest_separator_checker.out`, Git blob `62384c0b20e92a33ecad23a8847bbdff845d4382`; local output byte count 744 and SHA-256 `3ea0f67a88e5cb57dc34b1cdda10c38214d7574b990181293d3fc3bed6dfc531`.

Checks passed:
- diamond cross factorization and overlap identity;
- same-side `lambda=1/3` compression and failure of unit replacement;
- triangle contraction parallel-edge multiplicity;
- 48 exhaustive tiny cross-separator instances, zero failures;
- 8 exhaustive tiny same-side weighted-compression instances, zero failures;
- the `k=1,...,5` parallel two-edge-channel response formula.

These computations are regression evidence only. The separator identities in Sections 4-6 are proved algebraically and do not depend on the finite check.

## 10. Failures, limits, and handoff state

No full proof is claimed. I attempted to strengthen the weighted step computationally by looking for a small one-boundary-edge positive-weight sign failure; no counterexample was found in the bounded local search used during derivation, so I do not promote either universal weighted Rayleigh or its negation from that search. The decisive result is instead the exact separator transfer and the explicit induced-weight adversary.

This run closes the cross-side proper 2-separator case for a vertex-minimal simple counterexample and reduces the same-side case to one exact scalar response. It does not solve the weighted boundary implication, the eta-aware three-terminal core, or the parent conjecture.

Scheduler observation for this account found all 20 managed slots enabled and hourly-valid under the current allocation, with B03 role-aligned and quiet delivery flags observed off; this run performed zero scheduler mutations.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured effort: `UNKNOWN_NOT_EXPOSED`. Known/self-reported effort label: `UNKNOWN`. Provider reasoning tokens/time: `null` / not exposed. Elapsed execution is recorded in the matching finish/receipt and is wall-clock work including tool/network time, not pure thinking.

Status: `ESSENTIAL_STEP_APPLIED`.
