# Second serious attempt at C0109 — 2026-10-11

Status: a new unconditional truncation stability bound is proved below.
The optimal circular-law exponent is NOT determined.
The two new approaches are recorded in SECOND_APPROACHES.md. This file
pursues singular-value comparison and identifies its exact remaining gap.

## 1. Definitions and uniform published input

For an n-by-n complex matrix A, let mu_A be its empirical eigenvalue
measure and define, almost everywhere in z,

    U_A(z)=(1/n)log|det(A-zI)|
          =(1/n)sum_i log|z-lambda_i(A)|.

This is the positive-sign potential; distributionally Delta U_A=2pi mu_A.
We use planar Lebesgue measure, and K denotes a fixed radius, not a
spectral truncation. Write Omega={|z|<=K} and m_K=pi K^2.

Published input: Tao–Vu, Random matrices: The circular law,
arXiv:0708.2895v5, Theorem 2.5 on p.8, with Definition 2.2 on pp.6–7
and Lemma 2.4 on p.7. For ANY prescribed failure power Q and deterministic
shift norm bound n^C, it gives an inverse-norm bound n^B with failure
<=C' n^-Q, uniformly over entry laws with one fixed controlled-second-
moment constant. B,C' depend only on Q,C, and that constant.
Theorem 2.5 does NOT require centered entries or higher moments.

For clarity, kappa-controlled means E|X|^2<=kappa and

 E[Re(w X-v)^2 1{|X|<=kappa}] >= (Re w)^2/kappa

for all complex w,v. Lemma 2.4 says a finite positive-variance law has
this property after a fixed phase rotation. These statements are checked
in the downloaded PDF, not inferred from a brain card.

## 2. Raw truncation preserves the uniform input

Let X have mean zero and E|X|^2=1. Rotate X by the fixed phase from
Lemma 2.4 temporarily. For R>=kappa put X_R=X 1{|X|<=R}.
Then E|X_R|^2<=kappa, and its controlled-moment lower inequality holds
with the SAME kappa. Indeed, on {|X|<=kappa} it equals X, that event is
contained in {|X_R|<=kappa}, and the contribution from its complement is
nonnegative. This proves the inequality for all w,v without having to
estimate a difference of covariance matrices.

Undoing the rotation changes only phases of the deterministic shifts and
preserves every singular value. Thus the published theorem applies
uniformly to the raw laws X_R for ALL R>=kappa, even when R varies with n.
This is a genuine uniform statement, unlike the first attempt's
all-moments circular-law rate, whose thresholds depended on the past law.

## 3. Deterministic rank bound for clipped singular logarithms

Let rank(A-B)<=r and let s_i(A),s_i(B) be singular values in descending
order. For i<=n-r,

    s_{i+r}(A)<=s_i(B),  s_{i+r}(B)<=s_i(A).

Proof: by the variational characterization, there is a subspace of
dimension n-i+1 on which ||Bx||<=s_i(B)||x||. Intersect it with
ker(A-B), whose codimension is at most r. The resulting dimension is
at least n-i-r+1, and A=B there. The variational characterization for
A now proves the first inequality; exchange A and B for the second.
The characterization itself follows from diagonalizing B*B: the span
of the n-i+1 right singular vectors belonging to the smallest values
gives the upper inequality; every subspace of that dimension intersects
the span of the i largest right singular vectors nontrivially, giving
the lower inequality. This also covers repeated and zero singular values.

For every u>=0 the proportions of singular values >u consequently
differ by at most r/n: if B has k values >u, A has at least k-r,
and conversely. Define, for 0<m<L,

    g(s)=log m + integral_m^L 1{s>u} du/u.

It is the logarithm clipped to [log m,log L]. Summing this representation
gives

 |(1/n)sum_i g(s_i(A))-(1/n)sum_i g(s_i(B))|
       <=(r/n)log(L/m).                                      (RANK)

In particular if all singular values of A and B lie in [m,L], this
bounds the difference of their normalized log determinants. This is
NOT a direct rank inequality for eigenvalue discrepancy. No such
inequality is asserted.

## 4. A deterministic L2 bound that needs only a second entry moment

Let e_A=||A||_F^2/n. The Schur triangularization gives
(1/n)sum_i |lambda_i(A)|^2<=e_A, since its diagonal consists of the
eigenvalues and the Frobenius norm is unchanged by a unitary conjugation.

Use log_+(x)=max(log x,0) and log_-(x)=max(-log x,0).
The negative part of U_A is bounded by (1/n)sum_i log_-|z-lambda_i|.
For each complex lambda,

 integral_C (log_-|z-lambda|)^2 dz
   =2pi integral_0^1 r(log r)^2 dr=pi/2.

To check the last integral, substitute r=exp(-t): it is
2pi integral_0^infinity t^2 exp(-2t)dt=pi/2, using two integrations
by parts. Minkowski therefore bounds ||(U_A)_-||_L2(Omega)
by sqrt(pi/2), regardless of n or the eigenvalues.

The positive part satisfies, at |z|<=K,

 (U_A)_+(z) <=(1/n)sum_i log_+|z-lambda_i|
 <=(1/(2n))sum_i log(1+|z-lambda_i|^2)
 <=(1/2)log(1+(1/n)sum_i |z-lambda_i|^2)
 <=(1/2)log(1+2K^2+2e_A).

The middle inequality is Jensen for the concave logarithm. Since
log(1+x)<=2sqrt(x) for x>=0 (integrate 1/(1+t)<=t^-1/2), we have
log^2(1+x)<=4x. Hence the positive part's squared L2 norm is at most
m_K(2K^2+2e_A). Because positive and negative parts have disjoint
supports,

    ||U_A||_L2(Omega)^2 <= pi/2 + m_K(2K^2+2e_A).             (L2)

Every term is locally integrable even at eigenvalues; those points have
area zero. Consequently, for random matrices with E e_A<=1,
E||U_A||_L2(Omega)^2 is bounded by a constant depending ONLY on K.
No E|X|^4 and no deterministic operator-norm bound is required.

## 5. Unconditional expected L1 truncation transfer theorem

Let X be centered with unit variance and finite second moment. Make an
n-by-n iid matrix N with entries X and couple its raw truncation N_R
entrywise. Let J be the all-ones matrix, mu_R=E X_R, and put

    A=N/sqrt(n), B=(N_R-mu_R J)/sqrt(n), q_R=P(|X|>R).

For every fixed K,D>0 there are constants C and R_0, depending on X,K,D,
such that, for all sufficiently large n and all R>=R_0,

 E||U_A-U_B||_L1(Omega)
      <= C[(n q_R+1/n) log n + n^-D].                         (TRANSFER)

Proof, including its exceptional-set handling:

(a) The coupled difference A-B is a matrix supported on the changed
entries plus mu_R J/sqrt(n). If T is their number then its rank is
at most T+1 (and at most n). A matrix with T nonzero entries is a sum
of T rank-one coordinate matrices. Thus

    E rank(A-B)/n <= E(T+1)/n = n q_R+1/n.

(b) Apply Theorem 2.5 to N-sqrt(n)zI and to
N_R-mu_R J-sqrt(n)zI. We have |mu_R|<=E|X_R|<=1, and the deterministic
shift norm is <=n+Ksqrt(n)<=n^2 for all sufficiently large n.
Section 2 supplies a common controlled-moment constant. For ANY Q>0
there exist common B_0,C_0 such that, uniformly in z in Omega and R>=R_0,
both matrices A-zI and B-zI have smallest singular value at least
n^(-B_0) except with probability <=C_0 n^-Q. The normalization adds
1/2 to the exponent of the bound for the raw matrices, which is absorbed
in B_0. No simultaneous pointwise event in all z is being claimed.

(c) E||A||_F^2=n and E||B||_F^2=n Var(X_R)<=n.
Thus ||A-zI||<=||A||_F+K, and Markov's inequality gives, with L_0
large enough, a common upper singular-value bound n^L_0 with failure
<=C_0 n^-Q, uniformly in z,R. For example any L_0>(Q+1)/2 suffices
after absorbing K and constants and enlarging the threshold in n.

(d) For each sample let E_bad be the set of z in Omega where at least
one bound in (b),(c) fails. Fubini gives

    E area(E_bad)<=C_1 m_K n^-Q.

On its complement, (RANK) applied to A-zI, B-zI gives
|U_A-U_B|<=(rank(A-B)/n)(B_0+L_0)log n. The shift does not change rank.
The expected integral over that complement is therefore
<=m_K(B_0+L_0)(n q_R+1/n)log n.

(e) On the bad set use Cauchy–Schwarz in the PRODUCT space consisting
of sample probability and planar area:

 E integral_E_bad |U_A-U_B|
 <=[E integral_Omega |U_A-U_B|^2]^(1/2)
   [E area(E_bad)]^(1/2)
 <=C_2 n^(-Q/2).

The first factor is bounded using (L2) and E e_A,E e_B<=1. It need
not be independent of the second factor. Taking Q=2D completes the
proof. This pays the small-singular-value error WITHOUT a bulk count
estimate, by using the rank comparison itself down to a polynomial cutoff.

## 6. Smooth eigenvalue-statistic corollary and moment dependence

For f in C_c^2(C) supported in Omega, distributional integration by
parts gives exactly

    integral f d(mu_A-mu_B)=(1/(2pi))integral Delta f (U_A-U_B) dz.

For completeness, Delta log|z-lambda|=2pi delta_lambda: integrate by
parts outside a radius-h disk around lambda, note the outward normal
for its inner boundary, and let h->0. The normal derivative term
converges to 2pi f(lambda); the term involving h log h converges to
zero. Summation over the eigenvalues proves the identity.
Taking absolute values and expectations in (TRANSFER) gives

 E|integral f d(mu_A-mu_B)|
  <= C ||Delta f||_infinity [(n q_R+1/n)log n+n^-D].            (SMOOTH)

Now suppose M=E|X|^(2+eps)<infinity. Put p=2+eps and
tau_R=E[|X|^2 1{|X|>R}]. Then q_R<=M R^-p, tau_R<=M R^-eps,
and, since E X=0,

 |mu_R|^2=|E X1{|X|>R}|^2<=q_R tau_R<=tau_R.

Let sigma_R^2=Var(X_R)=1-tau_R-|mu_R|^2. For R sufficiently large
sigma_R>0, and 1-sigma_R<=1-sigma_R^2<=2M R^-eps.
Define the normalized truncated matrix B_hat=B/sigma_R, whose iid
entries have mean zero and variance one.

For ANY globally Lipschitz f, scaling the eigenvalues gives

 E|integral f d(mu_B-mu_B_hat)|
 <=Lip(f)(1/sigma_R-1) E[(1/n)sum_i |lambda_i(B)|]
 <=Lip(f)(1/sigma_R-1) [E||B||_F^2/n]^(1/2)
 =Lip(f)(1-sigma_R)<=2Lip(f)M R^-eps.

Combining this with (SMOOTH) proves the unconditional finite-moment bound

 E|integral f d(mu_A-mu_B_hat)|
 <=C||Delta f||_infinity[(n M R^-p+1/n)log n+n^-D]
   +2Lip(f)M R^-eps.                                        (NORMALIZED)

At R=sqrt(n), for fixed f and eps this is
O_{X,f}(n^-eps/2 log n+n^-1 log n). This is a comparison of TWO empirical
measures, not a bound on their circular-law discrepancy. It is a proved
reduction under exactly the weak-moment hypothesis.

## 7. Why this does not close C0109

The normalized truncated law depends on n. Its kth moments are generally
not bounded uniformly for k>p, and its entry bound is O(R), not an
n-independent constant. The all-moments theorem used in the FIRST attempt
therefore cannot be inserted with its fixed-law threshold. Theorem 2.5
is different: its quantifiers explicitly ARE uniform in a controlled-
second-moment constant; that is why it could be used above.

Suppose (as an additional UNPROVED input) that the normalized truncated
matrices have a circular-law smooth-statistic rate O(n^-gamma(a)) at
R=n^a. The triangle inequality and (NORMALIZED) would then give exponent
min(gamma(a),ap-1,a eps,1), up to logarithms, whenever ap>1.
For a<1/2, ap-1<a eps, so the rank term governs the moment-dependent
part; choosing a arbitrarily close to 1/2 would approach eps/2. This
optimization is a conditional consequence, not a rate theorem.

Even a fixed-smooth-test rate does not automatically give the uniform
rectangle rate in the source. Smooth rectangles have derivatives growing
as the smoothing width shrinks. A simultaneous bound and its derivative
cost must be proved and optimized, together with tightness outside the
compact disk. The precise unproved input is now isolated: a UNIFORM
quantitative circular law for the n-dependent normalized truncations,
with explicit growth of high moments/bounds, followed by a full-domain
rectangle smoothing estimate. None is supplied by the cached papers.

## 8. Hostile-referee audit

- The rank used is rank(A-B), NOT rank of A*A-B*B or eigenvalue rank.
- The lower singular-value theorem handles raw truncations. Their
  preservation of controlled moments is exact, not a continuity assertion.
- Centering changes rank by at most one and is included in the deterministic
  shift norm n+Ksqrt(n); its operator norm is NOT just |mu_R|.
- The normalized inverse bound includes the sqrt(n) factor.
- The bad-set bound is an expectation of area; no invalid union over
  uncountably many z, nor pointwise uniform event, occurs.
- Cauchy–Schwarz is in the joint space and does not require independence.
- The L2 argument uses log^2 growth and eigenvalue negative logarithms;
  replacing it with an energy-squared bound would erroneously need fourth
  moments. The bound remains valid for heavy tails and discrete laws.
- Scaling to variance one is handled on eigenvalues and needs only the
  second moment, via Schur and Cauchy–Schwarz.
- A theorem on the DIFFERENCE of two ESDs is not called a circular-law
  rate. Neither the smooth-test conclusion nor the n-dependent law gap
  is hidden in the final verdict.

Formal/numerical checks concern only auxiliaries; the complete stochastic
proof remains conventional mathematics relying on the specified published
least-singular-value theorem.
