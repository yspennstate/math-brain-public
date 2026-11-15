# Exact rational certificate for the four-atom cubic bound

Let alpha_3 denote the limiting independence ratio of the uniform random
simple cubic graph, with the number of vertices tending to infinity through
even integers. This note certifies a particular published upper bound. It
does not determine alpha_3 or improve the best published upper bound.

## The inequality used

Viktor Harangi, *Improved replica bounds for the independence ratio of random
regular graphs*, Journal of Statistical Physics 190, article 60 (2023),
[arXiv:2204.01353v4](https://arxiv.org/html/2204.01353), equation (3), gives
the following consequence of the interpolation bound. For lambda>1,
0<m<1, p_i>=0 with sum_i p_i=1, and 0<=q_i<=1, put

\[
 V=\sum_{i,j,k=1}^4 p_i p_j p_k
 \left(1+(\lambda-1)(1-q_i)(1-q_j)(1-q_k)\right)^m,
\]
\[
 E=\sum_{i,j=1}^4 p_i p_j
 \left(1-(1-1/\lambda)q_iq_j\right)^m.
\]
Then

\[
 \alpha_3\le B:=\frac{\log V-\frac32\log E}{m\log\lambda}. \tag{1}
\]

The published interpolation theorem is the input to this note; its proof
is not reproduced here. The remaining numerical substitution is proved
using rational arithmetic.

Take the following exact rational numbers, as in Section 1.2 of that paper:

\[
 \lambda=\frac{193}{10},\qquad m=\frac{557}{1000},
\]
\[
 (p_1,p_2,p_3,p_4)=\frac1{10000}(2493,2778,2880,1849),
\]
\[
 (q_1,q_2,q_3,q_4)=\frac1{10000}(1184,5947,8876,9827).
\]

All entries are in the required ranges and
2493+2778+2880+1849=10000. Thus (1) applies. The star bases are in
[1,lambda]; the edge bases are in [1/lambda,1], since 0<=q_iq_j<=1.
Every fractional power and every logarithm below therefore has a positive
argument.

## Grouping the sums

For an unordered tuple I of length r, written in nondecreasing order, let
c_j be the number of occurrences of j. There are

\[
 M(I)=\frac{r!}{\prod_{j=1}^4c_j!}
\]

ordered tuples having those entries. Their bases agree, because the
expressions above are symmetric. Their combined weight is

\[
 w(I)=M(I)\prod_{i\in I}p_i.
\]

There are binomial(6,3)=20 star tuples and binomial(5,2)=10 edge tuples.
Each grouped weight is nonnegative, and the sum of the weights in each
sum is (sum_i p_i)^r=1. Equivalently, summing the multiplicities gives
4^3=64 star terms and 4^2=16 edge terms. The script also verifies the
grouping by independently enumerating the ordered tuples and comparing
the total exact rational weight attached to every exact rational base.

## Enclosing a fractional power by integer comparisons

Let x=A/C>0 be a reduced fraction with positive integers A,C. Fix S=10^24
and form the integer

\[
 T=\left\lfloor\frac{S^{1000}A^{557}}{C^{557}}\right\rfloor.
\]

Let a be the integer satisfying a^1000<=T<(a+1)^1000. Integer bisection
finds a. An initial upper endpoint is
2^ceil(bitlength(T)/1000), whose 1000th power exceeds T, and the lower
endpoint is zero. Every step retains the inequality at the endpoints and
reduces the interval until its endpoints are consecutive integers.

By the definition of T,

\[
 a^{1000}\le\frac{S^{1000}A^{557}}{C^{557}}<(a+1)^{1000}.
\]

For the strict upper inequality, (a+1)^1000 is an integer larger than T,
so it is at least T+1, while the fraction defining T is less than T+1.
Taking the increasing positive 1000th root gives

\[
 \frac aS\le x^{557/1000}<\frac{a+1}{S}. \tag{2}
\]

After bisection, the program directly checks the integer inequalities

\[
 a^{1000}C^{557}\le S^{1000}A^{557}
 <(a+1)^{1000}C^{557},
\]

so the final brackets are verified against x itself. No numerical
transcendental function occurs in this step.

Multiply the endpoints in (2) by their nonnegative grouped weights and
add them. This yields rational endpoints V_-,V_+,E_-,E_+ containing V,E.
Each of these sum intervals has width exactly 1/S, since the corresponding
weights sum to one. All of their lower endpoints are positive.

## Enclosing logarithms by a rational series

First suppose 1<=y<=2 and put z=(y-1)/(y+1). Thus 0<=z<=1/3. Integrating
the geometric series for 1/(1-t^2) from 0 to z gives

\[
 \log y=2\sum_{j=0}^{\infty}\frac{z^{2j+1}}{2j+1}.
\]

For an integer N>=1 let

\[
 L_N(y)=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}.
\]

The remainder is nonnegative and is bounded above by

\[
 2\sum_{j=N}^{\infty}\frac{z^{2j+1}}{2j+1}
 \le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}=:R_N(y). \tag{3}
\]

Indeed each denominator in the tail is at least 2N+1, and the resulting
numerators sum to a geometric series. Thus [L_N(y),L_N(y)+R_N(y)] encloses
log y with rational endpoints whenever y is rational. It also encloses
log 2 by taking y=2. The certificate uses N=64.

For a general rational x>0, find an integer k and a rational y in [1,2)
with x=2^k y. Repeated exact multiplication or division by 2 produces
them. Then log x=k log 2+log y. If log 2 is enclosed by [a,b] and log y
by [c,d], use [c+ka,d+kb] for k>=0 and [c+kb,d+ka] for k<0. This reversal
when k is negative preserves the interval inequalities.

Monotonicity of log now gives log V between a lower bound on log V_- and
an upper bound on log V_+. The same applies to E. Denote the resulting
logarithm bounds by

\[
 v_-\le\log V\le v_+,\quad
 e_-\le\log E\le e_+,\quad
 \ell_-\le\log\lambda\le\ell_+.
\]

All endpoints here are exact fractions. Set

\[
 n_-=v_--\tfrac32 e_+,\quad n_+=v_+-\tfrac32 e_-,
 \qquad d_-=m\ell_-,\quad d_+=m\ell_+.
\]

The program checks 0<n_-<=n_+ and 0<d_-<=d_+. Hence

\[
 \frac{n_-}{d_+}\le B\le\frac{n_+}{d_-}. \tag{4}
\]

This accounts for both the subtraction in the numerator and the uncertainty
in the positive denominator.

## Certified result and independent checks

Running `certify.py --digits 24 --series-terms 64 --audit` gives the following
outward decimal enclosures of the exact fractions in (4):

\[
\begin{aligned}
 V&\in[1.33787206871340330831,\ 1.33787206871340330832],\\
 E&\in[0.73974606806929845553,\ 0.73974606806929845554],\\
 B&\in[0.45078995170969821695,\ 0.45078995170969821696].
\end{aligned}
\]

To print a fraction u/v to t decimal places, the lower endpoint is
floor(10^t u/v)/10^t and the upper endpoint is ceil(10^t u/v)/10^t.
The program compares the unrounded upper fraction in (4) with the exact
rational 450789952/10^9. The comparison is strict. Therefore

\[
 \boxed{\alpha_3\le B<0.450789952.}
\]

Its positive margin is enclosed by

\[
 0.450789952-B\in
 [0.0000000002903017830494,\ 0.0000000002903017830495].
\]

An independent calculation in `audit_decimal.py` uses the original 64 and
16 ordered terms, with powers evaluated as exp(m log x) at 70 and 110
decimal digits. The values agree within 10^-67 and fall inside both the
default and refined rational enclosures. This calculation is an audit;
the certificate rests on (2)–(4).

Additional exact checks cover integer-root boundaries at 0, 1 and 2^1000;
logarithms at 1, 1/2, 2 and 4; all q_i=0 and all q_i=1; and an interior
one-atom distribution. The all-zero choice gives B=1, because V=lambda^m
and E=1. The all-one choice gives B=3/2, because V=1 and E=lambda^(-m).
For a single atom q, the factor m cancels and (1) becomes

\[
 \frac{\log(1+(\lambda-1)(1-q)^3)
 -\frac32\log(1-(1-1/\lambda)q^2)}{\log\lambda}.
\]

At q=3/5 the certificate encloses the direct rational-log evaluation of
this expression. These cases test multiplicities, the sign of the edge
term, and the normalization by m log lambda.
