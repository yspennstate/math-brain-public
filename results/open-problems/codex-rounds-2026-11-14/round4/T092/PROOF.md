# A centered block with square-root loss at most three times its squared budget

Write T=R/Z with normalized Haar measure dz, and e(z)=exp(2 pi i z).
All phase expectations below use independent normalized Haar variables on
the unit circle. The color set is finite and nonempty.

## Single-block estimate

Let p_r:T->[0,infinity) be integrable, put p=sum_r p_r, and suppose

\[
 \int_T p\le2.
\]

Let b_r be complex constants with |b_r|<=1. On {p>0} define

\[
 t_r=p_r/p,\qquad \beta=\sum_r t_r b_r.
\]

Set beta=0 on {p=0}. Let q be a bounded measurable complex function with
|q|<=2. Suppose that

\[
 0<\delta\le\frac1{100},\qquad
 \int_T\sqrt p\,|\beta-q|^2\le\delta.                 \tag{1}
\]

Let n>=1 and lambda>0 satisfy

\[
 \frac\delta2\le s:=n\lambda^2\le\delta,
 \qquad 6\lambda\le1.                               \tag{2}
\]

For Z=(Z_1,...,Z_n) on the product phase torus define

\[
 a_r(z)=b_r-q(z),\qquad
 H_r(z,Z)=\prod_{i=1}^n
   \left[1+\lambda\bigl(a_r(z)\overline{Z_i}
                      +\overline{a_r(z)}Z_i\bigr)\right],
 \quad
 D(z,Z)=q(z)+\frac1{n\lambda}\sum_{i=1}^n Z_i.        \tag{3}
\]

Every factor in H_r is nonnegative because |a_r|<=3 and 6lambda<=1.
The following two estimates hold simultaneously:

\[
 \int_T\mathbb E\sqrt{\sum_r p_rH_r}\,dz
 \ge \int_T\sqrt p\,dz-\frac{243}{82}\delta^2
 \ge \int_T\sqrt p\,dz-3\delta^2,                   \tag{4}
\]

and, for any bounded measurable A:T->C and integer k>=0,

\[
 \sum_r\int_T p_r\,
   \mathbb E\left[H_r|A+D-(k+1)b_r|^2\right]dz
 \le\sum_r\int_T p_r|A-kb_r|^2dz+\frac4\delta.       \tag{5}
\]

### The mixture variance

Fix z with p(z)>0 and suppress z from the notation. Set

\[
 m=\sum_r t_ra_r=\beta-q,\quad x=|m|^2,\quad
 v=\sum_r t_r|a_r|^2,\quad R=\sum_r t_rH_r.
\]

Expanding the squared norm about beta gives

\[
 v=\sum_r t_r|b_r-\beta|^2+|\beta-q|^2
   =\sum_r t_r|b_r|^2-|\beta|^2+x\le1+x.            \tag{6}
\]

Also |beta|<=1 and |q|<=2 imply 0<=x<=9. Consequently

\[
                  v^2\le(1+x)^2\le1+11x.           \tag{7}
\]

For one Haar phase Z_i put

\[
 Y_{r,i}=a_r\overline{Z_i}+\overline{a_r}Z_i.
\]

The basic moments E Z_i=E Z_i^2=0 and E|Z_i|^2=1 give

\[
 \mathbb E Y_{r,i}=0,\qquad
 \mathbb E(Y_{r,i}Y_{u,i})
          =2\operatorname{Re}(a_r\overline{a_u}).    \tag{8}
\]

Expand each product in (3) by subsets of {1,...,n}. Then

\[
 R-1=\sum_{\varnothing\ne S\subseteq\{1,...,n\}}
       \lambda^{|S|}\sum_r t_r\prod_{i\in S}Y_{r,i}.
\]

Terms belonging to distinct subsets S are orthogonal in real L2 of the
phase torus. Indeed, choose an index belonging to exactly one of two
distinct subsets and integrate that phase first; (8) makes the integral
zero. Thus E R=1, and

\[
 \operatorname{Var}(R)=
 \sum_{j=1}^n\binom nj\lambda^{2j}
       \sum_{r,u}t_rt_u
          [2\operatorname{Re}(a_r\overline{a_u})]^j. \tag{9}
\]

The j=1 term is exactly 2s|m|^2. For j>=2,

\[
 \begin{aligned}
 \left|\sum_{r,u}t_rt_u
        [2\operatorname{Re}(a_r\overline{a_u})]^j\right|
 &\le2^j\left(\sum_r t_r|a_r|^j\right)^2\\
 &\le2^j9^{j-2}v^2,
 \end{aligned}                                    \tag{10}
\]

since |a_r|^(j-2)<=3^(j-2). Although individual summands in (9) may
have signs, their sum for each fixed j is a squared L2 norm; taking
absolute values in (10) is a valid upper bound.

Using binom(n,j)<=n^j/j! and j!>=2 for j>=2, and extending a
nonnegative finite sum to an infinite sum, gives

\[
 \begin{aligned}
 \operatorname{Var}(R)
 &\le2sx+\frac{v^2}{81}
                  \sum_{j=2}^\infty\frac{(18s)^j}{j!}\\
 &\le2sx+\frac{2s^2v^2}{1-18s}.
 \end{aligned}                                    \tag{11}
\]

The denominator is positive because 18s<=18/100<1. This argument is
also valid for n=1, when the actual remainder in (9) is zero.

### Square-root loss

For every nonnegative random variable R with E R=1,

\[
 1-\mathbb E\sqrt R
 =\tfrac12\mathbb E(\sqrt R-1)^2
 =\tfrac12\mathbb E\frac{(R-1)^2}{(\sqrt R+1)^2}
 \le\tfrac12\operatorname{Var}(R).                 \tag{12}
\]

Apply (11), (12), and (7) at each z with p(z)>0. All terms are
multiplied by sqrt(p), so {p=0} contributes zero and needs no division.
Writing I=int_T sqrt(p) and J=int_T sqrt(p)|beta-q|^2, we obtain

\[
 \begin{aligned}
 I-\int_T\mathbb E\sqrt{\sum_rp_rH_r}
 &\le sJ+\frac{s^2}{1-18s}(I+11J)\\
 &\le\delta^2+
       \frac{\delta^2}{1-18\delta}(I+11\delta).
 \end{aligned}                                    \tag{13}
\]

Cauchy--Schwarz gives I<=sqrt(2)<3/2. Since delta<=1/100,

\[
 1+\frac{I+11\delta}{1-18\delta}
 \le1+\frac{50}{41}\left(\frac32+\frac{11}{100}\right)
 =\frac{243}{82}<3.                               \tag{14}
\]

Equations (13) and (14) prove (4). All integrals are finite: the
number of factors is finite, their coefficients are bounded, and
p and sqrt(p) are integrable.

### Prediction

For a fixed color r and z, H_r is a probability density on the phase
torus: its factors are nonnegative and each has integral one. Under
this density the phases are independent. One-phase integration gives

\[
 \mathbb E_{H_r}Z_i=\lambda a_r,\qquad
 \mathbb E_{H_r}|Z_i-\lambda a_r|^2
                         =1-\lambda^2|a_r|^2.      \tag{15}
\]

Indeed, multiplying Z_i by its density leaves only the constant term
lambda a_r after integration. The second identity follows from
|Z_i|=1 and the first. Independence and (3) now imply

\[
 \mathbb E_{H_r}D=b_r,\qquad
 \mathbb E_{H_r}|D-b_r|^2
       =\frac{1-\lambda^2|a_r|^2}{n\lambda^2}
       =\frac1s-\frac{|a_r|^2}{n}\le\frac1s.        \tag{16}
\]

For fixed z and r, A-kb_r is constant in the phase variables. The
cross term in the expansion of |(A-kb_r)+(D-b_r)|^2 vanishes by
unbiasedness. Therefore the exact increase in (5) is

\[
 \frac1s\int_Tp
       -\frac1n\sum_r\int_Tp_r|b_r-q|^2
 \le\frac2s\le\frac4\delta.                       \tag{17}
\]

This proves (5), without requiring A to be independent of z or to have
come from a previous block.

## Transfer to diagonal phases and perturbed densities

Under the same assumptions, let nu>0. For every sequence of finite
integer lower bounds B_i(L_1,...,L_(i-1)), there are positive integers
L_1,...,L_n exceeding those bounds such that the following statement
holds. Put

\[
 \begin{split}
 h_r(z)&=p_r(z)H_r\bigl(z,e(L_1z),...,e(L_nz)\bigr),\\
 D_L(z)&=q(z)+\frac1{n\lambda}\sum_i e(L_iz),\\
 W&=\bigl(\|A\|_\infty+2+1/\lambda+k+1\bigr)^2,\\
 e_0&=\min\left\{(\nu/2)^2,\frac{\nu}{2(W+1)}\right\}>0.
 \end{split}                                      \tag{18}
\]

The supremum in (18) may be replaced by any finite uniform bound
for A, by choosing a bounded representative. For every collection of
nonnegative integrable functions g_r with

\[
                         \sum_r\|g_r-h_r\|_1\le e_0,             \tag{19}
\]

one has simultaneously

\[
 \int_T\sqrt{\sum_rg_r}
             \ge\int_T\sqrt p-3\delta^2-\nu,                    \tag{20}
\]

\[
 \sum_r\int_Tg_r|A+D_L-(k+1)b_r|^2
       \le\sum_r\int_Tp_r|A-kb_r|^2+\frac4\delta+\nu.           \tag{21}
\]

The number e_0 is fixed before the lower bounds are supplied and before
the L_i are chosen.

### A finite Fourier averaging fact

Suppose finitely many tests have the form

\[
 P(z,Z)=\sum_{\alpha\in E}c_\alpha(z)\prod_i Z_i^{\alpha_i},
 \qquad c_\alpha\in L^1(T),\quad E\subset Z^n\text{ finite}.
\]

For any eta>0 their product-phase integrals can simultaneously be
approximated to error less than eta by substituting Z_i=e(L_i z),
with the positive L_i exceeding the prescribed successive bounds.

To prove this, gather the finite coefficient list over all tests and
let d>=1 bound all absolute exponents. The zero monomial contributes
exactly the same integral on both spaces. Every other monomial has
product-phase mean zero; its diagonal integral is a Fourier coefficient
of c_alpha at frequency -sum_i alpha_i L_i. Fourier coefficients of an
L1 function tend to zero: approximate it in L1 by a trigonometric
polynomial, whose sufficiently high coefficients vanish, and bound
the remaining coefficient by the L1 approximation error.

Choose an integer R large enough that the sum of all nonconstant
contributions is less than eta when their frequencies exceed R in
absolute value. Recursively impose, in addition to each given bound,

\[
                  L_j>R+d\sum_{i<j}L_i.
\]

If j is the last nonzero position of alpha, then

\[
 \left|\sum_i\alpha_iL_i\right|
    \ge L_j-d\sum_{i<j}L_i>R.
\]

This proves the fact for arbitrary finite lower bounds depending on
earlier choices. It makes no assertion of independence for diagonal
phases.

### The two tests

For x>=0 define Q(x)=1+(x-1)/2-(x-1)^2/2. Then

\[
 \sqrt x-Q(x)=\tfrac12\sqrt x(\sqrt x-1)^2(\sqrt x+2)\ge0.
                                                                    \tag{22}
\]

On {p>0} use the two tests

\[
 T_1(z,Z)=\sqrt p\,Q(R),\qquad
 T_2(z,Z)=\sum_rp_rH_r|A+D-(k+1)b_r|^2.
\]

Set T_1=0 on {p=0}. Both are finite Laurent polynomials in the phase
variables, with L1 coefficient functions. For T_1 this follows because
t_r and q are bounded and sqrt(p) is integrable; for T_2 use boundedness
of A and q and integrability of p_r. On the phase torus conjugation
replaces Z_i by Z_i^(-1), so absolute squares remain Laurent polynomials.

Since E R=1, the expectation of T_1 is
sqrt(p)[1-Var(R)/2]. The estimate (13) applies to this expression itself,
not just to E sqrt(R). Consequently its integral is at least
I-3delta^2. The integral of E T_2 is bounded by (5).

Apply the averaging fact to these two tests with eta=nu/2. By (22),
sqrt(sum_r h_r) is pointwise at least the diagonal value of T_1.
This proves (20) for h with nu/2 in place of nu. The same choices of
L_i prove (21) for h with nu/2 in place of nu.

For nonnegative f,g on the probability circle,

\[
 \left|\int_T\sqrt f-\int_T\sqrt g\right|
 \le\int_T\sqrt{|f-g|}\le\|f-g\|_1^{1/2}.           \tag{23}
\]

The first inequality follows from
|sqrt(f)-sqrt(g)|^2<=|f-g|, and the second from Cauchy--Schwarz.
The total-density L1 error in (19) is at most e_0, so (23) costs
at most sqrt(e_0)<=nu/2.

Also |D_L|<=2+1/lambda, since each phase has modulus one. Thus the
squared weight in (21) is at most W, independently of the L_i.
Replacing h_r by g_r changes that integral in absolute value by
at most W e_0<=nu/2. This proves (20) and (21).

## Independent checks and boundary cases

There is a second derivation of the variance bound. Direct integration
of one pair of factors, followed by independence, gives

\[
 \mathbb E(H_rH_u)
    =[1+2\lambda^2\operatorname{Re}(a_r\overline{a_u})]^n.
\]

Expand this scalar binomial and sum with weights t_rt_u. The constant
term is one, the linear term is 2s|beta-q|^2, and the terms of degree
j>=2 satisfy (10). This reproduces (11) without using orthogonality
of subsets.

The identity in (6) can also be checked by

\[
 \sum_r t_r|b_r-\beta|^2
     =\tfrac12\sum_{r,u}t_rt_u|b_r-b_u|^2
     =\sum_r t_r|b_r|^2-|\beta|^2.
\]

The scalar square-root lower bound (22) independently gives the
factor 1/2 in (12) after taking expectations. Its coefficient cannot
be decreased in a global inequality of that quadratic form, since
x=0 requires at least 1/2.

The numerical comparison in (14) uses only rational arithmetic:
1-18/100=41/50, 3/2+11/100=161/100, and
1+(50/41)(161/100)=243/82. Alternatively, the inequality that this
quantity is less than three reduces to
I+47delta<2, which follows from I<3/2 and 47delta<=47/100.

The estimator variance can be checked without centered variables:
under H_r, the diagonal terms in E|sum_i Z_i|^2 contribute n and
the n(n-1) off-diagonal terms contribute lambda^2|a_r|^2 each.
Subtracting |E sum_i Z_i|^2=n^2 lambda^2|a_r|^2 gives
n(1-lambda^2|a_r|^2), exactly (16) after division by n^2lambda^2.

If p is identically zero, both model conclusions hold directly, and
the perturbation conclusions follow from the same error estimates.
Individual zero colors can be retained. If there is one color and
q=b_r, then H_r=1 and the mixture loss is zero, while the estimator
variance is 1/s. At n=1 the variance is exactly 2s|beta-q|^2.
For two equal-weight colors with b_1=1, b_2=-1 and q=0, the linear
term vanishes and direct calculation gives

\[
 \operatorname{Var}(R)
     =\tfrac12[(1+2\lambda^2)^n+(1-2\lambda^2)^n]-1;
\]

its leading nonzero term is 2n(n-1)lambda^4. This checks the
quadratic budget scale and the factor two in the variance tail.
Complex tags require no additional symmetry: (8), (15) and the
pairwise identities remain valid over C.

The centering condition is essential for a uniform quadratic loss.
For example, take p=1, one color b=1, q=0, n=1, and lambda=sqrt(delta).
Then J=1, so (1) fails. Here R=1+2sqrt(delta) Re(Z), E R=1,
Var(R)=2delta and R<=6/5 for delta<=1/100. Since
(sqrt(R)+1)^2<5, the identity in (12) gives

\[
                         1-\mathbb E\sqrt R\ge\delta/5.
\]

Thus omitting (1) would allow loss of first order in delta.

If colors have an involution r->r* with
p_(r*)(-z)=p_r(z), b_(r*)=conj(b_r), and q(-z)=conj(q(z)), then
the diagonal estimator satisfies D_L(-z)=conj(D_L(z)) and
h_(r*)(-z)=h_r(z). These identities follow by conjugating each
phase and each bias in (3). The diagonal selection needs no change
to preserve this symmetry.

## Scope

This is an analytic single-block statement. It supplies simultaneous
diagonal tests for any prescribed successive frequency bounds and
any final densities satisfying (19). It does not produce those densities
by a measure-preserving change of coordinates, prove the required
smooth physical estimates, or construct a Koopman operator with simple
Lebesgue spectrum. The constant three is a valid bound; no optimality
claim is made for it.
