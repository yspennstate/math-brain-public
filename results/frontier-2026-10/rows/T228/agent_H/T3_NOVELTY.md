# T228 target 3: novelty rerun for the d-dimensional statement

agent H, 22 Oct 2026 05:1x. Web searches (three wordings), results read on 22 Oct.

Statement searched: exact norm tail P_pi(|x| > t) ~ c0 t^(-alpha), c0 in (0, oo), for the stationary law of constant-step
SGD on a nonlinear single-index model in R^d, d >= 2, with Gaussian data.

Found, none of which states it:
- Gurbuzbalaban, Simsekli, Zhu, arXiv 2006.04740 (ICML 2021): linear regression only (quadratic loss, Gaussian data);
  the tail is stated with a direction-dependent function e_alpha on S^(d-1), via Kesten/Goldie and Mirek.
- Hodgkinson, Mahoney, arXiv 2006.06293: implicit renewal for recurrences with "almost linear" gradients, a general
  framework; no d-dimensional nonlinear theorem with a positive constant.
- Gurbuzbalaban et al., arXiv 2302.05516 (cyclic/random stepsizes): linear, about stepsize schedules.
- Ziyin, Li, Ueda, arXiv 2308.06671 (PRE 2025): stationary law of stochastic gradient flow for diagonal linear networks;
  no tail theorem of this kind.
- Alsmeyer (2016, iterated random Lipschitz functions) and Buraczewski-Damek-Mirek are cited in 2006.04740 as the
  Lipschitz and multivariate tools; neither is applied there to a nonlinear SGD chain in R^d.
- Earlier row work: ABB arXiv 2102.02299 is on the real line (agent_AF/src/ABB.txt).

Nothing found combines the three: nonlinear link, d >= 2, and a strictly positive constant for the norm. The closest
open point is what GSZ's own d-dimensional theorem rests on (Mirek's similarity condition, see T3_CLAIM.md); that
belongs to the review, not to this note. Verdict: no prior statement found; the search was web-only, not a full
arXiv full-text sweep.
