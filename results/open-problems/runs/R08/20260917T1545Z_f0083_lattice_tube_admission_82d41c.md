Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **I0082 remains RETIRED/FROZEN at `2/3` with retirement count `6`; successor F0083 is now ADMITTED for R08 with explicit-candidate metric `1/2`. New movement: an exact lattice-subset radius cap, an exact critical-corner transfer asymptotic in `d=4`, and a concrete nonperiodic expanding-tube candidate whose local interaction graph contains a finite-energy two-ended channel. Methods actually used: B13 FIND WHAT ONLY INCREASES, B14 FIND THE GROUP ACTING, B29 ADD THE POINTS AT INFINITY.** GPT-6 / maximum was requested in prompt text, but the exposed runtime has no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083 admitted via a critical lattice with an expanding transient defect tube

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The later six-unchanged R08 handoff controls operationally despite the stale historical `ADMITTED_ACTIVE` wording in `operations/claims/I0082.md`: the frozen I0082 metric remains `2/3`, retirement count `6`, and the C005/C006 classification remains only `PARTIAL / audit pending`. The old R08 FPP strict-convexity route remains retired from this slot.

Before new work I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling new-methods owner directive, the historical I0082 claim, the newest R08 report `runs/R08/20260917T1447Z_f0083_parcel_thickening_6f2a9d.md`, the F0083 intake / F0083-A001 history, and the newest neighboring R09 state. R09 is separately owned on G0013 and has no ownership overlap with F0083.

The previous R08 run proved two facts which I preserve rather than rederive: (i) every one-dimensional stable Lebesgue allocation is unique a.e., so any F0083 counterexample needs `d>=2`; and (ii) in an all-sated disagreement component, incoming and outgoing transferred Lebesgue volume are exactly equal at every center, so the source's one-in/one-out atomic harmonic chain cannot simply be thickened. The unresolved geometric obstruction was global shielding: how to give each center appetite one while allowing shrinking, branching disagreement parcels without creating closer unclaimed holes.

This run removes that particular obstruction by putting the construction inside a critical cubic lattice and deleting a carefully shaped deterministic tube. The intact lattice supplies the appetite-one background automatically.

## 2. Source, current literature, and ownership refresh

Primary source: Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668.

The source's Open problem (i) asks literally whether there exists a discrete set of centers in Euclidean space with two stable allocations differing on a Lebesgue-nonnull set. Immediately before the problem, the paper proves:

- existence for every discrete center set;
- uniqueness when every bounded-distance graph `G_b` is recurrent;
- almost-sure uniqueness for translation-invariant finite-intensity point processes;
- and an atomic, non-Lebesgue one-dimensional example with two stable allocations.

The source states that a Lebesgue counterexample would have to escape the recurrent/stationary uniqueness mechanisms and have greater-than-quadratic growth.

Fresh bounded searches dated 2026-09-17 used the exact title/authors and phrases `two stable allocations`, `discrete set of centers`, `Lebesgue`, `nonuniqueness`, together with later stable-allocation / random-appetite / stable-transport literature. They recovered the original paper, Hoffman--Holroyd--Peres' 2009 *Tail Bounds for the Stable Marriage of Poisson and Lebesgue*, and later Poisson/random-appetite work, but no later primary paper claiming to resolve exact Open problem (i). This remains bounded negative-search evidence only: worldwide open status and publication novelty are **UNVERIFIED**.

A repository-wide exact-ID search again recovered F0083 only in intake/catalog material, the old F0083-A001 attempt, and recent R08 reserve reports. No pre-existing canonical `operations/claims/F0083.md` and no competing current owner were found. The explicit candidate below is now concrete enough to freeze a source-sized metric, so this run admits F0083 to R08 and creates the canonical claim in the same Git commit as this report.

## 3. B13 — deletion monotonicity gives a universal lattice-subset radius cap

This is the key structural lemma. It replaces the earlier attempt to manufacture private reservoirs center by center.

### Theorem 1 — every stable territory for a lattice subset is local

Let `d>=1`, let `Xi subset Z^d` be arbitrary, and let the appetite be `alpha=1`. For **every** stable allocation `psi` to `Xi` and every center `xi in Xi`,

`L(psi^{-1}(xi)) = 1`

and

`ess sup{|x-xi| : psi(x)=xi} <= R_d := sqrt(d)/2`.            (3.1)

In particular every center is sated and all of its territory lies, up to a null set, in `B(xi,R_d)`.

### Proof

Start with the full lattice `Lambda=Z^d`. Randomly translating `Lambda` by a uniform point of `[0,1)^d` produces a translation-invariant finite-intensity point process. Hoffman--Holroyd--Peres Theorem 3 therefore gives an a.e. unique stable allocation for almost every translate. The ordinary unit Voronoi cubes are stable, hence for the unshifted lattice the site-optimal allocation is, a.e.,

`Q_xi = xi + [-1/2,1/2)^d`.

The cube has volume one and is contained in the closed ball of radius

`R_d=sqrt(d)/2`,

so for the full-lattice site-optimal allocation `phi`,

`gamma_xi(phi,R_d)=1`.                                        (3.2)

Now regard `Xi` as a subset of `Lambda`. Let `psi^s` be the site-optimal Gale--Shapley allocation for `Xi`. Proposition 21(ii) of the source says that deleting competing centers makes each surviving center weakly happier in the radial cumulative order. Hence, for every `xi in Xi`,

`gamma_xi(psi^s,R_d) >= gamma_xi(phi,R_d)=1`.                 (3.3)

No center may receive more than its appetite one, so equality holds in (3.3). Thus every center is already sated inside `B(xi,R_d)` under the site-optimal allocation.

Finally let `psi` be **any** stable allocation to `Xi`. Source Lemma 15(ii) says the site-optimal allocation is the worst stable allocation from the point of view of each center:

`gamma_xi(psi,r) >= gamma_xi(psi^s,r)` for every `r`.         (3.4)

Putting `r=R_d` into (3.4) and using (3.3) gives `gamma_xi(psi,R_d)>=1`, hence again equality. Therefore `psi` gives `xi` its full appetite inside the radius-`R_d` ball, proving (3.1). QED.

### Consequence 1 — exact finite-range reduction

The earlier R08 active-ball lemma now becomes especially useful. For an all-sated stable allocation with finite territory radii `rho_xi`, the territory of `xi`, modulo null sets, is

`C_xi(rho) = {x : |x-xi|<rho_xi and |x-xi|<|x-eta| for every eta!=xi with |x-eta|<rho_eta}`.    (3.5)

Theorem 1 gives `rho_xi<=R_d`. Hence a competitor `eta` can affect `C_xi` only if

`|eta-xi| < 2 R_d = sqrt(d)`.                                (3.6)

So for lattice-subset candidates the source problem is an **exact local infinite system**, not a global shielding problem. In `d=4`, `R_4=1`, and only lattice centers at Euclidean distance strictly less than `2` can exchange positive-volume active-cell pieces. This is a finite neighborhood.

The earlier parcel construction failed because a remote disputed parcel forced a center to covet all the unfilled space before it. In a lattice-subset candidate, Theorem 1 eliminates that failure mode: every center's entire appetite lives at one fixed lattice scale.

This is the B13 outcome: deleting centers can only increase each surviving center's radial cumulative territory relative to the critical lattice, and that monotonicity supplies a global invariant bound `rho<=sqrt(d)/2` for **every** stable allocation, not only a selected algorithmic one.

## 4. B14 — cubic symmetry reveals the first nonzero transfer law

A second obstacle in the earlier radius-Jacobian route was that, away from radius ties, the Jacobian is triangular and regular finite truncations cannot bifurcate. The critical cubic lattice sits exactly on a massive radius tie. Its response is not linear: the first nonzero transfer comes from small simplices at Voronoi corners.

I compute that response exactly in the dimension used by the new candidate.

### Lemma 2 — critical corner transfer in `d=4`

Work with the full lattice `Z^4`, appetite one, and the critical radius

`R_4=1`.

Keep every center except the origin at radius `1`, but reduce the origin's active radius to

`1-epsilon`,  `epsilon>0` small.

Then the volume lost by the origin from its old unit Voronoi cube satisfies

`Delta V_0 = (32/3) epsilon^4 + O(epsilon^5).`                (4.1)

To leading order the lost volume is split equally among the eight face-neighbor centers `+/- e_i`; each fixed face neighbor receives

`(4/3) epsilon^4 + O(epsilon^5).`                            (4.2)

### Proof

Consider one old Voronoi corner, say

`c=(1/2,1/2,1/2,1/2)`.

Write a nearby point inside the origin's cube as

`x_i=1/2-y_i`, `y_i>=0`,

and put

`S=y_1+y_2+y_3+y_4`,  `Q=y_1^2+y_2^2+y_3^2+y_4^2`.

Then

`|x|^2 = 1 - S + Q`.

The point is cut off by the smaller origin ball precisely when

`1-S+Q >= (1-epsilon)^2 = 1-2 epsilon+epsilon^2`,

or

`S-Q <= 2 epsilon-epsilon^2`.                                (4.3)

The relevant `y_i` are `O(epsilon)`. Scaling `y_i=epsilon z_i`, (4.3) converges to the simplex

`z_i>=0`,  `z_1+z_2+z_3+z_4 <= 2`.

Its four-dimensional volume is

`2^4/4! = 2/3`.

The perturbation of the boundary in the scaled variables is `O(epsilon)`, hence the physical volume lost at one corner is

`(2/3) epsilon^4 + O(epsilon^5)`.                            (4.4)

There are sixteen cube corners, giving (4.1).

Now ask which surviving center receives a generic lost point. For the positive face neighbor `e_i`,

`|x-e_i|^2-|x|^2 = 2 y_i`.

Any edge-, three-coordinate-, or body-diagonal corner center has squared-distance excess equal to twice a sum of at least two `y_i`, so the nearest competitor is a face neighbor corresponding to the smallest `y_i`. Away from a lower-order sliver where all `y_i=O(epsilon^2)`, that nearest face neighbor is still inside its unchanged radius-one ball; the exceptional sliver has volume `o(epsilon^5)` and does not affect the leading coefficient. Ties have measure zero.

By permutation symmetry, each of the four face directions incident to a given corner receives one quarter of (4.4). A fixed signed face neighbor is incident to eight corners of the origin's cube. Therefore its received volume is

`8 * (1/4) * (2/3) epsilon^4 + O(epsilon^5)`
`= (4/3) epsilon^4 + O(epsilon^5)`,

which is (4.2). QED.

### Why this matters

The ordinary derivative of the volume map at the critical cubic lattice vanishes in these corner directions. The natural small variable is therefore not the radius deficit `epsilon` but the **defect mass scale**

`h = epsilon^4`.                                              (4.5)

For one isolated shrink, the leading outgoing defect mass is distributed uniformly among the eight face neighbors. Formally, far from a forcing defect, simultaneous small radius deficits should therefore generate a nonlinear local balance whose first homogeneous term acts on the `h` variables like an eight-neighbor averaging operator.

I do **not** promote that coupled harmonic equation to a theorem in this run. Lemma 2 treats one shrinking radius with the incident competitors held critical. The next exact analytic obligation is to compute the simultaneous multi-radius corner functional and prove the error is controlled uniformly along the candidate below. The important movement is that the correct order and coefficient are no longer guessed: the critical response is quartic, with exact leading constants `32/3` total and `4/3` per face neighbor.

This is the B14 outcome: cubic symmetry turns the radius-tie singularity from a nuisance into an explicit local transfer law.

## 5. B29 — put a genuine boundary at infinity into a lattice-subset candidate

The previous Euclidean scaffold had a transient two-ended flow but no way to supply unit appetite without remote holes. Theorem 1 says a lattice subset automatically supplies the appetite and shielding. We can therefore move the transient structure from the **centers themselves** into a deterministic set of **missing lattice sites**.

### Explicit candidate

Work in `R^4` with appetite one. Define

`m_n = floor((1+|n|)^(3/4))`,  `n in Z`,                    (5.1)

and delete the expanding three-dimensional tube

`H = {(n,a,b,c) in Z^4 : 1<=a,b,c<=m_n}`.                   (5.2)

The center set is

`Xi_* = Z^4 \ H`.                                            (5.3)

This set is discrete and nonperiodic. Moreover

`#(H intersect B(0,R)) = O(R^(13/4))`,                       (5.4)

because a layer with `|n|<=R` contains `m_n^3=O((1+|n|)^(9/4))` deleted sites. Thus

`#(Xi_* intersect B(0,R)) = Theta(R^4)`,                     (5.5)

so the source's greater-than-quadratic necessary growth condition is satisfied. The stationary point-process uniqueness theorem is not being invoked for this deterministic nonperiodic set.

The recurrent-configuration theorem also does not dispose of this candidate. Already the nearest-neighbor graph on `Xi_*` contains the four-dimensional half-space `{a<=0}`, a transient subgraph; adding edges cannot turn a transient network recurrent. Hence the relevant bounded-distance graph is transient.

By Theorem 1, **every** stable allocation of `Xi_*` has every center sated inside its radius-one ball. Therefore all possible disagreement lives in a finite-range local active-cell system.

### Exact two-ended finite-energy channel on the tube boundary

The fixed side `a=0` of the deleted tube contains, for each `n>=0`, the surviving-center layer

`S_n = {(n,0,i,j): 1<=i,j<=m_n}`.                            (5.6)

It has `m_n^2 = Theta(n^(3/2))` centers. Since `x^(3/4)` is concave with derivative below one for `x>=1`,

`m_{n+1}-m_n in {0,1}`.                                      (5.7)

For `m'=m` or `m+1`, partition `[0,1)` into `m` intervals `I_i` and `m'` intervals `J_a`, and put

`t_m(i,a) = Leb(I_i intersect J_a).`                          (5.8)

Then

`sum_a t_m(i,a)=1/m`,  `sum_i t_m(i,a)=1/m'`.                (5.9)

Between `S_n` and `S_{n+1}`, define edge capacity

`q((i,j),(a,b)) = t_m(i,a) t_m(j,b)`.                        (5.10)

The row sums are exactly `1/m^2`, the column sums are exactly `1/(m')^2`, and the total flow across every layer is one. Whenever `q>0`, the two interval indices differ by at most one in each transverse coordinate. The centers `(n,0,i,j)` and `(n+1,0,a,b)` therefore lie at Euclidean distance at most

`sqrt(1^2+1^2+1^2)=sqrt(3) < 2 = 2R_4`.                     (5.11)

Thus these are genuine edges of the finite-range interaction geometry allowed by Theorem 1; unlike the old abstract scaffold, no long-distance parcel is required.

The energy of the flow across one layer is

`E_n = (sum_{i,a} t_m(i,a)^2)^2`.                             (5.12)

Since every overlap has length at most `1/m` and the overlaps sum to one,

`sum_{i,a} t_m(i,a)^2 <= 1/m`,

hence

`E_n <= 1/m_n^2 = O(n^(-3/2)).`                              (5.13)

Therefore

`sum_n E_n < infinity`.                                       (5.14)

By the electrical-network criterion, the positive-end boundary channel is transient. Reflecting `n` gives a second transient end. The tube boundary consequently contains exactly the kind of two-ended, finite-energy local channel which the source's disagreement-graph argument permits and which the earlier R08 scaffold was trying to realize.

This is the main reason to admit the candidate now. The three previous defects of the reserve constructions are simultaneously gone:

1. **fixed appetite:** the ambient critical lattice supplies unit-volume territories;
2. **global shielding:** every stable territory is automatically contained in a radius-one ball;
3. **boundary at infinity:** the expanding nonperiodic defect tube supplies a two-ended finite-energy channel using only interaction edges of length `<2`.

What is **not** proved is the decisive source obligation: that the site-optimal and center-optimal stable allocations actually choose different boundary conditions on this channel.

## 6. The frozen F0083 metric

F0083 is now promoted from reserve screening to an admitted R08 successor with one explicit candidate `Xi_*` and a two-obligation metric.

**Obligation 1 — candidate admissibility / local mechanism. PROVED.**  
`Xi_*` is a discrete source-admissible deterministic set with `Theta(R^4)` growth; source recurrence does not apply; every stable territory is sated and radius at most one; and the local interaction graph contains the exact finite-energy two-ended boundary channel (5.6)--(5.14).

**Obligation 2 — source-closing nonuniqueness. OPEN.**  
Exhibit two stable appetite-one Lebesgue allocations of `Xi_*` differing on positive measure. It is enough to show that the site-optimal and center-optimal allocations have different radial cumulative territory functions `gamma_xi(r)` for some center and radius.

Thus the newly frozen successor metric is

`F0083 explicit-candidate obligations: 1/2`.                  (6.1)

This is genuine admission movement, not a reset of the retired I0082 metric. I0082 remains separately frozen at `2/3`, retirement count `6`.

The canonical ownership claim `operations/claims/F0083.md` is created in the same commit as this report. I do not edit root ledgers or peer-track files; the structured delta below is the handoff for a coordinator/root writer.

## 7. What the three methods did

- **B13 FIND WHAT ONLY INCREASES.** Applied the source's center-deletion monotonicity and stable-allocation optimality in the critical lattice. Outcome: Theorem 1, an exact universal radius cap `sqrt(d)/2` for every stable allocation of every lattice subset. This removes the previous global-reservoir/shielding obstruction.
- **B14 FIND THE GROUP ACTING.** Used the full hypercubic symmetry at the critical radius tie. Outcome: Lemma 2; the first nonzero cell-transfer response in `d=4` is quartic, with exact total coefficient `32/3` and face-neighbor coefficient `4/3`. The correct small variable is defect mass `h=epsilon^4`, not `epsilon`.
- **B29 ADD THE POINTS AT INFINITY.** Replaced a finite/local defect by the explicit double-ended expanding tube (5.2). Outcome: an exact source-admissible candidate whose boundary has a finite-energy local channel to each end, while the ambient lattice handles appetite and shielding.

None of these results closes F0083. They turn the remaining obligation into one exact question for one explicit set rather than another open-ended construction search.

## 8. What remains and the next nonrepeating attacks

The exact blocking statement is now

`psi_site-opt != psi_center-opt  (mod null sets)  for Xi_* ?`  (8.1)

The simplest source-valid target is to show that on one fixed boundary center, say `(0,0,1,1)`, the two extremal allocations have different acceptance radii or different `gamma(r)` at some rational `r<1`.

The next run should **not** repeat B13/B14/B29. Three unused methods that now fit the sharpened problem are:

- **B4 PROVE SOMETHING WEAKER, COMPLETELY:** truncate the tube to `|n|<=N`, impose two opposite explicit boundary conditions outside, and prove a monotone separation at the central boundary center which is uniform in `N`;
- **B10 DERANDOMIZE:** replace any boundary-at-infinity probabilistic/flow intuition by an explicit deterministic pair of monotone radius iterates on the exact local volume system;
- **B21 ASK WHO ELSE HAS THIS SHAPE:** port potential-theoretic boundary-value methods for monotone finite-range systems on transient tubes, but only after translating every hypothesis into the active-cell volume map.

A finite truncation is useful only if it yields a rigorous inequality uniform in `N`. A plot showing two approximate radii is not movement of obligation 2.

The missing analytic ingredient behind the quartic heuristic is also precise: compute the simultaneous multi-radius version of Lemma 2, giving the homogeneous degree-four corner functional when all incident lattice centers have deficits of order `epsilon`. That functional should determine whether the two tube ends can support distinct fixed boundary data. If it turns out to be contractive despite finite electrical resistance, this candidate should be released rather than patched indefinitely.

## 9. Checker / audit status

No exact-arithmetic checker was created in this run. The new claims are theorem-sized analytic/geometric statements with proofs on the page; the finite-energy calculation is symbolic and contains no finite enumeration whose correctness would be improved by a checker. This follows the 90/10 rule rather than creating certificate-only activity.

F0083 is **not closed**. It has no outside audits, no paper folder, and no closure label. Closure would require obligation 2, a complete proof, the applicable exact finite certificate if a finite core is introduced, a dated prior-art record, and two independent OTHER-track audits.

## 10. Model / reasoning and task-control status

The model-control limitation remains exactly what the current repository ledger records and what the exposed task interface shows. The task surface allows prompt/title/schedule/timing/enabled controls, but exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum is still a prompt request only in this context.

Actually enforcing GPT-6/maximum would require an authorized product/API/workspace surface that exposes those two settings and reports the model/reasoning level used on the completed run. The historical P26 `You cannot modify this task` error was authorization-context-specific; repository state records that P26 was later successfully modified from another authorized context. The legitimate workaround is the owning context, supported ownership/admin transfer, or platform support, not task duplication. Per the controlling prompt, no scheduler modification was attempted here.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  retired_target:
    id: I0082
    status: RETIRED_FROZEN_PARTIAL
    metric_name: explicit_candidate_obligations_proved
    before: 2/3
    after: 2/3
    retirement_count_before: 6
    retirement_count_after: 6
    movement: false
  active_successor:
    id: F0083
    source: Hoffman_Holroyd_Peres_2006_Open_problem_i
    status_before: HOLD_NOT_READY_CLOSABLE
    status_after: ADMITTED_ACTIVE_PARTIAL
    ownership: R08_EXCLUSIVE_CLAIM_CREATED
    candidate: Xi_star_equals_Z4_minus_expanding_tube_H
    metric_name: explicit_candidate_obligations_proved
    before: NOT_ADMITTED
    after: 1/2
    obligations:
      candidate_admissibility_local_transient_channel: PROVED
      two_stable_allocations_positive_measure_disagreement: OPEN
    new_results:
      - any_stable_allocation_to_any_Xi_subset_Zd_has_all_centers_sated_with_radius_at_most_sqrt_d_over_2
      - d4_single_radius_shrink_loses_32_over_3_epsilon4_plus_O_epsilon5
      - each_d4_face_neighbor_receives_4_over_3_epsilon4_plus_O_epsilon5
      - explicit_Z4_expanding_tube_boundary_contains_local_two_ended_finite_energy_channel
    remaining_obligation: prove_site_optimal_and_center_optimal_allocations_differ_for_Xi_star
  methods_used: [13, 14, 29]
  checker: NOT_APPLICABLE_THEOREM_SIZED_ARGUMENTS_ON_PAGE
  shared_root_ledgers_edited: false
  peer_files_edited: false
  canonical_claim_created: operations/claims/F0083.md
```
