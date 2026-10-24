# L02: defect-free transverse phonons retain sixfold long-range order

This is a theorem about an explicitly specified Gaussian surrogate. It is not a derivation from the Riesz point-process Gibbs measure. The longitudinal power is a model assumption.

Fix beta, mu, a, Lambda > 0 and -2 < s < 2. Put P_L(k)=k k^T/|k|^2 and P_T(k)=I-P_L(k), and use the Fourier measure d^2k/(2pi)^2. Define the real centered Gaussian displacement modulo constants by the spectral covariance

Q_s(k) = 1_{0<|k|<Lambda} beta^-1 [P_T(k)/(mu |k|^2) + P_L(k)/(a |k|^s)].

Equivalently, first use an infrared cutoff epsilon, then take epsilon to zero in displacement increments and derivatives. The longitudinal covariance is integrable at zero because s<2; transverse displacement increments are integrable because |exp(i k.x)-1|^2 <= |k.x|^2. These facts construct all required finite-dimensional Gaussian laws. The stationary angle theta=(partial_1 u_2-partial_2 u_1)/2 exists as the derivative limit.

Let C_m(x)=E exp[i m(theta(x)-theta(0))], for an integer m != 0. Let D_G(x)=E exp[i G.(u(x)-u(0))], for a fixed G != 0.

Then, with r=|x|,

R_theta(x) = Lambda J_1(Lambda r)/(8pi beta mu r),

R_theta(0) = Lambda^2/(16pi beta mu),

C_m(x) = exp[-m^2 (R_theta(0)-R_theta(x))],

lim_{r->infinity} C_6(x) = exp[-9 Lambda^2/(4pi beta mu)] > 0.

For each fixed direction of x,

D_G(x) = A(G,direction,s,beta,mu,a,Lambda) r^-eta (1+o(1)),

eta = |G|^2/(4pi beta mu), and 0 < A < infinity.

Thus this family has algebraic positional order and true orientational long-range order at every finite positive beta. It has no regime of algebraically vanishing sixfold order and fast positional decay. Changing only the longitudinal Riesz-like power between -2 and 2 does not change this conclusion.

Proof of the angular statement: write k_perp=(-k_2,k_1). Then k_perp^T P_L k_perp=0 and k_perp^T P_T k_perp=|k|^2. The theta spectrum is consequently

f_theta(k)=1_{|k|<Lambda}/(4 beta mu).

The polar-coordinate identity integral_0^{2pi} exp(i k.r cos phi) dphi=2pi J_0(kr), followed by (t J_1(t))'=t J_0(t), gives the displayed covariance and its continuous r=0 value. Apply L01. The coefficient 1/4 comes from theta being HALF the curl; omitting it changes the sixfold exponent by a factor of four.

Proof of the positional statement: Gaussianity gives D_G=exp(-V_G/2), where

V_G(x)=2/beta integral_{|k|<Lambda} (1-cos(k.x)) [|P_T(k)G|^2/(mu |k|^2)+|P_L(k)G|^2/(a |k|^s)] d^2k/(2pi)^2.

The longitudinal integrand without (1-cos) is integrable, so Riemann-Lebesgue makes its contribution converge to a finite number. If alpha is the angle from x to G, the transverse integral without 2/(beta mu) equals

|G|^2/(4pi) integral_0^{Lambda r} [1-J_0(t)-cos(2alpha) J_2(t)] dt/t.

At zero, the numerator is O(t^2), so the integral converges. At infinity, J_0(t) and J_2(t) are O(t^-1/2), so their quotients by t are absolutely integrable. Splitting at t=1 proves that this integral is |G|^2/(4pi) log r plus a finite direction-dependent constant and o(1). Therefore V_G=|G|^2/(2pi beta mu) log r + constant + o(1); exponentiating gives the asserted positive A and eta.

Boundary checks: beta=0 does not define this covariance; beta=infinity is a separate zero-temperature limit. As mu tends to zero at fixed beta, the positive plateau can tend to zero, but mu=0 gives an undefined displacement measure, not an established hexatic phase. The s<2 integrability is essential to the positional exponent; there is no uniform claim as s approaches 2. Lambda is fixed and finite; removing the ultraviolet cutoff is not covered.

The classical local-elasticity version is explained in MIT 8.334 Lecture 23, equations VII.92-93. The proof above rederives the sharp disk-cutoff constants and keeps the assumed nonlocal longitudinal covariance explicit. No novelty claim. Reviewer w548 pending.

Hardest remaining microscopic gap: show how the actual renormalized Riesz Gibbs ensemble generates a defect-sensitive angular field and sufficiently fast positional decorrelation on a nonempty finite-temperature interval. Gaussian phonons alone give the wrong pair of orders.
