# QFORM research plan, 2026-09-25

**Framing.** The owner wants the full conjecture. It is open, so I target the leaves the digest shows still open, check what they rest on, and run a bounded counterexample search alongside. Partial results get reported as partial.

**State (digest only; all unrefereed).**
- Closed, provisionally: spread bound (Lemma 1.1); three hubs, any remainder (Thm 6.3); single hub without diagonal on any fixed number of light coordinates; hub diagonal with 1 − aC < 0 (no proof on file); hub that sees P under bounded-partner/window-law hypotheses (Props 5.5–5.6).
- Open: the single hub without diagonal is only O(log #light coordinates) (Prop 3.17); the diagonal regime 1 − aC ≥ 0, where the eps-twist returns; two-hub leaf: status not visible.

**Build on.** Prop 3.17 and its fixed-number predecessor; the cross-term absorption (09-23 20:03); Prop 5.6; Prop 5.1(a); the √2 linear-form bound (Ball/Rogozin) and the LPP plane constant 2. Conditioning on coordinate blocks, not rotated projections, keeps a product law. Multilinearity in the densities restricts to extreme laws, uniform on unit-measure sets (check this matches "window laws").

**Avoid.**
1. Fourier inversion as a uniform tool: withdrawn after a hand-checked counterexample. Only the spread version (Lemma 1.1) survives.
2. Hölder/mixed-frame-norm reductions (Prop 5.3) and 2-D maximal functionals. Numerics show frame integrals growing on spread frames while the density stays bounded. Example 5.2 (unproved) makes the maximal functional unbounded while curved marginals stay bounded. Proofs through them inherit that loss, probably the log.
3. Refining "hub that sees P": corrected numerics show a few per cent gain.
4. Random-submatrix singular-value routes: they need a fourth moment (third moment refuted), bounded density gives none, and angular decorrelation is still open.
5. Quoting BGKS or Meka–Nguyen–Vu unchecked: an MNV quote already failed a citation check.

**Main line (hours 1–3): uniform single hub without diagonal.** It is the leaf with a quantified gap, and the others look like perturbations of it. Integrating out the hub gives density(t) = E[g((t − R)/2L)/(2|L|)]. Split by dyadic scale |L| ≍ 2^{-k}. The trivial bound is O(1) per scale, and I expect the log counts scales. After absorbing the L·P cross term, a conditional small-ball bound with any power gain, uniform in eps, suffices (A = hub window):

    P(R ∈ t − 2L·A | |L| ≍ 2^{-k}) ≤ C·2^{-θk}.

This is far weaker than a bounded (L, R) density.

Mechanism: localize L through a coordinate set B with |w_B| ≥ δ|w|, for an absolute δ. B is one heavy coordinate or a greedy block of light ones, and Ball bounds L_B's density by √2/(δ|w|) regardless of |B|. Take R's gain from outside B. Pigeonhole over two disjoint such sets keeps R's large eigendirection mostly outside one of them; Prop 5.6 is the template. w concentrated on one coordinate should go to the fixed-number result. If instead the log is a harmonic sum over added coordinates, I'll charge each step to w_i²/|w|², which sums to 1.

**Hour 4: diagonal, two hubs.** Carry the proof into 1 − aC ≥ 0, using Prop 5.1(a) for the −L²/a curvature that completing the square in x₁ creates. Then write out two hubs: near-parallel partners should reduce to one hub, and transversal ones to E|(L₁,L₂)|⁻¹ plus the LPP bound (hub–hub terms to check).

**Counterexample check (~45 min, alongside).** Take the family on which Prop 3.17 is tight, with window laws and N = 2⁴…2¹² light coordinates. Use an exact inner hub integral, stratified by |L| scale (the 1/|L| weight is heavy-tailed; earlier numerics needed a bias fix). Validate on a closed-form case first. Saturation shows which cancellation to capture. Growth like log N is a potential counterexample, reported to the owner at once.

**First concrete step.** Read the proofs on file for Prop 3.17 and the fixed-number proposition. Mark where the log enters (dyadic |L| scales, a harmonic sum, or a frame integral) and restate the small-ball target in their normalization. Also check that hub definitions and thresholds in Lemma 1.1, Thm 6.3 and the single-hub results fit one case tree.

**Standard.** One note per result, status-tagged; nothing called proven without a written proof checked line by line.
