# P0286 — further attempt, 12 October 2026

The first attempt left sharp general-ASEP line decay and general-ASEP canonical ring/critical finite-size scaling unresolved. All definitions below retain its convention: 0<a<b<1, p=a(1-b), q=(1-a)b, r=p/q, h=1-p-q, and reverse jump rate theta in (0,1). The exclusive second-color density is delta=b-a. The earlier queue covariance reduction is retained, but every new spectral step must be proved independently of the brain hints.

## Two approaches not previously tried

1. **Factor the reversible queue Jacobi matrix.** Its coefficients are those of a q-deformed Hermite/Al-Salam-Chihara family. Instead of only comparing Dirichlet forms as before, factor its positive generator into a bidiagonal operator and its adjoint. Interchanging the factors may lower the drift parameter and classify discrete eigenvalues above the continuous spectrum. If the first nonconstant bound state couples to the occupation observable, it would give a sharp pure exponential covariance regime and show why the TASEP power prefactor need not persist for general ASEP. This targets the exact general-ASEP exponent/prefactor gap.

2. **Use a cyclic bridge/excursion reduction for the critical TASEP ring.** The two fixed-count queue input rows yield a random-walk bridge with total drift -k2. A cycle lemma and exact ballot/reflection counts could compute joint probabilities of unused service sites when k2 is of order sqrt(N), then lead to Brownian-bridge rather than infinite Brownian-motion covariance scaling. This directly targets N*delta^2 of order one. Unlike the first attempt's local-window total-variation coupling, it would retain the global bridge constraint. The main difficulty is evaluating two queue-minimum events with fixed counts and simultaneous arrivals/services, rather than only obtaining height convergence.

Approach 1 is selected first: its operator is explicit, permits low-cost numerical checks of each factorization and eigenvalue, and may yield a complete sharp special case with an elementary proof. Approach 2 remains a concrete unpursued direction, not a claimed result.

## Progress log

- Read the entire original attempt and its remaining gaps. Asked math_recall.py: "ASEP queue spectral gap Al Salam Chihara q Charlier birth death correlations". Response recorded in LITERATURE.md once returned.
- Proofs, computations, failures, and remaining gap will be appended here as they are established.

## 1. Complete queue spectrum by a Darboux factorization

This section is an elementary operator proof; it does not assume an orthogonal-polynomial spectral formula. Let d_k=product_{j=1}^k(1-theta^j), d_0=1, t=sqrt(pq), and A=sqrt(q/p)>1. Under the unitary stationary-weight map, the queue transition operator is J=hI+tK_A, where the bounded self-adjoint Jacobi operator on l2(N0) is

    (K_A w)_k = sqrt(1-theta^k) w_{k-1}
                + A theta^k w_k
                + sqrt(1-theta^(k+1)) w_{k+1}.

The first term is absent at k=0. Define a bounded upper-bidiagonal operator

    (B_A w)_k = A^(-1/2) w_k
                - A^(1/2) sqrt(1-theta^(k+1)) w_{k+1}.

Multiplying the two bidiagonal matrices gives exactly, as bounded operators,

    B_A* B_A = (A+A^(-1))I - K_A,                    (S1)
    B_A B_A* = (A+A^(-1))I - K_(A theta).            (S2)

For (S1), diagonal entry k is A^(-1)+A(1-theta^k), with the second summand zero at k=0; the adjacent entries are -sqrt(1-theta^(k+1)). For (S2), diagonal entry k is A^(-1)+A(1-theta^(k+1)), with the same adjacent entries. All other entries vanish. Equality of the finite-coordinate matrix elements and boundedness prove operator equality. A finite truncated product has an extra last-row boundary defect in (S2); it must not be mistaken for the infinite identity.

The equation B_A w=0 has exactly the formal solutions

    w_k = w_0 A^(-k)/sqrt(d_k).

Since d_k tends to a strictly positive limit L, this is in l2 if and only if A>1. The kernel is then one-dimensional. The equation B_A* w=0 starts with A^(-1/2)w_0=0 and recursively forces every coordinate to zero, so ker(B_A*)={0} for every A>0.

Use the polar decomposition B_A=U|B_A|. Its initial space is ker(B_A)^perp, and its final space is closure(range(B_A))=ker(B_A*)^perp=l2. Thus U is a unitary from ker(B_A)^perp onto l2, and it takes the restriction of B_A*B_A to B_AB_A*. Combining (S1)-(S2), the restriction of K_A to ker(B_A)^perp is unitarily equivalent to K_(A theta). This step uses the standard bounded-operator polar decomposition, not an unjustified inversion of B_A; closedness of its range is not needed.

For 0<A<=1, the entire spectrum of K_A is exactly [-2,2]. To see the upper bound, K_A<=K_1 in quadratic-form order and (S1) with A=1 gives K_1<=2I. The lower bound K_A>=-2I follows from nonnegative diagonal and the adjacent-coefficient bound sqrt(1-theta^(k+1))<=1, using 2|w_k w_(k+1)|<=|w_k|^2+|w_(k+1)|^2. Finally K_A is a compact perturbation of the free half-line matrix with diagonal zero and adjacent entries 1: truncating its decaying diagonal and decaying adjacent-entry differences gives finite-rank approximations in operator norm. The free matrix has spectrum and essential spectrum [-2,2] (sine-transform diagonalization, or cutoff sine-wave Weyl sequences together with its norm bound). The standard compact-perturbation invariance of essential spectrum therefore gives [-2,2] as the essential spectrum of K_A. The upper/lower bounds leave no possible additional spectral points. These named spectral-theory facts apply to bounded self-adjoint operators on the stated Hilbert space.

Iterate the unitary factor swap until A theta^M<=1. At each earlier step one one-dimensional eigenspace is removed. It follows that the full spectrum of the original queue is

    [lambda_-,lambda_+] union {lambda_j : j>=0,
                                      theta^j>sqrt(r)},              (S3)
    lambda_+/- = h +/- 2 sqrt(pq),
    lambda_j = h + q theta^j + p theta^(-j).

There are finitely many listed discrete eigenvalues, each simple. Their order is strictly decreasing as j increases while theta^j>sqrt(r): x+x^(-1) is strictly increasing for x>1, and x=A theta^j decreases. The stationary eigenvalue is lambda_0=1. Equality theta^j=sqrt(r) contributes no separate discrete atom above the band. No claim about the type of spectral measure within the band is needed for (S3).

In particular the exact L2 queue gap is

    1 - lambda_+,                 if theta<=sqrt(r),
    1 - (h+q theta+p/theta),       if theta>sqrt(r).                  (S4)

This sharply improves the first attempt's comparison gap bound. It is an exact operator-gap result, not yet by itself a covariance prefactor theorem in the band-dominated regime.

## 2. Sharp pure exponential covariance when theta>sqrt(r)

Assume sqrt(r)<theta<1. For n>=1, define

    lambda_1=h+q theta+p/theta,
    W_1=pq(1-theta)(1-r/theta^2)>0,
    R=lambda_2 if theta^2>sqrt(r), and R=lambda_+ otherwise.

Then R<lambda_1<1 and the exact covariance satisfies

    C_22(n)=W_1 lambda_1^(n-1)+E_n,
    0<=E_n<=(C_22(1)-W_1) R^(n-1),                 (S5)
    C_22(1)-W_1=p^2(1-theta)(theta^(-2)-1).

Consequently C_22(n)~W_1 lambda_1^(n-1). This is a genuine stronger general-ASEP infinite-line special case. In this regime a universal n^(-3/2) prefactor would be false; no such universal conjecture was asserted by the source or the earlier attempt.

Here is the full computation of the observable projection. Put f(k)=theta^k, m=1/(1-r/theta), and g(k)=theta^(-k)-m. The stationary series Z(s)=sum_k s^k/d_k obeys

    Z(theta s)=(1-s)Z(s), 0<=s<1.

Proof: d_k=(1-theta^k)d_(k-1), so Z(s)-Z(theta s)=sum_{k>=1}s^k/d_(k-1)=sZ(s). Absolute convergence justifies the subtraction and shift. Applying this identity at s=r/theta and s=r/theta^2 (both less than one) gives

    E_pi theta^(-Q)=1/(1-r/theta),
    E_pi theta^(-2Q)=1/[(1-r/theta)(1-r/theta^2)].

Thus g is centered and lies in L2(pi). Direct substitution into the queue kernel gives

    P(theta^(-k))=lambda_1 theta^(-k)+q(1-theta),
    Pg=lambda_1 g,

including k=0: the downward coefficient is zero there, and the same identity holds. Also

    Var_pi(g)=r(1-theta)/[theta^2(1-r/theta)^2(1-r/theta^2)],
    Cov_pi(f,g)=-r(1-theta)/[theta(1-r/theta)].

The second identity uses f(k)theta^(-k)=1 and E_pi f=1-r. Therefore the covariance spectral weight at lambda_1 is

    q^2 Cov_pi(f,g)^2/Var_pi(g)=W_1.

By (S3), this simple eigenvalue is the strictly largest nonstationary eigenvalue; the rest of the centered spectrum is bounded above by R. The previous attempt proved P is positive semidefinite, so all remaining spectral values are nonnegative. Decompose f-E_pi f orthogonally into its g projection and remainder. The spectral theorem and the earlier exact covariance identity (2.1) give (S5), with the remaining total mass q^2 Var_pi(f)-W_1=C_22(1)-W_1. The displayed simplification follows from C_22(1)=(1-theta)(q-p)p. All divisions are legitimate under theta^2>r and 0<theta<1.

## 3. A further weak-asymmetry spatial limit

As an immediate proved consequence, fix a,b and let epsilon=1-theta down to zero. For integers n>=1 with n epsilon->s in [0,infinity),

    C_22(n)/epsilon -> p delta exp(-delta s).                         (S6)

Indeed the condition theta>sqrt(r) eventually holds. From (S5), W_1/epsilon->pq(1-r)=p delta, and

    1-lambda_1=epsilon(q-p/theta),

so lambda_1^(n-1)->exp(-delta s), by the elementary logarithm expansion. The nonnegative remainder is bounded by

    p^2 epsilon(theta^(-2)-1)=O(epsilon^2),

uniformly in n, since 0<=R<=1. Dividing by epsilon proves (S6). This is a fixed-density weak-asymmetry limit on the line, not the source's closing-density-gap ring regime. It is consistent with the earlier positive-lag integrated covariance p, since the limiting exponential has integral p.

## Computation saved so far

`spectral_verify.py` and `spectral_checks.json` check (S1)-(S2) on an interior block, explicitly omitting the artificial last-row defect of (S2); enumerate all predicted eigenvalues above the band at theta=0.2,0.5,sqrt(2/7),0.7,0.9 for a=0.3,b=0.6; verify the direct eigenfunction equation; and compare W_1 to the numerical occupation-observable projection. All checks passed. At theta=0.7, W_1=0.006303673469..., lambda_1=0.925428571429..., and the n=1000 covariance/leading-term ratio is 1.000000000166. At theta=0.9 there are five nonstationary discrete modes; the n=1000 ratio is 1.000000000004. These checks use principal finite sections only as numerical evidence; the infinite proof is the operator argument above.

## 4. Checked neighbouring-area input and continuous covariance measure

Write (z;theta)_infinity=product_{j>=0}(1-z theta^j), L=(theta;theta)_infinity, and pi_0=(r;theta)_infinity. The last identity follows from Z(theta s)=(1-s)Z(s): iterate it, let theta^M s->0 so Z(theta^M s)->1, and obtain Z(s)=1/(s;theta)_infinity. All product limits converge uniformly on compact sets of bounded complex z, since sum theta^j is finite.

External input, with its exact hypotheses and normalization: Koekoek and Swarttouw, *The Askey-scheme of hypergeometric orthogonal polynomials and its q-analogue*, arXiv:math/9602214 (20 February 1996), Section 3.18, formulas (3.18.2), (3.18.4), (3.18.7), PDF pp.82–83 (printed pp.80–81). Only the real |c|<1 orthogonality identity is needed. In probability normalization it says: the polynomials H_k(x;c|theta), H_0=1, H_-1=0, satisfying

    2x H_k=H_(k+1)+c theta^k H_k+(1-theta^k)H_(k-1),

are orthogonal for the probability measure on phi in [0,pi]

    dmu_c(phi)=L/(2pi) *
       |(exp(2i phi);theta)_infinity /
         (c exp(i phi);theta)_infinity|^2 dphi,

with squared norm d_k for H_k(cos(phi)). This is the reference's formula after multiplying its unnormalized weight by L and putting x=cos(phi). It applies for 0<theta<1 and real |c|<1. The norms and recurrence identify K_c with multiplication by 2cos(phi), in the basis H_k/sqrt(d_k): polynomials are dense in L2 of this finite compactly supported measure, by continuous-function density and polynomial approximation. This is a checked orthogonal-polynomial theorem used as an input, not a theorem in print solving the ring question.

The generating function is

    sum_{k>=0} H_k(cos(phi);c|theta) z^k/d_k
      = (c z;theta)_infinity /
        [(z exp(i phi);theta)_infinity
         (z exp(-i phi);theta)_infinity], |z|<1.       (S7)

It also follows directly, without needing another orthogonality assumption. The right-hand product is analytic for |z|<1, equals 1 at z=0, and satisfies

    (1-2cos(phi)z+z^2)F(z)=(1-cz)F(theta z).

Comparing its nth coefficient gives exactly the stated polynomial recurrence, divided by d_(n-1). Thus its Taylor coefficients are H_k/d_k. Uniform analytic convergence on compact z-disks proves (S7) and justifies the spectral-series evaluation below. No arbitrary polynomial basis is assumed to be orthogonal.

The same probability measure formula remains valid at c=1, with the removable endpoint ratio interpreted by its limit. Here is the endpoint proof. K_c->K_1 in operator norm as c increases to one, so their e_0 spectral measures converge weakly (first for polynomials in the bounded operators, then for continuous functions by polynomial approximation). The factors with j>=1 in the denominator have modulus bounded below by product(1-theta^j)=L. Those in the numerator are bounded above by a finite constant depending only on theta. The first numerator factor has squared modulus 4sin^2(phi), and for 1/2<=c<=1 the first denominator factor satisfies

    |1-c exp(i phi)|^2=(1-c)^2+2c(1-cos(phi))
                       >=1-cos(phi).

Since sin^2(phi)/(1-cos(phi))<=2, all these densities have a uniform finite bound. Dominated convergence gives the density at c=1 and preserves total mass one. It therefore identifies the weak spectral-measure limit and leaves no unaccounted endpoint atom. The recurrence and orthogonality also pass to the limit for each finite polynomial degree.

Now assume theta<=sqrt(r), so c=A theta<=1 and the original centered queue has no discrete modes. Let w^0_k=sqrt(pi_0) A^(-k)/sqrt(d_k) be the normalized stationary vector and v_k=w^0_k(theta^k-(1-r)) the centered occupation vector. The bidiagonal formula gives

    (B_A v)_k = sqrt(pi_0)(1-theta)/sqrt(A)
                      * (theta/A)^k/sqrt(d_k).

Its spectral transform under K_c, using (S7) at z=theta/A, is

    F_B(phi)=sqrt(pi_0)L/sqrt(A) /
       [(z exp(i phi);theta)_infinity
        (z exp(-i phi);theta)_infinity].

Indeed c z=theta^2 and (theta^2;theta)_infinity=L/(1-theta). The series converges in L2, and (S7) identifies its pointwise analytic representative. By (S1)-(S2) and polar decomposition, the spectral measure of B_A v for K_c is (A+A^(-1)-x) times the spectral measure of v for K_A. The divisor is uniformly positive on the band because A>1. Divide by it, multiply by q^2 as in the queue covariance identity, and use

    A(A+A^(-1)-2cos(phi))=|1-A exp(i phi)|^2,
    (A exp(i phi);theta)_infinity
      =(1-A exp(i phi))(A theta exp(i phi);theta)_infinity.

This proves the exact formula for every n>=1 in this parameter regime:

    C_22(n)=integral_0^pi (h+2t cos(phi))^(n-1) w(phi) dphi,   (S8)

    w(phi)=q^2 pi_0 L^3/(2pi) *
       |(exp(2i phi);theta)_infinity|^2 /
       [|(A exp(i phi);theta)_infinity|^2
        |((theta/A) exp(i phi);theta)_infinity|^4].

At theta=sqrt(r) the endpoint value is the removable limit. This derivation is restricted to c<=1; it does not silently use a continuous-only orthogonality formula at a parameter with discrete atoms.

## 5. The remaining two sharp line regimes

Let lambda=lambda_+=h+2t. If 0<theta<sqrt(r), put D=(A;theta)_infinity (a nonzero real product) and E=(theta/A;theta)_infinity>0. Then

    C_22(n) ~ B_< lambda^(n+1/2) n^(-3/2),
    B_< = q^2 pi_0 L^5 / [2 sqrt(pi) t^(3/2) D^2 E^4].     (S9)

At theta=sqrt(r), the power changes:

    C_22(n) ~ B_= lambda^(n-1/2) n^(-1/2),
    B_= = t^(3/2)(1-theta)/sqrt(pi).                        (S10)

Together with (S5), these give sharp leading decay in all fixed positive-density infinite-line priority ASEP regimes (theta=0 is covered by the original exact TASEP proof). They make no canonical-ring or optimal finite-size claim.

Proof of the edge constants: in the strict subcritical regime, the products in (S8) are continuous and nonzero at phi=0 except the first numerator factor. That numerator satisfies

    |(exp(2i phi);theta)_infinity|^2 ~ 4phi^2 L^2,

so w(phi)~K_< phi^2, with K_<=2q^2 pi_0 L^5/(pi D^2 E^4). At the threshold A theta=1, precisely the j=1 denominator factor vanishes at zero. Its squared modulus is ~phi^2; its remaining factors tend to ((1-A)L)^2. Also r=theta^2, pi_0=E=(theta^2;theta)_infinity=L/(1-theta), and (1-A)^2=(1-theta)^2/theta^2. Substituting these yields the finite positive endpoint density

    w(0)=2pq(1-theta)/pi.

In both regimes the density is bounded on [0,pi]; off the endpoint it is smooth. There are no other zeros of the denominator on that interval: A theta^j=1 can occur only at j=1 in the regime considered and then only phi=0. Since t>0 and lambda>0,

    h+2t cos(phi)=lambda-t phi^2+O(phi^4).

Any interval phi>=eta>0 has strictly smaller nonnegative spectral values, so its contribution is exponentially smaller. Near zero substitute phi=u/sqrt(n), use (spectral value/lambda)^(n-1)->exp(-t u^2/lambda), and bound it by exp(-c u^2) for all sufficiently large n. The density, or its quotient by phi^2 in the strict regime, is bounded near zero. Dominated convergence therefore uses respectively

    integral_0^infinity u^2 exp(-t u^2/lambda) du
      =sqrt(pi)/4 * (lambda/t)^(3/2),
    integral_0^infinity exp(-t u^2/lambda) du
      =sqrt(pi)/2 * (lambda/t)^(1/2).

Multiplying the endpoint density, the factor lambda^(n-1), and the Jacobian proves (S9)-(S10), including the stated powers of lambda. The endpoint at phi=pi cannot compete: its spectral value lambda_- is strictly less than lambda_+ and is nonnegative by the earlier positive-spectrum argument.

## 6. Closing color-density gap: extension to every fixed theta<1

Fix theta in (0,1), let a->a_0 in (0,1), b=a+delta with delta down to zero, and choose integers n such that n delta^2->s in (0,infinity). Put v=a_0(1-a_0), beta=1/(4v). Then the *general ASEP* line covariance has exactly the same leading scaling as the first attempt proved only for TASEP:

    C_22(n)/delta^2 -> sqrt(v)/pi *
       integral_0^infinity sqrt(z)/(beta+z) exp(-s(beta+z)) dz. (S11)

Thus at cumulative density a_0=1/2 the explicit limit is independent of the fixed reverse jump rate theta. This extends the line closing-gap result; it does not assert a ring result or uniformity as theta itself tends to one.

Full limiting argument: r->1 and A->1, so eventually A theta<1 and (S8) applies without a discrete nonstationary contribution. The identities q-p=delta and A=sqrt(q/p) give

    pi_0/delta -> L/v,
    (A-1)/delta -> 1/(2v),
    (1-lambda_+)/delta^2 -> beta,
    t->v.

The first follows by splitting the first factor (1-r) from (r;theta)_infinity and using 1-r=delta/q. Uniform convergence of the remaining infinite products justifies each product limit. Set phi=delta y in (S8), and write c_0=1/(2v). For each fixed y>=0 the product expansions yield

    w(delta y)/delta -> (2v/pi) y^2/(c_0^2+y^2),
    (h+2t cos(delta y))^(n-1) -> exp[-s(beta+v y^2)].

To check the first limit explicitly, split the first numerator factor and the first A-denominator factor: their squared moduli are asymptotic to 4delta^2 y^2 and delta^2(c_0^2+y^2). Their remaining product factors tend respectively to L^2 and L^2. The z-product tends to L, where z=theta/A, and pi_0/delta->L/v; all powers of L cancel in (S8). At y=0 both sides are zero and the same limit follows directly.

For domination choose a fixed A_max<1/theta with A<=A_max eventually. The A-denominator tail has modulus at least product_{j>=1}(1-A_max theta^j)>0, while the z-denominator has modulus at least L. The numerator tail is bounded above by product_{j>=1}(1+theta^j). Also

    |1-A exp(i phi)|^2=(A-1)^2+2A(1-cos(phi))
                       >=c(delta^2+phi^2), 0<=phi<=pi,

for a constant c>0, using (A-1)/delta->c_0 and 1-cos(phi)>=2phi^2/pi^2. Since pi_0<=C delta, these estimates give

    w(phi)<=C delta * phi^2/(delta^2+phi^2)<=C delta.

The spectral values are nonnegative and satisfy

    1-(h+2t cos(phi)) >= c(delta^2+phi^2),

because t stays bounded away from zero and (1-lambda_+)/delta^2->beta>0. For small delta, (n-1)delta^2>=s/2. Thus after phi=delta y, the integrand of C_22(n)/delta^2, extended by zero past y=pi/delta, is bounded by C exp(-c' y^2), integrable independently of delta. Dominated convergence gives

    (2v/pi) integral_0^infinity
      y^2/(c_0^2+y^2) exp[-s(beta+v y^2)] dy.

The substitution z=v y^2, with v c_0^2=beta, proves (S11). The theta=0 case is already proved independently in ATTEMPT.md. Neither proof covers theta depending on delta and approaching one.

## 7. The literal exclusive-color near-half regime

The source's wording can also be read literally as both exclusive color densities tending to one-half. Set epsilon=1-b down to zero and a->a_0 in (0,1), retaining a fixed theta in (0,1). Then p=a epsilon, q=(1-a)(1-epsilon), r=p/q->0, so theta>sqrt(r) eventually. Formula (S5) yields the following uniform-in-distance statement with the *actual* epsilon-dependent W_1 and lambda_1:

    0 <= C_22(n)/(W_1 lambda_1^(n-1))-1
       <= r(theta^(-2)-1)/(1-r/theta^2), for all n>=1.       (S12)

The right side is O(epsilon), at fixed theta,a_0. This follows by dividing the remainder estimate (S5) by its positive leading term, using R/lambda_1<=1, and simplifying (C_22(1)-W_1)/W_1. Thus the small-hole line covariance is asymptotically geometric uniformly in n when its exact rate is retained. For each fixed n>=1,

    C_22(n)/epsilon -> a_0(1-a_0)(1-theta)
        [a_0+(1-a_0)theta]^(n-1).                         (S13)

Indeed W_1/epsilon->a_0(1-a_0)(1-theta) and lambda_1->a_0+(1-a_0)theta, and (S12) controls the relative remainder. In particular at a_0=1/2, both exclusive color densities approach one-half and the limiting coefficient and rate are (1-theta)/4 and (1+theta)/2. This addresses the source's literal near-half reading on the infinite line; it makes no finite-ring or Brownian-horizon assertion.

For theta=0, (S13) also holds for each fixed n, interpreted with rate a_0 and coefficient a_0(1-a_0), but (S12) is not claimed. Proof: the exact original TASEP integral is a nonnegative measure of mass C_22(1)=delta p, supported on [h-2sqrt(pq),h+2sqrt(pq)]. As epsilon->0 this interval shrinks to {a_0}. Hence its normalized (n-1)st moment tends to a_0^(n-1) for each fixed n, while C_22(1)/epsilon->a_0(1-a_0). This proves the fixed-distance assertion without taking an invalid theta->0 limit of the bound-state formula.

## Remaining gap after this further attempt

The sharp fixed-density *line* exponent/prefactor gap and the fixed-theta *line* closing-density-gap limit are now resolved within this attempt, by (S5), (S9)-(S11). Both cumulative and literal exclusive-color near-half readings have precise line results, the latter in (S12)-(S13). The actual requested canonical growing-ring question remains unresolved in general ASEP: no quantitative ring-to-line transfer or pointwise conservation profile for theta>0 has been established, particularly when N delta^2 is of order one or distances are of order N. The previous TASEP ring transfer still imposes its restrictive sufficient condition. Simultaneously closing the density gap and approaching symmetric rates is also not covered. Approach 2 (cyclic bridge/excursion analysis) remains a specific route toward the principal finite-size gap. Overall verdict remains PARTIAL; no SOLVED_IN_LITERATURE claim is made.

## Hostile referee checklist and independent checks

1. **Infinite versus finite factorization.** Direct multiplication proves (S1)-(S2) for bounded operators; the finite-section verification explicitly ignores the last-row defect of (S2). No infinite-spectrum conclusion is based on finite eigenvalue plots.
2. **Kernel and missing modes.** Both kernels are solved coordinate by coordinate; the one-dimensional stationary kernel occurs precisely at A>1. Polar decomposition removes that kernel without assuming invertibility. Recursive removal terminates, and base spectral bounds plus compact-perturbation invariance account for the entire spectrum, excluding an unobserved slower eigenvalue.
3. **L2 eigenfunction domain and nonzero projection.** theta>sqrt(r) is exactly the needed condition r/theta^2<1 for the second moment of theta^(-Q). Its centered mean, norm, and occupation covariance are computed explicitly. W_1 is strictly positive under that condition, so operator gap and covariance decay are not incorrectly equated without an overlap calculation.
4. **Known-theorem hypotheses.** Only the checked real |c|<1 big q-Hermite orthogonality is imported. Its normalization is d_k after multiplying by L. At c=1 the endpoint extension has a dominated-convergence proof; at c>1 it is not used as a continuous-only probability law. The old PDF fraction layout was also inspected through text-span coordinates: the delta_mn numerator lies above the (theta^(n+1);theta)_infinity denominator in (3.18.2), confirming the normalization.
5. **Observable spectral weight and index.** Applying B to the centered observable removes the stationary component, and the divisor A+A^(-1)-2cos(phi) stays positive. The q^2 factor and n-1 power are inherited from the independent unused-service emission calculation, not guessed from a return probability.
6. **Edge phase and constants.** A theta<1 gives a quadratic zero in density, A theta=1 cancels exactly one quadratic denominator zero, and A theta>1 is treated by its bound state. The two Gaussian integrals fix the powers and prefactors. Limits are for fixed parameters and are not uniform across the mode threshold.
7. **Closing-gap domination.** theta is fixed, A eventually stays below a fixed 1/theta bound, and the infinite-product tails are controlled uniformly. An integrable Gaussian bound is proved after rescaling; height-process convergence is not substituted for occupation-covariance convergence. No interchange with a finite-ring limit is made.

`band_verify.py` independently integrates the product density and compares occupation covariance to principal Jacobi matrices at n=1,2,5,20. Errors are below 5e-17 in the tested cases; the spectral probability normalization is within 3.4e-12 of one, including the threshold. The normalized sharp-asymptotic ratios at n=1,000,000 are 0.99998436 (theta=0.2), 0.99866747 (theta=0.5), and 1.00001182 (the threshold theta=sqrt(2/7)). Near the threshold the n=1000 strict-subcritical ratio is only 0.5140: finite-distance use of the fixed-parameter asymptotic can be badly inaccurate, so no uniform threshold claim is inferred. The closing-gap covariance/delta^2 values for theta=0.2,0.6,0.9 approach the common limit 0.02512727083 at a_0=1/2,s=1, with slower convergence at theta=0.9. Raw results are in `band_checks.json`.

The four identities in `SpectralAlgebra.lean` formalize the two factorization diagonal calculations, the scaled first-mode gap identity, and the scaled remaining-spectral-mass identity. The single compiler invocation exited with code 0 and no diagnostics; the result and four theorem names are recorded in `second_lean_result.txt`. These algebraic steps are kernel-checked. The operator, probability, orthogonal-polynomial reduction, and limit proofs are handwritten; they are not claimed to be Lean-formalized.

`rare_holes_verify.py` passed nine independent principal-matrix cases with theta=0,0.3,0.7 and hole density 0.05,0.005,0.0005. It checks fixed-distance covariances against (S13), and at theta>0 checks the uniform relative bound (S12) at n=1,10,100,1000. Results are saved in `rare_holes_checks.json`; no finite-ring statement is inferred from them.

The supplemental attempt is complete with **VERDICT: PARTIAL**. The operator factorization, checked orthogonal-polynomial reduction, and their derived line theorems were pursued to a sharp classification and precise scaling limits. The unpursued cyclic-bridge approach is the next concrete avenue for the remaining ring question. No originality or full literature-solution claim is made.
