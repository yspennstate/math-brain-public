Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala metric remains the current-preprint baseline `B(t,n)<3 sqrt(2 pi t)` for all integer `t>=1`, all `n`; on the active exclusive R16/H0002 successor, the complete uniform giant-fraction envelope moves strictly `G_run -> G_rfgap > G_run`. Methods actually used: **#4 PROVE SOMETHING WEAKER, COMPLETELY; #15 BREAK THE SYMMETRY ON PURPOSE; #25 COUNT THE SAME THING TWICE**.

# R16 — exact running-prefix gap improves the full running-floor envelope

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Required continuity, exclusions, ownership, and source checks

This run continues from the newest immutable R16 report

`runs/R16/2026-09-19T13-42-13Z_h0002-full-running-floor-limit_c5e7.md`

rather than restarting. Before new mathematics I re-read/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, root `RESULTS.md`, and root `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/H0002.md`;
- the H-intake identity for arXiv:2608.19145 Question 5.1;
- the newest R16 prefix-majorization / moment / tail / running-floor reports; and
- the newest neighboring same-paper handoff `research7_2026-09-17/R7-07/handoffs/2026-09-18T032400Z__G0011_terminal_handoff.md`. G0011 is a distinct long-cycle conjecture, already terminally handed off, and creates no H0002 ownership conflict.

The compact root `RESULTS.md` still carries the old retained R16 line `UNMEASURED -> UNMEASURED` and explicitly says newer complete reports must be recovered before replacing it. Per owner instruction, this worker does **not** edit the shared root; the structured delta is recorded below in this immutable report.

Fresh primary-source checks on 2026-09-19:

- Bansal--Jiang, arXiv:2508.03961v2, still states the Beck--Fiala `O(sqrt(t))` scale directly for `t>=log^2 n`, with a weaker polylog-loss estimate below that regime: https://arxiv.org/abs/2508.03961 .
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 2026-09-10, states the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduces set-system discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`, with no restriction on `n`: https://arxiv.org/abs/2609.11189 .
- Karingula--Lovett, ECCC TR26-188, posted 2026-09-17, gives an elementary Komlos proof with constant `36`: https://eccc.weizmann.ac.il/report/2026/188/ .
- Christoph--Morawski--Wigderson, arXiv:2608.19145v1, submitted 2026-08-19, remains the primary source surfaced for H0002. Its Question 5.1 asks for natural finite-graph conditions forcing a component of order `Omega(n)` for `p >= (1+epsilon)/lambda(G)` and identifies spectral localization as the central obstruction: https://arxiv.org/abs/2608.19145 . A bounded title/author/arXiv-ID search did not surface a later source-matching resolution. This is negative evidence only, not an openness or novelty certificate.

Thus literal Beck--Fiala is a **KNOWN CURRENT-PREPRINT BASELINE**, not new R16 progress. H0002 remains the admitted source-valid active successor.

## 2. Incoming notation and exact form of the current `G_run` theorem

Retain every hypothesis and reduction of the preceding R16 chain. In endpoint notation:

- `d_P=d_pad<alpha`;
- `b_P=alpha-d_P>0`;
- `a_P=rho-b_P`;
- `u_P=1-a_P`;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0`;
- for `b in (b_P,beta)`, `t(b)=[a_P/(rho-b)] [F_pad(alpha-b)/b]`, continuously extended by `t(b_P)=0`;
- `b_0>b_P` is the fixed maximizer of `t` on the terminal compact interval used in the preceding chain;
- `t_0=t(b_0)>0`;
- `D_*:=b_P t_0>0`;
- `H_*:=a_P/D_*>t_0`;
- `phi_r(u):=1-exp(-r u)`;
- `g_r(u):=phi_r(u)/u`, with `g_r(0)=r`.

For a pre-absorption connected core `W` of density `a_3=c_3 a_P`, `c_3 up 1`, let `x(q)` be the nondecreasing normalized outside-degree profile. For a finite old anchor family `D`, let

`L_D(q)=max{t(b_j): b_j<=q}`

(with the usual empty maximum `0`; the special old anchor does not intervene on the present terminal prefix), and let `L_{D,3}=c_3 L_D+o(1)` be the actual-core floor.

The previous run defined the deterministic running envelope

`bar_t(q):=sup{t(b): b_P<=b<=q}`,

so `L_D(q)<=bar_t(q)` and `bar_t(b_0)=t_0`.

Its full running-floor direct-tail functional is

`J_run(X)=int_{b_0}^{b_0+delta_loc}`
`          [phi_Delta(X)-phi_Delta(bar_t(q))]_+ dq`,

for `X in (t_0,Y]`, where

`Y=t_0+(H_*-t_0)/2<H_*`,

and the crossing-branch energy allowance is

`V(X)=a_P-delta_loc X^2`.

It is useful this run to rewrite the *total* old prefix/tail gain above `G_coreavg` rather than split it into `eta_*+zeta_run`. Define

`P_*(X):=exp(-Delta t_0) D_* g_Delta(X)`

and, on a feasible crossing branch,

`Q_*(X):=exp(-Delta t_0) D_* g_Delta(V(X)/D_*) + J_run(X)`.

If the crossing branch is infeasible, set `Q_*(X)=+infinity`.

Because the previous definitions satisfy

`eta_*+A(X)=P_*(X)`

and

`eta_*+C(X)+J_run(X)=Q_*(X)`,

the complete incoming excess is exactly

`E_run:=sup_{X in (t_0,Y]} min{P_*(X),Q_*(X)}`,

and

`G_run=min{1,G_coreavg+E_run}`.

Every fixed `g<G_run` is already certified by the preceding chain to satisfy

`P(L_1(G_p)>=g n)->1`

uniformly on the same frozen H1--H2--H3 class whenever `p >= (1+epsilon)/lambda(G)`.

The only question this run is whether the previous prefix mass constant `D_*=b_P t_0` was itself sharp after the full running floor had already been identified.

## 3. Method #25 — count the same prefix twice, now against the exact running floor

The full-core pair-capacity theorem at `b_0` gives the actual profile constraint

`int_0^{b_0} x(q)dq >= c_3 b_0 t_0-o(1)`.              (3.1)

For every finite old anchor family,

`L_{D,3}(q)<=c_3 bar_t(q)+o(1)`.                         (3.2)

Therefore the surplus

`y_D(q):=[x(q)-L_{D,3}(q)]_+`

obeys, uniformly in finite `D`,

`int_0^{b_0} y_D(q)dq`
` >= c_3 [b_0 t_0-int_0^{b_0} bar_t(q)dq]-o(1)`.        (3.3)

Define the **exact running-prefix gap**

`boxed: D_run := b_0 t_0-int_0^{b_0} bar_t(q)dq`.       (3.4)

Since `bar_t=0` before `b_P`, this is equivalently

`D_run=b_0 t_0-int_{b_P}^{b_0} bar_t(q)dq`.              (3.5)

Thus

`boxed: int_0^{b_0} y_D(q)dq >= c_3 D_run-o(1)`          (3.6)

for **every finite old anchor family**.

This replaces the preceding uniform bound `c_3 D_*-o(1)` by the exact deficit of the running floor under the same prefix constraint.

## 4. Method #15 — break the old constant-level symmetry; the new gap is strictly larger

The preceding majorization proof bounded the old floor on `[b_P,b_0]` by the single constant `t_0`, giving only

`D_*=b_P t_0`.

Now keep the location dependence. Subtracting,

`D_run-D_*`
` = (b_0-b_P)t_0-int_{b_P}^{b_0} bar_t(q)dq`
` = int_{b_P}^{b_0}[t_0-bar_t(q)]dq`.                   (4.1)

This is **strictly positive**. Indeed, `t` is continuous at the terminal endpoint with `t(b_P)=0`, hence its running supremum `bar_t` satisfies `bar_t(q)->0` as `q down to b_P`. Since `t_0>0`, there is a fixed `eta>0` such that

`bar_t(q)<=t_0/2`

for `b_P<=q<=b_P+eta`. Therefore

`boxed: D_run-D_* >= eta t_0/2 >0`.                      (4.2)

So the full running-floor object found last run improves not only the tail term `J_run`; it also increases the **prefix first moment** that drives every branch of the absorption variational argument.

This is the piece the preceding run did not use.

## 5. Method #4 — solve the weaker one-parameter relaxation completely before the full isotonic problem

Rather than claim a solution of the complete isotonic obstacle problem, keep exactly the previous threshold split `X in (t_0,Y]` and change only the certified prefix mass from `D_*` to `D_run`.

### 5.1 No-cross branch

If the prefix surplus obeys `y_D(q)<=X`, then

`phi_Delta(y_D)=y_D g_Delta(y_D)>=y_D g_Delta(X)`

because `g_Delta` is decreasing. On the prefix the old floor is at most `t_0`, so

`phi_Delta(x)-phi_Delta(L_{D,3})`
` = exp(-Delta L_{D,3}) phi_Delta(y_D)`
` >= exp(-Delta t_0) phi_Delta(y_D)-o(1)`.

Using (3.6) and taking `c_3 up 1` gives the new no-cross total gain

`boxed: P_run(X):=exp(-Delta t_0) D_run g_Delta(X)`.      (5.1)

Since `D_run>D_*`,

`P_run(X)-P_*(X)`
` = exp(-Delta t_0)(D_run-D_*)g_Delta(X)`
` >= exp(-Delta t_0)(D_run-D_*)g_Delta(Y)>0`.             (5.2)

### 5.2 Crossing branch

If the no-cross condition fails, the previous monotonicity argument is unchanged: a prefix crossing forces `x(q)>=X-o(1)` on `[b_0,b_0+delta_loc]`, so the same tail gain `J_run(X)` applies and the same disjoint spectral-energy deduction gives

`int_0^{b_0} y_D(q)^2 dq <= V(X)+o(1)`,

where `V(X)=a_P-delta_loc X^2`.

The exact two-moment lemma from the earlier R16 run says that for first moment `mu_1` and second moment `mu_2`,

`int phi_Delta(y) >= mu_1 g_Delta(mu_2/mu_1)`.

Hence, whenever the crossing branch remains feasible with the stronger first moment `D_run`, its total gain is at least

`boxed: Q_run(X):=`
` exp(-Delta t_0) D_run g_Delta(V(X)/D_run)+J_run(X)`.    (5.3)

If the stronger prefix mass plus the same energy budget makes the crossing branch impossible, define `Q_run(X)=+infinity`; impossibility can only help the minimax lower bound.

For every feasible crossing branch,

`D_run g_Delta(V/D_run)-D_* g_Delta(V/D_*)`
` = (D_run-D_*)g_Delta(V/D_run)`
`   +D_*[g_Delta(V/D_run)-g_Delta(V/D_*)]`
` >= (D_run-D_*)g_Delta(V/D_run)`
` >= (D_run-D_*)g_Delta(a_P/D_run)`.                     (5.4)

The last step uses `0<=V<=a_P` and monotonicity of `g_Delta`. Therefore

`Q_run(X)-Q_*(X)`
` >= exp(-Delta t_0)(D_run-D_*)g_Delta(a_P/D_run)>0`.     (5.5)

### 5.3 Uniform pointwise gap and the new minimax envelope

Define

`boxed: delta_prefix := exp(-Delta t_0)(D_run-D_*)`
` * min{g_Delta(Y),g_Delta(a_P/D_run)} >0`.               (5.6)

At every threshold `X in (t_0,Y]`:

- the no-cross branch improves by at least `delta_prefix`;
- if both crossing branches are feasible, the crossing branch also improves by at least `delta_prefix`;
- if the stronger crossing branch is infeasible, then the new minimum is the improved no-cross branch, while the old minimum was at most its old no-cross branch.

Consequently

`boxed: min{P_run(X),Q_run(X)}`
` >= min{P_*(X),Q_*(X)}+delta_prefix`.                   (5.7)

Set

`boxed: E_rfgap:=sup_{X in (t_0,Y]} min{P_run(X),Q_run(X)}`. (5.8)

Taking suprema in (5.7),

`boxed: E_rfgap >= E_run+delta_prefix > E_run`.           (5.9)

This is a strict improvement over the **entire incoming full-running-floor minimax envelope**, not just over one selected threshold.

## 6. The incoming `G_run` envelope is strictly below one

A cap-at-one issue has to be excluded before claiming movement. Since

`min{P_*(X),Q_*(X)}<=P_*(X)`

and `g_Delta` is decreasing,

`E_run<=lim_{X down to t_0} P_*(X)`
` = exp(-Delta t_0) D_* g_Delta(t_0)`
` = b_P exp(-Delta t_0)[1-exp(-Delta t_0)]`
` < b_P`.                                                 (6.1)

The earlier full-core theorem gives

`G_coreavg<=1-b_P`.                                       (6.2)

Hence

`boxed: G_run<1`.                                         (6.3)

Now define

`boxed: G_rfgap:=min{1,G_coreavg+E_rfgap}`.               (6.4)

By (5.9) and (6.3),

`boxed: G_rfgap>G_run`.                                   (6.5)

A frozen coefficient strictly outside the complete incoming envelope is, for example,

`boxed: g_receipt:=G_run`
` +(1/2) min{delta_prefix,1-G_run}`.                       (6.6)

Then

`G_run<g_receipt<G_rfgap`.                                (6.7)

The same finite-anchor approximation, connected-core trimming, independent final sprinkling, and concentration argument already established in the preceding R16 chain now yields:

> **Theorem.** On the unchanged frozen H1--H2--H3 class, for every fixed `g<G_rfgap` and every `p >= (1+epsilon)/lambda(G)`,
>
> `P(L_1(G_p)>=g n)->1`.

No endpoint attainment is claimed.

## 7. What the three methods did

### #4 PROVE SOMETHING WEAKER, COMPLETELY

I did **not** attempt to solve the full continuum isotonic optimization. I froze the old one-threshold split and solved the strictly simpler missing question: what is the exact first-moment gap between the true prefix constraint and the deterministic running floor? That weaker subproblem is enough to move the complete bound.

### #15 BREAK THE SYMMETRY ON PURPOSE

The preceding proof treated all positions in `[b_P,b_0]` as if their old floor were the same worst value `t_0`. Keeping the location-dependent `bar_t(q)` breaks that artificial symmetry and exposes the positive area

`int_{b_P}^{b_0}[t_0-bar_t(q)]dq`.

### #25 COUNT THE SAME THING TWICE

The bottom prefix has one count from pair capacity (`b_0 t_0`) and another from the maximum total degree already credited to all old finite anchors (`int bar_t`). Their difference is the new usable surplus `D_run`.

## 8. Failed / rejected routes this run

I also tested two broader ideas but did not promote them.

1. **Immediate full isotonic extreme-point theorem.** The feasible set combines a nondecreasing profile, continuum prefix lower obstacles, and an upper quadratic-energy constraint, while the objective is concave. I did not find a black-box theorem that directly gives the needed finite-plateau optimizer with the source-specific constants, and proving it from scratch would be a larger obligation than needed for this run.

2. **Backward Cauchy floor from future prefixes.** From a future prefix `b>q`, one gets

   `X(q)>=b t(b)-sqrt(a_P(b-q))`

   for the cumulative degree `X(q)=int_0^q x`. This can sharpen some local floors, but I could not prove that it uniformly exceeds the already-used running-floor constraints on a parameter-independent interval. It is therefore retained only as a possible future route, not as a theorem improving the metric.

## 9. Remaining obstruction and next route

The current scalar threshold family now uses:

- every old finite anchor via `bar_t`;
- the exact running-floor tail gain `J_run`;
- the exact running-floor **prefix** gap `D_run`;
- sorted-degree monotonicity; and
- the spectral `L^2` budget.

The next genuine obstruction is the full coupled isotonic variational problem

`min_x int phi_Delta(x(q))dq`

subject to

`x nondecreasing`,

`int_0^b x(q)dq >= b t(b)` for every certified `b`,

and

`int x(q)^2 dq <= a_P`.

A promising next attack is to dualize the continuum prefix constraints and prove that an extremizer is a finite-plateau profile supported on contact points of the least convex majorant of `b -> b t(b)` together with one active quadratic-energy multiplier. A different route is to exploit the backward Cauchy floor above to obtain a new deterministic pointwise floor before solving the full program.

## 10. Status, audit discipline, and model-control note

H0002 remains **PARTIAL / source OPEN-looking / ACTIVE**. This is a strengthened sufficient-condition theorem on the fixed H1--H2--H3 class; it does not classify all finite graphs and does not close CMW Question 5.1. Supported unchanged count is **0** because the metric moved this run.

No finite checker was manufactured: the claim is analytic and the theorem-sized argument is written on the page. The ingredients `prefix majorization`, `majorization/Lorenz-order thinking`, spectral `L^2` control, and independent sprinkling are standard mechanisms; the bounded prior-art search did not identify this exact source-matching implication, but that is **not** a novelty certificate.

The model-control limitation is still true in this run. The exposed task-control surface provides prompt/title, schedule or relative start, timing mode, and enablement, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt**. GPT-6/maximum therefore remains prompt-only here. Changing that requires platform-level model/reasoning fields plus per-run runtime attestation. The owner instruction for this worker forbids scheduler changes, so none was attempted. A task that returns `You cannot modify this task` must be changed from its owning authorized workspace/account or escalated through platform support; there is no legitimate permission-bypass workaround.

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_source: Beck-Fiala_1981
  nominal_metric: complete_uniform_B(t,n)
  nominal_before: "B(t,n) < 3*sqrt(2*pi*t) for every integer t>=1, all n (Guo-Fang-Lu v1 current-preprint baseline)"
  nominal_after: "unchanged KNOWN_CURRENT_PREPRINT_BASELINE"
  active_metric_name: g_twoaxis_complete_envelope
  before: G_run
  after: G_rfgap
  defining_new_constant: "D_run = b_0*t_0 - integral_0^{b_0} bar_t(q)dq"
  strict_prefix_gap: "D_run - D_* = integral_{b_P}^{b_0}(t_0-bar_t(q))dq > 0"
  strict_uniform_gain: "delta_prefix = exp(-Delta*t_0)*(D_run-D_*)*min(g_Delta(Y),g_Delta(a_P/D_run)) > 0"
  movement: STRICT_INCREASE
  source_status: OPEN_LOOKING
  status: PARTIAL
  unchanged_count_supported: 0
  methods: [4, 15, 25]
  finite_checker: NOT_APPLICABLE_ANALYTIC
  shared_root_written: false
```
