# Renyi containment

Every theorem below is marked PROVED, with numerical tests recorded in audit.json. OPEN means this work has no proof. CHECKED never means a proof in arbitrary dimension. Logarithms are base two except ln. Let v=Var(f), and omit zero spectral weights from weighted logarithms.

## 1. The quantity and the Renyi interpretation — PROVED

Write mu(S)=fhat(S)^2 and u(S)=sum_{U superset S}mu(U). Parseval for D_S f gives u(S)=E(D_S f)^2. Consequently

    WC = sum_S mu(S)u(S)
       = Pr_{S,U independent, law mu}[S subset U]
       = E_x sum_S fhat(S)^2 (D_S f(x))^2.

The empty derivative is f, so u(empty)=1, not mu(empty). This distinction matters near constants.

Here is an exact interpretation as a standard Renyi divergence. On pairs of sets put P(S,U)=mu(S)mu(U), E={S subset U}, and

    nu(S,U)=1_E mu(S)mu(U)/u(S).

Its S-marginal is mu, hence it is a probability measure. For 0<q<1,

    sum nu^(1-q) P^q = sum_S mu(S)u(S)^q,
    D_(1-q)(nu || P) = -(1/q) log sum_S mu(S)u(S)^q = L_q.

The endpoints are D_0(nu||P)=-log P(E)=L_1, and D_1(nu||P)=A. Thus the brief's interpolation is between support divergence and relative entropy for this particular coupling; it is not the usual Renyi entropy of mu. Set rho=P(.|E). Direct division of the densities gives

    A - L_1 = D(nu || rho) >= 0.

This also identifies the Jensen gap exactly. The S-marginal of rho is mu(S)u(S)/WC, whereas nu retains mu. Passing from event probability to containment entropy requires controlling this change of marginal.

Since u(S)>=mu(S), for q>0

    L_q <= H_(1+q)(mu) <= (1+1/q) H_infinity(mu).

The second inequality follows by keeping a maximum atom p in sum mu^(1+q): it is at least p^(1+q). In particular

    WC >= sum mu(S)^2 >= (max mu)^2,
    0 <= L_1 <= A <= H(mu).

Power-mean monotonicity gives L_q nonincreasing in q. Expanding exp(q ln u) on the finite positive spectral support gives L_q -> A as q decreases to zero, and more precisely

    L_q = A - (q ln2 / 2) Var_{S~mu}(log(1/u(S))) + O_f(q^2).

The error constant here depends on f. This expansion supplies no dimension-uniform interchange of limits or suprema.

## 2. Normalization and a false quadratic target — PROVED

The empty S term alone gives WC>=mu(empty)=1-v. Poincare gives v<=I. For v<=1/2,

    L_1 <= -log(1-v) <= v/((1-v)ln2) <= 2I/ln2.

Therefore the raw linear-in-I conjecture needs no division by variance; highly biased functions are already covered with a universal constant. Replacing I by I/v on its right side weakens that raw conjecture.

A more informative, separate conjecture removes the empty spectral atom on both draws. For v>0 define

    mu_plus(S)=mu(S)/v, S nonempty,
    WC_plus=Pr_{S,U independent, law mu_plus}[S subset U].

Then, exactly,

    WC = 1-v + v^2 WC_plus,
    kappa = E_mu_plus |S| = I/v.

The natural strengthened formulation is log(1/WC_plus)<=C kappa, or equivalently v log(1/WC_plus)<=C I. The raw and conditional conjectures are not asserted equivalent. The conditional version implies the raw one: for v>=1/2 use L_1<=2 log(1/v)+log(1/WC_plus), and for v<1/2 use the preceding atom bound. The converse is OPEN here. Conditioning changes the problem precisely in the regime where the raw statistic is easy.

For AND_n let p=2^-n. Its empty spectral weight is (1-2p)^2, each other weight is 4p^2, and I=2np. A fixed nonempty S has u(S)=4p 2^-|S|, hence

    WC(AND_n) = (1-2p)^2 + 16p^3[(3/2)^n-1],
    A(AND_n) = (n-2)4p(1-p)+2np.

Since (3/16)^n=o(p), WC=1-4p+o(p). It follows that

    L_1 = (4/ln2)p(1+o(1)),
    L_1/I^2 = 2^n/(n^2 ln2)(1+o(1)) -> infinity.

Thus the literal target L_1<=C I^2 for every Boolean f is false. It is valid after assuming I is bounded below, in particular for balanced f, as proved next. The regularized logarithm in section 4 is also necessary when stating an all-I version of the I log I target.

For this same family,

    WC_plus=(3^n-2^n)/(2^n-1)^2,
    kappa=n 2^(n-1)/(2^n-1),
    log(1/WC_plus)/kappa -> 2 log(4/3).

This conditional statistic remains nontrivial as the function becomes constant in probability.

## 3. A self-contained fixed-level route to a quadratic bound — PROVED

This rederives the selector argument in FEIB09/PROOFS.md, sections 2–3, which strengthens the exact-size A_r in FLOW by retaining the contribution of smaller spectral sets. That distinction is needed; simply summing the printed exact-level inequalities would lose another factor.

First prove a convenient, nonoptimal singleton constant. Put q_i=u({i}) and

    A_single = E_S max_{i in S} log(1/q_i),

with zero cost at empty S. Assign every nonempty S to a coordinate i(S) attaining the maximum, and let nu_i be the assigned mass. Set T=(ln2)A_single and b=(1-t)/(1+t), 0<t<1. Since D_i f is {0,+1,-1}-valued, hypercontractivity gives

    sum_{S contains i} t^(|S|-1)mu(S)
        <= ||D_i f||_(1+t)^2 = q_i^(1+b).

Jensen on the mass nu_i assigned to i, followed by this upper bound, yields

    (1+b)nu_i ln(1/q_i)
       <= nu_i ln(1/nu_i) + ln(1/t) sum_{i(S)=i} (|S|-1)mu(S).

The log-sum inequality with sum q_i=I and sum nu_i=v gives

    sum_i nu_i ln(1/nu_i)
       <= sum_i nu_i ln(1/q_i) + v ln(I/v).

Combining,

    b T <= v ln(I/v)+ln(1/t)(I-v).

For x=I/v>=1 the right side divided by I is ln(1/t)+(ln x-ln(1/t))/x, whose maximum is ln(1/t)+t/e. Therefore

    A_single <= [(ln(1/t)+t/e)/(b ln2)] I.

At t=1/3 the coefficient is 2(ln3+1/(3e))/ln2<4. The constant calculation is in proof_constants.json. Constants cause no difficulty: if v=0, A_single=I=0.

For an integer k>=1 choose R(S) subset S, |R(S)|=min(k,|S|), minimizing u(R). Set R(empty)=empty and denote its law by eta. The event R(S)=R implies S contains R, so eta(R)<=u(R). Consequently

    E log(1/u(R(S))) <= H(eta).

Use the reference probability pi(R)=product_{i in R}q_i / product_i(1+q_i) on all subsets, ignoring zero-influence coordinates. Gibbs' inequality gives

    H(eta) <= E sum_{i in R(S)}log(1/q_i)+sum_i log(1+q_i)
           <= k A_single+I/ln2
           <= (4k+1/ln2)I.

For every |S|<=k the selected R(S) equals S. Thus

    T_k = E[1_{|S|<=k} log(1/u(S))] <= (4k+1/ln2)I.

Take k=ceil(2I) and p0=Pr[|S|<=k]>=1/2. Jensen on this submeasure gives

    WC >= p0 2^(-T_k/p0) >= (1/2)2^(-2T_k),
    L_1 <= 1+2(4ceil(2I)+1/ln2)I.

When I>=1/2, ceil(2I)<=2I+1 and 1<=2I, so

    L_1 <= 16I^2+(10+2/ln2)I <= 16I^2+13I.

When I<1/2 the empty-atom bound proves this last inequality as well. Therefore, globally,

    L_1 <= 16I^2+13I.

For balanced f, I>=v=1, so L_1<=29I^2. Neither constant is claimed sharp. The independently checked stronger singleton constant 3.520226 in the input improves these numbers, but is unnecessary for the stated conclusion.

## 4. The known near-linear bound transfers to WC — PROVED using a read theorem

[Kelman–Kindler–Lifshitz–Minzer–Safra, Theorem 1.1 and section 7.2](https://www.ias.edu/sites/default/files/math/csdm/19-20/KelmanKiLiMiSa-Towards.pdf) gives a nonempty Fourier atom, in our sign-valued convention, of size

    mu(S) >= v 2^(-K kappa log(1+kappa)), kappa=I/v,

for an absolute K. Constants absorb the square of the amplitude and the harmless change between their indicator and our sign convention. No explicit numerical K is claimed.

For v>=1/2 this atom and WC>=mu(S)^2 imply

    L_1 <= 2 log(1/v)+2K kappa log(1+kappa)
         <= 2+4K I log(1+2I)
         = O(I log(2+I)).

Here I>=1/2, so the additive constant is absorbed. For v<1/2 the atom bound of section 2 already gives O(I). Hence the following holds for every Boolean f:

    L_1 <= C I log(2+I).

For I>=2 this is O(I log I), the target's usual asymptotic meaning. The form with log(2+I) is the all-I statement proved here. This is a corollary of known work, not a new solution of FMEI or FEI. It is stronger than section 3 at large I. For every fixed q>0 the same argument, using L_q<=(1+1/q)H_infinity, gives O((1+1/q) I log(2+I)). This dependence is not uniform as q decreases to zero.

For the conditional normalization, the same nonempty atom gives

    log(1/WC_plus) <= 2K kappa log(1+kappa).

OPEN: deleting the logarithmic factor in general, or bounding A by C I. The cited theorem gives no such assertion.

## 5. Classes with a linear WC bound — PROVED

Monotone and unate, with an explicit elementary constant. For monotone f, after choosing signs, |fhat({i})|=q_i. Let q*=max_i q_i. Every nonempty S has max_{i in S}log(1/q_i)>=log(1/q*), so section 3 implies v log(1/q*)<=4I. The singleton contribution to WC is mu({i})u({i})=q_i^3. Therefore

    L_1 <= 3log(1/q*) <= 12I/v.

For v>=1/2 this gives L_1<=24I. For v<1/2 the empty atom gives L_1<=2I/ln2<=24I. Thus WC>=2^(-24I) for every monotone f. Input negations preserve Fourier squares, so this holds for every unate f. This derives WC directly from the singleton theorem; the published FMEI implication is an alternative route. The same singleton term after removing the empty atom gives

    WC_plus >= (q*)^3/v^2,
    log(1/WC_plus) <=12I/v+2log v <=12 kappa.

The constant 24 is only a convenient certificate.

Symmetric. [O'Donnell–Wright–Zhou, Theorem 1](https://www.cs.cmu.edu/~odonnell/papers/fei.pdf) proves H<=12.04I, hence L_q<=12.04I for the entire interpolation, including q=0. The newer symmetric constant found by the brain is not used: this report has not audited its proof. Conditioning gives H(mu_plus)=(H(mu)-h(v))/v<=12.04kappa, so log(1/WC_plus)<=12.04kappa.

Read-once. [Chakraborty–Kulkarni–Lokam–Saurabh, Theorem 5.11 and Remark 5.1](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/) proves H<=10I for read-once AND/OR/XOR/NOT formulas. Thus L_q<=10I, and the conditional bound has constant 10. [O'Donnell–Tan](https://arxiv.org/pdf/1304.1347) proves FEI for read-once formulas over any fixed bounded-arity gate set, so WC follows with the corresponding gate-dependent constant. Read-once with an unrestricted arbitrary gate is all Boolean functions and is OPEN.

Low real degree, by granularity. Let the real multilinear degree be at most d>=1. The {0,1}-valued function (1-f)/2, expressed in {0,1} input coordinates, has integer multilinear coefficients by finite differences. Its degree remains at most d under affine changes of variables. Substituting z_i=(1-x_i)/2 shows that every Fourier coefficient of f is a multiple of 2^(1-d). The constant coefficient includes the integer 1, which is also a multiple of 2^(1-d). Thus every nonzero mu(S)>=2^(2-2d). For nonempty S, u(S)>=mu(S), and the empty term in A is zero. Consequently

    L_q <= A <= (2d-2)v <= (2d-2)I, 0<=q<=1.

For constants the cost is zero. This gives a constant depending on fixed real degree d, not an absolute constant uniform in d; the latter would include every Boolean function. It says nothing about a fixed degree over F_2. For the conditional statistic the collision probability is at least the smallest nonzero conditional atom, yielding log(1/WC_plus)<=2d-2+log v<=2d-2.

## 6. Tensor products, restrictions, and the remaining gap — PROVED identities; OPEN general bound

For Boolean functions f,g on disjoint variables and h(x,y)=f(x)g(y), the spectral law is mu_h(S,T)=mu_f(S)mu_g(T), and u_h(S,T)=u_f(S)u_g(T). Hence

    WC_q(h)=WC_q(f)WC_q(g),
    L_q(h)=L_q(f)+L_q(g),
    I(h)=I(f)+I(g), H(h)=H(f)+H(g), A(h)=A(f)+A(g).

These include both endpoints. Tensor powers remove a universal additive overhead from a hypothetical bound L_1<=CI+K, by dividing the bound for f^tensor(m) by m. They do not remove the extra I in a quadratic bound: that operation gives L_1(f)<=Cm I(f)^2. Nor does additivity change q=1 into q=0. The Renyi/Jensen gap remains additive under products.

There is also an exact recursion, valid for real functions with the unnormalized quartic definition C(g)=sum ghat(S)^2 sum_{U superset S}ghat(U)^2. Write f=a+x_i d. With alpha=ahat^2, beta=dhat^2,

    C(f)=C(a)+C(d)+sum_T alpha(T)up_beta(T).

This follows by partitioning spectral sets according to whether they contain i. It is numerically checked on every four-variable function in audit.json. Although a and d have disjoint pointwise supports for Boolean f, they are {0,+1,-1}-valued rather than Boolean. Applying the Boolean conjecture to them is unjustified. The cross term is not determined by their norms or their own containment probabilities.

The actual Boolean restrictions f_+=a+d and f_-=a-d have spectra (ahat+dhat)^2 and (ahat-dhat)^2, which contain signed interference. The identity in section 1 expresses WC using their top coefficients on a random spectral coordinate set, but neither this identity nor averaging restrictions supplies a closed induction. audit.json records an explicit four-variable failure of the naive zero-overhead inequality L(f)<=average L(f restricted to i).

There is a stronger obstruction to a common induction rule. For address_k, restriction of any data variable to either sign gives

    WC(f restricted to data_j=b)=(2-2^-k)WC(f),
    Inf_data_j(f)=2^-k.

To see this, the original Fourier support consists of 2^k disjoint classes, one for each data bit, each class containing all address subsets with weight 4^-k. The restriction removes one data bit from its class, turning that class into address-only sets. All old containment pairs persist, contributing WC(f). Newly allowed pairs have S in this changed class and U in any of the other 2^k-1 classes. Each ordered pair of classes contributes 3^k16^-k, so the increase is (2^k-1)3^k16^-k=(1-2^-k)WC(f). The sign b changes coefficients but not these squares.

It follows that the necessary constant in the local rule

    L_1(f) <= E_b L_1(f restricted to i=b)+C Inf_i(f)

is at least 2^k log(2-2^-k), which diverges. A universally quantified local rule of this form is therefore false. An address-coordinate restriction has gap log(8/3), since it reduces k by one. Averaging over all n=k+2^k coordinates gives the necessary constant for the uniform-coordinate induction

    [k log(8/3)+2^k log(2-2^-k)]/(1+k/2),

which also diverges. Thus the analogous uniform-average rule with charge C I/n is false. restriction_address.json checks the exact formulas on full truth tables at k=1,2,3 and evaluates the obstruction at larger k. An induction allowed to choose coordinates in a more sophisticated way remains OPEN; these counterexamples do not disprove the WC conjecture.

The elementary second-moment route gives collision probability sum mu^2 and therefore order-two Fourier entropy. Its available general bound is the near-linear one in section 4, with the same missing logarithm. A new lower bound on this random restriction statistic would be needed to prove the general linear statement. No such bound was obtained here.

## 7. Exact family formulas and lower bounds on a universal constant — PROVED

Bent f on even n has mu uniform on all subsets, so u(S)=2^-|S|, I=n/2, H=n, A=n/2, and

    WC_q=[(1+2^-q)/2]^(n/q),
    L_1/I=2log(4/3).

Address/MUX with k address bits and 2^k independent data bits is balanced. Its nonzero coefficients, each of square 4^-k, occur at one data bit together with any subset R of address bits. Thus u(S)=2^(-k-|R|), and

    I=1+k/2, H=2k, A=3k/2,
    WC=(3/8)^k,
    L_q=k[1+(1/q)log(2/(1+2^-q))].

The q=0 value is the continuous limit. Therefore every universal raw WC constant is at least 2log(8/3), and every universal containment constant is at least 3. Also, for every k>=1,

    L_1/(I-1)=2log(8/3), A/(I-1)=3.

For tribes with t disjoint width-w AND terms, put p=2^-w, d=1-p, z=d^t and v=4z(1-z). A nonempty spectral S meeting k tribes, with r=|S|, has

    mu(S)=4p^(2k)d^(2(t-k)),
    u(S)=4p^k 2^-r d^(t-k).

Summing independently over blocks gives, for q>0,

    M_q=E_mu u(S)^q
       =(2z-1)^2+4^(1+q){[d^(2+q)+p^(2+q)((1+2^-q)^w-1)]^t-d^((2+q)t)},
    WC_q=M_q^(1/q).

Put K1=4ztp. Then I=K1 w/(2d), and summing k and r gives

    H=-(2z-1)^2 log((2z-1)^2)-2v+(2w+2log d)K1-2t(log d)v,
    A=-2v+(w+w/(2d)+log d)K1-t(log d)v.

Choose t nearest to ln(1/2)/ln d. Then z=1/2+O(p), I=w ln2+o(w), and

    WC=2ln2 (3/8)^w(1+o(1)).

Indeed at q=1 the bracket is d^3+c_w with c_w=(3/16)^w-(1/8)^w; tc_w tends to zero, so its t-th power minus d^(3t) is d^(3t)t c_w/d^3(1+o(1)). The empty atom is O(p^2)=o((3/8)^w). This gives

    L_1/I -> log(8/3)/ln2,
    A/I ->3, H/I ->4.

analytic_families.py evaluates these formulas with high precision. Its formulas for odd majority use c_(2j+1)=(-1)^j [binom(m,j)/binom(2m,2j)] binom(2m,m)/2^(2m), n=2m+1, then sum u_s=sum_{l>=s}binom(n-s,l-s)c_l^2. Numerical checks through n=255 are CHECKED, not a new majority asymptotic theorem.

OPEN: the global extremizers of WC and the optimal universal constant. The finite census and these families do not resolve them.
