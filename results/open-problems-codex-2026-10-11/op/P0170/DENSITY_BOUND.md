# P0170 — a further conditional bound for all polynomial thresholds

Date: 2026-10-12. A proved special case with an additional density hypothesis, not a solution or a novelty claim.

**Theorem.** Let k>=2, let gamma_n be product standard Gaussian measure, and suppose nu is an exact k-wise Gaussian law in R^n. Assume in addition that nu has density r with respect to gamma_n and B=||r-1||_(L2(gamma_n))<infinity. For every polynomial p of degree at most d,

    |nu{p>=0}-gamma_n{p>=0}| <= min(1, B sqrt(d) k^(-1/4)).

Thus k>=max(2,B^4 d^2/epsilon^4) suffices under this added hypothesis. If r<=M almost everywhere, one may take B<=sqrt(M-1). There is no uniform B assumption in P0170.

## Full proof

### A. Gaussian noise disagreement from a circle root count

Let Z,W be independent standard Gaussian vectors and put Z_theta=cos(theta)Z+sin(theta)W for 0<=theta<=pi/2. Set f=1_{p>=0}. We show

    P(f(Z)!=f(Z_theta)) <= d theta/pi.                       (1)

For fixed z,w the function g(phi)=p(cos(phi)z+sin(phi)w) is a real trigonometric polynomial of degree at most d. If it is identically zero, the event indicator is constantly 1 and contributes no disagreements. Otherwise it has at most 2d zeros on the circle: substitute u=exp(i phi), use cos(phi)=(u+u^-1)/2 and sin(phi)=(u-u^-1)/(2i), and multiply the resulting Laurent polynomial by u^d. It is a nonzero ordinary complex polynomial of degree at most 2d, so has at most 2d distinct roots. Multiplication by u^d adds no roots on the circle.

Away from endpoints at zeros, a disagreement between the indicator at phi and phi+theta requires at least one zero in that circular arc, by continuity and the intermediate value theorem. A fixed zero can be contained in such arcs for a set of starting angles of Lebesgue measure theta. The union bound therefore gives disagreement on a set of starting angles of measure at most 2d theta, among a total measure 2pi. Endpoint zeros have measure zero. This bound also holds for the identically zero case already handled.

For each fixed phi, the pair (cos(phi)Z+sin(phi)W, -sin(phi)Z+cos(phi)W) has the same law as (Z,W), by orthogonal invariance of their product Gaussian distribution. Consequently the expected disagreement between the rotated vectors at phi and phi+theta is independent of phi and equals the left side of (1). Average the preceding circle bound over phi and over (Z,W), using Fubini for bounded measurable indicators, to obtain (1). This argument handles p identically zero and constant polynomials as well; their disagreement is zero.

### B. Hermite tail bound

Use the normalized multivariate probabilists' Hermite basis H_alpha of L2(gamma_n), with |alpha| the total degree, and write f=sum_alpha f_alpha H_alpha. Define f_m to be its homogeneous degree-m component. For correlation rho in [0,1), the Gaussian noise operator is

    T_rho g(x)=E_W g(rho x+sqrt(1-rho^2)W).

It satisfies T_rho H_alpha=rho^|alpha| H_alpha. The generating function exp(tx-t^2/2)=sum_m He_m(x)t^m/m! proves this directly: take expectation after substituting rho x+sqrt(1-rho^2)W, which gives exp(rho tx-rho^2 t^2/2), and compare coefficients. Orthogonality follows by taking expectations of two generating functions, giving exp(st); independent coordinate products give the multivariate identities.

For completeness, density of this polynomial basis in Gaussian L2 follows as well: if g is orthogonal to every polynomial, the entire function F(z)=integral g(x)exp(z dot x) dgamma_n(x) has every Taylor coefficient zero. It is entire because Cauchy-Schwarz and Gaussian exponential integrability dominate the integrand and all its derivatives on each compact subset of C^n. Hence F=0. On imaginary arguments it is the Fourier transform of the finite signed measure g dgamma_n (finite by Cauchy-Schwarz). Uniqueness of Fourier transforms of finite measures then gives g=0 almost everywhere. This establishes completeness; Parseval and the noise eigenvalue formula extend from polynomials to all L2 functions by the contraction property of conditional expectation.

Since f is an indicator, (f(Z)-f(Z_theta))^2 is its disagreement indicator. For rho=cos(theta), the eigenvalue identity gives

    P(f(Z)!=f(Z_theta))
      =2 sum_(m>=0) (1-rho^m)||f_m||_2^2.                  (2)

To check the factor 2, expand the square: both marginal second moments are ||f||_2^2 and the cross moment is <f,T_rho f>=sum_m rho^m||f_m||_2^2.

Take rho=1-1/k, so theta=arccos(rho). For m>k, rho^m<=exp(-m/k)<=exp(-1). Equations (1) and (2) imply

    ||sum_(m>k) f_m||_2^2
      <= d theta / (2pi(1-exp(-1))).                       (3)

On [0,pi], sin(theta/2)>=theta/pi (concavity of sin on [0,pi/2], compared with its chord). Hence 1-cos(theta)=2sin(theta/2)^2>=2theta^2/pi^2. Our choice 1-rho=1/k yields theta<=pi/sqrt(2k). Substitution into (3) gives

    ||sum_(m>k) f_m||_2^2
      <= d / (2sqrt(2)(1-exp(-1))sqrt(k))
      <= d/sqrt(k),                                      (4)

since e>2 implies 2sqrt(2)(1-exp(-1))>1. No asymptotic constant is hidden here.

### C. Exact marginal laws kill the low-degree part

Let h=r-1. Its mean is zero. For any nonzero multi-index alpha of total degree <=k, H_alpha depends on at most k coordinates. Its expectation under nu is its expectation under the corresponding product Gaussian marginal, which is zero. Therefore <h,H_alpha>=0. All these integrals are finite by the exact marginal law, or by Cauchy-Schwarz under the density assumption. Thus h is orthogonal to the entire Hermite subspace of degrees <=k.

We conclude, by Cauchy-Schwarz and (4),

    |nu f-gamma_n f|
      =|<h,f>|=|<h,sum_(m>k)f_m>|
      <=B ||sum_(m>k) f_m||_2
      <=B sqrt(d) k^(-1/4).

The trivial upper bound 1 gives the stated minimum. Finally, if 0<=r<=M, then integral r^2 dgamma_n<=M integral r dgamma_n=M, so B^2=integral (r-1)^2 dgamma_n=integral r^2 dgamma_n-1<=M-1. QED.

## Referee checks and precise scope

- The circle root count is for the restriction of a degree-d polynomial and is bounded by 2d, not d. Dividing by 2pi gives the d theta/pi factor.
- Correlated endpoints at a polynomial zero do not invalidate the argument: finitely many circle endpoint angles have measure zero, and identically zero circle restrictions give no indicator disagreement.
- Exact coordinate marginals, rather than a density moment assumption, are what imply the Hermite orthogonality in Section C. The density assumption is used only for the L2 Cauchy-Schwarz estimate.
- The factor 2 in the noise spectral identity has been checked by expanding the squared indicator difference.
- The tail starts at m>k; rho^m<=e^-1 is valid for every such m and every k>=2.
- B may depend on dimension and may be arbitrarily large or undefined. This theorem supplies no bound uniform over the laws in P0170. In particular, singular admissible laws are outside this argument.
- No novelty is claimed: the Gaussian noise bound is a standard Kane-type argument, and the final estimate is the usual Hermite-tail/Cauchy-Schwarz reduction. All details are supplied to make its applicability and limitation reviewable.

## Why exact independence alone cannot supply the added density control

**Lemma.** For every fixed k>=1, exact k-wise Gaussian laws can have arbitrarily large finite ||r-1||_2, and can also be singular relative to product Gaussian measure.

**Proof of the first assertion.** Put n0=k+1. Take m independent blocks of the parity-conditioned Gaussian law from ATTEMPT.md, Section 1, each block of length n0. A set of at most k coordinates uses at most k coordinates of any one block, hence has product Gaussian law within that block. Independence of the blocks gives the same conclusion across blocks. Thus the combined vector of dimension m(k+1) is exact k-wise Gaussian. Its density relative to product Gaussian measure is r=product_(j=1)^m(1+B_j), where B_j is the product of the coordinate signs in block j. Under the product Gaussian comparator the B_j are independent uniform signs. Therefore E r=1 and E r^2=product_j E(1+B_j)^2=2^m. Consequently ||r-1||_2=sqrt(2^m-1), unbounded as m grows. Every density is nonnegative and finite. This does not assert that these laws have large PTF error; it only disproves a uniform density bound from k-wise independence alone.

**Proof of the singular assertion.** Let U_1,...,U_k be independent uniform variables on [0,1), put U_(k+1)=frac(sum_(i=1)^k U_i), and set X_i=Phi^-1(U_i). Endpoint values can be defined arbitrarily on their probability-zero occurrences. Omitting the last coordinate leaves k independent uniforms. If instead coordinate j<=k is omitted, condition on all k-1 other first coordinates. Then U_(k+1) is a fixed translate modulo 1 of the independent uniform U_j, so is uniform with a conditional law not depending on the conditioned values. Translation modulo 1 preserves Lebesgue measure: split [0,1) at the wrapping point and translate the two pieces. Hence the other k-1 coordinates together with the last coordinate are independent uniforms. All k-coordinate projections, and therefore all smaller projections, are product uniform laws. Applying the inverse Gaussian CDF coordinatewise gives exact product standard-Gaussian marginals.

The full vector lies almost surely on the Borel graph

    Phi(x_(k+1)) = frac(sum_(i=1)^k Phi(x_i)),

with the right-hand side in (0,1). Under product Gaussian measure, condition on the first k coordinates: the equation specifies at most one value of x_(k+1), which has zero probability under a continuous independent Gaussian. Fubini gives product Gaussian measure zero for the graph, while the constructed law gives it probability one. The law is therefore singular and has no density r at all. QED.

These exact-law examples show that the remaining obstacle is not removable by deriving an L2 bound solely from the stated marginal hypothesis.

## A sharper corollary under a uniformly bounded density

**Corollary.** Under the same exact k-wise marginal hypothesis, if 0<=r<=M, then for k>=2 and every degree-d polynomial threshold f,

    |nu f-gamma_n f|
      <= min(1, (M+1)d sqrt(log(k)/(2k)) + sqrt(M-1)/k).     (5)

For fixed M this gives independence of order O_M(d^2 epsilon^-2 log(d/epsilon+2)) as a sufficient bound. The explicit inequality (5), rather than this asymptotic notation, is the proved quantitative statement.

**Proof.** Put rho=exp(-log(k)/k), theta=arccos(rho), and g=T_rho f. The binary-valued nature of f implies the exact identity

    integral |f-g| dgamma_n = P(f(Z)!=f(Z_theta)).

Indeed, condition on Z: when f(Z)=0 the conditional expected disagreement is g(Z), and when f(Z)=1 it is 1-g(Z). These are exactly |f(Z)-g(Z)|. By (1) and 1-rho<=log(k)/k, this integral is at most d theta/pi<=d sqrt(log(k)/(2k)). Domination r<=M gives integral |f-g| dnu<=M integral |f-g| dgamma_n. Therefore

    |nu(f-g)-gamma_n(f-g)| <=(M+1)d sqrt(log(k)/(2k)).

As in Section C, h=r-1 is orthogonal to all Hermite degrees <=k. The high-degree part of g has norm at most rho^(k+1)||f||_2<=rho^k=1/k. Cauchy-Schwarz consequently gives

    |nu g-gamma_n g| <=||h||_2/k<=sqrt(M-1)/k.

Add the two inequalities and the trivial upper bound 1 to obtain (5). To justify the displayed sufficient asymptotic order, set A=d/epsilon+2>=2 and choose k=ceil(C_M A^2 log A) for a sufficiently large constant depending only on M. Then log k=O_M(log A), so the first term is O_M(d/A) times an arbitrarily small constant obtained by increasing C_M; more explicitly the controlling coefficient is of order sqrt((log C_M+1)/C_M), which tends to zero. The second term is at most sqrt(M-1)/(C_M A^2 log A). Since d/A<=epsilon and 1/A^2<=epsilon^2<=epsilon, both terms can be made <=epsilon/2, uniformly in d>=1 and 0<epsilon<1. Constant polynomials already have zero error. QED.

This proof uses r<=M with M fixed independently of dimension and epsilon. The preceding block example has M=2^m and therefore lies outside every fixed-M class as m grows. Neither (5) nor its asymptotic form settles P0170 for unrestricted exact k-wise laws. This does not claim that a comparable bound for the unrestricted class is false; that remains unproved here.
