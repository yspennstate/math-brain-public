# C0017 statement packet for w412

2026-10-10, w411. Statement only; proof route kept in a separate file.

Intake record: probability_1000_intake_claude_20260907/problems.jsonl, line 17, source garban_steif_noise_2012, Chapter II section 4, p.26. Its target is critical independent bond percolation on the square lattice, p=1/2, with conformal invariance in the scaling limit, Cardy's formula, and convergence of exploration interfaces to SLE(6). The September status search is historical evidence, not a current certificate. Current openness: UNKNOWN pending a bounded primary-literature and owner-work check.

Precise working formulation. Let D be a bounded simply connected Jordan domain, with distinct boundary points a,b,c,d in counterclockwise order for the upper-half-plane normalization below. Use square-lattice mesh delta tending to zero and canonical lattice approximations of D, with marked boundary arcs converging to the indicated arcs and no extra boundary identifications. Edges inside the approximation are mutually independent Bernoulli(1/2). The primary notes label their points clockwise; reversing labels to (b,a,d,c) preserves the two unoriented crossing arcs and gives this equivalent counterclockwise convention.

(1) The probability of an open primal path joining arc ab to arc cd converges to Cardy's conformally invariant value. Under a conformal map taking (D;a,b,c,d) to (the upper half plane;0,eta,1,infinity), with eta in (0,1), that value is

    C(eta) = [integral from 0 to eta of t^(-2/3)(1-t)^(-2/3) dt]
             / [integral from 0 to 1 of t^(-2/3)(1-t)^(-2/3) dt].

(2) For two marked boundary points a,b, impose Dobrushin boundary conditions: the primal boundary arc on one side is wired/open, and the complementary dual arc is wired/open in the dual (equivalently closed on the primal). The medial exploration from a_delta to b_delta converges in law, as an unparameterized curve with the uniform metric modulo increasing reparameterization, to chordal SLE(6) from a to b in D. Interior edge independence is retained.

These are two proof obligations. A claim about one crossing probability or a finite gadget does not establish either whole obligation. The Jordan-domain formulation makes boundary prime ends and arc approximations unambiguous; extension beyond it requires its own argument. No mathematical success claim has been made.
