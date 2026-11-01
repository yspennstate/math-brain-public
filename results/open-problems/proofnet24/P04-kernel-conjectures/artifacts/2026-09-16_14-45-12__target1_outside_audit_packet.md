Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; the scheduler exposes no model selector or reasoning-effort selector, so GPT-6 / maximum is requested but not claimed.

# P04 Target 1 / squared-ridge outside-audit packet

Date: 2026-09-16 14:45:12 +03:00 (Asia/Jerusalem)  
Repository: `yspennstate/math-open-problems`  
Branch: `master`  
Owner track: `proofnet24/P04-kernel-conjectures`  
Controlling fleet protocol: `operations/FLEET_2026-09-16.md`, blob `6cdbe40094b889a25df1264706dff55312601429`.

This packet freezes the only P04 scope authorized by the 2026-09-16 fleet reorientation. It is an audit request / closure packet, not a new theorem and not a request to restart the proof.

## 1. Fixed tracked quantity and frozen obligations

Tracked quantity: **number of required outside-audit obligations still unresolved for the frozen Target-1 claim package**.

Frozen obligation list:

1. `P04-T1-OUTSIDE-AUDIT-P26` — **SATISFIED** by `P26-AUDIT-P04-T1-ENDTOEND-17 = PASS` in `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_04-37-56__run-report.md`, creation commit `7127886502112192812294d55ed05862dc057b8b`. This audit covers both the optimized squared-ridge training-objective equivalence and the separately matched clean-test risk statement. Do **not** discard or restart this valid audit. Re-open it only if the second auditor identifies a concrete defect that affects the dependency chain it checked.
2. `P04-T1-OUTSIDE-AUDIT-P03` — **OPEN**. Under `operations/FLEET_2026-09-16.md`, the distinct registry-cycle auditor is P03. The requested deliverable is one genuinely independent end-to-end audit of the frozen claim package below, with an explicit PASS / FAIL / UNVERIFIED verdict and real source path, commit/blob, and claim IDs.

Therefore the frozen metric is currently

`outside-audit obligations unresolved = 1`.

The two outputs below are one claim package for closure purposes. The first P26 audit already checked both outputs, and the second auditor is asked to check both in one independent end-to-end review. P21 self/specialist audits do not count as the second OTHER-track audit.

## 2. Exact frozen theorem scope

### Assumptions

- Exactly two augmentations per original sample.
- Fixed augmentation strength `Delta > 0`.
- Fixed ridge parameter `lambda > 0`.
- Smooth bounded odd activation in the proved class, with `tanh` as the canonical example and the derivative bounds used by the Hermite/Stein estimates.
- Gaussian feature matrix entries iid `N(0,1/d)`.
- `n/d -> alpha > 0` and `m/d -> beta > 0`.
- Initially a unit-norm linear teacher `t_i = xi^T a_i`, `||xi||=1`.
- The two views of one original sample share the original latent `a_i`; the matched Gaussian surrogate preserves the corresponding shared latent component. View-private augmentation noises remain view-private.
- Put `N=2n`. The exact objective is

  `L_M(w) = (1/(2N)) sum_{i=1}^n sum_{j=1}^2 (t_i - x_{ij}^{M,T} w)^2 + (lambda/2)||w||^2`,

  so the per-view loss coefficient is exactly `1/(2N)=1/(4n)`.

### Conclusion A — optimized squared-ridge objective

For the actual nonlinear model `A` and the jointly matched correlated Gaussian surrogate `G`, the candidate-complete proof gives total replacement error

`| E L_A^* - E L_G^* | = O(d^{-1/2})`,

and the retained bounded-`C^2` test-function version has first-order `O(d^{-1/2})` and second-order `O(d^{-1})` error. The Lindeberg replacement unit is the **whole original-sample two-row block**, not an individual augmented view.

### Conclusion B — clean prediction risk

Clean population/test risk is a separate comparison, not a corollary of Conclusion A. The actual and Gaussian training models are coupled to a **jointly matched clean test surrogate**, including the teacher/test feature dependence required by the model. The retained theorem has the same leading `O(d^{-1/2})` transfer for bounded smooth tests of clean risk; an independent empirical clean-test block of size `M` adds the ordinary `O(M^{-1/2})` sampling term.

No claim is made here for ReLU, nonlinear teachers, vanishing ridge, an arbitrary number of augmentations, a coordinatewise Gaussian replacement, or independence of plus/minus channels.

## 3. Frozen dependency identifiers

The stable P04 claim identifiers to be checked are:

- `T1-EXACT-OBJECTIVE-NORMALIZATION`;
- `T1-TWO-VIEW-LOO-WOODBURY`;
- `T1-TOTAL-BLOCK-LINDEBERG`;
- `T1-SHARED-LATENT-PRESERVATION`;
- `T1-CLEAN-TEST-JOINT-MATCH`.

The newest complete P04 checkpoint before this packet is

`proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_13-46-59__run-report.md`,
creation commit `c3e1a07f60ec5fcf4e2a9cd11f6d0926ce192980`, blob `6ae13780900ecc81af61d744a910227c17f06aba`, with immutable readback receipt commit `3e94a51b50d0b581a9044694d740e479ced7d44c`.

The newest complete P21 specialist checkpoint is

`proofnet24/P21-kernel-cGEC/runs/2026-09-16/2026-09-16_14-17-15__run-report.md`,
creation commit `769bd546286b6989944e92c87d2d18c8afb38c4a`, readback receipt commit `ddf25fc9a8ba9d18bb9df0a92212bb8503173768`.

P21's newest support claims include

- `P21-RESOLVENT-FREEZING-WITHOUT-DECOUPLING-50`;
- `P21-CLEAN-JOINT-RESOLVENT-FREEZING-50`;
- `P21-EXACT-TOTAL-NORMALIZATION-50`.

These are useful independent strengthenings / simplifications. They are **not used to invalidate or restart** the earlier dependency chain already independently audited by P26. The second auditor may use the newest P21 route if desired, but must audit the frozen theorem scope, not merely one optional support lemma.

## 4. Exact audit checklist for P03

Please independently verify, without treating P26's PASS as proof:

1. **Primary-source normalization.** Dhifallah–Lu equation (3) has coefficient `1/(2 n ell)`; at `ell=2`, this is `1/(4n)=1/(2N)` with `N=2n`. Confirm the feature-entry variance convention `1/d` under the track notation.
2. **Source dependence structure.** The source correlated Gaussian surrogate shares the original-sample latent terms across both views and keeps view-private terms private. Confirm that the repository proof never replaces the two views independently.
3. **Exact block Woodbury identity.** With both rows deleted and global normalization retained, check

   `L_i^* - L_-^* = (1/(2N)) e^T (I_2 + Q)^{-1} e`,

   where `Q=(1/N)X_i B X_i^T`, `B=(lambda I + N^{-1}X_-^T X_-)^{-1}`.
4. **Total, not per-block, replacement scale.** Check the conversion from the unscaled current-block bracket discrepancy to the objective increment, and the full `n=N/2` telescope. In the newest P21 normalization certificate, a uniform unscaled bracket discrepancy `K/sqrt(d)` gives per-block cost `K/(2N sqrt(d))` and total first-order cost exactly `K/(4 sqrt(d))`.
5. **Dependence-aware moment control.** Check the teacher-feature Stein identity, the odd-Hermite cubic off-diagonal accumulation, and the diagonal/bilinear feature-norm terms without assuming independence between the current residual vector and leverage matrix or between the leave optimizer and feature columns.
6. **Clean risk is separate.** Check the clean-test comparison with its own matched test law and its own resolvent/bilinear terms. Do not accept training-objective equivalence as a substitute.
7. **No false shortcuts.** Reject coordinatewise Gaussianization, actual plus/minus independence, or a per-view Lindeberg unit.
8. **Quantifiers.** Confirm fixed `Delta>0`, fixed `lambda>0`, the stated smooth bounded odd activation class, `n/d -> alpha>0`, `m/d -> beta>0`, Gaussian feature entries of variance `1/d`, and a unit-norm linear teacher.

Requested audit result format:

- claim ID such as `P03-AUDIT-P04-T1-ENDTOEND-<run> = PASS` or `FAIL` / `UNVERIFIED`;
- exact P04/P21 source paths and commit/blob identifiers actually read;
- direct primary-source check;
- independent derivation/check of the normalization, block identity, total telescope and clean-test step;
- any defect localized to the smallest claim/dependency it affects.

A PASS on only a Target-4 P04 lemma, a P21 self-audit, or a narrow support lemma does not satisfy `P04-T1-OUTSIDE-AUDIT-P03`.

## 5. P26 request under the new fleet protocol

P26 already supplied the first qualifying audit. The request to P26 is therefore **not** to redo it. Please preserve `P26-AUDIT-P04-T1-ENDTOEND-17 = PASS` as outside-audit slot 1 when refreshing the fleet ledger. If P03 later records a concrete defect, re-open only the affected dependency and audit the repair; otherwise the existing PASS remains valid evidence.

## 6. Current literature/status check to be considered by auditors

The original 2021 PMLR paper explicitly labels the correlated Gaussian equivalence as a conjecture and leaves the dependent extension as future work. A bounded current search on 2026-09-16 also found Morisset–Durmus–Hardy, arXiv:2605.10290v1 (11 May 2026), which develops deterministic equivalents for regression with dependent/arbitrary data augmentation. Its main augmented loss is an **expectation over the augmentation randomness conditional on each training sample**, not the finite empirical `ell=2` two-draw objective frozen above. It is therefore relevant prior art and should be cited in a closure package, but on the checked formulation it does not directly subsume the finite-two-view squared-ridge theorem. If an auditor finds a theorem in that or another current paper that exactly covers the frozen finite-`ell=2` statement and hypotheses, mark the status `KNOWN` rather than `PROVED` and provide the precise theorem citation.

## 7. Closure action after the second audit

If `P04-T1-OUTSIDE-AUDIT-P03` is PASS and identifies no repair debt, the metric moves `1 -> 0`. Only then should P04 prepare the required self-contained closure folder (`paper_<name>/`) with the exact theorem scope, proof, source comparison, prior-art note, and the two outside-audit receipts. If the second audit FAILs, the metric remains 1 and P04 repairs only the cited defect before requesting re-audit.

**End of P04 Target-1 outside-audit packet.**