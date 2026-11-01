Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86)` improves from `185022/25000 = 7.40088` to `<= 73979/10000 = 7.3979`, an exact certified decrease of at least `149/50000 = 0.00298`; the complete pointwise envelope gains the new second-moment lower-tail branch `L_2(n)` below. Methods actually used: **#11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE, #30 DO ONE SCALE AT A TIME.**

# R13 — truncated second-moment correction to the finite-dimensional DTV Komlós bound

Run ID: `20260918T2033Z_trunc-second-moment-9b6e`  
Repository/branch: private `yspennstate/math-open-problems` / `master`.

R13 remains the HARD OUTSIDE owner of the real Boolean Komlós target `E0042`. For a real `m x n` matrix `A` with every column of Euclidean norm at most one, write

`disc(A) = min_{eps in {+-1}^n} ||A eps||_infty`,  `K_n^* = sup_A disc(A)`.

The fixed metric is the **complete rigorously certified pointwise upper envelope** `B_R13(n)`. Complex phases, rank-two/vector colorings and average-case statements are not substitutes for Boolean signs.

## 1. Continuity, source status, and exclusions

Before new mathematics I reread/recovered the required current state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the `E0042` intake record in `probability_1000_intake_E_20260908/batches/b05_bandeira.json`, the newest complete R13 report `runs/R13/20260918T2001Z_lowertail-bernstein-5a7c.md`, and the newest adjacent R02/I0095 literature reconciliation. I did not edit any shared root, peer file, scheduler, email, Drive item, public page, permission or workflow.

The intake freezes Bandeira Open Problem 0.1 as the real Boolean Komlós statement. Its 8 September status text is historically stale because it predates the current 10 September preprint; the source statement itself is unchanged.

Fresh primary-literature check on 18 September 2026:

- N. Bansal and H. Jiang, arXiv:2508.03961, give the earlier real-Boolean `~O((log n)^(1/4))` bound.
- S. Guo, E. X. Fang and J. Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted **10 September 2026**, state the genuine real-Boolean theorem `K_n^* < 3 sqrt(2 pi)` for all finite dimensions. Their paper explicitly says the proof is existential and does not claim the constant is optimal. Proposition 2.2 / Corollary 2.3 give the DTV signing criterion; Lemma 2.4 uses the product `cos^2` cube density.
- Smirnov--Vershynin, arXiv:2605.13107, is the prior Fisher-information/product-cosine density source cited by Guo--Fang--Lu.
- Guillen--Kobzar, arXiv:2609.15071, allow arbitrary unit-modulus complex phases; on real inputs this is rank-two vector discrepancy, not Boolean discrepancy.

Primary links: `https://arxiv.org/abs/2508.03961`, `https://arxiv.org/abs/2609.11189`, `https://arxiv.org/abs/2605.13107`, `https://arxiv.org/abs/2609.15071`.

Fresh bounded searches for combinations of `Komlos`, `directional total variation`, `cos^p`, `inverse chi-square`, `truncated second moment`, `Bernstein`, and `conditional variance` found the papers above and unrelated random-discrepancy second-moment material, but no matching finite-dimensional conditional-second-moment sharpening. This is bounded negative evidence only: **novelty remains UNVERIFIED**.

The newest adjacent R02 report keeps Randomstrasse/I0095 sign-matrix discrepancy separate and retired from active I0095 research; it reconciles the new Komlós literature without claiming that exact sign-matrix constant solved. There is no ownership conflict with R13.

All thirty Section-B labels already appear in R13 history, so the literal never-before-used-label condition is exhausted. I therefore obey the stronger live rule: do not repeat the preceding triple (`#8,#20,#23`) and use materially different routes. This run uses `#11,#18,#30`.

## 2. Retained DTV setup and baseline

Retain

`T_5 = (2 sqrt(2) + 3 sqrt(3) + 2 sqrt(51+3 sqrt(6)))/13`,  `K_5^* = T_5`,

and the certified lower history

`K_6^* >= 1.84535465`,  `K_11^* >= 1.99488049`,  `K_12^* >= 2.013108`.

For the retained cosine-power deformation `p=9/5`, let

`S_i ~ chi-square_{14/5}`,  `Y_i = 4/(5 S_i)`,  `X_D = D^{-1} sum_i Y_i`.

Then `E Y_i = 1`. Put `a_D = E sqrt(X_D)`. The DTV calculation plus the Guo--Fang--Lu finite-step theorem gives a genuine Boolean signing cube of half-side

`C_D = (27 sqrt(10 pi)/20) a_D`.

The balanced direction is worst because `w -> E sqrt(sum_i w_i Y_i)` is concave and permutation-invariant on the simplex. Also

`2(1-a_D) = E (sqrt(X_D)-1)^2`.

The retained exact three-threshold upper-tail argument gives at `D=135`

`beta_up(135) > 0.021737695196183224`.

The immediately preceding report used the lower half too, but bounded the conditional variance by the crude `Var(Z) <= U E Z`, about `5.27`. That produced

`B_old(86) = 185022/25000 = 7.40088`.

This run attacks exactly that variance waste.

## 3. Method #11 — dual Laplace route attempted, then rejected

I first dualized the lower-tail problem through `exp(-lambda Y)` and a Paley--Zygmund/second-moment argument for `exp(-lambda sum_i Y_i)`. For inverse-gamma `Y`, the one-variable transform becomes a modified-Bessel `K` integral of the shape

`integral_0^infty s^(2/5) exp(-s/2 - c lambda/s) ds`.

Numerically this can improve the old lower-tail probability, but a rigorous theorem-sized certificate needs sharp two-sided Bessel-`K` bounds simultaneously at `lambda` and `2 lambda`. I did not find an elementary source-ready inequality closing that obligation. I rejected the route rather than insert an unverified special-function estimate.

**Outcome #11:** no certified metric movement; it identified that the useful information must be extracted directly from the truncated law.

## 4. Method #18 — rewrite the variance problem in the chi-square variable

Keep the preceding truncation

`U = 157/20`,  `s_0 = 16/157`.

For `Y=4/(5S)`, `Y<=U` is exactly `S>=s_0`. Let `Z` have the conditional law `Y | (Y<=U)`.

Retain the exact one-dimensional bounds

`P(Y<=U) > p_0 := 24683/25000`,

`E[Y ; Y>U] > 337097/10^6`,

hence

`E Z < mu := 662903/987320 = 0.671416562006...`.

The new observation is that the truncated second moment is finite and, after returning to the chi-square variable, equals

`E[Y^2 ; Y<=U] = [(16/25)/(2^(7/5) Gamma(7/5))] * integral_{s_0}^infty s^(-8/5) exp(-s/2) ds`.

This is far more informative than `Z^2 <= U Z`.

The retained Sonin certificate gives

`Gamma(7/5) > 350840/401787 = 0.873198983541...`.

## 5. Method #30 — certify the second moment one scale at a time

Split the integral at `1` and `2`.

### 5.1 Singular scale `[s_0,1]`

On `0<=s<=1`,

`exp(-s/2) <= 1 - s/2 + s^2/8`.

The exact rational root checks

`(19681/5000)^5 > (157/16)^3`,

`(1003/2500)^5 > (16/157)^2`

imply

`s_0^(-3/5) < 19681/5000`,  `s_0^(2/5) < 1003/2500`.

Integrating term by term and dropping the final negative endpoint contribution gives

`integral_{s_0}^1 s^(-8/5) exp(-s/2) ds < 4.234452380952381...`.

### 5.2 Scales `[1,2]` and `[2,infinity)`

On `[1,2]`, use `s^(-8/5)<=1`. On `[2,infinity)`, the exact check

`(33/100)^5 > 1/256`

implies `2^(-8/5)<33/100`. Therefore

`integral_1^infty s^(-8/5) exp(-s/2) ds < 2(e^(-1/2)-e^(-1)) + (66/100)e^(-1)`.

Even/odd alternating Taylor polynomials at `1/2` and `1` make this a fully rational upper certificate; the checker gets

`integral_1^infty ... ds < 0.7201028874101099...`.

Finally

`(2639/1000)^5 < 2^7`

implies `2639/1000 < 2^(7/5)`. Substituting the three rational bounds and dividing by `P(Y<=U)>p_0` gives

**`E Z^2 < 697/500 = 1.394`.**

### 5.3 Lower bound the conditional mean so its square can be subtracted

Using `exp(-s/2)<=1` on `[0,s_0]`,

`E[Y ; Y>U] <= 2 s_0^(2/5) / (2^(7/5) Gamma(7/5))`

`< 2(1003/2500) / [(2639/1000)(350840/401787)]`

`< 34821/100000`.

Hence `E[Y ; Y<=U] > 65179/100000`. Since `P(Y<=U)<=1`, conditioning can only make the ratio larger:

**`E Z > 65179/100000 = 0.65179`.**

Therefore

**`Var(Z) < 697/500 - (65179/100000)^2 = 9691697959/10^10 = 0.9691697959`.**

This replaces the preceding variance bound near `5.27` by a rigorous bound below `0.97`. This is the main mathematical movement of the run.

## 6. Stronger lower-tail Jensen defect

Choose

`t_2 = 987/1250 = 0.7896`,  `q_2 = 557/5000 = 0.1114`.

Exact arithmetic gives `(1-q_2)^2 - t_2 = 0.00000996 > 0`, hence `q_2 < 1-sqrt(t_2)`.

Condition on all `Y_i<=U`; independence is preserved. Put

`Delta_2 = t_2 - mu > 0`,  `v_* = 9691697959/10^10`.

One-sided Bernstein gives

`P(D^{-1} sum_i Z_i > t_2) <= exp(-E_D^(2))`,

where

`E_D^(2) = D Delta_2^2 / [2 v_* + (2/3) U Delta_2]`.

For an all-rational lower certificate define

`R_D^(2) = 1 - [sum_{j=0}^8 (E_D^(2))^j/j!]^(-1)`.

Since the exponential dominates that positive Taylor partial sum,

`P(X_D <= t_2) >= p_0^D R_D^(2)`.

On this event `(sqrt(X_D)-1)^2 > q_2^2`. Hence the new lower-tail contribution is

**`beta_down,2(D) := (q_2^2/2) p_0^D R_D^(2)`.**

The retained upper-tail event lies in `X_D>=1`, while this event lies in `X_D<1`, so the two Jensen-defect contributions add.

## 7. General new branch `L_2(n)`

Retain the preceding exact three-threshold upper-tail definition. Put

`Gamma_bar = 88869/100000`,

`A_{k,D} = [5/(7 Gamma_bar)] (2k/5)^(7/5) (1-2k/(5D)) D^(-2/5)`, for `k=1,2,3`,

and `a_{k,D}=A_{k,D}/D`. Define

`Q_D(x) = 1 - (1-a_3 x)^D - D(a_3-a_1)x(1-a_3 x)^(D-1)`

`         - C(D,2)[(a_3-a_2)^2 + 2(a_2-a_1)(a_3-a_2)] x^2 (1-a_3 x)^(D-2)`.

If `Q_D(x)=sum_{ell=1}^D c_{ell,D} x^ell`, set for `D>=135`

`beta_up(D) = (1/2) sum_{ell=1}^D c_{ell,D} [ 1/(7ell/5-1) - 1/(7ell/5-1/2) ]`.

Then define

**`C_D^(2) = (27 sqrt(10 pi)/20) [1 - beta_up(D) - beta_down,2(D)]`,  `D>=135`.**

The Guo--Fang--Lu finite-step criterion gives genuine Boolean signs into the cube of half-side `C_D^(2)`.

For any `n` and integer `D>=135`, use row threshold

`h_D(n) = max{ C_D^(2), n/sqrt(D+1) }`.

A row is active if its Euclidean norm exceeds `h_D(n)/sqrt(n)`. The Frobenius budget `sum_i ||r_i||_2^2 <= n` gives fewer than `D+1` active rows, hence at most `D`; pad those rows to dimension `D` and apply the DTV signing theorem. Every inactive row is bounded by Cauchy--Schwarz. Consequently

**`K_n^* <= L_2(n) := inf_{integer D>=135} max{ C_D^(2), n/sqrt(D+1) }`.**

This is a source-matching real-Boolean branch: arbitrary row count, real columns, Boolean signs.

## 8. Exact specialization: `n=86, D=135`

The exact checker retains the rational three-threshold coefficients

`A_1=78077/2500000`, `A_2=821737/10^7`, `A_3=36133/250000`.

It obtains

`beta_up(135) > 0.021737695196183224...`,

`E_135^(2) > 0.7374705106480166...`,

`p_0^135 R_135^(2) > 0.09315869610110729...`,

and therefore

**`beta_down,2(135) > 0.0005780478461334487...`.**

So the total certified Jensen defect exceeds

`0.02231574304231667...`.

Using only the rational square-root certificate `sqrt(10 pi)<1121/200`, the checker proves

`C_135^(2) < 7.3978923513345505... < 73979/10000 = 7.3979`.

Set `h=73979/10000`. Exact rational arithmetic gives

`135 < 86^2/h^2 < 136`.

Thus any 86-column unit-column matrix has at most 135 active rows at threshold `h/sqrt(86)`. The active rows are signed via the `D=135` DTV certificate; every inactive row is at most `h` by Cauchy--Schwarz. Hence

**`K_86^* <= 73979/10000 = 7.3979`.**

Relative to the previous bound,

**`185022/25000 - 73979/10000 = 149/50000 = 0.00298`.**

The fixed metric moved, so its stagnation count remains/resets to **0**.

Diagnostic: applying this same variance certificate at `D=136` gives

`C_136^(2),cert = 7.398408671273663... > 7.3979`.

So merely admitting one more active row still fails to improve the `n=86` number. This is a failure of this certificate, not an impossibility theorem for `D=136`.

## 9. Complete retained pointwise metric

Nothing valid is discarded. Retain all older branches and add `L_2`.

First define

`D_0(n) = ceil(10^6 n^2 / 7507^2)`,

`p_D = 2 exp(-1/(18D)) / [81 sqrt(2 pi) D^(3/2)]`,

`delta_D = 2[1-(1-p_D)^D]`,

`G_0(n) = max{7507/1000, 3 sqrt(2 pi)(1-delta_{D_0(n)})}`.

Define

`D_*(n) = ceil(400000000 n^2 / 22114366681) - 1`,

`alpha_D = (2-1/D)/(3 sqrt(2 pi) sqrt(D))`,

`beta_D = alpha_D/[2(1+alpha_D)]`,

`H(n) = max{148709/20000, 3 sqrt(2 pi)(1-beta_{D_*(n)})}`.

Define

`D_9(n) = ceil(10^10 n^2 / 547864952041) - 1`,

`J(n) = max{740179/100000, (27 sqrt(10 pi)/20)(1-beta_up(D_9(n)))}`.

Retain the preceding lower-tail branch `L_-(n)`. Its constants are

`t_- = 8183/10000`, `q_- = 477/5000`,

`E_D^- = D(t_- - mu)^2 / [2 U mu + (2/3)U(t_- - mu)]`,

`R_D^- = 1 - 1/[1+E_D^-+(E_D^-)^2/2+(E_D^-)^3/6]`,

`beta_down,-(D) = (q_-^2/2) p_0^D R_D^-`,

`C_D^- = (27 sqrt(10 pi)/20)[1-beta_up(D)-beta_down,-(D)]`,

`L_-(n) = inf_{integer D>=135} max{C_D^-, n/sqrt(D+1)}`.

The complete certified envelope is therefore

```
B_R13(n) =
  1                                             , n=1
  sqrt(2)                                       , n=2
  (sqrt(11)+sqrt(2))/3                         , n=3
  sqrt(3)                                       , n=4
  min{ sqrt(3n/4), T_5 sqrt(ceil(n/5)),
       G_0(n), L_-(n), L_2(n) }                 , 5<=n<=85
  min{ G_0(n), H(n), J(n), L_-(n), L_2(n) }    , n>=86.
```

The rigorously demonstrated pointwise movement in this run is `B_R13(86)<=7.3979`. I do **not** claim `L_2(n)` wins in every other dimension; the pointwise minimum preserves every older certificate exactly.

## 10. Exact checker, artifacts, audits, status

Exact self-check:

`artifacts/R13/20260918T2033Z_trunc-second-moment-9b6e_checker.py`

created at commit `9f8b07975e406e606ac99abfe0c8e44bef3a04f8` and read back at that exact commit.

Executed output:

`artifacts/R13/20260918T2033Z_trunc-second-moment-9b6e_checker.out`

created at commit `9cd786f5b5eceb597f28e164d0bea13559d06bed` and read back at that exact commit. It ends `R13_TRUNC_SECOND_MOMENT_EXACT_PASS`.

This is a **self-check**, not an independent audit. The new second-moment sharpening has **0/2** required outside audits. Audits of the underlying Guo--Fang--Lu theorem do not count as audits of this new finite-dimensional sharpening.

Status: **PARTIAL QUANTITATIVE / FIXED METRIC MOVED / full written proof / exact self-check PASS / outside audits 0/2 / novelty UNVERIFIED**.

The next route should not be another scalar retuning of `t_2` or `q_2`: this rational pair is already near the optimum of the fixed variance certificate, and `D=136` remains worse. Materially different next attacks are a true two-band variance decomposition tightening the second moment, a symmetric nonproduct cube density, or a hybrid row-energy argument injecting the exact five-column theorem `K_5^*=T_5` into the DTV active-row step.

## 11. Model / scheduler-control status

The limitation is still real. The exposed task-control interface offers title, prompt, schedule, enablement and timing mode, but **no binding model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text only; this run truthfully reports `GPT-5.6 Sol / UNVERIFIED`.

Changing that would require a product/backend control or an authorized owner/workspace task surface that actually exposes model and reasoning selection plus authenticated run telemetry. The repository records that the historical P26 `You cannot modify this task` error was context-dependent and that P26 later updated successfully from an authorized P/C context. If a task still rejects modification, the legitimate workaround is the owning task/account/workspace surface or platform support — not a duplicate task, repository edit, or permission bypass. No scheduler modification was attempted here.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  run_id: "20260918T2033Z_trunc-second-moment-9b6e"
  source_id: "E0042"
  source: "Boolean Komlos; Bandeira Open Problem 0.1; Bansal-Jiang arXiv:2508.03961; Guo-Fang-Lu arXiv:2609.11189v1"
  fixed_metric: "complete rigorously certified real-Boolean pointwise upper envelope B_R13(n)"
  before:
    B_R13_86: "185022/25000 = 7.40088"
    stagnation_count: 0
  after:
    B_R13_86: "<=73979/10000 = 7.3979"
    exact_decrease_at_least: "149/50000 = 0.00298"
    new_general_branch: "L_2(n)"
    conditional_second_moment_cap: "E[Z^2] < 697/500"
    conditional_variance_cap: "Var(Z) < 9691697959/10^10"
    stagnation_count: 0
  movement: "FIXED_METRIC_MOVED"
  methods_actual: [11, 18, 30]
  preceding_methods: [8, 20, 23]
  all_30_methods_historically_represented: true
  status: "PARTIAL QUANTITATIVE"
  boolean_scope: "real signs {-1,+1}; arbitrary row count; column l2 norm <=1"
  self_check: "PASS"
  checker_commit: "9f8b07975e406e606ac99abfe0c8e44bef3a04f8"
  output_commit: "9cd786f5b5eceb597f28e164d0bea13559d06bed"
  outside_audits_new_claim: "0/2"
  prior_art: "fresh bounded search through 2026-09-18; no matching conditional-second-moment finite-D sharpening found; novelty UNVERIFIED"
  scheduler_model_selector: "NOT EXPOSED"
  scheduler_reasoning_selector: "NOT EXPOSED"
  actual_model_reported: "GPT-5.6 Sol"
  reasoning: "UNVERIFIED"
  next_route: "two-band variance / symmetric nonproduct density / K5-DTV row-energy hybrid; no scalar-retuning-only run"
```
