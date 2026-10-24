Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **No movement: `T_corr=4 -> 4`. Methods tried: B5/B11/B30. New theorem-sized PARTIAL result: for every Campbell--O'Rourke C2 angular law with positive off-axis mass, if `F_theta(r)=mu_{alpha,theta}({|z|>r})`, then `r^alpha log(r) F_theta(r) -> +infinity`; on pure C2 axis support the same quantity tends to `0`. Thus arbitrarily small positive off-axis contamination produces a pointwise radial-tail anti-thinning jump, and the truncated critical `alpha`-moment grows faster than `log log R`. Question 1.9 remains OPEN because this does not determine regular variation, sharp constants, directional tails or the full tail profile.**

# HARD7-02 — Campbell--O'Rourke Question 1.9: a Tauberian anti-thinning dichotomy

Status: **PARTIAL / source Question 1.9 remains OPEN under bounded current-literature search / the new implication is proved on-page from the preceding HARD7-02 tail inputs and has an exact symbolic algebra self-check, but the full HARD7-02 theorem chain has not received the two independent closure audits required by CONTROL.md.**

Frozen source metric:

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=4`.

After: **`T_corr=4` — no movement.**

This is deliberate metric discipline. The preceding global positive-off-axis theorem already covers all such C2 families, so merely naming another covered family would be bookkeeping rather than new mathematical movement. The substantive progress below sharpens the radial tail itself, not the family count.

## 1. Continuity, repository state, ownership and runtime honesty

I resumed the active exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

from the newest completed checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T21-12-11Z__q19-global-moment-index-dichotomy.md`.

Before the mathematical work I re-read or refreshed:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current Q1.9 claim and newest HARD7-02 reports;
- the C0026--C0032 non-Hermitian/heavy-tail neighborhood of `probability_1000_intake_claude_20260907/problems.jsonl` (including the distinct C0031 almost-sure convergence question and C0032 iid explicit-density question);
- the neighboring R7-06 C0032 terminal handoff/current ownership material;
- repository-wide current hits for Campbell--O'Rourke Question 1.9 and its canonical wording.

The repository still records Q1.9 as owned by HARD7-02. Current admission-screen records explicitly recognize Q1.9 as owned HARD material; no competing create-only claim, public posting, source-resolution record or release was found. C0032 remains a different iid heavy-tailed circular-law density problem and is not an alias.

The runtime capability situation remains unchanged. The exposed scheduler/task surface has title/prompt, schedule/timing mode, enabled state and ordinary task controls, but **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry and no guaranteed-duration field**. Therefore `GPT-6 / maximum` is still prompt-requested only. Making it binding would require a product/backend interface that exposes model and effort controls for the task. The historical P26 `You cannot modify this task` response was a permission-context failure; repository state records that P26 was later editable from another authorized context. The compliant workaround for any task still refusing mutation is the owning/authorized account/workspace context, ownership transfer, or platform support, never a duplicate schedule or permission bypass. No scheduler mutation was attempted in this run.

No Gmail, Drive, public posting, paid compute, workflow execution, force push, neighboring-track edit, schedule creation/modification or permission bypass was performed.

## 2. Exact external source and bounded current-status refresh

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Current arXiv source:

`https://arxiv.org/abs/2010.01261` (v3, revised 2 February 2022).

Theorem 1.6 gives the deterministic limiting empirical spectral measure `mu_{alpha,theta_d}` under Condition C2. Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The source explicitly contrasts the heavy-tailed Hermitian regime with the iid non-Hermitian regime, whose limiting law has much lighter tails and finite moments of every order, and says its simulations suggest that tail behavior depends on `theta_d` and may vary with direction.

Fresh bounded searches on 19--20 September 2026 used the exact source title/authors, exact `Question 1.9` wording, `theta_d`, `mu_{alpha,theta_d}`, tail behavior, heavy-tailed elliptic, PWIT, dependence, moment index, and 2023--2026 follow-up terms. They recovered the source, Campbell--O'Rourke's later *Spectrum of Levy--Khintchine Random Laplacian Matrices* (J. Theor. Probab. 37 (2024), online 26 July 2023), and Carpenter--O'Rourke, *The Limiting Spectral Distribution for Sparse Elliptic Random Matrices* (arXiv:2508.04891, 2025), among unrelated elliptic/heavy-tail results. I did **not** locate a paper claiming a general resolution of Question 1.9, the support dichotomy below, or the pointwise anti-thinning statement below. This is bounded negative evidence, not a worldwide novelty or priority certificate.

## 3. Idea-before-code checkpoint and exact self-check

The route was written before checker construction at

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T22-12-00Z__idea-before-code-q19-tauberian-antithinning.md`

commit

`cdcdae0a16bb40eb03ef5c5e10f1932d563c27f5`.

Only after that checkpoint I wrote and executed the exact symbolic algebra self-check:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T22-12-00Z__q19-tauberian-antithinning-check.py`

commit

`91c308e34becf5040e392df1295cb6ef7781bdb2`,

with archived output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T22-12-00Z__q19-tauberian-antithinning-check.out`

commit

`215556180f6e0eaf1b3a8fd4c0133e5d355a8d16`,

ending

`ALL_EXACT_CHECKS_PASS = True`.

The checker is a **self-check only**. It verifies the symbolic scale identities and constants used below; it is not an independent proof audit of the preceding random-matrix inputs.

## 4. Inputs from the preceding HARD7-02 chain

Let `0<alpha<2`, normalize the finite nonzero angular measure to a probability measure using the already proved mass-homogeneity/dilation relation, and put

`F_theta(r) := mu_{alpha,theta}({z in C: |z|>r})`.                 (4.1)

For positive off-axis mass

`rho_off(theta):=theta({(w_1,w_2):w_1 w_2 !=0})>0`,                (4.2)

the preceding on-page theorem chain established the following two facts.

### Input A — all subcritical radial moments are finite

For every `0<p<alpha`,

`M_p(theta):=int_C |z|^p mu_{alpha,theta}(dz)<infinity`.           (4.3)

Hence Markov gives

`F_theta(r) <= M_p(theta) r^(-p)`.                                 (4.4)

### Input B — uniform integrated-tail lower signal

There exist `A_theta>0` and `r_0(theta)<infinity` such that

`V_theta(r):=int_r^infinity F_theta(t) dt/t`

obeys

`V_theta(r) >= A_theta r^(-alpha)`                                 (4.5)

for every `r>=r_0(theta)`.

The immediately preceding run used (4.3)--(4.5) to prove that the critical `alpha`-moment diverges. The new result extracts substantially stronger pointwise information.

## 5. Main theorem: positive off-axis mass forbids a `1/log r`-thin power tail

### Theorem 5.1 — Tauberian anti-thinning law

Assume (4.2). Then

`lim_{r->infinity} r^alpha log(r) F_theta(r) = +infinity`.         (5.1)

Equivalently, for every fixed `L>0` there is `R_L<infinity` such that

`F_theta(r) >= L r^(-alpha)/log r`                                 (5.2)

for all `r>=R_L`.

This does **not** assert regular variation or an exact constant in `r^alpha F_theta(r)`.

#### Proof

Fix an arbitrary `delta>0` and write `A=A_theta`. Choose the explicit subcritical exponent

`p_delta := alpha(2+delta)/(2(1+delta))`.                          (5.3)

Then

`alpha-p_delta = alpha delta/[2(1+delta)]>0`,                      (5.4)

and

`p_delta-alpha/(1+delta) = alpha delta/[2(1+delta)]>0`.            (5.5)

Thus `0<p_delta<alpha` and

`(1+delta)p_delta-alpha = alpha delta/2>0`.                        (5.6)

Set

`R=r^(1+delta)`.                                                    (5.7)

By the subcritical moment bound (4.4),

`V_theta(R)`
`<= int_R^infinity M_{p_delta} t^(-p_delta) dt/t`
`= [M_{p_delta}/p_delta] R^(-p_delta)`
`= [M_{p_delta}/p_delta] r^(-(1+delta)p_delta)`.                   (5.8)

Divide by `r^(-alpha)`. By (5.6),

`V_theta(R)/r^(-alpha)`
`<= [M_{p_delta}/p_delta] r^(-alpha delta/2) -> 0`.                (5.9)

Hence there is `r_delta<infinity` such that for all `r>=r_delta`,

`V_theta(R) <= (A/2) r^(-alpha)`.                                  (5.10)

For example, the exact algebra gives the sufficient threshold

`r^(alpha delta/2) >= 2M_{p_delta}/(A p_delta)`
` = 4M_{p_delta}(1+delta)/[A alpha(2+delta)]`.                     (5.11)

Now use only that `F_theta` is nonincreasing. For `R=r^(1+delta)`,

`V_theta(r)`
`= int_r^R F_theta(t)dt/t + V_theta(R)`
`<= F_theta(r) log(R/r) + V_theta(R)`
`= delta F_theta(r) log r + V_theta(R)`.                           (5.12)

Combine (4.5), (5.10), and (5.12): for all sufficiently large `r`,

`A r^(-alpha)`
`<= delta F_theta(r) log r + (A/2) r^(-alpha)`,                   (5.13)

so

`F_theta(r) >= [A/(2delta)] r^(-alpha)/log r`.                    (5.14)

The key point is that `delta>0` was arbitrary. Given any `L>0`, take for example

`delta=A/(4L)`.                                                     (5.15)

Then (5.14) gives, for all sufficiently large `r` depending on `L`,

`F_theta(r) >= 2L r^(-alpha)/log r`.                              (5.16)

In particular it eventually exceeds the right side of (5.2). Since `L` is arbitrary,

`r^alpha log r F_theta(r) -> +infinity`.                           (5.17)

`QED`

### What the theorem rules out

The previously known logarithmic exponent

`-log F_theta(r)/log r -> alpha`

alone permits tails such as `r^(-alpha)/(log r)^2`, `r^(-alpha)/(log r)`, or even much thinner slowly varying corrections. Divergence of the `alpha`-moment alone also does not exclude `r^(-alpha)/(log r)`. Theorem 5.1 excludes every eventually bounded multiple of

`r^(-alpha)/log r`.                                                (5.18)

That is genuinely new tail information extracted from the integrated determinant/PWIT lower signal.

## 6. Critical truncated moment diverges faster than `log log R`

Define the truncated critical radial moment

`Q_alpha(R):=int_C min(|z|^alpha,R^alpha) mu_{alpha,theta}(dz)`.   (6.1)

Layer cake gives

`Q_alpha(R)=alpha int_0^R t^(alpha-1)F_theta(t)dt`.                (6.2)

Fix arbitrary `L>0`. By Theorem 5.1 there is `R_L` such that

`F_theta(t)>=L t^(-alpha)/log t`                                  (6.3)

for all `t>=R_L`; enlarge `R_L` so `R_L>e`. Then for `R>=R_L`,

`Q_alpha(R)`
`>= alpha L int_{R_L}^R dt/[t log t]`
`= alpha L [log log R-log log R_L]`.                              (6.4)

Divide by `log log R` and take `liminf`. This gives at least `alpha L`. Since `L` was arbitrary,

`Q_alpha(R)/(log log R) -> +infinity`.                             (6.5)

Thus the preceding statement “the critical moment is infinite” can be strengthened to an explicit asymptotic lower-divergence class, albeit without a sharp rate beyond `log log`.

## 7. Full C2 support dichotomy for this pointwise tail functional

The preceding run proved that if `rho_off(theta)=0`, Condition C2 forces positive mass on both coordinate axes and the limiting law is an exact nonzero dilation of the iid heavy-tailed circular limit. In particular every positive radial moment is finite.

Choose any `q>alpha`. Then Markov gives

`F_theta(r)<=M_q r^(-q)`,                                         (7.1)

so

`r^alpha log r F_theta(r) <= M_q r^(-(q-alpha)) log r ->0`.       (7.2)

Combining this with Theorem 5.1 gives the exact dichotomy

`lim_{r->infinity} r^alpha log r F_theta(r)`
`= 0`       if `rho_off(theta)=0`,
`= +infinity` if `rho_off(theta)>0`.                              (7.3)

Therefore the entire C2 angular class has no intermediate finite positive value for this tail functional.

This is invariant under the deterministic output dilation induced by rescaling the total mass of the finite angular measure: replacing `X` by `cX` changes `F(r)` to `F(r/c)` and multiplies the `r^alpha` scale by a finite constant, while `log(r)/log(r/c)->1`. Thus the `0` versus `+infinity` dichotomy applies to the original finite `theta_d`, not only its probability normalization.

## 8. B5 — deform away from the iid axis endpoint: the tail transition is singular

Take any C2 axis-supported angular probability `theta_0`, and any C2 angular probability `theta_1` having positive off-axis mass. For `0<=epsilon<=1`, define

`theta_epsilon=(1-epsilon)theta_0+epsilon theta_1`.                (8.1)

For `epsilon=0`, `rho_off(theta_epsilon)=0`, so by (7.3)

`r^alpha log r F_{theta_0}(r)->0`.                                 (8.2)

For every fixed `epsilon>0`,

`rho_off(theta_epsilon)>=epsilon rho_off(theta_1)>0`,              (8.3)

and therefore

`r^alpha log r F_{theta_epsilon}(r)->+infinity`.                   (8.4)

So this tail functional does **not** interpolate continuously from the iid/axis endpoint into the interior. An arbitrarily small but fixed positive off-axis contamination changes the asymptotic from zero to infinity.

**B5 outcome: success.** Adding a dependence parameter and pushing it to the boundary exposes a singular phase transition rather than a smooth perturbative tail law. This directly attacks the intuitive “near-axis means smoothly near-iid tail” heuristic suggested by finite-size pictures.

## 9. B11 — dualize the determinant lower signal into a pointwise tail law

The previous determinant/PWIT route naturally produced `V_theta(r)`, an integrated tail object. The obstruction was that an integrated lower bound does not ordinarily give a pointwise lower bound without extra control on the tail beyond the scale of interest.

The subcritical moment family supplies exactly that dual control. By moving the far cutoff to `R=r^(1+delta)` and choosing `p_delta` just large enough that `(1+delta)p_delta>alpha`, the remote tail becomes `o(r^-alpha)`. Monotonicity on the finite multiplicative annulus then transfers the remaining integrated mass back to `F_theta(r)`.

**B11 outcome: success.** The integrated-potential lower bound and the family of subcritical moment upper bounds are dual enough to produce a uniform pointwise anti-thinning theorem.

## 10. B30 — one radial scale at a time

The precise localization unit is the annulus

`[r, r^(1+delta)]`.                                                (10.1)

The proof glues exactly three pieces at this scale:

1. source-derived integrated lower signal at `r`;
2. remote-tail disposal beyond `r^(1+delta)` via a source-valid subcritical moment;
3. monotonicity of the limiting radial tail inside the annulus.

There is no finite-size spectral fit, no conversion of numerical evidence into an infinite-volume claim, and no claim that a sufficient moment argument is necessary.

**B30 outcome: success.** Radial-scale localization identifies the logarithmic annulus width as the only loss in transferring `V` to `F`; varying that width then forces the coefficient to diverge.

## 11. Counterexample-first outcome and remaining obstruction

The first stress test was the natural candidate

`F(r) approximately r^(-alpha)/log r`.                             (11.1)

It has the already known power exponent `alpha` and an infinite critical moment, so neither previous conclusion rules it out. But

`int_r^infinity F(t)dt/t`

is only order `r^(-alpha)/log r`, contradicting (4.5). The same is true for any eventually bounded multiple of (11.1).

The new theorem still does **not** force

`liminf r^alpha F(r)>0`.                                           (11.2)

For example, the present argument is compatible with tails whose slowly varying factor tends to zero more slowly than `1/log r`, because the threshold associated with `p_delta` can deteriorate arbitrarily as `delta downarrow0` through the unknown growth of `M_p` as `p upalpha`.

The next real obstruction is therefore quantitative control of the subcritical moment blow-up

`M_p(theta)` as `p up alpha`,                                     (11.3)

or an independent annular upper bound on `V_theta(r^(1+delta))` that is uniform as `delta downarrow0`. Either could remove the logarithmic localization loss and potentially force a true `c_theta r^-alpha` pointwise lower tail or a regularly varying profile.

This is the source-relevant next target, not another checker for the unchanged family count.

## 12. Why Question 1.9 is not closed

The source asks how the full tail behavior varies with `theta_d`. The current HARD7-02 chain now supplies substantial radial classification:

- exact output law on pure axis support up to a deterministic dilation;
- exact radial power exponent `alpha` for every positive-off-axis C2 law;
- exact radial moment-index dichotomy `infinity` versus `alpha`;
- the new pointwise functional dichotomy (7.3);
- super-`log log` divergence of the truncated critical moment in the off-axis regime.

But a full answer still requires at least some combination of:

- sharp asymptotic constants or a proof/disproof of radial regular variation;
- classification of possible slowly varying corrections;
- directional/anisotropic tail behavior, which the source explicitly flags as potentially varying by direction;
- an exact connection between those finer tails and the full angular measure rather than only the support statistic `rho_off=0` versus `>0`.

Therefore the honest source status is **OPEN / PARTIAL**, not PROVED.

## 13. Exact checker scope

The symbolic self-check verifies exactly:

`p_delta=alpha(2+delta)/(2(1+delta))`,

`alpha-p_delta = p_delta-alpha/(1+delta) = alpha delta/[2(1+delta)]`,

`(1+delta)p_delta-alpha=alpha delta/2`,

`V(r^(1+delta))/r^(-alpha) <= [M_p/p] r^(-alpha delta/2)`,

`log(r^(1+delta)/r)=delta log r`,

the half-signal threshold

`r^(alpha delta/2) >= 4M_p(1+delta)/[A alpha(2+delta)]`,

the pointwise coefficient `A/(2delta)`, and

`int alpha L dt/(t log t)=alpha L log log t`.

These are exact algebraic identities. The random-matrix statements feeding `A` and `M_p` are theorem-sized inputs from prior HARD7-02 reports and remain subject to the independent audit requirement.

## 14. Stuck/rotation status

The frozen metric did not move this run, but the previous run moved `T_corr=3->4`; therefore this is **not** a three-run stagnant sequence and Section I is not yet triggered. More importantly, the remaining obligation changed materially from “decide the endpoint moment” to the quantitative boundary problem (11.3).

If future runs fail to improve the fixed metric or the same remaining obligation persists for the Section-I threshold, the track must execute the prescribed thinking-only stuck protocol and eventually rotate rather than manufacture more certificates.

Suggested next method triple, different from B5/B11/B30: **B3 / B17 / B28** — try to prove a stronger uniform near-critical moment estimate, search known stable/PWIT moment-blowup constants in adjacent fields, and replace a full all-`theta` target by a typical/off-axis angular class if the uniform problem is too rigid.

## 15. Ledger delta for coordinator consumption

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell--O'Rourke (2022) Question 1.9
  quantity: T_corr
  before: 4
  after: 4
  movement: no movement
  status: PARTIAL
  methods: [B5, B11, B30]
  theorem_candidate: "For rho_off(theta)>0, r^alpha log(r) F_theta(r) -> +infinity; for rho_off(theta)=0 under C2 it tends to 0. Off-axis truncated critical alpha moment divided by log log R tends to infinity."
  source_status: OPEN under bounded current-literature search
  audit_status: self-check only; independent closure audits not requested because source is not closed
  next_obligation: "Control M_p(theta) as p approaches alpha, or obtain a delta-uniform annular V-tail estimate, to attack regular variation/sharp radial constants and then directional tails."
```
