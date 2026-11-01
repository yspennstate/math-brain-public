# What would justify a random return phase

Status: deterministic probability lemma PROVED below; application to the trained-network moving return is CONDITIONAL and presently unpaid. This is classical oscillatory averaging, not a novelty claim.

Let T be a real random variable with an absolutely continuous law, Y any jointly defined random element in a Polish space, and lambda_n->infinity deterministic. For any measurable finite offsets b_1(Y),...,b_k(Y), the vector

    (Y,T, {lambda_n T+b_1(Y)},...,{lambda_n T+b_k(Y)})

converges weakly, with phases interpreted on the circle, to

    (Y,T, {U+b_1(Y)},...,{U+b_k(Y)}),

where U is uniform on [0,1) and independent of (Y,T). The phase is ONE shared U, not k independent uniforms. Braces denote fractional part; conclusions for threshold indicators require the limiting threshold boundary to have zero probability, which holds for a fixed finite set of proper phase thresholds conditional on Y,T,U's independence.

Proof. For bounded measurable g(Y,T) and integer vector ell, the Fourier character of the phase vector contributes

    E[g exp(2pi i sum_j ell_j b_j(Y)) exp(2pi i lambda_n T sum_j ell_j)].

If sum ell_j=0, this is already its proposed limiting value. Otherwise the complex measure obtained by weighting the law of T by the bounded first factor has an L1 density: its total variation is bounded by ||g|| times the absolutely continuous law of T. Its Fourier transform tends to zero by the Riemann-Lebesgue lemma. These are precisely the Fourier moments of a shared independent uniform phase. Trigonometric approximation on the compact phase torus, together with tightness of the unchanged (Y,T) coordinates, proves the assertion. Measurable offsets cause no problem because they enter the bounded weight in this argument. The same proof gives stable convergence relative to every fixed bounded observable on the original probability space.

This can be applied to an approximation T_n only under additional control. A sufficient condition is

    lambda_n(T_n-T)->0 in probability,
    b_{j,n}-b_j(Y)->0 in probability.

The circle distances between the actual and ideal phases then vanish, so the same limit holds. Another sufficient route is convergence in total variation of the relevant weighted return-time densities, strong enough to control their Fourier transforms at frequency lambda_n. Ordinary weak convergence or uniform macroscopic path convergence alone supplies neither condition.

Exact counterexample to the weaker inference: T uniform on [1,2], lambda_n=n, and T_n=floor(nT)/n. Then |T_n-T|<=1/n->0, but {nT_n}=0 identically. The ideal phase {nT} is uniform. Thus even an O(1/lambda_n) return-time error can completely change the selected phase. This example is not a trained-network construction.

For T384, lambda_m=L_m/gamma and the relevant return time and Euler-sum correction are coupled to the original marked population and residual. A stopped macroscopic theorem proves convergence before a clock zero, not the sub-grid error above. Any valid Euler-Maclaurin expansion must retain its O(1) unscaled correction, and any finite-width conditional-density argument must be proved jointly with retained marks. Treating different atoms as independent phase thinnings is also unjustified: even under the ideal averaging lemma, atoms at a common return inherit the same U with different offsets. Atoms with more general phase frequencies require their actual frequency relations to be analyzed separately.

This gives two concrete proof routes, neither completed here: prove a sufficiently sharp coupled return-clock expansion, or prove high-frequency weighted-density control directly. If neither is available, retain an augmented phase variable in subsequential laws rather than asserting a selected network law.
