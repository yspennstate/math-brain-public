# P0170 — exact Gaussian limited independence

Date: 2026-10-12. This is a partial result, not a solution of the open problem and not a novelty claim.

## Statement and conventions

Let K(d,eps) be the least positive integer k such that, for every finite n, every real polynomial p of total degree at most d, and every law X on R^n whose projections onto every set of at most min(k,n) coordinates are product N(0,1),

    |P(p(X)>=0) - P(p(Z)>=0)| <= eps,    Z ~ N(0,I_n).

This is the question on PDF page 9 of Ryan O'Donnell, arXiv:1204.6447. Product Gaussian coordinate marginals are the assumption throughout. The vector X need not be jointly Gaussian. For n<k, the standard meaning of k-wise independence includes full independence; a literal requirement involving only nonexistent k-tuples would otherwise be vacuous. The source uses 'degree-d'; as usual for a PTF class this means degree at most d. Every main construction below has its displayed degree exactly, and the special-case theorem also applies if one restricts to exactly degree d.

The source itself reports an Omega(d^2/eps^2) necessary bound and older general upper bounds. No result below improves that reported lower bound. See LITERATURE.md for the checked literature and search limitations.

## 1. Exact-law parity obstruction (rechecked brain lead)

**Theorem 1.** For every integer n>=2, there is an (n-1)-wise independent standard-Gaussian vector X in R^n for which prod_i X_i>0 almost surely. The degree-n polynomial prod_i x_i has error 1/2. Consequently K(d,eps)>=d for d>=2 and eps<1/2.

**Proof.** Let S be uniform on the 2^(n-1) sign vectors in {-1,1}^n whose product is +1. For a subset J of size j<n, and any assigned signs on J, there are exactly 2^(n-j-1) extensions: freely choose all but one of the remaining signs, then the last sign is uniquely forced. Thus P(S_J=s_J)=2^-j, which proves product uniform marginals, not just zero mixed moments. Independently sample iid R_i=|G_i| with G_i standard normal, and put X_i=S_i R_i. On each J, the pairs (S_i,R_i) are independent and each signed half-normal is exactly standard normal: its density at a nonzero x is (1/2)*sqrt(2/pi)*exp(-x^2/2). Thus X_J has product Gaussian law. Since every R_i>0 almost surely, prod X_i>0. Under full Gaussian independence the product sign is uniform, so P(prod Z_i>=0)=1/2. Taking n=d produces the lower bound. QED.

For k<d-1 the same law is also k-wise independent. The d=1 assertion K>=1 follows from the positive-integer convention. The example has an absolutely continuous joint density (1+prod_i sign(x_i)) times the product Gaussian density, so the discrepancy is not an artifact of mass on a polynomial zero set.

## 2. Explicit linear-threshold discrepancies at arbitrarily large k

**Theorem 2.** Let n=2m+1>=3 be odd, and let X have the parity-conditioned Gaussian law in Theorem 1. For p(x)=sum_i x_i, its signed probability discrepancy is

    P(sum X_i>=0)-1/2 = (-1)^m / pi * integral_0^infty A(t)^n dt/t,

where

    A(t)=E sin(t|G|)=sqrt(2/pi)*exp(-t^2/2)*integral_0^t exp(u^2/2) du.

In particular the discrepancy in absolute value is at least

    (log 2)/pi * c^n,       c=(1/2)*sqrt(2/pi)*exp(-1/2)>0.

**Proof.** Write Z for the independent Gaussian vector, B=prod_i sign(Z_i), and H={sum Z_i>=0}. The parity law has density 1+B relative to the product law, so the discrepancy is E[1_H B]. The hyperplane sum Z_i=0 has zero probability. Since E B=0, this expectation equals (1/2)E[sign(sum Z_i)B]. For eta>0, elementary integration gives

    (2/pi)*integral_0^infty exp(-eta*t)*sin(ts) dt/t = (2/pi)*arctan(s/eta).

For completeness, differentiate the integral in s: integral exp(-eta*t) cos(ts) dt = eta/(eta^2+s^2), and integrate from s=0. The expression is bounded by 1 and converges to sign(s) for s!=0. Fubini is legitimate: near zero use |sin(t sum Z_i)|<=t|sum Z_i|, and away from zero the exponential factor is integrable after division by t. Independence gives

    E[exp(it sum Z_i) B] = product_i E[exp(it Z_i) sign(Z_i)] = (i A(t))^n.

Its imaginary part is (-1)^m A(t)^n. The ODE A'(t)=sqrt(2/pi)-t A(t), A(0)=0, follows by integration by parts against exp(-r^2/2); solving it gives the displayed formula and proves A(t)>0 for t>0. Also |A(t)|<=t E|G| near zero. Integration by parts in the sine integral gives |A(t)|<=2 sqrt(2/pi)/t for t>0. Hence A(t)^n/t is absolutely integrable for every n>=1. Dominated convergence removes eta and proves the exact formula. For 1/2<=t<=1, the ODE formula gives A(t)>=sqrt(2/pi)*exp(-1/2)*t>=c. Restricting the integral to that interval gives the lower bound, since integral_(1/2)^1 dt/t=log 2. QED.

For any given k>=1 choose the least odd n>k, so n<=k+2. This supplies an exact k-wise Gaussian law with linear-threshold error at least (log 2)/pi*c^(k+2). Thus it independently proves logarithmic growth in 1/eps for the linear case. It is much weaker than the source's reported Omega(eps^-2) lower bound and is included as an explicit checked construction, not an improvement.

The integral formula also extends algebraically to n=1, where parity conditioning makes X half-normal. The n=1 quadrature entry is only a normalization check for the integral; that one-coordinate law is not an admissible standard-Gaussian marginal counterexample.

## 3. A self-contained upper bound for polynomials of one linear form

**Theorem 3.** Let k>=2 be even. If X satisfies the exact marginal hypothesis and a is a nonzero real vector, then with S=(a dot X)/||a||_2,

    sup_x |P(S<=x)-Phi(x)| <= 32/sqrt(k).

Consequently, for every real univariate q of degree at most d,

    |P(q(a dot X)>=0)-P(q(a dot Z)>=0)| <= min(1,32d/sqrt(k)).

An even integer k>=1024d^2/eps^2 therefore suffices for this special class, uniformly in n and a. If the right-hand side exceeds 1, the probability bound is simply the trivial bound 1.

### 3.1 Moments and the characteristic-function remainder

Write b=a/||a||_2. For each j<=k, expand (sum b_i X_i)^j by the multinomial formula. Each monomial has at most j distinct coordinates in its support, so its expectation is its product-Gaussian expectation. Absolute integrability follows from those same product marginals and finite Gaussian moments. Consequently E S^j=E G^j for 0<=j<=k. In particular E|S|^k=E G^k, since k is even. This is a consequence of the assumption; it is not substituted for that assumption in the problem.

Taylor's formula with integral remainder for exp(iu) implies

    |exp(iu)-sum_(j=0)^(k-1) (iu)^j/j!| <= |u|^k/k!.

Indeed the remainder is (iu)^k/(k-1)! times integral_0^1 (1-v)^(k-1) exp(ivu) dv, whose absolute value is at most |u|^k/k!. Taking expectations and cancelling the matching terms gives

    |phi_S(t)-phi_G(t)| <= 2 |t|^k E G^k/k!.

For k=2m, integration by parts in the Gaussian density gives E G^(2m)=(2m)!/(2^m m!). Also log(m!)>=integral_1^m log x dx>=m log m-m, hence

    E G^k/k! = 1/(2^m m!) <= (e/k)^(k/2).

### 3.2 A proved smoothing inequality with explicit constants

Use the probability density

    K(v)=3/(4pi) * (sin(v/2)/(v/2))^4,

with its continuous value at 0. Its characteristic function psi has support in [-2,2]. Here are the normalization and support calculations. For U uniform on [-1/2,1/2], E exp(ivU)=sin(v/2)/(v/2). The sum of two copies has triangular density B2(u)=(1-|u|)_+, and the sum of four has density B4=B2*B2 supported in [-2,2]. B4(0)=integral_(-1)^1(1-|u|)^2 du=2/3. Fourier inversion therefore gives integral sinc(v/2)^4 dv=2pi B4(0)=4pi/3 and psi(t)=(3/2)B4(t). Thus K is normalized and |psi|<=1.

Let V have density K. The elementary bounds K(v)<=3/(4pi) and K(v)<=12/(pi v^4) yield

    E|V| <= 3/(4pi)+12/pi=51/(4pi) <=17/4,
    q0:=P(V>4)=P(V<-4) <=4/(pi*4^3)=1/(16pi)<=1/48.

The inequalities use pi>3. Let F be the CDF of S, let G0=Phi, let D=sup |F-G0|, and let H_T be the difference of the CDFs of S+V/T and G+V/T. With M=sup Phi'<=1/2, we claim

    (1-2q0) D <= sup|H_T| + M(4+E|V|)/T.                 (S)

To prove (S), put D_+(x)=F(x)-G0(x). On V<=4, monotonicity of F and the Lipschitz bound for G0 give

    D_+(x+(4-V)/T) >= D_+(x)-M(4-V)/T.

On V>4 the same difference is at least -D. Taking expectations shows

    H_T(x+4/T) >= (1-q0)D_+(x)-q0 D - M(4+E|V|)/T.

If the supremum D comes from the positive side, take a sequence x with D_+(x) tending to D; no attainment assumption is needed. If it comes from the negative side, apply the identical argument to G0-F at x-4/T and the event V>=-4, using monotonicity of F for the upper bound at points <=x. Both give (S).

Fourier inversion gives the additional bound

    sup |H_T| <= (1/pi)*integral_0^(2T) |phi_S(t)-phi_G(t)| dt/t.  (F)

To justify the CDF form of inversion rather than only the density form: the product (phi_S-phi_G)psi(t/T) is compactly supported and integrable, so it inverts to the difference of the two continuous smoothed densities. Division by -it is also integrable, by the Taylor bound at zero. Its inverse Fourier transform has derivative equal to that density difference and tends to zero at both infinities by the Riemann-Lebesgue lemma. The CDF difference has the same derivative and zero limit at minus infinity, hence equals that transform. Taking absolute values proves (F); the integrand on negative t has the same absolute value as on positive t. The Fourier inversion and Riemann-Lebesgue statements used here are the usual elementary L1 Fourier theorems; no probabilistic smoothing theorem is being assumed.

Take T=sqrt(k)/(4sqrt(3)). Combining the Taylor bound with (F) gives

    sup |H_T| <= (2/(pi k)) * (2T)^k * (e/k)^(k/2)
               <= (2/(pi k))*2^(-k) <=1/sqrt(k),

since e<3. Moreover

    M(4+E|V|)/T <= (33/8)*4sqrt(3)/sqrt(k)
                 <=231/(8sqrt(k)),

using 4sqrt(3)<7. Since 1-2q0>=23/24, (S) implies

    D <= (24/23)*(1+231/8)/sqrt(k)
       = (717/23)/sqrt(k) <32/sqrt(k).

This proves the first assertion of Theorem 3.

### 3.3 Root multiplicities, endpoints, and atoms

After rescaling q to absorb ||a||_2, it suffices to compare q(S) and q(G). A zero or constant polynomial defines a constant event, of error zero. Otherwise list its real roots r_i with multiplicities m_i; sum m_i<=d. Between roots the sign is constant. At an odd-multiplicity root, the signs on the adjacent intervals differ, and the event q>=0 has value 1 at the root. Its indicator can therefore be represented by adding or subtracting one half-line indicator with that endpoint, either 1_{s>=r_i} or 1_{s>r_i}, chosen so the root is included. The absolute coefficient cost is 1<=m_i.

At an even-multiplicity root the adjacent signs agree. If both are positive there is no change to the indicator. If both are negative, the event contains just the singleton root locally, represented by 1_{s>=r_i}-1_{s>r_i}, of coefficient cost 2<=m_i. Starting with the constant indicator on the leftmost interval and adding these local terms gives the event indicator on every interval and at every root. The total absolute coefficient cost is at most sum m_i<=d.

Each open or closed half-line has discrepancy at most D. For a closed half-line this uses F(r-)=lim_(x upward r)F(x) and continuity of Phi; the Kolmogorov bound passes to the limit. In particular, atoms of S at roots have not been discarded. The triangle inequality gives event error at most dD. If a=0 both events are the same constant, so this case is also settled. QED.

## 4. An explicit barrier to using only the scalar moments of p(X)

**Theorem 4 (scalar barrier, not a counterexample to P0170).** The scalar law of Y=G^3, G standard normal, has a different probability law with all the same raw moments but a different threshold probability at a positive threshold.

**Proof.** Define the bounded even function

    h(y)=sin((sqrt(3)/2)*|y|^(2/3)-pi/6).

Let mu be the law of Y and define dnu=(1+h)dmu. Since |h|<=1, this is nonnegative. Put U=G^2/2, whose density on (0,infinity) is u^(-1/2)exp(-u)/Gamma(1/2). For m>=0,

    E[Y^(2m)h(Y)]
      = 2^(3m)/Gamma(1/2) * Im[exp(-i*pi/6)
          * integral_0^infinity u^(3m-1/2)exp(-(1-i*sqrt(3))*u) du]
      = 2^(3m) Gamma(3m+1/2)/Gamma(1/2)
          * Im[exp(-i*pi/6)*(1-i*sqrt(3))^(-(3m+1/2))]
      = 0.

The final equality uses 1-i*sqrt(3)=2 exp(-i*pi/3), so the complex expression whose imaginary part is taken has argument (3m+1/2)*pi/3-pi/6=m*pi. The Laplace integral identity used in the second equality follows from the defining real Gamma integral by positive-real change of variables; both sides are analytic in the right half-plane (dominated differentiation on compact subsets), so the identity theorem extends it there, using the branch with argument in (-pi/2,pi/2). This checks the complex phase and does not assume an invalid change of variable along a complex contour.

All odd mixed terms E[Y^(2m+1)h(Y)] vanish because mu and h are even. The m=0 case proves E h(Y)=0, so nu has mass 1. All absolute moments of nu are finite, since its density relative to mu is at most 2, and every raw moment equals the corresponding mu moment.

Nevertheless nu differs from mu on thresholds. Set

    t=(pi/(6sqrt(3)))^(3/2)>0.

For 0<y<t, the sine's argument is strictly between -pi/6 and -pi/12, so h(y)<0. Both mu and nu are symmetric and nonatomic. Their difference on [t,infinity) is therefore

    integral_[t,infinity) h dmu = -integral_(0,t) h dmu >0,

because integral_(0,infinity) h dmu=0 and mu gives positive density to (0,t). This proves the claimed threshold discrepancy. QED.

This theorem explicitly shows why matching arbitrarily many moments of the *scalar* polynomial value is insufficient as a stand-alone reduction for degree 3. It **does not** supply a vector with the required Gaussian coordinate marginals: for one coordinate the map x->x^3 is a bijection, and pulling nu back through it changes that coordinate's Gaussian law. It cannot be used to contradict Kane's finite-k theorem. No novelty is claimed for this classical type of moment-indeterminate perturbation.

To phrase the scalar barrier at threshold zero, subtract the same t from both laws. The binomial formula shows that every raw moment of Y-t is still preserved, while P(Y-t>=0) changes. Thus the issue persists for the scalar value of the degree-3 polynomial x^3-t; the Gaussian-coordinate condition remains precisely the missing hypothesis in this example.

## 5. Referee audit and computations

Potential failure points and their disposition:

1. A moment-matched law need not have product coordinate marginals. The constructions in Sections 1 and 2 are checked by counting *every* sign assignment and by multiplying full half-normal densities. Section 3 starts from the exact assumption and only then derives moments.
2. Positivity of the parity density and its normalization: 1+B is either 0 or 2 and E B=0.
3. Boundary convention >=0: the lower examples are absolutely continuous and the upper proof explicitly treats isolated roots and open/closed endpoints.
4. Oscillatory integral cancellation: n is odd, A(t)>0, and the entire integrand has fixed sign. For even n, this particular threshold has discrepancy zero by central symmetry; it is not used to infer a positive discrepancy.
5. Exchanging expectation and the sine integral: exponential damping is retained until after Fubini; integrable bounds at 0 and infinity are proved before its removal.
6. Smoothing at an unattained CDF supremum: take a maximizing sequence, as in Section 3.2.
7. Fourier support, normalization, and moment of K: calculated from B2*B2 and explicit tail bounds, rather than inferred from numerical integration.
8. Generalization to arbitrary degree-d polynomials: **not justified**. The entire special-case upper proof uses a Gaussian scalar comparator. For a general nonlinear p, p(Z) is not Gaussian and its high moments can grow too fast for this choice of cutoff to give the same bound.
9. The scalar moment barrier is not an admissible vector counterexample: its cube-root marginal is not Gaussian. Its role is to rule out an attempted scalar-moment-only implication, not exact limited independence.

Executable checks and their actual outcomes are recorded in checks.json and lean_check.log. ParityCheck.lean checks finite n=3 and n=5 sign counts using kernel `decide +kernel`, not native_decide. It does not formalize Gaussian measure or the analytic upper theorem; those proofs are given above. Numerical quadrature is supporting evidence only.

## 6. Remaining gap and stopped directions

A further conditional result, proved in full in DENSITY_BOUND.md, treats arbitrary degree-d PTFs when the exact k-wise law has density r relative to product Gaussian measure with ||r-1||_2<=B: the error is at most min(1,B sqrt(d) k^(-1/4)), for k>=2. Its circle-root-count, Hermite spectral and Cauchy-Schwarz steps are written out and independently reviewed. The original problem has no uniform L2 density bound and permits singular laws, so this does not close the gap.

For a stronger bounded-density assumption 0<=r<=M, that file also proves error <=(M+1)d sqrt(log(k)/(2k))+sqrt(M-1)/k. Thus for fixed M there is a sufficient k of order O_M(d^2 epsilon^-2 log(d/epsilon+2)). It also constructs exact k-wise Gaussian laws with arbitrarily large density norms and singular laws, proving that the added density hypothesis does not follow from exact independence.

The two precise steps needing a different argument for unrestricted laws are the transfer of Gaussian smoothing error to nu using r<=M, and the control of the high-degree expectation using ||r-1||_2. Exact k-wise marginals give low-degree orthogonality but do not bound either density norm. Smoothing a singular law first does not provide a uniform density bound or, without another theorem, control its original threshold probability near polynomial zeros. This is an obstruction to the current proof method, not a proof that the desired unrestricted bound is false.

The optimal K(d,eps) for **all** degree-d polynomials has not been determined. In particular there is no proof here that O(d^2/eps^2) exact coordinate independence suffices for arbitrary multivariate PTFs, nor a stronger matching lower bound closing the general literature gap. PRGs consisting of independent sums cannot be substituted for an arbitrary k-wise Gaussian vector: membership of the sum in the k-wise class does not imply every member has that representation.

Directly applying the scalar moment argument to p(X) matches only floor(k/d) powers of p, while the independent comparison variable p(Z) can have moment growth characteristic of a degree-d chaos and poor anti-concentration. The Gaussian cutoff calculation in Section 3 does not extend. Treating this as a proof for arbitrary p would be an error.

The special case proved above, the exact-law lower examples, the explicit scalar moment barrier, and the literature audit are the completed results of this attempt. No optimality or novelty is claimed. The general problem remains unresolved by this work.

## Final verification record — 2026-10-12

At closure no completed result was available from the corrected finite Lean run. It is unverified; live output remains in lean_check.log. The complete written counting proof and Python exact enumeration are the independent checks. No Lean certification is claimed.

The first Lean run failed to infer DecidablePred for named definitions; the corrected source uses reducible abbreviations. The failed output is preserved in lean_check_first_attempt.log. Only one Lean command ran at a time, from ~/lean_verify, with a 3600-second timeout.

All exact parity checks (n=2 through 9), all 142 rational endpoint representations, all quadrature and Monte Carlo assertions, the scalar-perturbation phase and normalization checks, and the required-file/JSON audit passed. Floating-point checks are evidence only; the probability claims rely on the full written proofs. The search limitations are recorded in LITERATURE.md.

Final verdict: PARTIAL. The completed work does not determine the optimal k(d,epsilon) for arbitrary degree-d polynomials. No SOLVED or SOLVED_IN_LITERATURE claim is made.
