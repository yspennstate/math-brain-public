Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `C_large = 1/pi -> 1/pi`; Section-B methods actually tried: #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE FOR ALL WITH FOR TYPICAL. Status: PARTIAL.**

# NM13-12 — E0086 two-trap Green bound sharpens the whole source main regime

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0086` / `operations/claims/E0086.md`  
Canonical dedup key: `favorite_sites::op_2`  
Canonical SHA-256 / shard: `a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c`, residue `11 mod 13`

## 1. Runtime, controls, continuity, and required reads

The prompt requests `GPT-6 / maximum`. That is not the model this invocation can honestly report. The actual model is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning was bound at runtime.

The exposed task-control interface still has ordinary task prompt/title, timing/schedule and enabled-state fields but no bindable model-family selector and no bindable reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those fields together with authenticated per-run runtime attestation. `RESULTS.md` records that the historical P26 `You cannot modify this task` failure was authorization-context-specific and that a later P26 update succeeded from another authorized context. The lawful workaround for a denied task is therefore an owning/otherwise-authorized context or platform/admin support, not cloning a task or bypassing permissions. This invocation did not create, modify, disable, or duplicate a schedule and does not claim a support escalation.

Before mathematics I reread or targeted-search-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0086.md`;
- newest own report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T07-51-25Z__e0086-potential-kernel-hazard-upper-bound.md`;
- newest neighboring NM13-11 report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T08-24-00Z__e0082-ladder-composition-quotient.md`;
- newest visible NM13-13 report `proofnet24/NM13-13/runs/2026-09-18/2026-09-18T08-02-00Z__successor-admission-screen-3-h-i0059.md`;
- E0086 intake/source material, the old substantive attempt `E0086-A001`, current/historical ownership material, handoffs, claims, and audit searches.

Large aggregate JSONL and root ledgers can be connector-truncated when displayed wholesale. I therefore used the current root files, exact IDs/paths, canonical claim, predecessor continuity, targeted E0086 searches, and current neighboring reports rather than pretending a truncated rendering was a byte-for-byte reread of every historical row.

Pre-write `master` was observed at `16c0d116d2b55396f0c68bc7b39fec2711cff41d`. The mandatory P0483 handoff remains preserved and was not reopened. E0086 remains exclusively owned by NM13-12; no release, duplicate owner, POSTED settlement, source-specific retirement, P26 PASS, or NM13-13 PASS was recovered.

The preceding E0086 report proved a one-forbidden-point geometric hazard bound and the source-main-regime in-probability upper constant `4 beta / pi`, plus an entropy-sensitive almost-sure version. Its methods #1/#12/#24 are spent. The admission/source-correction run had already spent #2/#6/#30. The frozen metric remained `C_large=1/pi` and its counters were `unchanged_runs=1`, `stuck_recoveries=0`.

## 2. Exact source scope and frozen metric

The source remains Izumi Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787, Open Problem 2. For planar simple random walk

\[
R(n)=\{S_0,\ldots,S_n\},\qquad
K(n,x)=\sum_{i=0}^n {\bf1}_{\{S_i=x\}},
\]

and a finite displacement pattern `H`,

\[
\partial_HG=\{y\in G:y+H\subset G^c\},\qquad
M_H(n)=\max_{y\in\partial_HR(n)}K(n,y).
\]

The source's main moving-pattern regime is

\[
\widetilde D_n\subset D(0,n^\beta)^c\cap D(0,2n^\beta),
\qquad 0<\beta<\tfrac12. \tag{2.1}
\]

The frozen metric is unchanged and is deliberately not renamed to capture the theorem below:

\[
C_{\rm large}:=\lim_{n\to\infty}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\quad\text{under the separate source large-radius condition }a_n\ge n^{1/2+\varepsilon}.
\]

The previous source-correction run proved

\[
C_{\rm large}=\frac1\pi.
\]

This run instead sharpens the upper theorem in (2.1). That is substantive source progress but not frozen-metric movement.

## 3. Three fresh Section-B attacks and the idea before any code

No code was written in this run. The result is analytic and theorem-sized, so the proof is written on the page rather than manufacturing a checker for an unchanged metric.

### #20 — FIND WHY THE ALGORITHM FAILS

The previous one-point hazard bound killed the walk only when it hit the forbidden translate `y+h`. That deliberately forgot the finite time horizon. The exact failure is now clear: a candidate site must make many return excursions **before time n**, and on the typical diffusive event all of those excursions are also confined to a ball of radius `n^(1/2+o(1))`. Escaping that ball before returning is a second killing mechanism. Ignoring it loses a source-scale amount in the exponent.

### #11 — DUALIZE

Once both failure mechanisms are kept, the relevant object is not the one-point potential kernel `2 a(h)` but a killed Green function with two absorbing alternatives: the forbidden point `h` and the outer boundary. Eliminating the single interior trap from the disk Green matrix gives an exact Schur-complement identity. This converts the excursion problem into three standard disk Green asymptotics.

### #28 — REPLACE FOR ALL WITH FOR TYPICAL

The second trap is justified on the high-probability confinement event

\[
\max_{k\le n}|S_k|\le n^\alpha/4,
\qquad \alpha>\tfrac12.
\]

Its complement has stretched-exponential probability by a coordinate maximal inequality. On the confinement event, after the first visit to any candidate `y`, every later displacement from `y` lies inside a translated disk of radius `n^\alpha`, uniformly over the random choice of `y`. Thus a typical-path restriction produces a rigorous unconditional probability bound after adding the confinement error.

The key gain is that the disk boundary and the forbidden translate interact through the Green-function Schur complement rather than by an unjustified addition of hazards.

## 4. Exact two-trap Green identity

For `R>0`, let

\[
\tau_R=\inf\{k\ge0:S_k\notin D(0,R)\}
\]

and define the disk Green function

\[
G_R(x,z)=E_x\left[\sum_{k<\tau_R}{\bf1}_{\{S_k=z\}}\right].
\]

For `h\ne0` with `|h|<R`, let

\[
G_R^{\neg h}(0,0)
:=E_0\left[\sum_{k<\tau_R\wedge T_h}{\bf1}_{\{S_k=0\}}\right],
\qquad T_h=\inf\{k\ge0:S_k=h\}.
\]

### Lemma 4.1 — exact one-point elimination

\[
\boxed{
G_R^{\neg h}(0,0)
=G_R(0,0)-\frac{G_R(0,h)^2}{G_R(h,h)}.
} \tag{4.1}
\]

#### Proof

Split visits to `0` before `tau_R` according to whether they occur before or after the first hit of `h`. By the strong Markov property,

\[
G_R(0,0)=G_R^{\neg h}(0,0)
+P_0(T_h<\tau_R)G_R(h,0). \tag{4.2}
\]

Likewise every visit to `h` before exit must start with the first hit of `h`, hence

\[
G_R(0,h)=P_0(T_h<\tau_R)G_R(h,h). \tag{4.3}
\]

Simple random walk is reversible with counting measure, so `G_R(h,0)=G_R(0,h)`. Substituting (4.3) into (4.2) gives (4.1). `square`

The number of visits to `0`, including time zero, before `T_h\wedge\tau_R` is geometric. Therefore its one-excursion killing probability is exactly

\[
q_{R,h}
=P_0(T_h\wedge\tau_R<T_0^+)
=\frac1{G_R^{\neg h}(0,0)}. \tag{4.4}
\]

This is the finite-horizon correction missing from the previous one-trap bound.

## 5. Source-scale asymptotic of the two-trap Green function

Let

\[
R_n=n^\alpha,
\qquad \alpha>\frac12,
\]

and let `h_n` satisfy

\[
n^\beta<|h_n|\le2n^\beta,
\qquad 0<\beta<\frac12. \tag{5.1}
\]

Write `a(x)` for the standard planar simple-random-walk potential kernel,

\[
a(x)=\frac2\pi\log|x|+\frac{2\gamma+\log8}{\pi}+O(|x|^{-2}). \tag{5.2}
\]

The standard disk identity

\[
G_R(x,z)=E_x[a(S_{\tau_R}-z)]-a(x-z) \tag{5.3}
\]

and `|h_n|=o(R_n)` give, uniformly over (5.1),

\[
\begin{aligned}
G_{R_n}(0,0)
&=\frac{2\alpha}{\pi}\log n+O(1),\\
G_{R_n}(h_n,h_n)
&=\frac{2\alpha}{\pi}\log n+O(1),\\
G_{R_n}(0,h_n)
&=\frac{2(\alpha-\beta)}{\pi}\log n+O(1).
\end{aligned} \tag{5.4}
\]

Inserting (5.4) into (4.1) yields the exact leading constant

\[
\boxed{
G_{R_n}^{\neg h_n}(0,0)
=
\left[
\frac2\pi\left(2\beta-\frac{\beta^2}{\alpha}\right)+o(1)
\right]\log n.
} \tag{5.5}
\]

As `alpha downarrow 1/2`, the bracket tends to

\[
\boxed{
g(\beta):=\frac{4\beta(1-\beta)}\pi.} \tag{5.6}
\]

This is strictly smaller than both the previous `4 beta/pi` hazard constant and the unrestricted favorite-site constant `1/pi` for every `0<beta<1/2`.

## 6. New source-main-regime upper theorem

### Theorem 6.1 — finite-time two-trap tail

Fix `0<beta<1/2`, `alpha>1/2`, and deterministic `h_n` satisfying (5.1). Let `R_n=n^alpha`. Then for every integer `m>=1`,

\[
P(M_{\{h_n\}}(n)\ge m)
\le
P\left(\max_{k\le n}|S_k|>R_n/4\right)
+(n+1)\left(1-\frac1{G_{R_n}^{\neg h_n}(0,0)}\right)^{m-1}. \tag{6.1}
\]

#### Proof

On the confinement event

\[
\mathcal C_n=\{\max_{k\le n}|S_k|\le R_n/4\},
\]

let `y` witness `M_{\{h_n\}}(n)>=m` and let `sigma` be the first visit to `y`. Since both `y` and every later `S_k` lie in `D(0,R_n/4)`, every displacement `S_k-y` lies in `D(0,R_n/2)` and therefore certainly inside `D(0,R_n)`. Also `y+h_n` is unvisited through the `m`th visit to `y`. Thus, after time `sigma`, the translated walk makes at least `m-1` returns to `0` before either hitting `h_n` or exiting `D(0,R_n)`.

Conditional on `F_sigma`, the strong Markov property and (4.4) make this probability exactly

\[
\left(1-\frac1{G_{R_n}^{\neg h_n}(0,0)}\right)^{m-1}.
\]

Dropping the requirement that a candidate time be the first visit to its site and union-bounding over the at most `n+1` possible values of `sigma` gives the second term in (6.1). Adding `P(C_n^c)` gives the claim. `square`

A standard coordinate maximal inequality gives

\[
P(\mathcal C_n^c)\le 4\exp(-c n^{2\alpha-1}) \tag{6.2}
\]

for some absolute `c>0` and all large `n`.

### Corollary 6.2 — strict upper constant throughout `0<beta<1/2`

For every deterministic nonempty source-valid pattern sequence satisfying (2.1), and every `epsilon>0`,

\[
\boxed{
P\left(
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
>
\frac{4\beta(1-\beta)}\pi+\epsilon
\right)\longrightarrow0.
} \tag{6.3}
\]

#### Proof

Choose any deterministic witness `h_n in \widetilde D_n`. Since

\[
\partial_{\widetilde D_n}R(n)\subseteq\partial_{\{h_n\}}R(n),
\]

one has `M_{\widetilde D_n}(n)<=M_{\{h_n\}}(n)`. Fix `epsilon>0`, choose `alpha>1/2` sufficiently close to `1/2` that

\[
\frac2\pi\left(2\beta-\frac{\beta^2}{\alpha}\right)
<\frac{4\beta(1-\beta)}\pi+\frac\epsilon2,
\]

and put

\[
m_n=\left\lceil
\left(\frac{4\beta(1-\beta)}\pi+\epsilon\right)(\log n)^2
\right\rceil.
\]

By (5.5), (6.1), `1-x<=e^{-x}`, and (6.2), the confinement error tends to zero and the second term is

\[
n^{1-c_\epsilon+o(1)}\to0
\]

for some `c_epsilon>1`. This proves (6.3). `square`

The previous report's candidate upper phase boundary `beta=1/4` was therefore an artefact of discarding finite-time escape. The corrected two-trap constant is strictly below `1/pi` for **every** `0<beta<1/2` because

\[
4\beta(1-\beta)=1-(1-2\beta)^2<1. \tag{6.4}
\]

No matching lower bound is claimed.

## 7. Almost-sure entropy refinement

Keep a deterministic witness `h_n in \widetilde D_n`. For dyadic `N_j=2^j`, define

\[
W_j=\{h_n:N_j\le n<2N_j\},
\qquad
\rho=\limsup_{j\to\infty}\frac{\log|W_j|}{\log N_j}. \tag{7.1}
\]

As before, source geometry alone gives `0<=rho<=2 beta`.

### Theorem 7.1

Under (2.1),

\[
\boxed{
\limsup_{n\to\infty}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\le
\frac1\pi\min\{1,\,4\beta(1-\beta)(1+\rho)\}
\quad\text{a.s.}
} \tag{7.2}
\]

Consequently,

\[
\boxed{
\limsup_{n\to\infty}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\le
\frac1\pi\min\{1,\,4\beta(1-\beta)(1+2\beta)\}
\quad\text{a.s.}
} \tag{7.3}
\]

For block-frozen or subpolynomial-entropy witnesses (`rho=0`), the almost-sure upper constant is the same `4 beta(1-beta)/pi` as the in-probability bound and is strictly below `1/pi` throughout `0<beta<1/2`.

#### Proof

Fix `c>g(beta)(1+rho)`. On a dyadic block `[N,2N)`, if some source event `M_{\widetilde D_n}(n)>=c(log N)^2` occurs, then for `h=h_n in W_j` there is a first-visit time `k<=2N` from which at least that many visits to the candidate site occur before the first hit of its translate. On the confinement event up to time `2N`, Theorem 6.1's translated two-trap argument applies with one common radius `(2N)^alpha` and uniformly over all `h in W_j`.

Hence, for every `eta>0` and all large `j`,

\[
P\left(\sup_{N\le n<2N}M_{\widetilde D_n}(n)\ge c(\log N)^2\right)
\le
\exp(-N^{2\alpha-1+o(1)})
+N^{1+\rho+\eta-c/g_{\alpha,\beta}+o(1)}, \tag{7.4}
\]

where

\[
g_{\alpha,\beta}=\frac2\pi\left(2\beta-\frac{\beta^2}{\alpha}\right).
\]

Choose `alpha>1/2` close enough to `1/2` and then `eta>0` small enough that the exponent of `N` in (7.4) is negative. Since `N=2^j`, the right side is summable in `j`. Borel--Cantelli proves the `g(beta)(1+rho)` part of (7.2). The ordinary planar favorite-site law gives the independent `1/pi` bound. Finally `rho<=2beta` gives (7.3). `square`

The universal almost-sure improvement over the bare `1/pi` bound therefore extends from the previous threshold `beta<(sqrt(3)-1)/4 approx 0.1830` to the unique root in `(0,1/2)` of

\[
4\beta(1-\beta)(1+2\beta)=1,
\]

namely approximately

\[
\beta<0.222520934. \tag{7.5}
\]

## 8. What this does and does not settle

The full source problem remains **OPEN / PARTIAL**. The run proves a strictly stronger source-main-regime upper theorem than the previous report, but it does not determine the almost-sure asymptotic requested by Okada and does not prove a matching lower bound even for singleton `\widetilde D_n={h_n}`.

The two-trap computation suggests the new singleton candidate constant

\[
\boxed{\frac{4\beta(1-\beta)}\pi} \tag{8.1}
\]

rather than `4beta/pi`. This is a conjectural sharp value only. Proving a lower bound now requires showing that among roughly linear-many candidate first visits, enough translated two-trap excursion stacks survive with controlled dependence. The exact obstruction is no longer the one-site return probability; it is the second-moment/correlation structure across candidate sites.

The frozen large-radius metric does not move:

```text
C_large: 1/pi -> 1/pi
unchanged_runs: 1 -> 2
stuck_recoveries: 0 -> 0
```

This is the second consecutive unchanged frozen-metric run. Section I is not yet triggered. If the next run also leaves `C_large` unchanged, the track will have reached three consecutive unchanged runs; the following invocation must obey the required stuck-thinking protocol rather than filing another incremental lemma.

## 9. Literature/status refresh — 2026-09-18

Bounded dated searches included:

- exact source title and `Open Problem 2`, `favorite sites`, `moving boundary`, `translated boundary`, `M_{Dtilde_n}` and potential-kernel terms;
- Izumi Okada plus later-author/citing-paper searches;
- the later Hao--Li--Okada--Zheng paper *Favorite Sites for Simple Random Walk in Two and More Dimensions*, arXiv:2409.00995 / *Probability Theory and Related Fields* (accepted 2025), whose stated results concern simultaneous ordinary favorite sites in `d=2` and their number in higher dimensions, not this moving translated-boundary problem;
- Lawler--Limic, *Random Walk: A Modern Introduction*, Chapters 4 and 6, for the standard potential-kernel and killed-Green inputs; and current Green-kernel literature searches for the disk asymptotics.

The source page still presents Okada's 2016 article as proposing open problems for `d=2`. I did not locate a later source-matching resolution of Open Problem 2 or the constant (8.1). Search-engine coverage, citation indexing, and full-text access are incomplete. Therefore this is **bounded negative evidence only**; publication novelty is **UNVERIFIED**. The potential-kernel/Green-function mechanism itself is standard and is not claimed as new.

## 10. Audit state and next route

No closure is claimed. Required independent audits remain:

```text
P26: NOT PASSED / no E0086 PASS recovered
NM13-13: NOT PASSED / no E0086 PASS recovered
```

No audit request counts as movement, and none was manufactured merely because the upper theorem improved.

The next high-value obligation is a matching **lower bound for the singleton or block-frozen class** at the new candidate constant `4 beta(1-beta)/pi`. Fresh methods reserved for the next substantive run are:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** interpolate the two-trap Green kernel by trap radius/strength to expose covariance derivatives for candidate-site indicators;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** search whether `4 beta(1-beta)` is the known two-point thick-point / pinned-GFF exponent in another language and import only a theorem whose hypotheses match exactly;
- **#25 COUNT THE SAME THING TWICE:** define successful candidate first visits and attack the second moment by ordered-pair counting, separating near and far candidate centers.

No shared root, peer namespace, claim file, workflow, permission, public surface, email/Gmail, Drive resource, paid compute, or schedule was modified.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: E0086
  claim_id: E0086
  canonical_dedup_key: favorite_sites::op_2
  status: PARTIAL
  metric:
    name: C_large
    definition: lim M_Dtilde_n(n)/(log n)^2 under source large-radius a_n >= n^(1/2+epsilon)
    before: 1/pi
    after: 1/pi
    movement: false
  methods_this_run:
    - 11
    - 20
    - 28
  method_outcomes:
    11: exact disk Green one-point elimination gives the two-trap return hazard
    20: diagnosed the missing finite-time escape hazard in the prior one-trap bound
    28: high-probability diffusive confinement turns that hazard into an unconditional tail bound
  new_source_relevant_results:
    - G_R^{not h}(0,0)=G_R(0,0)-G_R(0,h)^2/G_R(h,h)
    - source-annulus two-trap Green constant g(beta)=4*beta*(1-beta)/pi after alpha down to 1/2
    - in-probability upper constant 4*beta*(1-beta)/pi for every 0<beta<1/2
    - almost-sure entropy upper constant min(1,4*beta*(1-beta)*(1+rho))/pi
    - universal almost-sure corollary min(1,4*beta*(1-beta)*(1+2*beta))/pi
  unchanged_runs_before: 1
  unchanged_runs_after: 2
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  audits:
    P26: NOT_PASSED
    NM13-13: NOT_PASSED
  exact_artifact: NONE_ANALYTIC_THEOREM_NO_FINITE_CORE
  literature_check_date: 2026-09-18
  literature_result: no source-matching later resolution found in bounded search; novelty UNVERIFIED
  next_target: matching lower bound for singleton/block-frozen h_n at candidate constant 4*beta*(1-beta)/pi
  next_methods:
    - 5
    - 17
    - 25
```
