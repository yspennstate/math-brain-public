# FEIB12 proofs and limits

Logs in the functionals are base 2. I is total influence, V=Var(f), and all sums omit zero spectral masses. A theorem marked PROVED below has its proof here. CHECKED scopes and files are listed in RESULTS.md. OPEN means no general proof was obtained. None of the finite censuses proves FEI.

## 1. Noise identities and the equivalence

PROVED. Use characters chi_S(x)=product_{i in S} x_i and the uniform measure on {-1,1}^n. Then

    D_S f = sum_{U superset S} fhat(U) chi_{U-S},
    F_S(u) := <D_S f,T_u D_S f>
            = sum_{U superset S} mu(U) u^{|U-S|}.

This is orthogonality and T_u chi_V=u^{|V|}chi_V. In particular F_S(0)=mu(S) and F_S(1)=up(S). On the support of mu these numbers are positive. Every coefficient of F_S is nonnegative, so F_S increases and Phi(u)=sum mu(S)log(1/F_S(u)) decreases. The endpoint equalities are Phi(0)=H and Phi(1)=A. Also

    Phi(0)-Phi(1)=sum_S mu(S)log(up(S)/mu(S))=B.

For rho=1-u>0 define tau_rho(S)=rho^{|S|} F_S(u). Sum in the opposite order:

    sum_S tau_rho(S)
      = sum_U mu(U) sum_{S subset U} rho^{|S|}u^{|U-S|}
      = sum_U mu(U)(rho+u)^{|U|}=1.

Its probabilistic interpretation is a mu-sample U with each element retained independently with probability rho. Equivalently, fixing the other coordinates uniformly and retaining a rho-random set of live coordinates gives this averaged Fourier law: each surviving coefficient's mean square is the sum of mu over its compatible supersets. This also proves the random-restriction interpretation without assuming it.

Relative entropy is nonnegative. Therefore

    0 <= D(mu||tau_rho)
       = Phi(u)+I log(1/(1-u))-H.

For each fixed 0<=u<1, Phi(u)<=H shows that FEI implies Phi(u)<=C I. Conversely Phi(u)<=C_u I implies

    H <= [C_u+log(1/(1-u))] I.

The additive constant depends on the fixed u. At u=1 this inference is unavailable. Constants have all four functionals zero; they require no division by I.

CHECKED: check.py, check_all4.json and check_sample6.json verify the endpoints, monotonicity, Gibbs inequality, thinning normalization, and F_S by directly transforming each actual derivative. The support convention is explicit; an endpoint check alone would be weaker.

## 2. Replacement for the failed median shortcut

For up(S)>0 let q_S(k)=Pr[|U-S|=k | U contains S] under the original spectral law mu. Write w_S=q_S(0)=mu(S)/up(S), m_S=E_q k and L=log_2(1/u), for 0<u<=1.

PROVED counterexample to the proposed uncorrected median inequality. Take n=4, f with negative truth-table bits 0xaaa9 and S={1}, where set {1} has bit mask 1. Its derivative is +1 at seven assignments and -1 at one, up(S)=1, and

    (q(0),q(1),q(2),q(3))=(9,3,3,1)/16.

Its unique median is zero. But F_S(1/2)/up(S)=91/128<1=(1/2)^0. Thus even choosing an upper median cannot fix this example. unique_median_counterexample.json checks the truth table and fractions. The larger failure in check_all4.json uses a distribution with exactly half its mass at zero, so the unique-median example is the decisive one.

PROVED corrected quantile bound. If q([0,r])>=eta>0, then

    F_S(u)/up(S)=E_q u^k >= eta u^r.

Consequently

    Phi(u)-A <= E_mu min_r {r L + log_2(1/q_S([0,r]))}.       (Q)

Zero cumulative probabilities are excluded from the minimum. A median gives the valid, weaker bound 1+rL. That extra 1 cannot generally be removed. This bound retains a nonzero quantile mass even for a very long upper tail.

PROVED atom-plus-mean bound. If w<1, Jensen applied only to k>0 gives

    E_q u^k >= w+(1-w)u^{m/(1-w)}.

For w=1 take the right side to be one. Thus

    Phi(u)-A <= R(u)
      := E_mu log_2[1/(w+(1-w)u^{m/(1-w)})]
      <= min{B, L E_nu |U-S|}.                            (AM)

The first comparison follows because the denominator is at least w. For the second, apply Jensen once more to the two-point variable taking 0 with probability w and m/(1-w) otherwise; its mean is m. This proves the displayed simultaneous improvement over the old mean bound. It is strict when 0<u<1, 0<w<1, and m>0. It is not a universal O(I) theorem: R still depends on the unknown cancellation through w.

The bound nevertheless removes the majority defect of the mean estimate: R<=B<=3.459354 I for symmetric Boolean f, by the supplied final FEIB02 theorem, whereas the old mean estimate divided by I grows on majority. No new proof of the symmetric B theorem is claimed here. families.json compares both sides through majority_513. The quantile bound is also at most B, by choosing r=0. In the saved majority rows it is stronger than (AM); no general ordering between the two new bounds is claimed.

CHECKED before this proof was written: check.py tested the quantile, corrected median and (AM) inequalities on every four-variable function and 12,000 mixed six-variable draws. The raw median claim failed there. Families were then tested separately.

## 3. What the other three routes actually give

PROVED exact noisy sign decomposition. Put h=|g| and F^abs(u)=<h,T_u h>. The kernel of T_u is nonnegative, so for u>=0,

    0 < <g,T_u g> <= <|g|,T_u |g|>

whenever g has a nonzero mean (which is the only case weighted by mu). Therefore

    log(up/F_g(u))
      = log(up/F^abs(u)) + log(F^abs(u)/F_g(u)).           (SC)

At u=0 the last term is 2 log(alpha/|E g|); at u=1 it is zero. Its mu-average at zero is 2 Gamma, including S=empty.

CHECKED: the standard reverse-hypercontractive candidate for nonnegative h,

    <h,T_u h> >= ||h||_{1-u}^2,

was tested at u=1/2, where the right side is (E sqrt(h))^4, on every derivative of every four-variable f and the six-variable sample. No violation was found. We do not use that external inequality as a new proved result here. Even granting it, (SC) leaves the second, signed ratio unbounded by any proved universal CI in this work. Nonnegative noise stability alone does not close the cancellation problem.

PROVED derivative identity (route c). For 0<u<=1 let h_S=T_sqrt(u) g_S. Orthogonality gives

    ||h_S||_2^2=F_S(u),
    I(h_S)=sum_{U superset S}|U-S|mu(U)u^{|U-S|}.

Differentiate the finite polynomial:

    -Phi'(u) = (1/(u ln 2)) E_mu [I(h_S)/||h_S||_2^2],
    Phi(u)-A = (1/ln 2) int_u^1 E_mu [I(h_S)/||h_S||_2^2] dv/v.   (DI)

Here h_S in the integral uses sqrt(v). Tilting q by u^k gives exactly the normalized influence in (DI). In t=ln(1/u), each log E_q exp(-tk) is convex, with second derivative the tilted variance. Integrating or replacing the tilted mean by the untilted mean recovers the old bound; a new uniform integral estimate is still OPEN. check.py compares (DI) to centered finite differences at u=1/2.

PROVED coupling identities (route d). Define nu(S,U)=mu(S)mu(U)1[S subset U]/up(S), w(S)=mu(S)/up(S), Z_U=sum_{S subset U}w(S). Summing first over U gives the S marginal mu and total mass one; summing first over S gives the U marginal mu(U)Z_U. In particular E_mu Z=1. On the joint support,

    Pr_nu[S | U]=w(S)/Z_U,
    H_nu(S|U)=E_nu log(1/w(S))+E_nu log Z_U
              =B+D(mu Z||mu).

Hence B<=H_nu(S|U)<=H(mu). The upper bound is the ordinary fact that conditioning reduces entropy (equivalently, nonnegativity of mutual information).

A bound H_nu(S|U)<=C I is itself equivalent, up to constants, to FEI. One direction is H_nu(S|U)<=H. In the other direction, Boolean granularity gives H<=2B+2I-2V: for nonempty S, |fhat(S)|<=2^{|S|-1}up(S), whence log(1/up(S))<=2(|S|-1)+log(up(S)/mu(S)); summing gives A<=B+2I-2V, with the empty-set A term zero and its B term nonnegative. Thus

    H <= (2C+2)I-2V.

This route is a reformulation, not an entropy bound already proved. The coarse estimate H(S|U)<=E_nu |U| retains the majority problem. CHECKED conditional entropies appear in both census_audit.json and families.json.

## 4. Classes and their limitations

PROVED monotone/unate first-level statement. If f is monotone increasing, D_i f takes values 0 and 1, so fhat({i})=E D_i f=Inf_i. For a decreasing coordinate the sign changes; input negation reduces every unate function to the increasing case. Its singleton Gamma contributions are therefore zero. This does not include the empty set.

At higher levels the equality need not survive. For any Boolean f and i in S, derivative contraction |(a-b)/2|<=(|a|+|b|)/2 implies

    alpha(S)<=alpha({i})=Inf_i.

The bound survives but fixed sign does not. Majority_5 is both monotone and a linear threshold function, yet active third derivatives have alpha=3/8 and |fhat|=1/8; their Gamma contributions are positive. There are ten such triples. Their total is (10/64)log_2(3), while the fifth derivative contributes zero. No dimension-independent bound Gamma<=CI, B<=CI, or Phi(1/2)<=CI for all monotone/unate functions or all linear threshold functions is proved here. Those requested universal class results remain OPEN in this work. The degree-dependent bound below of course applies to their finite-dimensional members.

PROVED consequence of FEIB02's supplied theorem. Every symmetric Boolean f satisfies

    B <= 3.459354 I,    Gamma <= (8/5)I.

These are inherited results, not new claims from a second census. FEIB02/PROOFS.md section “Final B constant from the unsimplified envelope” proves the sharper B coefficient; its REPORT.md and B_final_constant_certificate.json agree. Since 0<=Phi(u)-A<=B, the same coefficient controls every symmetric noise cancellation cost. Combining with the granularity inequality in section 3 also gives H<=8.918708 I-2V, a weaker FEI corollary than the existing symmetric FEI bound. We do not claim an improvement to that literature bound.

PROVED one-sign nonempty derivatives. Suppose every D_S f with S nonempty has a fixed sign (the sign may depend on S). At each active nonempty S, alpha(S)=|fhat(S)|. With b=E f,

    Gamma(f)=b^2 log_2(1/|b|)
            <= (1-b^2)/(2 ln 2) <= I/(2 ln 2).          (OS)

At b=0 take the continuous value zero. To prove the first inequality, set x=b^2 and use -x ln x<=1-x; the second is Poincare, V=sum_{S nonempty}mu(S)<=sum_S |S|mu(S)=I. Thus C=1/(2 ln 2) is explicit. No sharpness assertion is made for this coefficient. If “all derivatives” includes D_empty=f, the only Boolean functions in the class are constants.

PROVED read-once AND/OR/NOT formulas satisfy the hypothesis of (OS). Use 0/1 output notation. At an AND root the output is F_1 F_2 on disjoint variables. A nonempty mixed derivative factors into the derivatives of the children it touches, times the unchanged 0/1 child if it touches only one. At an OR root write 1-(1-F_1)(1-F_2); the same factorization has a fixed extra minus sign if both children are touched. Negation changes the global sign. Starting with literals, induction shows every nonempty mixed derivative has a fixed sign. Rescaling 0/1 to +/-1 preserves this property. Hence Gamma<=I/(2 ln 2) for this read-once class, and Gamma is exactly the bias term above. This argument does not cover unrestricted read-once gates such as XOR; parity has sign-changing first derivatives. It does not derive a B or Phi bound from Gamma alone.

PROVED degree-d bound with explicit dependence on d. Let d>=1 be the degree of a nonconstant Boolean f. In 0/1 coordinates its multilinear coefficients on nonempty monomials are even integers: each is an alternating sum of +/-1 values with equally many plus and minus signs. Degree remains d under x_i=1-2y_i. Substituting y_i=(1-x_i)/2 shows every nonempty Fourier coefficient is a multiple of 2^{1-d}. In particular, any nonzero one has squared magnitude at least 2^{2-2d}. Thus

    H_nonempty <= 2(d-1)V,
    H_empty = -(1-V)log_2(1-V) <= V/ln 2,
    H <= [2(d-1)+1/ln 2]I.                              (DG)

The empty-set bound is again -x ln x<=1-x. Since B<=H and Phi(u)<=H, (DG) bounds both with the displayed C(d); Cauchy-Schwarz alpha(S)<=sqrt(up(S)) gives Gamma<=B/2 and hence

    Gamma <= [d-1+1/(2 ln 2)] I.

For degree 0 all functionals vanish; for degree 1 a nonconstant Boolean f is a signed dictator and H=B=Gamma=Phi=0. This is an elementary O(d) class bound, not a constant uniform in unbounded d. class_checks.py tests (OS), (DG), lattice granularity and the first/higher-level statements on all four-variable functions and 3,000 mixed six-variable draws.

## 5. Recursion, a finite LP, and a cone obstruction

PROVED real-function recursion. For g=a+x_i d, coefficients not containing i are ahat(T), and those containing i are dhat(T). For T not containing i,

    up_g(T)=up_a(T)+up_d(T),    up_g(T+i)=up_d(T).

Separate the two types of terms in B(g)=sum mu log(up/mu), and subtract B(a)+B(d). This gives

    B(g)=B(a)+B(d)+J_i(g),
    J_i(g)=sum_T ahat(T)^2 log_2(1+up_d(T)/up_a(T)).      (REC)

Zero ahat terms contribute zero; if ahat(T) is nonzero then up_a(T)>0. No normalization to ||g||_2=1 is needed. Also

    I(g)=I(a)+I(d)+||d||_2^2.

A local induction certificate B(g)<=c I(g)+G(g), with G zero on constants, therefore follows from

    J_i(g)<=c||d||_2^2+G(g)-G(a)-G(d)                   (LOC)

at every node used by the induction. Descendants are real functions even when the root is Boolean. Checking only Boolean-root inequalities is not an induction certificate.

The request for the “largest c” has no finite optimum: if (LOC) holds for c, it also holds for every larger c. The useful problem minimizes c (or the resulting coefficient after bounding G at Boolean roots) in a specified family. “Best G” without a function class is also unspecified; G=B is a tautological certificate and controls the root only if the desired bound is already known.

CHECKED finite LP family. Put M=E g^2, alpha=E|g|, p=Pr[g!=0], b=E g, and use zero for every feature when M=0. The first five features are

    Ent(g^2)=E g^2 log_2(g^2/M),
    M-alpha^2,
    M log_2(M/alpha^2),
    M log_2(1/p),
    M log_2(||g||_infinity^2/M).

They are 2-homogeneous, nonnegative, and vanish at Boolean roots and constant leaves. The optional sixth feature b^2 log_2(M/b^2) vanishes at constants and is <=V/ln 2 at a Boolean root. We allow signed or nonnegative coefficients in explicitly separate runs. The last coefficient is nonnegative, and its root price divided by ln 2 is included in the objective.

induction_lp.py recursively generates every E/D descendant and every remaining coordinate of the 222 four-variable NPN representatives, deduplicating exact dyadic truth vectors. Sign flips and input permutations preserve all features and carry E/D descendants to globally signed, permuted descendants, so the quotient covers all four-variable Boolean roots. The LP imposes (LOC) on every generated node, rather than only at the root. The dataset, coefficients, residuals and numerical duals are saved. All fitted families fail on fresh five- and six-variable descendants; audit_lp.py records explicit witness vectors. These failures block extrapolating any fitted G to all dimensions.

PROVED obstruction for the entire nonnegative cone of the first five features. No fixed finite nonnegative combination of these features can make (LOC) hold on every descendant of Boolean roots with any finite universal c.

First use an AND_n root. Its D-child is a signed indicator of a subcube of density p=2^{-(n-1)}. For that child M=p; each of features 1,3,4,5 equals p log_2(1/p)=p(n-1). Every feature of both children is nonnegative, and all features of the Boolean root are zero. Since J>=0, (LOC) forces

    c >= (theta_1+theta_3+theta_4+theta_5)(n-1).

A finite universal c therefore forces those four coefficients to be zero. Only G=theta_2(M-alpha^2) remains.

Now let N=4^r, let y have N coordinates, and use one extra coordinate x. Define

    a(y)=(1/(2N))sum_j y_j,
    d(y)=(1/(2 sqrt(N))) product_j y_j,
    g(x,y)=a(y)+x d(y).

These are dyadic, |g|<=1/2+1/(2 sqrt(N))<=1, and

    ||a||_2^2=||d||_2^2=1/(4N),     M(g)=2||d||_2^2.

At each of the N singleton coefficients of a, up_d equals 1/(4N), while up_a=1/(4N^2). Therefore

    J/||d||_2^2=log_2(N+1).

Because 0<=M-alpha^2<=M, the right-hand potential difference is at most 2 theta_2 ||d||_2^2. Hence (LOC) would require log_2(N+1)<=c+2 theta_2 for arbitrarily large N, a contradiction.

Finally these bounded dyadic g really are descendants of Boolean roots, not arbitrary inadmissible real functions. If g takes values in 2^{-k} Z intersect [-1,1], introduce k+1 fresh bits and, at each original input, choose a Boolean truth table with exactly 2^k(1+g) positive entries. Averaging over those bits gives g. Thus a coordinate-order-independent certificate on all Boolean E/D trees must apply to these nodes. This completes the obstruction. audit_lp.py checks the explicit spectral calculation at N=4 and records the growing exact-form ratios at larger N.

OPEN: a universal signed combination in this or a larger controlled family, a general CI estimate for the recursion, and an optimal general induction potential. The cone obstruction is limited to the stated nonnegative family and (LOC); it does not rule out induction with child slacks, selected coordinate orders, or richer potentials.
