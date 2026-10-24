Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum.** No authenticated runtime model/effort telemetry or binding GPT-6/maximum selector is exposed here.

# R7-01 admission screen — E0075 renewal polling / large switch-over times

Date of literature check: **2026-09-19**  
Slot: `R7-01`  
Native ID: `6aabe777361481919c9e614646464772`  
Shard check: `sum(ord(c) for c in "E0075") = 273`, hence `273 mod 7 = 0`.  
Status after this screen: **HARD OUTSIDE / SOURCE OPEN-LOOKING / NOT_ADMITTED**.  
Canonical claim created: **no**.

## 1. Exact outside source and scope

Primary source:

- Marko A. A. Boon, Onno J. Boxma, Erik M. M. Winands, **“On open problems in polling systems”**, *Queueing Systems* 68 (2011), 365–374, published online 9 July 2011, DOI `10.1007/s11134-011-9247-9`.
- Current open-access source: https://link.springer.com/article/10.1007/s11134-011-9247-9
- Later arXiv copy: https://arxiv.org/abs/1408.0142
- Exact endpoint: Section 4.2, **Conjecture 4.2**, journal p. 371 / PDF p. 7, followed by **Open problem 2**, journal p. 372 / PDF p. 8.

The literal conjecture is:

> A cyclic polling system with general (renewal) arrival processes converges to a deterministic cyclic system when the deterministic switch-over times tend to infinity.

Open problem 2 asks for a rigorous proof of that conjecture.

The Section-4 context is essential. The problem concerns `N` cyclically visited queues in the class allowing the multitype-branching interpretation in the Poisson model; service requirements are independent with finite means, the load is stable, switch-over times are deterministic and tend to infinity with their ratios fixed, and the Poisson theorem being generalized scales waiting time by the total switch-over time `S`. In the Poisson case the source records

`W_i/S => ((1-rho_i)/(1-rho)) U_i`,

where `U_i` is uniform on `[(1-Phi_i)/Phi_i, 1/Phi_i]`, with `Phi_i` the exhaustiveness of the discipline. The source also uses the SCV of the queue length at a polling instant as a direct diagnostic and expects it to vanish.

The intake record is `probability_1000_intake_E_20260908/problems.jsonl`, canonical ID `E0075`, title “Large switch-over time asymptotics for polling systems with renewal arrivals”, source key `polling::open_problem_2`. No `operations/claims/E0075.md` existed in the current pre-write master check.

## 2. Current literature gate

Bounded current-source / later-author / citing-family checks on 2026-09-19 found:

1. **Boon–Boxma–Winands (2011)** itself, which states the general-renewal endpoint as open and explicitly identifies the circular dependence between random visit periods as the difficulty.
2. **Dorsman–van der Mei–Winands**, *A New Method for Deriving Waiting-Time Approximations in Polling Systems with Renewal Arrivals*, *Stochastic Models* 27 (2012), 318–332, DOI `10.1080/15326349.2011.567933`. It treats renewal arrivals and uses the large-switch-over regime as a limiting calibration/approximation; it does not provide a source-level rigorous proof of the whole branching-type Conjecture 4.2.
3. **Boon–Boxma**, “Polling: past, present, and perspective”, *TOP* 26 (2018), 335–369. Section 6 still describes renewal input as an area with relatively sparse exact results, and Section 10 explicitly lists both relaxing Poisson arrivals and studying large switch-over times among further-research directions.
4. **Boon–van der Mei–Winands**, “Heavy traffic analysis of roving server networks”, *Stochastic Models* 33 (2017), 171–209, arXiv:1611.02608. It gives powerful large-switch-over/fluid heuristics and special-case extensions for gated/exhaustive networks with renewal input, but the authors themselves describe the presentation as partly informal and identify rigor as further work. This is substantial partial prior art, not evidence that the full 2011 source endpoint has been rigorously closed.
5. **Hu–Dong–Perry**, “Asymptotic Optimality of the Binomial-Exhaustive Policy for Polling Systems with Large Switchover Times”, *Annals of Applied Probability* 32 (2022), 4803–4848, arXiv:2005.08840. Their large-switchover fluid/HDS analysis supplies a useful nearest solved analogue and a global fluid-cycle stability mechanism, but their stochastic model assumes Poisson arrivals, so it does not close the renewal endpoint.

A bounded 2026-09-19 phrase/title/follow-up search did not locate a later rigorous theorem matching all of Open problem 2. This negative search is **not** a novelty or openness certificate. The correct disposition is therefore “open-looking with substantial partial prior art,” not “verified open.”

A neighboring independent fleet admission screen (`proofnet24/NM13-03/.../2026-09-17T22-14-07Z__admission-screen-2.md`) independently classified E0075 as a **theorem-sized asymptotic problem**, not CLOSABLE-shaped.

## 3. Prior repository attempt and a correction

The prior intake attempt `E0075-A001` correctly noticed that the renewal problem should be attacked at the law-of-large-numbers level, but it claimed that heavy-tailed interarrivals with infinite mean residual life destroy uniform tightness and may force a finite-second-moment hypothesis.

That obstruction is not valid at the source scaling. **Finite mean interarrival time already suffices to make the residual renewal gap negligible after division by `S` on every fixed fluid horizon.** Infinite *mean* equilibrium residual life is not the same as failure of tightness, and more importantly the fluid-scale argument below bypasses residual-life independence altogether.

## 4. New derivation I — uniform renewal FLLN at endogenous polling intervals

Let `X_1,X_2,...` be iid positive interarrival times with

`mu = E X_1 in (0,infinity)`, `lambda = 1/mu`,

and let `N(t)` be the associated renewal counting process. For every fixed `T < infinity`,

`Delta_S(T) := sup_{0 <= t <= T} | N(S t)/S - lambda t | -> 0`

almost surely as `S -> infinity`.

### Proof

The ordinary renewal SLLN gives `N(u)/u -> lambda` almost surely as `u -> infinity`. Fix an outcome on which this holds. For any finite grid `0=t_0<...<t_m=T`, pointwise convergence gives

`N(S t_j)/S -> lambda t_j`

at every grid point. Since `N` is nondecreasing, for `t in [t_j,t_{j+1}]`,

`N(S t_j)/S <= N(S t)/S <= N(S t_{j+1})/S`.

Hence the deviation from `lambda t` is at most the maximum grid-point deviation plus `lambda (t_{j+1}-t_j)`. First let `S -> infinity`, then refine the grid. This proves uniform convergence on `[0,T]`.

Now let `0 <= U_S <= V_S <= ST` be **arbitrary random endpoints**, possibly stopping times or complicated polling epochs depending on the same arrival process. Then pathwise

`| (N(V_S)-N(U_S))/S - lambda (V_S-U_S)/S |`

`<= |N(V_S)/S-lambda V_S/S| + |N(U_S)/S-lambda U_S/S|`

`<= 2 Delta_S(T) -> 0`.

No independence between the interval endpoints and the renewal process is required. Thus the “circular interdependence” emphasized in the source does **not** obstruct the finite-horizon fluid law of large numbers for arrivals.

## 5. New derivation II — residual life is automatically o(S) with only a first moment

Let renewal epochs be `T_n = X_1+...+X_n`, and define the forward recurrence time

`R(t)=T_{N(t)+1}-t`.

For fixed `T`,

`sup_{0 <= t <= ST} R(t)/S -> 0`

almost surely.

### Proof

Because `E X_1 < infinity`, the tail-sum criterion implies `X_n/n -> 0` almost surely; consequently

`max_{1 <= k <= n} X_k/n -> 0`

almost surely. Also the renewal SLLN gives `N(ST)=O(S)` almost surely. Therefore the largest interarrival interval intersecting `[0,ST]` is `o(S)`, and every forward recurrence time on that horizon is bounded by that largest interval. Dividing by `S` proves the claim.

For comparison, if the renewal process is put in equilibrium, its residual tail is

`P(R_e>x) = (1/mu) int_x^infinity P(X_1>u) du`,

which is a proper probability law whenever `E X_1<infinity`, even if `E X_1^2=infinity` and hence `E R_e=infinity`.

**Consequence.** The old E0075-A001 “finite second moment needed because residual life is not tight” obstruction is removed. At the source’s `S` scale, a finite first moment is enough for residual gaps to vanish on finite fluid horizons.

## 6. New derivation III — explicit deterministic cycle balance for gated/exhaustive fluid systems

Write `rho_i=lambda_i E[B_i]` and `rho=sum_i rho_i<1`. Let the deterministic switch-over times be `S_i=s_i S`, with total scaled switch-over constant `s=sum_i s_i`.

Any periodic deterministic fluid cycle with unit-rate service must satisfy the work balance

`C = s S + sum_i V_i`,

while class-i flow conservation over a full cycle gives

`V_i = rho_i C`.

Therefore

`C/S = s/(1-rho)`,

`V_i/S = rho_i s/(1-rho)`.

These identities can also be recovered discipline-by-discipline:

- **Exhaustive:** the class-i fluid present at visit start is `rho_i(C-V_i)` work units; during service new work arrives at rate `rho_i`, so net drain rate is `1-rho_i`. Hence
  `V_i = rho_i(C-V_i)/(1-rho_i) = rho_i C`.
- **Gated:** the gate at a visit serves exactly the class-i work accumulated since the previous gate, a full-cycle interval, so directly `V_i=rho_i C`.

Thus the source’s deterministic-cycle candidate is not merely heuristic at the level of fluid fixed-point durations: its cycle and visit fractions are forced and unique by conservation. The renewal input distribution disappears from these first-order equations; only the rates survive.

## 7. What these lemmas do and do not prove

The lemmas remove the most obvious stochastic circularity **for bounded fluid horizons**. Given fluid-scale-tight initial conditions, renewal counts over all arrival intervals selected by the polling dynamics are asymptotically deterministic, and residual interarrival state is `o(S)` without a second-moment assumption.

They do **not** yet prove the source open problem, because Open problem 2 is a steady-state asymptotic statement. The missing theorem-sized gate is an interchange-of-limits/global-attraction statement:

1. establish tightness of stationary queue/workload states after scaling by `S`, uniformly as `S -> infinity`;
2. identify every subsequential stationary fluid limit;
3. prove the deterministic polling fluid dynamics has the required unique globally attracting periodic orbit for the full branching-type discipline class in the source;
4. deduce concentration of polling-instant queue lengths and the source waiting-time limit.

The 2022 Hu–Dong–Perry Poisson analysis is a close analogue precisely because it proves global fluid-cycle stability via a hybrid dynamical system / contraction mechanism and then controls stochastic stationary behavior. Extending that machinery to general renewal input requires augmenting the Markov state by renewal ages/residuals and proving the uniform stationary bounds; the two lemmas above show that **finite-horizon arrival noise itself is not the core blocker**.

## 8. Source-matching diagnostic and admission decision

A source-faithful observable is

`M(S) = max_i c^2_{P_i}(S)`,

the maximum squared coefficient of variation of the scaled queue length at a polling instant, because Tables 1–2 of the source use exactly this quantity as evidence for deterministic collapse.

For an admitted target its baseline would have to be frozen from rigorous evidence. Here:

- candidate metric baseline: **UNKNOWN/UNMEASURED**;
- candidate target: `M(S) -> 0` (only one observable implied by the broader conjecture, not a substitute definition of closure).

The source endpoint remains too broad/theorem-sized for R7-01’s preferred CLOSABLE role, and the current literature contains substantial special-case/fluid work. Therefore **E0075 is NOT_ADMITTED** and no canonical claim is created.

This is not a declaration that the source is closed, false, novel, or verified open. It is an admission decision: the honest remaining gate is a full stationary fluid-limit theorem, not a finite certificate, sharp constant, or short counterexample route.

## 9. Durable disposition

- Canonical ID: `E0075`
- Shard: `0` — eligible for R7-01 screening
- Ownership: no canonical `operations/claims/E0075.md` found at pre-write check
- Exact source: recovered
- Prior attempt: recovered and corrected
- Current literature: bounded check completed 2026-09-19
- Classification: **HARD OUTSIDE / theorem-sized / NOT_ADMITTED**
- Slot successor metric: remains **UNKNOWN/UNMEASURED**
- Slot stagnation: remains **NOT_STARTED**
- Section-B research methods: **not charged**, because no source crossed admission
- Next cursor: continue to the next unscreened/currently eligible residue-zero source; do not repeat E0075 unless source status, ownership, or a genuinely short closure route changes.
