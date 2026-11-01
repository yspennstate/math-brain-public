# T357: original scope and primary-source comparison

This report concerns the Gaussian, nonlinear random-feature continuation. It does not recategorize the earlier categorical example or add T228 a second time.

## Exact target

The preserved registry row is in `followup/source_registry_rows.json`, copied from `a03/registry422.jsonl` (SHA-256 `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0`). Its identifier is **T357**, title **Overconfidence of overparameterized classifiers**, list **TOP200_DL**. Its rank 335 is in the combined registry, not its within-list rank.

The operative request is a theorem for a two-layer classifier trained by gradient descent on cross-entropy, in a solvable random-feature or single-index regime, with calibration characterized by sample/input ratio, width, and training time, and an answer concerning early stopping. It does not require training both layers: random features are explicitly permitted. It does require the training algorithm and all asymptotic restrictions to be stated. A fixed first-update result alone does not address the entire training-time request.

The source row itself marks its open-status and source locator as unverified. Therefore completion of this user-curated question and proof of a previously recognized, still-open published conjecture are different assertions. The latter requires additional evidence; an unsuccessful literature search is not a proof of novelty.

## Primary literature checked

1. **Bai, Mei, Wang, Xiong (ICML 2021), “Don't Just Blame Over-parametrization for Over-confidence.”** [arXiv:2102.07856v2](https://arxiv.org/abs/2102.07856v2). The original target's cited source proves overconfidence for proportional logistic regression, including an underparameterized, realizable regime. Its result does not by itself supply a finite-iteration nonlinear random-feature GD calibration trajectory. This comparison does not assert that the paper posed the registry wording verbatim.

2. **Clarté, Loureiro, Krzakala, Zdeborová (AISTATS 2023), “On double-descent in uncertainty quantification in overparametrized models.”** [Primary proceedings and full paper](https://proceedings.mlr.press/v206/clarte23a.html). The paper already analyzes random-feature uncertainty and calibration. Its Theorem 3.1 and Corollary 3.2 give asymptotic estimator and calibration descriptions for ERM and Bayesian constructions; Appendix B derives fixed-point equations with AMP and discusses their rigorous foundations. Thus neither “first calibration theorem for random features” nor “first Gaussian overlap formula for calibration” is an acceptable novelty claim here. The inspected result does not characterize the ordinary reused-data GD trajectory at every finite iteration or uniform model-conditional calibration over data-dependent stopping times.

3. **Ji, Li, Telgarsky (NeurIPS 2021), “Early-stopped neural networks are consistent.”** [Primary paper](https://proceedings.neurips.cc/paper/2021/file/0e1ebad68af7f0ae4830b7ac92bc3c6f-Paper.pdf). This proves consistency, including approximation of conditional probabilities, for early-stopped shallow networks under its scaling and temperature choices. A fixed-proportional-ratio obstruction with fixed positive learning scale is not a contradiction: the asymptotic hypotheses differ. We must not claim that early stopping can never calibrate neural networks in general.

4. **Clarté et al. (UAI 2023), “Expectation consistency for calibration of neural networks.”** [Primary proceedings](https://proceedings.mlr.press/v216/clarte23a.html). This studies post-training calibration by rescaling and compares it with temperature scaling. It is relevant context for the scalar overconfidence calculation, but does not establish the proposed original-model training-time theorem.

5. **Li and Sur (NeurIPS 2025), “Optimal and Provable Calibration in High-Dimensional Binary Classification: Angular Calibration and Platt Scaling.”** [Primary proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/debdbf60e8c45811886f7623b07e75df-Abstract-Conference.html). This concerns Gaussian linear scores and provably calibrated postprocessing. We make no novelty claim for the conditional Gaussian calibration formula or for the possibility of calibrated postprocessing.

6. **Wang, Zhong, Fan, “Universality of Approximate Message Passing algorithms and tensor networks.”** [arXiv:2206.13037v5](https://arxiv.org/html/2206.13037v5). Proposition D.1(b2), Theorem 2.22, and the rectangular Onsager prescriptions are mathematical inputs, not new results of this work. Their application requires more than a singular-value law: signed-permutation symmetry, entry bounds for matrix powers, independent side information, and the correct causal algorithmic embedding must all be verified. Those verifications are part of the new proof files and independent audits.

## What would constitute full completion of this row

The acceptance record must verify all of the following together: a genuine Gaussian-input tanh random-feature network; the exact ordinary full-batch GD recursion from zero; deterministic finite-time state evolution with width and sample ratios present; convergence of exact unbinned calibration conditional on the trained model, not just a weak-law lower bound; a signed overconfidence conclusion with its tuning stated; and an explicit early-stopping answer including the range of times and aspect ratios covered.

For the proposed theorem, arbitrary fixed finite horizons may allow any positive finite aspect ratios. A stronger uniform-in-time statement uses a sufficiently large sample-to-width ratio and a stable, fixed positive step. These are substantive mathematical restrictions and must appear in the theorem and user-facing description. No assertion for feature learning, every architecture, every step schedule, or every overparameterized late-time limit follows from this regime.

The source search found related established results and did not certify publication novelty. A final proof can be accepted as an internally checked mathematical answer to the precise T357 regime while still requiring external expert review and a broader novelty assessment before being announced as a new resolution of a published open problem.
