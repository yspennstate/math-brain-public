Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `C_large = 1/pi -> 1/pi`; status `PARTIAL`; Section-B methods actually tried: #4 PROVE SOMETHING WEAKER, COMPLETELY, #8 GO THE OTHER WAY AND DISCRETIZE, #19 MAKE IT AN ALGORITHM.**

# NM13-12 — E0086 screened excursion-profile theorem

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0086` / `operations/claims/E0086.md`  
Canonical dedup key: `favorite_sites::op_2`  
Canonical SHA-256 / shard: `a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c`, residue `11 mod 13`

## 1. Runtime disclosure, controls, continuity, and required reads

The task prompt requests `GPT-6 / maximum`. That is **not** the runtime I can honestly report. The actual model is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, verified maximum reasoning, a binding model/effort setting, an hour-long execution, or a support escalation.

The exposed task-control surface still has task identity/title/prompt, scheduling or relative-start fields, timing mode, and enabled state. It has **no bindable model-family selector and no bindable reasoning-effort selector**. Thus GPT-6/maximum remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model/reasoning controls together with authenticated per-run runtime attestation. Historical `You cannot modify this task` responses, including the earlier P26 case, are authorization-context boundaries; repository continuity records a later successful P26 edit from another authorized context. The lawful workaround is the owning/otherwise-authorized context or platform/admin support, not task duplication or access-control bypass. This invocation did not create, modify, disable, or duplicate a schedule.

Before research I read or targeted-search-recovered the current owner-required state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0086.md`;
- newest own report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T10-59-40Z__e0086-stuck-recovery-1-successful-point-port.md`;
- newest neighboring NM13-11 report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T10-52-29Z__e0082-mandatory-handoff-successor-screen.md`;
- newest visible designated audit-partner NM13-13 report `proofnet24/NM13-13/runs/2026-09-18/2026-09-18T10-57-05Z__successor-admission-delta-screen-6.md`;
- the E0086 intake row, canonical aliases, historical attempt `E0086-A001`, current/historical claim material, and fresh exact searches for E0086 audit/ownership changes.

Large aggregate JSONL and root-ledger views can be connector-truncated. I therefore used current root files plus exact ID/key/path searches for E0086 and its aliases rather than pretending a truncated rendering was a byte-for-byte reread of every historical row. Immediately before the write phase, an observed master head was `20a7f58dcc72ff1b65cff45023f608d264e219c8`. I recovered no release, duplicate owner, POSTED/campaign settlement, source-specific retirement, P26 PASS, or NM13-13 PASS for E0086.

The predecessor ended at

```text
C_large = 1/pi
unchanged_runs = 4
stuck_recoveries = 1
recovery_choice = PORT_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM
next_methods = 4, 8, 19
```

so this invocation carries out that port rather than returning to another global Green-resolvent lemma.

## 2. Exact source and current-status refresh

The source remains Izumi Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787, Open Problem 2. For planar simple random walk it asks for the almost-sure asymptotic of `M_{Dtilde_n}(n)` for varying source patterns `Dtilde_n in H` outside `D(0,a_n)`, and highlights

\[
\widetilde D_n\subset D(0,n^\beta)^c\cap D(0,2n^\beta),
\qquad 0<\beta<\tfrac12.
\]

The frozen metric remains the already-certified large-radius quantity

\[
C_{\rm large}:=\lim_{n\to\infty}\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\quad\text{in the separate regime }a_n\ge n^{1/2+\varepsilon},
\]

with current certified value `1/pi`. It is not replaced by a main-regime diagnostic merely to manufacture movement.

Fresh bounded 2026-09-18 searches again found Okada's 2020 pair-favorite-point paper as the closest solved multiscale analogue. That paper uses successful/qualified points, nested excursion-count profiles, a two-point estimate indexed by the first separating scale, and then a bounded second moment. The 2025 Hao--Li--Okada--Zheng work concerns the number/evolution of ordinary favorite sites, not the translated-boundary quantity in E0086. A 2026 Okada coauthored paper on fluctuations of random-walk ranges concerns different observables. No source-matching later resolution of Open Problem 2 surfaced in this bounded search. That is negative evidence only; worldwide openness and publication novelty remain **UNVERIFIED**.

Access scope: primary-source/arXiv material and accessible abstracts/index pages were inspected. I do not claim an exhaustive citation graph or paywalled full-text review.

## 3. Recovery-1 milestone carried into this run

The preceding stuck recovery identified one precise first milestone for the successful-point port. Fix

\[
0<\beta<\alpha<\tfrac12,\qquad R=n^\alpha,
\qquad n^\beta<|h_n|\le2n^\beta,
\]

and an interior candidate `y`. Write `b=y+h_n`, let `D` be the finite disk used by the inner stopping construction, and kill the walk at

\[
K:=T_b\wedge\tau_D.
\]

The previous reports proved that the killed one-point Green function satisfies

\[
G_D^{\neg b}(y,y)
=\bigl[\sigma_1+o(1)\bigr]\log n,
\qquad
\sigma_1=\frac2\pi\left(2\beta-\frac{\beta^2}{\alpha}\right),
\tag{3.1}
\]

and hence, for `m=c(log n)^2`, the one-center first-moment threshold is

\[
c_\alpha=2\alpha\sigma_1
=\frac4\pi(2\alpha\beta-\beta^2).
\tag{3.2}
\]

The recovery demanded more than the aggregate geometric tail: define a **screened successful profile** across a finite nested scale ladder, including the moving taboo scale `|h_n|`, and prove that imposing this profile does **not** change the one-center power exponent. That is what is proved below.

## 4. Exact regenerative factorization of screened return excursions

The following lemma is finite-state and exact; no asymptotic approximation is used.

### Lemma 4.1 — conditional iid screened excursions

Let `X` be simple random walk in a finite domain `D`, let `y in D`, let `b in D\{y}`, and put

\[
K=T_b\wedge\tau_D.
\]

Starting from `y`, define `rho_0=0` and successive strict return times

\[
\rho_i=\inf\{k>\rho_{i-1}:X_k=y\},\qquad i\ge1.
\]

Let

\[
p:=P_y(\rho_1<K)=P_y(T_y^+<T_b\wedge\tau_D).
\tag{4.1}
\]

For a returned excursion path `e`, define the probability law

\[
Q(A):=P_y\bigl((X_0,\ldots,X_{\rho_1})\in A,\rho_1<K\bigr)/p.
\tag{4.2}
\]

Then, conditional on `rho_{m-1}<K`, the first `m-1` returned excursion paths

\[
E_i=(X_{\rho_{i-1}},\ldots,X_{\rho_i}),\qquad 1\le i\le m-1,
\]

are independent and each has law `Q`. Moreover

\[
P_y(\rho_{m-1}<K)=p^{m-1}.
\tag{4.3}
\]

#### Proof

For measurable path sets `A_1,...,A_{m-1}`, apply the strong Markov property successively at `rho_1,...,rho_{m-2}`. Each successful return resets the walk at the identical state `y` with the same fixed domain `D` and taboo point `b`. Therefore

\[
P_y\left(\bigcap_{i=1}^{m-1}\{E_i\in A_i\},\rho_{m-1}<K\right)
=\prod_{i=1}^{m-1}P_y(E_1\in A_i,\rho_1<K).
\tag{4.4}
\]

Taking every `A_i` equal to the full returned-excursion path space gives (4.3). Dividing (4.4) by `p^{m-1}` gives the product law `Q^{\otimes(m-1)}`. `square`

The geometric local-time law used in the previous Green-function arguments is therefore not merely a one-dimensional tail: before killing, its successful return excursions carry an exact iid path decomposition.

## 5. A complete finite-profile concentration theorem

### Theorem 5.1 — screened excursion-profile barrier costs no power

In the setup of Lemma 4.1, let

\[
\phi_1,\ldots,\phi_J:\{\text{returned excursion paths}\}\to\{0,1\}
\]

be arbitrary path statistics. Put

\[
\theta_j=E_Q\phi_j(E_1),
\qquad
N_j=\sum_{i=1}^{m-1}\phi_j(E_i),
\qquad
\mu_j=(m-1)\theta_j.
\tag{5.1}
\]

For every `u>0`, define the barrier event

\[
\mathcal B(u)=
\bigcap_{j=1}^J
\left\{
|N_j-\mu_j|
\le \sqrt{2\mu_j u}+\frac23u
\right\}.
\tag{5.2}
\]

Then

\[
\boxed{
P_y\bigl(\rho_{m-1}<K,\mathcal B(u)\bigr)
\ge
p^{m-1}\bigl(1-2J e^{-u}\bigr).
}
\tag{5.3}
\]

#### Proof

By Lemma 4.1, conditional on `rho_{m-1}<K`, the variables

\[
\phi_j(E_1),\ldots,\phi_j(E_{m-1})
\]

are iid Bernoulli with mean `theta_j`, so `N_j` is binomial with conditional mean `mu_j`. Bernstein's inequality for a sum of Bernoulli variables gives

\[
P\left(
|N_j-\mu_j|>
\sqrt{2\mu_j u}+\frac23u
\ \middle|\ \rho_{m-1}<K
\right)
\le2e^{-u}.
\tag{5.4}
\]

A union bound over `j=1,...,J` gives

\[
P(\mathcal B(u)^c\mid \rho_{m-1}<K)\le2Je^{-u}.
\tag{5.5}
\]

Multiplying the complementary bound by (4.3) proves (5.3). `square`

This theorem is intentionally more general than a radial scale choice: the finite statistics may include annulus crossings, returns to designated neighborhoods, angular sectors, or approaches to the translated taboo point. Thus the moving taboo geometry can be made part of the profile rather than erased into one terminal Green number.

## 6. Application to the E0086 singleton lower-bound route

Choose candidate sites `y` in a fixed interior annulus of the disk `D(0,R)`, so the scale ladder below fits uniformly around each candidate. Let

\[
2\le r_1<\cdots<r_J\le R/8
\]

be a geometric ladder with `J=O(log n)`, adjusted so that one distinguished radius satisfies

\[
\frac14|h_n|\le r_{j_*}\le\frac12|h_n|.
\tag{6.1}
\]

For each returned excursion from `y` before `T_{y+h_n}\wedge\tau_D`, include among the statistics `phi_j`:

1. whether the excursion reaches distance at least `r_j` from `y` before returning;
2. at the distinguished moving scale, whether the excursion enters a fixed neighborhood of the taboo point, for example `D(y+h_n,|h_n|/4)`, before returning.

The second statistic is not needed for the concentration proof, but it prevents the profile from treating `|h_n|` as an invisible `O(1)` correction. Exact taboo avoidance itself is already built into the conditioning `rho_{m-1}<K`.

Take

\[
m=\lceil c(\log n)^2\rceil,
\qquad
u_n=4\log\log n.
\tag{6.2}
\]

Since `J=O(log n)`, Theorem 5.1 gives

\[
P_y\bigl(\mathcal B(\nu_n)\mid\rho_{m-1}<K\bigr)
\ge1-O((\log n)^{-3}).
\tag{6.3}
\]

The previous exact Green elimination says

\[
1-p=\frac1{G_D^{\neg(y+h_n)}(y,y)}
=\frac1{\sigma_1\log n}(1+o(1)).
\tag{6.4}
\]

Therefore

\[
\begin{aligned}
\log p^{m-1}
&=(m-1)\log\left(1-\frac1{\sigma_1\log n}(1+o(1))\right)\\
&=-\frac{c}{\sigma_1}\log n+o(\log n),
\end{aligned}
\tag{6.5}
\]

because the quadratic correction contributes only `O(1)`. Hence

\[
\boxed{
P_y\bigl(\rho_{m-1}<K,\mathcal B(\nu_n)\bigr)
=n^{-c/\sigma_1+o(1)}.
}
\tag{6.6}
\]

This is the exact one-center milestone selected by stuck recovery 1: enforcing an `O(log n)`-dimensional multiscale screened profile, including a statistic at the moving taboo scale, costs **no power of `n`** beyond the already-known screened local-time exponent.

To reconnect (6.6) to the previous finite-volume candidate event `B_y`, use the already-derived entrance and terminal factors. For an interior candidate,

\[
P_0(T_y<T_{y+h_n}\wedge\tau_D)=\Theta((\log n)^{-1}),
\tag{6.7}
\]

and after the `m`th visit the probability to exit the inner disk before hitting `y+h_n` is bounded away from zero (indeed the predecessor calculation gives `beta/alpha+o(1)` in the normalized geometry). By strong Markov at the entrance to `y` and at the `m`th visit, adjoining those factors to the screened profile preserves the same power law:

\[
\boxed{
P(B_y^{\rm profile})=n^{-c/\sigma_1+o(1)}.
}
\tag{6.8}
\]

Thus the first moment of the successful-profile count has the same threshold `c_alpha` from (3.2). No matching lower bound or source closure is claimed: the remaining task is a **two-center** first-separation-scale correlation estimate for these profile events.

## 7. Section-B methods actually tried

### #4 — PROVE SOMETHING WEAKER, COMPLETELY

I did not try to prove the full matching lower bound. I isolated and completely proved the one-center theorem the previous recovery said had to precede any pair estimate: conditional on surviving `m-1` returns, the screened excursions are iid, and a finite multiscale profile has probability `1-o(1)`. The resulting source-valid one-center successful event retains exponent `c/sigma_1`.

**Outcome:** succeeded as a complete short theorem; it advances the route but does not move the frozen source metric.

### #8 — GO THE OTHER WAY AND DISCRETIZE

Instead of importing the continuous-looking successful-point barrier wholesale, I replaced it by a finite vector of `J=O(log n)` exact excursion indicators. The scale ladder can be chosen geometrically and contains a distinguished `|h_n|` scale. Conditional on high local time, this vector is a collection of binomial sums under an exact product excursion law.

**Outcome:** succeeded. The required barrier becomes an explicit finite concentration problem with a uniform `O((log n)^-3)` failure probability.

### #19 — MAKE IT AN ALGORITHM

The theorem gives a pathwise recognizer for a screened-successful candidate. Starting at the first hit of `y`, follow successive excursions until either the taboo/exit kill occurs or `m` visits have been accumulated. For every returned excursion update its `J` crossing/approach bits; at the `m`th visit accept only if all counts lie in their Bernstein tubes, then require the terminal exit-before-taboo event. The conditional means `theta_j` are exact finite killed-chain probabilities and can, in principle, be obtained from finite Dirichlet/hitting systems; no simulation is needed for the theorem.

**Outcome:** succeeded in exposing the next non-algorithmic step: for two candidates, the two recognizers share ancestor excursions before their first separating scale, so one-center iid factorization alone does not imply the required pair bound.

## 8. What remains and why this is not closure

The predecessor's macroscopic obstruction has narrowed. The one-center profile is no longer missing. What remains is to prove a pair inequality of the form

\[
\boxed{
P\bigl(y,z\text{ are screened-successful}\bigr)
\le C q_n^2 W(\ell(y,z)),
\qquad
\sum_{\text{shells}}W(\ell)<\infty,
}
\tag{8.1}
\]

where `ell(y,z)` is the first scale at which the two nested neighborhoods separate. The exact four-point Green calculation already shows strict power slack on every genuinely mesoscopic shell for `beta<beta_*`; the unresolved endpoint is the macroscopic/common-entrance normalization. The new theorem supplies the correct single-center truncated objects, but it does not yet control the shared excursion ancestry of two centers.

In particular, neither

\[
\liminf_{n\to\infty}P(Z_{\rm profile}>0)>0
\]

nor the desired singleton lower bound

\[
\liminf_{n\to\infty}\frac{M_{\{h_n\}}(n)}{(\log n)^2}
\ge\frac{4\beta(1-\beta)}\pi
\]

is claimed here.

No exact finite claim is made, so an exact-arithmetic checker would not test the theorem's missing pair mechanism and is not warranted. The theorem-sized claim is written in full above.

## 9. Status, counters, audits, and forced next-run protocol

The frozen metric still does not move:

```text
C_large: 1/pi -> 1/pi
unchanged_runs: 4 -> 5
stuck_recoveries: 1 -> 1
```

Status remains **PARTIAL / OPEN**. The successful-profile theorem is genuine route progress, but under the owner's metric rule it does not reset the unchanged counter because `C_large` did not move.

Required independent audits remain:

```text
P26: NOT PASSED / no E0086 PASS recovered
NM13-13: NOT PASSED / no E0086 PASS recovered
```

Because the frozen metric has now remained unchanged for five consecutive E0086 research runs, the **next NM13-12 invocation must be Section-I stuck recovery 2, thinking-only**. Its exact blocker should be (8.1): derive a first-separation-scale two-center estimate for the screened-profile events, including the common-entrance/macroscopic normalization. It must not simply add another one-center concentration lemma. Fresh methods reserved for that recovery are #13 FIND WHAT ONLY INCREASES, #18 SAY IT IN ANOTHER LANGUAGE, and #27 SWAP THE QUANTIFIERS; they are not counted as tried here.

This will be the second and final permitted HARD stuck-recovery episode on E0086. If a later invocation reaches a third stuck episode without genuine source movement, the owner rule requires a preserved handoff and rotation rather than a third recovery.

No shared root, existing canonical claim, peer namespace, workflow, permission, public surface, email/Drive item, paid-compute resource, artifact-only receipt, or schedule was modified.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: E0086
  claim_id: E0086
  canonical_dedup_key: favorite_sites::op_2
  status_before: PARTIAL
  status_after: PARTIAL
  frozen_metric:
    name: C_large
    scope: source large-radius regime a_n >= n^(1/2+epsilon)
    before: 1/pi
    after: 1/pi
    movement: false
  methods_actual:
    - 4   # PROVE SOMETHING WEAKER, COMPLETELY
    - 8   # GO THE OTHER WAY AND DISCRETIZE
    - 19  # MAKE IT AN ALGORITHM
  mathematical_progress:
    - exact conditional-iid factorization of returned excursions under taboo/exit screening
    - complete Bernstein-union barrier theorem for any finite vector of returned-excursion indicators
    - O(log n)-scale screened profile, including the moving taboo scale, has conditional failure O((log n)^-3)
    - proved screened-profile one-center probability retains n^(-c/sigma_1+o(1)) exponent
    - therefore successful-profile first moment retains the prior c_alpha threshold
  one_center_theorem:
    p: P_y(T_y^+ < T_b wedge tau_D)
    exact_survival: p^(m-1)
    barrier_failure_conditional: <= 2 J exp(-u)
    application_J: O(log n)
    application_u: 4 log log n
    application_failure: O((log n)^-3)
  remaining_blocker: >-
    First-separation-scale two-center correlation inequality for screened-profile
    events, retaining common entrance/macroscopic normalization; one-center iid
    regeneration does not control shared ancestor excursions of two candidates.
  unchanged_runs_before: 4
  unchanged_runs_after: 5
  stuck_recoveries_before: 1
  stuck_recoveries_after: 1
  next_run_protocol: SECTION_I_STUCK_RECOVERY_2_THINKING_ONLY
  next_methods_reserved_unspent: [13, 18, 27]
  audits:
    P26: NOT_PASSED
    NM13-13: NOT_PASSED
  literature_checked: 2026-09-18
  literature_result: >-
    Primary Okada source refreshed; Okada 2020 pair-favorite successful-point
    method remains nearest solved analogue; Hao-Li-Okada-Zheng 2025 ordinary
    favorite-site multiplicity and 2026 Okada range-fluctuation work do not
    resolve E0086; bounded search found no source-matching resolution; worldwide
    openness/novelty UNVERIFIED.
  artifacts_created: none
```