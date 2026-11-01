# C0052 paired main-step audit

Scope: w477 ATTEMPT.md L002-L003 and L007 (read after w478's independent L1/L2 checkpoint and L4 comparison). Verdict: KEEP as conditional reductions; the uniform current-overlap premise is unproved. This is an author/adversary audit, not a different-model review receipt.

L007 uses pi_beta(x)=G_beta(0,x)/chi(beta), valid in the stated positive-beta, subcritical, free, zero-field state. Substitution z=y+r in the four-point switching identity gives -g=(2/xi^3) sum_y p_y. The relative endpoint laws are independent and translation invariant. All summands are nonnegative, so Tonelli justifies the rearrangement; no conditional per-site probabilities are multiplied. Repeated endpoints cancel their source parity, and a root belongs to its own cluster.

For H={0,...,ceil(xi)-1}^3, its cardinal N satisfies N>=xi^3. A uniform Y on H makes the restricted sum N times the averaged connection probability. For the SINGLE-current cluster witness I, {I>0} implies the original union-current connection. Cauchy-Schwarz then gives -g>=2 N(E I)^2/(xi^3 E I^2)>=2/Q. The Y=0 case guarantees E I>=1/N>0 when W contains the root. Finite W bounds I and its second moment. These facts justify the divisions and the factors of two and xi^3.

Minimal missing premise for this route: Q(beta)=E I_beta^2/(E I_beta)^2 remains bounded along a sequence beta_n increasing to beta_c, under exactly the source-weighted single-current laws and the stated independent shift. A bound only for critical currents, arbitrary fractal sets, or clusters enlarged by sourceless currents does not provide that premise. A uniform bound throughout the approach is sufficient but stronger than the source's nonvanishing requirement.

L002's averaged endpoint identity and L003's Cauchy-Schwarz implication pass for the same reason. The claims do not assume independence of two occupancy events inside one current. The first-moment counterexample is appropriately labelled an obstruction to an inference, not an Ising counterexample. No parent problem has been proved.

Independent comparison L4 in w478 ATTEMPT.md supplies a different route from near-critical block deficits to g, with its own explicit variance-capture premise. Its new deductions require w479's independent check. The hardest unclosed piece in either route is the scale-uniform anti-concentration/current second-moment bound.
