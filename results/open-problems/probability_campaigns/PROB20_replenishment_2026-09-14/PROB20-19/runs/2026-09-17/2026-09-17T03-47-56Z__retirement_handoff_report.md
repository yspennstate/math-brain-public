Model actually run: **GPT-5.6 Sol**. Reasoning/effort: **UNVERIFIED**. GPT-6 / maximum was requested, but the exposed scheduler/runtime surface provides no authenticated model selector or reasoning-effort selector. **Frozen metric: NO MOVEMENT, `(-1/2500,0) -> (-1/2500,0)`; supported consecutive no-movement count `5 -> 6`; methods: B9, B14, B27.** B9 was the only Section-B label not previously used on this target; recovered PROB20-19 history shows the other 29 labels had already appeared, so B14 and B27 below are genuinely new subroutes inside previously used categories, not falsely claimed globally-unused labels.

# PROB20-19 sixth-no-movement retirement handoff

Problem/source: **Stéphane Mallat and Ofer Zeitouni (2011), arXiv:1109.0489, Conjecture 1.** Exact target: whether, for a centered Gaussian vector with fixed covariance eigenvalues, the covariance eigenbasis maximizes the expected sum of the `d` largest squared coordinates among all orthogonal bases. Mathematical status: **PARTIAL / SOURCE OPEN**. Operational research status after this run: **RESEARCH_RETIRED_HANDOFF / ROTATION_WAIT_SUCCESSOR_ADMISSION_REQUIRED** under the owner-installed six-consecutive-no-movement rule. This is not a source-level proof, refutation, or literature-resolution claim.

## 1. Recovery and pinned state

Captured pre-research `master` snapshot:

`844303da1245be88f3e944f3aebe765560b52ee0`.

At that snapshot I recovered the required campaign/control surfaces, including `operations/VISIBLE_FLEET_2026-09-16.md`, `QUEUE.md`, root `POSTED.md` and `RESULTS.md`, `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, path-scoped own history, and current neighboring Gaussian/transport evidence. The latest own checkpoint is

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-19/runs/2026-09-17/2026-09-17T02-33-26Z__report.md`

at creation commit

`94dd1f7ec65c02a0e8d4222b84a0b9b7673bc897`.

That report fixed the retained metric at `(-1/2500,0)` and the supported unchanged count at 5, and supplied the exact finite `p=3,d=2` orthant/truncated-normal evaluator. Nothing in this run certifies a source-valid rotated-basis excess closer to zero or positive, so the frozen metric does not move.

The current coordinator/admission evidence at the captured snapshot does **not** expose a candidate that is simultaneously source-current, ownership-clear, unassigned, READY, and CLOSABLE OUTSIDE. In particular, current screening marks leading queue candidates as owned, source-held, substantially resolved, or genuinely HARD. Therefore this report retires active PROB20-19 research but does **not** fabricate a successor or inherit the old metric.

## 2. Dated current-literature check

Fresh 2026-09-17 searches confirm the following scope distinctions.

- Mallat--Zeitouni (2011), arXiv:1109.0489, is the exact conjectural source.
- Gao--Ji--Liu, arXiv:2607.15035, submitted 2026-07-16, prove a `1+O(d^{-1/2})` approximation to the retained-energy conjecture. That is not the exact constant-one statement.
- Litvak--Tikhomirov prove a universal-constant comparison for dependent-coordinate order statistics; again this is not constant one.
- Kunisky (2026), arXiv:2605.02023, disproves a different fixed-correlation Gaussian-minimum conjecture. That does not refute the fixed-spectrum Mallat--Zeitouni problem.

No exact proof or source-valid counterexample was found in the bounded current search. This negative search is not a novelty certificate.

## 3. Mathematical idea before code: condition on magnitudes, randomize only signs

For `a=(a_1,...,a_p) in R_+^p`, define

\[
\Phi_d(x)=\sum_{j=1}^d j\text{-}\max_i\, x_i^2
\]

(the sum of the `d` largest squared coordinates), and for `Q in O(p)` define the conditional sign gap

\[
\Delta_Q(a)
:=\mathbb E_{\varepsilon}\Phi_d\!\bigl(Q(\varepsilon\odot a)\bigr)-\Phi_d(a),
\tag{3.1}
\]

where the coordinates of `epsilon` are independent uniform signs.

For the actual fixed-spectrum Gaussian problem, write

\[
X=\Lambda^{1/2}Z,
\qquad A_i=\sqrt{\lambda_i}|Z_i|.
\]

The Gaussian signs are independent of the magnitudes, hence exactly

\[
\boxed{
F_d(Q;\Lambda)-F_d(I;\Lambda)
=\mathbb E_A\,\Delta_Q(A).
}
\tag{3.2}
\]

This is a legitimate reformulation retaining the full Gaussian law. It suggests a strong possible proof route: prove `Delta_Q(a)<=0` pointwise for every magnitude vector. B9 attacks that stronger statement first.

## 4. B9 RANDOMIZE -- exact refutation of pointwise conditional-sign domination

Take `p=3,d=2`, magnitude vector

\[
a=(1,1,1),
\]

and the exact rational orthogonal matrix

\[
Q=
\begin{pmatrix}
3/5&4/5&0\\
-4/13&3/13&12/13\\
48/65&-36/65&5/13
\end{pmatrix}.
\tag{4.1}
\]

The exact checker verifies `Q^TQ=I`. For the eight sign vectors `epsilon in {+-1}^3`, the squared minimum coordinate of `Q epsilon` is, in exact arithmetic,

\[
\frac{1369}{4225},\frac1{25},\frac1{25},\frac1{25},
\frac1{25},\frac1{25},\frac1{25},\frac{1369}{4225}.
\tag{4.2}
\]

Therefore

\[
\mathbb E_\varepsilon\min_i (Q\varepsilon)_i^2
=\frac{469}{4225}.
\tag{4.3}
\]

Before rotation the minimum squared coordinate is exactly 1. Since `Q` is orthogonal and `||epsilon||_2^2=3`, in dimension three

\[
\Phi_2(Q\varepsilon)=3-\min_i(Q\varepsilon)_i^2.
\]

Thus

\[
\mathbb E_\varepsilon\Phi_2(Q\varepsilon)
=3-\frac{469}{4225}
=\frac{12206}{4225},
\]

while

\[
\Phi_2(\varepsilon)=2.
\]

Hence the exact conditional-sign gain is

\[
\boxed{
\Delta_Q(1,1,1)=\frac{3756}{4225}>0.
}
\tag{4.4}
\]

So the strong pointwise statement

\[
\Delta_Q(a)\le0\quad\forall a
\]

is false, and false by a large rational margin. By continuity, the conditional integrand is positive on an open neighborhood of `(1,1,1)`.

This does **not** refute Mallat--Zeitouni: equation (3.2) still averages over the correct half-normal magnitude distribution, and positive magnitude regions may be outweighed by negative ones. The result instead proves that any successful sign-conditioning proof must exploit cancellation across magnitudes rather than establish pointwise domination.

Exact artifact:

`artifacts/2026-09-17T03-47-56Z__b9_sign_orbit_exact_check.py`

creation commit `58a9e9384bf3c53a84609845b1ffb0d5b9f90810`, readback blob `e72d68b76bade6769055cd39a4efe6048be50c0d`.

Executed exact output:

`artifacts/2026-09-17T03-47-56Z__b9_sign_orbit_exact_check_results.txt`

creation commit `d11a31627cdcd4a2a4f64b441990fc93806ec425`, readback blob `440ce501229b3d8d338c1ccda18ee77b5c51617c`.

The output records `ALL_EXACT_CHECKS_PASS`.

## 5. B14 FIND THE GROUP ACTING -- why orthostochastic averaging does not repair B9

The natural symmetry quotient is the hyperoctahedral sign action. Set

\[
M=Q\circ Q,
\]

where `circ` denotes entrywise square. Orthogonality makes `M` doubly stochastic. For `Y=Q(epsilon odot a)`, sign averaging gives

\[
\mathbb E_\varepsilon Y_i^2=(Ma^2)_i.
\tag{5.1}
\]

The sum of the `d` largest coordinates is a convex symmetric function. Therefore Jensen gives only

\[
\operatorname{Top}_d(Ma^2)
\le
\mathbb E_\varepsilon\operatorname{Top}_d(Y_1^2,...,Y_p^2),
\tag{5.2}
\]

while Hardy--Littlewood--Polya majorization gives

\[
Ma^2\prec a^2
\quad\Longrightarrow\quad
\operatorname{Top}_d(Ma^2)
\le
\operatorname{Top}_d(a^2).
\tag{5.3}
\]

These are two lower bounds from the same middle quantity; they do **not** compare the desired conditional expectation from above with the KL value. The rational witness in (4.4) shows that the Jensen gap can be large enough to reverse the hoped-for sign. Thus a proof based only on the orthostochastic matrix `Q circ Q`, diagonal variances, or sign-orbit barycenters necessarily discards the decisive fluctuation information.

This B14 subroute is distinct from the earlier matching-support B14 use: here the group quotient itself is used to diagnose why the sign-randomization proof cannot close.

## 6. B27 SWAP THE QUANTIFIERS -- compact signed angular integral is the correct residual object

Write a standard Gaussian as

\[
Z=RU,
\]

where `U` is uniform on `S^{p-1}`, `R>=0` is independent, and `E R^2=p`. Decompose `U=epsilon odot W`, where `W=|U|` lies in the positive spherical orthant and `epsilon` is an independent uniform sign vector. Since `Phi_d` is 2-homogeneous, (3.2) becomes

\[
\boxed{
F_d(Q;\Lambda)-F_d(I;\Lambda)
=p\,\mathbb E_W
\Delta_Q\!\left(\sqrt\lambda\odot W\right).
}
\tag{6.1}
\]

This exchanges an impossible pointwise sign claim for the actual integrated claim over a **compact positive spherical orthant**. In `p=3,d=2`, the remaining universal statement is precisely

\[
\boxed{
\mathbb E_{W\in S^2_+}
\Delta_Q(\sqrt\lambda\odot W)\le0
\quad
\text{for every }\lambda_1,\lambda_2,\lambda_3>0,\ Q\in O(3).
}
\tag{6.2}
\]

The exact B9 witness proves the integrand itself has positive patches. In the isotropic case the whole integral is exactly zero by rotational invariance. Earlier task-local near-isotropy work shows sufficiently small non-scalar spectral perturbations favor KL. Therefore the first possible source counterexample must arise through a genuinely finite anisotropic redistribution in which the positive sign-orbit patches outweigh all negative patches.

This is the cleanest handoff formulation I found. It preserves the exact fixed-spectrum Gaussian dependence and removes all unbounded radial variables.

## 7. Exact blocking statement and route audit for handoff

The smallest global unresolved obligation can be written as (6.2). A concrete two-angle benchmark lying in the previously identified variance-inversion geometry is

\[
\boxed{
\Lambda=\operatorname{diag}(2,1,3),
\qquad
Q(\alpha,\beta)=G_{23}(\beta)G_{12}(\alpha),
\qquad
(\alpha,\beta)\in(0,\pi/2)^2.
}
\tag{7.1}
\]

The task-local route audit now reads:

1. Mallat--Zeitouni's invalid independent-same-marginals replacement cannot be used for `d>1`.
2. The exact one-Givens theorem is safe but cannot be naively iterated through overlapping supports.
3. A naive Jacobi/diagonalization monotonicity route has an exact wrong-sign obstruction in recovered history.
4. Matching-support, fresh-leaf, repeated-eigenvalue/spike, balanced-spike, near-isotropy, and Schur--Horn safe-ball theorems certify large classes but leave genuine three-distinct-spectrum overlap.
5. Pointwise threshold stochastic domination is false; recovered exact p=4 work contains a certified threshold reversal.
6. Endpoint small-threshold and large-threshold signs for the complementary `d=p-1` problem do not control the intermediate signed area.
7. The exact `p=3,d=2` finite orthant evaluator removes the integration obstacle but has not yielded a global extremization proof.
8. This run adds another exact obstruction: even after conditioning on all Gaussian magnitudes, pointwise Rademacher-sign domination is false by (4.4).

A full proof therefore needs a **global cancellation principle over the half-normal/spherical magnitude law** that keeps the dependence between the selection event and the rotated coordinates. A full counterexample needs a rigorously certified positive value of the integrated expression (6.1), not a positive conditional patch, Monte Carlo estimate, or altered covariance spectrum.

Nearest solved/partial literature analogues do not contain this ingredient: source `d=1` is known exactly; Litvak--Tikhomirov lose a universal constant; Gao--Ji--Liu lose a `1+O(d^{-1/2})` factor through Schur--Horn/correlation-gap relaxation. Task-local exact safe classes retain dependence but do not cover arbitrary three-distinct overlap.

## 8. Retirement / successor gate

This is the sixth consecutive supported run with unchanged frozen metric after the last reset:

`0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6` across the retained post-reset sequence.

Per the installed owner rule, active research on Mallat--Zeitouni in this native slot is now **retired with handoff**. This is an operational retirement, not a mathematical claim that the conjecture is solved or hopeless.

At captured snapshot `844303da1245be88f3e944f3aebe765560b52ee0`, current repository admission evidence does not provide a lawful source-verified + current-status-verified + ownership-clear + READY + CLOSABLE OUTSIDE successor. Therefore:

- do not start a seventh PROB20-19 research run;
- do not inherit `(-1/2500,0)` into any successor;
- do not steal a claimed target or relabel a HARD/PENDING/HOLD target as CLOSABLE;
- keep the native hourly slot available as a bounded successor-admission gate until a lawful successor exists.

## 9. Scheduler/model control status

The exposed task controls still provide title/prompt/schedule/timing/enabled-state style fields but **no model selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. GPT-6 / maximum can be requested in prompt text but cannot be enforced or verified from this surface. Actually changing that requires an owner/platform scheduler surface exposing those fields and runtime telemetry.

Historical `You cannot modify this task` results for protected tasks such as one P26 context are authorization-context boundaries. The legitimate remedy is the owning/authorized context, explicit permission transfer, or platform support; duplication or bypass is not permitted.

## 10. ledger_delta

```yaml
ledger_delta:
  native_task_id: 6aa7b517489c8191a5250c9384e9b33c
  target_id: PROB20-19
  source: "Mallat--Zeitouni (2011), arXiv:1109.0489, Conjecture 1"
  captured_master: 844303da1245be88f3e944f3aebe765560b52ee0
  previous_report_path: "probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-19/runs/2026-09-17/2026-09-17T02-33-26Z__report.md"
  previous_report_commit: 94dd1f7ec65c02a0e8d4222b84a0b9b7673bc897
  frozen_metric:
    before: "(-1/2500,0)"
    after: "(-1/2500,0)"
    movement: false
  supported_consecutive_no_movement:
    before: 5
    after: 6
  methods:
    - "B9: conditional Rademacher-sign randomization; pointwise domination exactly refuted"
    - "B14: new hyperoctahedral/orthostochastic sign-orbit subroute; identified irreparable Jensen/majorization direction mismatch"
    - "B27: new pointwise-to-integrated quantifier swap; exact compact positive-orthant signed integral handoff"
  exact_artifacts:
    checker:
      path: "probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-19/artifacts/2026-09-17T03-47-56Z__b9_sign_orbit_exact_check.py"
      creation_commit: 58a9e9384bf3c53a84609845b1ffb0d5b9f90810
      readback_blob: e72d68b76bade6769055cd39a4efe6048be50c0d
    output:
      path: "probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-19/artifacts/2026-09-17T03-47-56Z__b9_sign_orbit_exact_check_results.txt"
      creation_commit: d11a31627cdcd4a2a4f64b441990fc93806ec425
      readback_blob: 440ce501229b3d8d338c1ccda18ee77b5c51617c
  mathematical_status: PARTIAL_SOURCE_OPEN
  operational_status: RESEARCH_RETIRED_HANDOFF_ROTATION_WAIT_SUCCESSOR_ADMISSION_REQUIRED
  closure_audits: []
  successor:
    admitted: false
    metric: UNMEASURED
    reason: "no source-current, ownership-clear, READY + CLOSABLE OUTSIDE candidate verified at captured snapshot"
  source_audit_refs:
    - "Mallat--Zeitouni 2011 arXiv:1109.0489"
    - "Gao--Ji--Liu 2026 arXiv:2607.15035 (approximation only)"
    - "Litvak--Tikhomirov 2018 universal-constant comparison"
    - "Kunisky 2026 arXiv:2605.02023 (different fixed-correlation Gaussian-minimum problem)"
```

No shared root ledger, peer report, historical report, Gmail/email, Drive item, public page, workflow, permission, credential, or schedule was edited in producing this handoff.
