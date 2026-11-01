# C0065: The recorded derivative inequality does not imply susceptibility divergence

Label: proof; author checked only. Independent audit: PENDING w347.

The implications theta(delta)~delta and theta'(delta)<=C*chi(delta), even with theta,chi positive and smooth on 0<delta<1, do not imply chi(delta)>=c/delta for any c>0. Therefore the earlier C0065 attempt's claimed inverse-distance lower bound does not follow from the two displayed premises. This refutes that inference, not the percolation lower bound itself.

Assumptions: Only the two derivative-and-order premises quoted in the earlier attempt are being tested

Take theta(delta)=delta, chi(delta)=1 and C=1. Then theta'(delta)=1<=C*chi(delta), and theta(delta)/delta=1 exactly. However delta*chi(delta)=delta->0, so no positive c can satisfy chi(delta)>=c/delta for all sufficiently small delta. Both functions meet the stated smoothness and positivity requirements. Extra percolation inequalities could still prove a susceptibility lower bound, but they are additional premises and are not supplied by this derivative comparison.

Limits: No claim is made that the actual high-dimensional finite-cluster susceptibility has this counterexample behavior. The claimed percolation theorem must be re-proved from valid percolation-specific inputs.

Existing card: math:probability.percolation:open-problem-c0065-existence-and-equality-of-the-supercritical-exponents-gamma-nu-nu-2-in
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:1912
