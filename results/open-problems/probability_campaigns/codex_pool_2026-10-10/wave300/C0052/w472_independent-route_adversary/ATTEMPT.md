# C0052 independent route checkpoint (2026-10-10)

This checkpoint precedes reading w471's proposed proof. Independent referee: w473 (pending). No solution or novelty claim is made.

Route: use complex-field Lee-Yang zeros of a nonnegative block magnetization, rather than estimating a random-current intersection. For a finite zero-field ferromagnetic Ising measure with free or periodic boundary, let S be a nonzero nonnegative weighted sum of spins, X=S/sqrt(E S^2), and F(z)=E exp(zX). Assume the Lee-Yang property for this particular marginal. Because X is bounded, F is even, of exponential type, with F(0)=1 and zeros in imaginary pairs +/- i r_j. Pairing the Hadamard product gives F(z)=product_j(1+z^2/r_j^2), counting all positive zeros with multiplicity. There is no Gaussian prefactor at finite volume: the entire function has order at most one, and evenness removes the possible linear exponential factor.

Differentiate the logarithm near zero. Since Var(X)=1,

    sum_j r_j^(-2) = 1/2,
    3-E X^4 = 12 sum_j r_j^(-4).

Writing r_1 for the smallest positive zero yields

    12/r_1^4 <= 3-E X^4 <= 6/r_1^2.

Thus a bound r_1 <= R uniform along a critical sequence would give a fourth-moment deficit at least 12/R^4. Also F(t)<=exp(t^2/2) for real t, so all moments are uniformly integrable. Any weak limit under such a bound is non-Gaussian. Conversely r_1 -> infinity gives a Gaussian limit: for |z|<r_1, the error between log F(z) and z^2/2 is at most |z|^4/[4 r_1^2 (1-|z|^2/r_1^2)]. This is an elementary zero criterion, not a proof that r_1 stays bounded in 3D.

The hardest missing premise is a bound on the FIRST VARIANCE-NORMALIZED zero for the SAME critical 3D block law and limit/boundary regime as the target. Mere Lee-Yang zero location, susceptibility divergence, or an unnormalized first zero tending to zero does not yet establish it. In particular, replacing the infinite-volume critical block by a finite box with free/periodic boundary needs an explicit comparison or a compatible target statement.

Next: recover the target's exact primary statement and prior local routes; verify the product identities against a primary Lee-Yang source; then inspect w471's actual key step.

## Source recovery and disjoint continuation

The exact source target is the subcritical infinite-volume coupling, followed by beta increasing to beta_c (Duminil-Copin 2017, p94). A critical block criterion alone needs a bridge to this target. After the independent checkpoint above, w471's precommit was found to use the same Lee-Yang method. Its full L1/L2 proof was then read and audited. To avoid repeating its computations, the new work here uses the thermodynamic cumulant-density normalization, a variance-weighted zero measure, and an exact 1D transfer-matrix obstruction to an invalid order-of-limits shortcut. The complete derivations, assumptions, and KEEP-conditional verdict are in THERMAL_TRANSFER.md. Current openness is UNKNOWN; C0052 remains unproved in this packet.

NEXT: Send the concrete review packet to w473; the next proof step is the uniform 3D zero-mass bound, with the thermodynamic and critical limits in the stated order.
