from pathlib import Path
p=Path('ATTEMPT.md')
s=p.read_text(encoding='utf-8-sig')
s+='''

## Proved special case: dimension-linear TV relaxation

**Theorem.** For every d>=1 let R have diagonal 1 and subdiagonal -1, let
Gamma=(R+R^T)/2, let U(x)=-exp(-x), and let mu_i<=-m for one fixed m>0.
The resulting GRBM has a unique stationary probability pi_d. There is a finite
W_d(x)>=1 for every x such that, for all t>=0,

    ||P_t(x,.)-pi_d||_TV <= W_d(x) exp(-c_m t/(4d)),
    c_m = min(m/4,m^2).

When m>=1, one may take the sharper exponent m/(4d).
W is allowed to depend on dimension and inputs, as in Conjecture 1.5.
No lower bound on mixing time, and no uniform control on W, is asserted.

### 1. Admissibility and invariant measure

Gamma has diagonal 1 and adjacent off-diagonal -1/2. For v_0=0,

    2 v^T Gamma v = sum_{i=1}^d (v_i-v_{i-1})^2 + v_d^2.

This is strictly positive for v!=0. Its norm is at most 2. U'=exp(-x) is smooth,
positive and decreasing everywhere, has the required two limits, and
U'(ay)/U'(by)=exp(-(a-b)y) tends to infinity for a>b>0 and y->-infinity.
The source's existence and recurrence conclusions therefore apply.

Let M_i=-sum_{j=1}^i mu_j>=im and a_i=2M_i. Define

    p_i(x)= [2^(a_i)/GammaFunction(a_i)] exp(-2exp(-x)-a_i x),
    p(x)=product_i p_i(x).

The normalizing constant follows on putting y=2exp(-x): y has the Gamma(a_i,1)
density. Every a_i>0, so p is a probability density. Set h_i=exp(-x_i)-M_i.
Because R M=-mu, b=mu+R(exp(-x_i))=Rh. Also grad log p=2h.
Write K=(R-R^T)/2, so R=Gamma+K. The stationary probability current is

    b p - (1/2)Gamma grad p = p K h.

Its divergence is zero: div(Kh)=sum_i K_ii partial_i h_i=0, since each h_i
only depends on x_i and K_ii=0; and (grad p)^T Kh=2p h^T Kh=0 by skew symmetry.
Thus integral Lf p dx=0 for every smooth compactly supported f.
The infinitesimal-invariance criterion for a well-posed conservative diffusion
martingale problem (Echeverria's criterion) then makes p dx invariant. The source's
uniqueness result identifies it with pi_d. This application uses a probability
measure, smooth coefficients, nonexplosion and uniqueness of the martingale
problem; all are available here. No product-form formula with an ambiguous
matrix transpose is assumed.

### 2. One-dimensional log-gamma Poincare inequality

For a>0 and beta>0, let rho_a(x) be the normalized density proportional to
exp(-V_a(x)), V_a(x)=a x+beta exp(-x). We prove

    Var_rho_a(f) <= k(a)^(-1) integral |f'|^2 rho_a dx,

where k(a)=a^2/4 for 0<a<=1, k(a)=a/8 for 1<a<2,
and k(a)=a-1 for a>=2. The constants in the middle regime are deliberately loose.

Here are the operator details of the proof. Multiplication by sqrt(rho_a)
is a unitary map from L2(rho_a) to L2(dx). Put
A_a=partial_x+V_a'/2, initially on C_c^infinity and then closed.
For u=f sqrt(rho_a), A_a u=f' sqrt(rho_a).
The kernel of A_a is the span of sqrt(rho_a): its first-order differential
equation has exactly these solutions. Orthogonality to this kernel is precisely
mean zero for f. With y=beta exp(-x), integration by parts gives

    H_a=A_a^* A_a=-partial_x^2+(a-y)^2/4-y/2,
    A_a A_a^*=-partial_x^2+(a-y)^2/4+y/2.

These identities extend from compactly supported functions to the nonnegative
self-adjoint operators. One may use the Friedrichs realizations: these smooth
Schrodinger potentials are bounded below and are limit-point at both ends on
the whole real line, so there is no boundary condition or extension ambiguity.
The three lower bounds for the partner operator are:

* a<=1: its potential is a^2/4 + (1-a)y/2 + y^2/4 >= a^2/4.
* 1<a<2: completing the square gives potential
  (y-(a-1))^2/4+(2a-1)/4 >= a/8, since a>=1.
* a>=2: the exact identity A_a A_a^*=H_(a-2)+(a-1) implies
  A_a A_a^*>=a-1. H_(a-2) is nonnegative as a factorization even when a=2,
  where its would-be ground state is not square integrable.

Consequently ||A_a^* v||^2>=k(a)||v||^2. The range of A_a^* is closed
and equals (ker A_a)^perp (the coercive bound gives closed range, and the
usual adjoint identity gives its closure). For u in Dom(A_a) perpendicular
to its kernel, write u=A_a^*v. Adjointness and Cauchy-Schwarz give

    ||u||^2 = <A_a u,v>
             <= ||A_a u|| ||v||
             <= ||A_a u|| ||u|| / sqrt(k(a)).

Dividing proves ||A_a u||^2>=k(a)||u||^2, as required. The inequality extends
to the weighted Sobolev domain by closure; subtracting the mean is legitimate
since the ground state belongs to Dom(A_a). This supplies the full Poincare
inequality, rather than just a formal polynomial identity.

For a_i>=2mi the bounds imply k(a_i)>=c_m i, c_m=min(m/4,m^2).
If a_i<=1, k=a_i^2/4>=m^2 i^2>=m^2 i. If 1<a_i<2, k=a_i/8>=mi/4.
If a_i>=2, k=a_i-1>=a_i/2>=mi. All three dominate c_m i.
If m>=1 every a_i>=2 and k(a_i)>=mi directly.

### 3. Tensorization and the chain estimate

For a product probability distribution, variance tensorization states
Var_pi(f)<=sum_i E_pi[Var_{p_i}(f | other coordinates)]. For completeness,
induct on the number of coordinates using
Var(f)=E[Var(f | first d-1 coordinates)]+Var(E[f | first d-1 coordinates]).
Apply the induction hypothesis to the conditional expectation, and use Jensen
in each other-coordinate conditional variance to bound its variance by the
conditional variance of f. This proves the displayed inequality; applying
section 2 in each coordinate yields

    Var_pi(f) <= (1/c_m) sum_i (1/i) E_pi[(partial_i f)^2].

For any v, Cauchy-Schwarz in v_i=sum_{k=1}^i(v_k-v_{k-1}) gives
v_i^2/i<=sum_{k=1}^i(v_k-v_{k-1})^2. On summing,

    sum_i v_i^2/i
       <= sum_k (d-k+1)(v_k-v_{k-1})^2
       <= d sum_k (v_k-v_{k-1})^2
       <= 2d v^T Gamma v.

Thus

    Var_pi(f) <= (2d/c_m) E_pi[grad f^T Gamma grad f].

For smooth compact f, invariance and L(f^2)=2f Lf+grad f^T Gamma grad f
imply -E_pi[f Lf]=(1/2)E_pi[grad f^T Gamma grad f]. The same energy
inequality extends to the semigroup domain by closure (or by the usual
localized diffusion energy identity). For centered g in L2(pi), the invariant
Markov diffusion semigroup therefore satisfies

    d/dt ||P_t g||_2^2
       = -E_pi[grad P_t g^T Gamma grad P_t g]
       <= -(c_m/(2d)) ||P_t g||_2^2.

Integration and square root give

    ||P_t g||_2 <= exp(-lambda_d t)||g||_2,
    lambda_d=c_m/(4d).

First prove this for regular functions and positive time, then approximate
arbitrary L2 functions using the invariant semigroup's L2 contraction.
No detailed balance is used: the skew current drops out of the energy.

### 4. From L2 decay to TV at every deterministic start

We use the standard interior parabolic L2 mean-value estimate for smooth
uniformly elliptic equations: for a solution of partial_s u=L u on a spatial
ball around x over a unit time interval, its squared value at the final
central point is bounded by a finite constant times the space-time integral
of u^2 over that cylinder. The estimate follows from the local parabolic
energy inequality and Moser iteration; its hypotheses require ellipticity
and bounded coefficients on a slightly larger compact cylinder, not global
bounds on the drift. The covariance here is strictly positive definite and
the drift is smooth, hence these hypotheses hold on every fixed ball.
Time homogeneity makes the constant independent of the time interval.

For |g|<=1 set u(s,y)=P_s g(y)-pi(g). It is a smooth solution for s>0;
Var_pi(g)<=1. Choose a fixed ball B centered at x. Since p is strictly
positive and continuous, inf_B p>0. For t>=2 the local estimate yields

    |P_t g(x)-pi(g)|^2
      <= A_x integral_{t-1}^t integral_B |P_s g(y)-pi(g)|^2 dy ds
      <= B_x integral_{t-1}^t ||P_s(g-pi(g))||_L2(pi)^2 ds
      <= B_x exp(-2lambda_d(t-1)).

A_x and B_x may depend on d and x, but are finite and independent of g and t.
For bounded measurable g the statement follows either directly from elliptic
smoothing or bounded approximation. Supremizing over |g|<=1 uses exactly the
source's TV norm (its maximal value for two probabilities is 2). Thus the
TV bound holds for t>=2 with prefactor sqrt(B_x) exp(lambda_d).
For 0<=t<2 use the bound 2. Taking

    W_d(x)=max(1, sqrt(B_x) exp(lambda_d), 2 exp(2lambda_d))

finishes the theorem. A locally finite measurable choice of constants B_x
can be made by bounding coefficients and inf p on balls around x; alternatively
use a countable covering of space and take one valid constant on each covered
smaller ball. This ensures that W is a genuine finite function on all of R^d.
Replacing c_m by m proves the sharper m>=1 version.

### 5. Hostile-referee audit and remaining gap

1. A Lyapunov constant is not a TV rate. The proof uses an invariant-measure
   Poincare inequality, semigroup energy, and a separate local PDE argument.
2. The density must match the *lower* bidiagonal generator. Direct stationary
   current cancellation verifies the prefix sums M_i. The source's formula
   (1.4) has a transpose/convention issue if applied literally to (1.11);
   no conclusion here relies on that formula.
3. An unweighted covariance bound would lose d^2. The weighted estimate
   sum v_i^2/i<=2d v^T Gamma v is proved explicitly, and checked numerically.
4. Large shape alone does not give a uniform Hessian bound: V'' tends to zero
   at +infinity. The factorization proof supplies the needed Poincare estimate.
5. Nonreversibility does not invalidate Poincare decay, because invariance
   and the diffusion product rule identify the symmetric energy exactly.
6. L2 decay alone does not control a delta start. Local parabolic mean-value
   estimates repair that step, and their constants are permitted in W.
7. These assumptions exclude Gamma=I for d>1 and exclude general U. Nothing
   here proves the source's full conjecture. No stationary density estimate
   or suitably weighted Poincare bound is established for those general inputs.
8. A common drift lower bound m is explicit. Without dimension-uniform input
   controls the source's phrase 'order 1/d' is ambiguous; for a single fixed d
   it is already vacuous, since any positive rate can be written C/d.
9. The free prefactor W means this is a rate bound, not a uniform mixing-time
   statement over x or a two-sided asymptotic assertion.

Remaining gap: establish a dimension-uniform global convergence rate at least
C/d for the whole Theorem 1.3 class, especially Gamma=I and general potentials
without product stationary distributions. Neither the earlier frozen-rate
argument nor these product-form energy estimates bridge that gap.
'''
p.write_text(s,encoding='utf8')
print('Saved complete special-case proof')
