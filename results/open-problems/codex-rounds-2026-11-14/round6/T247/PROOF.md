# Logarithmic volume drift at the depth scale n/a

All matrices and vectors are real. Let O_l be independent Haar matrices on O(n), and let xi_l be independent standard Gaussian vectors, independent of the matrices. Consider

\[
h_l=\tanh(gO_lh_{l-1}+\sqrt b\,\xi_l),\qquad
J_l=g\operatorname{diag}(\operatorname{sech}^2(gO_lh_{l-1}+\sqrt b\,\xi_l))O_lJ_{l-1},
\quad J_0=I_n.
\tag{1}
\]

The input is deterministic and nonzero. The gain g>0 and bias variance b>=0 are deterministic and identical across layers. The Jacobian differentiates the input with all parameters fixed. Define

\[
q_l=g^2\|h_{l-1}\|^2/n,\quad
\mu_n(q,b)=\mathbb E\operatorname{sech}^4(\sqrt{nq}\,u_1+\sqrt b\,G),\quad
S_k=\prod_{l=1}^k g^2\mu_n(q_l,b),
\tag{2}
\]

where u is uniform on the unit sphere and G is an independent standard normal. Put

\[
H_k=\frac1n\log\det(J_kJ_k^\top)
=\frac1n\sum_{i=1}^n\log s_i(J_k)^2,\qquad H_0=0.
\tag{3}
\]

Every factor in (1) is invertible almost surely, so these logarithms are finite.

**Theorem.** Suppose n,L=L(n) tend to infinity, a=a_n>0, La^2 tends to zero, and eventually

\[
0\leq b\leq14a^3,\qquad |\log(g^2)-2a|\leq15a^2,\qquad
|q_1/a-1|\leq14a^2.
\tag{4}
\]

There is no restriction on La/n. Then

\[
\max_{l\leq L+1}|q_l/a-1|\xrightarrow{\mathbb P}0,\qquad
\max_{k\leq L}|H_k-\log S_k|\xrightarrow{\mathbb P}0,
\tag{5}
\]

and, for t_n=La/(n+2),

\[
\frac{\max_{0\leq k\leq L}|H_k+4ak/(n+2)|}{1+t_n}
\xrightarrow{\mathbb P}0.
\tag{6}
\]

The same statement (6) holds with H_k replaced by log S_k. In particular:

* If La/n tends to t in [0,infinity), then H_L tends to -4t, and both S_L and the geometric mean det(J_L J_L^top)^(1/n) tend to exp(-4t), in probability.
* If La/n tends to infinity, then H_L/(La/n) and log S_L/(La/n) tend to -4; both geometric mean and S_L tend to zero, in probability.

The conventional simultaneous Gaussian critical initialization satisfies (4): if

\[
\mu_G(a)=\mathbb E\operatorname{sech}^4(\sqrt aG),\quad
A_G(a)=\mathbb E\tanh^2(\sqrt aG),\quad
g^2=\mu_G(a)^{-1},\quad b=a-g^2A_G(a),\quad
\|h_0\|^2/n=A_G(a),
\tag{7}
\]

then b>0, b<=14a^3 and q_1=a-b for sufficiently small a. These facts are proved again below.

This is a logarithmic spectral statistic, not a full limiting density or a bound on spectral edges. It does not assert failure of empirical isometry when t>0.

## 1. Scalar inequalities and moments

For all real x,

\[
0\leq\tanh^2x-x^2+\tfrac23x^4\leq\tfrac{17}{45}x^6,
\quad
0\leq\operatorname{sech}^4x-1+2x^2\leq\tfrac73x^4,
\quad
0\leq\tfrac{x^2}{2}-\log\cosh x\leq\tfrac{x^4}{12}.
\tag{8}
\]

Here is a direct derivation. For x>=0 set v=x-tanh x. Integration of tanh^2 s<=s^2 gives 0<=v<=x^3/3. Consequently 0<=x^2-tanh^2 x<=2x^4/3, and a second integration gives 0<=x^3/3-v<=2x^5/15. The first remainder in (8) is 2x(x^3/3-v)+v^2, bounded by (4/15+1/9)x^6. The second remainder is 2(x^2-tanh^2 x)+tanh^4 x. The last inequality follows by integrating 0<=x-tanh x<=x^3/3. Evenness handles negative x.

For u uniform on the sphere,

\[
\mathbb E\prod_i u_i^{2j_i}
=\frac{\prod_i(2j_i-1)!!}{n(n+2)\cdots(n+2\sum_i j_i-2)}.
\tag{9}
\]

Indeed a standard Gaussian vector is its independent radius times its uniform direction. Gaussian integration by parts gives both its coordinate moments and the radial moments in the denominator of (9). Odd coordinate moments vanish by sign symmetry.

For z_i=sqrt(nq)u_i+sqrt(b)xi_i and r=q+b, expansion of the powers, independence and (9) give

\[
\mathbb Ez_i^2=r,\quad
\mathbb Ez_i^4=\frac{3n}{n+2}q^2+6qb+3b^2\leq3r^2,
\quad \mathbb Ez_i^6\leq15r^3,\quad\mathbb Ez_i^8\leq105r^4.
\tag{10}
\]

Each surviving coefficient is nonnegative, and every even spherical moment is at most the corresponding Gaussian moment. This proves the last two comparisons term by term.

By (8),(10), for r<=1/4,

\[
1-2r\leq\mu_n(q,b)\leq1,\qquad
|\log\mu_n(q,b)+2r|\leq15r^2.
\tag{11}
\]

For completeness, 0<=mu-1+2r<=7r^2. If w=-log mu, then 0<=w<=4r, and 0<=w-(1-exp(-w))<=w^2/2. The last bound follows by integrating 1-exp(-v)<=v. Adding 7r^2 and 8r^2 proves (11).

The Gaussian Poincare inequality gives A_G(a)<=a mu_G(a). One elementary proof sufficient here uses independent standard normals G,B and G_t=sqrt(t)G+sqrt(1-t)B. For smooth bounded f with bounded derivatives, integration by parts gives

\[
\frac{d}{dt}\mathbb E[f(G)f(G_t)]
=\frac1{2\sqrt t}\mathbb E[f'(G)f'(G_t)].
\]

The terms involving f'' cancel. Cauchy–Schwarz bounds the expectation by E f'(G)^2; integration from 0 to 1 proves Var f(G)<=E f'(G)^2. Take f(G)=tanh(sqrt(a)G), whose mean is zero. The bound is strict for a>0, because f' is nonconstant and, at t=0, the expectation of the product of two independent derivatives is strictly below E f'(G)^2; continuity preserves this strict inequality on an interval. Hence b>0 in (7).

Also (8) gives A_G=a-2a^2+R_A and mu_G=1-2a+R_mu, with 0<=R_A<=17a^3/3 and 0<=R_mu<=7a^2. For a<=1/4,

\[
0<b=\frac{aR_\mu-R_A}{\mu_G}\leq14a^3.
\tag{12}
\]

The Gaussian version of (11) gives the gain bound (4), and q_1=g^2 A_G=a-b proves its input bound.

## 2. Forward estimates without a restriction on La/n

The following estimates reproduce the radius part of the preceding round with all constants specified. Work at

\[
n\geq64,\qquad 0<a\leq1/16384,
\tag{13}
\]

which holds eventually. From (4) and the exponential remainder,

\[
g^2\leq2,\quad |g^2-1|\leq4a,\quad |g^2-1-2a|\leq32a^2.
\tag{14}
\]

For example |log g^2|<=5a/2, and |exp(v)-1-v|<=v^2 exp(|v|)/2 proves all three bounds.

Given the preceding network, O_l h_(l-1)/||h_(l-1)|| is uniform on the sphere, independent of the fresh bias. Thus the conditional law of the next radius is exactly

\[
q'=\frac{g^2}{n}\sum_i\tanh^2z_i,\qquad
U=(q'-q)/q,\quad d(q)=\mathbb E U,\quad c_n=2n/(n+2).
\tag{15}
\]

For q in [a/2,2a],

\[
|d(q)-(2a-c_nq)|\leq300a^2,\quad |d(q)|\leq7a,
\quad \mathbb EU^2\leq12000a^2.
\tag{16}
\]

To verify the drift, (8),(10) yield

\[
\mathbb E(q'/g^2)=q+b-c_nq^2-4qb-2b^2+R_F,
\qquad 0\leq R_F\leq17(q+b)^3/3.
\tag{17}
\]

After division by q, the errors against 2a-c_nq are bounded, in units of a^2, by 32,16,56,1,1,153. In order these are g^2-1-2a, -(g^2-1)c_nq, g^2b/q, -4g^2b, -2g^2b^2/q and g^2R_F/q. For the last term, b/q<=28a^2<=1/2, so it is at most (34/3)(3/2)^3 q^2<=153a^2. The sum is 259<300. Then 2a+c_nq+300a^2<=7a.

For the second moment let v=n^(-1)sum z_i^2 and B=v-n^(-1)sum tanh^2 z_i. The exact Gaussian calculation and (8),(10) give

\[
\mathbb E(v-q)^2=b^2+(4qb+2b^2)/n\leq3b^2+4qb/n,
\quad 0\leq B\leq\frac2{3n}\sum_i z_i^4,
\quad \mathbb EB^2\leq140(q+b)^4/3.
\tag{18}
\]

For the first identity write v=q+2sqrt(qb/n)u dot xi+(b/n)||xi||^2. The centered linear and quadratic Gaussian terms have covariance zero. For the last inequality use the square of an average at most the average of squares and E z_i^8<=105(q+b)^4. Since q'-q=(g^2-1)q+g^2(v-q)-g^2B, the square of a sum of three terms is at most three times the sum of their squares, so

\[
\mathbb EU^2\leq48a^2+36(b/q)^2+48b/(nq)+560(q+b)^4/q^2.
\]

The four terms are at most 48a^2, a^2,21a^2,11340a^2, respectively, using (4),(13), b/q<=28a^2 and q+b<=3q/2. Their sum is 11410a^2<12000a^2, proving (16).

Put x_k=q_(k+1)/a-1. Stop at its first exit from (-1/2,1), include that exit step, and freeze afterwards. An active step is one begun before this exit. Its conditional drift is B(x)=(1+x)d(a(1+x)), with |B(x)|<=14a. Let r_0=8/n+600a. Equation (16) implies B(x)<=0 for x>=r_0 and B(x)>=0 for x<=-r_0 within the active interval: divide d by a, use 2-c_n=4/(n+2), c_n>=1, and absorb the error 300a by r_0.

The stopped process has the decomposition

\[
\bar x_k=x_0+\sum_{j<k}\bar B_j+M_k,
\qquad \mathbb E M_L^2\leq48000La^2.
\tag{19}
\]

The indicator of an active step is measurable before its fresh randomness, so M is a martingale. The variance bound follows from (16) and (1+x)^2<=4.

Pathwise,

\[
\max_{k\leq L}|\bar x_k|\leq r_0+14a+2\max_{k\leq L}|M_k|.
\tag{20}
\]

If bar x_k>r_0, take the last j<k with bar x_j<=r_0. Such a j exists since |x_0|<=14a^2<=r_0. The first subsequent drift is at most 14a, and every later drift is nonpositive or frozen. Thus bar x_k<=r_0+14a+M_k-M_j. The lower crossing is identical with signs reversed. This argument includes a possible exit jump.

Define two further stopped sums

\[
N_k=\sum_{l\leq k}{\bf1}_{\mathrm{active},l}(U_l-d(q_l)),\qquad
V_k=\sum_{l\leq k}{\bf1}_{\mathrm{active},l}U_l^2.
\tag{21}
\]

Here N is a martingale, E N_L^2<=12000La^2 and E V_L<=12000La^2. A square-martingale maximal inequality and Markov's inequality show that, for 0<delta<=1/16 and eta>0, with exceptional probability at most

\[
p_0=60000La^2/\delta^2+12000La^2/\eta,
\tag{22}
\]

one has max |M_k|<=delta, max |N_k|<=delta and V_L<=eta. The square-martingale inequality follows by stopping at its first crossing of delta^2 and comparing its expected square there with the final expected square. On this event (20) precludes radius exit, since

\[
\max_{l\leq L+1}|q_l/a-1|\leq\varepsilon,
\quad\varepsilon=8/n+614a+2\delta<1/2.
\tag{23}
\]

The numerical strict inequality follows already at n=64,a=1/16384,delta=1/16. Notice that (19)–(23) contain no accumulated La/n term. Positivity of the radii holds almost surely: a nonzero vector stays nonzero for b=0, while b>0 gives a fresh preactivation density with no atom at the zero vector.

## 3. The signed accumulated scalar law

Set s(q)=log(g^2)+log mu_n(q,b). By (4),(11) and q+b<=3a on active steps,

\[
|s(q)-(2a-2q)|\leq152a^2,\qquad
\left|s(q)-d(q)+\frac{4q}{n+2}\right|\leq452a^2.
\tag{24}
\]

Indeed the first error is at most 15a^2+2b+15(q+b)^2<=152a^2; the second adds 300a^2 from (16) and uses 2-c_n=4/(n+2). This retains the sign lost by taking the absolute size of the width correction.

On the event in (22)–(23), every adjacent radius ratio is in [1/4,4]. The second derivative of log has absolute value at most 16 there, so for every k<=L,

\[
\left|\sum_{l\leq k}U_l-\log(q_{k+1}/q_1)\right|\leq8V_k\leq8\eta.
\tag{25}
\]

Moreover |log(q_(k+1)/q_1)|<=2epsilon+28a^2, by (4),(23) and |log(1+x)|<=2|x| for |x|<=1/2. Summing (24), using sum U=sum d+N, and applying (25) gives

\[
\max_{k\leq L}\left|\log S_k+\frac4{n+2}\sum_{l\leq k}q_l\right|\leq C_0,
\quad C_0=16/n+1228a+28a^2+5\delta+8\eta+452La^2.
\tag{26}
\]

The coefficient 5delta is 4delta from 2epsilon and delta from N. Since |q_l-a|<=a epsilon,

\[
\max_{k\leq L}|\log S_k+4ak/(n+2)|\leq C_0+4t_n\varepsilon.
\tag{27}
\]

Under La^2->0 choose delta=(La^2)^(1/4), eta=(La^2)^(1/2). Eventually delta<=1/16; then p_0,epsilon,C_0 all tend to zero. Division of (27) by 1+t_n proves the scalar version of (6), for arbitrary t_n. It also proves the radius assertion (5).

## 4. Comparison with the determinant of the actual Jacobian

By multiplicativity of the determinant and |det O_l|=1, the exact increment of (3) is

\[
H_l-H_{l-1}=\log(g^2)+\frac1n\sum_i\log\operatorname{sech}^4z_{li}.
\tag{28}
\]

For a single active step write v=n^(-1)sum z_i^2, r=q+b and

\[
R=\frac1n\sum_i\log\operatorname{sech}^4z_i-\log\mu_n(q,b).
\]

Equation (8) gives log sech^4 z=-2z^2+rho(z), with 0<=rho(z)<=z^4/3. Also E v=r and Var v=(4qb+2b^2)/n by (18). Together with (10),(11) this proves

\[
\mathbb E|R|\leq2\sqrt{(4qb+2b^2)/n}+16r^2\leq150a^2.
\tag{29}
\]

For the last constant, q<=2a,b<=14a^3 and a<=1/16384 give 4qb+2b^2<=113a^4. Since n>=64, its square-root term is at most 3a^2; also 16r^2<=144a^2. Thus 147a^2 would suffice, and 150a^2 is a convenient upper bound. These expectations average the fresh bias and sphere direction, conditional on the preceding network. No gate independence is assumed.

Let W=sum_(l<=L) 1_active,l |R_l|. By conditional expectation E W<=150La^2. On no radius exit, (28) implies max_(k<=L)|H_k-log S_k|<=W. Consequently, for any rho>0,

\[
\mathbb P\left\{\max_{k\leq L}|H_k+4ak/(n+2)|
>C_0+4t_n\varepsilon+\rho\right\}
\leq p_0+150La^2/\rho.
\tag{30}
\]

The same bound without the deterministic threshold terms proves the second assertion in (5). Take rho=(La^2)^(1/2), together with the delta and eta chosen after (27), to prove (5)–(6). If t_n stays bounded the error is absolute o_P(1), giving H_L->-4t. If t_n->infinity, division by t_n gives H_L/t_n->-4, hence H_L->-infinity. Because (n+2)/n->1, replacing t_n by La/n yields precisely the theorem's consequences. Exponentiation gives the asserted geometric means and scalar limits.

There is also a uniform time version. If n a->0 and T>0 is fixed, set K_n(t)=floor(t(n+2)/a) for 0<=t<=T. Applying the theorem at L=K_n(T) gives

\[
\sup_{0\leq t\leq T}|H_{K_n(t)}+4t|\xrightarrow{\mathbb P}0,
\qquad
\sup_{0\leq t\leq T}|S_{K_n(t)}-e^{-4t}|\xrightarrow{\mathbb P}0.
\tag{31}
\]

Indeed La^2<=T(n+2)a->0, t_n<=T, and rounding changes 4ak/(n+2) by at most 4a/(n+2). Uniform exponentiation is valid on the bounded limiting range.

## 5. Limits of this conclusion

The coefficient 4 has a second derivation at first order. The forward mean (17) has leading nonzero equilibrium q_*=a(n+2)/n. The mean logarithmic squared volume per layer is 2a-2q_*=-4a/n. The proof above justifies this calculation without assuming exact stationarity, and bounds the initial transient and accumulated errors.

The log-volume law does not rule out W2 convergence of the empirical squared-singular-value measure to delta_1. For example the deterministic positive spectrum

\[
\lambda_1=e^{-4tn},\qquad\lambda_2=\cdots=\lambda_n=1
\]

has n^(-1)sum log lambda_i=-4t, while its squared W2 distance to delta_1 is (1-e^(-4tn))^2/n<=1/n. This example concerns the logical strength of the statistic, not a claim about how many exceptional directions occur in (1). Establishing empirical isometry under La^2->0 alone still requires new control of the forward-direction terms in the conditional trace recursion.
