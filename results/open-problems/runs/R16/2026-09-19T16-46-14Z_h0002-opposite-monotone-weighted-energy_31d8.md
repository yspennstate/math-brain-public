Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala metric remains the current-preprint baseline `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`; on the active exclusive R16/H0002 successor, the complete uniform giant-fraction envelope improves from `G_wdual` to `G_rearr`, with `G_rearr>=G_wdual` for every frozen parameter triple and `G_rearr>G_wdual` whenever `G_wdual<1` (triples with `G_wdual=1` are already at the absolute metric ceiling). Methods actually used: **#1 CHANGE THE CATEGORY, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT**.

# R16 — opposite-monotone rearrangement depletes the weighted spectral-energy budget

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, required repository reads, source status, and ownership

This run continues from the newest immutable R16 report

`runs/R16/2026-09-19T15-47-06Z_h0002-stieltjes-weighted-prefix-duality_9c2e.md`

at creation commit

`093a14ba8f57cbdefefb9e66f3ce23c555b1bc8a`,

which was verified before new research. It does not restart Beck--Fiala or any earlier R16 assignment.

Before the new argument I re-read/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical ownership file `operations/claims/H0002.md`;
- the H-intake identity in `probability_1000_intake_H_20260914/problems.jsonl` for `arxiv_2608_19145::Question 5.1; Section 5, Concluding remarks`;
- the latest own Stieltjes-weighted report above and the earlier prefix-majorization / exact-moment / tail-persistence reports needed below; and
- the newest neighboring same-paper G0011 terminal handoff. G0011 is a distinct long-cycle conjecture and creates no H0002 ownership conflict.

The compact root `RESULTS.md` still warns that its R-series table is stale (`UNMEASURED -> UNMEASURED`) and that newer complete own-track reports must be recovered before replacement. Per policy, this worker records the new structured delta only in this immutable report and does not edit the shared root.

### Current primary-source check, 2026-09-19

- Bansal--Jiang, arXiv:2508.03961v2, directly obtain the Beck--Fiala `O(sqrt(t))` scale for `t>=log^2 n`; below that range their displayed bound retains a polylogarithmic loss. Their result is algorithmic. Source: https://arxiv.org/abs/2508.03961 .
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 2026-09-10, prove the stronger Komlos statement with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`, with no restriction on `n`. Source: https://arxiv.org/abs/2609.11189 .
- Karingula--Lovett, ECCC TR26-188, posted 2026-09-17, give an elementary Komlos proof with constant `36` and describe it as a simplification of Guo--Fang--Lu. Source: https://eccc.weizmann.ac.il/report/2026/188/ .
- Christoph--Morawski--Wigderson, arXiv:2608.19145v1 (2026-08-19), remains the primary H0002 source: https://arxiv.org/abs/2608.19145 . A bounded fresh title/author/question search again surfaced this source and no later source-matching resolution of Question 5.1. This is negative evidence only, not a proof of worldwide openness or novelty.

Thus literal Beck--Fiala is a **KNOWN CURRENT-PREPRINT BASELINE**, not new R16 progress. The source-valid active successor remains H0002, whose exact source question asks for natural graph conditions forcing a linear component above `(1+epsilon)/lambda(G)`. The R16 H1--H2--H3 theorem is still only a sufficient-condition PARTIAL answer to that broader question.

### Prior-art check for the new mechanism

I searched combinations of `percolation / sorted degree profile / spectral L2 / rearrangement / Chebyshev integral inequality / majorization / giant component`. The bounded search returned classical rearrangement/majorization material and degree-sequence percolation, but no source-matching deterministic statement coupling the CMW spectral-energy bound with the decreasing Stieltjes absorption weight used below. **The rearrangement inequality itself is classical folklore; it is not claimed as new.** Failure of this bounded search is not a novelty certificate.

## 2. Incoming endpoint theorem and notation

Retain every hypothesis and reduction of the existing H0002 chain. At the connected-core endpoint:

- `b_P=alpha-d_P>0`;
- `a_P=rho-b_P`;
- `u_P:=1-a_P` is the density of vertices outside the endpoint core;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0`;
- `t(b)=[a_P/(rho-b)] [F_pad(alpha-b)/b]`, continuously extended by `t(b_P)=0`;
- `b_0>b_P` is the fixed maximizer on the terminal compact interval selected earlier, and `t_0:=t(b_0)>0`;
- the construction of that interval gives `b_0<u_P`;
- `bar_t(q):=sup_{b_P<=b<=q} t(b)` on the terminal prefix, extended by `bar_t(q)=0` for `q<b_P`, with `bar_t(b_0)=t_0`;
- `phi_r(z):=1-exp(-r z)` and `g_r(z):=phi_r(z)/z`, with `g_r(0)=r`.

Let `x(q)` be the nondecreasing normalized outside-degree profile into the connected core. The earlier full-core pair-capacity theorem gives, at the endpoint,

`int_0^b x(q)dq >= b t(b)`                                      (2.1)

for every certified terminal `b`, in particular

`int_0^{b_0} x(q)dq >= b_0 t_0`.                              (2.2)

The spectral-energy estimate is

`int_0^{u_P} x(q)^2 dq <= a_P`.                                (2.3)

For every finite old anchor family `D`, write its floor as `L_D(q)`. On `[0,b_0]`,

`0<=L_D(q)<=bar_t(q)`.                                         (2.4)

The immediately preceding run defined

`w_0:=exp(-Delta t_0)`,

`v(q):=exp(-Delta bar_t(q))-w_0 >=0`,                           (2.5)

so `v` is nonincreasing on `[0,b_0]` and `v(b_0)=0`. With

`y(q):=[x(q)-L_D(q)]_+`,                                       (2.6)

that run established, uniformly over finite `D`, the Stieltjes weighted first-moment lower bound

`int_0^{b_0} v(q)y(q)dq >= Theta`,                              (2.7)

where

`mu:=-d v = Delta exp(-Delta bar_t) d bar_t`,                    (2.8)

`K(s):=s bar_t(s)-int_0^s bar_t(q)dq`,                           (2.9)

and

`Theta:=int_{(0,b_0]} K(s) mu(ds).`                              (2.10)

It also proved the explicit coarse lower bound

`Theta>=Theta_*`,                                               (2.11)

`Theta_*=(b_P/Delta)[1-(1+Delta t_0)exp(-Delta t_0)]>0`.         (2.12)

The previous run then used only the crude weighted second-moment estimate

`int v y^2 <= M_*`,                                             (2.13)

`M_*:=(1-exp(-Delta t_0)) a_P`,                                 (2.14)

and the exact two-moment lemma

`int v phi_Delta(y) >= A g_Delta(B/A)`                           (2.15)

for `A=int v y`, `B=int v y^2`, obtaining

`eta_*:=Theta_* g_Delta(M_*/Theta_*)>0`,                         (2.16)

and the conservative finite-parameter increment

`delta_w:=eta_*/4`.                                             (2.17)

Its complete incoming envelope is

`E_wdual:=E_rfgap+delta_w`,                                     (2.18)

`G_wdual:=min{1,G_coreavg+E_wdual}`.                             (2.19)

This run attacks exactly the only crude inequality in that new correction: (2.13).

## 3. Method #20 — why the preceding weighted-moment algorithm loses information

The bound (2.13) treats the weighted energy as though all spectral energy could be placed where the extra absorption weight `v` is largest. That is the correct worst case for an arbitrary unsorted function. It is **not** compatible with the actual graph profile.

There are two structural restrictions which (2.13) ignores:

1. `x` is sorted nondecreasing while `v` is nonincreasing; high degree cannot be moved to the high-weight left edge without violating the ordering.
2. The prefix average (2.2), together with that ordering, forces every degree after `b_0` to stay at least `t_0`; hence a fixed amount of the global spectral `L2` budget is spent **outside** the weighted prefix before the weighted optimization even starts.

These are not additional graph hypotheses. They are consequences of the already-established prefix theorem and the definition of `x`.

This pinpoints the failure of the preceding relaxation and gives a route that acts on the entire weighted correction rather than on another local threshold.

## 4. Method #1 — change category: the graph constraint is an opposite-monotone rearrangement problem

### 4.1 The prefix average forces a permanent tail floor

Since `x` is nondecreasing on `[0,u_P]`, its value at and after `b_0` is at least the average on `[0,b_0]`. Thus (2.2) implies

`boxed: x(q)>=t_0 for a.e. q in [b_0,u_P].`                (4.1)

Indeed, if the right-continuous value at `b_0` were below `t_0`, every earlier value would also be below `t_0`, contradicting (2.2).

Substitute (4.1) into the global spectral budget (2.3). The energy available on the weighted prefix is at most

`int_0^{b_0} x(q)^2dq`
` <= a_P-(u_P-b_0)t_0^2`.                                  (4.2)

Define

`boxed: A_tail:=a_P-(u_P-b_0)t_0^2.`                       (4.3)

The selected terminal interval has `b_0<u_P` and `t_0>0`, hence

`boxed: A_tail<a_P.`                                       (4.4)

Feasibility also guarantees `A_tail>=0`: by Cauchy--Schwarz on the prefix and (4.1) on the tail, (2.2)--(2.3) imply `u_P t_0^2<=a_P`.

Thus the preceding report's use of the full `a_P` as a prefix second-moment budget was strictly wasteful for every frozen parameter triple.

### 4.2 Opposite monotonicity gives a second, independent depletion

Put

`V_0:=int_0^{b_0} v(q)dq`.                                    (4.5)

The function `v` is nonincreasing, while `x^2` is nondecreasing. Therefore the opposite-order Chebyshev/rearrangement inequality gives

`boxed: int_0^{b_0} v(q)x(q)^2dq`
` <= [V_0/b_0] int_0^{b_0}x(q)^2dq.`                         (4.6)

For completeness, this classical inequality has a one-line self-check. Since the two factors are oppositely monotone,

`(v(q)-v(s))(x(q)^2-x(s)^2)<=0`

for every `q,s`. Integrating over `[0,b_0]^2` and expanding gives exactly (4.6).

Because `0<=y<=x`, equations (4.2) and (4.6) yield

`boxed: int_0^{b_0} v(q)y(q)^2dq <= M_rearr`,              (4.7)

where

`boxed: M_rearr:=(V_0/b_0) A_tail.`                         (4.8)

This is a strict improvement over the incoming `M_*`. Indeed

`0<=v(q)<=1-exp(-Delta t_0)`,

so

`V_0/b_0 <= 1-exp(-Delta t_0)`.                              (4.9)

Together with `A_tail<a_P`,

`boxed: M_rearr < (1-exp(-Delta t_0))a_P=M_*.`              (4.10)

Strictness comes already from the forced tail-energy expenditure, so no equality-case subtlety for (4.6) is needed.

## 5. Method #24 — identify the actual weighted-energy extremal obstruction

The previous abstract obstruction allowed the weighted second moment to place all its energy where `v` is maximal. Equation (4.6) shows that this is not an admissible extremizer once the graph's sorted degree order is retained. Among oppositely ordered profiles with fixed unweighted prefix energy, the product integral cannot exceed the product of the averages. In particular, left-concentration of energy is the wrong extremal shape; the order constraint pushes high energy to the low-weight side.

So the correct extremal budget for the weighted two-moment lemma is not `M_*`, but `M_rearr`.

The exact first-moment information from the preceding Stieltjes argument can also be retained rather than replaced by the coarse `Theta_*`. Define

`boxed: eta_rearr:=Theta g_Delta(M_rearr/Theta).`           (5.1)

This is a fully specified functional of the already-defined threshold profile `bar_t` and the frozen parameters.

It strictly improves the previous endpoint correction. Let

`F(A,M):=A g_Delta(M/A)`.

The preceding exact-moment report already proved that, for `A>0,M>=0`, `F` is strictly increasing in `A` and strictly decreasing in `M` whenever the comparison in `M` is strict. Since

`Theta>=Theta_* >0`

and

`M_rearr<M_*`,

we have

`eta_rearr=F(Theta,M_rearr)`
` >= F(Theta_*,M_rearr)`
` > F(Theta_*,M_*)`
` = eta_*`.                                                (5.2)

Thus

`boxed: eta_rearr>eta_*.`                                  (5.3)

This is a strict gain at the endpoint before any conservative finite-core slack is introduced.

## 6. Finite connected core and finite sprinkling: the improvement survives the actual proof

The endpoint theorem is obtained through connected cores of density

`a_3=c_3 a_P`, `c_3<1`, `c_3 up 1`,

and a reserved independent sprinkling rate `r<Delta`, `r up Delta`. Let

`u_3:=1-a_3`.

For `c_3` sufficiently close to one, `b_0<u_3`. The finite-core prefix theorem gives

`int_0^{b_0}x(q)dq >= c_3 b_0 t_0-o(1)`.                   (6.1)

Monotonicity of the empirical sorted degree profile therefore gives

`x(q)>=c_3t_0-o(1)`

for every later position `q in [b_0,u_3]`. The spectral estimate is

`int_0^{u_3}x(q)^2dq <= a_3+o(1)`.                         (6.2)

Consequently

`int_0^{b_0}x(q)^2dq`
` <= a_3-(u_3-b_0)c_3^2t_0^2+o(1)`.                       (6.3)

Define the finite weight

`v_{c,r}(q):=exp(-r c_3 bar_t(q))-exp(-r c_3t_0)`,          (6.4)

which is still nonincreasing, and

`V_{c,r}:=int_0^{b_0}v_{c,r}(q)dq`.                        (6.5)

Applying the same opposite-order double-integral argument to `v_{c,r}` and `x^2`, then using `y^2<=x^2`, gives

`int_0^{b_0}v_{c,r}(q)y(q)^2dq <= M_{c,r}+o(1)`,            (6.6)

where

`M_{c,r}:=[V_{c,r}/b_0]`
` * [a_3-(u_3-b_0)c_3^2t_0^2].                            (6.7)

The finite Stieltjes first-moment argument from the preceding run gives the exact lower bound

`int_0^{b_0}v_{c,r}(q)y(q)dq >= Theta_{c,r}-o(1)`,          (6.8)

with

`mu_{c,r}:=r c_3 exp(-r c_3 bar_t)d bar_t`,                 (6.9)

`Theta_{c,r}:=c_3 int_{(0,b_0]} K(s) mu_{c,r}(ds)`.         (6.10)

The exact two-moment lemma, now with `phi_r`, therefore gives the finite endpoint-approximation correction

`eta_{c,r}:=Theta_{c,r} g_r(M_{c,r}/Theta_{c,r})`.          (6.11)

As `c_3 up 1` and `r up Delta`,

`M_{c,r}->M_rearr`,

`Theta_{c,r}->Theta`,

and hence

`eta_{c,r}->eta_rearr`.                                    (6.12)

The Stieltjes integral can, exactly as in the preceding report, be approximated by a finite partition of continuity points before the host-size limit, so no uncountable probabilistic intersection is introduced.

Choose `c_3,r` and that finite partition sufficiently close to the endpoint that the new weighted correction is at least `eta_rearr/2`, and then make the inherited finite-anchor, connected-core trimming, floor-cleaning, and concentration losses smaller than `eta_rearr/4`. The same independent final sprinkling edges and Poisson-binomial concentration already used in the R16 chain apply unchanged.

A conservative frozen increment is therefore

`boxed: delta_rearr:=eta_rearr/4>0.`                        (6.13)

Since `eta_rearr>eta_*`,

`boxed: delta_rearr>delta_w.`                              (6.14)

No new independence hypothesis has been added.

## 7. New complete envelope and strict comparison

The correction above replaces, rather than double-counts, the preceding Stieltjes weighted correction. The constant-weight prefix/tail minimax contribution `E_rfgap` remains unchanged. Define

`boxed: E_rearr:=E_rfgap+delta_rearr`,                      (7.1)

and

`boxed: G_rearr:=min{1,G_coreavg+E_rearr}.`                 (7.2)

The incoming report had

`G_wdual=min{1,G_coreavg+E_rfgap+delta_w}`.                 (7.3)

By (6.14),

`boxed: G_rearr>=G_wdual`                                  (7.4)

for every frozen H1--H2--H3 parameter triple, and whenever the incoming numerical metric is not already saturated,

`boxed: G_wdual<1  ==>  G_rearr>G_wdual.`                  (7.5)

If `G_wdual=1`, the metric itself is already at its absolute ceiling and no uniform giant-fraction lower bound can be numerically increased beyond one. This run does not pretend otherwise.

For every nonsaturated triple an explicit coefficient outside the entire incoming envelope is

`boxed: g_receipt:=G_wdual`
` +(1/2) min{delta_rearr-delta_w,1-G_wdual}.                (7.6)

Then

`G_wdual<g_receipt<G_rearr`.                               (7.7)

Consequently, on the **same frozen H1--H2--H3 class** and with no additional assumptions, the existing harvesting/gluing/sprinkling proof plus Sections 4--6 gives

`P(L_1(G_p)>=g n)->1`                                     (7.8)

for every fixed

`g<G_rearr`                                                (7.9)

whenever

`p>=(1+epsilon)/lambda(G)`.                               (7.10)

No endpoint attainment is claimed.

## 8. Why this is genuinely new movement rather than another checker or threshold tweak

The preceding Stieltjes report already harvested the full variable absorption multiplier. This run improves that same correction by proving that its putative worst second-moment distribution is incompatible with the sorted graph-degree profile.

The gain uses two pieces simultaneously:

- **mandatory tail energy:** the prefix-average constraint forces the sorted profile to stay above `t_0` on a positive-length tail, so the prefix cannot spend the whole spectral budget `a_P`;
- **opposite ordering:** on the weighted prefix the Stieltjes weight decreases exactly where sorted degree energy increases, so the weighted energy is at most the product of the averages.

Both are global structural consequences of the existing theorem. There is no finite enumeration claim and therefore no exact checker to manufacture.

The most important remaining obligation is now narrower than in the preceding run. The weighted first moment, the variable exponential multiplier, one exact weighted second-moment rearrangement, and the forced post-prefix energy have all been used. A further gain has to use information still discarded here, most naturally:

1. the **entire** family of prefix lower bounds to control the unweighted prefix energy more sharply than the single `b_0` average;
2. a full KKT/extreme-point theorem for the isotonic variational problem with all prefix obstacles; or
3. the complete post-`b_0` running floor rather than only the universal tail level `t_0` when subtracting energy.

The next serious route should be (1) or (2), not another scalar threshold certificate.

## 9. Section-B accounting

- **#1 CHANGE THE CATEGORY — SUCCESS.** Recasting the weighted spectral-energy term as an opposite-monotone rearrangement problem exposed a strict loss in the previous `M_*` budget.
- **#20 FIND WHY THE ALGORITHM FAILS — SUCCESS.** The previous moment relaxation fails because it lets high spectral energy occupy the high-weight left edge and ignores mandatory energy on the post-prefix tail; neither is compatible with the sorted degree profile.
- **#24 FIND THE EXTREMAL OBJECT — SUCCESS.** The double-integral rearrangement argument identifies the admissible worst weighted-energy profile under opposite ordering and replaces `M_*` by the strictly smaller `M_rearr`.

This triple is different from the immediately preceding run's `#2/#11/#13`.

## 10. Model and scheduler-control status

This run actually reports **GPT-5.6 Sol / reasoning UNVERIFIED**, not GPT-6 maximum. The currently exposed task-control schema still offers task prompt/title, schedule/start, timing mode, and enablement, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt**. GPT-6/maximum is therefore still prompt-only. Enforcing it would require platform-level model/reasoning fields plus per-run runtime attestation.

No scheduler modification was attempted because this research worker's controlling instruction forbids scheduler changes. The repository's current ledger says the historical P26 `You cannot modify this task` event was authorization-context-specific and that a later P26 update succeeded from an authorized context. For any task that still returns that denial, the compliant path is the owning authorized account/workspace or platform support; there is no permission-bypass workaround and no duplicate task should be created.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_source: Beck-Fiala_1981
  nominal_metric: complete_uniform_B(t,n)
  nominal_before: "B(t,n) < 3*sqrt(2*pi*t) for every integer t>=1, all n (Guo-Fang-Lu v1 current-preprint baseline)"
  nominal_after: "same KNOWN current-preprint baseline"
  nominal_movement: NONE_SOURCE_KNOWN
  metric_name: g_twoaxis_complete_envelope
  before: "G_wdual = min(1, G_coreavg + E_rfgap + delta_w)"
  after: "G_rearr = min(1, G_coreavg + E_rfgap + delta_rearr)"
  new_constants:
    A_tail: "a_P - (u_P-b_0)*t_0^2"
    V_0: "integral_0^b0 [exp(-Delta*bar_t(q))-exp(-Delta*t_0)] dq"
    M_rearr: "(V_0/b_0)*A_tail"
    Theta: "integral K(s) mu(ds), K(s)=s*bar_t(s)-integral_0^s bar_t, mu=Delta*exp(-Delta*bar_t)dbar_t"
    eta_rearr: "Theta*g_Delta(M_rearr/Theta)"
    delta_rearr: "eta_rearr/4"
  comparison: "M_rearr < M_*; eta_rearr > eta_*; delta_rearr > delta_w; G_rearr>=G_wdual, strict if G_wdual<1"
  movement: STRICT_POINTWISE_ON_NONSATURATED_TRIPLES
  status: PARTIAL
  supported_unchanged_count: 0
  methods: [1, 20, 24]
  finite_checker: NOT_APPLICABLE_ANALYTIC
  closure_audits: []
  remaining_obligation: >-
    Solve the full all-prefix isotonic/KKT variational problem, or use the
    complete post-b0 running floor to sharpen the forced spectral-energy
    depletion. Source Question 5.1 remains broader than the frozen H1-H2-H3
    sufficient-condition theorem.
```

## 12. Honest status

`H0002` remains **PARTIAL / source OPEN-looking / ACTIVE**. This report proves a strict quantitative strengthening of the current R16 sufficient-condition theorem on every nonsaturated frozen parameter triple; it does **not** claim to close CMW Question 5.1, and it does not claim novelty merely from a negative bounded search. No checker was created because the new claim is analytic and the full new inequality is proved above.
