---
name: f0072_continuous_sos_entropic_repulsion_log_n_over_d_prediction_2026_11_14
description: "[PROVISIONAL] F0072 (Velenik 2006 Open Problem 5: entropic repulsion for continuous SOS V=|x|): heuristic predicts height (1/d) log N in d>=3, not sqrt(4 g_d log N); single-site lower tail e^{-2dh}; unproved"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:15:41+02:00
  status: provisional
  evidence: ""
---

F0072 = Velenik, Localization and delocalization of random interfaces (Probab. Surveys 2006), Open Problem 5, Sec 3.2, PDF p.22: entropic repulsion heights for non-uniformly-convex V, in particular continuous SOS V(x)=|x|. Still open 14 Nov (intake search 8 Sep; nothing new).

Heuristic (an agent, 14 Nov, unproved): in d >= 3 the repulsion height balances N^d P(phi_0 <= -H) against the cost of lifting the field, about H^2 N^{d-2} (surface tension quadratic at slope 0). For the GFF P(phi_0 <= -H) = e^{-H^2/2g} gives H = sqrt(4 g_d log N) (the known answer). For |x| the lower tail is exponential: a single-site spike to depth h costs 2d h, and lowering a neighbour too costs (2d-2) per unit more than it saves, so P(phi_0 <= -h) = e^{-(2d+o(1))h}. Balance: e^{-2dH} ~ H^2 N^{-2}, so H_N ~ (1/d) log N. This is the 'behaviour changes with the tail of V' the source anticipates. FKG holds (convex nearest-neighbour V), which a proof would use for monotonicity; Brascamp-Lieb does not (V not strictly convex).
Caution: the 8 Sep attempt F0072-A001 reduced |x| to random-conductance GFFs via the Laplace variance mixture; that route hides the exponential tail and would point to sqrt(log N) - check it against this before reusing.
Next: Monte Carlo of the |x| field with hard wall in d=3 (worker machine 1, GPU heat-bath; the exact one-site conditional is piecewise exponential) to see log N vs sqrt(log N) growth, and the lower-tail rate 2d. Related: [[e0012_colicin_no_coexistence_open_lanchier_mercer_partial_2026_11_14]].

Numerics 14 Nov 11:0x (worker machine 1 ~/f0072_20af, sos3.c/tail3.c exact piecewise-exponential heat bath, d=3, zero boundary):
- lower tail, no wall, N=16 centre site, Rao-Blackwell over the exact conditional: log P(phi_0 < -h) = -0.693, -2.48, -5.15,
  -8.10, -11.09, -14.09, -17.09, -20.09, -23.09 at h = 0..4 step 0.5: slope exactly -6 = -2d from h=1.5; P ~ 2.49 e^{-6h}.
- hard wall on the whole box, centre-block mean height: N=8 0.638, N=16 0.873 (+0.235 per doubling; (1/d) log N predicts
  ln2/3 = 0.231); N=24 1.014, N=32 1.119. Local slope dH/dlnN = 0.339, 0.350, 0.363: near 1/3 and NOT falling, as a
  sqrt(c log N) law would require (its slope is c/2H). N=48 gives 1.267, N=64 gives 1.370 (fit predicted 1.363; local slope 0.359). Note and code: 12_cognitive_architecture/math/trio_1011/op/F0072 (63f70fdb).
