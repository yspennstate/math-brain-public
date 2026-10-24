Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: the current repository-internal certified width ceiling remains `0.033609950762282625015106581538`; status OPEN/PARTIAL. This is the third consecutive R17 PROB10 refocus run without a new endpoint, so this run changes method and proves an exact obstruction inside PROB10-02 rather than rotating.** Three materially different attacks were executed: (A) solve the arbitrary-incoming-carry suffix relaxation analytically; (B) test whether the hidden prefix can be replaced by its pair of Boolean carry maps; (C) construct and minimize the exact hidden-prefix input/output machine.

# PROB10-02 / R17 — suffix-control domination and an exact hidden-prefix boundary obstruction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Controlling owner directive: `operations/PROB10_2026-09-20.md`. The later `operations/PROGRESS20_2026-09-20.md` is also respected: P02 owns the complementary covering/cone variational route, P13 owns the complementary boundary-recursion route, and this R17 run works on the precise missing question of whether the forgotten prefix can be compressed to a small exact controller.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every transition below retains the common source letter shared by the whole column. No independent-Bernoulli matching model is used.

## 0. Continuity, ownership, and current baseline

The owner-required H0021 handoff was already completed in
`runs/prob10_2026-09-20/PROB10-02/20260919T2316Z_r17_strip_variational_7f2a.md`.
The canonical H0021 record remains released/unassigned and preserves R16/R17 work including
`runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`
and navigation commit
`c8891869a1335d67bada83f23f63f2ce09603565`.
No H0021 file, claim, counter, or artifact is changed here.

The newest completed R17 LCS report before this run is
`runs/prob10_2026-09-20/PROB10-02/20260920T0012Z_r17_carry_separator_c1e8.md`.
It proved the exact carry factorization and an exact local Bellman separator, and showed rigorously that strip widths `w<=5` cannot improve the retained lower endpoint.

There were then four R17 artifact commits at timestamp prefix `20260920T0142Z` but no immutable R17 report. They contain an exact projection checker and a numerical-only suffix occupation LP. This run treats those files as an interrupted checkpoint rather than as a completed research run, proves what that relaxation actually computes, and records the obstruction. No failure/stagnation counter is reset.

Two same-source companion reports appeared after R17 C0012:
- P02: `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T00-42-00Z__run-report.md`, covering the deterministic covering/cone variational route;
- P13: `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T01-24-00Z__boundary-carry-reachable-reset-certified-endpoint.md`, covering boundary recursion.

P13 compiled the inherited exact C045 cone endpoint more tightly, so the current repository-internal interval used for continuity is
\[
\boxed{0.792665992\le \gamma_2<
0.826275942762282625015106581538},
\]
with certified width ceiling
\[
\boxed{W<
0.033609950762282625015106581538}.
\]
This run does not claim a new endpoint. The upper endpoint is an internally exact-certified candidate inherited from R17 C045 and remains subject to the repository's independent-review/public-priority standard; the public literature still quotes roughly `0.826280`.

The old invalid C033--C035 certificates remain withdrawn because of the complement-gauge bug repaired at C036. The old lower-side exact blocker also remains:
an `ell=22` feasible-triplet/Bellman certificate must certify
\[
r>\frac{99083249}{150916751}
\]
to improve the literature lower bound `0.792665992`.

## 1. Current literature/status check

A bounded current check on 20 September 2026 found no primary-source determination of the binary constant.

- Tiskin, arXiv:2212.01582v2, last revised 13 August 2024, explicitly says the binary proportionality coefficient remains unresolved. Its comments say that claims in the earlier preprint about the stochastic process and `gamma` turned out to be incorrect and were removed. None of those withdrawn claims is used here.
- Heineman--Miller--Reichman--Salls--Sárközy--Soiffer, arXiv:2407.10925, prove the retained lower bound `0.792665992`.
- Li--Ren--Wen, published online 2 March 2026 (Bull. Aust. Math. Soc., August 2026 issue), still describe determination of the two-string binary constant as open and summarize the public rigorous range as roughly `0.792665 <= gamma <= 0.826280`.
- Chia--Bundschuh remains prior art for correlated finite-width LCS models. No novelty claim is made for finite-width truncation itself.

A bounded negative search is not a priority certificate for the structural lemmas below.

## 2. Exact suffix transition

Fix a suffix length `k`. A formal state is
\[
z=(x_1,\ldots,x_k;g_1,\ldots,g_k)\in\{0,1\}^{2k}.
\]
The `x_i` are actual source bits and the `g_i` are frontier increments. For the actual fresh column bit `v`, an incoming left-boundary carry `c in {0,1}`, and fresh row bit `u`, define
\[
d_0=c,\qquad
d_i=(1-g_i)\bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\bigr),
\quad 1\le i\le k.
\tag{2.1}
\]
The next raw window is
\[
x'=(x_2,\ldots,x_k,u),
\]
and
\[
g'_i=g_{i+1}+d_{i+1}-d_i,\qquad i<k,
\tag{2.2}
\]
\[
g'_k=(1-d_k){\bf1}_{\{u=v\}}.
\tag{2.3}
\]
This is the exact shared-letter transition inherited from the correlated strip derivation. The same `v` is used at every site.

The interrupted `0142Z` occupation LP allowed the incoming carry `c` to be selected after observing `(z,v)`, subject only to stationarity and the fair-`v` constraint. Numerically it returned
\[
1-p_k^*\approx
0.6666667,\ 0.7000000,\ 0.7233076,\ 0.7375038
\]
for `k=1,2,3,4`. The first attack was to determine exactly whether this apparent relaxation contains new information.

## 3. Attack A — arbitrary incoming carry gives no stronger lower relaxation

### Lemma 3.1 — carry-one can only delete outgoing gradient bits

Fix `(x,g,v,u)` and compare (2.1)--(2.3) with incoming carries `c=0` and `c=1`. Let
\[
\Delta_i=d_i^{(1)}-d_i^{(0)}.
\]
Then
\[
\boxed{\Delta_i=
\prod_{j=1}^{i}(1-g_j){\bf1}_{\{x_j\ne v\}}}
\tag{3.1}
\]
for `i>=1`, while `Delta_0=1`. Hence `Delta_i` is nonincreasing in `i`, and
\[
g_i'^{(1)}-g_i'^{(0)}
=\Delta_{i+1}-\Delta_i\le0,\qquad i<k,
\]
while
\[
g_k'^{(1)}-g_k'^{(0)}
=-\Delta_k{\bf1}_{\{u=v\}}\le0.
\]
Therefore
\[
\boxed{g'^{(1)}\le g'^{(0)}
\quad\hbox{coordinatewise}.}
\tag{3.2}
\]

**Proof.** If `g_i=1`, both carries reset to zero. If `g_i=0` and `x_i=v`, both become one. Only when `g_i=0` and `x_i!=v` is the previous discrepancy copied. This proves (3.1), and (2.2)--(2.3) give the two displayed differences. QED.

### Lemma 3.2 — the zero-carry transition is monotone in the gradient state

Fix `x,v,u`. If
\[
g\le \widetilde g
\]
coordinatewise, then under incoming carry zero,
\[
\boxed{g'(x,g)\le g'(x,\widetilde g)}
\tag{3.3}
\]
coordinatewise.

**Proof.** Induction in (2.1) gives
\[
d_i(x,\widetilde g)\le d_i(x,g).
\]
For `i<k`, (2.1)--(2.2) can be rewritten as
\[
g'_i=(1-d_i)
\left(g_{i+1}\vee{\bf1}_{\{x_{i+1}=v\}}\right).
\tag{3.4}
\]
Both factors on the right weakly increase when `g` is replaced by `g_tilde`: the first because the carry decreases, the second because `g_{i+1}` increases. Equation (2.3) handles the final coordinate in the same way. QED.

### Theorem 3.3 — zero control dominates every adapted carry policy

Let a controller choose `c_t in {0,1}` at time `t` using the current suffix state, the current column bit `v_t`, and arbitrary extra randomization, but not the unseen fresh `u_t`. Couple it to the policy `c_t=0` using the same iid source pairs `(u_t,v_t)` and the same initial state. Then at every time
\[
\boxed{g_t^{\rm control}\le g_t^{0}}
\tag{3.5}
\]
coordinatewise, pathwise.

**Proof.** The raw windows are identical under the coupling. If (3.5) holds at time `t`, Lemma 3.1 first gives
\[
T_{c_t}(x_t,g_t^{\rm control})
\le
T_0(x_t,g_t^{\rm control})
\]
in gradient coordinates, and Lemma 3.2 gives
\[
T_0(x_t,g_t^{\rm control})
\le
T_0(x_t,g_t^0).
\]
Induction proves the claim. Conditioning on controller randomization handles randomized policies. QED.

Thus every coordinatewise increasing finite-horizon reward is maximized by **never injecting an incoming carry**. In particular this applies to the terminal-gradient reward `g_k`.

### Corollary 3.4 — exact solution of the interrupted suffix occupation LP

Every feasible stationary occupation measure of the `0142Z` LP disintegrates into a stationary state law and a randomized carry policy `c|(z,v)`. By Theorem 3.3 its average terminal-gradient reward is no larger than the zero-carry chain. Conversely, the zero-carry chain is feasible.

The zero-carry chain has a unique recurrent class: the source word
\[
(u,v)=(0,1)
\]
repeated `2k` times sends **every formal state** to
\[
(0^k;0^k).
\]
Indeed, after the first `k` repetitions the raw window is `0^k`; during the next `k` repetitions there are no matches to `v=1`, so carries remain zero and the gradient vector shifts left while zeros enter from the right.

Therefore, if `p_k^*` is the LP optimum,
\[
\boxed{p_k^*=\mathbf E_{\pi_k^0}g_k,}
\tag{3.6}
\]
where `pi_k^0` is the unique stationary law of the zero-carry chain.

For even `k=2w`, that zero-carry chain is exactly the width-`w` correlated strip chain from the preceding R17 reports. Moreover
\[
\boxed{1-p_{2w}^*=\gamma_w.}
\tag{3.7}
\]
To see (3.7), let `p=E_pi g_{2w}`. Stationarity of the final gradient gives
\[
p=\frac12-\frac14\mathbf E_\pi(d_{2w}^{(0)}+d_{2w}^{(1)}).
\tag{3.8}
\]
For the explicit potential
\[
h_0(z)=\sum_{i=w+1}^{2w-1}g_i+\frac23 g_{2w},
\]
direct substitution of (2.1)--(2.3) and averaging over the fresh `u,v` gives the exact one-site telescoping coboundary; stationarity cancels `P h_0-h_0` and yields
\[
\gamma_w=
\frac13+\frac13p+
\frac13\mathbf E_\pi(d_{2w}^{(0)}+d_{2w}^{(1)}).
\tag{3.9}
\]
Substituting (3.8) into (3.9) yields `gamma_w=1-p`.

This explains the numerical checkpoint exactly: `k=2` gives the known `w=1` strip value `0.7`, while `k=4` gives the known `w=2` value `~0.737503806`. The apparently more permissive incoming-carry LP **does not strengthen the finite-width lower hierarchy at all**.

The same relaxation is useless for an upper bound: the policy `c=1` preserves the invariant set `g=0^k`, so its stationary terminal-gradient frequency is exactly zero. Hence the relaxation permits the trivial surrogate upper value `1`.

This is the first exact obstruction of the run: a finite-state variational method that forgets the prefix and allows its carry to be reselected independently each time cannot close the full problem. The temporal law of the forgotten prefix is the essential missing information.

## 4. Attack B — the pair of carry maps is not a Markov boundary state

A stronger idea is to remember the whole Boolean action of the hidden prefix on incoming carry.

For a prefix
\[
q=(x_1,\ldots,x_r;g_1,\ldots,g_r)
\]
and test symbol `v`, let
\[
F_q^{(v)}:\{0,1\}\to\{0,1\}
\]
be the map taking an incoming carry to the outgoing carry after (2.1). Each `F` is one of the three monotone Boolean maps `0`, `id`, `1`, so the pair
\[
(F_q^{(0)},F_q^{(1)})
\]
has at most nine values.

That nine-state summary is **not Markov** under column evolution.

Take
\[
A=(x=00,g=01),\qquad
B=(x=10,g=01).
\]
Because the final gradient bit is `1`, both test-symbol carry maps are reset:
\[
(F_A^{(0)},F_A^{(1)})
=(F_B^{(0)},F_B^{(1)})
=(0,0).
\]
Now append boundary site `(x,g)=(0,0)` and expose current column bit `v=1`, then update and drop the leftmost site. Exact arithmetic gives
\[
A'=(x=00,g=10),\qquad
B'=(x=00,g=00).
\]
Their carry-map summaries are different:
\[
A':(1,0),\qquad
B':(1,\mathrm{id}).
\]
Thus two prefixes with identical present carry action evolve to different future carry actions under the same input.

The checker records this as `PAIR_TRANSDUCER_NONMARKOV_PASS`.

So a four-output / nine-map boundary summary cannot supply the stationary finite-state characterization requested by the owner. The obstruction is temporal: information erased from the *current* carry can survive in raw prefix letters and reappear after the resetting gradient moves out of the window.

## 5. Attack C — exact hidden-prefix input/output machine

The failed nine-state summary suggests using the full observational quotient instead of guessing a statistic.

For a length-`r` hidden prefix, let the external input alphabet be
\[
a=(b_x,b_g,v)\in\{0,1\}^3.
\]
Append the boundary site `(b_x,b_g)`, perform one exact zero-left-carry column update with column letter `v`, and drop the old leftmost site. The output of the hidden-prefix state is its pair of current carry maps. This is a finite deterministic Moore machine with `4^r` raw states.

### Proposition 5.1 — a general exact congruence

Let
\[
\ell(g)=\max\{t:g_1=\cdots=g_t=1\}
\]
(with `ell=0` if `g_1=0`). Raw letters `x_1,\ldots,x_{\ell(g)}` can be discarded exactly. Equivalently, canonicalize a state by replacing those raw letters by zeros.

This canonicalization is an exact machine congruence: canonically equivalent states have identical current carry-map output, and after every input `a` their next states are again canonically equivalent.

**Proof.** At a site with `g_i=1`, (2.1) resets the carry to zero regardless of `x_i`; hence the current prefix output cannot depend on a raw bit lying under the leading reset run. Under one update, `x_1` is dropped. If the leading run has length at least two, a differing `x_2` shifts into the first raw position, but the transformed first gradient is still `1`, so the difference remains underneath a leading reset and is erased by canonicalization. Iterating this observation through the whole leading run proves equality of the canonical successors for every boundary input. QED.

The number of canonical states is exactly
\[
\boxed{
N_r=\frac{2\,4^r+1}{3}.
}
\tag{5.1}
\]
Indeed, if the leading run has length `t<r`, there are `2^{r-t-1}` gradient patterns and `2^{r-t}` relevant raw strings, contributing `2*4^{r-t-1}` classes. The all-one gradient has one class. Summing gives (5.1).

This exact quotient is positive progress—a dependence-preserving boundary automaton smaller than the raw one—but its size is still asymptotically `(2/3)4^r`, so it only saves a factor `3/2`.

The executed exact Moore minimizer goes further. For every `r<=6`, the **minimal** observational machine has exactly the same number of states:
\[
3,\ 11,\ 43,\ 171,\ 683,\ 2731.
\]
For `r=6`, the 4096 raw states minimize to 2731 classes, with exact class-size distribution
\[
\{1:2048,\ 2:512,\ 4:128,\ 8:32,\ 16:8,\ 32:2,\ 64:1\}.
\]
The canonical congruence itself was exhausted through `r=7`, where it has 10923 classes out of 16384 raw states.

I do **not** infer from six minimized depths that every conceivable exact representation has exponential size; that would be an unjustified asymptotic claim. The exact conclusion is narrower and sufficient for method triage: neither the nine-map statistic nor ordinary exact Moore minimization of this natural hidden-prefix machine reveals the small stationary state space that the desired finite-to-infinite argument would need.

## 6. Exact executed checks

New artifacts:

- `artifacts/prob10_2026-09-20/PROB10-02/20260920T0212Z_r17_suffix_control_obstruction_4a6c_exact.py`
- `artifacts/prob10_2026-09-20/PROB10-02/20260920T0212Z_r17_suffix_control_obstruction_4a6c_exact.out`

The checker exhausts:

1. carry-one domination for every formal state/input through `k=7`;
2. zero-carry gradient monotonicity for every ordered pair `g<=g_tilde` through `k=7` (`1,119,744` ordered/input cases at `k=7`);
3. the `2k` synchronizing word on every formal state through `k=7`;
4. the explicit two-site non-Markov carry-map counterexample;
5. the canonical congruence through `r=7`;
6. exact Moore minimization through `r=6`.

The output ends `ALL_EXACT_CHECKS_PASS`. These are self-checks, not independent audits.

## 7. Source-level before/after and mechanism progress

Source-level metric before:
\[
0.792665992\le\gamma_2<
0.826275942762282625015106581538,
\qquad
W_{\rm ceiling}=0.033609950762282625015106581538.
\]

Source-level metric after: **unchanged**.

Mechanism-level progress:

- proved that arbitrary per-step incoming-carry control collapses exactly to the zero-boundary finite-width strip lower hierarchy;
- proved that the same relaxation gives only the trivial upper value `1`;
- gave an exact two-site counterexample to the nine-state carry-map boundary summary;
- constructed a valid exact hidden-prefix quotient with `(2*4^r+1)/3` states and exactly minimized the corresponding observational machine through `r=6`.

This is the third consecutive completed R17 PROB10 refocus report with no new source endpoint. Under the owner instruction, that triggers a **method change within this problem**, not rotation. This report is the required exact obstruction record.

## 8. Residual full-scope gap and next method

The full gap is unchanged: no exact value of `gamma_2` and no strict improvement of the current source interval is proved here.

The obstruction identifies precisely what the next route must preserve:

> The forgotten prefix cannot be replaced by a carry chosen afresh each time, nor by its current pair of carry maps. A useful finite approximation must retain **temporal constraints on the hidden prefix** and attach a rigorous error to forgetting older information.

The next R17 attack should therefore be a **history-coupled interval Markov chain / approximate bisimulation**, not another uncontrolled strip solve. A concrete target is to keep `h` steps of predictive hidden-prefix information, propagate a set of admissible carry-map states rather than a free action, and use the exact carry-extinction event to prove a deterministic bound on the stationary Bellman residual created by truncating older history. Only after such an error theorem is on the page should a numerical or exact LP be run.

This is complementary to P13's boundary recursion: P13 supplies exact carry identities; R17's next obligation is to turn temporal hidden-prefix uncertainty into a certified approximation theorem. It is also distinct from P02's covering/cone route.

```yaml
ledger_delta:
  worker: R17
  focus: PROB10-02
  source_status: OPEN
  worker_status: PARTIAL
  metric: "repository-internal certified width ceiling for binary gamma_2"
  lower_before: "0.792665992"
  upper_before: "<0.826275942762282625015106581538"
  width_before: "<0.033609950762282625015106581538"
  lower_after: "0.792665992"
  upper_after: "<0.826275942762282625015106581538"
  width_after: "<0.033609950762282625015106581538"
  source_movement: false
  completed_refocus_no_movement_reports: 3
  method_change_required_and_executed: true
  attacks:
    - "arbitrary incoming-carry stationary control: solved exactly, collapses to zero carry"
    - "pair of Boolean carry maps: exact two-site non-Markov counterexample"
    - "hidden-prefix Moore machine: exact congruence and exact minimization through r=6"
  next_method: "history-coupled interval Markov approximation with a proved truncation/Bellman error"
```

No schedule, cadence, enabled state, shared root, peer file, email, Drive item, public post, workflow, permission, or purchase is modified.
