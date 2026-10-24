Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `D_rev,0` stayed `0 -> 0`. Section-B methods actually tried: #21, #23, #26. This is the sixth consecutive unchanged P0292 run, so the report ends with the required P0292 handoff/rotation.**

# NM13-01 — P0292 nonreversible three-state cycle theorem and six-run handoff

**Track:** NM13-01  
**Category:** CLOSABLE OUTSIDE  
**Source ID / claim:** P0292 / `operations/claims/P0292.md`  
**Canonical dedup key:** `characterize_ctmc_speed_monotonicity_in_supermodular_order`  
**Canonical SHA-256 / shard:** `3aded70a56a908e9042798ee4a8ac614005a51635e52453716ea79167c073ae5`, residue `0 mod 13`  
**Source:** Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), Problem 4, source p. 215  
**Source status:** OPEN in full generality in the bounded current-literature check below  
**Track status through the mathematics below:** PARTIAL  
**Frozen metric:** `D_rev,0`, normalized frozen-limit first-order supermodular speed defect over finite stationary irreducible reversible CTMCs  
**Metric before / after:** `0 -> 0` exactly; **no movement**  
**Consecutive unchanged runs since metric movement:** 6  
**Stuck recoveries used:** 1  
**Rotation state after this report:** **HANDOFF REQUIRED / P0292 no longer continues on NM13-01 next run**  
**Audits:** P26 NOT REQUESTED / NOT PASSED; NM13-02 NOT REQUESTED / NOT PASSED  
**New internal claim labels:** `NM13-01-P0292-COMPLEX-SPECTRUM-NECESSARY-06`, `NM13-01-P0292-ONEWAY3-BIVARIATE-06`  
**Exact finite artifact:** `proofnet24/NM13-01/artifacts/2026-09-18/p0292_nonrev_cycle_exact.py`, archived output beside it; script commit `63de3fe3e8b991594bd3efa9f3d85a8af962e5bc`, output commit `308a378af8e7f93c1245f377b838c69ed7223d48`.

## 1. Authoritative continuity, required reads, ownership and six-run gate

I continued the already-admitted P0292 source for exactly one final source-level attack. I did **not** reopen or overwrite admission, change the canonical identity, change the frozen metric, or count any screening as mathematical movement. Immediately before this run the canonical claim still named NM13-01 as owner, and no later release, retirement, competing P0292 claim, POSTED entry, or source-level PROVED/REFUTED/KNOWN correction was recovered.

Before the attack I reread/recovered the current required state: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; `operations/claims/P0292.md`; the newest NM13-01 report `2026-09-18T02-14-06Z__p0292-reversible-three-state-classification.md`; the newest neighboring NM13-02 report `2026-09-18T02-09-03Z__p0037-stuck-recovery-1.md`; and targeted P0292 source/attempt/alias/ownership searches. The P0292 claim still fixes the exact source and residue. NM13-02 remains on its distinct P0037 claim and creates no ownership conflict.

The previous immutable report was explicit: the frozen metric had been unchanged for five consecutive runs; this sixth invocation was allowed one source-level nonreversible three-state attack using new methods #21/#23/#26; if the metric still did not move, the CLOSABLE six-run policy required a preserved handoff and rotation rather than a seventh P0292 run. That condition is met here. Accordingly, Section 9 below is the explicit handoff. The shared canonical claim file is not edited because workers are forbidden to edit shared roots; the `ledger_delta` requests P26 to reconcile the shared ownership ledger. A stale shared claim entry must not be read as permission for NM13-01 to run P0292 a seventh time.

## 2. Exact source and bounded literature check — 2026-09-18 UTC

The accepted-author/source version of Leskelä's paper was rechecked. The source condition is the all-finite-dimensional supermodular speed order

\[
 c_1\le c_2 \quad\Longrightarrow\quad \lambda_{c_1}\ge_{\rm sm}\lambda_{c_2},
 \qquad \lambda_c(t)=\lambda(ct),
\]

for a stationary ergodic CTMC on an ordered real state space. The source asks for a simple necessary-and-sufficient characterization and emphasizes that outside stochastically monotone chains little was known even on three states.

Fresh bounded searches dated 2026-09-18 covered the exact source title/problem wording, `three-state nonreversible Markov chain supermodular lag`, `one-way cycle covariance monotonicity`, `concordance lag three state`, and the older dependence-in-lag literature. The closest recovered paper remains Rafał Kulik, *Monotonicity in Lag for Nonmonotone Markov Chains*, PEIS 18 (2004), which proves decreasing covariance/dependence for a special nonmonotone doubly stochastic class. I did not recover a later source-matching all-FDD characterization, a theorem matching the complex-spectrum obstruction below, or the exact directed-three-cycle bivariate classification below. This is a bounded search with ordinary index/access limits. It is **not** proof of worldwide openness or publication novelty; novelty is **UNVERIFIED**.

The equal-rate directed cycle had already appeared elsewhere in the repository in work on a different Leskelä source problem. I therefore do **not** count “a directed cycle can oscillate” as a new discovery. The new work below is the general complex-spectrum necessity, an exact **real-spectrum** nonreversible counterexample, and a complete two-time classification of the entire positive-rate one-way three-cycle family.

## 3. Source-level two-time consequence of the all-FDD order

Let `X` be stationary on ordered states `1<2<3`. For increasing functions `f,g`, the function

\[
C_{f,g}(t)=\operatorname{Cov}(f(X_0),g(X_t))
\]

must be nonincreasing in `t` if the source all-FDD order holds. Indeed, for any `t_1<=t_2`, apply the source order to the two observation times `(0,1)` and the supermodular function

\[
\phi(x,y)=f(x)g(y).
\]

Stationarity fixes the one-dimensional marginals, so the comparison is exactly the monotonicity of the joint product expectation, hence of the covariance.

On a finite linearly ordered state space, bivariate supermodular order with common marginals is equivalent to concordance order; for three states it is enough to test the four upper-tail pairs generated by

\[
h_2=\mathbf 1_{\{x\ge2\}},\qquad h_3=\mathbf 1_{\{x\ge3\}}.
\]

This converts the first nonreversible test into four exact scalar semigroup functions.

## 4. Method #21 — ASK WHO ELSE HAS THIS SHAPE: complex eigenmodes are forbidden

The nonreversible obstruction is most transparent when treated as a damped-oscillator problem rather than as a Markov-order cone problem.

### Theorem 4.1 — complex spectrum is incompatible with the source order on three states

Let `Q` be an irreducible three-state CTMC generator with stationary law `pi`. If its two nonzero eigenvalues are

\[
-a\pm ib,\qquad a>0,\ b\ne0,
\]

then Leskelä's speed order fails already for two observation times. Consequently, **any irreducible three-state CTMC satisfying the source all-FDD speed order must have real nonzero spectrum.**

### Proof

Choose any nonconstant increasing threshold `h`, for example `h=h_2`. Since the state space is finite and the nonconstant spectral subspace is the real two-dimensional span of the complex conjugate modes,

\[
C_h(t):=\operatorname{Cov}(h(X_0),h(X_t))
=e^{-at}\bigl(A\cos bt+B\sin bt\bigr)
\]

for real `A,B`. At `t=0`,

\[
A=C_h(0)=\operatorname{Var}_\pi(h)>0.
\]

Hence the sinusoidal factor is nonzero and assumes negative values. Therefore `C_h(t)` is negative at some times, while `C_h(t)\to0` as `t\to\infty`.

If the source order held, Section 3 would force `C_h` to be nonincreasing. But a nonincreasing function that starts positive, becomes negative, and has limit `0` is impossible: once below zero it could never increase back toward zero. Contradiction. `QED`

**Outcome of #21.** This gives a clean source-level necessary condition without reversibility: the only unresolved three-state candidates have real nonzero spectrum. It also explains exactly why the previously known equal-rate directed-cycle obstruction works, without re-counting that old example as new progress.

## 5. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: a real-spectrum nonreversible failure

Complex eigenvalues make failure comparatively cheap. To test whether “real spectrum” might accidentally be sufficient, I attacked the opposite case and sought a source-valid nonreversible counterexample with two real decay rates.

Consider the ordered states `1<2<3` and the one-way cycle generator

\[
Q_*=
\begin{pmatrix}
-10&10&0\\
0&-1&1\\
1&0&-1
\end{pmatrix}.
\]

Its stationary law is exactly

\[
\pi=\frac1{21}(1,10,10),
\]

and its characteristic polynomial is

\[
\chi_{Q_*}(\lambda)=\lambda(\lambda^2+12\lambda+21).
\]

Thus its nonzero decay rates are real and distinct:

\[
\mu_1=6-\sqrt{15},\qquad \mu_2=6+\sqrt{15}.
\]

Take the increasing threshold `h=h_2=(0,1,1)`. Write

\[
C(t)=\operatorname{Cov}(h(X_0),h(X_t))
=Ae^{-\mu_1t}+Be^{-\mu_2t}.
\]

The exact initial data are

\[
C(0)=\frac{20}{441},\qquad C'(0)=-\frac{10}{21}.
\]

Solving for the modal coefficients gives

\[
A=\frac{10-3\sqrt{15}}{441}<0,
\qquad
B=\frac{10+3\sqrt{15}}{441}>0,
\]

where the first sign is exact because `135>100`. Therefore the slow term is negative and dominates for large `t`, so

\[
C'(t)>0
\]

for all sufficiently large `t`. More explicitly, with

\[
t_*=rac{1}{\mu_2-\mu_1}
\log\!\left(\frac{\mu_2B}{-\mu_1A}\right),
\qquad
\frac{\mu_2B}{-\mu_1A}=31+8\sqrt{15}>1,
\]

we have `C'(t)>0` for every `t>t_*`.

Hence for sufficiently small positive `eps`,

\[
E[h(X_0)h(X_{t_*+\epsilon})]
>
E[h(X_0)h(X_{t_*})],
\]

which violates the two-time consequence of Leskelä's speed order. Thus **real spectrum is necessary but not sufficient** even on three states.

The exact checker archived this run verifies the stationary distribution, characteristic polynomial, decay rates, covariance initial data, modal coefficients, exact signs, and the general symbolic formulas used in Section 6. Its archived output ends `ALL_EXACT_CHECKS_PASS`. The checker is a self-check, not an independent audit.

## 6. Method #26 — HUNT THE SPORADIC CASE: complete bivariate classification of the positive-rate one-way three-cycle

The preceding witness suggests solving its whole three-parameter family rather than filing a single counterexample.

Let

\[
Q(a,b,c)=
\begin{pmatrix}
-a&a&0\\
0&-b&b\\
c&0&-c
\end{pmatrix},
\qquad a,b,c>0,
\]

on the fixed order `1<2<3`. Put

\[
s=a+b+c,
\qquad
S=ab+bc+ca,
\qquad
\Delta=s^2-4S.
\]

When `Delta>=0`, define

\[
\mu_1=\frac{s-\sqrt\Delta}{2},
\qquad
\mu_2=\frac{s+\sqrt\Delta}{2}.
\]

### Theorem 6.1 — exact two-time speed-order classification for one-way three-cycles

For the stationary one-way cycle `Q(a,b,c)`, the following are equivalent:

1. for every `0<=t_1<=t_2`, the stationary pair `(X_0,X_{t_1})` dominates `(X_0,X_{t_2})` in supermodular order;
2. all four upper-tail joint probabilities for thresholds `h_2,h_3` are nonincreasing in the lag;
3. `Delta>=0` and

\[
\boxed{b\ge\mu_1.}
\]

Thus the entire family is exactly classified at the bivariate level.

### Proof

The stationary law is

\[
\pi=\frac1S(bc,ca,ab).
\]

If `Delta<0`, the two nonzero eigenvalues are complex, so Theorem 4.1 proves failure.

Assume first `Delta>0`. For `r,s in {2,3}`, put

\[
C_{rs}(t)=\operatorname{Cov}(h_r(X_0),h_s(X_t)).
\]

Each lies in the two-dimensional nonconstant spectral subspace, hence

\[
C_{rs}(t)=A_{rs}e^{-\mu_1t}+B_{rs}e^{-\mu_2t}.
\]

Direct stationary calculation gives

\[
\begin{array}{c|c|c}
(r,s)&C_{rs}(0)&C'_{rs}(0)\\ \hline
(2,2)&\dfrac{abc(b+c)}{S^2}&-\dfrac{abc}{S}\\[4pt]
(2,3)&\dfrac{ab^2c}{S^2}&0\\[4pt]
(3,2)&\dfrac{ab^2c}{S^2}&-\dfrac{abc}{S}\\[4pt]
(3,3)&\dfrac{abc(a+b)}{S^2}&-\dfrac{abc}{S}.
\end{array}
\]

For any two-exponential function `C(t)=Ae^{-mu_1t}+Be^{-mu_2t}` with `0<mu_1<mu_2` and `C'(0)<=0`, one has

\[
C'(t)\le0\ \forall t\ge0
\quad\Longleftrightarrow\quad
A\ge0.
\]

Necessity follows because `-mu_1 A e^{-mu_1t}` is the slow asymptotic derivative term. For sufficiency, if `B>=0` the derivative is manifestly nonpositive; if `B<0`, the inequality at `t=0` says `mu_2(-B)<=mu_1A`, and the positive fast contribution decays faster thereafter.

Using

\[
A_{rs}=\frac{C'_{rs}(0)+\mu_2C_{rs}(0)}{\mu_2-\mu_1}
\]

and `mu_1 mu_2=S`, the signs of the four slow coefficients are the signs of

\[
\mu_2(b+c)-S,
\qquad
\mu_2b,
\qquad
\mu_2b-S=\mu_2(b-\mu_1),
\qquad
\mu_2(a+b)-S.
\]

The second is always positive. The third is nonnegative exactly when `b>=mu_1`. Under that condition the first and fourth are strictly positive because `c>0` and `a>0`. Hence all four threshold covariances are nonincreasing exactly when `b>=mu_1`.

If `Delta=0`, write `mu=s/2`, so `S=mu^2`. Each covariance has the Jordan-limit form

\[
C_{rs}(t)=e^{-\mu t}(V_{rs}+K_{rs}t),
\qquad
K_{rs}=C'_{rs}(0)+\mu C_{rs}(0).
\]

Since every listed initial derivative is nonpositive, `C'_{rs}(t)<=0` for every `t>=0` iff `K_{rs}>=0`. The same four brackets with `mu_1=mu_2=mu` appear; again the only potentially binding one is

\[
\mu b-S=\mu(b-\mu),
\]

so the condition is `b>=mu=mu_1`.

Finally, for two probability laws on a finite product of two chains with identical one-dimensional marginals, supermodular order is equivalent to concordance order, i.e. comparison of all upper-tail rectangles. On three states the four rectangles generated by `(h_2,h_3)` are exactly the nontrivial ones. This proves the equivalence. `QED`

### Exact examples on opposite sides

- `(a,b,c)=(10,1,1)`: `Delta=60`, `mu_1=6-sqrt(15)>1=b`; the bivariate speed order fails, as certified in Section 5.
- `(a,b,c)=(1,10,1)`: the same real spectrum has `b=10>mu_1`; **every two-time supermodular test is monotone in the source direction**. Whether this passing nonreversible example also satisfies the source's **all-finite-dimensional** order is not proved here and is the cleanest remaining three-state question left by this handoff.

This second example matters because it shows that the bivariate obstruction does not settle the source: some genuinely nonreversible one-way cycles pass every pairwise test.

## 7. What moved mathematically, and what did not move metrically

New source-relevant mathematics in this invocation:

1. Every three-state source-satisfying CTMC must have real nonzero spectrum.
2. Real spectrum is not sufficient: the exact nonreversible generator `Q_*` above fails the source order already for two times.
3. The complete bivariate speed-order region of every positive-rate one-way three-cycle is exactly `Delta>=0` and `b>=mu_1`.
4. The first clean all-FDD nonreversible test case left open is the bivariate-passing family, e.g. `(a,b,c)=(1,10,1)`.

None of these changes the **frozen metric**, which was fixed at admission as the reversible frozen-limit first-order defect:

\[
\boxed{D_{\rm rev,0}=0\to0.}
\]

Changing the metric now to “number of nonreversible families classified” or to a bivariate defect would violate the frozen-metric rule. Therefore this run honestly records **no metric movement** and increments the unchanged counter to six.

## 8. Exact artifact and checker scope

The exact script `p0292_nonrev_cycle_exact.py` was written only after the analytic route produced a source-valid real-spectrum witness and a family theorem worth checking. It uses exact SymPy arithmetic to verify:

- `chi_Q*(lambda)=lambda(lambda^2+12lambda+21)`;
- `pi=(1,10,10)/21`;
- `C(0)=20/441` and `C'(0)=-10/21` for `h_2`;
- `A=(10-3sqrt(15))/441<0`, `B=(10+3sqrt(15))/441>0`;
- the exact turning ratio `31+8sqrt(15)`;
- the general stationary law and the four exact `C_rs(0), C'_rs(0)` formulas;
- the four slow-coefficient numerators used in Theorem 6.1.

The executed output ends `ALL_EXACT_CHECKS_PASS`. This is explicitly a **self-check**. It does not substitute for P26 or NM13-02 audit and is not evidence of publication novelty.

## 9. Mandatory six-run handoff and rotation

The CLOSABLE policy says that after six unchanged runs the source rotates, preserving the full handoff. This report is that handoff. **NM13-01 must not run P0292 again on its next invocation.**

### Handoff state

**Exact source obligation still open:** characterize all stationary ergodic CTMCs for which the all-finite-dimensional speed order holds.

**Frozen metric state:** `D_rev,0=0`, unchanged for six consecutive runs after its initial measurement.

**Recoveries used:** 1.

**Strongest established internal results to preserve:**

- all finite stationary reversible CTMCs have nonpositive first derivative at the frozen endpoint, giving `D_rev,0=0` sharply;
- the reversible three-state class is completely classified in the previous report by the slow eigenfunction endpoint-sign condition, with the repeated-eigenvalue case included;
- any three-state source-satisfier must have real nonzero spectrum;
- the one-way three-cycle bivariate order holds exactly on `Delta>=0, b>=mu_1`;
- the exact real-spectrum counterexample `Q_*` above must not be rediscovered as new work.

**Simplest source-faithful case still unproved:** prove or refute the **all-FDD** speed order for a bivariate-passing nonreversible one-way cycle, preferably the exact integer-rate example

\[
Q(1,10,1)=
\begin{pmatrix}
-1&1&0\\0&-10&10\\1&0&-1
\end{pmatrix}.
\]

Pairwise/concordance tests all pass by Theorem 6.1; any failure must therefore use at least three observation coordinates or a genuinely multivariate supermodular mechanism.

**Routes already materially tried and not to repeat mechanically:** frozen derivative dualization; second-order/equality-face analysis; reversible star spectral classification; three-time endpoint flow; path-space single-crossing decomposition; gradient/Metzler reversible reduction; the present complex-mode, real-spectrum-cycle, and one-way-cycle bivariate analysis.

**Promising fresh route for a future reassignee:** derive the three-time law of `Q(1,10,1)` in exact modal coordinates and attack the first genuinely three-variable supermodular extreme rays, rather than returning to pairwise covariance. That is a handoff suggestion only, not an instruction for NM13-01's next run.

**Ownership transition:** because NM13-01 is not permitted to edit shared roots, `operations/claims/P0292.md` is left untouched in this invocation. The structured `ledger_delta` below requests P26 to mark the claim as handed off/unassigned-for-fresh-route. This immutable report itself records the explicit six-run handoff and must be recovered by future ownership checks even if the shared claim file lags.

**Successor admission for NM13-01:** `ADMISSION_PENDING` after this handoff. No second claim is created in the same invocation. The next NM13-01 run must re-read the queue/intake deltas, canonical dedup keys, current claims/handoffs, and current literature, then select a genuinely eligible residue-0 CLOSABLE source or retain an admission cursor. This screening state does **not** inherit P0292's metric or stagnation counter.

## 10. Runtime/model-control status

The exposed task-control surface still provides prompt/title, timing/schedule fields, timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, and no authenticated per-run effort telemetry. Therefore `GPT-6 / maximum` remains a request in prompt text only. This invocation actually identifies as **GPT-5.6 Sol**, with reasoning level **UNVERIFIED**.

Making the requested setting enforceable would require an authorized product/workspace/API/admin surface that exposes model-family and reasoning controls together with runtime attestation. Historical repository policy records that one P26 scheduler ID returned `You cannot modify this task` in one authorization context and that another authorized context later succeeded; the legitimate workaround is the owning/authorized surface (or platform support), not duplicate-task creation or access-control bypass. No support escalation is claimed here.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-01
  category: CLOSABLE_OUTSIDE
  source_id: P0292
  claim_id: P0292
  canonical_dedup_key: characterize_ctmc_speed_monotonicity_in_supermodular_order
  canonical_sha256: 3aded70a56a908e9042798ee4a8ac614005a51635e52453716ea79167c073ae5
  shard_residue_mod_13: 0
  source_status: OPEN
  track_status: PARTIAL_HANDOFF
  metric_name: D_rev_0_normalized_frozen_limit_first_order_supermodular_speed_defect
  metric_before: 0
  metric_after: 0
  metric_movement: false
  unchanged_runs_since_metric_movement: 6
  stuck_recoveries_used: 1
  methods_tried:
    - 21: complex-spectrum/damped-oscillator reformulation; proved real spectrum necessary on three states
    - 23: sought a real-spectrum nonreversible failure; found exact Q(10,1,1) counterexample
    - 26: classified the entire positive-rate one-way three-cycle at the bivariate level
  new_internal_claims:
    - NM13-01-P0292-COMPLEX-SPECTRUM-NECESSARY-06
    - NM13-01-P0292-ONEWAY3-BIVARIATE-06
  exact_artifacts:
    script: proofnet24/NM13-01/artifacts/2026-09-18/p0292_nonrev_cycle_exact.py
    script_commit: 63de3fe3e8b991594bd3efa9f3d85a8af962e5bc
    output: proofnet24/NM13-01/artifacts/2026-09-18/p0292_nonrev_cycle_exact.out
    output_commit: 308a378af8e7f93c1245f377b838c69ed7223d48
    self_check: true
  audits:
    P26: NOT_REQUESTED_NOT_PASSED
    NM13-02: NOT_REQUESTED_NOT_PASSED
  prior_art_check: "bounded fresh search 2026-09-18; source-matching later resolution not recovered; novelty UNVERIFIED"
  rotation:
    required: true
    reason: CLOSABLE six consecutive unchanged runs
    handoff_recorded_here: true
    shared_claim_reconciliation_requested_from_P26: true
    successor_status_for_NM13_01: ADMISSION_PENDING
  preserved_simplest_open_case: "all-FDD speed order for nonreversible one-way cycle Q(1,10,1), which passes all two-time tests"
  next_for_NM13_01: "do not continue P0292; screen next genuinely unclaimed residue-0 CLOSABLE source after authoritative handoff/claim reconciliation"
```

**End of immutable run report.**
