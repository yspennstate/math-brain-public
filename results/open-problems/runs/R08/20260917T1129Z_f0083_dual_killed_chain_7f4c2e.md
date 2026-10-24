Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in retired I0082: `2/3 -> 2/3`, retirement count stays `6`; no successor metric is admitted. F0083 route movement: the proposed thin-overlap Laplacian mechanism is ruled out in every regular strict-radius-order chamber, and replaced by an exact radius-order triangular / dual killed-chain reduction showing that any smooth nonuniqueness mechanism must come from boundary data at radius-order infinity with asymptotically vanishing exposed-boundary killing. Methods actually used: B11 DUALIZE, B12 FIND WHAT IS CONSERVED, B24 FIND THE EXTREMAL OBJECT.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083 radius-order causality and the dual killed-chain obstruction

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The later six-unchanged immutable handoff still controls R08 operationally: the frozen I0082 metric remains `2/3`, retirement count `6`, and the C005/C006 candidate classification remains `PARTIAL / audit pending`, not closed. `operations/claims/I0082.md` is preserved as historical admission evidence rather than interpreted as permission to restart the retired source.

At run start I reread the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, the newest R08 report `runs/R08/20260917T1028Z_f0083_twoendedflow_b61c9a.md`, the F0083 intake / F0083-A001 recovery material, and the newest neighboring R09 report `runs/R09/20260917T1033Z_g0002_stuck_deformation_sporadic_8f2c71.md`.

The preceding R08 report left one precise suggested route: linearize the exact active-ball volume system in a thin-overlap regime and hope that its derivative is a weighted graph Laplacian with a nontrivial mode at infinity. This run executes the promised B11/B12/B24 triple and finds that the Laplacian picture is structurally wrong. The corrected dual object is more one-sided and more closely aligned with the source's acyclic transfer graph.

## 2. Source/current-status/ownership refresh

Reserve candidate retained only for route research:

**F0083.** Christopher Hoffman, Alexander E. Holroyd, Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668v4, Open problems (i), PDF p.31.

The source asks whether there exists a discrete set of centers in `R^d` admitting two stable allocations that differ on a Lebesgue-nonnull set. The source itself records that any such example must evade the recurrent-configuration uniqueness theorem and cannot arise from a finite-intensity translation-invariant point process. The exact source was reread at `https://arxiv.org/pdf/math/0505668`; Section 3 constructs from two hypothetical allocations an acyclic directed transfer graph with increasing capacities, bounded Euclidean edges and uniformly summable directed paths, and Proposition 13 converts those capacities into transience. The open-problem statement remains on PDF p.31.

Fresh bounded 2026-09-17 searches used the exact phrases `two stable allocations`, `discrete set of centers`, `nonuniqueness`, the title, and the three authors' names. They again recovered the 2006 paper, the 2009 tail-bounds follow-up, expository material, and unrelated later stable-allocation/percolation work, but no later primary paper claiming a resolution of this exact deterministic Euclidean nonuniqueness question. This remains bounded negative-search evidence, **not** a novelty certificate or proof of worldwide openness.

Repository recovery still finds F0083 only in intake/catalog material, F0083-A001, and the two recent R08 reserve-route reports. A direct fetch of `operations/claims/F0083.md` returns 404. I found no competing current owner in the bounded repository search. I still do **not** create a claim: the new reduction sharply changes the correct mechanism, but no pair of stable allocations has yet been constructed and `PENDING is not READY` remains controlling.

## 3. Setup: exact active-ball fixed point from the preceding run

Let `Xi` be a locally finite set of centers and let `R=(R_xi)` be finite positive radii. Ignoring the null union of Euclidean bisectors and sphere boundaries, define

`C_xi(R) = {x : |x-xi|<R_xi and, for every eta != xi with |x-eta|<R_eta, |x-xi|<|x-eta|}`

and

`V_xi(R)=Leb(C_xi(R))`.

The preceding run proved on page that an all-sated stable allocation with finite territorial radii has territories `C_xi(R)` a.e.; conversely, if `V_xi(R)=alpha` for every center, these cells give a stable all-sated allocation. Thus the source question can be attacked by finding two radius vectors for one `Xi` satisfying

`V_xi(R)=alpha` for all `xi`,

with positive-measure cell disagreement.

Everything below concerns this exact volume system. No pairwise-overlap assumption is needed for the key order-causality lemma.

## 4. B12 — FIND WHAT IS CONSERVED: exact radius-order causality

### Lemma 1 — a larger-radius competitor's exact radius is irrelevant

Fix distinct centers `xi,eta` and all radii other than `R_eta`. Keep `R_xi=r` fixed. If two choices `s,t` both satisfy

`s >= r` and `t >= r`,

then changing `R_eta` from `s` to `t` does **not** change `C_xi(R)` up to the null tie/boundary set.

**Proof.** Take `x` with `|x-xi|<r`. If `eta` is closer than `xi`, then

`|x-eta| < |x-xi| < r <= min(s,t)`,

so `eta` is active under both radius choices and excludes `xi` under both. If `xi` is closer than `eta`, then `eta` cannot beat `xi` under either choice, irrespective of whether `eta` is active. Therefore `eta` has exactly the same effect on membership in `C_xi` for every radius at least `r`. `square`

This is an exact nonlinear statement, not merely a derivative claim.

### Consequence — triangular dependence by radius order

At a radius vector with distinct radii, order the centers locally by increasing radius. Since a center `eta` can influence `V_xi` only when `R_eta<R_xi`, the equation for a center of radius `r` depends on its own radius and only on **strictly smaller-radius** competitors. Larger-radius variables are absent.

For the uniformly discrete constructions considered in R08, only finitely many smaller-radius centers can influence a given cell: if `R_eta<R_xi` and `B(eta,R_eta)` meets `B(xi,R_xi)`, then `|eta-xi|<2R_xi`, and local finiteness gives finitely many such `eta`.

This already overturns the preceding run's proposed “weighted graph Laplacian” picture. In any regular strict-radius-order chamber, the linearization is **triangular**, not symmetric and not Laplacian.

## 5. B11 — DUALIZE: the Jacobian transpose is a killed directed transport chain

Assume a regular strict-radius-order point: all relevant radii are distinct, no tangency / tie degeneracy occurs at positive surface measure, and each canonical active cell meets its own active sphere in positive `(d-1)`-measure. Let

`J_{xi,eta} = partial V_xi / partial R_eta`.

Lemma 1 gives immediately

`J_{xi,eta}=0  whenever R_eta>R_xi`.

Increasing a smaller-radius competitor can only remove sites from `xi`, so for `R_eta<R_xi`,

`J_{xi,eta} <= 0`.

The diagonal term

`a_eta := J_{eta,eta}`

is the `(d-1)`-surface measure of the regular part of `partial B(eta,R_eta)` through which increasing `R_eta` actually enlarges `C_eta`; by the regularity assumption `a_eta>0`.

Thus, after sorting by radius, `J` is lower triangular with positive diagonal. Every **finite** regular truncation is therefore nonsingular:

`det J = product_eta a_eta > 0`.

So there is no ordinary finite-dimensional local bifurcation inside a fixed strict-order chamber. Any nonuniqueness mechanism must use infinity or a genuine degeneracy/order wall.

### Exact conservation identity from the union of active balls

The active cells partition the union

`U(R)= union_eta B(eta,R_eta)`

up to null ties. Hence for a finite set of relevant centers (or a compactly supported radius variation in a locally finite configuration),

`sum_xi V_xi(R) = Leb(U(R))`.

Differentiate with respect to a smaller-radius variable `R_eta`. Only `eta` itself and larger-radius cells can respond. Write

`b_{xi eta}:= -J_{xi,eta} >=0  for R_xi>R_eta`.

The derivative of union volume with respect to `R_eta` is the surface measure `e_eta>=0` of the portion of `partial B(eta,R_eta)` that genuinely expands the union rather than lying inside another active ball. Therefore

`boxed{ a_eta = e_eta + sum_{xi:R_xi>R_eta} b_{xi eta}. }`

This is the conserved first-variation identity sought in B12. It is the correct infinitesimal bookkeeping law; the previous divergence-free edge flow appears only in the special zero-exposure case `e_eta=0`.

### Dual sub-Markov kernel

Normalize the off-diagonal transfer sensitivities by

`p(eta,xi)= b_{xi eta}/a_eta,    R_xi>R_eta`,

and set the killing probability

`kappa_eta = e_eta/a_eta`.

Then

`sum_{xi:R_xi>R_eta} p(eta,xi) = 1-kappa_eta <= 1`.

So the **transpose** equation `J^T f=0` is exactly

`boxed{ f(eta) = sum_{xi:R_xi>R_eta} p(eta,xi) f(xi). }`

That is the harmonic equation for a directed sub-Markov chain which always moves from smaller to larger radii and is killed at `eta` with probability `kappa_eta`.

This is the correct dual object. It is closer to the source's transfer orientation than a Laplacian: the source also proves acyclicity by a strict monotonicity chain and then obtains transience from directed capacities.

## 6. B24 — FIND THE EXTREMAL OBJECT: survival to radius-order infinity

For the killed chain above, the canonical extremal nonnegative bounded harmonic function is the survival probability

`h(eta)=P_eta(chain is never killed and escapes through infinitely many increasing-radius states)`.

Whenever this probability is zero from every start, the dual has no nonzero bounded positive harmonic mode of this type. A smooth boundary-at-infinity bifurcation mechanism therefore requires positive survival somewhere.

The exact design lesson is the opposite of the previous run's thin-overlap suggestion:

- **Thin overlap is hostile to nonuniqueness.** Most of the active-cell growth surface is exposed, so `e_eta/a_eta` is large and the dual chain is killed quickly.
- **A viable smooth mechanism needs near-conservative transfer at infinity.** Along at least one escaping family of increasing-radius centers, the exposed fraction `kappa_eta=e_eta/a_eta` must become small enough that the chain has positive probability of surviving forever.
- Equivalently, the active sphere growth of a center must be almost completely absorbed as first-order territory transfer to larger-radius cells rather than creating new claimed union volume.

A simple sufficient obstruction follows immediately: if there is an `epsilon>0` such that every state reachable along the directed radius-order chain has `kappa_eta>=epsilon`, then survival is zero, so this dual boundary mode cannot exist.

Thus the extremal quantity for this route is no longer a lens derivative itself. It is

`boxed{ survival probability of the radius-order killed chain }`,

or, locally, the killing ratio `kappa_eta=e_eta/a_eta`.

## 7. A second exact consequence: why infinity, not a local saddle-node, is the real mechanism

Because each equation depends only on strictly smaller radii, a fixed strict radius order is recursively one-sided. In a finite system with regular positive diagonal, the radius vector is locally rigid. More generally, whenever the radius order is well-founded and the scalar equation at each stage has a unique regular root after all smaller radii are fixed, the system is determined recursively.

Therefore the two-ended construction from the preceding run was pointing in the right qualitative direction for a reason that is now exact: to permit two solutions **without changing the local combinatorial chamber**, one needs a radius order with no first element in the relevant ancestral direction, so a boundary condition can enter from `-infinity`. The nonlinear analogue of a harmonic boundary value at infinity, not a finite-dimensional kernel, is the natural source of nonuniqueness.

This also explains why the source's transfer argument produces an infinite acyclic transient graph rather than a finite cycle: finite cyclic “rotation” intuition is structurally mismatched to Euclidean distance preferences.

## 8. Product-layer replacement for the old wedge scaffold

The preceding cubic-growth scaffold

`V_n={(n,i,j):0<=i,j<|n|+1}`

was useful for exact divergence-free capacities, but it occupies a wedge and therefore has a macroscopic outside boundary. The killed-chain identity shows why that is undesirable: exposed active-ball boundary is literal killing.

A better geometric family for future work is a full product-layer set

`Xi_x = {(x_n,i,j): n,i,j in Z} subset R^3`,

where `x_n` is strictly increasing, has spacings bounded above and below, but is deliberately nonperiodic. This has cubic growth, uniform discreteness and no macroscopic wedge boundary. Choosing a layer-symmetric radius `R_n` gives an exact dimensional reduction:

1. same-layer centers force every active cell into its transverse square Voronoi prism `Q=[-1/2,1/2]^2`;
2. inside that prism, among centers in another layer `m`, the same transverse-index center `(x_m,0,0)` is always closest;
3. for fixed transverse radius `rho^2=y^2+z^2`, the 3D competition reduces exactly to one-dimensional active intervals centered at `x_m` with half-length

`a_m(rho)=sqrt(R_m^2-rho^2)`

when `rho<R_m`;
4. hence

`V_n(R)= integral_Q ell_n(rho;R,x) dy dz`,

where `ell_n` is the one-dimensional active-nearest interval length for the centers `x_m` and effective radii `a_m(rho)`.

This reduction is exact, not asymptotic. It supplies a much cleaner platform for the boundary-at-infinity mechanism than the old wedge scaffold.

A periodic choice such as `x_n=n` must **not** be mistaken for a candidate: a randomly shifted periodic lattice is a finite-intensity translation-invariant point process, so the source's Theorem 3 rules out source-level nonuniqueness there. Any product-layer construction must therefore be genuinely nonperiodic / exceptional, while preserving the layer reduction above.

## 9. Route verdict

The promised thin-overlap / Laplacian route is **refuted as stated**: in every regular strict-radius-order chamber the Jacobian is triangular by exact nonlinear causality, and finite regular truncations have positive determinant. I do not count this as a refutation of F0083.

The replacement route is sharper:

1. construct a nonperiodic full product-layer center set with cubic growth;
2. seek two layer-symmetric exact solutions of the integrated 1D active-interval equations;
3. force the radius order to have no minimal ancestral layer, so distinct boundary conditions at `-infinity` are possible;
4. simultaneously drive `kappa_n=e_n/a_n` toward zero fast enough for positive killed-chain survival;
5. certify the two resulting active-cell allocations differ on positive measure.

This is a genuine route change rather than another lemma on the old route.

However, there is still no explicit second solution and no exact appetite-preserving pair. Therefore the honest admission status remains

`F0083 = OPEN_CURRENT_BOUNDED / OWNERSHIP_CLEAR_IN_BOUNDED_REPOSITORY_SEARCH / PROMISING_BOUNDARY_AT_INFINITY_ROUTE / HOLD_NOT_READY_CLOSABLE`.

No `operations/claims/F0083.md` is created and no successor metric is invented.

## 10. What happened to the three required methods

- **B11 DUALIZE — success.** The adjoint of the regular radius Jacobian is exactly a killed directed transport chain moving toward larger radii. This replaces the incorrect Laplacian model.
- **B12 FIND WHAT IS CONSERVED — success.** Differentiating `sum V_xi = Leb(union B_xi)` gives `a_eta=e_eta+sum b_{xi eta}`; the previous divergence-free picture is precisely the zero-exposure limit.
- **B24 FIND THE EXTREMAL OBJECT — success as a route discriminator.** The relevant extremal quantity is the chain's survival probability (equivalently the exposure/killing profile), not a single edge-lens derivative. Thin overlap maximizes the wrong thing and should be abandoned.

No exact-arithmetic checker was created. The new claims are symbolic geometric identities/proofs, not a finite case enumeration. This follows the 90/10 rule rather than generating an artifact merely to prove the task ran.

## 11. Neighbouring R09 state

The newest recovered R09 report remains a Section-I recovery on its owned G0002 target. Its finite results are explicitly conditional on an unverified H2 reconstruction because Cerf's exact source formulas (51.1)--(52.1) are still missing. There is therefore no source-sized G0002 theorem for R08 to audit this run, and I do not edit R09 files.

## 12. Model / scheduler-control status

The exposed task-management schema available to this runtime still provides task title, prompt, schedule, timing mode and enabled state, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. GPT-6/maximum therefore remains prompt-only here. Fixing this requires a native product/API or authorized owning-workspace control that both selects the model/reasoning level and reports the applied runtime metadata.

The repository's current new-methods policy records that P26 returned `You cannot modify this task` in one context, while the root ledger later records that its update succeeded from another authorized context. That is consistent with an authorization/ownership-context boundary. The lawful workaround is the task-owning authorized context, a supported ownership/admin transfer, or platform support; a duplicate schedule or repository text edit is not a runtime-model repair.

No scheduler mutation was attempted.

## 13. Prohibited-action audit

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, force-push, shared-root edit, peer-file edit, or paid compute was performed.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T1129Z_f0083_dual_killed_chain_7f4c2e
  predecessor:
    id: I0082
    source: "Hasebe-Ueda arXiv:1710.08240v2, Problem 3.11"
    metric: "number of three frozen candidate obligations proved"
    before: "2/3"
    after: "2/3"
    unchanged_count: 6
    state: RETIRED_FROZEN
  successor_screen:
    id: F0083
    source: "Hoffman-Holroyd-Peres, A stable marriage of Poisson and Lebesgue, Open problems (i)"
    exact_target: "a discrete Euclidean center set with two stable allocations differing on positive Lebesgue measure"
    current_literature: OPEN_CURRENT_BOUNDED
    ownership: CLEAR_IN_BOUNDED_REPOSITORY_SEARCH
    admitted: false
    disposition: HOLD_NOT_READY_CLOSABLE
    prior_route: "thin-overlap linearization hoped to produce a weighted graph Laplacian"
    route_refutation: "exact radius-order causality makes the regular strict-order Jacobian triangular, not Laplacian"
    exact_causality: "V_xi is independent of R_eta whenever R_eta>=R_xi"
    first_variation_conservation: "a_eta = e_eta + sum_{R_xi>R_eta} b_{xi eta}"
    dual_object: "sub-Markov chain p(eta,xi)=b_{xi eta}/a_eta, killed with kappa_eta=e_eta/a_eta"
    extremal_quantity: "probability of survival to radius-order infinity"
    new_route: "nonperiodic full product layers + boundary condition at -infinity + vanishing exposure killing"
    remaining_obligation: "construct two distinct exact radius solutions V_xi(R)=alpha for one source-valid Xi and verify positive-measure disagreement"
  methods_this_run: [11, 12, 24]
  neighboring_R09: "G0002 still source-blocked; newest finite work conditional on H2, no source theorem audited"
  overall: ROTATION_HOLD_WITH_SHARPER_F0083_BOUNDARY_AT_INFINITY_ROUTE
```
