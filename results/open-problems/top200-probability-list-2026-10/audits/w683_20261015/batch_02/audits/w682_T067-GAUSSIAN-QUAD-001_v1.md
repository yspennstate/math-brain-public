# T067-GAUSSIAN-QUAD-001 v1: PASS

Exact proof SHA256 `b758797c78377588ab24fc48f7d86709a31470b1533fe1473a8898eb8ce5c776`. Checked the complete method proof from its raw statement.

For each positive-mass product bin, expand about its exact conditional mean. The linear remainder integrates to zero independently in each coordinate. The global Euclidean Hessian norm bound gives absolute quadratic remainder at most K/2 times the squared Euclidean displacement. Its integrated sum is K/2 times sum_(i,j)(v_i w_j+w_i v_j)=K P D. This uses unnormalized v_i exactly as defined, with no missing factor of bin mass or factor two. Null boundary sets can be discarded; actual applications have strictly positive Gaussian mass in every bin.

The outside-square probability is 1-P^2 by independence. Since 0<=f<=B its contribution is in [0,B(1-P^2)], yielding both printed one-sided full-integral bounds. Finitely many bins and bounded f ensure all sums and integrals are finite. C^2 and the stated global Hessian bound justify the integral Taylor remainder on every convex product interval.

Integration by parts gives the zeroth, first and second bin moments w, phi(a)-phi(b), and w+a phi(a)-b phi(b). Subtracting the square of the first moment divided by w gives exactly the displayed unnormalized centered variance. Validated enclosures must cover weights and conditional means, as explicitly required; the statement does not treat rounded midpoints as exact conditional means.

For the q=3 signal function displayed in PIECEWISE-D0 Part B, the orthogonal logit noise matrix has squared norm 9s/2. The previously checked softmax Hessian bound 1/5 even gives 9s/10, hence the older certificate's advertised 9s/4 is a valid larger bound. A direct generic softmax Hessian bound 1/2 also yields 9s/4. Constants shifts by -1/3 are applied after the full integral, preserving its tail contribution. The lemma itself makes no reconstruction or literature-priority claim.

**Verdict: PASS** for the quadrature method. This is an elementary Taylor and Gaussian integration-by-parts argument; individual endpoint certificates require separate independent numerical verification and are not passed by this verdict.
