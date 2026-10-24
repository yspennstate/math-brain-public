Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `D_rev,0 = 0 -> 0`; Section-B methods #5, #18, #20 were genuinely attempted.**

# NM13-01 — P0292 frozen-endpoint barrier and route correction

Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-01` (`proofnet24/NM13-01/`)  
Category: `CLOSABLE OUTSIDE`  
Canonical source / claim: `P0292` / `operations/claims/P0292.md`  
Run date: 2026-09-17 UTC

## 1. Runtime, continuity, and controlling policy

The requested `GPT-6 / maximum` setting remains prompt text only on the task-control surface visible to this invocation. That surface exposes task prompt/title, schedule/timing mode, and enabled state, but no binding model-family field and no reasoning-effort field, and it does not return authenticated applied-runtime routing metadata. I therefore report the model family actually exposed to this invocation as **GPT-5.6 Sol** and reasoning level as **UNVERIFIED**. Making GPT-6/maximum enforceable would require product/backend support for persistent authorized model/reasoning fields plus per-run attestation of what actually executed.

I did **not** modify or probe any scheduler in this research run: the owner rules prohibit creating/modifying additional schedules here. Repository history still records a P26 edit attempt that returned `You cannot modify this task`, and later P26 reports explicitly treat that as an authorization/context denial rather than permission to bypass it. The lawful workaround is to use an owner/account/workspace context that actually owns the task, or a product/admin surface that exposes the required controls; never duplicate the task merely to evade ownership.

Before doing mathematics I recovered the current state required by the owner policy, including:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the NM13 deployment record;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the existing exclusive claim `operations/claims/P0292.md`;
- the newest NM13-01 report, `2026-09-17T21-03-28Z__p0292-first-order-reversible.md`;
- neighboring NM13-02's newest report (still admission-pending there, with no conflicting P0292 ownership);
- the P0292 historical attempt ledger (`P0292-A002`), the older Leskelä/P0291-P0292 memo, and its 3-state spectral/LP diagnostics.

The claim remains exclusively owned by NM13-01. This invocation therefore continues P0292; it does not rerun admission and does not create another claim.

## 2. Exact source and recovered state

Source: Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), Problem 4 (journal numbering; the arXiv numbering differs).

Exact source target: characterize by a simple necessary-and-sufficient condition the stationary ergodic CTMCs `lambda` on an ordered real state space for which

`c1 <= c2  ==>  lambda_{c1} >=_sm lambda_{c2}`,

where `lambda_c(t)=lambda(ct)` and `>=_sm` means all finite-dimensional supermodular stochastic order.

Canonical dedup key remains `characterize_ctmc_speed_monotonicity_in_supermodular_order`, SHA256 `3aded70a56a908e9042798ee4a8ac614005a51635e52453716ea79167c073ae5`, residue `0 mod 13`.

Historical P0292-A002 already established, and is **not** counted as new progress here:

- on the reversible 3-state star `1 -> 2` at `a2`, `1 -> 3` at `a3`, `2 -> 1` at `b2`, `3 -> 1` at `b3`, the source property fails when `b3>b2` already at two times;
- it is proved when `b2=b3` for all positive `a2,a3`;
- the unresolved star regime is `b2>b3`, numerically consistent with the conjecture that the star satisfies the source property iff `b2>=b3`;
- for arbitrary reversible 3-state chains the recovered necessary two-time criterion is `ell_1(1) ell_1(3) <= 0` for the slow left eigenvector `ell_1=pi v_1`; old finite LP experiments matched that sign criterion on their tested 3- and 4-time instances, but this is not a proof of all-FDD sufficiency.

The previous NM13-01 run froze and measured

`D_rev,0 = sup F_phi'(0+)`

over finite stationary irreducible reversible CTMCs, observation spans normalized to 1, and bounded supermodular tests `|phi|<=1`, obtaining the exact value `D_rev,0=0` by an edgewise conductance decomposition. Its proposed next route was to inspect second and higher Taylor coefficients on the first-order equality face.

## 3. Metric this run

Frozen metric (unchanged, as required):

- before: `D_rev,0 = 0` exactly;
- after: `D_rev,0 = 0` exactly;
- movement: **none**;
- unchanged-run counter after this report: **1**;
- stuck-recovery counter: **0**.

I do not replace the metric with a lemma count or a different local constant. The substantive result below changes the route, not the already-sharp first-order value.

## 4. The three genuinely attempted Section-B moves

### #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

I followed the previous report's proposed route and asked whether a first-order equality case could hide a **positive second-order (or later) coefficient** at the frozen endpoint `c=0`, thereby producing a local counterexample even though `F'(0+)=0`.

Outcome: the route is impossible for a structural reason stronger than the reversible first-order calculation. At `c=0` all sampled coordinates coincide, which is the comonotone coupling of their common stationary marginal. That coupling globally maximizes every supermodular expectation among all couplings with those marginals. Hence `F(c)<=F(0)` for every `c>=0`, even without reversibility or the Markov property. For a finite CTMC, analyticity then forces the **first nonzero Taylor coefficient at 0 to be negative**, never positive.

So the second-derivative hunt did not move `D_rev,0`; it instead proved that no finite Taylor order at the frozen endpoint can be the missing counterexample mechanism.

### #18 — SAY IT IN ANOTHER LANGUAGE

I rewrote the frozen-speed problem as a finite multimarginal coupling problem rather than a generator problem. The `c=0` law is the diagonal/comonotone coupling `(Z,...,Z)` of the stationary marginal. A self-contained finite rearrangement proof is given below.

Outcome: this exposes why the prior generator calculation had the right sign. The sign itself is a standard comonotone/supermodular extremality fact; the prior reversible conductance formula remains useful because it describes the **equality face**, but its endpoint sign should not be presented as a new reversibility phenomenon.

This is explicitly a **folklore / standard rearrangement mechanism, not a novelty claim**. Its value in this run is the route correction.

### #20 — FIND WHY THE ALGORITHM FAILS

The previous plan was: restrict to `F'(0)=0`, compute `F''(0)`, and look for positivity. The exact failure is now clear: the algorithm is searching for a local increase away from a point that is already a global supermodular maximum for fixed marginals.

Outcome: any genuine counterexample to Leskelä's speed order for a finite CTMC must have an **interior positive-speed increase**. Concretely, if `F(c2)>F(c1)` for some `0<=c1<c2`, analyticity/differentiability gives some `c_* in (c1,c2)` with `F'(c_*)>0`. Thus future work must attack positive-gap conditional kernels (the recovered `E1/E2` mechanism on three states), not higher derivatives at zero.

## 5. Route theorem: frozen endpoint is supermodular-maximal

### Proposition (standard comonotone endpoint barrier; rederived here)

Let `X=(X_t)` be **any stationary process** taking values in a finite totally ordered state space `S`. Fix `n>=2`, real times `t_1,...,t_n`, and a bounded supermodular function `phi:S^n -> R`. Define

`F(c) = E[phi(X_{c t_1},...,X_{c t_n})]`, `c>=0`.

Then

`F(c) <= F(0)` for every `c>=0`.

If in addition `X` is a finite-state CTMC, then `F` is real analytic in `c`. Hence either `F` is constant, or if `m>=1` is the least index with `F^(m)(0+) != 0`, then

`F^(m)(0+) < 0`.

In particular,

- `F'(0+) <= 0` for every stationary finite CTMC, reversible or not;
- if `F'(0+)=0`, then `F''(0+)<=0`;
- more generally, no first nonzero Taylor coefficient at the frozen endpoint can be positive.

### Proof

The only nontrivial ingredient is the finite comonotone rearrangement inequality, so I prove it rather than citing it as a black box.

Let `Y=(Y_1,...,Y_n)` be any `S^n`-valued random vector whose `n` one-dimensional marginals are all the same law `pi`. Let `Z~pi`. I claim

`E phi(Y) <= E phi(Z,...,Z)`.

First suppose the joint law of `Y` has rational masses. Choose a common denominator `N` and represent the law by `N` equally weighted row vectors

`x^(1),...,x^(N) in S^n`.

Because every coordinate marginal is `pi`, each coordinate column contains exactly the same multiset of state values.

Whenever two rows `x,y` are incomparable in the coordinatewise order, replace that pair by

`x wedge y` and `x vee y`.

This operation preserves every coordinate column as a multiset, because in each coordinate the unordered pair `{x_j,y_j}` is exactly `{min(x_j,y_j),max(x_j,y_j)}`. By supermodularity,

`phi(x wedge y)+phi(x vee y) >= phi(x)+phi(y)`,

so the empirical mean of `phi` does not decrease.

The uncrossing terminates after finitely many steps. To see this, encode the ordered states by integer ranks and use

`M = sum_r (sum_j rank(x_j^(r)))^2`.

For an incomparable pair `x,y`, write `m=x wedge y`, `Mrow=x vee y`. The total coordinate sum is preserved, while

`sum_j rank(Mrow_j) - sum_j rank(m_j)
 > |sum_j rank(x_j)-sum_j rank(y_j)|`

because incomparability means there are both positive and negative coordinate differences. For fixed total sum, this makes the sum of the two squared row-sums strictly larger. Thus each genuine uncrossing strictly increases the integer-valued bounded quantity `M`, so only finitely many are possible.

At termination all rows are pairwise comparable. Order them increasingly. Then every coordinate column is nondecreasing in that same row order. Since the coordinate columns have identical multisets, their sorted lists are identical term-by-term. Therefore every terminal row is diagonal:

`x^(r)=(z_r,...,z_r)`.

Its empirical law is exactly the diagonal/comonotone coupling of `pi`. Since the uncrossings never decreased the empirical `phi`-mean, the claimed inequality follows for rational joint laws.

For an arbitrary finite joint law with identical marginals, approximate it by rational points of the finite polytope defined by nonnegativity, total mass one, and equality of the coordinate marginals. That polytope has rational defining equations, so rational points are dense in each face. The joint masses, their common marginal, and the two expectations above vary continuously. Passing to the limit proves the same inequality without a rationality assumption.

Now apply this with

`Y=(X_{c t_1},...,X_{c t_n})`.

Stationarity gives every coordinate the same marginal `pi`. At `c=0`, all coordinates are literally the same random variable `X_0`, so the law is the diagonal coupling. Hence `F(c)<=F(0)` for every `c>=0`.

For a finite CTMC, every finite-dimensional probability is a finite sum of products of entries of matrix exponentials `exp(c Delta Q)`, so `F(c)` is real analytic. If it is not constant and `m` is the first nonzero Taylor order at zero, then

`F(c)-F(0) = F^(m)(0) c^m / m! + o(c^m)`

for `c downarrow 0`. Since the left side is nonpositive for all small positive `c`, the first nonzero coefficient must be strictly negative. QED.

## 6. What this corrects, and what it does not solve

This proposition does **not** solve P0292 and is not claimed as new literature. The source itself describes the frozen limit as the maximally autocorrelated endpoint, and comonotone maximization of supermodular costs is standard rearrangement/optimal-transport folklore.

It does, however, correct the strategic interpretation of NM13-01's previous result:

1. The previous reversible conductance identity for `F'(0+)` remains correct and useful for describing which first-order directions are flat.
2. The nonpositivity of `F'(0+)` is not special to reversibility; it is forced for every stationary process by the frozen comonotone endpoint.
3. Therefore the proposed search for `F''(0+)>0` on the reversible equality face cannot work. Nor can a third-, fourth-, or later-order endpoint search work: the first nonzero Taylor coefficient must be negative.
4. A source-valid failure of speed monotonicity must be generated at **positive speed / positive gaps**.

For the recovered reversible 3-state spectral reduction, varying one positive gap with all surrounding gaps fixed gives

`G(g)=C + alpha exp(-mu_1 g) + beta exp(-mu_2 g)`, `0<mu_1<mu_2`,

and gap monotonicity is equivalent to the two inequalities already present in the historical P0292 work:

`[E1]  mu_1 alpha + mu_2 beta >= 0` (equivalently the conductance-weighted local increasing-difference condition at `g=0` for the conditional kernel `Phi`),

`[E2]  alpha >= 0` (equivalently `<Phi, ell_1 tensor ell_1> >= 0`).

The unresolved mathematical obligation is still to control these **conditional** inequalities at positive surrounding gaps, especially for the star regime `b2>b3`, or to produce a positive-speed counterexample. This run did not prove that step.

## 7. Literature/status check (bounded, dated, and access-limited)

Search date: 2026-09-17 UTC (crossing into 2026-09-18 local time for this worker).

Queries included exact-title / exact-DOI searches for Leskelä's paper, `"Ross's second conjecture" supermodular stochastic ordering`, `supermodular Markov time ordering Leskelä`, and searches for `dependence in lag` / `nonmonotone Markov chains` / `supermodular stochastic ordering continuous-time Markov chain` through 2026.

Findings:

- Leskelä's author page still lists the 2022 Queueing Systems paper (DOI `10.1007/s11134-022-09824-0`); the bounded search did not recover a later source-matching resolution of Problem 4. This is **not** evidence of worldwide openness.
- The source itself cites T. Hu and X. Pan, *Comparisons of dependence for stationary Markov processes*, PEIS 14 (2000), 299–315. Its abstract explicitly studies decrease of dependence with lag in supermodular and concordance orders for stationary Markov processes, including continuous time. Any paper claim here must be compared carefully against those sufficient conditions.
- A particularly relevant older paper surfaced in this run: R. Kulik, *Monotonicity in lag for nonmonotone Markov chains*, PEIS 18 (2004), 485–492, DOI `10.1017/S0269964804184040`. Its abstract proves decreasing lag-covariance for a special subclass of nonmonotone doubly stochastic Markov chains. The accessible abstract does **not** establish Leskelä's all-FDD supermodular characterization, and the exact theorem hypotheses were not fully accessible through the bounded web view, so I do not infer that it settles P0292. It must nevertheless be included in the prior-art audit before claiming novelty for a nonmonotone finite-chain theorem.
- Kulik–Wichelhaus (Stochastic Models 23 (2007), 683–696) also studies dependence in lag using supermodular-type orders under sufficient assumptions. Again, this is neighboring machinery, not a recovered source-level resolution.
- The comonotone endpoint mechanism above is standard: modern optimal-transport references state that comonotone couplings maximize supermodular costs on fixed univariate marginals. I therefore label the endpoint proposition as a rederivation/route diagnosis, not a new theorem of independent novelty.

Access limits: some older journal full texts are paywalled or only partially indexed. I did not treat an abstract or a bounded negative search as proof that no theorem exists elsewhere.

## 8. Next step

Do **not** spend another run differentiating at `c=0`. The endpoint route is exhausted in principle.

Next Section-B triple (not yet attempted):

- **#15 BREAK THE SYMMETRY ON PURPOSE:** attack the unresolved star family with `b2>b3`, where the old equal-exit coin/skeleton proof breaks;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** read the exact hypotheses of Hu–Pan 2000 / Kulik 2004 / Kulik–Wichelhaus 2007 and test whether the star's slow-eigenvector sign criterion is a disguised known lag-order condition;
- **#30 ONE SCALE / ONE DIRECTION AT A TIME:** freeze all but one positive gap and seek a complete proof of `[E1]` and `[E2]` for the `b2>b3` star, starting with one-prefix or one-suffix conditional laws before attempting arbitrary histories.

A useful target for the next run is a genuine theorem of the form: for `b2>b3`, one of `[E1]` or `[E2]` holds for **all** one-sided conditional histories, with the remaining inequality isolated exactly. If that cannot be obtained, the run should try to construct an explicit positive-gap counterexample rather than returning to the frozen endpoint.

## 9. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-01
  category: CLOSABLE_OUTSIDE
  source_target: P0292
  claim_id: P0292
  status: PARTIAL
  source_status: OPEN
  metric:
    name: D_rev,0
    normalization: "finite stationary irreducible reversible CTMC; observation total span 1; bounded supermodular |phi|<=1"
    before: 0_exact
    after: 0_exact
  mathematical_movement: false
  substantive_route_result: "Frozen endpoint is the comonotone supermodular maximum for any stationary finite-state process; for finite CTMCs the first nonzero Taylor coefficient at c=0 is negative, so all endpoint Taylor counterexample routes are structurally impossible. Standard/folklore mechanism, not novelty claim."
  section_B_methods:
    attempted:
      - 5: "Differentiated beyond first order; endpoint Taylor route ruled out at every order."
      - 18: "Recast c=0 as a fixed-marginal coupling / rearrangement problem; self-contained finite proof recorded."
      - 20: "Identified exact failure of the previous second-order algorithm and redirected to positive-gap E1/E2 conditions."
    next: [15, 17, 30]
  unchanged_run_count: 1
  stuck_recovery_count: 0
  prior_art_update:
    - "Hu-Pan 2000: supermodular/concordance dependence-in-lag conditions; cited by source."
    - "Kulik 2004: nonmonotone doubly stochastic Markov chains, lag-covariance monotonicity; exact relation to P0292 still requires full-text theorem audit."
    - "Kulik-Wichelhaus 2007: supermodular-type dependence-in-lag sufficient conditions."
  audit_status:
    P26: NOT_REQUESTED
    NM13-02: NOT_REQUESTED
  artifacts_created: none
  shared_root_edits: none
  next_step: "Positive-speed / positive-gap attack on b2>b3 star via E1/E2; audit exact older lag-order hypotheses before any novelty claim."
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, peer-file edit, shared-root edit, or schedule creation/modification was performed.

**End of complete run report.**
