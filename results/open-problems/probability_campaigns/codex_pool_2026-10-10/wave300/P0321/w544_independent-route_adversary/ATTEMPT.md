# P0321 independent route: compatible displacement fields

This route was saved before opening any proposed proof in w543. The earlier recorded route used rotation mixtures and a vanishing one-point order parameter. This route instead tests the compatibility between a displacement field and its induced local rotation.

The intake points to Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown* (2022), Section VI.B, PDF pages 66-67, https://arxiv.org/abs/2202.09240v2. The exact primary phase description is being checked. Current openness is UNKNOWN; neither the ranking nor this calculation establishes novelty or solves the gas problem.

The single hardest missing piece is a controlled passage from the microscopic, neutralized Riesz Gibbs law to a defect-bearing effective law, on a nonempty temperature interval, with errors strong enough to transfer both orientational and positional correlations through the thermodynamic and long-distance limits. A harmonic calculation in a fixed topological sector cannot supply that passage.

## Exact comparison model

Fix beta, a, b, Lambda, rho > 0 and 0 < s < 2. Let u be a centered real Gaussian vector field defined modulo constants, with Fourier covariance

    beta^{-1} 1_{0<|k|<=Lambda} [ P_L(k)/(a |k|^s) + P_T(k)/(b |k|^2) ],
    P_L(k) = k k^T / |k|^2,    P_T(k) = I - P_L(k),

using inverse Fourier measure d^2 k/(2 pi)^2. This is a stipulated Gaussian model, not a derived Riesz point process. The transverse infrared singularity prevents stationary values of u, but increments and all its derivatives are well defined: the increment factor 1-cos(k dot r) cancels that singularity, and the cutoff controls high frequencies.

Define the *linearized rotation* theta = (partial_1 u_2 - partial_2 u_1)/2. Define the linearized density fluctuation delta rho = -rho div u. These are precise observables of the comparison model, not an identification with Delaunay bond angles of particles.

## Derivation A: orientational correlations do not become hexatic

The Fourier multiplier of theta is (i/2)(-k_2,k_1). It annihilates P_L, and its squared norm is |k|^2/4. Consequently its spectral density is exactly

    f_theta(k) = 1_{|k|<=Lambda} / (4 beta b).

The covariance is integrable in frequency. Its variance is

    C_theta(0) = Lambda^2/(16 pi beta b),

and the Riemann-Lebesgue lemma gives C_theta(r) -> 0 as |r| -> infinity. The Gaussian characteristic function therefore gives, for p=6,

    C_6(r) = E exp(6 i [theta(r)-theta(0)])
           = exp(-36 [C_theta(0)-C_theta(r)]),
    lim_{|r|->infinity} C_6(r) = exp(-9 Lambda^2/(4 pi beta b)) > 0.

This is long-range orientational order at every fixed positive beta and b. It is incompatible with a claimed positive decay exponent C_6(r) asymptotic to r^{-eta_6}, eta_6>0, inside this comparison model. Taking beta down to zero after the spatial limit is a different limit; allowing b to vanish with volume changes the hypotheses.

The formula can also be written

    C_theta(r) = Lambda J_1(Lambda |r|)/(8 pi beta b |r|),

with its continuous value at r=0. This exact expression is reserved for a constant check, not an unproved assertion about the gas.

## Derivation B: density suppression does not determine orientational decay

The density multiplier i rho k annihilates P_T. Therefore

    f_{delta rho}(k) = rho^2 |k|^{2-s} / (beta a),  0<|k|<=Lambda.

It tends to zero, independently of b. This is suppressed long-wavelength density noise in the linear model. It is not a particle-process hyperuniformity theorem. The longitudinal density sector therefore cannot fix the orientational exponent: the latter depends on the transverse sector that density does not see.

## Derivation C: algebraic positional correlations identify the comparison as solid

For any nonzero fixed vector G, let

    Q_G(r) = E exp(i G dot [u(r)-u(0)]).

The longitudinal contribution to Var(G dot Delta u) converges to a finite constant because |k|^{-s} is integrable in two dimensions for s<2. The transverse contribution is

    (|G|^2/(2 pi beta b)) integral_0^{Lambda |r|}
        [1-J_0(t)-cos(2 alpha) J_2(t)] dt/t,

where alpha is the angle between G and r. The numerator is O(t^2) at zero; J_0 and J_2 are O(t^{-1/2}) at infinity. Thus this integral is log |r| + O(1), with the constant allowed to depend on direction, and

    log Q_G(r) = -(|G|^2/(4 pi beta b)) log |r| + O(1).

For each fixed direction, the O(1) term has a limit after adding log |r|. Thus Q_G has algebraic rather than short-range decay. The comparison model has the order pattern expected of a two-dimensional solid: algebraic positional correlations and nonzero limiting orientational correlations. Replacing absence of *strict* positional long-range order with *short-range* positional order is essential when defining the distinct intermediate phase.

## Topological premise that a harmonic transfer would miss

For a single-valued C^1 displacement u on a neighborhood of a closed piecewise C^1 loop gamma,

    integral_gamma partial_j u_i dx_j = 0

for each component i, by the fundamental theorem along the parameterized loop. Nonzero Burgers circulation requires leaving that single-valued displacement sector (a singularity, cut, or topological transition). The UV-cutoff Gaussian model is locally smooth and remains in the zero-Burgers sector. This elementary identity does not prove that actual Gibbs configurations lack dislocations.

To replace theta by an independent massless angular field with stiffness K_A one must derive that new law. Simply giving theta a covariance proportional to |k|^{-2} changes f_theta above; within compatible Gaussian elasticity it would require transverse displacement stiffness of order |k|^4 rather than b |k|^2. The missing premise is a justified loss of the stable shear sector and control of defects, not the Gaussian characteristic-function identity.

## Review scope and remaining work

All calculations above concern a specified Gaussian comparison model. They furnish a candidate obstruction to a harmonic-only proof route. They do not prove or disprove P0321. w545 is the designated independent reviewer; no independent verdict has been received. Next: check constants by finite Fourier sums under a fresh compute gate, then inspect w543's proposed argument for precisely the displacement-to-angle transfer.
