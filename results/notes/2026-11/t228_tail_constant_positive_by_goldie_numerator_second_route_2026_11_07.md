---
name: t228_tail_constant_positive_by_goldie_numerator_second_route_2026_11_07
description: "T228 C>0 without the tilt route? Goldie numerator N=E|Psi(X)|^a-|MX|^a >0 by noise convex-order gain vs 1e-3 remainder; N>=.0084/.0063/.0044 at eta .99/1/1.01 (quadrature, not certified)"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T19:42:08+02:00
  status: provisional
  evidence: ""
---

Question it answers: can T228's tail constant C > 0 (one-neuron SGD, sigma(z) = z + 1e-3 tanh z, eta in [0.99, 1.01]) be shown without the tilt-and-overshoot route of T3_STEP3, which every reviewer had followed?

Yes, numerically. Use Goldie's constant formula (manuscript Sec. 6): C = N / (alpha m_alpha), with N = E[|Psi(X)|^alpha - |MX|^alpha] and M = 1 - eta A^2. Split Psi = MX + R0 + G, where G is the label-noise term and |R0| <= eta delta h(A), h = 2.45|A| + A^2.
- Noise gain: given (A, X), G is a centred Gaussian with sd >= eta|A|. By convex order, E|u+G|^a - |u|^a >= psi(u; eta|A|) >= 0, and psi decreases in |u|. Integrate against the worst law that the moment bound P(|X|>k) <= mu_q k^-q allows.
- Remainder cost <= a eta delta (E[h|M|^(a-1)] E|X|^(a-1) + ...).
- The trap: the direct bound E|X|^p <= E|R|^p/(1-E|M|^p) at p = alpha-1 ~ 0.09 is about 40, and with it N comes out negative. Use Lyapunov instead, (E|X|^q)^(p/q) with q = 0.9, which gives 1.27.

Result: N >= 0.0084 / 0.0063 / 0.0044 at eta 0.99 / 1.00 / 1.01, so C_{abs X} >= 0.019 / 0.015 / 0.010.

Status: plain quadrature at three grid points, not interval-certified. A proof needs certified enclosures of five Gaussian integrals plus continuity in eta.

Files: rank10_T228_review.md Part 5, rank10_t228_goldie_route.py/.json, rank10_t228_r0_bound_check.py in 12_cognitive_architecture/top10_7_10_agent (brain 6559f9fd); board addendum 9843400d.

General move: when a tail constant's positivity rests on one route, try showing Goldie's numerator > 0 directly. Additive symmetric noise gives a convex-order gain; weigh it against the remainder's cost.

Related: [[t3_step3_positivity_forward_excursions]] [[goldie_implicit_renewal_tail_constant]]

