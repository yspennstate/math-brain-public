# P0297: exact LQG metric dimension, adversarial lane

Worker w517. Paired prover w516. Referee w518; any new result of w518 goes to w521. Current openness: UNKNOWN pending completion of the bounded source/status checks. No claim of an exact LQG dimension or novelty.

For gamma in (0,2), take a whole-plane GFF with unit-circle average zero and its canonical gamma-LQG metric D_h. The target is to determine the deterministic value d_gamma=dim_H(C,D_h) explicitly as a function of gamma. The sqrt(8/3) value is 4. The gamma=2 endpoint requires its critical construction and is kept outside this subcritical derivation. Euclidean dimension of a measure support and spectral dimension are different objects.

The primary source recovered independently is arXiv:2109.01252v2, equations (2.1)-(2.5) and its dimension section. Heat-kernel regularization gives the LFPP crossing

    C_eps(xi)=inf_P integral_0^1 exp(xi h_eps^*(P(t))) |P'(t)| dt,

where P is a piecewise C^1 left-to-right crossing staying in [0,1]^2. Let a_eps(xi) be a median of C_eps(xi). The known normalization exponent is

    a_eps(xi)=eps^(1-xi Q(xi)+o(1)).

In the subcritical branch xi=gamma/d_gamma and Q(xi)=2/gamma+gamma/2. Thus the hardest numerical input is the exact function Q(xi), or equivalently the exact LFPP crossing exponent chi(xi)=1-xi Q(xi). Gaussian area normalization does not evaluate it. These are sourced reductions, not a proof of a formula for d_gamma.

If chi(xi) is explicitly determined at a genuine subcritical xi, elementary algebra gives

    q=(1-chi(xi))/xi > 2,
    gamma=q-sqrt(q^2-4) in (0,2),
    d_gamma=gamma/xi.

The other quadratic root is greater than 2 and is excluded. The relation d_gamma=gamma/xi assumes xi is on the actual LQG branch; it cannot be inferred from a guessed identity at an arbitrary candidate xi without branch identification. The known source states Q is non-increasing, so I do not assume strict invertibility without a separately checked source.

A precise missing lemma for a proposed chi_*(xi) is: for each allowed fixed xi and every delta>0,

    P(eps^(chi_*(xi)+delta) <= C_eps(xi)
      <= eps^(chi_*(xi)-delta)) -> 1 as eps -> 0.

The lower bound must exclude every admissible crossing, including crossings selected after seeing all fine-scale fields. The upper bound must construct a crossing with the claimed exponent. Both need the actual GFF joint covariance, overlap and geometry. A fixed-path moment calculation, constant shifts, or independent scale components without control of the selected path do not prove either sharp bound.

The independent attempt is INDEPENDENT.md: two exact Gaussian graph obstructions, the second at normalization-exponent scale. They isolate a minimal missing premise: control of the joint law of competing crossings, including the selection effect. They do not refute any particular LQG dimension conjecture.

Candidate route: retain the field-dependent crossing functional through a multiscale decomposition; derive conditional crossing costs together with path-overlap entropy under the revealed filtration; prove matching upper and lower exponents; then use the sourced algebra above. The unsolved step is the sharp matching estimate for the actual GFF crossing optimization. Replacing it by an i.i.d. path count is unproved.

NEXT: Finish the exact intake and owner-work/source checks, then read w516's candidate and audit its largest dependency or quantifier gap against the saved independent obstructions.
