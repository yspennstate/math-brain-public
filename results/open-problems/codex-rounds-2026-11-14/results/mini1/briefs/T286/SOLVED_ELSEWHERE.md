# Substantial advances elsewhere; general T286 remains unresolved

The filename follows the requested stopping rule. It does **not** assert that general-activation T286 is solved. Checked 14 November 2026. The papers below predate the prompt's November 2026 status date; no later rigorous solution was found in the bounded search.

## Quadratic case: a rigorous follow-up with restrictions

Yizhou Xu, Antoine Maillard, Lenka Zdeborová, Florent Krzakala, *Fundamental Limits of Matrix Sensing: Exact Asymptotics, Universality, and Applications*, [arXiv:2503.14121v2](https://arxiv.org/abs/2503.14121v2), COLT 2025, PMLR 291:5757–5823. [Full text](https://arxiv.org/html/2503.14121v2), Section 2.5, Theorem 2.10; [proceedings](https://proceedings.mlr.press/v291/xu25a.html).

The paper proves asymptotic mutual-information and MMSE formulas for structured matrix sensing and applies them to extensive-width quadratic networks. The neural-network theorem uses Gaussian inputs and weights, width ratio κ>0 excluding κ=1, positive noise parameters Δ and Δ₀ as specified in its model, and sample ratios where the variational maximizer is unique. Theorem 2.5 excludes at most a countable set of sample ratios. This establishes a substantial restricted quadratic result, not the completely noiseless endpoint or general activations. The exact normalization should be taken from the paper rather than transferred between conventions.

## General activations: a much more developed conjectural theory

Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore, Rudy Skerk, *Statistical physics of deep learning: Optimal learning of a multi-layer perceptron near interpolation*, [arXiv:2510.24616v5](https://arxiv.org/abs/2510.24616v5), Phys. Rev. X 16, 031014 (2026), [publisher](https://journals.aps.org/prx/abstract/10.1103/56sb-pdh6), [full text](https://arxiv.org/html/2510.24616v5).

Equation (4) has precisely n/d²→α and width proportional to d. The theory covers ReLU and tanh, specialization and Bayes-error predictions. Remark 4 explicitly leaves exactness conjectural even for one hidden layer with vanishing second Hermite coefficient; the other case includes additional matrix-integral approximations. Appendix B.6 gives a partial interpolation argument for μ₀=μ₁=μ₂=0 with all-ones readouts. This is not a general proof. Section III.1 and Appendix B.5 supply optimizer experiments, including ADAM plateaus, rather than a theorem deciding gradient-descent optimality.

The arXiv page states that this paper supersedes [arXiv:2505.24849](https://arxiv.org/abs/2505.24849), also opened during the search.

## Other relevant advances, with different scope

Minh-Toan Nguyen, Jean Barbier, *Sharp feature-learning transitions and Bayes-optimal neural scaling laws in extensive-width networks*, [arXiv:2605.10395](https://arxiv.org/abs/2605.10395), [full text](https://arxiv.org/html/2605.10395v1). It develops feature-overlap and error predictions for hierarchical readouts. Section 2's rigor note expressly identifies the cavity argument and posterior-overlap concentration assumptions as non-rigorous. It does not close T286.

Shu Zhou, Jean Barbier, Sebastian Goldt, *Mesoscopic learning dynamics of extensive-width neural networks*, [arXiv:2610.23779](https://arxiv.org/abs/2610.23779), [full text](https://arxiv.org/html/2610.23779v1), submitted 16 October 2026. It develops dynamics under Gaussian closure and specialization-time predictions. Section II.1 uses fresh-sample online SGD with spherical normalization. Section IV expressly cautions about sample reuse. Thus it cannot decide optimality of gradient descent on a fixed dataset of αd² samples.

## Original caveat checked

Antoine Maillard, Emanuele Troiani, Simon Martin, Florent Krzakala, Lenka Zdeborová, *Bayes-optimal learning of an extensive-width neural network from quadratically many samples*, [arXiv:2408.03733](https://arxiv.org/abs/2408.03733), [full text](https://arxiv.org/html/2408.03733v1). Section 4 states the learning reduction using Conjectures 4.1 and 4.2 and proves the matrix-denoising component as Theorem 4.3. A rigorous denoising component alone did not prove the original full learning claim. The later matrix-sensing paper is the relevant update.
