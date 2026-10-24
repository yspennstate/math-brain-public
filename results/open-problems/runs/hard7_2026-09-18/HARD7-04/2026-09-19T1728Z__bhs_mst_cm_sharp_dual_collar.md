Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric: `beta_MST^- >= eta -> beta_MST^- >= eta`, with `eta=(tau-3)/(tau-1)`; methods actually used: B6 DEFORM, B20 FIND WHY THE ALGORITHM FAILS, B30 ONE SCALE AT A TIME.**

# HARD7-04 bounded research iteration — sharp dual subcriticality and the postcritical collar barrier

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Canonical target: `operations/claims/BHS-MST-CM-UNIV.md`, owner `HARD7-04`.

Status: **PARTIAL / source target remains OPEN**. This run proves an exact one-level branching/duality asymptotic that identifies the correct postcritical collar constant. It does **not** prove the configuration-model MST upper bound or scaling limit.

## 1. Continuity, source ownership, and required reads

I resumed the target admitted in the previous HARD7-04 run rather than restarting admission or revisiting I0049. The carry-in report is

`runs/hard7_2026-09-18/HARD7-04/2026-09-19T1631Z__bhs_mst_cm_critical_inheritance_lower_exponent.md`.

That run proved the source-relevant lower exponent

`beta_MST^- >= eta=(tau-3)/(tau-1)`

for the fixed minimum-degree-at-least-three configuration-model subclass, by deterministic inheritance of critical-component distances through Kruskal.

Before new mathematics I re-read the control / owner surfaces and continuity ledgers requested by the owner: `CONTROL.md`, `NEW_METHODS_2026-09-16.md`, `OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; I re-read the active `BHS-MST-CM-UNIV` claim, scanned the current HARD7 run directories and the nearby heavy-tailed configuration-model claim `P0150`, and refreshed the repository screen for I0049. The latter remains recorded as **KNOWN / RESOLVED IN QUEUED SCOPE**, so it is not reopened. Repository search found no competing owner for `BHS-MST-CM-UNIV` and no internal prior report already containing the `tau-3` dual-deficit calculation proved below.

No shared root ledger, peer track, claim owner, schedule, Gmail object, or Drive object was modified.

### Runtime capability honesty

The scheduler capability situation remains the same as the controlling repository record: the exposed automation interface has task title/prompt, schedule/timing mode and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed execution duration**. GPT-6/maximum is therefore prompt text only. This runtime identifies as GPT-5.6 Sol; reasoning-effort telemetry is unavailable, so the reasoning level is `UNVERIFIED`.

Changing that requires a platform/scheduler interface that actually exposes model and reasoning controls; a GitHub edit cannot create them. The historical P26 `You cannot modify this task` event is an authorization-context issue. The compliant workaround is the owning/authorized context or platform support, not bypassing permissions and not duplicating the task. I did not probe or modify P26 here.

## 2. Source/current-literature refresh — 19 September 2026

The primary target remains Shankar Bhamidi and Sanchayan Sen, *Geometry of the minimal spanning tree in the heavy-tailed regime: new universality classes*, PTRF 188 (2024), 729–804, DOI `10.1007/s00440-024-01259-3`, arXiv `2009.10696` v4 (12 January 2024).

Its abstract describes as a well-known open strong-disorder problem the prediction that MST distances for degree exponent `tau in (3,4)` scale as `n^eta`, and Section 8 explicitly identifies the next universality program as “starting with the configuration model and (simple) random graphs with given degree sequence.” The paper proves the rank-one inhomogeneous model, not the configuration-model case.

Relevant nearest results remain:

1. Dhara–van der Hofstad–van Leeuwaarden–Sen, *Heavy-tailed configuration models at criticality*, AIHP 56 (2020), 1515–1558, DOI `10.1214/19-AIHP980`: critical component-size / surplus scaling and critical percolation evolution for `tau in (3,4)`.
2. Bhamidi–Dhara–van der Hofstad–Sen, *Global lower mass-bound for critical configuration models in the heavy-tailed regime*, EJP 27 (2022), paper 103, arXiv `2005.02566`: GHP convergence of critical clusters and hence diameter convergence under the stated stronger assumptions.
3. van der Hofstad–Janson–Luczak, *Component structure of the configuration model: Barely supercritical case*, RSA 55 (2019), 3–55, DOI `10.1002/rsa.20837`: general barely-supercritical giant-component and exploration technology, including unbounded-third-moment regimes, but not the MST complement-control theorem needed here.
4. The Bhamidi–Sen rank-one proof itself: Section 6 controls the diameter outside the principal critical component at a slightly later level, then telescopes Hausdorff increments over a geometric level ladder. Proposition 6.15 and the subsequent Section 6.6 summation are the structural template this run targets.

Fresh bounded searches on 19 September 2026 for the exact source title plus `configuration model MST heavy-tailed`, `minimum spanning tree configuration model power law`, and later 2025–2026 variants found no source-matching configuration-model MST scaling-limit theorem. This is bounded negative evidence only, not a worldwide novelty certificate.

The branching-process extinction duality used below is classical/folklore machinery. I do **not** claim that the scalar coefficient `tau-3` is new to branching-process or percolation theory; the research gain here is identifying and proving the exact coefficient needed by this specific MST complement route, and exposing the sharp collar obstruction before attempting a graph-level transfer.

## 3. Frozen metric: before / after

The fixed task metric is

`beta_MST^- := sup{ beta >=0 : for every delta in (0,1) there exists c_delta>0 with liminf P(diam(M_n)>=c_delta n^beta)>=1-delta }`.

The previous run established

`beta_MST^- >= eta`,  `eta=(tau-3)/(tau-1)`.

The only unconditional upper bound currently certified in this track is the trivial `beta_MST^- <=1` from `diam(M_n)<=n-1`. This run does not yet control the postcritical Kruskal attachments in the actual configuration model, so the rigorous interval remains

`eta <= beta_MST^- <= 1`.

Thus the frozen metric has **NO MOVEMENT** this run. The value of the run is a new exact analytic subcriticality coefficient and a failure threshold for the next proof mechanism.

## 4. Idea-before-code checkpoint and method rotation

Before writing this proof I created and read back

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1728Z__bhs_mst_cm_sharp_dual_collar_idea.md`

at creation commit

`175014dbd81777473e75bf2c523d006a9ae5dffa`.

The previous BHS-MST run used B1/B2/B19. The fresh triple is disjoint:

- **B6 — DEFORM TO A POINT YOU CAN SOLVE.** Freeze one percolation level and pass from the full MST problem to the exactly solvable Galton–Watson extinction dual.
- **B20 — FIND WHY THE ALGORITHM FAILS.** Compute the maximal first-order sprinkling collar compatible with subcriticality; a wider collar is impossible through this mean mechanism.
- **B30 — ONE SCALE AT A TIME.** Use the resulting collar to prescribe a geometric `lambda` ladder, separating the analytic mean calculation from the still-missing uniform random-graph transfer.

No checker was created because there is no finite claim to certify; manufacturing one would violate the 90/10 instruction.

## 5. Exact one-level dual identity

Let `D` denote the limiting degree law of the canonical regularly varying power-law subclass, with

`0 < mu:=E[D] < infinity`,

and define the size-biased excess variable

`X:=D^*-1`,

with probability generating function

`h(s):=E[s^X]=E[D s^(D-1)]/mu`.

Write

`nu:=h'(1)=E[D(D-1)]/E[D]`

and `p_c:=1/nu`.

For bond percolation with parameter `p>p_c`, the excess offspring pgf is

`phi_p(s)=h(1-p+ps)`.

Let `u_p<1` be its extinction probability, `u_p=phi_p(u_p)`, and put

`q_p:=1-p+p u_p`.

Then `u_p=h(q_p)` and equivalently

`q_p=1-p+p h(q_p)`.

Set `y:=1-q_p>0`. The root equation is

`y=p[1-h(1-y)]`,

hence the exact secant identity

`1/p = [1-h(1-y)]/y = (1/y) int_0^y h'(1-t) dt`.                 (5.1)

The Galton–Watson process conditioned on extinction has pgf `phi_p(u_p s)/u_p`, so its mean is exactly

`m_-(p):=phi_p'(u_p)=p h'(q_p)=p h'(1-y)`.                     (5.2)

Define

`g(t):=nu-h'(1-t)`.

Subtracting the average in (5.1) from `nu` gives the exact identities

`p nu-1 = p A(y)`,                                               (5.3)

`1-m_-(p) = p [g(y)-A(y)]`,                                     (5.4)

where

`A(y):=(1/y) int_0^y g(t) dt`.

Therefore

`(1-m_-(p))/(p nu-1) = [g(y)-A(y)]/A(y)`.                       (5.5)

This is the useful dual formula: the supercritical excess is the **average** loss of the derivative over `[1-y,1]`, whereas the subcritical dual deficit is the remaining endpoint-minus-average loss.

### Universal sanity bound

Because `h` is a pgf, `h'',h'''>=0`. Hence

`g'(t)=h''(1-t)>=0`,  `g''(t)=-h'''(1-t)<=0`.

So `g` is increasing and concave, with `g(0)=0`. Concavity gives `g(t)>= (t/y)g(y)` for `0<=t<=y`, and therefore

`g(y)/2 <= A(y) <= g(y)`.

In (5.5), this yields

`0 <= (1-m_-(p))/(p nu-1) <= 1`.                               (5.6)

Thus the extinction-dual process is subcritical, but its deficit can be substantially smaller than the original supercritical excess. This already warns against importing the Erdős–Rényi coefficient `1` without checking the heavy-tail law.

## 6. Heavy-tail theorem: the coefficient is exactly `tau-3`

Assume the canonical regular-variation condition

`P(D>=k) = c k^{-(tau-1)} L(k)(1+o(1))`,                       (6.1)

with `tau in (3,4)` and `L` slowly varying.

Size-biasing lowers the tail exponent by one, so

`P(X>=x)` is regularly varying with exponent `-(tau-2)`.

Put

`alpha:=tau-2 in (1,2)`,  `beta:=alpha-1=tau-3 in (0,1)`.

Since `E[X]=nu<infinity`, the standard Karamata Abelian theorem for a regularly varying tail of index `-alpha` applied to the derivative of the pgf gives

`g(y)=nu-h'(1-y)` regularly varying at zero with index `beta`. (6.2)

Equivalently, for some slowly varying `L_1`,

`g(y)=y^beta L_1(1/y)` up to a positive asymptotic constant.

Karamata's integral theorem, valid because `beta>-1`, now gives

`A(y)=(1/y)int_0^y g(t)dt ~ g(y)/(beta+1)`.                    (6.3)

As `p downarrow p_c`, the nontrivial extinction root satisfies `q_p upward 1`, hence `y downarrow0`. Substituting (6.3) into (5.5),

`(1-m_-(p))/(p nu-1)
 -> [1-1/(beta+1)]/[1/(beta+1)]
 = beta
 = tau-3`.                                                     (6.4)

Therefore, writing

`p=(1+epsilon)/nu`,  `epsilon downarrow0`,

we obtain the sharp one-level expansion

`m_-(p)=1-(tau-3)epsilon+o(epsilon)`.                          (6.5)

This is a complete analytic proof of the scalar statement (6.5) for the regularly varying limiting degree law. No finite-size simulation enters.

### Height corollary for the exact Galton–Watson dual

Let `H_p` be the height of the Galton–Watson process with the extinction-conditioned offspring law. Since its mean is `m_-(p)`, for generation size `Z_r`,

`P(H_p>=r) <= P(Z_r>=1) <= E[Z_r]=m_-(p)^r`.

Thus for every fixed `a>0`, if `r=a/epsilon`, then by (6.5)

`limsup P(H_p>=a/epsilon) <= exp(-(tau-3)a)`.                  (6.6)

The natural dual-height scale is therefore `epsilon^{-1}`, with the explicit heavy-tail rate coefficient `tau-3`. This is precisely the scale `n^eta/lambda` when `epsilon=lambda n^{-eta}`.

## 7. B20: the sharp first-order collar obstruction

The rank-one source proof does not stop at the same level: it controls the complement of the principal component at level `lambda` after sprinkling to a slightly later level. To see what a configuration-model analogue may permit, freeze the extinction tilt from `p` and define the first-moment collar proxy

`m_proxy(delta):=p_delta h'(q_p)`,

where

`p=(1+epsilon)/nu`,

`p_delta=(1+(1+delta)epsilon)/nu`.

Then

`p_delta/p = [1+(1+delta)epsilon]/[1+epsilon]
            = 1+delta epsilon+O(epsilon^2)`.

Combining this with (6.5),

`m_proxy(delta)
 = 1-(tau-3-delta)epsilon+o(epsilon)`.                         (7.1)

Hence the **branching-proxy collar barrier** is

`delta_* = tau-3`.                                              (7.2)

For every fixed `delta<tau-3`, the proxy is subcritical by a linear margin. For every fixed `delta>tau-3`, it is supercritical to first order. At `delta=tau-3`, the first-order margin vanishes.

This is a genuine counterexample-oriented result: it shows why a tempting proof that sprinkles by an arbitrary fixed relative multiple of the nearcritical excess cannot work through extinction-tilted first-moment domination. The allowable collar collapses as `tau downarrow3`.

**Important scope:** `m_proxy(delta)` is an analytic proxy obtained by keeping the `p`-extinction tilt while raising the edge level. Equation (7.1) is not, by itself, a theorem about the actual conditioned two-level configuration-model remainder. The latter has pairing and conditioning structure that must still be transferred rigorously. I do not call (7.1) an MST upper bound.

## 8. B30: what the full graph proof now has to show

The preceding calculation fixes the scale choice rather than leaving it heuristic. Choose once and for all

`0<delta_0<tau-3`.

For a geometric ladder

`lambda_j=(1+delta_0)^j lambda_0`,

set the nearcritical excess `epsilon_j=lambda_j n^{-eta}`. If the configuration-model complement at level `lambda_j` can be shown uniformly to inherit the dual mean expansion, then the residual exploration at the next level has a deficit of order

`(tau-3-delta_0) lambda_j n^{-eta}`.

The exact remaining obligations are now:

1. **Triangular-array dual transfer.** Upgrade (6.5), which is a limiting-law statement, to the empirical percolated half-edge law after deleting the actual principal component, uniformly for a growing range of `lambda_j`.
2. **Two-level conditioning.** Show that sprinkling from `lambda_j` to `(1+delta_0)lambda_j` is dominated by a process whose effective mean is at most `1-c lambda_j n^{-eta}` with some fixed `c>0`.
3. **Path/height bound.** Convert that mean deficit into a uniform residual-diameter or longest-path estimate on the scale `n^eta/lambda_j` (a logarithmic weakening would still be enough for an exponent theorem).
4. **Kruskal telescoping.** Insert those residual bounds into the deterministic Hausdorff-increment mechanism used in Bhamidi–Sen Section 6 and sum the geometric series.
5. **Late regime.** Couple the final portion of the weight process, once `lambda` is polynomially large, without losing the `n^eta` scale.

The source's rank-one Proposition 6.15 plus Section 6.6 show exactly why obligations 2–4 are the decisive shape. The current CM critical-GHP theorem supplies the critical core but not these uniform postcritical complement estimates; this matches Bhamidi–Sen Section 8's warning that control of the complement is the difficult missing ingredient.

## 9. Why the frozen beta metric does not move yet

If obligations 1–5 yielded even

`diam(M_n)=O_P(n^eta (log n)^C)`

for some fixed `C`, then every `beta>eta` would be impossible in the definition of `beta_MST^-`, and the previous lower bound would immediately give

`beta_MST^-=eta`.

This run stops short of that because it has not proved the empirical two-level dual transfer. Treating the branching proxy as the graph would be exactly the kind of finite-/local-to-global overclaim prohibited by the owner instruction.

Accordingly:

**before:** `eta <= beta_MST^- <=1`;

**after:**  `eta <= beta_MST^- <=1` — **NO MOVEMENT**.

What did move is the proof architecture: the unknown postcritical collar is now pinned to the sharp first-order coefficient `tau-3`, and a collar wider than that is ruled out for the extinction-tilted mean route.

## 10. Next bounded run

This is the first no-movement run on the newly admitted BHS target, so section-I stuck rotation does not trigger. The next run should not repeat B6/B20/B30. The most useful fresh triple is:

- **B9 RANDOMIZE:** expose the percolated half-edge pairing and giant through a stopping construction that leaves a conditionally uniform remainder;
- **B11 DUALIZE:** formulate the empirical remainder mean as a weighted derivative/size-biased functional whose target is (6.5);
- **B25 COUNT THE SAME THING TWICE:** compute that functional both from deleted-half-edge mass and from the extinction tilt, aiming for an `o_p(lambda n^{-eta})` relative error uniformly on a controlled lambda range.

The success criterion for that run is not another scalar checker. It is a graph-level lemma transferring the `tau-3` deficit to the actual conditioned remainder on at least one nontrivial growing `lambda` window.
