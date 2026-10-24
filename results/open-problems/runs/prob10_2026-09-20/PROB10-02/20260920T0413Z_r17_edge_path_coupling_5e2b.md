Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but no authenticated model/effort selector or applied-effort receipt is exposed here, so I do not claim otherwise. **NO R17 SOURCE-ENDPOINT MOVEMENT THIS RUN:** with the newest companion P02 Farey--Collatz endpoint taken as the before-run baseline, the repository-internal deterministic interval remains `L <= gamma_2 <= U_F`, hence `W_before = W_after = U_F-L`; status **OPEN / PARTIAL**. The three new attacks were: (1) exact single-defect edge-chain/path coupling, (2) a position-only contraction dual, which is refuted exactly, and (3) exact multi-step block contraction on the edge chain.

# PROB10-02 / R17 — single-defect edge chain, path coupling, and a finite-horizon Bellman error

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. The whole construction below retains the genuine dependent match array: in each update the same fresh source bit is compared against the entire current raw-letter window. No independent Bernoulli matching surrogate and no simulation confidence interval is used.

## 0. Continuity, ownership, handoff, and current source metric

The owner-required H0021 handoff is already complete and is not rewritten here. The canonical file

`operations/claims/H0021.md`

still says `UNASSIGNED (released by R17 under later owner refocus)`, preserves the R16/R17 failure counters, preserves R17's H0021 report

`runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`

and navigation commit `c8891869a1335d67bada83f23f63f2ce09603565`, and leaves the H0021 metric at `Delta_near=2`. No H0021 claim or artifact is touched in this run.

The newest completed own PROB10-02 report before this run is

`runs/prob10_2026-09-20/PROB10-02/20260920T0320Z_r17_disagreement_flux_dual_d7c9.md`

(blob `1835a0c0db8271167d825666760473829e757e57`). It proved an exact synchronous disagreement-flux identity and finite joint-chain coalescence bounds. The old pre-refocus R17 LCS lifecycle and its failed routes remain preserved, including terminal handoff C050. In particular C033--C035 remain withdrawn after the complement-gauge error and are not reused.

Current same-source ownership is complementary rather than duplicative. Under `operations/PROGRESS20_2026-09-20.md` (blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`), P02 owns the covering/cone stationary-variational route and P13 owns the boundary-recursion/reset route. R17 here attacks the history-coupled finite-state error problem left by its previous report.

The newest P02 report recovered before doing new mathematics is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T04-03-12Z__farey-collatz-dual-report.md`

(blob `7f75484503fa5534cf357738df36fac84ace033f`). It strictly improves the preceding P02 upper endpoint. Retain
\[
L=\frac{99083249}{125000000}=0.792665992
\]
and denote P02's exact Farey--Collatz endpoint by
\[
U_F=\frac{\log(4t^2)}{\log\lambda_F},\qquad t=\frac{256717}{800000},
\]
with the exact rational `lambda_F` specified and checked in that report. Its diagnostic expansion begins
\[
U_F=0.82627594276228262501510658153729663282346199619319002388080618\ldots.
\]
Thus the source-level metric before and after **this R17 run** is
\[
\boxed{W_{\rm before}=W_{\rm after}=U_F-L}
\]
with diagnostic beginning
\[
0.03360995076228262501510658153729663282346199619319002388080618\ldots.
\]
The P02 strict improvement occurred between R17 runs and is credited to P02; this run does not claim it as R17 movement.

The newest P13 report recovered is

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T03-03-05Z__one-defect-reset-exact-error.md`

(blob `2040446847b5594df0dd9d44ef64fd89bc3afab6`). It proves a larger synchronizing-word family with reset waiting mean `(8*4^m+10)/21` for `m>=3`. The present route is different: it does not wait for a prescribed reset word, but follows every possible survival trajectory of a single discrepancy.

`POSTED.md` was checked (blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`); this exact LCS target is not a posted exclusion.

Fresh source/status checking on 20 September 2026 still finds the exact binary coefficient unresolved. Tiskin, arXiv:2212.01582v2 (revised 13 August 2024), explicitly says the problem remains unresolved and that incorrect claims in the earlier preprint were removed. Those withdrawn claims are not used. Heineman--Miller--Reichman--Salls--Sárközy--Soiffer give the retained lower endpoint `0.792665992`. A bounded current search found no later primary-source exact determination; this is status evidence, not a priority certificate.

## 1. Idea before code and three attacks

The new idea was written before checker code at

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0413Z_r17_edge_path_coupling_idea.md`

(commit `da9965ccf624d8f0530dd38ce47063abedfb54ee`).

The three materially different attacks were:

1. **Single-defect edge chain / path coupling.** Exploit the previous exact disagreement monovariant at distance one, rather than solve the full pair chain.
2. **Position-only dual.** Test whether a weight depending only on defect position gives one-step contraction. An exact inherited state refutes every such strict contraction at once.
3. **Multi-step block contraction.** Count exactly all source-pair words that leave one defect alive after `T` steps, giving an exact substochastic Bellman/path-coupling coefficient rather than a reset-word bound.

The checker was written only after these statements and failure modes were fixed.

## 2. Exact correlated strip update

Fix strip length `m=2w`. A state is
\[
S=(x;g),\qquad x=(x_1,\ldots,x_m),\quad g=(g_1,\ldots,g_m)\in\{0,1\}^m.
\]
For one fresh iid source pair `(u,v)`, define
\[
d_0=0,
\qquad
 d_i=(1-g_i)\Bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\Bigr),
\quad1\le i\le m.
\tag{2.1}
\]
Then
\[
x'=(x_2,\ldots,x_m,u),
\tag{2.2}
\]
\[
g_i'=g_{i+1}+d_{i+1}-d_i,\qquad1\le i<m,
\tag{2.3}
\]
\[
g_m'=(1-d_m){\bf1}_{\{u=v\}}.
\tag{2.4}
\]
If `g_{i+1}=0`, then `d_{i+1}>=d_i`; if `g_{i+1}=1`, then `d_{i+1}=0`; hence (2.3) remains a bit for every formal binary state. The same `v` appears at every position in (2.1), so the row/column dependence is exact.

The previous R17 report proved for two states with the same raw window and comparable fronts `g<=h` that, under the same `(u,v)`, order is preserved and, writing
\[
D=\sum_i(h_i-g_i),
\]
one has the exact flux identity
\[
D'=D-(h_1-g_1){\bf1}_{\{x_1\ne v\}}
      -(d_m^g-d_m^h){\bf1}_{\{u\ne v\}}.
\tag{2.5}
\]
In particular `D'<=D` pathwise.

## 3. New theorem: single defects form an exact substochastic edge chain

Let an **edge state** be
\[
e=(x,g,j)
\]
where `g_j=0`; it represents the ordered pair
\[
(x,g)\le (x,h),\qquad h=g+e_j.
\]
Thus the pair has Hamming disagreement `D=1`.

### Theorem 3.1 — edge closure

Under one common true-source update `(u,v)`, an edge state either coalesces or maps to another edge state. Therefore the nonabsorbed single defects form an exact finite substochastic Markov chain `Q_m` with
\[
\boxed{|E_m|=m\,2^m\,2^{m-1}=m2^{2m-1}.}
\tag{3.1}
\]

### Proof

The two copies have the same raw window before the update and receive the same fresh `u`, hence they have the same raw window after the update. They are ordered, so (2.5) applies. Since `D=1` initially and `D'` is a nonnegative integer with `D'<=1`, either `D'=0`, in which case the fronts agree, or `D'=1`, in which case the ordered binary fronts differ in exactly one coordinate. That is another edge state. There are `2^m` choices of `x`, `m` choices of the defect coordinate, and `2^(m-1)` choices of the lower front with that coordinate fixed to zero, proving (3.1). QED.

Define for integer `T>=0`
\[
\boxed{
\alpha_m(T):=\|Q_m^T\mathbf1\|_\infty.
}
\tag{3.2}
\]
This is exactly the worst, over all formal edge states, of the probability that a single discrepancy has not coalesced after `T` fresh iid source-pair inputs.

## 4. New theorem: path coupling of arbitrary strip states

### Theorem 4.1 — same-window path coupling

For any two fronts `g,h` with the same raw window `x`, and every `k>=0`,
\[
\boxed{
\Pr\{S_{kT}^{(x,g)}\ne S_{kT}^{(x,h)}\}
\le \min\{1,\,m\alpha_m(T)^k\}.
}
\tag{4.1}
\]

### Proof

Connect `g` to `h` by a Hamming path of at most `m` binary fronts, changing one coordinate at a time. Every adjacent pair is comparable, so Theorem 3.1 applies to it under the common source stream. For one initial edge, the survival probability after `kT` steps is
\[
(Q_m^{kT}\mathbf1)(e).
\]
Because `Q_m` is substochastic and nonnegative,
\[
\|Q_m^{kT}\mathbf1\|_\infty
\le \|Q_m^T\|_\infty^k
=\alpha_m(T)^k.
\]
If every adjacent pair on the original Hamming path has coalesced, the two endpoint chains agree. A union bound over at most `m` initial edges gives (4.1), capped by one. QED.

### Corollary 4.2 — arbitrary initial full states

For arbitrary initial strip states `s,s'`, couple them with the same future source pairs. After exactly `m` shifts their raw windows are both the same last `m` fresh `u` bits, regardless of the original raw windows. Hence
\[
\boxed{
\Pr\{S_{m+kT}^{s}\ne S_{m+kT}^{s'}\}
\le \min\{1,\,m\alpha_m(T)^k\}.
}
\tag{4.2}
\]
This is a dependence-preserving quantitative mixing statement obtained from a state space of single defects rather than all state pairs.

## 5. Rigorous finite-horizon-to-stationary error

The mismatch-reset theorem from the previous R17 work implies the finite strip chain has a unique recurrent class, hence a unique stationary mean reward `gamma_w`. Let `R_N` be the cumulative strip reward for the first `N` updates. One-step rewards lie in `{0,1}`.

Couple a chain started from arbitrary deterministic `s` to a stationary copy with the same future source pairs. During the first `m` steps, bound the reward discrepancy by one per step. Thereafter use (4.2). Once the two finite states meet, synchronous updates keep them equal. Therefore, whenever `alpha:=alpha_m(T)<1`,
\[
\boxed{
\left|\mathbf E_sR_N-N\gamma_w\right|
\le C_m(T)
:=m+T\sum_{k\ge0}\min\{1,m\alpha^k\}
}
\tag{5.1}
\]
for every `N` and every initial state `s`.

If
\[
K=\min\{k\ge0:m\alpha^k\le1\},
\]
then explicitly
\[
\boxed{
C_m(T)\le m+T\left(K+\frac{m\alpha^K}{1-\alpha}\right).
}
\tag{5.2}
\]
Consequently an exact finite-horizon computation has the certified transfer
\[
\boxed{
\frac{\mathbf E_sR_N-C_m(T)}N
\le\gamma_w\le
\frac{\mathbf E_sR_N+C_m(T)}N.
}
\tag{5.3}
\]
This is an actual finite-to-stationary error for the genuine correlated boundary process. It is **not yet** an explicit width-to-infinite-`w` bound for `gamma_2`, and by itself it does not move `L` or `U_F`.

A concrete metric-moving criterion follows: since `gamma_w<=gamma_2`, any exact finite computation satisfying
\[
\mathbf E_sR_N>N L+C_m(T)
\tag{5.4}
\]
would rigorously raise the source lower endpoint. Thus (5.2) turns the coupling theorem into a precise future certificate obligation rather than a qualitative mixing statement.

## 6. Attack 2 fails exactly: position alone cannot contract

The natural compressed dual would assign a positive weight `a_j` only to the defect coordinate. That cannot give strict one-step contraction.

At `m=3`, take the exact state already isolated in the preceding R17 disagreement analysis:
\[
x=(1,0,1),\qquad
 g=(0,0,1),\qquad
 h=(0,1,1).
\tag{6.1}
\]
The unique defect is at coordinate `j=2`. Exact enumeration verifies that under **all four** source inputs `(u,v) in {0,1}^2`, the pair remains nonabsorbed and its unique defect is again at coordinate `j=2`.

Therefore for every positive position-only weight `a_j`,
\[
\mathbf E[a_{J'}\mid e]=a_2.
\]
Any inequality of the form
\[
Q_ma\le q a
\]
valid for every edge state must have `q>=1`. Hence:
\[
\boxed{\text{no environment-free position-only multiplicative dual can prove one-step contraction.}}
\tag{6.2}
\]
The next scalable dual must retain some raw-window/front environment or history, not merely defect location.

## 7. Attack 3: exact block contraction without waiting for a reset word

For every edge state `e`, define the integer word count
\[
N_0(e)=1,
\]
\[
N_{t+1}(e)
=\sum_{a\in\{0,1\}^2:\,T_a(e)\ne\dagger}
N_t(T_a(e)),
\tag{7.1}
\]
where `T_a(e)` is the next edge under source pair `a` and `dagger` means coalescence. Then exactly
\[
\alpha_m(T)=\frac{\max_eN_T(e)}{4^T}.
\tag{7.2}
\]
This counts all genuine source-pair words that keep the discrepancy alive. It is not a reset-word approximation and not Monte Carlo.

Executed exact checker:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0413Z_r17_edge_path_coupling_exact.py`

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0413Z_r17_edge_path_coupling_exact.out`

The integer DP gives, with `T=4m`:

| `m` | edge states | exact numerator / denominator for `alpha_m(4m)` | decimal diagnostic | `m alpha` |
|---:|---:|---|---:|---:|
| 2 | 16 | `376 / 65536` | 0.0057373046875 | 0.011474609375 |
| 3 | 96 | `162486 / 16777216` | 0.009684920311 | 0.029054760933 |
| 4 | 512 | `51701671 / 4294967296` | 0.012037733337 | 0.048150933348 |
| 5 | 2560 | `18888821213 / 1099511627776` | 0.017179282816 | 0.085896414080 |
| 6 | 12288 | `6341593976672 / 281474976710656` | 0.022529867666 | 0.135179205998 |
| 7 | 57344 | `1960664449422089 / 72057594037927936` | 0.027209685191 | 0.190467796340 |
| 8 | 262144 | `666247718450140937 / 18446744073709551616` | 0.036117361188 | 0.288938889503 |

All these are `<1` exactly. For `m=8`, already `8 alpha_8(32)<1`, so `K=1` in (5.2) and
\[
C_8(32)
\le8+32\left(1+\frac{8\alpha_8(32)}{1-\alpha_8(32)}\right)
=\frac{881779270133612507032}{17780496355259410679}
<50.
\tag{7.3}
\]
The final strict inequality is checked entirely by integers (`133*num < 5*den` in the artifact).

For comparison, P13's general one-defect reset waiting constant at `m=8` is
\[
\frac{8\,4^8+10}{21}=\frac{524298}{21}\approx24966.57.
\]
Thus the edge-survival path coupling gives a more than 499-fold smaller **certified generic** additive finite-horizon error at this width. This comparison is mechanism-level only. It does not imply a new `gamma_2` endpoint. Also, at `m=6` the present generic block bound is not better than R17's earlier specialized full-joint Bellman constant `<19.139`; the point is the new edge-chain scaling and proof architecture, not uniform domination of every earlier finite-width constant.

The checker also exhaustively verifies edge closure for every formal edge through `m=8` and verifies the exact `m=3` position-only obstruction. The archived run ends `ALL_EXACT_CHECKS_PASS` and records elapsed execution time `0:29.93`. This is a self-check, not an independent audit.

## 8. What this accomplishes and what it does not

### Source-level before / after

No endpoint is changed by R17 in this iteration:
\[
\boxed{L=0.792665992,\qquad U=U_F,\qquad W_{\rm after}=W_{\rm before}=U_F-L.}
\]
The source remains **OPEN / PARTIAL**.

### Auxiliary mechanism progress

The previous full joint-pair coupling chain can now be replaced, for a rigorous mixing/error estimate, by the exact single-defect chain with only
\[
m2^{2m-1}
\]
states. The resulting path-coupling theorem gives a complete finite-horizon-to-stationary transfer (5.3). At `m=8` the exact additive bias constant is certified below `50` instead of the generic reset scale about `2.5e4`.

### Exact obstruction

The simplest hoped-for compression fails: defect position alone cannot support a strict one-step dual, even at `m=3`. Any scalable proof must carry environment/history information.

### Remaining full-scope gap

There are two distinct gaps before this can improve the Chvátal--Sankoff interval.

1. **Computational scaling.** The edge chain is exponentially smaller than the full pair chain but still has `m2^(2m-1)` formal states. Wider exact strips need a quotient/local dual for `Q_m`, or an analytic bound on `alpha_m(T)`, not brute-force enumeration forever.
2. **Source endpoint movement.** A lower-bound improvement requires a finite-width certificate satisfying (5.4), or another rigorous construction above `L`. The finite widths already solved in earlier R17 work lie below `L`. An upper-bound improvement remains P02's complementary covering/cone problem and is not duplicated here.

The next R17 method therefore should be **environment-aware edge compression**: classify only the local information around the defect that controls the two boundary fluxes in (2.5), build an exact quotient or Bellman supersolution for `Q_m`, and prove a width-uniform or polynomial-state block-contraction bound. A second distinct route is to use (2.5) to derive renewal times from actual flux hits rather than reset words. Re-enumerating the same full edge chain at one more width without such a compression would not count as a new method.

## 9. Consumed repository state and persistence

Material dependencies consumed in this run:

- `operations/PROB10_2026-09-20.md` (controlling owner directive);
- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`;
- `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- `operations/claims/H0021.md`, blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`;
- previous R17 report `20260920T0320Z_r17_disagreement_flux_dual_d7c9.md`, blob `1835a0c0db8271167d825666760473829e757e57`;
- P02 Farey--Collatz report, blob `7f75484503fa5534cf357738df36fac84ace033f`;
- P13 one-defect-reset report, blob `2040446847b5594df0dd9d44ef64fd89bc3afab6`;
- old R17 terminal handoff `runs/R17/20260918_1414Z_lcs_terminal_handoff_rotation_wait_c050_4a7d.md`, blob `17438a301124b51c12395070166841fdb11542c6`.

New immutable artifacts were created before this report at commits

- idea: `da9965ccf624d8f0530dd38ce47063abedfb54ee`;
- exact checker: `f022d070ed3e89adba99daac2f772e065b59fd61`;
- archived output: `11f761a47434deae3ac9dba14e088b42034f4a86`.

No schedule, cadence, enabled state, email, Drive, workflow, public posting, purchase, permission, or peer file was changed.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R17
  parent: PROB10-02
  source: binary_Chvatal_Sankoff_LCS_constant
  source_status: OPEN
  worker_status: PARTIAL
  model_requested: GPT-6_maximum
  actual_model: GPT-5.6_Sol
  reasoning_level: UNVERIFIED
  true_dependent_match_array_preserved: true
  metric:
    name: certified_repository_internal_interval_width_U_minus_L
    lower: 99083249/125000000
    upper: U_F_from_P02_Farey_Collatz_report
    before: U_F_minus_99083249_over_125000000
    after: U_F_minus_99083249_over_125000000
    movement_this_R17_run: false
  companion_movement_since_previous_R17:
    track: P02
    kind: strict_upper_endpoint_improvement_to_U_F
    credited_to_R17: false
  attacks:
    - exact_single_defect_edge_chain_and_path_coupling
    - position_only_dual_refuted_exactly
    - exact_T_equals_4m_block_survival_DP
  mechanism_progress:
    theorem: exact_path_coupling_finite_horizon_stationary_error
    edge_state_count: m_times_2_power_2m_minus_1
    m8_alpha_exact: 666247718450140937/18446744073709551616
    m8_additive_bias_certificate: C_8_less_than_50
  exact_obstruction:
    statement: no_positive_position_only_weight_can_have_uniform_one_step_contraction_q_less_than_1
    smallest_verified_example_m: 3
  unresolved_gap:
    - compress_environment_aware_edge_chain_or_prove_analytic_block_contraction
    - produce_finite_width_lower_certificate_above_L_or_other_source_endpoint_movement
  closure_claim: false
  independent_audit_this_run: false
  email_or_drive_used: false
  scheduler_or_permission_changed: false
```

**Conclusion:** this run produces a rigorous dependence-preserving finite-state coupling/error theorem and a sharp compression obstruction, but no new value of `gamma_2` and no new source endpoint. The next useful attack is an environment-aware quotient/dual for the single-defect chain, not another unchanged finite-width enumeration.
