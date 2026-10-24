# C0068: refuted scale comparison, 2026-10-10

Status: elementary proof of an error in the earlier attempt, with an explicit counterexample to its route. Giant concentration and uniqueness are not resolved by this correction. The local ledger supplies no verified torus literature solution.

The earlier attempt and live card say: "d > 6 <=> V^{-2/d} << V^{-1/3}" and consequently the whole regime above the critical window lies above the correlation-length crossover. This is false.

For d>6, 2/d<1/3, and

V^(-2/d)/V^(-1/3)=V^(1/3-2/d) -> infinity.

Thus V^(-1/3) << V^(-2/d). Let beta=(1/3+2/d)/2 and eps=V^(-beta). Then 2/d<beta<1/3. This yields eps/V^(-1/3) -> infinity but eps/V^(-2/d) -> 0. These eps are above the finite-volume critical window and BELOW the suggested correlation-length crossover.

Under the heuristic xi~eps^(-1/2), xi/V^(1/d)=V^(beta/2-1/d) -> infinity along this sequence. The proposed implication that the box side exceeds xi is therefore unavailable in precisely this part of the requested regime. This refutes that justification, not a valid sprinkling theorem supplied by other means.

The cached book at lines 11639-11652 actually sets p=p_c(T_(n,d);lambda)*(1+eps), with a finite-torus critical parameter, and asks to identify c with the right derivative of theta at p_c(Z^d). Do not silently replace this by the infinite-lattice parameter. There is also a normalization issue in the earlier attempted local-density identification: if c denotes the derivative of theta with respect to p at p_c, then theta(p_c(1+eps))/eps -> p_c*c, not c. A derivative with respect to the relative parameter eps would already include p_c. The exponent correction itself is independent of these conventions.

Checks: check_math.py verifies exponent signs and the midpoint construction with exact fractions for d=7,8,10,12,20. The five earlier asserted signs fail; all five corrected signs hold. Lean file KeyStep.lean isolates the order step 2/d<1/3 => 1/3-2/d>0, if the local compiler admits the run. The exponent arithmetic does not depend on any unverified percolation result.

Next mathematical step: seek estimates valid while xi exceeds the torus side, rather than invoking a local Euclidean giant argument for the entire window-above regime. Auditor w346 must KEEP the correction before landing it as a validated edge.
