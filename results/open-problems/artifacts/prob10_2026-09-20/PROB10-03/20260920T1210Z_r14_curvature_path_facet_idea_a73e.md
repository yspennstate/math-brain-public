Runtime model: **GPT-5.6 Sol**. Requested GPT-6/maximum is not an authenticated configurable setting here; reasoning-effort telemetry is **UNVERIFIED**.

# PROB10-03 / R14 — idea-before-code: curvature-variability upper cage, positive KL path, and facet obstruction

Status: **analytical work written before checker / source endpoint not yet changed**.

Exact source target remains: `M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)` exactly, and `<g_a,sigma> >= -sqrt(N)` for every `a<=M`, at fixed `kappa=-1` as `N->infinity`. A lower endpoint means SAT probability tends to one; an upper endpoint means SAT probability tends to zero.

The current entering repository-supported source bracket, after consuming the newer NM13-07 recentered complete-second certificate, is

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963446`,

`W = 6.01666008494`.

The `12.28722...` third-full capacity point remains numerical/conditional: no outward four-overlap inclusion has promoted it to a source endpoint.

## Attack A — exploit nonconstant curvature, rather than only its cap

The previous R14 run proved that the generic lower KL inequality based only on `(mean, score variance, curvature cap)` is sharp for quadratic tilts. This attack uses the *distribution* of curvature and gives an interval-friendly **upper** information cage whose correction vanishes when the curvature is constant.

Let `gamma=N(0,1)` and

`d nu/d gamma = exp(phi)/Z`,

where `phi` is concave and sufficiently regular/integrable for Gaussian integration by parts and Brascamp--Lieb. Put

`r=phi'`, `tau=-phi''>=0`,

`mu=E_nu X`, `v=Var_nu(X)`, `a=E_nu tau`,

and let `G=N(mu,v)` be the matching Gaussian.

### Theorem A1 — curvature-variability matched-Gaussian cage

Define

`eta_tau := (1/(1+a)) E_nu[(tau-a)^2/(1+tau)]`.

Then

`1 <= v(1+a) <= 1+eta_tau`,                                         (A.1)

and

`D(nu||gamma)`

` <= D(G||gamma) + (1/2) log(1+eta_tau)`.                           (A.2)

Here

`D(G||gamma)=(mu^2+v-1-log v)/2`.

The correction is zero for every quadratic tilt, because then `tau` is constant.

### Proof

The Lebesgue density of `nu` is proportional to

`exp(phi(x)-x^2/2)`.

If `ell=log(dnu/dx)`, then `ell''=-(1+tau)`. Therefore the ordinary Fisher information is

`J(nu)=E[(ell')^2]=-E ell''=1+a`.                                   (A.3)

The one-dimensional Cramer--Rao inequality gives

`v J(nu)>=1`, proving the left side of (A.1).

Brascamp--Lieb for the strongly convex potential `x^2/2-phi(x)` gives

`v <= E[1/(1+tau)]`.                                                 (A.4)

The following identity is exact:

`(1+a) E[1/(1+tau)] - 1`

` = (1/(1+a)) E[(tau-a)^2/(1+tau)]`

` = eta_tau`.                                                        (A.5)

Indeed, pointwise

`(tau-a)^2/(1+tau) = tau-(1+a) + (1+a)^2/(1+tau)`,

and expectation uses `E tau=a`. Combining (A.4)--(A.5) proves the right side of (A.1).

Next, matching first and second moments gives the exact information projection decomposition

`D(nu||gamma)=D(G||gamma)+D(nu||G)`.                                (A.6)

Stam's entropy--Fisher inequality yields

`D(nu||G)=h(G)-h(nu) <= (1/2)log(v J(nu))`.                          (A.7)

Insert (A.1) and (A.3) into (A.7) to obtain (A.2). QED.

### Inner hinge specialization

For the exact one-step perceptron kernel at fixed `x`,

`d rho_x/d gamma_H proportional exp[-B(x+sH)_+^2]`,

put

`A=2Bs^2`, `pi_x=P_{rho_x}(x+sH>0)`.

Then, a.e.,

`tau(H)=A 1_{x+sH>0}`,

so `a=A pi_x`, and direct two-point algebra gives

`eta_tau = A^2 pi_x(1-pi_x)/(1+A)`.                                 (A.8)

The exact Gaussian integration-by-parts identities already used in the repository give

`mu=s u_x(x)`,

`v=1+s^2 u_xx(x)`.

Hence

`KL(rho_x||gamma_H)`

` <= (1/2){s^2 u_x^2+s^2u_xx-log(1+s^2u_xx)}`

`    +(1/2)log(1+A^2 pi_x(1-pi_x)/(1+A))`.                           (A.9)

This upper cage uses only the closed kernel derivatives and the tilted positive-tail probability. Its non-Gaussian correction automatically decays in both outer tails where `pi_x` approaches `0` or `1`.

### Outer tilted-U specialization

For fixed outer `V=v`, with

`X=dU+sqrt(p3)v-1`,

`d nu_v/d gamma_U proportional exp[m u(X)]`,

the curvature is

`tau_v(U)=m d^2[-u_xx(X)]`.

Thus Theorem A1 gives a curvature-only upper enclosure of the outer KL contribution using

`a_v=<tau_v>_v`,

`eta_v=(1/(1+a_v))< (tau_v-a_v)^2/(1+tau_v) >_v`,

with no score-variance term. This is intended as a complementary subdivision cage, not as a claim that it is numerically tighter than the existing exact-Fisher matched-Gaussian upper cage.

## Attack B — remove subtractive KL evaluation by a positive thermodynamic path

The expensive third-full `c`-sector quantities are KL divergences. They can be represented exactly as integrals of nonnegative variances, which is better suited to rigorous interval subdivision than subtracting two nearby log-partition terms.

Let `mu_0` be any probability measure, let `Y` have finite exponential moments on `[0,T]`, and define

`F(t)=log E_{mu_0} exp(tY)`,

`d mu_t/d mu_0=exp(tY-F(t))`.

Then

`D(mu_t||mu_0)=tF'(t)-F(t)`,

so

`d/dt D(mu_t||mu_0)=t F''(t)=t Var_{mu_t}(Y)`.                       (B.1)

Since the divergence vanishes at `t=0`,

`boxed: D(mu_T||mu_0)=int_0^T t Var_{mu_t}(Y) dt`.                  (B.2)

Consequently, for a partition `0=t_0<...<t_n=T`, if throughout each interval

`L_i <= Var_{mu_t}(Y) <= U_i`,

then rigorously

`sum_i (t_{i+1}^2-t_i^2)L_i/2`

` <= D(mu_T||mu_0)`

` <= sum_i (t_{i+1}^2-t_i^2)U_i/2`.                                (B.3)

This is a certified-positive quadrature principle: no cancellation between a log partition and an energy expectation remains.

### Third-full compilation

For the outer c-sector at fixed `V=v`, take

`Y=u(X)`, `T=m`, `mu_0=gamma_U`.

Then

`D_U(v)=int_0^m t Var_{nu_{v,t}}(u(X)) dt`,                          (B.4)

where `nu_{v,t}` is the same tilted U-law but with exponent `t` rather than `m`. Averaging in `V` yields the complete outer KL term.

For the inner hinge at fixed `x`, take

`Y=-(x+sH)_+^2`, `T=B`, `mu_0=gamma_H`.

Then

`KL(rho_x||gamma_H)`

` = int_0^B b Var_{rho_{x,b}}((x+sH)_+^2) db`.                       (B.5)

The H integral is still analytically closed at each `b`; the remaining extra path integration is one-dimensional and positive.

For interval implementation, note

`d/dt Var_{mu_t}(Y)=E_{mu_t}[(Y-E_tY)^3]`.                           (B.6)

Thus a rigorous bound on the third central moment gives a direct Lipschitz enclosure of the variance between path mesh points. Existing Gaussian-tail moment envelopes can supply this without assuming any monotonicity.

### Negation test: variance monotonicity is false in general

A tempting shortcut would be to suppose the variance in (B.2) decreases along the negative-energy tilt. This is false even for a two-point law.

Let `H` be Bernoulli(`p`) with `p>1/2` and tilt by `exp(-bH)`. At `b=0`,

`kappa_3(H)=p(1-p)(1-2p)<0`,

while

`d/db Var_b(H)|_{b=0}=-kappa_3(H)>0`.

So the variance initially **increases**. Any rigorous implementation of (B.3) must enclose the variance on each path cell rather than invoking an unproved monotonicity shortcut.

## Attack C — exact polar/facet first moment, and why it cannot improve the current upper endpoint

Set

`K_N=conv(-g_1,...,-g_M)`.

Writing `sigma=sqrt(N)u`, the constraints are exactly

`h_{K_N}(u)<=1`, `||u||=1`.

On `0 in int(K_N)`, which holds with high probability for fixed `alpha>2` by Wendel's theorem, the centered inradius satisfies

`r(K_N)=min_{||u||=1}h_{K_N}(u)`.

Therefore

`SAT <=> r(K_N)<=1`,

`UNSAT <=> r(K_N)>1`.                                                  (C.1)

In Gaussian general position, the inradius is the minimum distance from the origin to a facet hyperplane, and each facet has `N` vertices.

Fix an N-subset of vertices and let `G` be the `N x N` matrix with those vertices as rows. The distance `R` from the origin to their affine hyperplane is

`R^2 = 1/[1^T (GG^T)^(-1) 1]`.                                      (C.2)

A Wishart/Schur-complement calculation gives

`N R^2 ~ chi-square_1`,                                               (C.3)

so

`f_R(r)=sqrt(2N/pi) exp(-Nr^2/2)`, `r>=0`.

Conditional on that hyperplane, orient it so the origin is on the interior side. Each remaining Gaussian vertex lies on that side with probability `Phi(r)`, independently. Hence the expected number `Z_{<=1}` of facets whose support distance is at most one is exactly

`E Z_{<=1}`

` = C(M,N) sqrt(2N/pi) int_0^1 exp(-Nr^2/2) Phi(r)^(M-N) dr`.         (C.4)

For `M/N->alpha`, the exponential rate is

`F_alpha(r)`

` = alpha log alpha-(alpha-1)log(alpha-1)`

`   -r^2/2 + (alpha-1)log Phi(r)`.                                  (C.5)

For `alpha>=6`,

`F_alpha'(r)=-r+(alpha-1)phi(r)/Phi(r)>0` on `[0,1]`,

so this first-moment route is controlled by `r=1`. Markov's inequality can prove `r(K_N)>1` only if `F_alpha(1)<0`. The zero of `F_alpha(1)` will be evaluated only as a numerical diagnostic after this proof is written; it is expected to lie far above the current `12.31963446` endpoint.

Thus this geometrically natural one-facet first-moment dual is useful mainly as a rigorous obstruction: it cannot be the mechanism that improves the current source upper bound. Any successful polar route needs a many-facet/correlated covering argument or a higher-order dual certificate rather than a union bound over individual facets.

## Three-route comparison before coding

1. **Curvature variability (A):** exact new theorem, designed to use the perceptron-specific nonconstant curvature that the previous run proved was necessary. It supplies an additional cheap upper KL cage for subdivision.
2. **Positive KL path (B):** exact representation that attacks the interval-cancellation bottleneck directly. It appears more promising for a future outward third-full certificate because every quadrature contribution is nonnegative; the explicit Bernoulli counterexample prevents an invalid monotonicity shortcut.
3. **Facet first moment (C):** exact geometric duality plus an exact facet count formula, but the anticipated exponent shows the simplest dual first moment is far too weak. Record this obstruction rather than rerunning it.

No source endpoint is promoted in this idea note. Numerical evaluation, if used, comes only after these proofs and remains explicitly auxiliary.