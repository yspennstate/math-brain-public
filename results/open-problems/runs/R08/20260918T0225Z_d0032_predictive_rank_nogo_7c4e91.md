Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **SCREEN MOVEMENT on D0032: a complete finite-predictive-rank no-go theorem is proved; every alpha-mixing finite-alphabet process whose conditional future laws have finite-dimensional signed-measure span is beta-mixing, hence Bernoulli. In particular no finite-hidden-state HMM / standard hidden-Markov sofic presentation can furnish a counterexample. D0032 remains HARD / NOT READY-CLOSABLE; no successor metric is admitted. I0082 remains RETIRED/FROZEN at 2/3 with retirement count 6. Methods B1, B4, B20.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, no reasoning-effort selector, and no completed-run effort telemetry, so I do not claim otherwise.

# R08 successor screen — D0032 / Ornstein finite-state strong-mixing question

## 1. Continuity, controls, and ownership

I did not reopen I0082 or the retired F0083 allocation route. The newest complete R08 report before this run is `runs/R08/20260918T0130Z_d0029_bconvex_reduction_a4c9f2.md`; that report left D0029 classified HARD / NOT READY and admitted no successor metric. The root R-series summary is stale by its own instructions, so continuity is taken from the newest own immutable report rather than the old scheduler title.

Before research I reread the required repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, the newest R08 report, recent neighboring ownership/rotation records, and the intake-D ledger containing D0032 and attempt D0032-A001.

The active-source exclusions remain unchanged: Hasebe--Ueda Problem 3.3 is a distinct posted result, R19's classical-convolution stable-law work is distinct, I0082 is frozen after its six-run handoff, and the old FPP/stable-allocation route is retired.

For D0032, direct fetch of `operations/claims/D0032.md` returned 404 at this run's current repository snapshot. Repository search recovered the intake/catalogue record but no canonical D0032 claim. This is bounded ownership evidence, not a global theorem of nonownership. I did **not** create a D0032 claim because the source remains theorem-scale HARD rather than honestly CLOSABLE.

Do not confuse D0032 with **I0032**, the unrelated Aldous--Fill problem currently carrying its own canonical claim/history.

## 2. Exact source and recovered prior attempt

D0032 is Bradley (2005), Question 4, Section 2.7, PDF p. 11:

> If a strictly stationary finite-state random sequence is strongly mixing in Rosenblatt's sense, alpha(n) -> 0, must it be isomorphic to a Bernoulli shift?

The source says the question remains open even if alpha-mixing is replaced by rho-mixing or rho-star-mixing, while sufficiently fast alpha-decay gives positive results. The recovered intake attempt D0032-A001 already identified the honest bottleneck: Bernoulli follows from a very-weak-Bernoulli/weak-Bernoulli criterion, but the elementary block-coupling route accumulates mixing errors across a growing block and therefore needs a rate; qualitative alpha(n)->0 alone does not make the sum small.

I preserve that obstruction and do not restart it.

## 3. Current-literature check

I reran bounded exact-phrase/current-author searches for the source question and nearby notions. The original Bradley survey remains a direct statement of Question 4. The search also recovered the classical very-weak-Bernoulli/Bernoulli criterion and Burton--Denker--Fiebig's finite-state phi-mixing examples showing that naive rate-based VWB control cannot simply be made rate-free. A 2025 paper on Doeblin measures resolves other ergodic-theory questions but did not supply a source-matching resolution of Bradley Question 4. I also checked hidden-Markov/sofic literature because that is the candidate class attacked below; modern sources still identify finite-state hidden Markov measures with the standard sofic-measure framework, and older sofic-process work organizes such processes by finitely many future measures.

Search strings included combinations of:
- `Bradley Question 4 strong mixing finite-state Bernoulli shift`;
- `strongly mixing finite-state process Bernoulli shift Ornstein open`;
- `finite-state phi mixing not very weak Bernoulli rate`;
- `hidden Markov sofic measure Bernoulli mixing`;
- `sofic random processes future measures`.

No later primary source claiming to settle the unrestricted D0032 statement was found in this bounded pass. This is **OPEN_CURRENT_BOUNDED** evidence only, not a worldwide novelty certificate.

**Priority disclaimer.** I make no priority claim for the finite-hidden-state/HMM corollary below; it is close to standard Markov/sofic folklore and may well follow from classical results in stronger form. The useful repository contribution is the self-contained finite-predictive-span reduction and the exact identification of where it stops.

## 4. B1 — change category: predictive signed-measure geometry

Let `A` be the finite output alphabet and let

\[
E=A^{\mathbb N_0}
\]

be the one-sided future path space. Put

\[
\mathcal P=\sigma(X_k:k\le 0),
\qquad
\mu=\operatorname{Law}(X_0,X_1,\ldots).
\]

For `n>=1`, choose a regular conditional future law

\[
Q_n(\omega,\cdot)
=
\operatorname{Law}\big((X_n,X_{n+1},\ldots)\mid\mathcal P\big)(\omega),
\]

viewed, after shifting time, as a probability measure on the fixed space `E`.

Define the **predictive signed-measure span**

\[
V_X
=
\operatorname{span}\{Q_n(\omega,\cdot)-\mu:\ n\ge1,\ \omega\text{ outside the chosen null sets}\}
\]

inside the vector space of finite signed measures on `E` having total mass zero.

This recasts Bradley's qualitative alpha-to-Bernoulli question as a norm-comparison problem on the family of conditional future laws. Alpha-mixing controls each scalar evaluation of these signed measures by a past event; beta-mixing controls their total-variation norm. Infinite dimensionality is exactly the place where pointwise control of all evaluations need not give a uniform norm estimate.

## 5. B4 — complete theorem in the finite-predictive-rank class

### Theorem (finite predictive rank forces absolute regularity)

Let `X=(X_k)_{k\in\mathbb Z}` be a strictly stationary process on a finite alphabet. Assume

\[
\dim V_X=d<\infty.
\]

If `X` is strongly mixing,

\[
\alpha_X(n)\to0,
\]

then in fact it is absolutely regular,

\[
\beta_X(n)\to0.
\]

More quantitatively, there is a finite constant `C_X` depending only on the finite-dimensional normed space `V_X` such that

\[
\beta_X(n)\le C_X\,\alpha_X(n)
\qquad(n\ge1).
\]

Consequently, for a finite alphabet, `X` is weak Bernoulli and hence isomorphic to a Bernoulli shift.

### Proof

For a total-mass-zero finite signed measure `eta` on `E`, define

\[
\|\eta\|_*:=\sup_{B\in\mathcal B(E)}|\eta(B)|.
\]

This is the usual total-variation distance norm on differences of probability measures (equivalently one half of the total-variation norm under the alternate signed-measure convention). Restricted to `V_X` it is a genuine norm.

For each measurable `B\subseteq E`, let

\[
e_B(\eta)=\eta(B).
\]

The family `{e_B}` separates points of `V_X`: if every measurable-set evaluation of a finite signed measure vanishes, then the measure is zero. Since `V_X` is `d`-dimensional, finite-dimensional linear algebra gives measurable sets

\[
B_1,\ldots,B_d\subseteq E
\]

such that

\[
T:V_X\to\mathbb R^d,
\qquad
T(\eta)=(\eta(B_1),\ldots,\eta(B_d))
\]

is injective. All norms on a finite-dimensional space are equivalent, so there is `K_X<\infty` with

\[
\|\eta\|_*
\le
K_X\max_{1\le j\le d}|\eta(B_j)|
\le
K_X\sum_{j=1}^d|\eta(B_j)|
\tag{1}
\]

for all `eta\in V_X`.

Fix `n` and `j`, and define the past-measurable random variable

\[
Z_{n,j}(\omega)
:=
(Q_n(\omega)-\mu)(B_j).
\]

Its mean is zero by the tower property. For every `A\in\mathcal P`, writing `F_{n,j}` for the future event that the shifted future belongs to `B_j`,

\[
\begin{aligned}
|\mathbb E[1_A Z_{n,j}]|
&=
|\mathbb P(A\cap F_{n,j})-\mathbb P(A)\mathbb P(F_{n,j})|\\
&\le \alpha_X(n).
\end{aligned}
\tag{2}
\]

Because `Z_{n,j}` is `\mathcal P`-measurable, the event `{Z_{n,j}>0}` belongs to `\mathcal P`. Taking that event in (2) and using `EZ_{n,j}=0`,

\[
\mathbb E|Z_{n,j}|
=2\mathbb E[Z_{n,j}1_{\{Z_{n,j}>0\}}]
\le 2\alpha_X(n).
\tag{3}
\]

Now use the standard conditional-law representation of absolute regularity on the standard Borel future space `E`:

\[
\beta_X(n)
=
\mathbb E\,\|Q_n-\mu\|_*
\tag{4}
\]

with Bradley's standard normalization; under the alternative convention for total variation one merely changes the harmless global factor two.

Since `Q_n(\omega)-\mu\in V_X`, equations (1)--(4) give

\[
\begin{aligned}
\beta_X(n)
&\le
K_X\sum_{j=1}^d\mathbb E|Z_{n,j}|\\
&\le
2dK_X\alpha_X(n).
\end{aligned}
\]

Thus `alpha_X(n)->0` implies `beta_X(n)->0`.

For finite-state stationary processes, absolute regularity is the weak-Bernoulli property in the standard partition formulation, and the classical Ornstein/Friedman--Ornstein theory gives Bernoullicity. This proves the theorem. `square`

### Corollary (finite hidden state cannot refute D0032)

Suppose `X` is the finite-alphabet observation process of a stationary hidden Markov model with a finite hidden state space `{1,...,M}`. Let

\[
\nu_i
=
\operatorname{Law}((X_0,X_1,\ldots)\mid Z_0=i)
\]

be the future observation law started from hidden state `i`. By the Markov property, for every observed past and every `n`,

\[
Q_n(\omega,\cdot)
=
\sum_{i=1}^M
\mathbb P(Z_n=i\mid\mathcal P)(\omega)\,\nu_i.
\]

The stationary future law `mu` is another convex combination of the same `nu_i`. Therefore

\[
Q_n(\omega)-\mu
\in
\operatorname{span}\{\nu_i-\mu:1\le i\le M\},
\]

so

\[
\dim V_X\le M-1.
\]

Hence every alpha-mixing finite-output, finite-hidden-state HMM is beta-mixing and Bernoulli.

The same conclusion applies to the standard finite hidden-Markov / finite-future-measure presentations usually called sofic processes. I deliberately avoid asserting more than this presentation-level statement because terminology differs across the ergodic-theory and symbolic-dynamics literatures.

A finite-order Markov chain is the special case obtained by taking the hidden state to be the last `r` output symbols, so it too cannot be a counterexample.

## 6. B20 — why this algorithm fails in the unrestricted problem

The theorem does **not** solve Bradley Question 4. Its stopping point is exact and informative.

The finite output alphabet does **not** imply finite predictive rank. Even when each single symbol takes only finitely many values, the conditional law of the entire infinite future given the entire past can vary through an infinite-dimensional family of signed measures. In that situation there need not exist finitely many future events `B_1,...,B_d` for which

\[
\|Q_n-\mu\|_*
\le C\max_j |(Q_n-\mu)(B_j)|
\]

with a dimension-free constant `C`.

That is precisely the old rate obstruction in a new language:

- alpha-mixing gives small covariance against **one** future event at a time;
- beta/weak-Bernoulli asks for uniform control of the **whole** conditional future law;
- finite predictive rank lets finite-dimensional norm equivalence bridge the two;
- unrestricted finite-state processes may have infinitely many predictive directions, and the bridge constant can diverge with the approximation dimension.

Thus any counterexample to D0032 must satisfy the necessary structural condition

\[
\boxed{\dim V_X=\infty.}
\]

Equivalently: no counterexample can come from a finite hidden-state mechanism, finite-order Markov mechanism, or any other model whose conditional future distributions live in one fixed finite-dimensional affine space.

A positive solution would need a genuinely new **dimension-free compactness or approximation principle** converting alpha-control of event evaluations into weak-Bernoulli control over an infinite-dimensional family. A negative solution must build a finite-output process with infinite predictive complexity while keeping `alpha(n)->0` and still violating Bernoullicity. This is substantially sharper than simply saying that a rate-free d-bar estimate is missing.

## 7. Method accounting

- **B1 CHANGE THE CATEGORY.** Rewrote the ergodic/isomorphism question as geometry of conditional future signed measures. Outcome: produced the predictive-rank invariant `dim V_X` and separated scalar alpha-control from total-variation beta-control.
- **B4 PROVE SOMETHING WEAKER, COMPLETELY.** Proved the finite-predictive-rank theorem and finite-hidden-state HMM corollary with a complete on-page argument. Outcome: an entire natural counterexample class is eliminated.
- **B20 FIND WHY THE ALGORITHM FAILS.** Located the exact extension failure: predictive rank can be infinite despite a finite output alphabet, so finite-dimensional norm equivalence supplies no uniform constant. Outcome: the unrestricted source problem remains HARD rather than being mislabeled solved.

This triple is different from the preceding R08 triple B18/B11/B21.

## 8. Disposition

D0032 is **OPEN_CURRENT_BOUNDED / OWNERSHIP_CLEAR_BOUNDED / HARD / NOT_READY_CLOSABLE**. I therefore create no exclusive claim, no artificial source metric, and no stagnation count. The theorem above is a screening reduction, not source closure.

No exact-arithmetic checker is created: the new result is an analytic finite-dimensional measure-theoretic theorem and has no finite computational core requiring certification. Manufacturing a checker here would violate the owner instruction to spend effort on ideas rather than receipts.

The next R08 invocation should continue the queue/intake admission cursor beyond already screened claimed, resolved, retired, or theorem-scale HARD rows, unless a genuinely free READY+CLOSABLE successor has appeared in the repository. It must not restart D0032 simply because this reduction is interesting.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  original_target:
    id: I0082
    status: RETIRED_FROZEN
    metric: obligations_proved
    value: 2/3
    retirement_count: 6
  screened_target:
    id: D0032
    source: Bradley_2005_Question_4
    status_before: source_says_open_unverified
    status_after: OPEN_CURRENT_BOUNDED__HARD__NOT_READY_CLOSABLE
    ownership: no_canonical_D0032_claim_found_in_bounded_snapshot
    active_claim_created: false
    metric_before: null
    metric_after: null
    stagnation_count: null
    mathematical_movement:
      - finite_predictive_rank_alpha_implies_beta
      - finite_hidden_state_HMM_counterexample_class_eliminated
      - any_D0032_counterexample_requires_infinite_predictive_rank
    priority_claim: none
  methods: [B1, B4, B20]
  finite_checker: not_applicable_analytic_theorem
  root_files_modified: false
  peer_files_modified: false
  next_action: continue_fresh_READY_CLOSABLE_successor_admission_screen
```

## 10. Model / scheduler control boundary

The available task-management surface still exposes title, prompt, schedule/timing mode, and enabled state, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed-duration field. Therefore GPT-6/maximum remains a prompt request rather than a setting I can certify.

The historical `You cannot modify this task` response is an authorization boundary, not a model-setting workaround. The legitimate remedies are to operate from the authorized owning context, use supported ownership/admin transfer, or escalate to platform support. Duplicating a task, editing GitHub, or bypassing permissions does not enforce the runtime model.
