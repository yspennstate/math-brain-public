# Next-target assessment from a02, a03, and a05

Author: A26. Date: 2026-10-23. This is a new followup assessment. Frozen deliverables, earlier reports, and registry statuses are unchanged.

**Best genuinely unresolved target in the preserved record: T357's actual finite-time GD calibration theorem for Gaussian-input nonlinear random features.** The concrete missing result is a rigorous evolving test-score law, with sufficient control to deduce conditional calibration and a nontrivial early-stopping/risk statement. The ridge-path calculations already in the dossier do not supply that theorem.

For an immediately tractable supplementary result, the parent proposed a categorical ReLU model. I developed it in [categorical_rf_calibration.md](categorical_rf_calibration.md). That note now contains a self-contained theorem for discrete full-batch GD, not merely a proposal. It must be described as a special model with disjoint feature supports, not as resolution of the Gaussian random-feature gap. Neither the new theorem nor this selection has an independent audit or a publication-novelty certification.

## What should and should not count as new work

| Candidate | Work already present or now supplied by external results | Actual remaining issue | Assessment |
|---|---|---|---|
| T336 | Corrected continuous-kernel raw-input approximation in a02; corrected prior-task ERM bridge in a05, reviewed in A19/A20 | Broader priors or stronger uniformity/architecture assumptions require a different theorem; a claimed original-row closure still needs an exact scope reconciliation | Do not repeat the established approximation or ERM argument. Efficient SGD is a separate extension, not an explicit requirement of the original registry sentence. |
| T354 | A written residual-neighborhood theorem with a prior audit; extensive scalar frozen-drift bias calculations | Original fixed-hyperparameter stationarity quantifiers and a provable Adam/SGD transformer advantage are broader; floor-free tracking alone addresses only a technical subproblem | Useful local repair work, but a new tracking lemma cannot be counted as full original-row closure. A29 is separately investigating the weaker step-schedule tracking sketch. |
| T357 | Fixed-ridge Gaussian-equivalent RF calculations, population sign analysis, and large-sample expansions; some linear-model late-GD heuristics | Actual finite-ratio nonlinear RF training dynamics, a justified calibration limit, and useful early stopping | Recommended unresolved mathematical target. |
| T366 | The local rate gap is stale: a June 2026 positive-contraction theorem gives the iid population rate; published historical-loss transfer and a permutation extension strongly reduce the remaining task to synthesis | Exact scope/metric reconciliation, lower-bound matching, and independent review of the synthesis; repeated reshuffling epochs are a separate process | Do not launch the iid last-iterate rate as a new open problem. Do not manufacture a distinct-seen-set metric to preserve an apparent gap. |

For T336, the accepted result uses a continuous PSD kernel on a compact Euclidean domain, positive observation noise, bounded contexts for deterministic uniform approximation, and a tail/generalization argument for average prior-task risk. It does not prove uniform KL over arbitrary unbounded labels or all priors. The C003 discontinuous-kernel obstruction remains relevant. Conversely, exhaustive grid ERM is an actual learning rule: the absence of practical SGD convergence does not erase the existing statistical theorem. The a05 polynomial lower bound is restricted to instance-independent polynomial solvers and is not a universal transformer-depth theorem.

## T366 freshness correction: a theorem-combination task, not the best open target

[Dereziński–Dong, arXiv:2606.29593v1](https://arxiv.org/html/2606.29593v1), Theorem 3.1 and Lemma 3.6, supplies a dimension-free operator/deletion bound for positive contractions. [Evron et al., arXiv:2504.04579v3](https://arxiv.org/html/2504.04579v3), Lemma B.1, transfers pre-update residual control to occurrence-weighted historical forgetting.

**Inference requiring independent review:** let $P_i$ be orthogonal projectors, $W_k=P_{I_k}\cdots P_{I_1}$, and $A_k=\mathbb E[W_k^\top W_k]$. For iid sampling or a uniform sample of length $k$ without replacement, deleting any position has the marginal for a sample of length $k-1$. Lemma 3.6 applied to reversed products therefore yields

\[
\|A_{k-1}-A_k\|\le3/k,
\quad
\mathbb E\|(I-P_{I_k})W_{k-1}e_0\|^2\le3\|e_0\|^2/k.
\]

With $\max_i\|X_i\|\le1$, Lemma B.1 then gives unhalved historical residual at most $8\|e_0\|^2/k$. This covers single-pass prefixes, not arbitrary repeated-epoch histories. It is an application of published ingredients, not an independently audited campaign closure. The exact occurrence metric and matching lower bound must be retained.

The newer [Xu–Ma, arXiv:2604.13460v2](https://arxiv.org/html/2604.13460v2), distinguishes historical loss from independent-task risk and gives distribution-dependent exponential behavior. That does not replace a uniform worst-case result. [Schliserman–Koren, arXiv:2610.25469v1](https://arxiv.org/html/2610.25469v1), also reports $O(1/T)$ quadratic rates for all admissible constant stepsizes. The local dossier's older $k^{-1/2}$ or $k^{-3/4}$ frontier should therefore not be taken as current evidence that the iid projection-rate problem is unresolved.

## Precise unresolved T357 target

Keep the dossier's substantive regime: $x\sim N(0,I_d)$, $Y\mid x\sim\operatorname{Bernoulli}(\sigma(\beta\theta_*^\top x))$, $\|\theta_*\|=1$, and $m$ frozen features

\[
h_j(x)=\tanh(f_j^\top x),\qquad f_j\stackrel{\mathrm{iid}}\sim N(0,I_d/d).
\]

Train $s_t(x)=a_t^\top h(x)$ from $a_0=0$ by actual full-batch GD on mean logistic cross-entropy, with an explicitly fixed step rule. Take $n/d\to\alpha>0$ and $m/d\to\psi>0$. The first milestone should cover every fixed finite horizon $J$, before attempting any exchange of $d\to\infty$ with $t\to\infty$.

The missing proof obligations are:

1. Derive a closed deterministic evolution, or a rigorous finite-time state-evolution system, for the joint fresh-test law of $Z=\theta_*^\top x$ and $S_t=s_t(x)$, simultaneously for $0\le t\le J$. The trained coefficients depend on the same random feature matrix and training examples, so a static Gaussian-equivalence theorem for fixed ridge ERM cannot simply be reused.
2. If the limiting pair is Gaussian, prove the relevant joint-law statement and identify its actual moments $q_t=\mathbb E S_t^2$ and $c_t=\mathbb E ZS_t$. The resulting candidate calibration curve is

   \[
   g_t(s)=\mathbb E_G\sigma\!\left(\beta\left[\frac{c_t}{q_t}s+
   \sqrt{1-c_t^2/q_t}\,G\right]\right),\qquad q_t>0.
   \]

   This formula is conditional on a proved Gaussian limit; it is not itself a dynamics theorem.
3. Justify the calibration functional, not only weak convergence of the scores. Conditional expectation and calibration error do not follow automatically from weak joint convergence. Sufficient routes include convergence of conditional regressions in $L^1$, or appropriate density/total-variation control plus tail bounds. Log-loss additionally requires uniform integrability.
4. Analyze a clearly named metric: the full score-conditional calibration curve and an $L^1$ or $L^2$ calibration error, with signed OC reported separately if used. A zero first-moment calibration statistic or a zero signed OC does not imply full calibration.
5. Prove an early-stopping statement subject to a nonzero risk-improvement requirement. At symmetric initialization $q_0=0$, prediction $1/2$ is calibrated, so “there exists a calibrated time” is vacuous. A useful result must quantify the tradeoff after learning, over a nonempty parameter region.

The concrete obstruction is the coupling of training-dependent feature coefficients with the same nonlinear random design over time, followed by the conditional-calibration limit. The next deliverable should be a theorem with verified hypotheses for this coupling, not another finite-ridge numerical sweep or a relabeling of the ridge parameter as time.

General dynamics theory already exists. [Gerbelot et al., arXiv:2210.06591](https://arxiv.org/abs/2210.06591), gives rigorous first-order-method DMFT; [Nishiyama–Imaizumi, arXiv:2602.06320v2](https://arxiv.org/abs/2602.06320v2), treats stochastic gradient flow; [Fan–Wang, arXiv:2601.21093v3](https://arxiv.org/abs/2601.21093v3), treats multi-pass SGD in multi-index models. These are candidate tools needing theorem-level checks for this exact nonlinear RF design and calibration observable. I did not find an exact matching end-to-end calibration theorem in the targeted current search; that is a scoped search result, not proof of global novelty.

## The categorical supplementary result: useful progress with a firm boundary

The new note uses isotropic categorical inputs $\pm\sqrt d e_j$ and frozen ReLU weights $\pm e_j/\sqrt d$. A feature activates only on its matching input cell. Poisson occupancy in the proportional limit then gives an exact scalar GD recurrence and a countable prediction mixture. Total-variation convergence of the empirical count law directly controls conditional calibration, including collisions between prediction atoms.

It proves all of the following within that special model: a time/sample/width-dependent law; positive-time miscalibration with an explicit lower bound; risk improvement after a sufficiently small first GD step for an informative teacher; and eventual divergence of population log-loss, making a risk-optimal stopping time finite and nonzero. That stopping time is miscalibrated. The all-success-cell argument does not require global GD stability.

This is more substantive than the pure-noise observation alone. Nevertheless, the model is exactly a random-coverage histogram because its feature supports are disjoint. It provides one literal random-feature example relevant to T357; it does not show the Gaussian-input tanh-RF claim, typical overconfidence for the informative teacher, or generic network behavior. Its relation to a whole original-row interpretation needs explicit adjudication rather than changing the registry silently.

## Evidence snapshot

The following SHA-256 values pin the substantive local sources read for this assessment. Historical notes inside them can be stale; the corrected current files and their actual review conclusions take precedence.

| Local source | SHA-256 |
|---|---|
| `a03/registry422.jsonl` | `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0` |
| `a03/TRIAGE_REPORT.md` | `65e94961a5ad0dea69cb1ca9546f5af15135ebc4239be98b7a7df757e937cfbb` |
| `a02/CONTINUOUS_KERNEL_EXTENSION.md` | `5cd1bdd401d2efbd15433e9fa5fc1834e792424fa70fba552da85b776ef45566` |
| `a02/C003.md` | `80a484b6a70e58716b1388390148e3cb847f3b8079c2c1dceba5f9601c1f9003` |
| `a05/ERM_BRIDGE.md` | `97eeb783f610ea4ce4ead20c547a0ec65ebc4ca0320d7a07e4d38c05bf936d96` |
| `a05/POLYNOMIAL_LOWER_BOUND.md` | `ff604cb8f6324e8d1c000cc4f8a19987c4445292974b505ba5318ad48f28e39d` |
| `a03/T354_theorem.md` | `fbf6011a14d439eff8208fa14c6a0625cc66aca91eebe09b19fb0b4c4bd59f28` |
| `a03/T354_independent_prior_audit.md` | `f5ccf97da806793c0937d77100d2f92d86ca1aa992749c8a27b86a5105034559` |
| `a03/rows_T357_DOSSIER.md` | `4f150d1a55209ed37d8b1c6bca8e6ed85b9b4b50dbac24e616b5126791fb5ff9` |
| `a03/T357_next.md` | `50a01286f797434db25ef2c1674daa86ae130bd1b4191b1e7de183badb2f973c` |
| `a03/rows_T366_DOSSIER.md` | `500c361765d5e1d1d560a6886c17ea52e723ab85d71619dd03d76ca6a9ca1d71` |
| `campaign/reviews/A19.md` | `3e72c44ecf3cd8cdeab361cd22009b9dc25b2929069eacd2709fd00d5882ba80` |
| `campaign/reviews/A20.md` | `a92cdce0c0e1e8bd18b3710351449e56b2079fd742535c2bca1fcc191f7cd70b` |

All online references above were checked on 2026-10-23. The followup changes no existing acceptance status. The categorical theorem is complete as a local derivation but awaits independent review; the proposed Gaussian-RF dynamics theorem remains unresolved here.
