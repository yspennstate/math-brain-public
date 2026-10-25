# P0177 - Location of the mode of classical and free Brownian motion at large time

Continuous-time stochastic processes, 13 September 2026.

## The problem and its source

Corpus id `P0177`, source `free_unimodality_journal_2018`, locator "Problem 4.6". The source is

> T. Hasebe and Y. Ueda, *Large time unimodality for classical and free Brownian motions with
> initial distributions*, ALEA Lat. Am. J. Probab. Math. Stat. **15** (2018), 353-374,
> arXiv:1710.08240.

Title, authors and journal reference checked against arXiv:1710.08240. Problem 4.6 reads:

> Estimate the position of the mode of classical Brownian motion with initial distributions
> satisfying the assumption (4.13). Our proof shows that for t >= (36/eps) log(2 alpha), the mode is
> located in the interval [-sqrt(t)/2, sqrt(t)/2]. How about free Brownian motion?

Assumption (4.13) is alpha := integral e^{eps x^2} dmu(x) < infinity for some eps > 0. So the
paper's own answer in the classical case is a window of width sqrt(t), and the free case is left
untouched.

Throughout mu is the initial law, with mean m and central moments mu_2, mu_3, ...; the classical
law is mu * N(0,t) and the free one is mu |+| S(0,t), where S(0,t) is the semicircle law of
variance t, density sqrt(4t - x^2)/(2 pi t). Both are unimodal for large t by the source's Theorems
3.2 and 4.3, so "the mode" is well defined.

## Result

**Theorem.** Let mu have compact support, mean m and central moments mu_k. For all large t,

    mode(mu * N(0,t))   = m - mu_3/(2t) + (mu_5 - 6 mu_2 mu_3)/(8 t^2) + O(t^-3),
    mode(mu |+| S(0,t)) = m - 3 mu_3/t  + (5 mu_5 - 22 mu_2 mu_3)/t^2  + O(t^-3),

and in both cases the mode is an analytic function of 1/t near 0.

The leading displacement of the free mode from the initial mean is exactly **six times** the
classical one, with the same sign, opposite to the sign of the third cumulant. Both are O(1/t),
far inside the source's window of width sqrt(t).

## Proof

### Free case

The engine is Biane's subordination description of mu |+| S(0,t) (P. Biane, *On the free
convolution with a semi-circular distribution*, Indiana Univ. Math. J. 46 (1997) 705-718). Write G
for the Cauchy transform of the free convolution. Subordination gives G(z) = G_mu(z - t G(z)). Put
z = x + i0, G(x) = a - ib with b = pi p_t(x) >= 0, and set

    xi = x - t a,    eta = t b.

Taking imaginary parts of G = G_mu(xi + i eta) and cancelling b gives, whenever b > 0,

    (B)   integral dmu(u) / ((xi-u)^2 + eta^2) = 1/t,
    (A')  a = integral (xi-u) dmu(u) / ((xi-u)^2 + eta^2),

so the density is parametrised by xi:

    eta = eta_t(xi), the unique positive root of (B),
    x_t(xi) = xi + t * integral (xi-u) dmu / ((xi-u)^2 + eta^2),
    p_t(x_t(xi)) = eta_t(xi) / (pi t),

and xi -> x_t(xi) is a homeomorphism onto the interior of the support.

Sanity check, done exactly: for mu = delta_0 this gives eta^2 = t - xi^2, x = 2 xi and density
sqrt(4t - x^2)/(2 pi t), the semicircle of variance t, as it must. Second, independent check:
integrating the density above against x^k for k <= 5 with mu a three-atom law at t = 3.7 reproduces
the moments predicted from free cumulants (kappa_n unchanged except kappa_2 -> kappa_2 + t) to nine
decimals.

So the mode sits at x_t(xi*) where xi* maximises eta_t. Differentiating (B) implicitly,
d eta / d xi = 0 exactly when

    (A)   integral (xi-u) dmu(u) / ((xi-u)^2 + eta^2)^2 = 0.

Now the expansion. Let tau = 1/t and s = 1/eta^2. With m_k(xi) = integral (xi-u)^k dmu(u),
equation (B) reads

    s * Phi(xi,s) = tau,     Phi(xi,s) = sum_{j>=0} (-1)^j m_{2j}(xi) s^j.

For mu supported in [-D,D] and |xi| <= 1 the series converges for s < (D+1)^{-2}, and Phi is jointly
analytic with Phi(xi,0) = 1. Since d/ds (s Phi) at s = 0 equals 1, the analytic implicit function
theorem gives an analytic s = S(xi,tau) with S(xi,0) = 0. Writing S = tau R(xi,tau),

    R(xi,tau) = 1 + m_2(xi) tau + (2 m_2(xi)^2 - m_4(xi)) tau^2 + O(tau^3),
    eta^2 = 1/S = t - m_2(xi) + (m_4 - m_2^2)/t + ...

Maximising eta is minimising R. Using m_2 = xi^2 + mu_2 and
m_4 = xi^4 + 6 xi^2 mu_2 - 4 xi mu_3 + mu_4 (taking m = 0 without loss),

    (d/dxi) R / tau = 2 xi + tau (4 xi^3 - 4 xi mu_2 + 4 mu_3) + O(tau^2).

The bracket vanishes at (xi,tau) = (0,0) with xi-derivative 2, so there is a unique analytic root
xi*(tau) with xi*(0) = 0; and the second xi-derivative of R is tau(2 + O(tau)) > 0, so it is a
strict local maximum of eta. By the source's Theorem 3.2 the density is unimodal once t >= 4 D^2,
so this local maximum is the mode. The threshold can be sharpened to t > D^2: corpus entry P0174
answers the same paper's Problem 3.3 with the optimal constant C = 1, so mu |+| S(0,t)
is unimodal for every t > D^2 and the expansion below is the expansion of a genuine unique mode
from that threshold on. Expanding,

    xi* = -2 mu_3 tau + (3 mu_5 - 14 mu_2 mu_3) tau^2 + O(tau^3).

Finally x* = xi* + t a with a = eta^{-2} [ m_1 - m_3/eta^2 + m_5/eta^4 - ... ], giving

    t a = -mu_3 tau + (2 mu_5 - 8 mu_2 mu_3) tau^2 + O(tau^3),
    x*  = -3 mu_3 tau + (5 mu_5 - 22 mu_2 mu_3) tau^2 + O(tau^3).                         QED

Note the split: two thirds of the free displacement comes from the mode of the subordinate parameter
xi, and one third from the subordination shift t a. That is why the free answer is not a rescaling
of the classical one.

### Classical case

Stationarity of the density is integral (x-u) exp(-(x-u)^2/(2t)) dmu(u) = 0, that is
sum_{j>=0} (-1)^j m_{2j+1}(x) / (j! (2t)^j) = 0. The same implicit-function argument (the series is
analytic in 1/t under compact support; under the source's assumption (4.13) it is an asymptotic
expansion valid to any fixed order, since the exponential-quadratic moment gives all moments) yields

    x* = m_3(x*)/(2t) - m_5(x*)/(8 t^2) + ...
       = -mu_3/(2t) + (mu_5 - 6 mu_2 mu_3)/(8 t^2) + O(t^-3).

An equivalent and more transparent derivation: stationarity says x is the mean of the tilted measure
dmu_{x,t}(u) proportional to exp((x u - u^2/2)/t) dmu(u); expanding the tilt in 1/t is the same
computation. The first-order term agrees with the partial answer recorded in the ledger for P0177
(attempt A001).

## Numerical verification

Checked to high precision, and for the general formulas rather than one instance, on four atomic
measures with quite different moment vectors - including one with mu_3 = 0.043 so that the
second-order term dominates. Root-finding on the stationarity equations at 60-digit precision,
t = 10^4 ... 10^10.

Classical:

| mu | predicted c1 | measured t x* | predicted c2 | measured t^2 (x* - c1/t) |
|---|---|---|---|---|
| (2/3,1/3) at -1,2 | -1 | -1.0000000000 | -1.75 | -1.75 |
| 0,1,5 weights 5,3,1 | -3.6652949 | -3.665294924 | 3.5111687 | 3.5111687 |
| -2,0.5,3 weights 1,6,2 | -0.021433471 | -0.02143347059 | -0.85626384 | -0.85626384 |
| -3,-1,0,4 weights 2,3,4,1 | -3 | -2.999999999 | 5.1 | 5.1 |

Free:

| mu | predicted c1 | measured t x* | predicted c2 | measured t^2 (x* - c1/t) |
|---|---|---|---|---|
| (2/3,1/3) at -1,2 | -6 | -6.000000004 | -38 | -38.0 |
| 0,1,5 weights 5,3,1 | -21.99177 | -21.99176952 | 276.56042 | 276.56042 |
| -2,0.5,3 weights 1,6,2 | -0.12860082 | -0.1286008264 | -33.562566 | -33.562566 |
| -3,-1,0,4 weights 2,3,4,1 | -18 | -17.99999996 | 369.6 | 369.6 |

Auxiliary quantities came out right too: eta^2 - t -> -mu_2 and t xi* -> -2 mu_3 in every case.


## Relation to other results on the same paper

Two other results bear on this:

- Corpus entry P0174 answers Problem 3.3 of the
  same paper: the optimal constant is C = 1, so mu |+| S(0,t) is unimodal for t > D^2. That is what
  makes "the mode" well defined in the range used above, and it improves the threshold of
  their Theorem 3.2.
- A separate result gives a sharp bound on p_t''(m_t), the CURVATURE at
  the mode, for t > D^2. It says how peaked the density is at the mode; the result here says where the mode
  is. The two are complementary, and neither implies the other.

That curvature result uses the same object, F_R(u) = int dmu(x)/((x-u)^2 + R^2) with
the level 1/t, and the same distinction between the subordinate coordinate u and the physical
coordinate (their Jacobian psi'(u) = 2v^2/(a+v^2)), reached for a different question.

## Trying to break it

The one external input the free computation rests on is Biane's density formula. A wrong
normalisation of the semicircle parameter would make every free number wrong by a fixed factor, and
the numerics - which use the same formula - would not catch it. Two independent checks were run for
exactly that reason: mu = delta_0 reproduces the semicircle of variance t exactly, and the first six
moments of the numerically integrated density match the free-cumulant prediction to 1e-9 at t = 3.7.
Both pass, so the parametrisation is the right one.

Second worry: is the stationary point the global mode? For general mu, eta_t could have several
local maxima. This is what unimodality for large t rules out, and unimodality is the source's own
theorem (Thm 3.2, compact support, t >= 4 D^2). For small t the statement is false in general - the
density can be bimodal - so "for large t" is not decoration.

Third worry: compact support. The free half is stated for compactly supported mu because that is
where both the analyticity and the unimodality theorem are available. Under only assumption (4.13)
the argument still gives the expansion to any fixed order provided the corresponding moments are
finite, but convergence of the 1/t series is not claimed.

## Status

- The two asymptotic expansions: **proved** (compact support; the classical one also under (4.13)
  as an asymptotic expansion to fixed order), and confirmed numerically on four measures.
- The factor 6 between free and classical leading displacements: **proved**. It is a structural
  constant, not a coincidence: both displacements are governed by the third cumulant, and the free
  case picks up an extra contribution from the subordination shift.

## Literature check

Searches run 2026-09-13: "free unimodality Problem 4.6 mode free Brownian motion", "Hasebe Ueda mode
free convolution semicircle unimodal", "Biane free Brownian motion density subordination mode",
"mode of free Brownian motion with initial distribution asymptotic location semicircle free
convolution", plus a citation sweep of arXiv:1710.08240. Nothing found that locates the mode of
mu |+| S(0,t). The nearest follow-up is Hasebe-Ueda-Wang (2022) on log-unimodality of free positive
multiplicative Brownian motion, a different question. The companion Problem 3.3 of the same paper
(the optimal C with 2 <= C <= 4 such that mu |+| S(0,t) is unimodal for t >= C D^2) has no published
answer; corpus entry P0174 records C = 1.

Hasebe and Ueda asked the free question explicitly and left it, and nothing since answers it, so the
free expansion looks new. The derivation is short enough that it could exist as folklore in the free-probability community.

## Remaining obligation

1. Drop compact support: prove the free expansion under the exponential-quadratic moment assumption,
   which needs Biane's parametrisation plus a tail estimate giving eta^2 = t - m_2(xi) + O(1/t)
   uniformly on the relevant xi range.
2. A uniform error constant in the classical case, which is what the source literally asks for: the
   expansion gives the location, but an explicit bound |mode(t) - m + mu_3/(2t)| <= C(alpha,eps)/t^2
   with C written out in terms of alpha and eps is still owed.
