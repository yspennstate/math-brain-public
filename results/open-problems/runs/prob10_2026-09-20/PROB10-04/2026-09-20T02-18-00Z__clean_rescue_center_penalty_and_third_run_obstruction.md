Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-reasoning telemetry is exposed, so I do not claim GPT-6 maximum. THIRD CONSECUTIVE SOURCE-METRIC NONMOVEMENT: explicit-decimal bracket `[3.52,4.4898]`, width `W=0.9698 -> 0.9698`.**

# PROB10-04 run 3 — clean rescue centers, an exponential radius-3 penalty, and the precise third-run obstruction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **source OPEN / PROB10-04 PARTIAL**.

## 1. Continuity, ownership, and evidence consumed

This run continued the claimed **cluster-aware weighted-counting / overlap-variational** route in `operations/claims/PROB10-04.md`. It did not take over the neighboring constructive lower-bound worker.

Consumed before new mathematics:

- `operations/PROB10_2026-09-20.md` on current master;
- current root `POSTED.md` exclusion registry;
- scoped claim `operations/claims/PROB10-04.md`;
- own run-1 report `runs/prob10_2026-09-20/PROB10-04/2026-09-19T23-59-30Z__cluster_weight_barrier_component_quotient.md`;
- own run-2 report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T00-58-00Z__global_max_radius3_flip_accessibility.md`;
- immutable HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, preserving the actual F0095/binary-cascade predecessor rather than relabeling it;
- newest neighboring constructive report `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T04-27-22__t04_majority_two_choice_repair.md`, which changed to a majority-start/nonbacktracking two-choice repair mechanism and still reports no source endpoint movement.

The run-2 exact clause identity remains the starting point. For a satisfying assignment `sigma`, write `T_C` and `F_C` for the variables whose literals in a clause `C` are respectively true and false under `sigma`. For a flip set `S`,

`C(sigma^S)=FALSE  <=>  T_C subseteq S and F_C cap S = empty`.    (1.1)

Run 2 also killed the naive statement that two unique-blocked zeroes sharing one rescuing one-variable automatically give a valid improving 3-flip: an `|T_C|=2` clause can spoil the composition. This run does not retry that false lemma. It identifies and removes exactly that obstruction.

## 2. Fresh source status and what is, and is not, a rigorous decimal endpoint

A bounded current source check used:

- Caragiannis--Gravin--Jiang, ESA 2025, `https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103`: this explicitly studies **k-wise-independent clauses**, not the classical iid-clause target here;
- Hajiaghayi--Sorkin, `https://arxiv.org/abs/math/0310193`: explicit classical 3-SAT lower endpoint `3.52`;
- Diaz--Kirousis--Mitsche--Perez-Gimenez, `https://arxiv.org/abs/0807.3600`: explicit classical 3-SAT upper endpoint `4.4898`;
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, CPC 2026, *The random k-SAT Gibbs uniqueness threshold revisited*: it states that interpolation yields a rigorous **variational upper bound** on the threshold sequence matching the 1RSB prediction, while its `d_sat(3)≈12.801` table entry is explicitly described as the physics prediction. Since this run did not independently interval-certify the k=3 variational evaluation, I do **not** silently replace `4.4898` by the rounded physics number `12.801/3≈4.267` in the explicit-decimal fleet metric;
- Carenini, ECCC TR26-145 (2026): `O(n/log n)` scaling window for every fixed `k>=3`, which is a sharp-window statement and does not prove convergence to one limiting density.

Thus the stable explicitly certified decimal bracket used for the fleet metric remains `alpha_L=3.52`, `alpha_U=4.4898`, `W=0.9698`.

This is a metric convention, not a claim that `4.4898` is the strongest variational information known in the literature. A future source-baseline update should certify the interpolation functional numerically before recording a smaller decimal endpoint.

## 3. Attack A — exact global triple-cover capacity: correct, but slack at the balanced saddle

Let `z=|{v:sigma_v=0}|`, `o=n-z`. A globally maximum-Hamming-weight satisfying assignment must have every improving triple `S={x,z',y}` with `x,z' in Z`, `y in O` blocked by at least one clause, since such a flip changes Hamming weight by `+1`.

For a satisfied clause `C`, let `a_C=|T_C cap Z|`, `b_C=|T_C cap O|`, `c_{0,C}=|vars(C) cap Z|`, `c_{1,C}=|vars(C) cap O|`. By (1.1), the exact number of improving triples falsified by this clause is

`A_C = C(z-c_{0,C}, 2-a_C) C(o-c_{1,C}, 1-b_C)`,    (3.1)

with impossible binomials interpreted as zero. Therefore every global maximum satisfies

`C(z,2) o <= sum_C A_C`.    (3.2)

This is exact and uses all clause truth types. But after division by `n^3`, only critical (`|T_C|=1`) clauses survive at leading order. At the balanced density `rho=z/n≈1/2`, the typical critical-clause counts under the `sigma`-satisfying law make (3.2) comfortably slack. Therefore the uniform capacity inequality creates no exponential penalty at the dominant saddle.

This is the first precise obstruction of the run: total cover capacity forgets the sparse rescue collisions where radius 3 actually gains information.

## 4. Attack B — disjoint improving triples give an exact occupancy penalty, but it is far too weak

Choose `L=min(floor(z/2),o)` pairwise variable-disjoint improving triples `S_1,...,S_L`. For each `i`, let `B_i` be the set of proper clauses that are satisfied by `sigma` but falsified by `sigma^{S_i}`.

### 4.1 Exact disjointness

The clause classes `B_i` are pairwise disjoint. If one clause were falsified by both `sigma^{S_i}` and `sigma^{S_j}`, its variable restriction under the two endpoint assignments would equal the unique falsifying bit pattern of that clause. Since `S_i,S_j` are disjoint, this forces the clause to avoid `S_i union S_j`; then its restriction equals `sigma` as well, contradicting that `sigma` satisfies the clause.

### 4.2 Exact one-bin probability

For `|S_i|=3`, an unconditional random proper clause belongs to `B_i` exactly when its variable triple intersects `S_i` and its signs are the unique pattern falsified by `sigma^{S_i}`. Hence

`q_n=(1/8)[1-C(n-3,3)/C(n,3)]`.    (4.1)

Conditioned on `sigma` satisfying that clause,

`r_n=q_n/(7/8)=(1/7)[1-C(n-3,3)/C(n,3)]=(9+O(1/n))/(7n)`.    (4.2)

A global maximum requires every bin `B_i` to contain at least one of the `m` clauses.

### 4.3 Poisson-conditioning upper bound

Condition on all `m` clauses satisfying `sigma`; the bin counts are multinomial with cell probabilities `r_n`. Let independent Poisson variables have means `m r_n` in the `L` bins and mean `m(1-Lr_n)` in the remainder. Conditional on their total being `m`, their joint law is exactly the multinomial law. Therefore

`P(all L bins hit | sigma satisfies) <= (1-exp(-m r_n))^L / P(Pois(m)=m)`.    (4.3)

The denominator is only polynomially small by Stirling. Thus for `rho=z/n` the first-moment exponent is at most

`Phi_alpha(rho)=h(rho)+alpha log(7/8)+min(rho/2,1-rho) log(1-exp(-9 alpha/7))`.    (4.4)

A numerical optimization of this auxiliary bound crosses zero near `alpha≈5.18851948`, only a tiny improvement over the elementary first-moment value `5.190893...` and still much worse than the explicit theorem endpoint `4.4898`.

So disjoint endpoint occupancy is a genuine cluster-aware penalty, but its forced disjointness throws away almost all radius-3 collisions. This is the second precise obstruction.

## 5. Attack C — clean rescue centers repair the run-2 counterexample

For a clause critical at `v` (`T_C={v}`), call it a blocker of `v`, and let `K_v` be the number of blockers.

Fix `y in O`. Distinct `x,z in Z` form a **clean rescue pair at center y** when:

1. `K_y=0`;
2. `K_x=K_z=1`;
3. the unique blocker of `x` contains `y` among its two false-literal variables;
4. the unique blocker of `z` contains `y` among its two false-literal variables;
5. no clause has `|T_C|>=2`, `T_C subseteq {x,z,y}`, and `F_C cap {x,z,y}=empty`.

### Proposition 5.1 — clean rescue pair gives a strictly heavier satisfying assignment

If `sigma` satisfies `F` and `(x,z;y)` is a clean rescue pair, then `tau=sigma^{ {x,z,y} }` satisfies `F` and has Hamming weight `|tau|_1=|sigma|_1+1`.

**Proof.** By (1.1), a clause can fail after the flip only when all of its initially true literals lie in `S={x,z,y}` and none of its initially false literals in `S` becomes true. If `|T_C|=1` and its unique true variable is outside `S`, it remains true. If the unique true variable is `y`, no such clause exists because `K_y=0`. If the unique true variable is `x`, it is the unique blocker of `x`; condition 3 puts `y` in its false-literal set, so flipping `y` makes that literal true. The same applies to `z`. Every possible failure with `|T_C|>=2` is excluded exactly by condition 5. Thus no clause fails. Two zeroes flip to one and one one flips to zero, so weight rises by one. QED.

This pinpoints the run-2 failure: its four-clause counterexample has exactly the missing higher-truth interference represented by condition 5.

## 6. Conditional density of clean centers

Fix a deterministic assignment `sigma` with zero density `rho in (0,1)` and condition on `sigma` satisfying all `m=floor(alpha n)` independent clauses. Under this conditioning the clauses remain independent; each variable triple is uniform and, given the triple, the seven nonempty truth patterns are equiprobable.

For fixed `v`,

`P(C critical at v | C(sigma)=1)=3/(7n)`.    (6.1)

Hence `K_v => Pois(lambda)`, `lambda=3 alpha/7`.

For distinct fixed `v,y`,

`P(C critical at v and y in C | C(sigma)=1)=6/[7n(n-1)]`,    (6.2)

so, given a critical blocker at `v`, the chance it contains specified `y` is exactly `2/(n-1)`.

For a fixed one-variable center `y`, let `L_y` count zero variables `x` with `K_x=1` whose unique blocker contains `y`. Standard factorial-moment evaluation of the multinomial critical-clause categories gives

`L_y => Pois(mu)`, `mu=2 rho lambda exp(-lambda)`,    (6.3)

jointly with `K_y=>Pois(lambda)`. Therefore the expected density of centers satisfying conditions 1--4 and having at least two rescue leaves tends to

`c0(rho,alpha)=(1-rho) exp(-lambda) [1-exp(-mu)(1+mu)]`.    (6.4)

The higher-truth interference in condition 5 changes only `O(1)` expected rescue stars: for a fixed specified `(x,z,y)`, the rescue-star event has probability `Theta(n^-2)`, while the chance of at least one `|T_C|>=2` interference clause is `O(n^-1)`; summing `O(n^3)` triples gives `O(1)`. Hence if `X` denotes the number of clean rescue centers,

`E[X | sigma satisfies]=(c0(rho,alpha)+o(1)) n`.    (6.5)

At `alpha=4.4898`, `rho=0.46`,

`lambda=1.9242`, `mu=0.2584452743743938...`, `c0=0.002220336639556037...`.    (6.6)

Thus the collision scale from run 2 survives after the exact interference correction: it was the composition lemma that was false, not the linear abundance of candidate rescue centers.

## 7. Exponential no-clean-center penalty by bounded differences

The center count `X` has a deterministic bounded-difference constant at most `12` under replacement of one conditioned clause.

Replacing one clause can change the unique-critical degree/blocker data of at most the old and new unique-true variables. A zero variable with `K_v=1` can serve as a rescue leaf only for the at most two variables in the false set of its unique blocker; changing the blocker can therefore affect at most four center identities for that variable. Across old/new critical variables this costs at most eight centers.

For higher-truth interference, a fixed `|T_C|=3` clause can obstruct at most one candidate center. A fixed `|T_C|=2` clause can obstruct at most two center identities: if its two true variables are the two zero leaves, a common center lies in the intersection of two size-two blocker-false sets; if one true variable is the one-center, the center is fixed. Old/new clauses therefore add at most four more affected centers.

McDiarmid's inequality applied to the `m` independent conditioned clauses gives

`P(X=0 | sigma satisfies) <= exp[-2(E X)^2/(144m)]`.    (7.1)

Using (6.5), for all sufficiently large `n`, `E X >= c0 n/2`, hence

`P(X=0 | sigma satisfies) <= exp[- c0(rho,alpha)^2 n/(288 alpha)]`.    (7.2)

Every globally maximum-Hamming-weight satisfying assignment has `X=0` by Proposition 5.1. Thus (7.2) is a rigorous exponential radius-3 penalty for the ordinary satisfying-assignment first moment.

At `alpha=4.4898`, `rho=0.46`, the safe exponent from (7.2) is only `3.8125729995e-9 n`.

This is far too small to beat the already much stronger Diaz configuration count when used as a standalone first moment. Its value is structural: it proves that the exact run-2 rescue collision can be made into an exponential penalty once the higher-truth obstruction is carried explicitly.

## 8. Exact missing lemma for a source-level upper-endpoint improvement

The current upper endpoint `4.4898` comes from a refined positively-prime / unbalanced configuration count that already has nearly zero variational margin. Therefore the next route is **not** another standalone local-max count.

Let `x` denote a feasible Diaz configuration type tuple and let `F_alpha(x)` be its normalized logarithmic first-moment objective. For the refined conditional configuration law at type `x`, define `c_clean(x)` as the limiting density of clean rescue centers using the exact truth-profile condition in Proposition 5.1.

The missing source-relevant lemma is:

**Uniform clean-center lemma near the Diaz maximizers.** There exist `delta>0` and `eta>0` such that for every feasible type tuple `x` with `F_4.4898(x)>=-delta`, the conditioned configuration law satisfies `c_clean(x)>=eta`, and the no-clean-center event costs `exp(-kappa n)` uniformly for some explicit `kappa>0` after paying the configuration-model conditioning error.

If this holds, the old objective is replaced near every maximizer by `F_alpha(x)-kappa`; away from the maximizing neighborhood the old negative margin is retained. Continuity in `alpha` then gives an actual explicit upper endpoint strictly below `4.4898`.

The unpaid difficulty is now finite-dimensional and precise: **prove that the old near-maximizing type tuples cannot send the clean-rescue density to zero through degree/type correlations.** This is materially narrower than run 2's false rescue-star capacity claim.

## 9. Third unchanged run — required obstruction and method change

### Source metric

`[3.52,4.4898] -> [3.52,4.4898]`, so `W: 0.9698 -> 0.9698`.

**No movement, for the third consecutive PROB10-04 run.**

### What did move

- exact all-triple cover inequality (3.2), with a proof of why its leading capacity is slack;
- exact disjoint-triple occupancy penalty (4.3)--(4.4), showing quantitatively why a naive independent endpoint packing is too weak;
- repaired radius-3 mechanism: clean rescue pairs plus the complete `|T_C|>=2` interference condition;
- full proof that every clean rescue pair contradicts global Hamming maximality;
- asymptotic clean-center density (6.4) and an explicit exponential no-center penalty (7.2).

### Precise obstruction

Every **standalone** local-max first-moment penalty found so far is dominated by the 4.4898 refined configuration bound. The source endpoint will not move by filing another local criterion outside that configuration polytope. The missing payment is a uniform positive clean-center density **inside the near-maximizing Diaz type family**, or alternatively a certified numerical evaluation of the rigorous interpolation upper functional.

### Required method change next run

The next PROB10-04 iteration should not derive another radius-`r` standalone first moment. It should do one of exactly these within the same 3-SAT parent:

1. reconstruct the Diaz finite-dimensional type variables/objective and express `c_clean(x)` explicitly, then prove or refute a positive infimum over the near-maximizer set; or
2. reconstruct the Franz--Leone / Panchenko--Talagrand k=3 interpolation functional and interval-certify a concrete rigorous upper decimal, updating the source baseline if that certification is genuinely complete.

This satisfies the three-unchanged-run rule by changing the method while staying on the owner-assigned 3-SAT problem.

## 10. Artifacts

Idea written before checking:

- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T02-05-00Z__clean_rescue_center_idea_before_code.md`

Exact combinatorial checks / numerical diagnostic:

- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T02-08-00Z__clean_rescue_center_exact_checks.md`

No code certificate is substituted for the theorem-sized proof above; the exact rational identities are archived explicitly in the second artifact.

## 11. Status

**OPEN / PARTIAL.** No source threshold endpoint is claimed improved, no limiting `alpha` is claimed to exist, the ESA k-wise-independent model is not conflated with the iid-clause model, and the rounded physics value is not recorded as a certified theorem decimal.