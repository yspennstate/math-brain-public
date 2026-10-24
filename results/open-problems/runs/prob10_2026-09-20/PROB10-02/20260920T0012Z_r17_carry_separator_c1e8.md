Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: internally certified interval width `0.033609950762282626 -> 0.033609950762282626`; status OPEN/PARTIAL.** Three materially different attacks were made: (A) factor the exact correlated strip update into a two-carry spatial automaton; (B) use that exact carrier to certify finite-width Bellman brackets through width 5 and determine whether any such width can move the source lower endpoint; (C) turn the carry automaton into a spatial separation oracle for finite-range Bellman potentials, then test the simplest exact telescoping potential and identify its quantitative obstruction.

# PROB10-02 / R17 — carry-factorized correlated strip process and a spatial Bellman separator

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Controlling owner directive: `operations/PROB10_2026-09-20.md`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. The true dependent matching array is retained throughout. No independent Bernoulli matching model is used.

Status after this run: **OPEN / PARTIAL**. No exact value of \(\gamma_2\) is claimed.

## 0. Continuity, ownership and the actual R17 successor handoff

The preceding PROB10 report

`runs/prob10_2026-09-20/PROB10-02/20260919T2316Z_r17_strip_variational_7f2a.md`

already performed the owner-required handoff of R17's actual then-current successor H0021. The canonical H0021 file now says `UNASSIGNED (released by R17 under later owner refocus)` and preserves the complete R16/R17 history, including R17 report

`runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`

and navigation commit

`c8891869a1335d67bada83f23f63f2ce09603565`.

The H0021 frozen metric remains `Delta_near=2`; no H0021 claim, report, counter, or artifact is modified here. The intervening G0004 and earlier R17 reports remain immutable. Thus this run continues the explicit PROB10 refocus rather than repeating or silently rewriting the handoff.

No competing canonical owner for the precise PROB10-02 route surfaced in the current repository search. The native slot remains R17 under `operations/PROB10_2026-09-20.md`.

The legacy LCS HARD history is also preserved rather than reset: the old R17 LCS lifecycle had already consumed two stuck recoveries and reached terminal handoff C050. The later owner directive explicitly reassigns the source to R17 with a different method; it does not erase those failures. Under the new PROB10 continuity rule, the source-level metric has now remained unchanged in two consecutive refocus runs. No unrelated rotation is performed.

## 1. Frozen source-level baseline

The complete old handoff is

`runs/R17/20260918_1414Z_lcs_terminal_handoff_rotation_wait_c050_4a7d.md`.

The best internally exact deterministic interval preserved from that lineage is
\[
\boxed{0.792665992\le \gamma_2\le0.826275942762282626},
\qquad
\boxed{U-L=0.033609950762282626}.
\]

The lower endpoint is the Heineman--Miller--Reichman--Salls--Sárközy--Soiffer rigorous lower bound. The upper endpoint is R17 C045's internally exact all-row cone certificate. C033--C035 remain withdrawn because of the complement-gauge error repaired at C036 and are not reused.

The old lower-side finite-lookahead blocker remains the exact `ell=22` threshold
\[
r>\frac{99083249}{150916751},
\]
and the old upper-side blocker remains a covering/cone certificate strictly below
\[
0.826275942762282626.
\]
This run does not repeat either dense route.

## 2. Fresh literature/status check

The current source check was repeated before using the finite-width construction.

- Alexander Tiskin, `https://arxiv.org/abs/2212.01582v2`, still presents the binary coefficient as unresolved. The v2 revision explicitly removes claims from the earlier preprint that turned out to be incorrect; none of those withdrawn claims is used here.
- Heineman--Miller--Reichman--Salls--Sárközy--Soiffer, `https://arxiv.org/abs/2407.10925`, gives the retained rigorous lower bound `0.792665992` for the binary two-string case.
- Ray Li, William Ren and Yiran Wen, *Expected length of the longest common subsequence of multiple strings*, published online 2 March 2026, still says determining the binary Chvátal--Sankoff constant is open and summarizes the public rigorous interval as approximately `0.792665 <= gamma <= 0.826280`.
- Lueker's 2009 JACM paper remains the source of the public `0.826280` upper bound and describes convergent numerical upper-bound recurrences.
- Chia--Bundschuh, *Finite Width Model Sequence Comparison*, Phys. Rev. E 70 (2004), is prior art for a correlated finite-width LCS Markov model. As in the previous report, no novelty claim is made for finite width itself.

A bounded current search found no later primary source determining \(\gamma_2\). This is current-status evidence, not a priority certificate for any internal R17 construction.

## 3. New idea before code: expose the hidden one-dimensional carry

The previous refocus report used the exact strip state
\[
s=(x_1,\ldots,x_{2w};g_1,\ldots,g_{2w}),
\]
where the `x` bits are the raw source-letter window and the `g` bits are frontier increments. That formulation is exact but appears to require a state space growing roughly exponentially in \(w\).

The first attack in this run was to factor the strip update *spatially* before writing any new enumeration code.

Fix the incoming target bit \(v\in\{0,1\}\). Set
\[
c^{(v)}_{-1}=0
\]
and, for \(1\le i\le 2w\), define
\[
\boxed{
 c^{(v)}_{i-1}
 =(1-g_i)\Bigl(c^{(v)}_{i-2}\vee\mathbf 1_{\{x_i=v\}}\Bigr).
}
\tag{3.1}
\]
Thus a frontier increment `g_i=1` resets the carry to zero, whereas on a zero-gradient run a single match propagates the carry to the right.

### Proposition 3.1 — exact carry factorization

For the genuine correlated strip transition, after exposing the fresh pair \((u,v)\),
\[
\boxed{
 g'_i=g_{i+1}+c^{(v)}_i-c^{(v)}_{i-1},
 \qquad 1\le i<2w,
}
\tag{3.2}
\]
\[
\boxed{
 g'_{2w}=(1-c^{(v)}_{2w-1})\mathbf 1_{\{u=v\}},
}
\tag{3.3}
\]
and the diagonal reward is
\[
\boxed{
 \rho(s;u,v)=g_{w+1}+c^{(v)}_w.
}
\tag{3.4}
\]
In particular the one-step update is a left-to-right two-state automaton once `v` is fixed; averaging over the two possible values of `v` requires only the carry pair
\[
(c^{(0)},c^{(1)})\in\{0,1\}^2.
\]

**Proof.** Let \(V_i=\sum_{j\le i}g_j\) and let \(Q_i\) be the next-column dynamic-programming values from the previous report. Define
\[
c_i=Q_i-V_{i+1}.
\]
The initial recurrence gives
\[
c_0=\max(g_1,\mathbf 1_{\{x_1=v\}})-g_1,
\]
which is exactly (3.1). For \(1\le i<2w\),
\[
Q_i=\max(Q_{i-1},V_i+\mathbf 1_{\{x_{i+1}=v\}},V_{i+1}),
\]
so
\[
c_i
=\max(c_{i-1},\mathbf 1_{\{x_{i+1}=v\}},g_{i+1})-g_{i+1}.
\]
Because all three entries are bits, this is again (3.1). Subtracting consecutive `Q` values gives (3.2). At the final boundary the recurrence has only the previous-column and fresh-match alternatives, yielding (3.3). Finally
\[
Q_w-V_w=g_{w+1}+c_w,
\]
and if \(g_{w+1}=1\), (3.1) forces \(c_w=0\), so the right side is indeed a bit. This proves (3.4). \(\square\)

This is the principal mechanism advance of the run. It keeps the shared-letter dependence exactly: the same incoming `v` drives every match test across the column.

## 4. Attack B: exact finite-width Bellman brackets through width 5

For a fixed width `w`, let \(P_w\) be the exact transition matrix on the reachable recurrent class and let \(\bar\rho_w\) be expected one-step reward. For any integer \(T\ge0\), set
\[
h_T=\sum_{t=0}^{T-1}P_w^t\bar\rho_w.
\]
Then the Bellman residual is exactly
\[
\bar\rho_w+P_wh_T-h_T=P_w^T\bar\rho_w.
\]
Therefore the average reward \(\gamma_w\) satisfies
\[
\boxed{
\min_s(P_w^T\bar\rho_w)(s)
\le \gamma_w\le
\max_s(P_w^T\bar\rho_w)(s).
}
\tag{4.1}
\]
No stationary floating-point solve is needed.

The executed checker uses integer numerators with denominator \(4^{T+1}\). It obtains:

| half-width `w` | reachable states | exact Bellman bracket |
|---:|---:|---:|
| 1 | 14 | `[0.699998855590820, 0.700000762939453]` |
| 2 | 224 | `[0.737503804388354, 0.737503808843812]` |
| 3 | 3,098 | `[0.755929160290860, 0.755929180074385]` |
| 4 | 39,774 | `[0.767011424485144, 0.767011520725479]` |
| 5 | 485,794 | `[0.774433965323272, 0.774484344052286]` |

The underlying endpoints are archived as exact integer ratios, not decimal certificates.

### Exact obstruction 4.2 — widths at most five cannot move the retained lower endpoint

Since the width-five upper Bellman endpoint is exactly
\[
\frac{3745176481648434628276480}{4835703278458516698824704}
<0.774485
<0.792665992,
\]
we have
\[
\boxed{\gamma_5<0.792665992.}
\]
The strip constants are monotone in width because enlarging the strip only enlarges the admissible path set. Hence
\[
\boxed{
\gamma_w<0.792665992\quad\text{for every }w\le5.
}
\]
Therefore **no exact finite-width lower certificate confined to `w<=5` can improve the current rigorous source lower endpoint**, regardless of how accurately that finite chain is solved. This is an exact method obstruction, not a performance guess.

It also explains why another hour spent making the `w=3,4,5` stationary solve prettier would be bookkeeping rather than progress.

## 5. Attack C: spatial Bellman separation without enumerating all strip states

The carry factorization suggests a different scaling variable: the *range of the potential*, rather than the total strip width.

Let
\[
z_i=(x_i,g_i)\in\{0,1\}^2.
\]
Consider a rational `k`-local additive potential
\[
 h(s)=\sum_{j=1}^{2w-k+1}
 \phi_j(z_j,\ldots,z_{j+k-1}).
\tag{5.1}
\]
For fixed coefficients \(\phi_j\), the Bellman residual
\[
R_h(s)=\bar\rho_w(s)+\mathbf E[h(S')\mid S=s]-h(s)
\]
can be minimized over **all** formal binary strip states by scanning left to right.

At spatial position `i`, an exact separator needs only:

1. the carry pair `(c^(0),c^(1))` — 4 possibilities;
2. the last `k-1` original symbols `z`;
3. the last `k-1` transformed symbols for `v=0`;
4. the last `k-1` transformed symbols for `v=1`.

Thus a direct exact dynamic program uses at most
\[
4\cdot4^{3(k-1)}=4^{3k-2}
\]
separator states per spatial layer, and four choices of the next `z`. Its complexity is therefore
\[
\boxed{O\!\left(w\,4^{3k-1}\right)}
\]
with exact rational arithmetic, **independent of the exponential reachable-state count in `w` for fixed `k`**.

The proof is constructive: (3.1)--(3.4) update both carry values; after a new original symbol is chosen, the next transformed `g'` symbol for each `v` is known, so every old/new `k`-window contribution whose right endpoint has just arrived can be charged immediately. The final fresh `u` is averaged exactly over two choices at the right boundary.

This gives a genuine LP separation oracle: one can optimize finitely many rational local-potential coefficients by cutting planes while every violated Bellman inequality is found by an exact spatial DP rather than by enumerating `R_w`.

### Sanity certificate: an exact telescoping one-site potential

The simplest nontrivial instance already has a clean closed form. Define
\[
h(s)=\sum_{i=w+1}^{2w-1}g_i+\frac23 g_{2w}.
\tag{5.2}
\]
For fixed `v`, summing (3.2) telescopes. Writing \(c=c^{(v)}_{2w-1}\), one obtains after adding the reward
\[
\rho+h'-h
=\frac13 g_{2w}+c+\frac23 g'_{2w}.
\]
Averaging only over the fresh `u`,
\[
\mathbf E_u[g'_{2w}\mid v,s]=\frac{1-c}{2},
\]
so
\[
\mathbf E_u[\rho+h'-h\mid v,s]
=\frac13+\frac13g_{2w}+\frac23c.
\]
If \(g_{2w}=1\), this is at least \(2/3\). If \(g_{2w}=0\), then among `v=0,1` one value matches `x_{2w}`, so
\[
c^{(0)}+c^{(1)}\ge1.
\]
Averaging over `v` therefore proves
\[
\boxed{R_h(s)\ge\frac23\quad\text{for every formal state }s.}
\tag{5.3}
\]
The exact spatial checker returns minimum `2/3` for widths `1,2,3,4,5,8,12,24,48`.

This certificate is intentionally **not** claimed as source progress; `2/3` is far below the retained lower endpoint. Its value is architectural: it verifies that the spatial separator can produce a global Bellman certificate without enumerating the strip chain.

The quantitative failure of the one-site ansatz is also informative. The next metric-moving attempt should increase potential range `k`, not increase finite-chain precision at widths already ruled out by Obstruction 4.2.

## 6. What was falsified / what remains unproved

The run deliberately tried to break the new route.

1. **Carry formula:** the checker compares the original column dynamic program against (3.1)--(3.4) on every reachable state and every input pair for widths `w=1,...,5`; all comparisons pass exactly.
2. **Small-width hope:** falsified rigorously. Width five itself has \(\gamma_5<0.774485\), so no exact computation at `w<=5` can touch `0.792665992`.
3. **Very short local potential:** the explicit one-site telescoping potential certifies only `2/3`. Thus the useful compression must carry a larger local interaction range or a richer nonadditive summary.

What is **not** proved is that a fixed small range `k` will ever reach the current lower endpoint, nor that the spatial LP remains computationally practical at the required `k`. No claim is made that this separator is new relative to all finite-width / transfer-matrix literature; the bounded prior-art search only establishes the already-known Chia--Bundschuh overlap at the finite-width level.

## 7. Source-level before/after versus mechanism progress

Source metric:
\[
L=0.792665992,
\qquad
U=0.826275942762282626,
\]
\[
\boxed{
(U-L)_{\rm before}=(U-L)_{\rm after}=0.033609950762282626.
}
\]
No finite computation in this run is promoted to a new source endpoint.

Separate mechanism progress:

- exact two-carry factorization of the dependence-preserving strip update;
- exact Bellman brackets through `w=5`;
- exact proof that `w<=5` cannot improve the current lower endpoint;
- exact spatial separation oracle for rational finite-range additive Bellman potentials, with state complexity exponential in range `k` but only linear in strip width `w`;
- exact telescoping `2/3` global certificate as a sanity test of the separator.

The highest-value next route is therefore precise: implement the `k`-local separation oracle as a cutting-plane LP with exact rational freeze/verification, increase `k` while keeping a genuinely large `w` (at least beyond the exact `w<=5` obstruction), and ask whether the minimum Bellman residual can be pushed above `0.792665992`. If short-range potentials plateau, preserve the exact plateau/dual obstruction and switch **within this same LCS problem** to a tensor/MPS or renewal representation rather than rotating away.

## 8. Exact artifacts and executed tests

Executed code:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0012Z_carry_separator_c1e8_checker.py`

created at commit

`a94cdc9243e5695914186d83eb2bfe18d1cda164`.

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0012Z_carry_separator_c1e8_checker.out`

created at commit

`81c75ce5e983e2c1fa5a18d7b45e5bdb4d33ef1a`.

The run ends with

`CARRY_FACTOR_EXACT_ON_ALL_ENUMERATED_REACHABLE_STATES_PASS`

and

`ALL_EXACT_CHECKS_PASS`.

No Monte Carlo confidence interval is used. Decimal displays are diagnostics for exact integer ratios archived in the output.

## 9. Model/control honesty and delivery boundaries

GPT-6 maximum reasoning was requested by the owner. This runtime identifies itself as GPT-5.6 Sol; no authenticated reasoning-effort selector/receipt is exposed here, so reasoning level is reported as `UNVERIFIED`, not as maximum. No scheduler, cadence, enabled state, permissions, workflow, email, Drive item, purchase, or public posting is changed.

```yaml
ledger_delta:
  worker: R17
  allocation: PROB10_2026-09-20
  source: binary_Chvatal_Sankoff_constant
  target: determine_gamma_2
  source_status: OPEN
  report_status: PARTIAL
  metric:
    name: certified_gamma2_interval_width
    lower: 0.792665992
    upper: 0.826275942762282626
    before: 0.033609950762282626
    after: 0.033609950762282626
    movement: false
  continuity:
    h0021_handoff_already_completed_in_predecessor: true
    h0021_metric_preserved: Delta_near_2
    old_lcs_hard_recoveries_consumed: 2
    reset_old_failure_history: false
    consecutive_owner_refocus_source_no_movement_runs: 2
  attacks:
    - exact_two_carry_spatial_factorization
    - exact_width_1_to_5_bellman_brackets_and_small_width_obstruction
    - finite_range_spatial_bellman_separation_oracle
  auxiliary_progress:
    w5_certified_upper_lt_current_source_lower: true
    finite_range_separator_exact: true
    one_site_tail_certificate: 2/3
    source_endpoint_changed: false
  exact_artifacts:
    checker_commit: a94cdc9243e5695914186d83eb2bfe18d1cda164
    output_commit: 81c75ce5e983e2c1fa5a18d7b45e5bdb4d33ef1a
    status: ALL_EXACT_CHECKS_PASS
  model_control:
    requested: GPT-6_maximum
    actual_model: GPT-5.6_Sol
    reasoning_level: UNVERIFIED
    selector_exposed: false
  closure_claim: false
  email_or_drive_used: false
  public_posting: false
  scheduler_changed: false
```

**BOTTOM LINE:** the certified interval does not move. The substantive gain is a dependence-preserving spatial factorization that converts Bellman verification from exponential-in-width state enumeration into a finite-range separation problem; at the same time, exact Bellman brackets prove that widths `w<=5` are incapable of improving the retained lower endpoint, so the next run has a concrete nonrepeating target rather than another small-strip calculation.
