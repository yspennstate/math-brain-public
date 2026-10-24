# R14 -> PROB10-03 refocus: immutable Campbell–O'Rourke Q1.8 handoff

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling owner directive: `operations/PROB10_2026-09-20.md` refocuses native R14 onto PROB10-03, the negative-margin spherical perceptron. This file preserves the actual intervening R14 successor before that refocus. It does **not** erase, relabel, solve, close, or silently transfer Campbell–O'Rourke Question 1.8.

Navigation point supplied by the owner: commit `3846db33296cfb6eea59ff7c488929087c7b62a2`, which created `runs/R14/2026-09-19T23-01-05Z_vdh_terminal_handoff_campbell_q18_reassign_f3a9.md` and records R14's prior admission of Campbell–O'Rourke Q1.8 after the VDH handoff.

Canonical claim read before this handoff: `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md` on current `master`.

## Preserved source state

Source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, EJP 27 (2022), paper 127, arXiv:2010.01261v3, Question 1.8.

Exact source question: determine which properties of the bivariate alpha-stable dependence/spectral measure `theta_d` determine the limiting spectral law `mu_{alpha,theta_d}` from Theorem 1.6. Question 1.9 (tails) is separate.

Status entering this refocus: `SOURCE OPEN in bounded current-status search / PARTIAL / canonical claim lists R14 as current owner`.

Inherited metric:

`S = number of exact nontrivial full-source transformation laws for theta_d -> mu_{alpha,theta_d}`.

Preserved value: `S=5`.

The five exact laws recorded in the canonical claim are:

1. transpose / coordinate-swap invariance;
2. common-phase covariance;
3. complex-conjugation covariance;
4. opposite-coordinate-phase invariance, with the relative-phase gauge and `q(z,w)=(|z|^2,zw)` quotient as consequences;
5. positive mass/scaling covariance `mu_{alpha,s^alpha theta}=D_s#mu_{alpha,theta}`.

Uncounted partial progress preserved from HARD7-02 / the canonical claim:

- full axis-support classification;
- fixed-eta joint-channel coherence;
- exact alpha=1 two-message Laplace RDE;
- strict `eta -> 0` normalized transverse-coherence gap for every interior member of the swap-symmetric family;
- exact alpha=1 zero-regularization marginal law `q_x(0) ~ Gamma(shape=1/2, rate=m_x/2)`, `m_x=(sqrt(x)+sqrt(1-x))/2`;
- for `x=1/4`, any curvature bridge based only on normalized coherence must beat `1-cos(pi/12)=1-(sqrt(6)+sqrt(2))/4=0.0340741737...`.

The preserved remaining obstruction is to convert the normalized joint-channel defect into a source-visible difference of the unregularized logarithmic potential, or prove exact cancellation. HARD7-02's final predecessor handoff is `runs/hard7_2026-09-18/HARD7-02/2026-09-19T14-12-00Z__terminal-handoff-q19-admission.md`.

## Refocus disposition

This PROB10 run performs **no new Campbell mathematics**. Campbell metric before/after this handoff remains `S=5 -> S=5`. The current owner instruction moves the native R14 research effort to PROB10-03. I do not overwrite the shared canonical Campbell claim in this handoff artifact; any subsequent ownership reassignment should be performed by the coordinator/authorized owner with current-claim reconciliation.

No scheduler change, email, Drive action, public posting, workflow execution, permission change, or force push is made.
