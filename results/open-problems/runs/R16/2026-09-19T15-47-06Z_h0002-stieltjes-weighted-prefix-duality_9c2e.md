Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala metric remains the current-preprint baseline `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`; on the active exclusive R16/H0002 successor, the complete uniform bound strengthens from `G_rfgap` to `G_wdual:=min{1,G_coreavg+E_rfgap+delta_w}`, with an explicit `delta_w>0`, hence strict improvement on every nonsaturated frozen parameter triple (`G_rfgap<1`), while triples already at `G_rfgap=1` are at the absolute giant-fraction ceiling. Methods actually used: **#2 ATTACK THE NEGATION FIRST, #11 DUALIZE, #13 FIND WHAT ONLY INCREASES**.

# R16 — Stieltjes-weighted prefix duality recovers the variable absorption factor

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, source status, exclusions, and ownership

This run continues from the newest immutable R16 report

`runs/R16/2026-09-19T14-47-00Z_h0002-exact-running-prefix-gap_f3a7.md`

at commit `5cd6d36dcdf075b95e33ebed126d5027731b5620`. It does not restart the chain.

Before new mathematics I re-read/reconciled `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H0002 intake row, the newest R16 report, and the newest neighboring same-paper G0011 handoff. G0011 is a distinct long-cycle conjecture and is terminally handed off; it creates no H0002 ownership conflict.

Fresh primary-source checks on 2026-09-19:

- Bansal--Jiang, arXiv:2508.03961v2, still states `O(sqrt(t))` directly only for `t>=log^2 n`, with a weaker polylog-loss estimate below that range: https://arxiv.org/abs/2508.03961 .
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 2026-09-10, states the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduces discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`, with no restriction on `n`: https://arxiv.org/abs/2609.11189 .
- Karingula--Lovett, ECCC TR26-188, posted 2026-09-17, gives an elementary Komlos proof with constant `36`: https://eccc.weizmann.ac.il/report/2026/188/ .
- Christoph--Morawski--Wigderson, arXiv:2608.19145v1 (2026-08-19), remains the primary H0002 source: https://arxiv.org/abs/2608.19145 . A bounded current title/author/arXiv-ID search again surfaced that v1 and no later source-matching resolution of Question 5.1. This is negative evidence only, not a proof of worldwide openness or novelty.

Thus literal Beck--Fiala is a **KNOWN CURRENT-PREPRINT BASELINE**, not new R16 progress. H0002 remains the admitted source-valid successor. The source asks for natural conditions forcing an `Omega(n)` component at `p>=(1+epsilon)/lambda(G)`; the R16 frozen H1--H2--H3 theorem is a PARTIAL sufficient-condition answer, not a classification.

A bounded prior-art search for combinations of `percolation / degree majorization / Stieltjes / prefix constraints / spectral radius / giant component` returned fixed-degree-sequence percolation and generic weighted-majorization literature, but not the source-matching deterministic prefix/Stieltjes absorption statement below. Stieltjes integration by parts, running maxima, majorization, spectral `L^2` control, and sprinkling are standard tools; the search failure is not a novelty certificate.

## 2. Incoming endpoint notation

Retain every hypothesis and reduction of the preceding R16 chain. In the endpoint notation of the newest report:

- `d_P=d_pad<alpha`, `b_P=alpha-d_P>0`, `a_P=rho-b_P`;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0`;
- `t(b)=[a_P/(rho-b)] [F_pad(alpha-b)/b]` for `b>b_P`, continuously extended by `t(b_P)=0`;
- `b_0>b_P` is the fixed terminal maximizer, `t_0=t(b_0)>0`;
- `bar_t(q):=sup_{b_P<=b<=q} t(b)`, with `bar_t(q)=0` for `q<b_P` and `bar_t(b_0)=t_0`;
- `phi_r(u)=1-exp(-r u)` and `g_r(u)=phi_r(u)/u`, with `g_r(0)=r`.

For a pre-absorption connected core `W`, let `x(q)` be the nondecreasing normalized outside-degree profile. For a finite old anchor family `D`, let `L_D(q)` be its degree floor. At the endpoint,

`0<=L_D(q)<=bar_t(q)`.

The full family of prefix inequalities established earlier is

`int_0^b x(q)dq >= b t(b)`                                             (2.1)

for every certified `b` in the terminal interval, after taking the connected-core endpoint limit. The spectral-energy inequality is

`int x(q)^2 dq <= a_P`.                                                (2.2)

The newest report already used the exact running-prefix first moment

`D_run=b_0 t_0-int_0^{b_0} bar_t(q)dq > D_*=b_P t_0`,

but then replaced the absorption multiplier `exp(-Delta L_D(q))` by the single worst constant `exp(-Delta t_0)`. This run keeps the variable multiplier.

Write the incoming total excess above `G_coreavg` as

`E_rfgap=sup_{X in (t_0,Y]} min{P_run(X),Q_run(X)}`,

with `P_run,Q_run` exactly as in the preceding immutable report, and

`G_rfgap=min{1,G_coreavg+E_rfgap}`.

## 3. Method #2 — attack the negation: can all new weighted gain hide where the weight vanishes?

The obvious attempted obstruction is to put every unit of prefix surplus arbitrarily near `q=b_0`, where the extra variable weight

`v(q):=exp(-Delta bar_t(q))-exp(-Delta t_0)`

vanishes. If this were possible, retaining the true multiplier would give no uniform improvement over the constant-weight bound.

The nested prefix inequalities (2.1) rule this out. The reason is not a pointwise floor: it is that the running maximum can increase only at record/contact points of `t`, and at precisely those points the corresponding prefix integral is forced to be large. This leads to a positive Stieltjes dual mass below.

So the negation route fails for a structural reason: surplus cannot be moved entirely into the zero-weight endpoint while preserving all record-prefix constraints.

## 4. Method #13 — the monotone object is the running maximum

Set

`w(q):=exp(-Delta bar_t(q))`,
`w_0:=exp(-Delta t_0)`,
`v(q):=w(q)-w_0>=0` on `[0,b_0]`.

Then `v` is continuous and nonincreasing, with `v(b_0)=0`. Let

`mu:=-dv`

be its positive Stieltjes measure. Because `bar_t` is the running maximum of the continuous function `t`, the Stieltjes measure `d bar_t` (and hence `mu`) is supported on the record/contact set

`t(q)=bar_t(q)`.                                                       (4.1)

Indeed, on any open interval on which `t<bar_t`, the previous record remains strictly above `t` and the running maximum is locally constant.

The chain rule for continuous bounded-variation functions gives

`d mu = Delta exp(-Delta bar_t) d bar_t`.                              (4.2)

## 5. Method #11 — Stieltjes dualization gives a uniform positive weighted first moment

Let

`y(q):=[x(q)-L_D(q)]_+`.

Since `y>=x-L_D` and `L_D<=bar_t`,

`int_0^{b_0} v(q)y(q)dq`
` >= int_0^{b_0} v(q)x(q)dq-int_0^{b_0}v(q)bar_t(q)dq`.                (5.1)

Define `X(s)=int_0^s x(q)dq`. Stieltjes integration by parts, using `v(b_0)=0` and `X(0)=0`, yields

`int_0^{b_0} v(q)x(q)dq = int_{(0,b_0]} X(s) mu(ds)`.                  (5.2)

On the support of `mu`, (4.1) and the full prefix constraint (2.1) give

`X(s)>=s t(s)=s bar_t(s)`.                                             (5.3)

Therefore

`int v x >= int s bar_t(s) mu(ds)`.                                   (5.4)

Also, because `v(q)=mu((q,b_0])`, Tonelli gives

`int_0^{b_0}v(q)bar_t(q)dq`
` = int_{(0,b_0]} [int_0^s bar_t(q)dq] mu(ds)`.                        (5.5)

Combining (5.1)--(5.5),

`int_0^{b_0}v(q)y(q)dq >= Theta`,                                     (5.6)

where

`Theta:=int_{(0,b_0]} [s bar_t(s)-int_0^s bar_t(q)dq] mu(ds)`.         (5.7)

Because `bar_t=0` before `b_P` and is nondecreasing,

`s bar_t(s)-int_0^s bar_t(q)dq >= b_P bar_t(s)`.

Hence the completely explicit lower bound

`Theta >= Theta_*`,                                                    (5.8)

with

`boxed: Theta_* := b_P int_0^{t_0} u Delta exp(-Delta u) du`
` = (b_P/Delta)[1-(1+Delta t_0)exp(-Delta t_0)] >0`.                  (5.9)

Strict positivity is just `e^z>1+z` for `z=Delta t_0>0`.

### Simultaneity / continuum point

No uncountable probabilistic intersection is required. For any desired error, approximate the Stieltjes integral in (5.7) by a finite partition of continuity points of `bar_t`; use only those finitely many prefix constraints, which hold simultaneously by the already-established deterministic pair-capacity inequalities/finite union step, and then refine the partition after taking the host-size limit. Thus (5.8) is a legitimate endpoint limit of finite certified inequalities.

## 6. Convert weighted first moment to absorption probability

The second moment under the same weight satisfies

`int_0^{b_0} v(q)y(q)^2 dq`
` <= (1-w_0) int x(q)^2 dq`
` <= M_*`,                                                            (6.1)

where

`boxed: M_*:=(1-exp(-Delta t_0)) a_P`.                                (6.2)

Apply the exact two-moment lemma from the earlier R16 run, now to the measure `v(q)dq`: for any nonnegative `y`, if `A=int v y` and `B=int v y^2`, then

`int v phi_Delta(y) >= A g_Delta(B/A)`.                               (6.3)

Since `B<=M_*` and `A>=Theta_*`, monotonicity gives

`boxed: int_0^{b_0}v(q)phi_Delta(y(q))dq >= eta_*`,                   (6.4)

where

`boxed: eta_*:=Theta_* g_Delta(M_*/Theta_*) >0`.                       (6.5)

For completeness: `g_Delta` is decreasing, and for fixed `M>0` the function

`H(A):=A g_Delta(M/A)`

is increasing because, with `z=M/A`,

`H'(A)=g_Delta(z)-z g_Delta'(z)`
`     =int_0^Delta (1+s z) exp(-s z) ds >0`.                           (6.6)

## 7. This is genuinely additive to the incoming branch bounds

For every `q<=b_0`,

`phi_Delta(x)-phi_Delta(L_D)`
` = exp(-Delta L_D) phi_Delta(y)`
` >= [w_0+v(q)] phi_Delta(y)`.                                        (7.1)

The preceding `P_run/Q_run` analysis used only the constant part `w_0 phi_Delta(y)`. Equation (6.4) supplies an additional **uniform** `eta_*` from the variable part. It does not overlap the old direct-tail term `J_run`, which lives on the interval after `b_0`.

Thus every no-cross and every feasible crossing branch receives the same positive endpoint correction `eta_*`; an infeasible crossing branch is still assigned `+infinity` and only helps the minimax lower bound.

## 8. Finite-core and finite-sprinkling stability

The actual argument reaches the endpoint through a connected core of density `a_3=c_3 a_P`, `c_3<1`, and a final independent sprinkling numerator `r<Delta`. The same proof works before the limit with

`v_{c,r}(q)=exp(-r c_3 bar_t(q))-exp(-r c_3 t_0)`,

and gives

`Theta(c_3,r)`
` = c_3 b_P int_0^{t_0} u (r c_3) exp(-r c_3 u)du >0`,                (8.1)

while

`M(c_3,r) <= [1-exp(-r c_3 t_0)] a_3`.                               (8.2)

The resulting two-moment correction `eta(c_3,r)>0` converges to `eta_*` as `c_3 up 1` and `r up Delta`.

Choose `c_3,r` sufficiently close to their endpoints and choose the finite Stieltjes partition sufficiently fine that the new correction is at least `eta_*/2`; then make all previously existing finite-anchor, core-trimming, and concentration approximation losses smaller than `eta_*/4`. A conservative frozen net increment is therefore

`boxed: delta_w:=eta_*/4 >0`.                                         (8.3)

No new independence assumption is introduced: the final attachment events use the same independent reserved sprinkling edges as in the preceding chain.

## 9. New complete envelope and the cap-at-one qualification

Define the strengthened endpoint excess

`boxed: E_wdual:=E_rfgap+delta_w`,                                    (9.1)

and the new complete bound

`boxed: G_wdual:=min{1,G_coreavg+E_wdual}`.                           (9.2)

Then

`boxed: G_wdual>=G_rfgap`                                             (9.3)

for every frozen parameter triple, and whenever the incoming theorem is not already saturated,

`G_rfgap<1  ==>  boxed: G_wdual>G_rfgap`.                             (9.4)

This cap qualification is necessary. The preceding immutable report proved `G_run<1` before moving to `G_rfgap`, but did not prove `G_rfgap<1` for every symbolic parameter triple. If `G_rfgap=1`, the certified giant-fraction lower bound has already reached the absolute ceiling and no theorem can move that numerical metric above one. I therefore do **not** claim strict movement on already-saturated triples.

For every nonsaturated triple a concrete coefficient outside the entire incoming complete envelope is

`boxed: g_receipt:=G_rfgap+(1/2)min{delta_w,1-G_rfgap}`,               (9.5)

so

`G_rfgap<g_receipt<G_wdual`.                                          (9.6)

Consequently, on the same frozen H1--H2--H3 graph class, for every fixed `g<G_wdual`, the already-established harvesting/gluing/sprinkling argument plus the new weighted correction yields

`P(L_1(G_p)>=g n) -> 1`

whenever

`p >= (1+epsilon)/lambda(G)`.                                         (9.7)

No endpoint attainment is claimed.

## 10. What the three methods did

- **#2 ATTACK THE NEGATION FIRST:** tried to kill the variable-weight gain by concentrating all prefix surplus at `q=b_0`, where the extra weight is zero. The full nested prefix constraints make this impossible; the Stieltjes record measure detects a fixed positive amount before the endpoint.
- **#11 DUALIZE:** converted the continuum of prefix constraints into the Stieltjes identity (5.7), using integration by parts against the measure generated by the running floor.
- **#13 FIND WHAT ONLY INCREASES:** `bar_t`, the running maximum of the anchor threshold profile, is the correct monovariant. Its measure increases only at contact/record points where the exact prefix lower bound is available.

The immediately preceding method triple was #4/#15/#25, so this is not a consecutive repeat.

## 11. Remaining obstruction

This run harvests the variable exponential multiplier that every preceding one-threshold proof replaced by its worst constant. It still does **not** solve the full isotonic obstacle problem. The remaining exact optimization is to minimize

`int phi_Delta(x(q))dq`

subject simultaneously to

- `x` nondecreasing;
- every prefix obstacle `int_0^b x >= b t(b)`;
- the spectral budget `int x^2<=a_P`;
- and the exact old finite-anchor baseline.

The next genuinely different route should characterize extreme points of this obstacle set (finite-plateau/isotonic KKT structure) or produce a finite obstruction to such a characterization. Another scalar floor refinement would mostly repackage information already present in `bar_t`.

## 12. Closure, checker, and lifecycle

H0002 remains **PARTIAL / source OPEN-looking / ACTIVE**. This is a stronger theorem on the frozen sufficient-condition class, not a solution of the open-ended source Question 5.1. No finite checker was manufactured because the new claim is analytic; the theorem-sized argument is written on the page. No shared-root file is edited by this worker.

Supported unchanged count remains `0` on the active mathematical bound: the complete bound function is strictly strengthened on every nonsaturated parameter triple, and its uncapped excess improves by the explicit positive `delta_w` on all triples. The hard two-recovery stuck protocol is therefore not triggered this run.

## 13. Model / scheduler control status

The currently exposed task-control surface still has fields for prompt/title, schedule/start, timing mode, and enablement, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt**. Thus `GPT-6 / maximum` remains prompt-only; this run actually reports GPT-5.6 Sol with reasoning level UNVERIFIED.

The root ledger records that P26's historical `You cannot modify this task` failure was authorization-context-specific and that a later P26 update succeeded from an authorized context. If a task still rejects modification, the compliant route remains the owning authorized workspace/account or platform support; there is no permission-bypass or duplicate-task workaround. Per the current owner instruction, this R16 run made **no scheduler changes**.

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_beck_fiala_status: KNOWN_CURRENT_PREPRINT_BASELINE
  nominal_beck_fiala_bound: "B(t,n) < 3*sqrt(2*pi*t), every integer t>=1, all n (Guo-Fang-Lu v1, 2026-09-10)"
  metric_name: g_twoaxis_complete_envelope
  before: G_rfgap
  after: G_wdual
  movement: "pointwise >= everywhere; strict whenever G_rfgap<1; uncapped excess +delta_w everywhere"
  delta_w: "(1/4)*Theta_* g_Delta(M_*/Theta_*) > 0"
  status: PARTIAL
  source_status: OPEN-looking
  supported_unchanged_count: 0
  methods: [2, 11, 13]
  checker: none_analytic_theorem
  shared_root_write: false
  scheduler_change: false
```
