# POS3 fleet03/B10 — first-interruption renewal has a macroscopic branch and exact bounded odds distortion across depth

**Run:** `20260922T092055Z-fleet03-B10-POS3-elliptic`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

Every probability below is either under the original uniform law on `L(P)` or under a channel law explicitly identified as uniform on its exact residual poset. No deletion-induced or projected distribution is renamed uniform.

## 1. Exact assignment and peer state consumed

The active fleet03/B10 assignment is to apply the bounded-width/high-variance results to the exact width-three target and make the remaining exceptional-case requirement explicit. The assigned OTHER-account partner is fleet04/B11.

I consumed fleet04/B11 r19,

`proofnet24/collective-POS3/fleet04/B11/20260922T084137Z-B11-POS3-r19/REPORT.md`, blob `7d3327d016a644c5792c8ba6af5d3ade1779e122`.

In a cardinality-minimal hypothetical no-balanced width-three counterexample it writes the first maximal strong-majority chain block as

`C={c_1<...<c_m}`, `Q=P\C`,

with at most two first interrupters

`M={q in Min(Q): lambda(q)<m}`,

and the exact full-extension renewal

`e(P)=e(Q)+sum_(q in M) sum_(j=lambda(q))^(m-1) e(R_(q,j))`,       (1.1)

where

`R_(q,j)=P\{c_1,...,c_j,q}`.                                      (1.2)

For a Q-order event `A`,

`Pr_P(A)=alpha Pr_Q(A)+sum_(q,j) beta_(q,j) Pr_(q,j)(A)`,          (1.3)

with

`alpha=e(Q)/e(P)`, `beta_(q,j)=e(R_(q,j))/e(P)`.                   (1.4)

The partner also proves

`m<=K`, where `K=pi(P)=max_v |Inc(v)|`,                              (1.5)

and for adjacent depths in a fixed branch,

`N_(j+1)(q) <= N_j(q) <= K N_(j+1)(q)`,                           (1.6)

where `N_j(q)=e(R_(q,j))`. Its first unpaid implication is `POS3-ELLIPTIC-BACKTRACK-RENEWAL-MIGRATION-v1`: the balancing pair may migrate between renewal components, so one cannot simply lift a fixed residual balanced pair.

I also use the already-proved fleet03/B10 actual-full-law first-block window

`4/9 < alpha < 7/9`.                                               (1.7)

In particular,

`2/9 < 1-alpha < 5/9`.                                             (1.8)

This is the exact full-law block mass, not an induced-law uniformity claim.

Finally, the compatible fleet04/B10 lead state says opposite-ray switching reduces to span descent, strict envelope expansion, or an exact heavy Hasse backtrack; fleet02/B10's newest exact-backtrack theorem shows the low-endpoint backtrack emits two disjoint external packets. Those facts motivate attacking the renewal-migration part rather than reopening the local Hasse-channel derivation.

## 2. A macroscopic first-interrupter branch is unavoidable

For `q in M` put

`beta_q=sum_(j=lambda(q))^(m-1) beta_(q,j)`.                       (2.1)

From the exact renewal,

`sum_(q in M) beta_q = 1-alpha > 2/9`.                            (2.2)

The partner proves `|M|<=2`, so there exists `q_* in M` with

`beta_(q_*) > 1/9`.                                               (2.3)

There is also a useful upper bound on every individual branch. Since `q in M`, one has `q||c_m`. The first block precedes `q` in the strong-majority total order, so in a no-balanced candidate

`Pr_P(q<c_m)<1/3`.                                                (2.4)

Every extension in the entire `q`-branch has `q` in its fixed prefix before `c_m`. Hence

`beta_q <= Pr_P(q<c_m)<1/3`.                                     (2.5)

Thus every branch is subcritical but one branch is uniformly macroscopic:

`1/9 < beta_(q_*) < 1/3`.                                        (2.6)

If `|M|=1`, this sharpens further to

`2/9 < beta_q < 1/3`, and consequently `2/3 < alpha < 7/9`.       (2.7)

This replaces the partner's earlier factorial-scale route to finding a positive branch by a direct actual-law mass bound.

## 3. Non-factorial coefficient floor across the heavy branch

Let

`ell=m-lambda(q_*)`,                                              (3.1)

so `1<=ell<=m<=K`, and abbreviate `b_j=beta_(q_*,j)`.

By (1.6), as depth increases the coefficients satisfy

`b_(j+1)<=b_j<=K b_(j+1)`.                                       (3.2)

Let `b_min` be the last/deepest coefficient. Iterating (3.2),

`beta_(q_*) <= b_min (1+K+...+K^(ell-1))`
`            = b_min (K^ell-1)/(K-1)`.                           (3.3)

Using (2.3), every component in the selected branch therefore satisfies

`beta_(q_*,j) > (K-1)/(9(K^ell-1))`
`              >= delta_K := (K-1)/(9(K^K-1)).`                  (3.4)

The significance is not that `delta_K` is numerically large; it is that no factorial boundary-atom term is needed. The heavy branch already carries `>1/9` of the original full-extension law, and adjacent-depth surgery spreads a definite portion of that mass across every one of its at most `K` depths.

### Rank-ladder consequence

In the exact depth-`j` component the fixed prefix is

`c_1,...,c_j,q_*`,                                               (3.5)

so `rank_P(q_*)=j+1` on that component. Hence `q_*` has at least `ell` consecutive rank atoms, each of mass `>delta_K`. Therefore

`Var_P(rank(q_*)) > delta_K * ell(ell^2-1)/12`.                  (3.6)

Combining with the inherited actual-uniform all-element bound `Var(rank(x))<6560` gives the necessary condition

`delta_K ell(ell^2-1) < 78720`.                                  (3.7)

This is a direct bridge between the first-interruption geometry and the bounded-width/high-variance input. It is not by itself a contradiction and does not imply a finite-poset kernel.

## 4. Exact adjacent-depth size-bias identity

The more important new point is measure-level, not scalar.

Fix `q in M` and adjacent allowed depths `j,j+1`. Let `Omega_j(q)` be the full extensions in the exact depth-`j` renewal component and let `Omega_(j+1)(q)` be the next component. Put

`c=c_(j+1)`.

A member of `Omega_j(q)` starts

`c_1,...,c_j,q,...`,                                             (4.1)

whereas a member of `Omega_(j+1)(q)` starts

`c_1,...,c_j,c,q,...`.                                           (4.2)

In (4.1), after deleting `c_1,...,c_j`, the element `c` is minimal. Therefore every residual element occurring between `q` and `c` is incomparable with `c`. Moving `c` left across those elements and across `q` gives a valid member of `Omega_(j+1)(q)`.

Conversely, for `omega in Omega_(j+1)(q)`, let `t(omega)` be the length of the maximal initial run immediately after `q` consisting of elements incomparable with `c`. Moving `c` right across `q` and then across any initial segment of those `t(omega)` elements gives all and only the preimages in `Omega_j(q)`. Thus the exact fiber size is

`W_j(omega)=t(omega)+1`.                                         (4.3)

The elements `q` plus those `t(omega)` elements are all incomparable with `c`, so

`1 <= W_j(omega) <= |Inc(c)| <= K`.                              (4.4)

Moving only the chain element `c` leaves the relative order of **all elements of Q** unchanged.

Let `mu_j` and `mu_(j+1)` denote the distributions of the Q-order trace induced respectively by the uniform laws on `Omega_j(q)` and `Omega_(j+1)(q)`. For every event `A` depending only on that Q-order trace,

`mu_j(A)`
` = E_(Omega_(j+1))[ W_j 1_A ] / E_(Omega_(j+1))[W_j].`          (4.5)

This is an exact identity between two genuine uniform channel laws. It does not claim either projected Q-order law is itself uniform on `L(Q)`.

Equivalently, if `bar W_j` is the conditional expectation of `W_j` given the Q-order trace, then

`d mu_j / d mu_(j+1) = bar W_j / E W_j`,                         (4.6)

and `1<=bar W_j<=K` pointwise on the common support.

Equation (4.5) upgrades the partner's total-count comparison (1.6): indeed

`E W_j = N_j(q)/N_(j+1)(q) in [1,K]`,                            (4.7)

but now the reweighting of every Q-order event is explicit.

## 5. Exact odds-distortion bound

Assume `0<mu_(j+1)(A)<1`. From (4.5),

`odds(mu_j(A))/odds(mu_(j+1)(A))`
` = E[W_j | A] / E[W_j | A^c]`.                                 (5.1)

By (4.4),

`1/K <= odds(mu_j(A))/odds(mu_(j+1)(A)) <= K`.                  (5.2)

Thus changing the interruption depth by one changes the log-odds of **any Q-order event** by at most `log K`. Iterating over `d` depths gives

`K^(-d) <= odds(mu_j(A))/odds(mu_h(A)) <= K^d`.                 (5.3)

This is the first direct actual-channel control on the partner's pair-migration obstruction. Adjacent renewal components are not arbitrary unrelated residual laws: on the entire sigma-field generated by Q relative orders, they are related by a bounded insertion size-bias.

### Corollary 5.1 — a Q-pair balanced in one depth cannot disappear in another

Suppose an incomparable pair `a,b` belonging to `Q` has, in one exact component of the selected `q_*` branch,

`1/3 <= mu_h(a<b) <= 2/3`.                                      (5.4)

For any other component in the same branch, at depth distance at most `ell-1`, (5.3) implies

`min{mu_j(a<b),mu_j(b<a)}`
` >= 1/(1+2K^(ell-1))`
` >= 1/(1+2K^(K-1)).`                                           (5.5)

Since the entire selected branch has mass `beta_(q_*)>1/9` under the original uniform law on `L(P)`, both orientations of this same pair receive from that branch alone more than

`1/[9(1+2K^(K-1))]`                                             (5.6)

of the original full-extension probability.

This does **not** prove the pair is balanced in `P`; the other top-level components can still generate a Simpson-type displacement. What (5.6) rules out is arbitrary singular loss of one orientation merely by moving the interruption depth within the heavy branch.

## 6. Refined first missing implication

The partner r19 residual allowed the balancing pair to migrate across residual components. The new identity separates that problem into two qualitatively different mechanisms.

Inside the selected heavy first-interrupter branch, depth migration of every Q-order event is now controlled by the exact bounded weight (4.3): per depth its odds can change by at most a factor `K`, and the whole branch has original-law mass `>1/9`. Therefore an unresolved evasion cannot be attributed to an unconstrained or vanishing-depth law inside this branch.

What remains is the sharper statement:

> **`POS3-TOPLEVEL-OR-CHAINTAIL-BACKTRACK-MIGRATION-v1`.** In a cardinality-minimal no-balanced width-three poset with `pi(P)=K`, take the heavy first-interrupter branch `q_*` above. Combine the lead's non-exact/multi-distinguisher exact-backtrack state with the renewal. Prove that either an authorized span descent / proper ordinal-or-autonomous reduction occurs, or a balanced pair is forced. After (4.5)-(5.3), any surviving migration must use at least one of two mechanisms: (i) a top-level Simpson displacement between the prefix component, the other first-interrupter branch (if present), and the heavy `q_*` branch; or (ii) balancing pairs whose identity essentially uses a surviving chain-tail element, so that they are not events on the common Q-order sigma-field preserved by the depth surgery.

This is strictly narrower than treating every depth component as an unrelated residual distribution. The next useful proof step is to couple the lead's two disjoint external backtrack packets to these two remaining escape mechanisms, rather than improve `delta_K` or the variance constant in isolation.

A useful minimality dichotomy is immediate: whenever an exact residual `R_(q_*,j)` is a nonchain, cardinality minimality gives it a balanced pair. If one such balanced pair lies wholly in the common Q part, Section 5 controls that fixed pair through every depth. If not, the obstruction at that depth is necessarily chain-tail-bearing. This is exactly the second mechanism above, not an unproved fixed-pair lift.

## 7. Status and integrity

- fleet04/B11 r19 exact renewal, `m<=K`, and adjacent count surgery: **CONSUMED/APPLIED**;
- prior fleet03/B10 exact full-law block window `4/9<alpha<7/9`: **CONSUMED/APPLIED**;
- macroscopic branch `1/9<beta_(q_*)<1/3`: **PROVED**;
- non-factorial per-depth coefficient floor (3.4): **PROVED**;
- consecutive rank-ladder variance lower bound (3.6): **PROVED**;
- exact adjacent-depth Q-order size-bias identity (4.5): **PROVED**;
- per-depth event-odds distortion at most factor `K`: **PROVED**;
- same-Q-pair persistence bound (5.5)-(5.6): **PROVED**;
- top-level / chain-tail migration exit: **OPEN / FIRST ESSENTIAL REMAINING IMPLICATION**;
- parent POS3: **OPEN / NOT PROVED**.

No finite census, surrogate-uniform law, benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex execution, remote/public workflow, permission change, or cross-account native action was used. No genuine authenticated brain retrieval/context use occurred, so this run remains `WITHOUT_VERIFIED_BRAIN_RESEARCH`.
