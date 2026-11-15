---
name: i0008_sheffield_minimal_gradient_phase_open_d1_case_2026_11_14
description: "[PROVISIONAL] I0008 (Sheffield Random Surfaces Conj 10.3.1/10.3.2: ergodic gradient Gibbs measure, interior slope => finite SFE and minimal) still open 14 Nov; d=1 nearest-neighbour case holds by de Finetti, with a condensation caveat"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:13:06+02:00
  status: provisional
  evidence: ""
---

I0008 = Sheffield, Random Surfaces (Asterisque 304, 2005; arXiv math/0304049) Conjectures 10.3.1 and 10.3.2, as quoted in Adhikari-Gheissari-Peled arXiv 2609.01499 Sec 2.4: (10.3.2) mu ergodic gradient Gibbs, slope in int S => SFE(mu) < infinity; (10.3.1) ergodic, SFE < infinity, slope in int S => mu minimal (SFE = surface tension). Known: Lipschitz height functions, isotropic interactions; Sheffield: uniqueness of the minimal phase at slopes with an irrational coordinate. Extended web search 14 Nov: no general resolution found (search outcome, not proof).

Small observation (an agent, 14 Nov, unrefereed): on Z with a nearest-neighbour simply attached potential V, the gradient specification is the canonical (fixed-sum) specification of the i.i.d. reference e^{-V}. Its Gibbs measures are mixtures of the tilted product measures P_lambda (Georgii, canonical Gibbs measures; de Finetti with sums), so an ergodic one is a single P_lambda: finite SFE when E_lambda V < infinity, and minimal by the 1D variational principle. Caveat: if V grows only linearly (e.g. |x| + 3 log(1+|x|)), Z(lambda) is finite only for |lambda| <= 1, the tilts reach slopes |s| <= m < infinity, while sigma(s) is finite for every s; for |s| > m there is no gradient Gibbs measure of slope s at all (condensation, as in zero-range). So both conjectures hold in d=1 nearest-neighbour, vacuously beyond m; the content is in d >= 2 or finite-range non-Lipschitz interactions. Check of Sheffield's exact hypotheses on V (growth, simply attached) not done - verify before quoting.
