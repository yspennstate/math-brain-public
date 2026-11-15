# Bounded literature check, 15 November 2026

No verified solution of the main GD-trained ReLU question was identified
in this check. This is a bounded search result, not an exhaustive claim.

Opened primary sources:

- Ichiro Hashimoto, *Directional Convergence, Benign Overfitting of
  Gradient Descent in leaky ReLU two-layer Neural Networks*,
  [arXiv:2505.16204](https://arxiv.org/abs/2505.16204), abstract and
  [v3 HTML](https://arxiv.org/html/2505.16204v3). Still v3, revised
  10 February 2026. It studies fixed-width leaky ReLU networks and
  directional convergence. No new version extending the earlier
  reports' conclusion was found.
- Kedar Karhadkar, Erin George, Michael Murray, Guido Montúfar, Deanna
  Needell, *Benign overfitting in leaky ReLU networks with moderate input
  dimension*, [arXiv:2403.06903](https://arxiv.org/abs/2403.06903),
  abstract. The stated regime requires d=Omega(n) and uses leaky ReLU
  with hinge loss. It does not supply n/d tending to infinity.
- Junhyung Park, Patrick Bloebaum, Shiva Prasad Kasiviswanathan,
  *Benign Overfitting for Regression with Trained Two-Layer ReLU
  Networks*, [arXiv:2410.06191](https://arxiv.org/abs/2410.06191),
  abstract; and *A Classical View on Benign Overfitting: The Role of
  Sample Size*, [arXiv:2505.11621](https://arxiv.org/abs/2505.11621),
  abstract. The latter says it subsumes the former. Its subject is
  approximate fitting in regression under gradient flow. The earlier
  report's detailed local proof objection was not re-audited here;
  neither abstract verifies the exact noisy-label classification
  interpolation question in T265.
- Yunwen Lei, Yufeng Xie, *Towards Initialization-dependent and
  Non-vacuous Generalization Bounds for Overparameterized Shallow
  Neural Networks*, [arXiv:2604.00505](https://arxiv.org/abs/2604.00505),
  abstract. It gives bounds involving path norm of the distance from
  initialization and empirical comparisons. The opened abstract does
  not give the requested GD interpolation/generalization theorem.

The exact norm formula in PROOF.md is proved directly. No claim that
this general formula is new in the convex neural-network literature
is being made. The contribution here is its explicit application and
strict interpolation-objective comparison for the round 3 construction.
