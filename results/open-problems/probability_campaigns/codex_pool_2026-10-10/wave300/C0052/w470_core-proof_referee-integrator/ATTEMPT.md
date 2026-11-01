# C0052 referee and conditional reduction

## Exact target

The primary source defines the three-dimensional target by its subcritical renormalized coupling

`g(beta) = [sum_{x,y,z in Z^3} U4(0,x,y,z)] / [chi(beta)^2 xi(beta)^3]`,

where `U4(a,b,c,d) = <sigma_a sigma_b sigma_c sigma_d> - G(a,b)G(c,d) - G(a,c)G(b,d) - G(a,d)G(b,c)`, `chi=sum_x G(0,x)`, and `xi` is the inverse exponential decay rate along a coordinate axis. The task is to show `g(beta)` does not tend to zero as `beta` increases to `beta_c`. Lebowitz's inequality makes `g<=0`. This is the operational formulation in Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, (7.1), Conjecture 6, Exercise 34. Current openness: UNKNOWN after a bounded check; no novelty claim.

## Conditional weighted-intersection criterion

Fix `0<beta<beta_c`. Let `G(x)=<sigma_0 sigma_x>`, `chi=sum_x G(x)`, `xi=xi(beta)`, and let `B={y in Z^3: ||y||_infinity <= floor(xi)}`. Draw `X` independently of `(Y,W)` with law `G(x)/chi`; draw `Y` uniformly in `B`, independently of `W`; draw `W` with law `G(w)/chi`; set `Z=Y+W`. Equivalently the full joint mass is `P(X=x,Y=y,Z=z)=G(x)G(z-y)/(|B|chi^2)` for `y in B`. For each triple `(x,y,z)`, sample independent random currents with source pairs `(0,x)` and `(y,z)` and let `p_beta(x,y,z)` be the probability that all four marked vertices are connected in their union. Assume the thermodynamic current limits exist and the source's Exercise 61(1) identity passes to them. Write `q_beta = E[p_beta(X,Y,Z)]`.

**Proved reduction, conditional on the quoted current identity:** `-g(beta) >= 2 |B| q_beta / xi^3`. Therefore if `xi(beta)->infinity` and `liminf_{beta up beta_c} q_beta>0`, then `liminf_{beta up beta_c} -g(beta)>0`. This is sufficient for C0052 in the source's operational sense. It does not construct a field limit.

**Derivation:** Exercise 61(1) states `-U4(0,x,y,z)=2G(x)G(z-y)p_beta(x,y,z)`. Sum this nonnegative identity over `x,z in Z^3` and `y in B`; the sum is `2 |B| chi^2 q_beta`. The unrestricted numerator of `-g` includes this partial sum, proving the inequality. Since `|B|/xi^3=(2 floor(xi)+1)^3/xi^3 -> 8` when `xi->infinity`, the last assertion follows. No factorization of current events is used.

**Referee correction:** w473 independently checked the algebra and issued FIX because the first draft gave the marginals without explicitly requiring `X` independent of `(Y,Z)`. The joint mass above is the corrected assumption. The infinite-volume current identity and `liminf q_beta>0` remain unproved inputs in this packet.

## Hardest missing lemma and attempted route

The missing input is `liminf q_beta>0`, an averaged intersection estimate for independent source-pair random currents sampled by the two-point function across a correlation-length box. The `x` and `z-y` endpoint laws are specified above; the claim is not a pointwise estimate for arbitrary four points. A route is to count intersections of current clusters inside a mesoscopic cube and use `P(N>0) >= E[N]^2/E[N^2]`. The historical C0052-A001 packet gives neither a lower bound for `E[N]` under the stated endpoint law nor a scale-uniform bound for `E[N^2]`; its guessed cluster fractal dimension is not an assumption or a theorem. Six-point or higher current correlations and source-conditioned geometry are the load-bearing gap. I cannot close it from the available inequalities.

I tested the tempting first-moment shortcut after peer review: replace the original sourced-current hit probability by the sourced-plus-sourceless hitting formula, even after averaging the endpoint by `G/chi`. `ENDPOINT_TREE_OBSTRUCTION.md` gives an exact degree-three tree sequence with `k(v)/G(o,v)->0`, so no graph-uniform linear reversal follows from endpoint averaging alone. This makes a genuine Z^3-specific occupation estimate, rather than generic current algebra, necessary for the proposed second-moment route. The finite-tree obstruction does not refute such a Z^3 estimate.

**Sanity check:** Restricting the source identity to `y=0` gives `-sum_{x,z} U4(0,x,0,z)=2 chi^2`, since the two source-pair current clusters share the marked vertex 0. Hence `-g(beta)>=2/xi^3`. This exact bound decays when `xi->infinity` and so cannot prove C0052.

## Referee boundary

KEEP the finite or infinite-volume identity as a source-backed input and the algebraic conditional reduction after independent review. FIX the historical use of an unqualified equivalence between nontriviality and a scale-wide intersection probability; the source defines a normalized weighted sum. DROP any claim that the unproved averaged intersection estimate, an exponent heuristic, or a source/hash receipt solves the parent problem. Peer artifacts from w468 and w469 are pending substantive content at this checkpoint.

NEXT: Check peers' completed arguments line by line; submit this conditional reduction to w473 for independent review; prepare a draft concept bundle that labels the current-intersection input as unproved.
