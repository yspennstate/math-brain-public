# L05: smooth bounded angle perturbations defeat covariance-only transfer

Fix m=6, h=2pi/m, and 0<A<1/m. Let g be L03's anchored stationary-increment Gaussian field. Let V,U be independent uniforms in [0,h), independent of g. Define f_A(t)=t+A sin(mt), q_A(x)=f_A(g(x)+V)-f_A(V), and theta_A(x)=U+q_A(x).

The map f_A is smooth and strictly increasing because f_A'(t)>=1-mA>0. It satisfies f_A(t+h)=f_A(t)+h, and |q_A(x)-g(x)|<=2A. The finite ultraviolet cutoff admits a smooth spatial modification of g: every positive-order derivative has finite spectral moments; Gaussian local Sobolev bounds of arbitrarily high order and Sobolev embedding give a C-infinity version. Discontinuous rounding is unnecessary.

The field q_A has stationary increments. For every x,y with v=Var(g(x)-g(y)),

Var(q_A(x)-q_A(y)) = v+A^2(1-exp[-m^2 v/2]).

Thus the variance differs from the Gaussian variance by at most A^2. Nevertheless its m-fold correlation tends to J_1(mA)^2>0 at large separation. The m-fold phase field is stationary, with zero one-point mean.

Proof of stationary increments: for a shift a, W_a=(g(a)+V) modulo h is uniform conditionally on g. The identity q_A(x+a)-q_A(a)=f_A(g(x+a)-g(a)+W_a)-f_A(W_a), together with stationary joint Gaussian increment laws, proves all finite-dimensional increment invariances. Adding U makes the phase stationary: U+q_A(a) modulo h remains uniform conditionally on g,V.

Proof of the exact variance: condition on g and use W=(g(y)+V) modulo h. For delta=g(x)-g(y), the increment is delta+A[sin(m(W+delta))-sin(mW)]. Its correction has conditional mean zero and conditional variance A^2(1-cos(m delta)). Total variance and the Gaussian characteristic function give the formula. Spatial increments were not assumed independent.

Proof of the positive plateau: p(t)=exp[i m f_A(t)] is h-periodic of unit modulus. Put c_n=(1/h) integral_0^h p(t) exp(-i m n t) dt. Integrating over W gives the periodic autocorrelation; averaging the centered Gaussian delta gives

C_m(x-y)=sum_{n in Z}|c_n|^2 exp[-m^2 n^2 v/2].

Parseval gives sum |c_n|^2=1. By L03, v tends to infinity, so dominated convergence gives limit |c_0|^2. For z=mA in (0,1), c_0=(1/(2pi)) integral_0^{2pi} exp[it+i z sin t]dt=-J_1(z). Positivity does not require a Bessel zero table: the constant Fourier coefficient of exp(it)(1+i z sin t) is -z/2, and the averaged Taylor remainder has modulus at most z^2/4. Hence |c_0|>=z/2-z^2/4>0. The U average makes the one-point mean zero.

For A=1/12, the plateau is J_1(1/2)^2, while the variance error is at most 1/144. Logarithmic variance with O(1) error, smoothness, stationary increments, and a bounded monotone perturbation of a Gaussian lift still do not imply algebraically vanishing sixfold order. The transfer must control periodic characteristic functions, not only covariance. This is an abstract counterexample to a stronger bridge, not a Riesz Gibbs law or a refutation of P0321.

Reviewer w548 pending. No novelty claim.
