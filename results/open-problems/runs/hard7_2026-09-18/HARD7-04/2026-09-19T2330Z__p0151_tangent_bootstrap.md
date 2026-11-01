Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: certified lower exponent **`b1 -> b2`**, where `b2=[m+m*pi_c*(m+delta)]/(2m+delta)>b1`; methods actually used: **B5 / B12 / B20**.

# HARD7-04 bounded research iteration — tangent-coefficient bootstrap for fixed-outdegree PA critical percolation

Status: **PARTIAL / SOURCE OPEN**. No closure claim. No simulation is used as proof. No exact-arithmetic checker was created because this run's substantive claim is an analytic theorem with its proof written below, not a finite certificate.

## 1. Continuity, repository state, and source/current-literature check

I resumed the exclusively claimed `P0151` target from `operations/claims/P0151.md` and the immediately preceding HARD7-04 report `2026-09-19T2228Z__bhs_handoff_p0151_block_activation.md`; I did not restart from the older P0157 / van-der-Hofstad / BHS-MST lines. Before doing mathematics I reread the required control surfaces: `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` / `RANKING.md`, root `POSTED.md` / `RESULTS.md` / `QUEUE.md`, the P0151 intake/catalog aliases, and the neighboring preferential-attachment status report `runs/R08/20260917T223457Z_rotation_preferential_attachment_status_5d8c41.md`. Repository searches still show `P0151` owned by `HARD7-04`; I found no conflicting canonical owner.

The frozen model remains Ray's sequential fixed-outdegree affine preferential-attachment model `PA_n^(m,delta)(d)` with fixed `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges from every arriving vertex, and independent bond retention `pi` after graph generation. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, EJP 31 (2026), arXiv:2312.14085, prove the threshold

`pi_c = delta / ( 2*( m*(m+delta) + sqrt(m*(m-1)*(m+delta)*(m+1+delta)) ) )`.

A fresh bounded literature search through **2026-09-20 local date** checked the exact fixed-outdegree phrases together with the current neighboring critical-window papers. It recovered:

- Hazra--van der Hofstad--Ray, arXiv:2312.14085 / EJP 2026: threshold and giant/no-giant dichotomy for the exact affine PA model; no finite-size critical-window theorem located. The paper's model-(d) discussion still distinguishes the fixed-edge sequential dependence from independently attached edges. URL: `https://arxiv.org/abs/2312.14085`.
- Jorritsma--Maillard--Mörters, arXiv:2512.18937 (2025): `(log n)^(-2)` critical window and `sqrt(n)/log n` largest-component scale for sparse growing graphs with **independent connections to earlier vertices**. URL: `https://arxiv.org/abs/2512.18937`.
- Mörters--Schätze, arXiv:2606.27844 (2026): critical percolation for an **inhomogeneous random graph with a preferential-attachment kernel in the infinite-variance regime**, not this fixed-`m`, `delta>0` sequential ensemble. URL: `https://arxiv.org/abs/2606.27844`.
- Eckhoff--Mörters--Ortgiese (2018), *Near Critical Preferential Attachment Networks have Small Giant Components*: near-critical asymptotics for a different independent-edge attachment-rule model; not a source-matching finite-size theorem for `PA^(m,delta)(d)`.

This is bounded negative evidence only; it is **not** a worldwide novelty certificate.

## 2. Frozen quantity and before/after

Let `C_max(n,pi_c)` be the largest percolation component at the exact threshold and define

`gamma_E := liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

Write

`A := 2m+delta`,
`q(pi) := 1-(1-pi)^m`.

The previous run proved

`gamma_E >= b1 := [m+(m+delta) q(pi_c)]/A`.

That is the **before** value for this run.

This run proves the stronger bound

`gamma_E >= b2 := [m+m*pi_c*(m+delta)]/A`.                         (2.1)

Because `m*pi > 1-(1-pi)^m` for `m>=2` and `0<pi<1`,

`b2>b1`.                                                            (2.2)

The exact threshold formula also gives

`pi_c < delta/[2m(m+delta)]`,

hence

`b2 < 1/2`.                                                         (2.3)

Thus the frozen metric moves strictly, but a positive power gap to the neighboring independent-edge `1/2` critical exponent remains.

For orientation only, not proof: when `m=2, delta=1`, `pi_c≈0.04587585477`, `b1≈0.4537882693`, while `b2≈0.4550510257`.

---

# 3. B20 — find why the obvious tangent argument fails

The preceding block-activation proof used the global chord

`1-(1-pi x)^m >= q(pi) x`, `0<=x<=1`,

which produces `b1`. The tempting stronger argument replaces the chord coefficient `q(pi)` by the tangent coefficient `m*pi`, since

`1-(1-pi x)^m = m*pi*x + O(x^2)` as `x->0`.

The obstruction is exact: without quantitative control of the quadratic defect, the step

`E f(W_t/t) ~ m*pi E W_t/t`

is invalid. A small mean of `W_t/t` alone does not rule out rare states with macroscopic shadow attractiveness. So the tangent coefficient cannot be inserted merely by saying that the critical component is sublinear.

The useful form of the obstruction is the second-order lower Taylor bound

`f(x):=1-(1-pi x)^m >= m*pi*x - C2*pi^2*x^2`,                      (3.1)

where `C2=binom(m,2)`. For `m>=3`, this follows from `f'''(x)>=0` on `[0,1]`; for `m=2` it is equality. Therefore the tangent route will close if one proves

`E W_t^2 = O(t)`.                                                   (3.2)

Outcome of B20: the previous qualitative obstruction is reduced to a concrete second-moment statement.

---

# 4. B12 — deterministic attractiveness conservation gives the missing second moment

Retain the previous run's shadow connected set `Q_t`, attractiveness

`W_t := sum_{u in Q_t}(d_u(t)+delta)`,

number of shadow vertices `N_t:=|Q_t|`, number `H_t` of the new vertex's `m` target hits in the frozen old set `Q_t`, and activation indicator `I_t` that at least one such hit is retained. The exact identity remains

`W_{t+1}=W_t+H_t+(m+delta) I_t`.                                   (4.1)

Put `Delta_t:=W_{t+1}-W_t`. Deterministically,

`0<=Delta_t<=m+(m+delta)=A`.                                       (4.2)

The total old-vertex attractiveness in the fixed-outdegree affine model is linear in `t`. Consequently there is a fixed `K` such that, for every sufficiently large `t` and every one of the `m` attachment trials in the next birth, its eligible denominator lies in

`[At-K, At+K]`.                                                     (4.3)

This is exactly the denominator control used in the preceding report; no asymptotic model replacement is being made.

For an **upper** drift estimate, during the birth the shadow numerator can increase by at most one per previous hit. Hence

`E[H_t | F_t] <= m(W_t+m)/(At-K)`.                                  (4.4)

Conditional on the targets, a union bound over retained hits gives

`P(I_t=1 | targets,F_t) <= pi H_t`.

Therefore

`E[Delta_t | F_t]
 <= [1+pi(m+delta)] E[H_t|F_t]
 <= r W_t/(At-K) + C/t`,                                           (4.5)

where

`r := m[1+pi(m+delta)]`.                                            (4.6)

Now square (4.1). Using `Delta_t<=A`, (4.5), and the deterministic bound `W_t<=At+K`,

`E[W_{t+1}^2 | F_t]
 <= W_t^2 + 2W_t( r W_t/(At-K)+C/t ) + A^2
 <= [1+2r/(At-K)] W_t^2 + C_0`.                                   (4.7)

Specialize now to `pi=pi_c`. Define

`b2:=r/A`.

By (2.3), `2b2<1`. Choose `a` with `2b2<a<1`. For all sufficiently large `t`,

`2r/(At-K) <= a/t`.

Taking expectations in (4.7) gives, with `Y_t:=E W_t^2`,

`Y_{t+1} <= (1+a/t)Y_t + C_0`.                                     (4.8)

A one-line induction yields

`Y_t <= C_1 t`.                                                     (4.9)

Indeed, if `Y_t<=Dt`, then the right side of (4.8) is at most `Dt+aD+C_0`, which is at most `D(t+1)` once `D(1-a)>=C_0`; enlarge `D` to absorb the finite initial segment.

Outcome of B12: **the exact linear total-attractiveness budget plus `b2<1/2` controls the rare large-shadow states strongly enough: `E W_t^2=O(t)`**.

---

# 5. B5 — interpolate the activation law and bootstrap from chord to tangent

We now use the parameter `x=W_t/(At+K)` inside the exact activation law rather than freezing it at the global chord.

As in the preceding report, conditional on `F_t`, every one of the `m` sequential trials has retained-hit probability at least

`pi W_t/(At+K)`

even after conditioning on no earlier retained hit. Therefore

`E[I_t|F_t] >= f(W_t/(At+K))`,

where `f(x)=1-(1-pi x)^m`. Combining (3.1) with the lower target-hit bound

`E[H_t|F_t] >= m W_t/(At+K)`

and (4.1) yields

`E[W_{t+1}|F_t]
 >= W_t + r W_t/(At+K)
    - d W_t^2/(At+K)^2`,                                           (5.1)

where

`d:=(m+delta) binom(m,2) pi^2`.                                    (5.2)

At `pi=pi_c`, take expectations and use (4.9): for `mu_t:=E W_t`,

`mu_{t+1} >= [1+r/(At+K)] mu_t - C_2/t`.                           (5.3)

The additive error looks dangerous, but the previous run's strictly positive chord exponent is exactly enough to seed the bootstrap.

Let

`G_{t+1}:=G_t[1+r/(At+K)]`, with `G_{t0}=1`.

Then standard product asymptotics give

`G_t = Theta(t^{r/A}) = Theta(t^{b2})`.                             (5.4)

Divide (5.3) by `G_{t+1}`:

`mu_{t+1}/G_{t+1} >= mu_t/G_t - C_3 t^{-1-b2}`.                    (5.5)

The tail of the error series after time `T` is `O(T^{-b2})`.

From the preceding block-activation theorem there are constants `c>0,T_0` with

`mu_T >= c T^{b1}`                                                  (5.6)

for all `T>=T_0`, where `b1>0`. By (5.4),

`mu_T/G_T >= c' T^{b1-b2}`.                                        (5.7)

Although `b1<b2`, the normalized seed in (5.7) dominates the remaining normalized error, because

`T^{b1-b2} / T^{-b2} = T^{b1} -> infinity`.                        (5.8)

Choose one fixed sufficiently large `T` so that the seed is more than twice the entire tail error in (5.5). Iterating (5.5) then gives a fixed `c_T>0` with

`mu_n >= c_T G_n >= c_4 n^{b2}`                                    (5.9)

for all `n>=T`.

Finally, the globally valid chord bound from the previous run still gives

`E[N_{t+1}-N_t]
 = E I_t
 >= q(pi_c) E W_t/(At+K)
 >= c_5 t^{b2-1}`.                                                  (5.10)

Summing (5.10),

`E N_n >= c_6 n^{b2}`.                                              (5.11)

By construction `Q_n` is contained in the true percolation component of the initial vertex, which is no larger than the largest component. Hence

`E|C_max(n,pi_c)| >= c_6 n^{b2}`,

and therefore

`gamma_E >= b2`.                                                    (5.12)

This proves (2.1).

### Strict improvement and remaining gap

For `m>=2` and `0<pi_c<1`, strict Bernoulli union inequality gives

`1-(1-pi_c)^m < m*pi_c`,

so `b2>b1`. Also the exact threshold has a strictly positive square-root term in its denominator, hence

`m*pi_c*(m+delta) < delta/2`,

which is equivalent to `b2<1/2`.

Outcome of B5: **the tangent coefficient is rigorously attainable at criticality; the quadratic activation defect is summable after a second-moment bootstrap**.

---

# 6. What this does and does not establish

**Established in this run:** for the exact fixed-`m`, sequential affine preferential-attachment model at its EJP-identified positive bond-percolation threshold,

`gamma_E >= [m+m*pi_c*(m+delta)]/(2m+delta)`.

This strictly improves the previous HARD7-04 certified lower exponent.

**Not established:** a matching upper bound, `gamma_E=1/2`, the `(log n)^(-2)` window, `sqrt(n)/log n` component size, tightness, or a distributional scaling limit. In particular, this run does not transfer the Jorritsma--Maillard--Mörters theorem from its independent-edge model to the exact fixed-outdegree sequential model.

The remaining structural obstruction is now sharper: the one-vertex shadow exploration saturates at the tangent exponent `b2<1/2`. To reach `1/2`, a new route must use information not present in the first-moment attractiveness recursion — likely a multi-seed / two-sided exploration or the spectral eigenfunction of the Pólya-point-tree offspring operator rather than a single connected shadow set.

## 7. Method accounting

- **B20 FIND WHY THE ALGORITHM FAILS:** isolated the exact quadratic loss preventing the naive tangent substitution.
- **B12 FIND WHAT IS CONSERVED:** used deterministic linear total attractiveness and bounded birth increments to prove `E W_t^2=O(t)` at criticality.
- **B5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** used the second-order expansion of the block activation law to upgrade the global chord coefficient to the tangent coefficient `m*pi_c`.

This triple is different from the previous run's `B2/B7/B19`.

## 8. Prior-art / novelty caution

Searches used the exact source model name, `fixed outdegree preferential attachment critical window`, `critical percolation preferential attachment m edges component size`, the EJP threshold paper and its model-(d) discussion, arXiv:2512.18937, arXiv:2606.27844, and the 2018 near-critical PA paper. I did not locate the exponent (2.1) or this second-moment/tangent bootstrap in those bounded searches. That does **not** establish novelty. The theorem is a self-derived **PARTIAL** result and has no independent other-track audits.

## 9. Scheduler / model-control honesty

The exposed automation schema in this runtime still has no model-family selector or reasoning-effort selector; it offers prompt/schedule/timing/enabled controls only. Therefore GPT-6 / maximum remains prompt-requested, while this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

No scheduler modification was attempted, because HARD7-04 is explicitly forbidden from modifying or creating other schedules. Repository records are context-dependent: `NEW_METHODS_2026-09-16.md` records earlier `You cannot modify this task` probes for P26/P01/P03, while the newer compact `RESULTS.md` records a later authorized context in which a P26 prompt update succeeded. Accordingly I do **not** claim P26 is currently modifiable or unmodifiable from this runtime. The permitted workaround for a genuine native permission denial remains the authorized owning account/workspace/interface or platform support; duplicating the task or editing GitHub is not a scheduler repair.

## 10. Structured checkpoint / ledger delta

```yaml
ledger_delta:
  track: HARD7-04
  source: P0151
  status: PARTIAL
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  methods: [5, 12, 20]
  metric: gamma_E_lower_bound
  before: "b1 = [m+(m+delta)*(1-(1-pi_c)^m)]/(2m+delta)"
  after: "b2 = [m+m*pi_c*(m+delta)]/(2m+delta)"
  movement: STRICT
  theorem_core:
    - "E W_t^2 = O(t) at pi=pi_c"
    - "quadratic activation defect is summable after normalization"
    - "E|C_max(n,pi_c)| >= c n^b2"
  source_closed: false
  independent_audits: 0
  next_obstruction: "single-shadow tangent exponent b2 remains strictly below 1/2"
  next_candidate_moves: [11, 18, 25]
```

Next run should not repeat `B5/B12/B20`. A promising different triple is **B11** (use the EJP offspring-operator eigenfunction as a dual weight), **B18** (translate the finite exploration into the Pólya-point-tree spectral language), and **B25** (count the same two-seed exploration both by vertex mass and eigenfunction mass).
