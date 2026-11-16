# F0073 attempt: the 2D field pinned at the origin and kept positive, uniformly convex V

agent A, 16 Nov 2026. Status: PROVISIONAL. Lower half proved modulo the exact statement of [DG00];
upper half (and with it existence of the infinite-volume measure) open. Not a solution.

Problem (Velenik, Probab. Surveys 2006, Open Problem 6, Sec. 3.3, display (21)): for d = 2 and V even with
c_- <= V'' <= c_+, show E^+_{Z^2\{0}}(phi_i) is of order log|i|, as is known for V(x) = x^2/2.

## Setup
Lambda_N = [-N,N]^2, D_N = Lambda_N \ {0}. mu_N: density prop. to exp(-sum_{x~y} V(phi_x - phi_y)) on R^{D_N},
phi = 0 at the origin and outside Lambda_N. Omega^+_N = {phi_x >= 0 for x in D_N}. mu^+_N = mu_N( . | Omega^+_N),
m_N(i) = E_{mu^+_N}(phi_i). FKG holds for mu_N and for mu^+_N (convex V gives the lattice condition; the
positivity set is a product sublattice), with monotonicity in boundary values.

## 1. The limit exists in [0, infinity] (proved)
D_N is inside D_{N+1}. Given phi outside D_N, mu^+_{N+1} restricted to D_N is mu_{D_N}^h( . | Omega^+) with h >= 0
on the outer boundary and h = 0 at the origin. FKG: it dominates mu^+_N. So mu^+_N increases in N and
m_N(i) increases to a limit m(i) in [0, infinity].

## 2. Variance bound uniform in N (proved)
mu^+_N is log-concave with Hess >= c_- (-Delta_{D_N}) (approximate the indicator by the convex penalties
k sum (phi_x^-)^2). Brascamp-Lieb: Var_{mu^+_N}(phi_i) <= c_-^{-1} G_{D_N}(i,i) <= c_-^{-1} G_{Z^2\{0}}(i,i), which is
of order log|i| (random walk killed at the origin; potential kernel). Bakry-Emery for convex restrictions gives
Gaussian concentration of phi_i at that scale. Consequence: the increasing family is tight iff sup_N m_N(i) < inf,
so EXISTENCE of the infinite-volume measure is EQUIVALENT to the upper bound being finite (one site suffices
by FKG and finite-energy comparison with a neighbour).

## 3. Lower bound m(i) >= c log|i| (proved, modulo [DG00])
Let r = |i| and B the box of side r/2 centred at i; B misses the origin and sits inside Lambda_N for N >= 2r.
Given phi outside B, mu^+_N restricted to B is mu_B^h( . | phi >= 0 on B) with h >= 0. FKG: it dominates
mu_B^0( . | Omega^+(B)), zero boundary outside B, positivity on all of B. That is the M = N case of
Deuschel-Giacomin, Entropic repulsion for massless fields, SPA 89 (2000) 333-354 [DG00]: strictly convex
even V, d = 2, height of order log(side) in the bulk (abstract; Velenik p. 133 states the M = N case and the
growth log L at distance L from the boundary, without matching constants). Since phi >= 0, a bulk
in-probability lower bound gives E >= c log r. Hence m_N(i) >= c log|i| for N >= 2|i|, and m(i) >= c log|i|.
To close: read DG00's d = 2 theorem itself (paywalled, ScienceDirect pii S0304-4149(00)00030-2) and check
the site range (centre of the box is enough) and the form (in probability or in expectation).

## 4. Upper bound sup_N m_N(i) <= C log|i| (OPEN: this is the content of the problem)
The pin is what keeps the field low: without it the box field sits at height ~ log N. Gaussian route: DLR on
B_R, FKG raise the boundary to M = max over the boundary of B_R (about log R), then shift by
u(x) = M a(x)/a(R), harmonic with u(0) = 0, u = M on the boundary of B_R; the shifted field is a zero-boundary field
conditioned on psi >= -u, which is dominated by psi >= 0; at |x| = r, u = O(M log r / log R) = O(log r).
For convex V the shift is not a symmetry. Its replacement (synchronous Langevin coupling, Helffer-Sjostrand):
d/dM E^M(phi_i) = annealed probability that the dynamic random walk with conductances V''(grad phi_t),
started at i, leaves B_R before hitting the origin. The upper bound needs this escape probability to be
<= C log r / log R, exponent exactly 1. The Delmotte-Deuschel heat-kernel bounds give only a lower bound on the
hitting probability by scale and hence (log r / log R)^gamma with an unknown gamma <= 1, which with M ~ log R
leaves (log R)^(1-gamma) and diverges. In the static case electrical resistance gives exponent 1; the dynamic
environment does not obviously allow that. Wu's local CLT (arXiv 2202.13578) controls phi(0) in an unpinned box
only within +-sqrt(log N), not in the repelled regime, so it does not close this directly.
Useful identity (proved, integration by parts at the wall): E_{mu^+_N}[ sum_{y~x} V'(phi_x - phi_y) ] = rho_x(0) >= 0,
rho_x the density of phi_x at 0. With Gaussian concentration (sec. 2), rho_x(0) <= (2/m) exp(-m^2 / (8 s^2))
whenever m >= K s (K absolute; split on whether the log-concave marginal's mode is above m/2),
m = m_N(x), s^2 = G(x,x)/c_-. For V Gaussian this makes m superharmonic with a polynomially small source once
m(x) >= A log|x|; for general V the identity is nonlinear in phi.

## Correction to F0073-A001 (8 Sep 2026)
A001 says the upper half follows by domination and "only the lower bound is at issue". This is reversed: the
comparison with a box of scale |i| bounds the infinite-volume mean from BELOW, not above. The lower half is the
easy one (sec. 3); the upper half, uniform in N, is open.

Sources: Velenik math/0509695 pp. 133-134; Deuschel-Giacomin SPA 89 (2000) abstract (RePEc); Wu arXiv 2202.13578
abstract; Schweiger-Wu-Zeitouni arXiv 2403.11500 (maximum of 2D GL fields, uniformly convex V) as a likely
toolkit for the multiscale part. The Gaussian proof is Giacomin, IHP notes 2001, Lemma 4.4 (not obtained).
