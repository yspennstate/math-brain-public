# Conditional Brownian-driving identification for C0049

Independent derivation saved 2026-10-10 before reading w588's proof. Mathematical status: proved special case, pending w590's independent check. This is an abstract reduction and does not prove discrete FK observable convergence.

## Exact assumptions

Fix sigma>0. Work on a filtered probability space satisfying the usual conditions. Let W be a continuous adapted real process with W_0=0, and let g_t be its capacity-parametrized chordal Loewner maps:

    dg_t(z) = 2/(g_t(z)-W_t) dt,     g_0(z)=z.

For every positive integer m, before z=im is swallowed, assume both real and imaginary parts of

    M_t(z) = exp(sigma (Log g'_t(z) - Log(g_t(z)-W_t)))

are continuous local martingales in the SAME filtration. Log g'_t is the continuous logarithm starting at 0; Log(g_t-W_t) uses the upper-half-plane branch. No unaccounted random phase or time-dependent normalization factor is permitted. M_0(z)=z^(-sigma).

Conclusion: W is a continuous local martingale with quadratic variation 8t/(1+sigma), hence W/sqrt(8/(1+sigma)) is standard Brownian motion in that filtration. This identifies its Loewner chain with chordal SLE(8/(1+sigma)). It does not assert convergence of discrete curves in any topology.

## Proof

1. Deterministic survival. Write Z_t=g_t(im)-W_t=X_t+iY_t. Because W is real, dY_t=-2Y_t/|Z_t|^2 dt. Therefore d(Y_t^2)=-4Y_t^2/|Z_t|^2 dt >= -4dt, giving Y_t^2 >= m^2-4t. For a fixed finite T choose integer m with m^2>4T. This point stays strictly inside the Loewner domain throughout [0,T]. Also g'_t is nonzero, since it solves dg'_t=-2g'_t/Z_t^2 dt.

2. Recover the semimartingale premise instead of assuming it. M_t(z) never vanishes on [0,T]. Locally along its continuous path choose the smooth holomorphic branch h(u)=u^(-1/sigma) matching h(M_t(z))=Z_t/g'_t(z). Such a branch exists in every disk avoiding 0, and its matching phase continues along the path. A C^2 function of a two-dimensional continuous local martingale is a semimartingale. Both g_t(z) and g'_t(z) are adapted finite-variation processes on [0,T]. Thus

    W_t = g_t(z) - g'_t(z) h(M_t(z))

is a real continuous semimartingale, locally and hence on [0,T]. Localize on compact subsets avoiding 0 and infinity before using derivatives. Continuous path lifting patches the branches; it does not assume a global single-valued power on C minus {0}.

3. Determine drift and bracket. Decompose W=L+A, with L a real continuous local martingale, A continuous predictable finite variation, and L_0=A_0=0. Put V=<L>. Complex Ito applied with the same continuous branches gives

    dM_t/M_t = sigma/Z_t dL_t
                 + sigma/Z_t dA_t
                 + sigma/Z_t^2 ((sigma+1)/2 dV_t - 4dt).

The coefficient -4 is the sum of the -2 from g'_t and the -2 from g_t. The quadratic variation term is sigma(sigma+1)/2. Since M is a complex local martingale, uniqueness of the real two-component semimartingale decomposition makes its finite-variation part zero. Multiply the resulting complex measure equality by Z_t^2/(sigma M_t), or equivalently start from the un-divided dM formula, to get

    Z_t dA_t + (sigma+1)/2 dV_t - 4dt = 0.

Taking imaginary parts gives Y_t dA_t=0. Since Y_t is continuous and bounded away from zero on [0,T], dA_t=0, including any signed or singular drift. Taking real parts then yields dV_t=8/(sigma+1)dt. This uses the FULL complex martingale, not just its real part.

4. For every T an m as above gives the same conclusions on [0,T]. Uniqueness of decomposition patches them over finite horizons. Levy's characterization gives the Brownian conclusion.

## The missing FK input

One must prove that the correctly normalized DISCRETE observable converges jointly with the explored slit domain to this M, and that the discrete conditional martingale identities pass to the limiting filtration after localization. Static convergence in a fixed smooth domain, an assumed Brownian driver, or conditional means without the actual filtration do not supply that input. For q in [1,4] the spin relation sin(pi*sigma/2)=sqrt(q)/2 gives 0<sigma<=1 and kappa=8/(1+sigma); exact primary-source matching remains to be saved. For q<1 the relevant crossing/tightness input must also be established rather than extrapolated.

NEXT: Ask w590 to check branch recovery, signed-measure drift elimination, and the absence of an assumed semimartingale driver; then audit the paired proof's observable convergence and limiting filtration.
