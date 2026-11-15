# Symmetric containment, dispersion and cancellation

Final direct bounds: B<=(3459354/1000000)I and Gamma<=(8/5)I for every symmetric Boolean function. The small-dimensional part is certified by exact integers; the remaining dimensions use the analytic proofs below. The inherited bound A<=3.3252155I-Var additionally uses the supplied FEI benchmark.

Logs in the definitions are base 2. In the proof of the bounds, ln denotes the natural logarithm. A value vector f_0,...,f_n consists of signs; t is the number of negative input coordinates. At zero spectral mass all summands are defined to be zero. Constant functions have all functionals and influence zero and need no ratios. Balanced functions with I=1 are dictators (in the symmetric class only n=1), so their ratios over I-1 are undefined.

## Exact closed forms

For 0<=k<=n and 0<=t<=n-k put

    d_k(t) = sum_{r=0}^k (-1)^r C(k,r) f_{t+r},
    F_k = sum_t C(n-k,t) d_k(t),
    L_k = sum_t C(n-k,t) |d_k(t)|,
    Q_k = sum_t C(n-k,t) d_k(t)^2,
    N_k = sum_t C(n-k,t) 1[d_k(t)!=0].

All five quantities are integers. The recursion d_0(t)=f_t and d_{k+1}(t)=d_k(t)-d_k(t+1) avoids cancellation in floating-point arithmetic. If |S|=k and the outside assignment has weight t, then

    c_S(z)=2^{-k} d_k(t),
    fhat(S)=2^{-n} F_k,
    abs1(S)=2^{-n} L_k,
    up(S)=2^{-(n+k)} Q_k,
    p(S)=2^{-(n-k)} N_k,
    W_k=C(n,k) F_k^2 / 2^{2n}.

The first identity follows by grouping the 2^k free assignments by their weight. The others follow by averaging over the C(n-k,t) outside assignments of each weight. In particular

    Gamma = sum_{k:F_k!=0} W_k log_2(L_k/|F_k|),
    P     = sum_{k:F_k!=0} W_k [(n-k)-log_2 N_k],
    A     = sum_{k:F_k!=0} W_k [(n+k)-log_2 Q_k],
    B     = sum_{k:F_k!=0} W_k [(n-k)+log_2 Q_k-2 log_2 |F_k|].

These include k=0: Q_0=L_0=N_0=2^n, so A_0=P_0=0 and Gamma_0=B_0/2. The equivalent level-weight forms of A and B in the brief follow from

    C(n,k) up_k = sum_{j>=k} W_j C(j,k).

One standard Krawtchouk form is

    F_k=sum_{w=0}^n f_w sum_r (-1)^r C(k,r) C(n-k,w-r).

The inner sum is the coefficient of x^w in (1-x)^k(1+x)^{n-k}. These identities specify the sign convention completely.

## A bound for the extra dispersion caused by the level weights

Use D for within-level entropy, D=sum_k W_k log_2 C(n,k). This is called B in the earlier symmetric-FEI paper; it is different from the B in this brief. Define u_k=up(S) for |S|=k. For every probability vector W, whether or not it is a Boolean spectrum, and every a>0,

    (B-D) ln 2 <= [a+1/(n(exp(a)-1))] I.                 (1)

To prove it, write

    (B-D) ln 2 = sum_k W_k ln(u_k/W_k).

Apply ln x<=x-1 to x=exp(-ak)u_k/W_k on the support of W. Adding the omitted nonnegative terms gives

    (B-D) ln 2 <= aI + sum_k exp(-ak)u_k -1.

Since u_0=1, the last two terms are

    E_{J~W} sum_{k=1}^J exp(-ak) C(J,k)/C(n,k).

For k<=J, the product formula gives C(J,k)/C(n,k)<=(J/n)^k. A geometric sum, extended to infinity, is therefore at most

    (J/n)/(exp(a)-J/n) <= J/[n(exp(a)-1)].

Average over J to prove (1). The best a is

    a_n=2 asinh(1/(2 sqrt(n))).

Put kappa_n=[a_n+1/(n(exp(a_n)-1))]/ln 2. In natural units the useful elementary upper bound is

    kappa_n ln 2 <= 2/sqrt(n)-1/(2n)+1/(8 n^{3/2}).       (2)

Indeed a_n<=1/sqrt(n), and the second term at this a is exactly sqrt(1+1/(4n))/sqrt(n)-1/(2n); use sqrt(1+x)<=1+x/2.

## The alternating derivative improves the within-level bound

For a nonconstant symmetric Boolean f on n>=2 coordinates, let N=n-1 and g=D_n f. At consecutive changing weights the nonzero values of g alternate between +1 and -1. In particular g(x)g(x with coordinate i flipped)<=0 for every x and i. Hence

    I(g) >= (N/2)||g||_2^2.

The derivative's normalized spectral level law is

    q_j = (j+1)W_{j+1}/I,     0<=j<=N.

It follows that E_q j>=N/2 and, with X=(j+1)/n, E_q X>=(n+1)/(2n).

Let Phi(v)=exp(-v)I_0(v), where I_0 is the modified Bessel function. The alternating-derivative estimate proved below is

    s(rho):=sum_j q_j rho^j <= Phi(N(1-rho^2)/4),   0<=rho<=1.   (3)

Since ln(n/(j+1))<=H_N-H_j, integration of the geometric series gives

    E_q ln(1/X) <= C_N,
    C_N=integral_0^1 [Phi(Nt(2-t)/4)-(1-t)^N] dt/t.

The elementary estimate proved below is

    C_N<ln 4,
    C_N<ln 4-(2-sqrt(2))/sqrt(pi N)+1/(2N),   N>=3.    (4)

The binomial entropy bound ln C(n,k)<=n h(k/n) gives

    D ln 2 / I <= E_q [ln(1/X)+r(X)],
    r(x)=-(1-x)ln(1-x)/x,    r(1)=0.

The power series r(x)=1-sum_{m>=1} x^m/[m(m+1)] shows that r is decreasing and concave. Thus Jensen's inequality gives

    E_q r(X) <= r((n+1)/(2n)) <= ln 2-(2 ln 2-1)/n.    (5)

The last inequality is the tangent at x=1/2; r'(1/2)=2-4 ln 2. Equations (4) and (5) in particular prove D<3I in every dimension. This improves the (2+1/ln 2)I within-level estimate used in the supplied earlier proof; it does not by itself improve that paper's best FEI constant.

## An explicit uniform bound for B and Gamma

Combining (1)--(5), and putting d=(2-sqrt(2))/sqrt(pi) and c=2 ln 2-1, gives for n>=4

    B/I < 3 + R(n)/ln 2,
    R(n)=(2-d)/sqrt(n)-c/n+1/[2n(n-1)]+1/[8n^{3/2}].  (6)

Here we used 1/sqrt(n-1)>=1/sqrt(n). Every term of R is decreasing for n>=1 after grouping its first two terms: the derivative of (2-d)/sqrt(n)-c/n is negative since 2-d>2c>0. The other terms decrease for n>1. Therefore, for n>=25, (6) is at most 3+R(25)/ln 2, which is less than 3.463. constants.json records a 90-decimal-digit evaluation; the slack is much larger than its precision.

For 1<=n<=24 the exhaustive integer census has B/I<2.1 (census_01.json through census_24.json), leaving a large margin. Thus the analytic proof with this finite check yields

    B <= 3.463 I,       Gamma <= 1.7315 I.              (7)

The second inequality follows pointwise from (E|c|)^2<=E c^2: Gamma<=B/2. The same argument gives A<=5.463I-2Var by Theorem 1, but this A bound is weaker than the supplied H<=4.650431I, since A<=H. For a result without a census, (6) is below 4.55 for n>=4, while direct evaluation in dimensions 1,2,3 gives B/I<1.373. Hence B<=4.55I is a fully analytic uniform version. The stronger bound (7) uses the finite census only in small dimension.

This is a bound for each functional, not a proof of its best constant. The use of the derivative-envelope method is explicit; there is no assumption of an FEI inequality in the proof of (7).

## Why Theorem 1 does not improve the symmetric FEI constant

A uniform bound B<=bI gives H<=2(b+1)I-2Var. To obtain a uniform coefficient below 4.650431 from this formula requires b<1.3252155. Already the symmetric function (+,+,+,-) in dimension 3 has

    I=3/4,
    B/I=1.3725562489182657...,

as checked by the census, the integer finite-difference evaluator and a direct truth-table transform. The dimension-24 maximum and the dimension-2000 threshold examples make the obstruction stronger. Dropping -2Var is necessary for this particular uniform-coefficient inference; it does not rule out a sharper argument retaining function-dependent information. No improvement to 4.650431 is claimed.

## Threshold identities and exact recurrences

For the threshold f_t=+1 when t<r and -1 otherwise, k>=1,

    d_k(t)=2(-1)^{r-t-1} C(k-1,r-t-1)

when 0<=r-t-1<=k-1 and is zero otherwise. Vandermonde's identity implies L_k=2C(n-1,r-1), independently of k. Therefore

    Gamma = H/2 + Var log_2(I/n).                       (8)

This also supplies a second way to check threshold cancellation. To evaluate all thresholds simultaneously in a fixed dimension, use coefficients indexed by r-1 of

    F_k(x)=(1+x)^{n-k}(1-x)^{k-1},
    Q_k(x)=(1+x)^{n-k} sum_s C(k-1,s)^2 x^s.

The actual F_k integer above is twice the corresponding coefficient of F_k(x), and its Q_k integer is four times that of Q_k(x). The recurrence F_{k+1}(x)=(1-x)F_k(x)/(1+x) is integral. The Legendre recurrence gives

    k(1+x)^2 Q_{k+1}(x)
      =(2k-1)(1+x)^2 Q_k(x)-(k-1)(1-x)^2 Q_{k-1}(x).

Exact coefficient division computes every threshold in O(n^2) integer operations per chosen dimension. thresholds.py asserts integrality and nonnegativity. For parity times threshold the restricted coefficient is a binomial cumulative sum instead; parity_thresholds.py computes the needed binomial convolutions by carry-free integer polynomial packing. The convention for this family is f_t=(-1)^t times a threshold. It includes both global sign choices through symmetry, and the ordinary parity function is recorded separately.

## Proof of the derivative envelope and the integral estimate

These two lemmas are the analytic method recalled from the brain and read in the supplied paper, inputs/fei_sym_v4/paper/main.tex, sections on noise stability and the analytic bound. Details are included here to make the argument checkable without using that paper's FEI theorem.

If a nonnegative sequence is unimodal, an alternating sum of a subsequence has absolute value at most its largest term. To see this, integrate the indicators of its superlevel sets: each set is an interval, whose selected indices form a consecutive block and have alternating sum 0 or +/-1.

A sum Z of N independent Bernoulli variables with parameters p or 1-p is unimodal. Its characteristic function has modulus at most exp(-Np(1-p)(1-cos(theta))), by 1-u<=exp(-u). Fourier inversion bounds every atom by Phi(Np(1-p)). Conditional on x, a rho-correlated copy has weight distributed as such a sum, with p=(1-rho)/2. The alternating nonzero values of g, the unimodal-sequence bound, and |g|=g^2 give

    Stab_rho(g)<=Phi(N(1-rho^2)/4) E|g|
               =Phi(N(1-rho^2)/4)||g||_2^2,

proving (3).

For completeness let G(v)=exp(-v)I_1(v). Three facts suffice for (4):

    sqrt(v)Phi(v)>1/sqrt(2pi), v>=1/2;
    integral_0^X v[-Phi'(v)]dv=XG(X);
    G(X)<1/sqrt(2pi X), X>0.

For the first, h(v)=sqrt(v)Phi(v) satisfies h''+2h'+h/(4v^2)=0. At a stationary point h''<0, so h has no local minimum. Also h(1/2)>1/sqrt(2pi), and its limit is 1/sqrt(2pi), by the integral representation of I_0 and dominated convergence. It cannot go below that limit without an interior minimum. The second follows by differentiating XG(X), using I_0'=I_1 and I_1'=I_0-I_1/X. For the third, integration by parts in the integral representation of I_1 gives

    G(X)=(X/pi) integral_0^2 exp(-Xu) sqrt(u(2-u))du
        <(sqrt(2)X/pi) integral_0^infty exp(-Xu) sqrt(u)du
        =1/sqrt(2pi X).

Split C_N into three integrals by inserting Phi(Nt/2) and exp(-Nt). The first is at most G(N/4)<sqrt(2/(pi N)): use complete monotonicity of Phi, the mean value bound and the second fact above. Frullani's identity and Phi(v)=E_theta exp(-v(1-cos(theta))) give

    integral_0^infty [Phi(Nt/2)-exp(-Nt)]dt/t=ln 4.

The tail over t>=1 is at least 2/sqrt(pi N)-E_1(N), by the first fact. Thus the second integral over [0,1] is at most ln 4-2/sqrt(pi N)+E_1(N). The third integral is exactly H_N-ln N-gamma-E_1(N). Adding and using H_N-ln N-gamma<1/(2N) proves (4) for N>=3. Its correction is negative there. For N=1, Phi<=1 gives C_1<=1<ln 4. For N=2, the bound Phi(v)<=1-v+3v^2/4 integrates to C_2<=59/64<ln 4. All integrals are convergent; the nonnegative Frullani integrand permits Tonelli's theorem.

## Integer-only verification of the finite part of (7)

The second census, census_cert.c, checks B<=3.463I with integer arithmetic on every global-sign representative through n=24. This check does not use its floating-point maxima. Its logarithm enclosures use units 1/1024 and are generated in quantlog.h. If 2^e<=x<2^(e+1), take the leading nine bits m in [256,511]. Then

    e + floor(1024 log_2(m/256))/1024 <= log_2 x
       < e + [floor(1024 log_2((m+1)/256))+1]/1024.

Every table entry is obtained without a logarithm: floor(1024 log_2(m/256))=bit_length(m^1024)-1-8192. The enclosure remains valid when the leading bits are exact and when x is a power of two.

For k>=1 substitute the upper Q_k enclosure and lower |F_k| enclosure into the closed form for B. The weighted numerator is an integer sum of C(n,k)F_k^2 times these quantized logarithms. At k=0 use

    -W_0 log_2 W_0 <= (1-W_0)/ln 2 < (1443/1000)(1-W_0),

and use zero when W_0=0. The strict rational bound on 1/ln 2 follows already by truncating ln 2=2 sum_{r>=0} 3^{-(2r+1)}/(2r+1) after four terms. Thus, with V=2^(2n)-F_0^2, T the quantized k>=1 numerator and J=sum_k k C(n,k)F_k^2, the exact assertion is

    1000 T + 1443*1024 V*1[F_0!=0] <= 3463*1024 J.

Unsigned 128-bit arithmetic suffices; n<=24 bounds every product well below 2^128. census_cert_*.json records that this assertion passed, and reports the largest (deliberately coarse) upper bound. The maxima themselves are discovered with floating-point logs; every contender within 1e-10 is separately compared at 100 digits, with the gap to excluded contenders recorded in candidates_audit.log. The finite proof certificate is rigorous even without relying on those discovery rankings.

The decimal choice in (7) can also be checked with rational bounds alone. Use d>33/100, c>386/1000 and ln 2>693/1000. The logarithm bounds follow from the first four positive terms of the series for ln 2. For d, sqrt(2)<99/70 and sqrt(pi)<1773/1000 (using pi<22/7) suffice. Then

    3+R(25)/ln 2
      < 3+[(167/100)/5-(386/1000)/25+1/1200+1/1000]/(693/1000)
      < 3463/1000.

Thus the numerical evaluation in constants.json is a cross-check, not a premise of the constant.

## A separate, stronger cancellation bound

In fact, for every symmetric Boolean function,

    Gamma <= 1.638 I.                                  (9)

First, taking another discrete derivative cannot increase L1 norm, because |(a-b)/2|<=(|a|+|b|)/2. Therefore abs1_k<=abs1_1=I/n for every k>=1. With v=Var=1-W_0, the closed form for Gamma gives

    Gamma ln 2 <= H ln 2/2 + v ln(I/n).                 (10)

Thresholds attain equality in (10), as shown in (8). For the normalized nonzero level law Q(k)=W_k/v, its mean is I/v. The maximum-entropy geometric law on positive integers gives H_e(Q)<=ln(I/v)+1; this follows directly by Gibbs' inequality, including its degenerate limit at mean one. Also h_e(v)<=v ln(1/v)+v. Consequently the level entropy L=H-D satisfies

    L ln 2 <= v[2+ln I-2 ln v].

Substitute into (10) and put rho=I/(nv), so 0<rho<=1. Dropping (1/2)ln v<=0 yields

    Gamma/I <= D/(2I)
      + [1+(1/2)ln n+(3/2)ln rho]/[n rho ln 2].

For n>=3 the maximum of the second term over 0<rho<=1 occurs at rho=(e/n)^(1/3). Hence

    Gamma/I <= D/(2I) + [3/(2e^(1/3) ln 2)] n^(-2/3). (11)

Using the sharper bound for D already proved, for n>=25 this is at most

    3/2 + [a n^(-2/3) - (d/2)n^(-1/2)
             +(1/4-c/2)/n+1/(4n(n-1))]/ln 2,
    a=3/(2e^(1/3)), d=(2-sqrt(2))/sqrt(pi), c=2ln 2-1.

On n>=25, the maximum of a n^(-2/3)-(d/2)n^(-1/2) is its value at 25. Indeed, putting t=n^(-1/6) turns it into a t^4-(d/2)t^3, which has an interior minimum and no interior maximum; its value at 25 is positive, whereas its limit at infinity is zero. The remaining two terms are positive and decreasing. The whole upper bound is therefore at most its displayed value at n=25.

A rational check avoids relying on decimals. We have a<100/93, because e^(1/3)>279/200; this follows from the first seven terms of the series for e. Also 25^(2/3)>427/50, by cubing. Together with d>33/100, c>386/1000 and ln 2>693/1000, these give

    Gamma/I < 3/2
       + [(100/93)(50/427)-33/1000+57/25000+1/2400]/(693/1000)
       =4507620883/2751972300 < 819/500.

For n<=24 the strengthened small-dimensional certificate checks B<=3.276I with integer arithmetic on every representative. Then Gamma<=B/2<=1.638I. This finite check is substantially looser than the observed maxima; it only closes the small-dimensional part of (9).

Finally, if the supplied symmetric FEI bound H<=4.650431I is used, Theorem 1 can be rearranged as 2A<=H+2I-2Var. This gives the inherited bound

    A <= 3.3252155 I - Var.                            (12)

Equation (12) is a consequence of the supplied FEI benchmark, not a new direct proof of the A conjecture.

## Sharpening the cancellation constant to 8/5

The final cancellation bound is

    Gamma <= (8/5) I.                                 (13)

There is an extra constraint that improves (11) in the remaining small range. Since q_{k-1}=kW_k/I,

    E_q(1/X)=nv/I=1/rho,
    E_q ln(1/X)<=ln(1/rho).

Thus for every rho=I/(nv), writing ell=ln(1/rho), the earlier argument gives

    Gamma/I <= [min(C_{n-1},ell)+r((n+1)/(2n))]/(2 ln 2)
           + exp(ell)[1+(1/2)ln n-(3/2)ell]/(n ln 2).   (14)

For n>=40 use (11). The endpoint argument following it applies with endpoint 40, giving a uniform upper bound below 1.6. A rational certificate is

    Gamma/I < 3/2
       + [(100/93)/(1169/100) - (33/100)/(2*(253/40))
                      +(57/1000)/40+1/(4*40*39)]/(693/1000)
       =479785646407/300358978920 <8/5.

Here 40^(2/3)>1169/100 and sqrt(40)<253/40 follow by cubing and squaring. This bounds the entire infinite range, not just n=40.

For 25<=n<=39, split at rho=4/15. If rho<=4/15, the second term of (14) is at most

    g(n) = (15/4)[1+(1/2)ln n-(3/2)ln(15/4)]/(n ln 2).

Indeed the unconstrained maximizer rho=(e/n)^(1/3) is larger than 4/15 throughout this range. The function g(n) decreases for n>=25, so g(n)<=g(25)<17/125=0.136. To bound the first term, the upper envelope in (4) increases on 24<=N<=38, and ln 2-c/n also increases. Therefore D/(2I) is at most its analytic upper bound at n=39, which is less than 183/125=1.464. Adding proves the strict bound 1.6 in this branch.

If rho>=4/15, use E ln(1/X)<=ell in (14). On 0<=ell<=ln(15/4), the derivative of its ell-dependent numerator is

    1/2 + exp(ell)[(1/2)ln n-1/2-(3/2)ell]/n >0.

For example ln 5>1.6 and ln(15/4)<1.322 make the bracket greater than -1, while exp(ell)/n<=3/20. Hence its maximum is at ell=ln(15/4). Using r<=ln 2 and g(n)<=g(25), this branch is at most

    1/2 + ln(15/4)/(2 ln 2)+0.136 <1.590 <1.6.

All numerical margins here have rational certificates in gamma_8_over_5_certificate.json, produced by sharpen_gamma_constants.py. The bounds ln 2 in (0.693,0.694), ln 5 in (1.6,1.61), and ln(15/4) in (1.3215,1.322) follow from the positive series ln x=2 sum_{j>=0} y^(2j+1)/(2j+1), y=(x-1)/(x+1), with its geometric remainder. For the D/(2I) bound use d>0.33, sqrt(38)<6.165, c>0.386 and ln 2<0.694; the negative numerator reverses the needed choice of denominator bound. This gives the certified small-block sum below 1.599661.

Finally, the integer-only finite census verifies the stronger B<=2.18I for n<=24, so Gamma<=B/2<=1.09I there. This completes (13). Statements (7) and (9) remain useful intermediate bounds but (13) is the final cancellation constant.

The B constant can be rounded more tightly than the convenient 3.463 used above: (6) gives B/I<=3+R(25)/ln 2=3.4620701729916498..., so

    B <= (3462071/1000000) I.                          (15)

sharpen_B_constants.py certifies this rounding with exact fractions. It encloses pi by Machin's formula and alternating arctangent series, sqrt(2) and sqrt(pi) by integer square roots, and ln 2 by its positive series. B_precise_constant_certificate.json records the resulting rational upper enclosure. The finite certificate B<=2.18I leaves ample room. This improves only the rounding of the proved B bound; it does not change the analytic method.

## Lower bounds from AND and majority

The direct constants are not sharp. The following intervals for the optimal uniform constants are proved:

    3 <= c_A <= 3.3252155   (the upper bound uses the supplied FEI theorem),
    2/ln 2 <= c_B <= 3.459354,
    1/ln 2 <= c_Gamma <= 8/5.

For a corner AND/OR, the nonzero-level Fourier coefficients have absolute value 2^(1-n), W_0=(1-2^(1-n))^2, and up_k=2^(2-n-k) for k>=1. Hence

    A/I = 3-4/n-(2-4/n)2^(-n) ->3,
    P/I = 1-2^(1-n) ->1.

For majority on n=2m+1 variables, I=n C(2m,m)/4^m grows as sqrt(2n/pi). Its derivative is the middle-layer indicator on 2m variables. The derivative's spectral law is

    q_{2j}=C(2j,j) C(2m-2j,m-j) 4^(-m),
    q_{2j+1}=0.

This follows from the middle-layer Krawtchouk coefficient: K_{2j}^{2m}(m)=(-1)^j C(m,j), and the factorial identity for its normalized square. The law of j/m converges to the arcsine law on (0,1), as is seen either from this factorial expression and Stirling's formula or from its beta-binomial representation. Therefore

    D/I -> (1/(pi ln 2)) integral_0^1
                         h(x)/[x sqrt(x(1-x))] dx =2/ln 2.

To justify the endpoints, q_{2j} is at most an absolute constant divided by sqrt((j+1)(m-j+1)), while ln C(n,k)/k<=1+ln(n/k). The resulting x^(-1/2)(1+|ln x|) majorant is integrable at zero; the other endpoint is easier. For the integral, E_arcsine[-ln X]=ln 4. Substitution x=sin^2 t and integration by parts give E_arcsine[-(1-X)ln(1-X)/X]=2-ln 4, so their sum is 2.

Level entropy is at most log_2(n+1), so L/I tends to zero. The threshold identity (8), with Var=1, now gives

    Gamma/I ->1/ln 2,

because log_2(I/n)/I tends to zero. Finally 2Gamma<=B<=H and H/I->2/ln 2 squeeze B/I to 2/ln 2. This also establishes A/I->0 for majority, without assuming it.

Consequently the coefficient obtained from Theorem 1 and a uniform B<=bI bound cannot be less than 2+4/ln 2=7.770780..., even asymptotically on majority. This is a limitation of that sufficient estimate, not a lower bound for the FEI constant. The finite three-variable witness remains a simpler obstruction to beating 4.650431.

## Dense parity-family enumeration

For the parity-times-threshold family, let v_k(a)=2 sum_{s<a}C(k,s)-2^k, with its constant tails outside 0<=a<=k+1. Then

    L(n,k,r)=sum_t C(n-k,t)|v_k(r-t)|,
    Q(n,k,r)=sum_t C(n-k,t)v_k(r-t)^2.

Adding an outside coordinate and using Pascal's identity gives, for k<n,

    L(n,k,r)=L(n-1,k,r)+L(n-1,k,r-1),
    Q(n,k,r)=Q(n-1,k,r)+Q(n-1,k,r-1).

At the new diagonal n=k, L(n,n,r)=|2 sum_{t<r}C(n,t)-2^n| and Q=L^2. The boundary r=0 has L(n,k,0)=2^n and Q(n,k,0)=2^(n+k). Reflection r->n-r+1 leaves L, Q and every functional unchanged, so only half the thresholds need to be stored. These are exact integer updates. parity_dense.c uses them for dense dimension coverage, while parity_thresholds.py supplies an independent carry-free convolution calculation at selected dimensions. The complete output is checked against both the direct finite-difference evaluator and that independent convolution.

## Rigorous finite suprema and exact extremal ties

The finite numerical claims are certified independently of floating-point discovery. census_interval.c encloses every functional ratio using integers at scale 2^56. A logarithm is split into an exponent, a leading-nine-bit table entry and a residual log(1+delta). The table is generated by exact rational positive-series bounds. For 0<=delta<1/256, the alternating Taylor polynomials satisfy P_6(delta)<=ln(1+delta)<=P_5(delta). Fixed-point roundoff in each six-term evaluation is less than 13 units; padding by 16 units gives outward bounds. interval_log.h and generate_interval_log.py implement these bounds. The weighted sums fit unsigned 128-bit integers for n<=24.

The scan maintains the greatest lower bound of any ratio. Any function whose upper bound is smaller is excluded; the retained lists therefore contain every possible maximizer. All 188 defined dimension/objective suprema are enclosed. Across the dimension/objective pairs, the retained lists contain 299 entries. A vector can occur for more than one objective; all possible maximizers are covered up to global sign.

certify_suprema.py then expresses each candidate's ratio as a rational linear combination of logarithms of positive integers. It verifies every integer factorization by multiplying the factors back, and checks that all candidates for a given supremum have exactly the same rational coefficient map. Matching maps prove exact ties; this argument does not require the factor labels to be prime. Consequently every retained vector attains the global supremum, and there are no omitted maximizers outside the retained lists.

For each common expression, the same script bounds its value with integer arithmetic at scale 2^440. After normalizing an integer into [1,2], use

    ln x=2 sum_{j>=0} y^(2j+1)/(2j+1),  y=(x-1)/(x+1)<=1/3.

The first 160 terms are evaluated with outward-rounded integer powers. The remainder is at most 9/[4(321)3^321]. Division by an independently enclosed ln 2 and exact rational weighting give a final interval. Its two endpoints round to the same 100 decimal places in every case. suprema_certified.json stores these values, the outward intervals, all exact extremal ties and their logarithm expressions; factorization_certificate.json supplies the checked decompositions. The verifier can run with --verify-only and needs no factor-search routine.

The largest final interval width is recorded in suprema_certificate_audit.log. The direct mpmath comparison at 170 digits is an independent check, not a premise of the certificate. Thus the finite suprema and extremal vectors are certified by integer arithmetic, including substantially more digits than the tables display.

## Final B constant from the unsimplified envelope

Keeping the exact a_n and r rather than replacing them by the simpler estimates in R(n) improves the final B constant to

    B <= 3.459354 I.                                  (16)

For real n>=25 define

    E(n)=[ln 4-d/sqrt(n-1)+1/(2(n-1))
             +r((n+1)/(2n))+a_n+1/(n(exp(a_n)-1))]/ln 2.

The preceding proof already gives B/I<=E(n) for integer n>=25. The envelope E decreases throughout this range. To see this, the derivative of the optimized last two terms is

    -sqrt(1+1/(4n))/n^(3/2)+1/(2n^2)
       <=-n^(-3/2)+1/(2n^2).

For x=(n+1)/(2n)<=13/25<2/3, concavity gives r'(x)>=r'(2/3)=3/2-(9/4)ln 3>-1. Thus the derivative of r(x(n)) is at most 1/(2n^2). The derivative of the C_N envelope is at most d/[2(n-1)^(3/2)]. Since d<1/2 and (n/(n-1))^(3/2)<9/8 for n>=25, this is less than (9/32)n^(-3/2). Altogether

    (ln 2)E'(n)<[-23/32+1/sqrt(n)]n^(-3/2)<0.

The estimate ln 3<10/9 follows already from the first five terms of exp(10/9)>3. Therefore the infinite range is bounded by E(25)=3.4593539592703766.... The finite range still has B/I<=2.18. sharpen_B_envelope.py encloses E(25) using exact rational logarithm series, integer square-root bounds and Machin's pi formula, proving E(25)<3459354/1000000. B_final_constant_certificate.json records the enclosure. This is the final B constant; the earlier 3.462071 and 3.463 are valid intermediate bounds.
