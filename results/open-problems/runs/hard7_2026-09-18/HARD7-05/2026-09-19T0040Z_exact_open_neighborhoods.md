Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 frozen metric no movement: `W_{1/4}=0 -> 0`; methods B21 / B27 / B29. Substantive source progress: the exact identity `theta_{2,H}=H/2` holds on nonempty open neighborhoods of both `H=1/4` and `H=1/3`.**

# HARD7-05 run 5 — strict-comparison openness gives exact Hurst neighborhoods

Status: **PARTIAL for the full Molchan source problem.** The source asks for the entire function `H -> theta_{2,H}` on `0<H<1`, `H != 1/2`. Runs 3 and 4 established the isolated exact values `theta_{2,1/4}=1/8` and `theta_{2,1/3}=1/6`. This run proves that neither exact value is isolated: each lies inside a nonempty open interval on which the source lower bound is sharp.

No numerical interval width is claimed. The theorem below is qualitative-open but rigorous; it is not inferred from sampled paths, a finite H-grid, or a finite-t grid.

## 1. Continuity, source, ownership, repository read

I resumed the exclusive canonical claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`, and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-05/2026-09-18T2341Z_theta_third_exact.md`.

Before new mathematics I re-read:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the canonical claim and all four preceding HARD7-05 reports recovered by repository search;
- newest neighboring reports `HARD7-04/2026-09-18T23-37Z__p0157_finite_population_hub_lln.md` and `HARD7-06/2026-09-18T23-55-00Z__stuck1_cluster_port.md`;
- targeted claim/intake/repository searches for `2509.10265`, the exact Molchan title, and integrated-fBM persistence aliases.

The large `probability_1000_intake_*/problems.jsonl` ledgers are not rendered byte-for-byte by the connector without truncation, so this is honestly a targeted intake/claim reread, not a false claim of literal full-file rendering. The canonical search still returns the Molchan target only as the HARD7-05 claim plus this track's reports; I found no release, duplicate owner, posted equivalent, or canonical collision.

The primary source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265. The current 25-page PDF was re-read directly on 19 September 2026. Printed p. 3 still says that the `alpha=2`, `H != 1/2` exponent values remain unsolved and gives

`(1/2)(H min (1-H)) <= theta_{2,H}`.

Printed p. 6, Statement 1.4, gives for the stationary Laplace-FBM family with covariance

`K_m(t)=cosh((1-2m)t/2)/cosh(t/2)`, `0<m<=1/2`,

the exact persistence exponent `3m/8`. The same page's Lemma 1.5 explicitly uses a parameter-dependent Slepian comparison with separate middle-lag and endpoint conditions. That source-adjacent architecture matters below; I do **not** claim that the general idea of splitting lag scales is new.

Fresh bounded web/arXiv searches dated 19 September 2026 used the exact title/identifier, `theta_{2,1/4}`, `theta_{2,1/3}`, `integrated fractional Brownian persistence exact exponent`, and `Slepian persistence exponent covariance continuity`. They recovered the current Molchan paper, Molchan's earlier bounds, adjacent 2026 Gaussian-field persistence work, and Aurzada--Bothe--Druet--Kettner--Profeta's 2024 perturbation theory for discrete MA(1)/Slepian persistence, but no later exact solution of the continuous integrated-fBM `theta_{2,H}` function or exact H-neighborhood theorem. This is bounded negative evidence only, **not** proof of worldwide novelty.

## 2. Frozen metric: before and after

The admission metric remains

`W_{1/4}=U_{1/4}-L_{1/4}`.

Run 3 saturated it by proving `theta_{2,1/4}=1/8`. Therefore this run must honestly report

`W_{1/4}: 0 -> 0`.

This is the **second consecutive no-movement run after saturation**, so Section I is not yet triggered under the track's retained counting convention. The full source obligation nevertheless moves substantively: two exact isolated H-values become exact open H-neighborhoods. I do not relabel that source progress as movement of the frozen metric.

## 3. New idea before checking: lock the reference exponent to the source lower bound

For `0<H<1/2`, Molchan's rigorous lower bound is

`theta_{2,H} >= H/2`.                                                    (3.1)

Fix `m in (0,1/2)` and define

`q(H)=4H/3`,   `c_m(H)=q(H)/m=4H/(3m)`.                                  (3.2)

Time-rescale Molchan's exactly solvable stationary reference:

`K_{m,H}(t)=K_m(c_m(H)t)`

`= cosh((1-2m)c_m(H)t/2) / cosh(c_m(H)t/2)`.                             (3.3)

Statement 1.4 and time scaling give its persistence exponent exactly:

`theta(K_{m,H})=(3/8)c_m(H)m=H/2`.                                       (3.4)

Thus, for every H where the all-lag covariance inequality

`R_H(t) >= K_{m,H}(t)  for all t>=0`                                    (3.5)

holds, ordinary Slepian comparison gives

`theta_{2,H} <= theta(K_{m,H})=H/2`,

which together with (3.1) forces

`theta_{2,H}=H/2`.                                                       (3.6)

The point of this run is to show that a **strict** comparison at one H, together with strict endpoint transversality, automatically persists for all nearby H. That converts the exact anchor calculations in runs 3--4 from isolated algebraic coincidences into open source regimes.

The previous suggested triple included B5/B30, but those moves had already been used on this problem in runs 1--2. The controlling directive asks for moves not previously tried, so this run instead uses the genuinely unused B21/B27/B29 triple.

## 4. B29 — add the points at infinity: compactify the lag obstruction

Let

`D_m(H,t)=R_H(t)-K_{m,H}(t)`.                                             (4.1)

Strict positivity at a single anchor H cannot be transferred by naive compactness on `(0,infinity)`, because `D_m(H,0)=0` and both covariances tend to zero at infinity. The right space has two boundary charts.

### 4.1 The t=0 chart

Runs 1--2 derived the exact source expansion

`R_H(t)=1-a(H)t^2+o(t^2)`,   `a(H)=(1-H^2)/2`.                            (4.2)

From (3.3),

`K_{m,H}(t)=1-b_m(H)t^2+O(t^4)`,

`b_m(H)=q(H)^2(1-m)/(2m)=8H^2(1-m)/(9m)`.                               (4.3)

Hence

`D_m(H,t)/t^2 -> g_m(H):=b_m(H)-a(H)` as `t downarrow 0`,                 (4.4)

with

`g_m(H)=((16-7m)H^2-9m)/(18m)`.                                         (4.5)

For fixed m,

`g_m'(H)=((16-7m)/(9m)) H > 0`.                                         (4.6)

The exact source covariance formula from run 1 also shows that `(H,t) -> D_m(H,t)/t^2` extends continuously to `t=0` on every compact H-interval inside `(0,1/2)`: the only nonanalytic source term is of order `t^(2H+2)`, and after division by `t^2` it is `O(t^(2H))`, uniformly vanishing when H is bounded away from zero.

Thus a strict condition `g_m(H0)>0` supplies a genuine open small-lag chart.

### 4.2 The t=infinity chart

For `0<H<1/2`, the exact covariance formula gives

`R_H(t) ~ A(H)e^(-Ht)`,   `A(H)=(H+1)/(2H+1)>0`.                         (4.7)

More precisely, on every compact `J=[h_-,h_+]` contained in `(0,1/2)`, the binomial expansion in `e^{-t}` is uniform and gives

`R_H(t)=A(H)e^(-Ht)(1+O_J(e^{-(1-2h_+)t}))`.                            (4.8)

The reference admits the exact exponential representation

`K_{m,H}(t)=[e^{-q(H)t}+e^{-(c_m(H)-q(H))t}]/[1+e^{-c_m(H)t}]`.          (4.9)

Since `m<=1/2`,

`0<K_{m,H}(t)<=2e^{-q(H)t}`.                                             (4.10)

But

`q(H)-H=H/3`.                                                            (4.11)

Therefore on a compact J around any positive anchor, the reference always decays uniformly faster than the source. Equations (4.8)--(4.11) give a T such that

`D_m(H,t)>0` for every `H in J` and every `t>=T`.                         (4.12)

This is the second boundary chart. In B29 language, after the natural renormalizations, both missing points `t=0` and `t=infinity` have strictly positive defects.

## 5. B27 — swap the quantifiers: from one H and every t to one neighborhood and every t

The useful statement is not merely

`for every t>0, there exists a neighborhood U_t of H0 with D>0`.

That pointwise assertion is too weak. What the source needs is the swapped, uniform form

`there exists one neighborhood U of H0 such that for every H in U and every t>0, D>0`.

The endpoint charts above make that quantifier swap possible.

### Lemma 1 — strict comparison is open in H

Fix `H0 in (0,1/2)` and `m in (0,1/2)`. Assume

1. `D_m(H0,t)>0` for every finite `t>0`; and
2. `g_m(H0)>0`.

Then there exists `delta>0` such that, for every

`H in (H0-delta,H0+delta) subset (0,1/2)`,                              (5.1)

we have

`R_H(t)>K_{m,H}(t)` for every `t>0`.                                     (5.2)

#### Proof

Choose a compact H-interval J about H0 contained in `(0,1/2)` and small enough that `g_m(H)>0` throughout J; this is possible by continuity and assumption 2.

**Small lags.** By the continuous extension in (4.4), there are `epsilon>0` and a smaller H-neighborhood `U_0` of H0 such that

`D_m(H,t)>0` for `H in U_0`, `0<t<=epsilon`.                             (5.3)

**Large lags.** Let `A_* = min_{H in J} A(H)>0`. Uniform asymptotic (4.8) gives T large enough that

`R_H(t) >= (A_*/2)e^{-Ht}`

for all `H in J`, `t>=T`. Equation (4.10), together with `q(H)-H=H/3>=h_-/3`, lets T be increased so that

`K_{m,H}(t) <= 2e^{-q(H)t} < (A_*/2)e^{-Ht} <= R_H(t)`                   (5.4)

for every `H in J`, `t>=T`.

**Middle lags.** At the anchor, assumption 1 and continuity give

`eta := min_{epsilon<=t<=T} D_m(H0,t) > 0`.                              (5.5)

Joint continuity of `D_m` on the compact rectangle near `{H0} x [epsilon,T]` yields a neighborhood `U_mid` on which

`D_m(H,t) > eta/2 >0` for all `epsilon<=t<=T`.                           (5.6)

Intersect `U_0`, `U_mid`, and J. Equations (5.3), (5.4), and (5.6) cover all `t>0` with one H-neighborhood. This proves the lemma. QED.

This is a theorem-sized analytic argument on the page; no finite checker is being substituted for it.

## 6. Apply Lemma 1 at the two exact anchors

### 6.1 Anchor H0=1/4

Run 3 proved the strict all-lag inequality

`R_{1/4}(t) > cosh(4t/3)/cosh(5t/3)` for every finite `t>0`.              (6.1)

This is exactly `K_{m,H0}` with

`m=1/10`, `q=1/3`, `c=10/3`.                                            (6.2)

The small-lag coefficients are

`a(1/4)=15/32`, `b_{1/10}(1/4)=1/2`,

so

`g_{1/10}(1/4)=1/32>0`.                                                  (6.3)

Equivalently, the explicit local condition (4.5) is `H^2>1/17`, and `1/16>1/17` strictly.

Lemma 1 therefore gives a number `delta_1>0` such that

`theta_{2,H}=H/2`

for every

`H in (1/4-delta_1,1/4+delta_1)`.                                       (6.4)

The interval is understood to lie inside `(0,1/2)`.

### 6.2 Anchor H0=1/3

Run 4 proved

`R_{1/3}(t) > cosh(8t/9)/cosh(4t/3)` for every finite `t>0`.              (6.5)

This is `K_{m,H0}` with

`m=1/6`, `q=4/9`, `c=8/3`.                                              (6.6)

Here

`a(1/3)=4/9`, `b_{1/6}(1/3)=40/81`,

so

`g_{1/6}(1/3)=4/81>0`.                                                   (6.7)

Equivalently the local condition is `H^2>9/89`, and `1/9>9/89` strictly.

Lemma 1 yields `delta_2>0` such that

`theta_{2,H}=H/2`

for every

`H in (1/3-delta_2,1/3+delta_2)`.                                       (6.8)

Again the interval lies in `(0,1/2)`.

### Theorem 2 — exact open source regimes

There exist `delta_1,delta_2>0` for which

`theta_{2,H}=H/2`

throughout the union

`(1/4-delta_1,1/4+delta_1) union (1/3-delta_2,1/3+delta_2)`.              (6.9)

This is strictly stronger than the two isolated exact values from runs 3--4. It remains PARTIAL for the full source function.

I deliberately do **not** report a numerical lower bound on `delta_1` or `delta_2`. The endpoint charts have explicit margins, but the compact middle-lag minimum in (5.5) has not been converted into a rigorous quantitative H-Lipschitz modulus. A sampled estimate of that minimum would not certify an interval width.

## 7. B21 — who else has this shape, and what is actually new here

The closest mechanism found in the current source is Molchan's own Lemma 1.5: it obtains persistence-exponent relations for a Gaussian family smoothly depending on a parameter and explicitly separates an intermediate lag window from small/large lag conditions. The closest fresh search hit outside the source was Aurzada--Bothe--Druet--Kettner--Profeta (arXiv:2407.06870), where a discrete MA(1) persistence exponent is handled through operator perturbation and the Slepian process.

That comparison changes how this run should be described:

- **Not novel in spirit:** parameter deformation, Slepian comparison, and endpoint/middle scale separation are established persistence techniques.
- **Source-specific candidate contribution:** the exact strict covariance certificates already proved here at `H=1/4` and `H=1/3`, combined with their strict quadratic and tail transversality, imply exact **open Hurst neighborhoods** by the elementary quantifier-swap lemma above.
- **Not claimed:** that no paper worldwide has observed this consequence; the literature search is bounded and negative only.

B21 therefore succeeded as a prior-art/method transfer: it identified the right conceptual framework and, equally importantly, prevented presenting the general scale-splitting mechanism as new.

## 8. Exact finite self-check

After the analytic idea and proof were written, I executed a small exact `Fraction` checker for the finite endpoint arithmetic only:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0040Z_open_neighborhoods_exact_check.py`

creation commit:

`be6c29b8557429bf41706c8f9c4f039fa0a174c5`.

Archived output:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0040Z_open_neighborhoods_exact_check.out`

creation commit:

`e51d7a603e00fe7869658c21ac3acd137d996954`.

It verifies exactly:

- at `(H,m)=(1/4,1/10)`, local margin `1/32`, reference exponent `1/8`, tail-rate margin `1/12`;
- at `(H,m)=(1/3,1/6)`, local margin `4/81`, reference exponent `1/6`, tail-rate margin `1/9`;
- the closed formula (4.5) at both anchors.

The executed output ends `ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check of finite arithmetic**, not an independent audit and not a substitute for Lemma 1's analytic proof.

## 9. What the three unused methods did

- **B21 — ask who else has this shape: succeeded.** Molchan's parameter-Slepian lemma and the MA(1) perturbation literature show that parameter deformation and scale separation are established machinery; the useful new step for this track is to apply that architecture to the exact strict anchors already certified here.
- **B27 — swap the quantifiers: succeeded.** The main theorem upgrades `for each t, nearby H works` to one uniform H-neighborhood that works for **all** lags, using endpoint transversality plus compactness on the middle scale.
- **B29 — add the points at infinity: succeeded.** Renormalizing by `t^2` at zero and by the exact exponential tail at infinity removes the two degeneracies that prevent naive compactness on `[0,infinity)`.

These are all new numbered moves for this target; I did not repeat any of the previously used B1/B2/B3/B4/B5/B6/B11/B13/B15/B17/B24/B30 moves.

## 10. Remaining obligation and next genuinely unused routes

The full source function remains open. This theorem does not show that the two exact neighborhoods overlap, does not quantify their widths, and does not cover arbitrary `H<1/2` or any `H>1/2` source value.

A high-value next run should not add another qualitative continuity lemma. The next unused triple should be **B16 / B19 / B26**:

- **B16** compute exact rational H-cases with the locked-exponent reference family and look for a repeatable algebraic pattern, but count only exact certificates, never grids;
- **B19** turn continuation in H into an algorithm whose stopping event is the first exact covariance contact `(H,t)` or loss of endpoint transversality;
- **B26** hunt a sporadic first-contact H where the continuation family genuinely fails, because that obstruction may identify the boundary of an exact interval.

If the frozen metric is again unchanged on the next run, the retained post-saturation no-movement streak reaches three and the following execution must obey the Section-I stuck protocol rather than manufacture another lemma.

## 11. Capability honesty

This runtime identifies the actual model as **GPT-5.6 Sol**. Reasoning effort is **UNVERIFIED**; no authenticated maximum-effort telemetry is exposed. The scheduler interface available to this task still exposes prompt/title/schedule/timing/enabled controls but no model selector or reasoning-effort selector, so GPT-6/maximum remains a text request rather than a verified setting. Changing that requires a platform/API surface that exposes authenticated model and effort controls.

The repository policy records historical `You cannot modify this task` failures for P26/P01/P03. The current root RESULTS ledger also records that P26 was later successfully updated in a different authorized native context, so I do **not** misstate the historical P26 denial as a proven current account-wide refusal. Where a native task genuinely refuses modification, the allowed remedy remains using the correct owning account/workspace or platform support; creating a duplicate task or bypassing permissions is not allowed. No scheduler was modified in this run.

## 12. ledger_delta

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  source_current_record: "arXiv:2509.10265; current PDF re-read 2026-09-19; prior checkpoint records v11 revised 2026-07-04"
  status: PARTIAL
  source_full_problem: OPEN
  metric: W_{1/4}
  before: 0
  after: 0
  movement: "no"
  post_saturation_no_movement_streak: 2
  methods: [B21, B27, B29]
  new_result: "There exist delta_1,delta_2>0 such that theta_{2,H}=H/2 on open neighborhoods of H=1/4 and H=1/3, via strict covariance-comparison openness with endpoint transversality."
  anchor_1_local_margin: 1/32
  anchor_2_local_margin: 4/81
  exact_checker_commit: be6c29b8557429bf41706c8f9c4f039fa0a174c5
  exact_output_commit: e51d7a603e00fe7869658c21ac3acd137d996954
  exact_output_tail: ALL_EXACT_CHECKS_PASS
  quantitative_delta_certified: false
  independent_audits: 0
  closure: false
  next_methods: [B16, B19, B26]
```
