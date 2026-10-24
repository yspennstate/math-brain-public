# P0315 — second serious attempt, 2026-10-11

## Two approaches not tried in the first attempt

1. **Finite normal form at infinity for every even beta.** At beta=2n,
   the exact moment system closes in dimension n. Construct a near-identity
   diagonalizing transformation for q'=(i diag(1,...,n)+C/r)q+b/r.
   Its distinct imaginary eigenvalues should permit a finite asymptotic
   integration argument, yielding actual harmonic expansions rather than
   only the first attempt's formal modes. The main remaining issue would
   be connection coefficients from the entrance solution at zero; this
   would remain a special-case route and would not control non-even beta.

2. **Synchronous contraction on the circle and a finite-density parametrix.**
   Couple the two exact entrance diffusions with the same complex Brownian
   motion. Their large forcing cancels in the difference. Test a fractional
   chordal distance V=(1-cos(theta-phi))^p. If its generator has a uniform
   negative drift for some p, obtain a genuine contraction estimate for
   the Markov kernels. Apply this directly to the Fourier observable,
   which is a Holder function on the circle, and compare the law with a
   finite inverse-distance density approximation. This attacks the
   infinite-mode remainder without a mode cutoff. We pursue this route.

## Brain query for the actual gap

Read-only math_recall: 'Qu Valko infinite Fourier moment hierarchy
asymptotic uniqueness weighted remainder'. It returned no relevant
theorem for this hierarchy. Another query on synchronous coupling will
be recorded below. Brain output is only a lead, never a proof.

## 1. Exact diffusion, now regarded as a circle Markov evolution

Use the exact Qu–Valko diffusion already derived in ATTEMPT.md. For
fixed final distance r and u<=0 it is

    d theta = (beta/4) r exp(beta u/4) du
              -(beta/2) sin(theta) du
              + Re[(exp(-i theta)-1)dZ_u].             (S)

Write x=r exp(beta u/4). The transition from distance s to distance r
corresponds to elapsed u-time (4/beta)log(r/s). The circle diffusion
in distance time x has generator

    L_x f = f' + x^(-1) M f,
    M f = (4/beta)(1-cos(theta)) f'' -2 sin(theta) f'. (G)

On any compact distance interval away from zero its drift and two real
noise coefficients are smooth and globally Lipschitz on the circle.
Thus it has a unique strong solution and Markov transition P_{s,r}.
The forcing in (S) is independent of the initial angle; this feature
is essential in the synchronous coupling below.

## 2. Fractional-distance contraction (proved)

Let theta,phi solve (S) with the same complex Brownian motion and the
same forcing. Set Delta=theta-phi modulo 2pi, h=1-cos(Delta), V=h^p.
Choose 0<p<1/2 and beta+2p<1. Define

    c=p(1-beta-2p)>0.

The difference drift is -(beta/2)(sin(theta)-sin(phi)), and its quadratic
variation density is 2(1-cos(Delta))=2h. For h>0, differentiation gives

    generator(V) / V
       = p[(p-1)+p cos(Delta)
                      -(beta/2)(cos(theta)+cos(phi))]
       <= p(2p-1+beta) = -c.                       (C)

For completeness, V'=p h^(p-1)sin(Delta), and
V''=p(p-1)h^(p-2)sin^2(Delta)+p h^(p-1)cos(Delta).
The diffusion contribution h V'' equals
pV[(p-1)+p cos(Delta)]. The drift contribution uses
(sin(theta)-sin(phi))sin(Delta)/h = cos(theta)+cos(phi).
Both identities hold away from h=0. The uniform inequality follows from
cos(Delta)<=1 and cos(theta)+cos(phi)>=-2.

Nonsmoothness at h=0 does not invalidate Ito's formula. If the two
initial angles coincide modulo 2pi, pathwise uniqueness makes them
coincide forever. Otherwise stop at tau_epsilon, the first time h<=epsilon,
and at a fixed finite time. V is smooth on the stopped region, and the
stopped stochastic integral is a true martingale: its coefficient is
bounded there. Ito's formula for exp(ct)V gives expectation at most its
initial value. The stopping times increase as epsilon decreases. If their
limit is finite, continuity gives h=0 at that time and pathwise uniqueness
gives h=0 afterwards. Otherwise there is no collision on the time interval.
In either case the stopped terminal V converges to the actual terminal V
(or to zero in the collision case). Fatou's lemma, with the nonnegative
exponential factor, therefore proves

    E V(theta_t,phi_t) <= exp(-c(t-a)) V(theta_a,phi_a). (SC)

This uses no differentiability of V at collision and no unproved local-time
assertion. All arguments take place on finite u intervals; their forcing
is bounded there, even though its bound depends on the final distance.
The contraction constant itself is independent of that forcing.

## 3. The exact correlation observable and its regularity

Let 0<beta<1 and put

    C_beta = Gamma(1+beta/2)^2 / Gamma(1+beta),
    g_beta(theta)=C_beta |exp(i theta)-1|^beta.

Qu–Valko's circle density (20), Fourier calculation in Lemma 10, and
Theorem 1 give the exact identity

    4 pi^2 T_beta(r) = integral g_beta d mu_r -1,       (O)

where mu_r is the law of the angle modulo 2pi in (S) at u=0.
Indeed g_beta has Fourier series 1+2 sum_{k>=1}w_k cos(k theta),
w_k=(-beta/2)_k/(1+beta/2)_k, convergent absolutely for beta>0.
The circle average of g_beta is 1 by the normalization in (20).
Consequently (O) is exactly the earlier correlation representation,
not a new approximation to the pair density.

For 0<beta<1, the elementary concavity bound |a^beta-b^beta|
<=|a-b|^beta, a,b>=0, follows by writing a=b+d and using
(b+d)^beta<=b^beta+d^beta. The latter follows, for b>0, by integrating
the decreasing derivative beta t^(beta-1) over [b,b+d] and comparing
with [0,d]; b=0 is immediate. The triangle inequality then yields

    |g_beta(theta)-g_beta(phi)|
       <= C_beta |exp(i theta)-exp(i phi)|^beta.

If 2p<=beta, the chord is at most 2, so the last quantity is at most
C_beta 2^(beta-p) V(theta,phi). Coupling (SC) and V<=2^p implies

    osc(P_{s,r}g_beta) <= G_beta (s/r)^kappa,
    G_beta=C_beta 2^beta,
    kappa=4p(1-beta-2p)/beta.                         (K)

Here osc is maximum minus minimum of a real continuous function. For
any finite signed measure nu of mass zero, subtracting a constant from
P g and using total variation gives the safe estimate

    |integral P_{s,r}g_beta d nu|
       <= G_beta (s/r)^kappa ||nu||_TV.              (KTV)

No Fourier cutoff is used. The Holder regularity of g_beta is essential;
it limits the admissible p to 2p<=beta.

## 4. A genuine two-term density approximation and its residual

Let

    a=1+2/beta, d=a(4/beta-1), e=-a(4/beta+1),
    f_x(theta)=(1/(2pi))[1+2a sin(theta)/x
                      +2(d cos(theta)+e cos(2theta))/x^2]. (P)

Its moments are Q_1=ia/x+d/x^2, Q_2=e/x^2, Q_k=0 for k>=3,
and Q_0=1. This is now an actual finite trigonometric density, not an
infinite formal sector. For

    R=max(1,8a,sqrt(8(|d|+|e|))),

the nonconstant part in square brackets has absolute value at most 1/2
for x>=R, so f_x is a probability density. Its smooth dependence on x
permits direct use in the Fokker–Planck equation of (G).

Put E_x=partial_x f_x-L_x^* f_x. Directly using the three relevant
moment equations, or differentiating (P), gives

    E_x(theta)=(1/(pi x^3)) sum_{k=1}^3 z_k cos(k theta),
    z_1=(4/beta-2)d-(2/beta-1)e,
    z_2=(16/beta-2)e-(8/beta+2)d,
    z_3=-(18/beta+3)e.                               (RES)

Here L_x^*f=-partial_theta f+x^(-1)[(4/beta)partial_theta^2
((1-cos(theta))f)+2partial_theta(sin(theta)f)]. Each term of orders
x^(-1) and x^(-2) cancels. The residual has mass zero and

    ||E_x||_TV <= H_beta x^(-3),
    H_beta=2(|z_1|+|z_2|+|z_3|).                     (TV)

The use of Fourier moments to check (RES) is exact: E_x is a
trigonometric polynomial of degree at most 3, so its mass and its first
three complex moments determine it. Higher moments vanish on both sides.

## 5. Duhamel estimate for the actual correlation (proved bound)

For r>=R the forward equation gives

    integral g_beta d(mu_r-f_r dtheta)
      = integral P_{R,r}g_beta d(mu_R-f_R dtheta)
           -integral_R^r integral P_{s,r}g_beta E_s dtheta ds. (D)

Here is justification without assuming an unproved infinite-hierarchy
uniqueness theorem. On a finite interval [R,r], smooth periodic test
functions are mapped by P_{s,r} to smooth functions satisfying the
backward equation; smooth globally bounded coefficients give smooth
stochastic flows and bounded derivative moments on that finite interval.
Apply the forward/backward product identity first to such a test function.
This gives (D) for every smooth test. Approximate the continuous g_beta
uniformly by smooth periodic functions. Markov kernels are contractions
in sup norm; mu_s and f_s are finite measures, and the integrated residual
has finite total variation by (TV). Thus all terms pass to the uniform
limit and (D) holds for g_beta. The entrance law mu itself is obtained
from the exact SDE, so its forward equation is already established.

Because both initial measures are probabilities, their difference has
TV<=2. Apply (KTV) and (TV), noting that 0<kappa<2:

    |integral g_beta d(mu_r-f_r dtheta)|
      <= G_beta r^(-kappa)
          [2R^kappa + H_beta integral_R^r s^(kappa-3) ds]
      <= G_beta [2R^kappa
                 +H_beta R^(kappa-2)/(2-kappa)] r^(-kappa). (ERR)

The finite approximation evaluates exactly by the weight cancellation
already checked in Coefficient.lean:

    integral g_beta f_r dtheta-1
       =2(w_1 d+w_2 e)/r^2 = -4/(beta r^2).

Combining (O) and (ERR) proves the following actual pointwise bound:

    |T_beta(r)+1/(pi^2 beta r^2)| <= B_beta r^(-kappa),
    B_beta=(G_beta/(4pi^2))
              [2R^kappa+H_beta R^(kappa-2)/(2-kappa)], r>=R. (THM)

This theorem is valid whenever 0<beta<1,
0<p<1/2, beta+2p<1, and 2p<=beta. In particular |T_beta(r)|
<=constant_beta r^(-kappa). It is a decay bound, NOT identification
of the displayed inverse-square term as an asymptotic leading term,
because every allowed kappa below is strictly less than 2.

Optimizing the proven bound subject to its actual Holder constraint gives

    p=beta/2, kappa=2-4beta,             0<beta<=1/3;
    p=(1-beta)/4, kappa=(1-beta)^2/(2beta), 1/3<=beta<1.

Both choices have beta+2p<1. At beta=1/3 they agree. The result improves
the exponent beta/2 in the previously recorded Qu–Valko bound for
0<beta<1/2; no novelty priority is asserted. For beta>=1/2 it is no
improvement over that bound and we retain the existing result instead.

## Remaining gap after the second approach

The coupling approach avoids the first attempt's moving Fourier cutoff
and proves an actual small-beta decay estimate. It still does not give
an error o(r^(-2)), nor any explicit oscillatory amplitude. Its largest
allowable contraction exponent is strictly below 2, because the exact
observable has only Holder-beta regularity and requires 2p<=beta.
Removing that loss would require a uniform smoothing estimate for the
rapidly driven, spatially degenerate circle diffusion, or a sharper
observable-specific cancellation argument. Such a smoothing estimate
has not been proved here. For beta>=1 the global contraction estimate
itself has no positive constant. General-beta harmonic amplitudes,
phases and higher-order pointwise remainders remain unproved.

## 6. Uniqueness of the probability-valued hierarchy for beta<1 (proved)

This supplies a separate reduction concerning the infinite hierarchy's
selection issue, with a precise additional constraint. Assume 0<beta<1
and that for every r>0 a sequence (q_k(r))_{k in Z} is positive definite,
q_0=1, q_{-k}=conjugate(q_k), its entries are continuous, and the positive
entries solve (H) from ATTEMPT.md. Then there is at most one such sequence
family on the whole interval r in (0,infinity). In particular the exact
SDE-selected sequence is uniquely characterized within this class.
No statement is made about arbitrary bounded complex solutions that
are not positive definite.

Here is a complete reduction to the already proved contraction. Positive
definiteness represents q as a probability measure on the circle. One
can see this without assuming a spectral theorem: the Fejer densities

    F_N(theta)=(1/(2pi)) sum_{j,l=0}^N
                 q_{j-l} exp(-i(j-l)theta)/(N+1)

are nonnegative by positive definiteness, and integrate to 1. Compactness
gives a subsequential weak limit; its kth moment is q_k because the
kth coefficient of F_N is (1-|k|/(N+1))q_k for |k|<=N.
Two measures with these moments coincide by density of trigonometric
polynomials in continuous periodic functions. Thus there is a unique
representing mu_r. Moment continuity implies weak continuity: approximate
any continuous test uniformly by a trigonometric polynomial, whose
integral is continuous, and use that all measures have mass 1.

The hierarchy implies the forward equation against trigonometric
polynomials. On any compact [s,r] with s>0, it extends to all smooth
periodic tests by uniform convergence of their Fourier approximations
and first two derivatives. The coefficients of L_x are bounded uniformly
on that finite interval, so the integrated forward equations pass to
this limit. The finite-interval backward-test argument in section 5
then gives mu_r=mu_s P_{s,r}. This uses smooth test functions only and
therefore does not require elliptic smoothing of nonsmooth functions.

The smooth backward-test fact used here can be justified directly from
the finite-interval SDE. The derivative J of a flow with respect to its
initial angle solves dJ=b_theta J du+sum sigma_{j,theta}J dB_j.
All coefficient derivatives are bounded on the finite interval, so Ito's
formula and Gronwall give finite moments of every order for J. The
second derivative solves the same linear equation with forcing terms
b_{theta theta}J^2 and sigma_{j,theta theta}J^2; its moments are finite
by the same estimates. Further derivatives follow inductively with
polynomial forcing in the lower derivatives. Difference quotients of
the solutions converge to these variational equations by the Lipschitz
estimates and Gronwall. Hence for a smooth periodic test one can
differentiate its expected value under the flow at least twice, using
the derivative moment bounds as domination. Markov composition and
Ito's formula on a short initial interval give the backward equation.
The resulting derivatives are continuous on the compact time interval.
To apply the weak forward equation to this time-dependent backward test,
first use finite sums of smooth time functions times trigonometric
polynomials, then approximate the test together with its time derivative
and first two space derivatives uniformly on the compact interval.
Integration of the product rule passes to the limit. This proves the
finite-interval propagation identity used in sections 5 and 6.

For two such families mu and nu, choose any admissible p with
0<p<min(1/2,(1-beta)/2). Every smooth periodic test f is Holder of
order 2p in chordal distance: bounded derivative gives a Lipschitz bound
in geodesic distance, geodesic distance is at most (pi/2) times chordal
distance, and the chord is at most 2. The contraction proof in section 3
applies to f with its own finite Holder constant, giving

    |integral f d(mu_r-nu_r)| <= C_f (s/r)^kappa, 0<s<r.

The initial difference has TV<=2, absorbed in C_f. Let s decrease to zero
while r is fixed. Since kappa>0, the right side tends to zero. All smooth
test integrals coincide, so mu_r=nu_r and all moments coincide. This
requires no specified entrance limit at zero; probability-valuedness on
the entire positive axis already forces uniqueness for beta<1.

## 7. Referee checks and the next obstruction

### Stronger consequence for fixed smooth modes

For 0<beta<3-2sqrt(2), the same method turns the first attempt's formal
inverse-square moment coefficients into actual asymptotics. Choose
p=(1-beta)/4; no condition 2p<=beta is needed for a smooth observable.
Its contraction exponent is kappa_*=(1-beta)^2/(2beta)>2.

Extend the finite density (P) by the third formal column from recurrence
(R) in ATTEMPT.md. Namely include moments sum_{j=1}^3 c_{k,j}r^(-j),
supported at k<=3, and their conjugates. All third-column coefficients
are purely imaginary, as proved in that recurrence. This finite
trigonometric density is normalized and is positive for all sufficiently
large R: one may take R=max(1,4 sum_{k=1}^3 sum_{j=1}^3 |c_{k,j}|),
which bounds the absolute nonconstant part by 1/2. The recurrence cancels
the actual forward equation through order r^(-3), leaving a residual
of order r^(-4), a trigonometric polynomial of degree at most 4 and
mass zero. Its total variation is bounded by H r^(-4) with a finite
beta-dependent constant. These are finite polynomial identities; they
do not assume convergence of the entire formal series.

Apply the same Duhamel proof to the smooth observable cos(k theta),
for any fixed integer k>=1. It is Holder of order 2p with a finite
k-dependent constant. The error is bounded by a constant times

    r^(-kappa_*) [1+integral_R^r s^(kappa_*-4) ds].

This is O(r^(-kappa_*)) if 2<kappa_*<3,
O(r^(-3)log r) if kappa_*=3, and O(r^(-3)) if kappa_*>3.
All are o(r^(-2)). Since the third column is imaginary and the second
column is supported only at k=1,2, we have proved for each fixed k:

    Re q_1(r) = d/r^2 + o(r^(-2)),
    Re q_2(r) = e/r^2 + o(r^(-2)),
    Re q_k(r) = o(r^(-2)), k>=3.                    (FIXED)

The constants depend on k; this is NOT the full correlation asymptotic.
Indeed for cos(k theta) the Holder-2p constant can be bounded by a
constant times k^(2p): use |cos(k theta)-cos(k phi)|<=min(2,Ck chord),
then min(2,t)<=2^(1-2p)t^(2p). The correlation weights decay only as
k^(-1-beta). Their product is summable only if 2p<beta. Our chosen
2p=(1-beta)/2 exceeds beta throughout beta<3-2sqrt(2), so this argument
cannot sum (FIXED) to prove the pair-density asymptotic. This pinpoints
the same cusp obstruction in a second, independent way.

### Check log

The source was re-read at Lemma 10, equations (20), (29)–(30), and
Theorem 1. The observable is the exact normalized circle density,
not a replacement of the pair-correlation function by an ad hoc test.

second_check.py verifies (RES) as an exact Laurent-polynomial identity
in exp(i theta), with symbolic beta and r. It also checks the generator
inequality at 33,800 angle pairs for eight beta values including 0.01,
1/3 from below, 0.49, 0.7 and 0.99, and checks density positivity on
1,001 angles at each chosen R. These are consistency checks; the proofs
are the pointwise generator inequality and the analytic positivity bound.
All results are saved in second_checks.json.

Contraction.lean checks just the algebraic generator inequality, with
cosine values abstracted to numbers satisfying the relevant bounds.
Its actual checker result is in contraction_lean_check.txt. The stopping
argument, Holder estimates, Markov/Duhamel argument and probability-valued
uniqueness are analytic proofs in this file, not claimed as Lean-checked.
The Lean command completed with exit code 0, using only Real.Basic,
Linarith and Ring imports. There is no sorry and no native_decide.
third_density_check.py verifies the third-density residual as a finite
Laurent-polynomial identity, its zero mass and degree bound, and the
imaginary parity of the third column. These results are in second_checks.json.

Potential failure points were checked individually:

* Same-noise differences retain quadratic variation; only their forcing
  cancels. Its variance is 2(1-cos(Delta)), not zero.
* The factor beta/2 in the sine drift is retained; forgetting it changes
  the contraction threshold and exponents.
* The fractional V is nonsmooth at coincidence; the stopping/Fatou proof
  explicitly handles this instead of applying global Ito to V.
* The correlation observable is only Holder beta. One cannot use the
  unconstrained optimum p=(1-beta)/4 when beta<1/3.
* The circle average of g_beta is 1 and the pair-density conversion is
  division by 4pi^2; this preserves the density-(2pi)^(-1) convention.
* The residual is an actual signed density of mass zero, not a list of
  formal moment errors whose summability was assumed.
* Duhamel is used on finite intervals away from the singular point r=0;
  the only invocation of r down to zero is the uniqueness comparison of
  already-existing probability families.
* Probability-valued uniqueness does not assert uniqueness for all
  bounded complex solutions of the hierarchy.
* The bound (THM) has kappa<2. Writing a candidate r^(-2) term on its
  left side does not turn it into a proved leading asymptotic term.

One possible further step would be to prove that P_{r/2,r}g_beta has a
uniform Lipschitz bound as r grows. Then one could couple over the earlier
interval using larger p, rather than retaining the observable's original
Holder exponent. This is not supplied by smoothness of the SDE flow:
composition with a smooth diffeomorphism preserves a cusp, and taking
expectations needs genuine regularization. The diffusion coefficient
vanishes at theta=0. Rapid positive forcing suggests a hypoelliptic
estimate, but a uniform bound in the large parameter has not been proved
here. Assuming it would leave precisely the missing step hidden.
