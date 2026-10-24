# PROB10-04 idea before code — priority-weighted rescue representatives

Model stays the classical iid proper random 3-SAT model.  This is a continuation of the scoped Diaz-style cluster-aware weighted-counting route, not the neighboring interpolation or constructive route.

## Exact obstruction after the previous run

The previous secondary potential

`W_K = # { true light variables of class (k,1) with k>K }`

forbids only one-rescue swaps from `t_{i,1}` with `i<=K` to `f_{k,1,1}` with `k>K`.  Its rounded-source-saddle correction was

`J_5 = 1.869587880794033e-7`,

but an endpoint still requires a global reoptimization of the Diaz `M=23` variational problem.  Repeating a cutoff search does not change that obstruction.

## Three materially different attacks for this run

### Attack A — one global degree potential instead of a cutoff

Among Hamming-maximizing satisfying assignments maximize

`W_deg = sum_{v true, class(v)=(i,1)} i`.

A completed one-rescue swap from a true center of class `t_{i,1}` to its false blocker leaf of class `f_{k,1,1}` preserves Hamming weight and raises `W_deg` whenever `k>i`.  Hence all such swaps are forbidden simultaneously.  This should replace the single cutoff leaf mass `E_{>K}` by the center-dependent tail `E_{>i}`.

Candidate finite penalty:

`P(no degree-improving completed swaps) <= prod_i (1-a_i b_1 e_i)^{C_{i,1}}`,

where

`a_i=(Q_safe)_i/(P)_i`, `b_1=B_can/U`, `e_i=E_{>i}/L1`.

At a fixed interior type this gives

`J_deg = -sum_i t_{i,1} log(1-q^i d_i)`,

`d_i=(B_can/U)(E_{>i}/L1)`.

This pointwise dominates every cutoff correction `J_K` because for `i<=K`, `E_{>i}>=E_{>K}`, and it has additional nonnegative terms.

### Attack B — iid random priorities on variables

Attach independent continuous priorities `U_v` to light variables, independently of the formula/configuration.  Among Hamming-maximizing satisfying assignments choose one maximizing `sum_v U_v 1{v true}`.

For a completed one-rescue pair `(center y, leaf x)`, the swap is satisfying and Hamming-neutral.  Therefore a priority-maximal representative requires `U_x<=U_y`.  Completed `j=1` rescue pairs are vertex-disjoint: each center has one canonical blocker and every eligible false leaf `f_{k,1,1}` has exactly one `ns1` copy, hence can belong to only one such pair.  Conditional on the formula/configuration, the comparison events for the completed pairs are independent and each has probability `1/2`.

Thus after averaging over priorities the local survival factor for one completed pair is `1/2`, not `0`; this permits the entire leaf pool

`E_all=sum_k f_{k,1,1}`

instead of a degree tail.  Candidate asymptotic correction:

`J_iid = -sum_i t_{i,1} log(1 - (1/2) q^i d_all)`,

`d_all=(B_can/U)(E_all/L1)`.

### Attack C — degree-separated priorities plus iid jitter

Use priorities with disjoint class intervals, e.g.

`U_v = class_index(v) + xi_v/3`, `xi_v iid Uniform(0,1)`.

Then a one-rescue swap from class `i` to leaf class `k` is automatically improving when `k>i`, improving with probability `1/2` when `k=i`, and never improving when `k<i`.  Since completed rescue pairs are disjoint, the same conditional independence gives the effective marked leaf mass

`E_eff(i)=E_{>i} + (1/2) f_{i,1,1}`.

The predicted correction is

`J_rank = -sum_i t_{i,1} log(1-q^i (B_can/U) E_eff(i)/L1)`.

This strictly strengthens Attack A whenever `f_{i,1,1}>0`, and can exceed the iid-priority correction by exploiting degree ordering.

## Exact theorem to prove before any endpoint claim

For one fixed integer Diaz coarse type, prove the following finite statement.  Let the `ps`, `nu`, and `ns1` copy matchings be independent uniform bijections, let `C_i` be the number of `t_{i,1}` centers, and use the same safe-anchor and canonical-blocker pools as the previous run.  With class-separated continuous priorities as in Attack C,

`E_{matching,priority}[ indicator{the selected representative survives all completed one-rescue improvements} ]`

is at most

`prod_i (1 - a_i b_1 [E_{>i}+(1/2)E_i]/L1)^{C_i}`.

The proof must justify: (1) completed pairs are a matching on variables; (2) priority comparisons factor conditional on the matchings; (3) the remaining heterogeneous leaf-hit events can be averaged with sampling-without-replacement negative association despite the center-dependent nested degree tails; (4) the same conditional averaging over `ps` and `nu` matchings gives the displayed product.

No endpoint moves unless the refined global Diaz objective is certified below one at some density `<4.4898`.  Rounded-saddle evaluation is mechanism evidence only.