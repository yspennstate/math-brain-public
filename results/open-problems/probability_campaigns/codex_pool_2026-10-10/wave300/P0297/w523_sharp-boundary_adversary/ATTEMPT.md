# P0297 adversary result

2026-10-10. The original problem is not solved. Current openness is UNKNOWN beyond the dated primary sources and targeted archive checks. No novelty claim is made. On resume, the actual w524 verdict file supplied a scoped KEEP for the counterexample below and the independent L1-L2 derivation; INDEPENDENT_REVIEW_RECEIPT.json records those verdicts.

The exact target is: for each fixed gamma in (0,2), determine the deterministic almost-sure Hausdorff dimension d_gamma of the whole plane with its gamma-LQG metric D_h, associated with a whole-plane GFF h. The metric's positive deterministic normalization does not change dimension. Gamma=0 and gamma=2 are outside this statement. The known gamma=sqrt(8/3) value is 4. Primary statement: Gwynne-Miller, Problem 7.1, https://link.springer.com/article/10.1007/s00222-020-00991-6 .

INDEPENDENT.md was saved before reading w522's statement or proof. It separately derives the exact quadratic deficit and the critical corner's different limits. These agree with w522's L1 and L2. The paired packet also handles the zero-dimension exception, keeps inverse stability normalized by xi, and explicitly limits its countermodels to numerical equations. I found no mathematical failure in those scoped statements; the five concrete audit verdicts are in AUDIT_VERDICTS.jsonl.

The single hardest piece remains an independent evaluation of the LFPP normalization relation Q_LFPP(xi). Optimizing a formula containing xi=gamma/d_gamma returns d_gamma and supplies no new equation for this unknown. The source's full-dimension corollary must be used to pass from a thick subset to the whole space; an uncountable union argument would not suffice.

## An exact counterexample to dropping the KPZ independence premise

The stronger auxiliary statement under attack is:

    For every random Borel subset X of the plane, even if X depends on h,
    dim_E X = xi*Q*dim_D X - (xi^2/2)*(dim_D X)^2.

Fix any gamma in (0,2), and set xi=gamma/d_gamma and Q=2/gamma+gamma/2. Define the field-dependent set

    X = T_h^gamma
      = {z : lim_{r->0} h_r(z)/log(1/r) = gamma},

where h_r(z) is the circle average. This is a random Borel set: use the jointly continuous circle-average version, express the epsilon-delta limit using all positive rational radii, and take countable intersections and unions of the resulting Borel conditions. Continuity in radius then recovers the limit over all radii. A single sparse sequence of radii would not suffice from continuity alone.

Gwynne-Pfeffer, https://arxiv.org/html/1905.11790, equation (1.11) with the deterministic ambient set U=C, gives, almost surely,

    dim_E X = 2-gamma^2/2.

The same paper's Corollary 1.7 gives, almost surely,

    dim_D X = d_gamma.

For this one fixed gamma, intersecting these two probability-one events is valid. No simultaneous-in-gamma statement is needed. Substitution in the proposed stronger KPZ equality yields

    xi*Q*d_gamma - (xi^2/2)*d_gamma^2
        = gamma*Q - gamma^2/2
        = 2.

Its error is exactly gamma^2/2>0. At gamma=sqrt(8/3), the actual Euclidean dimension is 2/3 and the false prediction is 2, a gap of 4/3. Thus the stronger auxiliary statement is false for every fixed subcritical gamma. This uses the published thick-point theorem and full-dimension corollary, not an application of independent-set KPZ to a dependent set.

The minimal repair for the published exact KPZ theorem is to retain its deterministic-set or h-independent random-set hypothesis. Some special dependent sets may also satisfy the equality; independence is a sufficient hypothesis, not a characterization of all equality cases. For general field-dependent Borel sets the paper supplies inequalities in Theorem 1.8. This counterexample does not refute P0297, does not calculate d_gamma, and does not show that w522 makes this invalid inference: the paired packet explicitly respects the hypothesis.

The numerical check records the proposed prediction versus the source-backed dimension for fixed rational gammas, and the exact Brownian anchor separately. Its role is to measure the rejected bridge; it is not a formal proof. The proof is the preceding substitution and the two precise source statements.

NEXT: The validating coordinator ingests reviewed concept-only bundle_002.json and verifies retrieval; the next mathematical advance needs an independent LFPP crossing-normalization estimate.
