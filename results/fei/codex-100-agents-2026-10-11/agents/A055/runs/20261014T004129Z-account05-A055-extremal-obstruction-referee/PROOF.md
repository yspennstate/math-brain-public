# Singleton phase error with the complete child reserve

Uniform finite cubes; Boolean signs; all entropies are bits. Fix a coordinate i.
Pair the real Fourier coefficients a_t=fhat(t), b_t=fhat(t+i) for t not containing i.
Omit zero rows, put q_t=a_t^2+b_t^2, e_t=min(a_t^2,b_t^2)/q_t,
c_t=4e_t(1-e_t), beta=sum q_t e_t, C_i=sum q_t c_t,
and O_i=Inf_i-beta>=0. The physical row is w_t(x)=a_t+x b_t.
The Boolean phase sign(w_t) is constant or a character. At equality |a_t|=|b_t|
one physical value vanishes; either convention sign(0)=1 is allowed. This does
not affect e_t or the formulas below; no deterministic-phase admission is used
at a tie.

## Exact identities and the quadratic improvement

The conditional spectral pair probabilities are (a_t^2,b_t^2)/q_t, so
B_i=sum q_t h2(e_t). Its row collision is
E w_t^4/q_t^2-1=4a_t^2 b_t^2/q_t^2=c_t. In particular
2 beta<=C_i<=4 beta. The actual row information transfer is
j(c_t), where

    j(c)=((1+sqrt(c))log2(1+sqrt(c))
         +(1-sqrt(c))log2(1-sqrt(c)))/2.

Thus J_i=sum q_t j(c_t), L_i=B_i+J_i. The sign of a_t b_t only
interchanges the two physical assignments and is retained before the square.
The expansion j(c)=(1/ln2)sum_{k>=1} c^k/[2k(2k-1)] has nonnegative
coefficients and j(1)=1, so j(c)<=c on [0,1]. Concavity of h2, sum q=1,
beta<=C_i/2<=1/2 give the dimension-free bound

    L_i <= h2(beta)+J_i <= h2(C_i/2)+C_i.             (1)

The exact spectral minority mass is order c, not sqrt(c):
e=(1-sqrt(1-c))/2 belongs to [c/4,c/2]. Formula (1) is O(C log(1/C))
as C approaches zero, improving the generic block phase-continuity error
O(sqrt(C) log(1/C)) for singleton cuts. At C=0 both B_i and J_i vanish.
This is an error estimate, not a new uniformly paid coordinate rule.
The squared Fourier law of a singleton Boolean phase is a point mass; its
TV distance from the row spectral law is exactly e, including a tied row.
Thus the actual singleton phase TV improves to at most c/2, as well as the
entropy estimate improving. This assertion does not extend to arbitrary blocks.

For completeness a self-contained sharper recentring bound is J_i<=kappa beta,
kappa=2/ln2. Set z=2sqrt(e(1-e)). The even-series comparison
sum_{k>=1} z^(2k)/[2k(2k-1)]<=1-sqrt(1-z^2) follows because the coefficient
of z^(2k) on the right is binom(2k,k)/(4^k(2k-1)), and
binom(2k,k)/4^k>=1/(2k). The latter holds at k=1 and induction multiplies
by (2k+1)/(2k+2), which is at least k/(k+1).
Since e<=1/2, 1-sqrt(1-z^2)=2e. This proves the bound including endpoints.

## Necessary critical-witness reserve, with no terminal discard

Assume K>=0 and f is a least-essential-dimension violation of FEI(K).
Every proper physical child satisfies D_K<=0. Define the actual child reserve
S_i=-[D_K(f_+)+D_K(f_-)]/2>=0 and D=D_K(f)>0.
The exact physical restriction identity gives

    D + K O_i + S_i
      = sum_t q_t [h2(e_t)+j(c_t)-K e_t]
      <= h2(beta)-(K-kappa)beta
      <= log2(1+2^(kappa-K)).                         (2)

The last step is a scalar Legendre identity: for any real t,
sup_{0<=x<=1} [h2(x)-t x]=log2(1+2^-t), with maximizer
x=1/(1+2^t). We maximize over a larger interval than beta in [0,1/2],
so (2) remains valid for K<kappa. For K>=kappa the maximizer is admissible.
Consequently a least-dimensional high-K witness has exponentially small root
deficit, every averaged child reserve, and (for K>0) K times its excess
orientation energy O_i. Since log2(1+u)<=u/ln2,

    D+K O_i+S_i <= 2^(kappa-K)/ln2.                  (3)

For rational log certificates, kappa<3 follows from
ln2=2 sum_{j>=0} (1/3)^(2j+1)/(2j+1)>2/3. Hence replacing the right side
of (2) by log2(1+2^(3-K)) is a rigorously weaker bound; the finite helper
tests this version at integer thresholds 2,4,8,16, without approximating
the transcendental exponent kappa. The sharper bound (2) is analytic.

All physical child entropy and influence remain in S_i. The same algebra
without the sign condition S_i>=0 holds for any f; imposing that sign on an
arbitrary activated hard core is precisely the invalid embedding step.
Also (1) supplies the independent exact necessary condition
D+K Inf_i+S_i<=h2(C_i/2)+C_i on a critical witness.

## Independent reconstruction of A052's phase exclusion

For any proper block A, an isospectral family of physical children has rows
w_t(x)^2=q_t. Their phases h_t=w_t/sqrt(q_t) are Boolean on |A|<n variables.
Walsh Parseval yields B_A=sum q_t H(h_t), I_A=sum q_t I(h_t).
Least essential dimension gives H(h_t)<=K I(h_t), while actual children give
E D_K(child)<=0. Then D_K(f)=B_A-K I_A+E D_K(child)<=0, contradiction.
For approximate rows, Fourier-law TV is at most their normalized L2 phase
error; maximal coupling bounds entropy by psi_|A|(error), and influence by
|A| error. Weighted concavity gives A052's stated Gamma+psi+K|A|error bound.
The proof works even when phases are not physical descendants because all
lower-dimensional Boolean functions are admitted. At zero physical rows,
sign(0)=1 is harmless for that approximate bound. The quadratic tensor
counterexample prevents weakening minimality to nonstrict ratio criticality.
Verdict: A052-CRITICAL-BOOLEAN-PHASE-EXCLUSION@1 HOLDS at its full analytic scope;
its bundled finite assertion count is not accepted merely from this review.

## First unsupported line

A uniform threshold and a proper block whose paid signed collision/phase
budget contradicts the positive witness deficit remain unproved. Equations
(2)--(3) do not contradict D>0: no dimension-independent positive lower bound
on D or S_i is available. Boolean dyadic Fourier granularity deteriorates with
dimension and does not provide that bound. This stage narrows the critical
source rather than asserts FEI, a new critical embedding, or a universal K.
