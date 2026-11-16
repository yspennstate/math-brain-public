---
name: t363_neurons_gain_activations_single_neuron_fate_ode_gives_1_8_basin_2026_11_01
description: [VERIFIED] T363 1/8 basin: neurons with v<0 GAIN activations; a single-neuron fate ODE gives pC'=0.089 and predicts P(1/8) within 1 SE at m 2-8, Theta(0.354^m)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T15:49:08+04:00
  status: verified
  evidence: "t363/fate_run1.txt, fate_run2.txt; moves m363a 2f878814"
---

Row T363 is the two-point example of Vardi-Shamir-Srebro 2110.02732, x1 = (1, 1/4), x2 = (-1, 1/4). It asks how often small-init
gradient flow lands on the non-optimal KKT point with margin 1/8.

The earlier dossier assumed that, since x1 . x2 < 0, a neuron can only LOSE activations. That is false. On an x1-only neuron,
d(w . x2) = v (x1 . x2) dt > 0 while v < 0, so a neuron that starts with a negative output weight turns onto both points. Then
it can grow along the bad direction.

The fix that worked is to compute each neuron's fate rather than classify it from its initial active pattern. In the
small-init phase e_i ~ 1, the neurons decouple, and each follows dv = sum_i relu(w . x_i), dw = v sum_(i active) x_i. That flow
is homogeneous and piecewise linear, so the fate depends only on the initial direction. With 400,000 directions the fates are
pA' = pB' = 0.323 and pC' = 0.0893, against 0.327 and 0.066 from the initial pattern.

Then P(1/8) = (1 - pA' - pB')^m - (1 - pA' - pB' - pC')^m. Measured against predicted at m 2, 3, 4, 6: 0.0542 / 0.0552,
0.0258 / 0.0258, 0.0119 / 0.0108, 0.0016 / 0.0016. That is within one standard error everywhere (pre-registered), and
P(1/8) = Theta(0.354^m).

**Why:** a sign argument on the growing neurons ("a neuron can only lose activations") was applied to all neurons, and it hid
a 30-45 pct channel that the dossier called "late rotation" and left underived.
**How to apply:** in small-init two-layer ReLU basin questions, integrate the decoupled single-neuron flow from each
initial direction to its fate, rather than reading the fate off the initial active set; check monotonicity claims against
the sign of v.
Locators: brain-repo 06_math_research/frontier/rows/T363/DOSSIER.md section "1 Nov (an agent)",
moves m363a (2f878814), fate.py. Related: [[t262_angle_chain_is_a_perpetuity_u_over_d_flip_var_44_over_15pi_2026_11_01]]
(the same session's other row).


ADDENDUM 1 Nov (same session, moves m363b 9b2e167d): the extra C mass is a Filippov sliding mode, not a crossing. Neurons arriving
at w . x2 = 0 with v < 0 are pushed back by both pieces, slide, and at v = 0 both pieces repel; GD releases them into C. The fates are
solid angles of five cones, four elementary and one with an elliptic constant J = 0.61622; pA' = 0.322548, pC' = 0.090122, matching a
2e7 Monte Carlo to |z| <= 1.31. Lesson for piecewise-linear ReLU flows: at an activation boundary check the normal component on BOTH
sides; when both point in, the neuron slides, and when both point out, the discretisation picks the fate.
