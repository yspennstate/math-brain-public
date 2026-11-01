# Independent Gaussian boundary calculation for P0321

w547, 2026-10-10. Frozen before reading w546's candidate proof. Author derivation; independent review pending. These are auxiliary Gaussian statements, not theorems about the Riesz Gibbs gas or claims of novelty.

## Exact model and claim C002

Fix T, mu, a, Lambda > 0, 0 <= p <= 2, and G in R^2 with G != 0. For k != 0 write P_L(k)=k k^t/|k|^2 and P_T(k)=I-P_L(k). Use the Fourier measure d^2k/(2*pi)^2. The centered real Gaussian displacement field, defined modulo a constant, has spectral covariance

    S_p(k) = T [P_T(k)/(mu |k|^2) + P_L(k)/(a |k|^p)] 1_{0<|k|<Lambda}.

It is enough to construct the field at an infrared cutoff epsilon, anchor u(0)=0, and take the joint Gaussian limit of all increments as epsilon -> 0. Increment covariances converge: near zero, 1-cos(k.x) is O(|k|^2), so all stated integrals are finite. Absolute u(x) without an anchor need not exist. The ultraviolet cutoff is essential for the pointwise rotation observable below.

Define C_G(x)=E exp(i G.(u(x)-u(0))). Define the mean-square curl theta=(partial_1 u_2-partial_2 u_1)/2 and C_6(x)=E exp(6 i (theta(x)-theta(0))). These are proxies defined by this model; theta is not being identified with a Voronoi/Delaunay bond observable in the gas.

For each fixed unit vector e and fixed p<2 there is A_p(G,e)>0 such that, as r -> infinity,

    C_G(r e) = A_p(G,e) r^(-eta_T) (1+o(1)),
    eta_T = T |G|^2/(4*pi*mu).

At p=2 the corresponding exponent is

    eta_T + eta_L,  eta_L = T |G|^2/(4*pi*a),

again with a finite positive prefactor. For every p in [0,2],

    lim_{|x|->infinity} C_6(x) = exp(-9 T Lambda^2/(4*pi*mu)) > 0.

Consequently this specified Gaussian model cannot have exponentially decaying C_G at positive T, and its C_6 does not have algebraic decay to zero. In particular, a harmonic proxy calculation of this form cannot by itself certify the standard hexatic correlation signature. No nonexistence conclusion about P0321 follows.

## Proof of C002

Gaussian characteristic functions give the exact expression

    -log C_G(x) = T integral (1-cos(k.x))
       [G.P_T(k).G/(mu |k|^2) + G.P_L(k).G/(a |k|^p)] d^2k/(2*pi)^2.

The factor is T, not T/2: the increment variance supplies the factor 2. There is no multiplication of conditional estimates and no independence premise beyond the specified joint Gaussian covariance.

Put x=r e and let alpha be the angle from e to G. In polar coordinates with phi measured from e, define

    F(z)=integral_0^z (1-cos t) dt/t, F(0)=0.

The transverse integral without T/mu is exactly

    I_T(r,e) = |G|^2/(2*pi)^2 integral_0^(2*pi)
                    sin^2(phi-alpha) F(Lambda*r*|cos phi|) dphi.

For z>=1, F(z)-log z tends to a finite constant kappa. Indeed, it equals F(1)-integral_1^z cos(t) dt/t, and the latter converges by integration by parts. For 0<=z<=1, 0<=F(z)<=z^2/4. With R=Lambda*r>=1, these bounds imply

    |F(R |cos phi|)-log R| <= C + |log |cos phi||

away from the two zeroes of cos, which have measure zero. The right side is integrable over the circle. Dominated convergence, and integral sin^2(phi-alpha) dphi=pi, therefore give

    I_T(r,e) = |G|^2/(4*pi) log r + b_T(G,e,Lambda) + o(1),

with finite b_T. This proves the exponent without assuming an angular stationary-phase bound.

For p<2, the longitudinal spectral integrand [G.P_L(k).G]/|k|^p is L^1 on the cutoff disk. The Riemann-Lebesgue lemma gives

    I_L,p(r,e) -> |G|^2 Lambda^(2-p)/(4*pi*(2-p)).

For p=2, repeat the F argument with cos^2(phi-alpha) in place of sin^2(phi-alpha). Its angular integral is also pi, so

    I_L,2(r,e) = |G|^2/(4*pi) log r + b_L(G,e,Lambda) + o(1).

Combining these terms and exponentiating gives finite strictly positive prefactors in both cases. In particular -log C_G(r e)/r -> 0; it is impossible to bound C_G(r e) by M exp(-c r) for all sufficiently large r with c,M>0.

For the curl, its Fourier multiplier annihilates the longitudinal projector. Its spectral covariance is T/(4*mu) on the cutoff disk. Thus

    sigma_theta^2 = T Lambda^2/(16*pi*mu),
    Cov(theta(x),theta(0)) = T/(4*mu) integral_{|k|<Lambda} cos(k.x) d^2k/(2*pi)^2 -> 0.

The last limit follows from integrability and the Riemann-Lebesgue lemma. Hence

    C_6(x) = exp[-36 (sigma_theta^2-Cov(theta(x),theta(0)))]

tends to the value claimed. Adding an independent common uniform angle to theta makes the one-point sixfold mean zero while preserving this pair correlation; that is the separate C001 obstruction.

## Sharp boundary corollary C003: noncommuting limits

Let L(p,r)=-log C_G,p(r e)/log r for r>1. For fixed finite r, its defining integral is continuous as p -> 2 from below. A dominating function near k=0 is a constant times (1-cos(k.r e))/|k|^2, which is integrable; on the rest of the fixed disk there is no singularity problem. Therefore

    lim_{p->2-} lim_{r->infinity} L(p,r) = eta_T,
    lim_{r->infinity} lim_{p->2-} L(p,r) = eta_T + eta_L.

Since eta_L>0, the limits differ. There cannot be a convergence estimate L(p,r)->eta_T uniform over all 0<=p<2. The finite longitudinal correction |G|^2 Lambda^(2-p)/(4*pi*(2-p)) diverges as p approaches 2. Merely extending a fixed-p long-range Gaussian asymptotic to the endpoint is an invalid bridge.

## Relation to the actual target and hardest gap

The symbol p is a stipulated stiffness exponent. Deriving it from the microscopic Riesz interaction, handling its endpoint (including any logarithmic kernel corrections), and identifying these proxy correlations with particle observables are separate unproved steps. The source's Riesz exponent s is not automatically interchangeable with p.

The hardest missing piece for a hexatic route is a controlled positive-temperature microscopic-to-defect theory: dislocations must disorder translation, while orientational correlations retain the required slow decay on an actual temperature interval. A curl of a single-valued Gaussian displacement has no such defect mechanism. This computation neither constructs a microscopic Gibbs measure nor controls free defects or their fugacity.

Independent reviewer: w548. Requested check: normalization; Gaussian increment construction; angular dominated convergence; p=2 continuity; distinction between elastic proxies and true bond correlations. Referee's own new results go to w551.
