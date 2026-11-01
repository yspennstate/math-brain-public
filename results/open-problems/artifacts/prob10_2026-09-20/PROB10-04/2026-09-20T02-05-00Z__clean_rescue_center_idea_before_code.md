# PROB10-04 idea before code — rescue stars become valid after isolating the only higher-truth obstruction

Model is the exact iid proper random 3-SAT model from the owner directive.  This note deliberately precedes any checker.

## New mechanism

Fix a satisfying assignment `sigma`, write `Z={v:sigma_v=0}` and `O={v:sigma_v=1}`, and for every clause `C` let `T_C` be its variables whose literals are true under `sigma`, `F_C` the false-literal variables.  The exact identity from the preceding run is

`C(sigma^S)=FALSE  <=>  T_C subseteq S and F_C cap S = empty`.

Call a clause **critical at v** when `T_C={v}` and let `K_v` be the number of critical clauses at `v`.

For `y in O`, call distinct `x,z in Z` a **clean rescue pair at y** if

1. `K_y=0`;
2. `K_x=K_z=1`;
3. the unique critical clause at `x` contains `y` among its two false-literal variables;
4. the unique critical clause at `z` contains `y` among its two false-literal variables;
5. there is no clause `C` with `|T_C|>=2`, `T_C subseteq {x,z,y}`, and `F_C cap {x,z,y}=empty`.

Then flipping `S={x,z,y}` changes two zeroes to ones and one one to zero, so Hamming weight rises by one.  Conditions 1--4 repair every critical (`|T_C|=1`) clause whose unique true literal lies in `S`; condition 5 removes exactly the remaining `|T_C|=2,3` obstructions.  Therefore every clean rescue pair produces a satisfying assignment of larger Hamming weight.  A globally maximum-Hamming-weight satisfying assignment can have **no** clean rescue center.

This repairs the false shortcut killed in run 2: the old four-clause counterexample contains precisely an `|T_C|=2` interference clause, which condition 5 now records instead of ignoring.

## Conditional random-formula calculation

Condition on a fixed `sigma` satisfying all `m=floor(alpha n)` clauses.  The clauses remain independent; each variable triple is uniform and each of the seven sign/truth patterns satisfying `sigma` is uniform.

For fixed `v`,

`P(C critical at v | C(sigma)=TRUE)=3/(7n)`

exactly, hence `K_v => Pois(lambda)` with

`lambda=3 alpha/7`.

Given a critical clause at `x`, its two other variables are a uniform two-subset of `[n]\{x}`, so for fixed `y != x`,

`P(y belongs to the unique blocker | K_x=1)=2/(n-1)`.

For a fixed one-variable center `y`, the number of zero variables `x` with `K_x=1` whose unique blocker contains `y` therefore converges to `Pois(mu)` with

`mu=2 rho lambda exp(-lambda)`,

where `rho=|Z|/n`.  Also `P(K_y=0)->exp(-lambda)`.  Consequently the expected density of rescue-star centers before the higher-truth interference test is

`c0(rho,alpha)=(1-rho) exp(-lambda) [1-exp(-mu)(1+mu)]`.

For any fixed prospective star `(x,z,y)`, an `|T_C|>=2` interference clause has probability `O(1/n)` over `m=Theta(n)` clauses, while the rescue-star event itself has probability `Theta(1/n^2)`.  Summing over `Theta(n^3)` triples gives only `O(1)` expected rescue stars spoiled by such interference.  Thus the number `X` of clean rescue centers satisfies

`E[X | sigma satisfies]=(c0(rho,alpha)+o(1)) n`.

At `alpha=4.4898`, `rho=0.46`, this gives `lambda=1.9242...`, `mu=0.259...`, and `c0=0.0022203366...`; this reproduces the previous heuristic collision density, but now with the exact missing obstruction isolated.

## Concentration route

Replacing one conditioned clause can change clean-center status only through:

- the old/new unique critical variable and at most the two false-variable centers of its blocker; or
- an old/new `|T_C|>=2` interference relation.

A fixed `|T_C|=2` clause can interfere with at most two center statuses: if its two true variables are the two zero leaves, a common center must lie in the intersection of the two size-two blocker-false sets; if one true variable is the one-center, that center is fixed.  A `|T_C|=3` clause determines at most one candidate center.  A safe deterministic bounded-difference constant is therefore `12` for replacing one clause.

McDiarmid then gives, for fixed `rho in (0,1)` and large `n`,

`P(X=0 | sigma satisfies) <= exp[- c0(rho,alpha)^2 n/(288 alpha)]`.

This is an exponential radius-3 penalty for ordinary satisfying assignments.  By itself it only shaves an extremely small amount from the elementary first-moment upper bound, so it does **not** beat the established 4.4898 explicit theorem endpoint.  Its intended source-compatible use is different: port the same clean-center statistic into the Diaz et al. positively-prime configuration polytope, where the old objective is already near zero at 4.4898.  The exact missing lemma is a uniform positive lower bound on the clean-center density over every maximizing/near-maximizing Diaz type tuple, together with the same bounded-difference penalty after conditioning on that type.

## Three materially different attacks in this run

1. **Uniform triple-cover capacity.** Derived the exact necessary cover inequality for all weight-improving triples.  It is slack at the balanced saddle (`rho≈1/2`), so it gives no exponential penalty there.
2. **Disjoint improving triples / occupancy.** For pairwise-disjoint triples, the clause sets falsifying the corresponding endpoints are disjoint, yielding an exact coupon-occupancy penalty.  Optimizing this only improves the elementary first-moment endpoint to about `5.18852`, far weaker than `4.4898`.
3. **Clean rescue centers.** Repair the run-2 counterexample by isolating `|T_C|>=2` interference.  This gives the linear-density clean-center statistic above and an exponential no-center penalty via bounded differences.  This is the route to carry into the Diaz configuration count.

No source threshold endpoint is claimed improved here.