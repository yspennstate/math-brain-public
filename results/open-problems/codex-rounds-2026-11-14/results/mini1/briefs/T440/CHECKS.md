# Checks and limitations

## Independent calculation of the barrier

For the scalar drift \(b(y)=y[d-\alpha y]\) and covariance amplitude \(a(y)=y(1-y)\), the zero-energy branch of the scalar Hamiltonian
\[
 H(y,p)=b(y)p+\tfrac12a(y)p^2
\]
is \(p(y)=-2b(y)/a(y)\). Integrating from the stable point \(q\) down to the absorbing endpoint gives
\[
 \int_q^0 p(y)dy
 =2\int_0^q\frac{d-\alpha y}{1-y}dy
 =2\int_0^q\left(\alpha-\frac\lambda{1-y}\right)dy
 =2[\alpha-\lambda+\lambda\log(\lambda/\alpha)].
\]
This independently checks the sign and factor of two in the exponent. No large-deviation principle for the infinite-dimensional process is used or inferred here. The numerical audit also integrates the middle expression directly, without evaluating F at q.

## Independent calculation of the scalar multiplier

The following flux matching is a check on the multiplier, rather than an additional proof of the asymptotic. The rigorous argument is Section 3 of PROOF.md.

The scalar forward probability flux is
\[
 j=b p-\frac{(a p)'}{2\nu}.
\]
In the bulk the zero-flux density is \(p(y)\simeq A e^{\nu F(y)}/a(y)\). A local Gaussian normalization at q gives
\[
 A\simeq a(q)e^{-\nu V}\sqrt{\frac{\nu|F''(q)|}{2\pi}}.
\]
At the absorbing boundary, write the outward loss flux as \(j=-J\). Replace \(b(y)\) by \(dy\) and \(a(y)\) by \(y\). If \(w(y)=y p(y)\), the boundary-layer equation is
\[
 w'-2\nu d w=2\nu J,\qquad w(0)=0.
\]
It has solution
\[
 w(y)=\frac Jd(e^{2\nu d y}-1).
\]
Matching in \(\nu^{-1}\ll y\ll1\) gives \(A=J/d\). Thus the reciprocal flux has multiplier
\[
 \frac1{d a(q)}\sqrt{\frac{2\pi}{\nu|F''(q)|}}
 =\frac{\sqrt\pi}{d\sqrt{\nu a(q)d}}
 =\frac{\alpha\sqrt\pi}{\sqrt\lambda d^2\sqrt\nu},
\]
where \(b'(q)=-d\), \(F''(q)=2b'(q)/a(q)\), and \(a(q)=\lambda d/\alpha^2\). This calculation checks both boundary and bulk factors separately.

Time scaling provides another check. Setting \(s=\alpha t\) reduces the parameter triple to \((1,r,\alpha\nu)\). The normalized scalar constant is
\(\sqrt\pi/[\sqrt r(1-r)^2]\); multiplying the lifetime by \(1/\alpha\) and the noise factor by \(1/\sqrt\alpha\) gives exactly the constant above. This scaling check also applies to the stated full diffusion, without identifying its sharp rate.

## Numerical cross-check

Run:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1
```

The script compares the positive exact integral in its original order with the Tonelli-reversed expression
\[
 e^{-\nu V}u_\nu(x_0)=2\nu\int_0^1
 \frac{e^{\nu(F(y)-V)}}{a(y)}
 \left(\int_0^{\min(x_0,y)}e^{-\nu F(z)}dz\right)dy.
\]
It stores both values, the asymptotic ratio, and independent barrier and multiplier checks in audit_data.csv. The checks use floating-point quadrature, not interval certification; the proof does not depend on them. The two orders share the integrand and quadrature library, so their agreement checks numerical integration and implementation but cannot by itself certify the modelling or generator normalization. Those are checked algebraically above.

## Attempts to break the argument

1. **Direction of the comparison.** The exact excess drift is
   \(\alpha X_0\sum_{k\ge2}(k-1)X_k\ge0\). Since \(u_\nu'>0\), the full generator is at least -1. The stopped identity then bounds the lifetime from below, as in (10). Reversing this inequality would be wrong.
2. **Upper endpoint.** Absorbing or killing at 1 would change the scalar problem. Formula (7) yields \(u_\nu'(1)=1/\lambda\), and the degenerate generator there is \(-\lambda\partial_x\). This gives -1 without any added boundary condition.
3. **Lower endpoint.** \(u_\nu'\) diverges logarithmically at 0, so applying Itô directly at 0 would be unjustified. The proof stops at epsilon, proves boundedness of \(u_\nu\), and only then passes to the boundary.
4. **Negative F beyond the saddle.** For example, at \(\alpha=1,\lambda=0.8\), F at the Poisson initial mass is negative. Bounding the outer integral by a global saddle approximation would then introduce a spurious larger exponential. The four-region estimate instead keeps the cancellation for z beyond b. This parameter pair is included in the audit.
5. **Critical and zero-mutation limits.** The constant diverges as \(\lambda\uparrow\alpha\) or \(\lambda\downarrow0\). The theorem fixes parameters strictly inside the range. At \(\lambda=\alpha\) the saddle collides with 0, while at \(\lambda=0\) the upper boundary changes character and the initial state is entirely class 0. Neither is covered. For \(\lambda>\alpha\), the scalar drift has no interior stable point, so continuing the formula for V would be wrong even though its algebraic expression is positive there.
6. **Initial state.** The Poisson mass satisfies \(x_0>q\), used to choose b. The actual Poisson profile is not supported on classes 0 and 1, so the drift comparison is generally strict, even at the initial time. An equality of exponential rates cannot be deduced.
7. **Expected time versus almost sure extinction.** The full expectation need not be assumed finite for the lower bound. Infinite expectation satisfies it automatically; the proof separates that case before sending time to infinity.
8. **No population-limit interchange.** Every stochastic step uses the diffusion in the question. No Wright--Fisher population size, Moran clicking rate, or limiting click process is substituted.

## What remains open

There is no upper bound matching V, and no prefactor for the full process. The bound supplies no positive metastable exponent at or above \(\lambda=\alpha\). It is not established that this comparison bound improves the strongest bounds already in the literature. It is an explicit verified partial result, without a novelty claim.
