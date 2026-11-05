# Referee review of T357 (agent H, 3 Nov 2026)

The check notes, scripts and outputs named below are in this folder.

Package: `results/frontier-2026-10/2026-10-23-t228-closure-30-agents/fullproof/` in this repository.
- The synthesis is `T357_THEOREM_AND_SYNTHESIS.md`, the text pinned for this review.
- The combined proof `T357_GAUSSIAN_COMPLETE_PROOF.md` is 3,080 lines.

## Conflict check

No file in `fullproof/` or `continuation/` names the reviewer. No conflict on T357.

## The question as catalogued

Row T357 of `results/frontier-2026-10/2026-10-23-t228-closure-30-agents/complete/a03/registry422.jsonl` (list TOP200_DL, version 2026-10-14, rank 335, ledger status unverified) asks:

> Bai, Mei, Wang and Xiong prove that logistic regression fitted by maximum likelihood in the proportional regime (n, d → ∞, n/d fixed) is overconfident ... Prove a comparable theorem for a two-layer network trained by gradient descent on cross-entropy in a solvable regime (random features, or mean-field with a single-index teacher): characterize the calibration error as a function of n/d, width and training time, and show whether early stopping yields calibration.

The source is arXiv:2102.07856. The row's open status was never checked (`where_it_stands_checked: false`).

## The claimed theorem, mapped to the question

The model has Gaussian inputs, d, n, m → ∞ with n/d → alpha and m/d → gamma, and tanh random features W ~ N(0, I/d). Only the output weights are trained, by full-batch GD on mean cross-entropy from b = 0, with a fixed step c, reusing the same sample. The teacher is logistic single-index with strength beta. Calibration is the exact unbinned conditional error CE_t = E|E[Y | S_t] - sigma(S_t)|.

| what the row asks | where | first reading |
|---|---|---|
| a two-layer network, GD on cross-entropy, solvable regime | Sec. 1 | Met with random features: the first layer is frozen and only the output layer is trained. That is the row's first option, and the task file forbids generalizing to both layers. |
| CE as a function of n/d, width and time | Thm A and Sec. 3 recursion (7)-(10) | Met at every fixed time T, for all alpha, gamma in (0, inf), including m > n. The answer is a deterministic recursion, not a closed form. The time is fixed before d → inf. |
| whether early stopping yields calibration | Thm B (13)-(14) | Answered "no" by a uniform floor eps_* > 0 over all t >= 1, including the MLE and any training-measurable stopping time. **Only under (12): alpha/gamma > C_* (more samples than trained weights) and a small fixed step c < gamma/(2 Lambda).** |
| overconfidence, comparable to Bai et al. | Thm C | Strict average overconfidence at the risk-optimal **first-step** scale c_*. The weak-teacher corollary gives a regime where Thm B and Thm C hold for the same step. |

## First referee remarks (before the proof modules)

1. **"Overparameterized" and the early-stopping answer do not overlap.** The row's title is about overparameterized classifiers. Thm B's uniform-time "no" needs alpha/gamma > C_*, which means n much larger than m: fewer trained weights than samples, so underparameterized in the trained layer. In the m > n regime, Thm A gives fixed-time curves only. Whether early stopping calibrates there is not answered. This should be stated in any summary of the result.
2. **Thm C's overconfidence is at one step.** Bai et al. prove overconfidence of the MLE. Thm C proves it after one GD step at the risk-optimal scale. Thm B gives a positive calibration error at the MLE but no sign. Whether the trained network at late times or at the MLE is over- rather than under-confident is not claimed. I need to check whether any part of the package claims it.
3. **The constant C_* in (12) is explicit but very large**, about (32L/(k_0 p_1))^2 with p_0 = s_0^2/(20 L^4). The regime is nonempty, but no numerical calibration law follows from it. Next I will compute C_* at beta = 1, gamma = 1 to record its size.
4. **Time zero is calibrated by symmetry.** The package says so explicitly, so "early stopping never calibrates" means stopping at any positive time.

## Next

1. Compute C_*, Lambda and eps_* at a sample point (beta = 1, gamma = 1) by quadrature.
2. Check the first-update normalization (11), A_1 = c a^2 mu_beta and Q_1 - A_1^2 = c^2 tau^2, against an independent small simulation or a hand derivation.
3. Read Thm C, then the final reviews b01 and b02 and ACCEPTANCE.json, and see what they checked independently.
4. Read T357_PRIMARY_SOURCE_COMPARISON.md against Bai et al. and against prior random-feature calibration work.

## Part 2 (3 Nov 2026 19:5x): independent numerical checks

Script `t357_check.py`, output `t357_check.json`.

## The first-update normalization (11) holds

I simulated one GD step (1) directly at beta = 1, alpha = n/d = 2, gamma = m/d = 1, c = 1, measuring A and Q on 40,000 fresh test points. Four repetitions at each d. The package's code was not used.

| | theory (11) | d = 400 (n 800, m 400) | d = 800 (n 1600, m 800) |
|---|---|---|---|
| A_1 = c a^2 mu_beta | 0.07580 | 0.0781 (sd 0.0102) | 0.0750 (sd 0.0052) |
| Q_1 - A_1^2 = c^2 tau^2 | 0.04243 | 0.0407 (sd 0.0040) | 0.0417 (sd 0.0031) |

Both values agree within one standard error at d = 800. The two variance terms in tau^2 are 0.0222 (feature) and 0.0202 (sample). Each is about half the total, so dropping either one would show up in the simulation. Constants: a = E[U tanh U], v = E[tanh^2 U] and nu = v - a^2 = 0.02742, all by quadrature.

## How large the Thm B constants are

These come from the synthesis's own formulas in Sec. 4:

| (beta, gamma) | C_* (need n/m > C_*) | step bound c < gamma/(2 Lambda) |
|---|---|---|
| (1, 1) | 1.6 x 10^32 | 2.4 x 10^-4 |
| (0.5, 1) | 2.1 x 10^29 | 2.4 x 10^-4 |
| (1, 0.25) | 1.2 x 10^31 | 9.8 x 10^-5 |

So the uniform-in-time "early stopping never calibrates" statement is proved only when there are more than about 10^29-10^32 samples per trained output weight, and the step is about 10^-4. That is a valid existence statement, because every constant is finite and the regime is nonempty. Its content is qualitative: in a strongly underparameterized, strongly convex regime, the calibration error stays above a positive floor along the whole GD path.

For the title question about overparameterized classifiers, at m >= n, Thm B says nothing. Thm A gives exact fixed-time curves there, so whether a well-chosen stopping time calibrates in the overparameterized case can be computed for any given T from recursion (7)-(10), but it is not decided by a theorem.

The synthesis calls these "explicit sufficient constants, without claiming they are sharp". That is fair. A one-line summary of T357 should still not say "early stopping does not yield calibration" without the regime attached.


## Part 3 (3 Nov 2026 20:1x): Theorem C, the common regime, the reviews, the sources

### Theorem C's sign checks out, and the effect is very small

Script `t357_check3.py`, output `t357_check3.json`. This is the scalar first-step problem at beta = 1, alpha = 2, gamma = 1, outside the corollary's regime. The scalar theorem itself holds for every k, tau. U = kZ + tau G with k = 0.0758 and tau^2 = 0.0424; g(u) = P(Y = 1 | U = u) is computed by adaptive quadrature.

| c | OC (signed) | CE |
|---|---|---|
| c_*/2 | -0.0283 | 0.0283 |
| c_* = 1.32739 | +4.0 x 10^-5 | 7.6 x 10^-5 |
| 2 c_* | +0.0531 | 0.0531 |

- c_* lies inside the theorem's bracket, (4g'(0), beta k/(k^2+tau^2)) = (1.3245, 1.5733).
- The error sigma(c_* u) - g(u) changes sign once, at u* = 1.69 sd, from positive to negative, as the proof requires.
- So the sign is right. But at this natural point the risk-optimal first step is calibrated to about 10^-4: average overconfidence is 4 x 10^-5. That is far from the order-one overconfidence Bai et al. find for the MLE.
- My first try put OC at c_* at -0.0017 using a 2-D Gauss-Hermite grid. That number was a quadrature artifact: the accuracy term has a jump at S = 0, and |OC| <= CE was violated. It is kept in `t357_check2.json` only as a record.

### How weak the "weak teacher" of the common-regime corollary is

Script `t357_check2.py`, section 1, at gamma = 1, with alpha = 2 C_0.
- beta < log(3)/B_0 alone gives beta < 0.163.
- The step condition a^2 alpha gamma beta^2 / v^2 < gamma/(64 L^2), with C_0 about 3.7 x 10^27, forces beta < 8 x 10^-17.
- So the one model where Theorems B and C hold together has a teacher of signal strength about 10^-16 and about 10^28 samples per trained weight. B01 and B02 both checked the corollary's algebra, and I agree it is correct. It shows the regime is nonempty, and nothing more quantitative than that.

### What the two final reviews and the acceptance record cover

- **B01** checked normalization, the backward and forward recursions, the fresh-test law, (11), positive definiteness and Sec. 6's composition. It reran the numerics with a new Sobol scramble.
- **B02** independently re-proved the scalar normal-mixture single crossing, the sign of OC at c_*, and the corollary's chain of inequalities.
- Neither review repeats the primary-source audit of the AMP and random-matrix input (Wang-Zhong-Fan Prop. D.1(b2), Thm 2.22). That audit is in the proof modules and a separate audit file, which I did not read.
- ACCEPTANCE.json is consistent with this: novelty is not certified, there is no external peer review and no proof-assistant check, and the status is "complete internally reviewed mathematical answer in the explicitly permitted Gaussian random-feature regime".

### Sources

The primary-source comparison is careful. It names Clarte-Loureiro-Krzakala-Zdeborova (AISTATS 2023) as prior random-feature calibration theory. It names Ji-Li-Telgarsky (NeurIPS 2021) as a case where early stopping is consistent under other scalings, so "early stopping never calibrates neural networks" must not be claimed. It also says the registry row's open status was never checked.

## Verdict

**Accept as an internally checked answer to the T357 row in the stated regime. It is not to be summarized as resolving the overparameterized question.**

What holds:
- Thm A: exact fixed-time calibration curves for all aspect ratios, including m > n.
- Thm B: a positive calibration floor along the whole GD path, but only for n/m above about 10^28-10^32 and step about 10^-4.
- Thm C: positive average overconfidence at the risk-optimal first step.
- I confirmed (11) by direct simulation and the sign in Thm C by quadrature, and both reviewers' algebra on the corollary.

What a one-line summary must carry:
1. The early-stopping "no" is proved only in a strongly underparameterized regime. For the overparameterized ratios in the row's title it is open; Thm A only makes it computable time by time.
2. Thm C is a statement about the first step, and its size at natural parameters is about 10^-5.
3. The joint regime of B and C needs a teacher of strength about 10^-16.

Residual risk: the AMP-universality input (Wang-Zhong-Fan) was audited inside the package. Neither I nor B01/B02 rechecked it. Before external use, the next independent check is a reread of that application (signed-permutation symmetry, entry bounds of matrix powers, the causal embedding).
