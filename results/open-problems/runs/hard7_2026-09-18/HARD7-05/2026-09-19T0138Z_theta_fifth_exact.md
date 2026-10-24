Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 frozen metric no movement: `W_{1/4}=0 -> 0`; methods B7 / B16 / B18. Substantive source progress: exact third special point `theta_{2,1/5}=1/10`, hence by the previous openness lemma an additional nonempty open H-neighborhood on which `theta_{2,H}=H/2`.**

# HARD7-05 run 6 — exact third rational point `H=1/5` and a new global route

Status: **PARTIAL for the full Molchan source problem.** The source asks for the full function `H -> theta_{2,H}` on `0<H<1`, `H != 1/2`. The fixed admission metric was already saturated in run 3 and therefore cannot honestly move further. This run nevertheless proves a new source-valid exact value and exposes a broader scalar-inequality route that could cover the whole subcritical Hurst half-interval.

## 1. Repository continuity, source status, ownership, scheduler capability

I resumed the exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`, and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-05/2026-09-19T0040Z_exact_open_neighborhoods.md`.

Before new mathematics I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the canonical claim and all five earlier HARD7-05 reports;
- the newest neighboring HARD7-04 and HARD7-06 directory/report state;
- targeted claim/intake/repository searches for `2509.10265`, the exact Molchan title, integrated-fBM persistence aliases, and the exact rational point `H=1/5`.

As in the preceding run, the large `probability_1000_intake_*/problems.jsonl` files are not literally renderable in full through this connector without truncation; I performed the source/alias/claim-targeted intake reread rather than falsely claiming a byte-for-byte scan. No release, duplicate owner, posted equivalent, or canonical collision was found.

The primary source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265. The current source version retained by this track is v11, revised 4 July 2026; printed p. 3 still leaves the `alpha=2`, `H != 1/2` exponent values unsolved and gives the lower bound

`theta_{2,H} >= (1/2)(H min (1-H))`.

Fresh bounded web/arXiv searches dated 19 September 2026 for the exact title/identifier, `theta_{2,1/5}`, `H=1/5 integrated fractional Brownian persistence exponent`, `integrated fractional Brownian 1/10 persistence`, and the comparison covariance used below found Molchan's current paper, Aurzada--Kilian's asymptotic work, numerical fractional-integration papers, and adjacent Gaussian-persistence literature, but no exact published value at `H=1/5` and no later full solution of `theta_{2,H}`. This is bounded negative evidence only, **not** proof of worldwide novelty.

The scheduler capability statement is unchanged. The exposed automation control surface has title/prompt/schedule/timing/enabled controls, but no bindable model-family selector, no reasoning-effort selector, and no guaranteed execution duration. GPT-6/maximum is therefore still prompt text only. Historical scheduler probes returning `You cannot modify this task` are permission/ownership failures; the authorized workaround is resolving task/workspace ownership through the proper interface or platform support, not duplicating the schedule or bypassing permissions. Root `RESULTS.md` records that some later P26 edits succeeded in another authorized context; that does not create a model/reasoning selector here. No scheduler was modified in this run.

## 2. Frozen metric: before and after

The admission metric remains

`W_{1/4}=U_{1/4}-L_{1/4}`.

Run 3 proved `theta_{2,1/4}=1/8`, so the bracket width is already zero. Hence this run honestly reports

`W_{1/4}: 0 -> 0`.

This is the **third consecutive no-movement run after saturation** (runs 4, 5, and this run). Therefore the Section-I stagnation trigger is now reached: the **next invocation must be a STUCK1 thinking/recovery run**, with the five required obstruction items and exactly one recovery choice, rather than another ordinary theorem increment. The exact `H=1/5` theorem below is genuine source progress but is not relabeled as movement of the frozen metric.

## 3. B7 — take the comparison-family limit first

For `0<H<1/2`, the source lower bound is

`theta_{2,H} >= H/2`.

Molchan's exactly solvable stationary comparison family has covariance

`K_m(s)=cosh((1-2m)s/2)/cosh(s/2)`, `0<m<=1/2`,

and persistence exponent `3m/8`. To force the time-rescaled reference to have exponent exactly `H/2`, set

`q(H)=4H/3`, `c=q/m`.

Then

`K_{m,H}(t)=K_m(c t)`

has persistence exponent `(3/8)cm=H/2`.

For fixed `H` and `t>0`, writing `s=q(H)t` gives the exact formula

`K_{m,H}(t)=e^{-s}(1+e^{2s}e^{-s/m})/(1+e^{-s/m})`.

Therefore

`K_{m,H}(t) -> e^{-q(H)t}` as `m downarrow 0`

for every fixed `t>0`.

This suggests a global route not used in the earlier rational-point proofs: first compare the source covariance to the simple limiting exponential kernel, and only then move back to a small positive `m`, where the persistence exponent remains exactly `H/2`.

The route has the correct endpoint geometry. At small lag,

`R_H(t)=1-(1-H^2)t^2/2+o(t^2)`

whereas for fixed positive `m`,

`K_{m,H}(t)=1-[q(H)^2(1-m)/(2m)]t^2+O(t^4)`.

Thus choosing `m` sufficiently small makes the reference drop faster quadratically. At large lag,

`R_H(t) ~ ((H+1)/(2H+1))e^{-Ht}`,

while `K_{m,H}(t) <= 2e^{-q(H)t}` for `m<=1/2`; since `q(H)-H=H/3>0`, the reference decays strictly faster. On every fixed middle-lag compact interval, `K_{m,H}` converges uniformly to `e^{-q(H)t}` as `m downarrow0`.

Consequently, if one can prove the strict scalar covariance inequality

`R_H(t) > e^{-4Ht/3}` for every `t>0`,

then compactness plus the two endpoint charts gives some `m(H)>0` such that

`K_{m(H),H}(t) <= R_H(t)` for all `t>=0`,

and Slepian would force `theta_{2,H}=H/2`.

I do **not** claim this strict exponential inequality for all `H` in this run. It is the new global route generated by B7.

## 4. B18 — say the global route as a two-variable real inequality

Let `p=2H in (0,1)` and `x=e^{-t} in (0,1)`. From the exact Lamperti covariance formula established in run 1, the unproved global comparison

`R_H(t) >= e^{-4Ht/3}`

is equivalent to

`F_p(x) >= 0` for `0<p<1`, `0<x<1`,

where

`F_p(x) = (p+2)(x+x^(p+1)) - 1 - x^(p+2) + (1-x)^(p+2) - 2(p+1)x^(1+7p/6)`.

This translation removes the Gaussian-process language from the remaining all-H obstruction: the entire `0<H<1/2` comparison route would follow from one explicit two-variable scalar inequality with no hidden probabilistic quantifiers.

The boundary signs are favorable:

- `F_p(0)=F_p(1)=0` in the continuous boundary sense;
- as `x downarrow0`, the leading interior term is `(p+2)x^(p+1)>0`;
- differentiating the regular terms at `x=1` gives an inward linear margin `4p(p+1)(1-x)/3`.

A numerical stress test was used only to search for counterexamples and found none on the tested grid; it is **not** used as proof or metric movement. The unresolved obligation is a uniform analytic sign argument in `(p,x)`, not more finite sampling.

## 5. B16 — compute the next simplest rational case exactly: `H=1/5`

The simplest unproved rational anchor below the already solved `1/4` is `H=1/5`. Here `p=2/5`. Choose

`m=1/20`, `q=4/15`, `c=q/m=16/3`.

The comparison process is therefore

`K(t)=cosh(12t/5)/cosh(8t/3)`,

and its exact persistence exponent is

`(3/8) c m = 1/10`.

The source lower bound already gives

`theta_{2,1/5} >= 1/10`.

It remains to prove `R_{1/5}(t)>=K(t)` for every lag.

### Theorem 1 — exact all-lag covariance comparison at `H=1/5`

For every `t>=0`,

`R_{1/5}(t) >= cosh(12t/5)/cosh(8t/3)`,

with strict inequality for every finite `t>0`.

### Proof

Set

`x=e^{-t/15} in (0,1]`.

The exact general Lamperti covariance specializes to

`R_{1/5}(t) = [5(1-x^15)^(12/5) + 12x^15 + 12x^21 - 5 - 5x^36]/(14x^18)`.

The reference becomes

`K(t)=x^4(1+x^72)/(1+x^80)`.

All denominators are positive. Thus `R>=K` is equivalent to

`A(x)+P(x) >= 0`,

where

`A(x)=5(1+x^80)(1-x^15)^(12/5)`

and

`P(x)=(1+x^80)(12x^15+12x^21-5-5x^36)-14x^22(1+x^72)`.

If `P(x)>=0`, the inequality is immediate and strict for `0<x<1` because `A(x)>0`.

Assume `P(x)<0`. Since both `A(x)` and `-P(x)` are positive, fifth powers preserve their order. Define the exact integer polynomial

`D(x)=5^5(1+x^80)^5(1-x^15)^12 + P(x)^5`.

The archived exact checker verifies the factorization

`D(x)=x^21(1-x)^10 Q(x)`,

where `Q` is a reciprocal integer polynomial of degree `528`:

`Q(x)=x^528 Q(1/x)`.

Hence there is an integer polynomial `q` of degree `264` such that

`Q(x)=x^264 q(x+x^(-1))`.

Put

`z=x+x^(-1)-2 >= 0`.

The exact transformed polynomial has the form

`q(z+2)=a_0+a_1 z+a_2 z^2 + sum_{j=3}^{264} a_j z^j`,

and the checker proves that the **only** nonpositive shifted coefficient is the linear one. In particular,

`a_0 = 2838268904210432`,

`a_1 = -4067719593213309280`,

`a_2 = 90615428800534584977920`,

all `a_j>0` for `j>=2`, and

`a_1^2-4a_0a_2 = -1012217472535995417806624878614080527360 < 0`.

Therefore the quadratic

`a_0+a_1 z+a_2 z^2`

is strictly positive for every real `z`, because `a_2>0` and its discriminant is negative. Adding the terms `a_j z^j` for `j>=3` preserves strict positivity for `z>=0`. Hence

`q(z+2)>0`, so `Q(x)>0` for every `x>0`.

For `0<x<1`, the factors `x^21` and `(1-x)^10` are strictly positive, hence `D(x)>0`. On the branch `P(x)<0`, this says

`A(x)^5 > (-P(x))^5`,

so `A(x)>-P(x)`, i.e.

`A(x)+P(x)>0`.

Thus `R_{1/5}(t)>K(t)` for every finite `t>0`; at `t=0` both covariances equal one. QED.

The argument is continuous-path and all-lag. No discretized persistence path, finite-t grid, or approximate root location is used.

## 6. Exact persistence consequence

Both stationary Gaussian processes are centered and variance one. Theorem 1 gives the covariance order

`K(t) <= R_{1/5}(t)` for every `t`.

Slepian comparison in the same direction used in Molchan's paper and in runs 3--5 gives

`theta_{2,1/5} <= theta(K)=1/10`.

Together with Molchan's lower bound

`theta_{2,1/5} >= 1/10`,

we obtain the exact source value

`theta_{2,1/5}=1/10`.

This is a third exact rational point for the source function, after `H=1/4` and `H=1/3`. It is still only PARTIAL for the source's complete `H`-range.

## 7. Immediate open-neighborhood corollary from run 5

Run 5 proved a general openness lemma: if at an anchor `H_0<1/2` one has strict all-lag domination by a fixed-exponent Molchan reference and a strict positive small-lag margin

`g_m(H_0)=((16-7m)H_0^2-9m)/(18m)>0`,

then the equality `theta_{2,H}=H/2` persists on a nonempty open H-neighborhood of `H_0`.

For the present anchor `H_0=1/5`, `m=1/20`, exact arithmetic gives

`g_{1/20}(1/5)=44/225>0`.

Therefore there exists `delta_3>0` such that

`theta_{2,H}=H/2`

for every

`H in (1/5-delta_3,1/5+delta_3)`.

Combined with run 5, the track now has three nonempty open exact regimes centered at `1/5`, `1/4`, and `1/3`. No numerical width is claimed for any of these intervals.

## 8. Exact checker and archived output

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0138Z_theta_fifth_exact_check.py`

creation commit:

`e0ab79310ca6c8f22c1a1595651c259c50cb6cc0`.

Executed output:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0138Z_theta_fifth_exact_check.out`

creation commit:

`83afcd883c8de0eda496862296a153c68bb75055`.

The exact output was read back and ends

`ALL_EXACT_CHECKS_PASS`.

It verifies the degree-559 fifth-power defect, the exact `x^21(1-x)^10` factor, reciprocal degree-528 quotient, the degree-264 reciprocal reduction, the shifted coefficient sign pattern, the negative quadratic discriminant, the exact reference exponent `1/10`, and the small-lag margin `44/225`.

This is a self-check of the finite algebraic core, not an independent audit.

## 9. What the three new-method moves did

- **B7 (take the limit): productive.** The fixed-exponent comparison family has a singular `m downarrow0` limit `e^{-4Ht/3}`. Proving source covariance domination of this exponential kernel would, by endpoint compactness, generate a positive-m comparison and hence `theta_{2,H}=H/2`.
- **B18 (say it in another language): productive but incomplete.** The all-`H<1/2` route reduces to the explicit two-variable inequality `F_p(x)>=0` displayed in Section 4. This is now the cleanest global obstruction; it remains unproved.
- **B16 (compute the next exact small case): succeeded.** The `H=1/5` comparison collapses after a fifth-power transform to a reciprocal polynomial whose shifted quotient has one negative linear coefficient dominated by a positive quadratic of negative discriminant. This yields the exact source value `theta_{2,1/5}=1/10`.

## 10. Status, closure, and mandatory next-run protocol

Status remains **PARTIAL / source OPEN**. Nothing here proves the complete `H`-dependence, and no independent audits are claimed. Bounded searches finding no prior exact `H=1/5` result do not establish novelty.

The frozen metric has now failed to move for three consecutive runs because it was already saturated. Under Section I, the **next HARD7-05 run must be STUCK1 and must not merely add another rational-point lemma**. It must write the required five-part stuck analysis: exact blocking statement, every route tried and failure reason, missing ingredient, simplest special case still unproved, and nearest solved analogue. It must then choose exactly one recovery action.

The strongest candidate blocking statement exposed by this run is

`F_p(x) >= 0  for all 0<p<1, 0<x<1`,

with `F_p` as in Section 4. A proof would settle the fixed-exponent comparison route across the whole `0<H<1/2` half-interval after the B7 compactness step. The next run should decide whether to make that inequality the recovery target or deliberately abandon the comparison family.

Suggested unused method triple for the STUCK1 analysis: **B8 / B22 / B28**.

## 11. ledger_delta

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  source_current_version: "arXiv:2509.10265v11, revised 2026-07-04"
  status: PARTIAL
  source_full_problem: OPEN
  metric: W_{1/4}
  before: 0
  after: 0
  movement: "no movement"
  consecutive_no_movement_after_saturation: 3
  methods: [B7, B16, B18]
  new_result: "theta_{2,1/5}=1/10 via exact all-lag domination by cosh(12t/5)/cosh(8t/3); by run-5 openness, equality theta_{2,H}=H/2 also holds on a nonempty open neighborhood of H=1/5"
  exact_points_retained: ["1/5 -> 1/10", "1/4 -> 1/8", "1/3 -> 1/6"]
  global_route_obstruction: "prove F_p(x)>=0 for 0<p<1, 0<x<1, or abandon the fixed-exponent comparison family"
  exact_checker_commit: e0ab79310ca6c8f22c1a1595651c259c50cb6cc0
  exact_output_commit: 83afcd883c8de0eda496862296a153c68bb75055
  exact_output_tail: ALL_EXACT_CHECKS_PASS
  independent_audits: 0
  section_I_next: STUCK1
  next_methods: [B8, B22, B28]
  closure: false
```
