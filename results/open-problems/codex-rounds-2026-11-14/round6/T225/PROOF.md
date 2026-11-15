# Second residual derivative and a larger positivity window

Let gamma denote N(0,1), pi=gamma tensor gamma, and set
\[
 f_\rho(x)=\int a\sin(vx)\,d\rho(a,v),\qquad
 R(\rho)=\tfrac12\|f_\rho-\sin\|_{L^2(\gamma)}^2.
 \tag{1}
\]
The temperature is constant, the prior pi is fixed, and time is physical
gradient-flow time for R+lambda KL(.||pi). Write
\[
 K(v,w)=e^{-(v^2+w^2)/2}\sinh(vw),\quad
 G_t(w)=\langle\sin-f_{\rho_t},\sin(w\,\cdot)\rangle,\quad
 g(w)=K(1,w).
 \tag{2}
\]
The weak generator is
\[
 L_t=\lambda(\partial_a^2+\partial_v^2)
 +(G_t(v)-\lambda a)\partial_a
 +(aG_t'(v)-\lambda v)\partial_v.
 \tag{3}
\]

## 1. Solution class and result

Fix T>0. For each 0<lambda<=1 consider any W2-continuous weak solution
of (3) on [0,T], initialized at pi, with locally bounded fourth moments
and
\[
 R(\rho_t)+\lambda\operatorname{KL}(\rho_t\Vert\pi)
 \leq R(\pi).
 \tag{4}
\]
No existence or uniqueness assertion for unbounded parameterizations is
part of the result.

Define
\[
 \begin{split}
 h(w)&=\frac{e^{-(1+w^2)/3}}{\sqrt3}\sinh(w/3),\\
 D(w)&=-2h''(w)-wh'(w)\\
 &=\frac{e^{-(1+w^2)/3}}{9\sqrt3}
 [(10-2w^2)\sinh(w/3)+5w\cosh(w/3)],\\
 E(w)&=\mathbb E[D(V)K(V,w)+D'(V)\partial_vK(V,w)],\\
 Z(w)&=-2D''(w)-wD'(w),\qquad V\sim\gamma.
 \end{split}
 \tag{5}
\]
Then
\[
 \dot G_0=-D,\qquad \ddot G_0=E+\lambda Z.
 \tag{6}
\]
In particular temperature first appears in the second derivative. The
following asymptotics hold as w tends to positive infinity:
\[
 \begin{split}
 E(w)&\sim\frac5{4096\sqrt2}\,w^4
       e^{-(5w^2-2w+5)/16},\\
 Z(w)&\sim\frac2{81\sqrt3}\,w^4
       e^{-(w^2-w+1)/3}.
 \end{split}
 \tag{7}
\]
There are constants C2>=0 and C3(T)>=1, independent of lambda and
of the solution, such that
\[
 E(w)+\lambda Z(w)\geq-C2\,g(w)\quad(w>0),
 \tag{8}
\]
and
\[
 \left|G_t(w)-g(w)+tD(w)-\tfrac{t^2}2[E(w)+\lambda Z(w)]\right|
 \leq C3(T)t^3\min(|w|,1).
 \tag{9}
\]
Here (9) holds throughout [0,T]. The constants are finite; no useful
numerical size for C3(T) is asserted.

Let C1=25e/(9sqrt(3)). If t<=T is small enough that
\[
 C1t+\tfrac12 C2t^2\leq\tfrac12,\qquad
 L_3(t)^2=6\log(1/t)-1-2\log(4C3(T))>0,
 \tag{10}
\]
then the actual solution satisfies
\[
 G_t(w)\geq\tfrac14g(w)>0\quad(0<w\leq L_3(t)).
 \tag{11}
\]
Consequently, for every 0<kappa<sqrt(6), this positivity holds on
0<w<=kappa sqrt(log(1/t)) for all sufficiently small t, uniformly over
0<lambda<=1. The previous first-order argument gave every kappa<2.

## 2. Rechecking the first derivative

Let Bq=q''-vq' and ell_q=(1-B)q=q+vq'-q''. Gaussian integration by
parts gives, for the functions below,
\[
 \mathbb E\ell_q(V)k(V)=\mathbb E[q(V)k(V)+q'(V)k'(V)].
 \tag{12}
\]
The OU part of (3) annihilates pi in the weak equation. The initial
risk drift therefore has density derivative
\[
 \dot\rho_0=a\ell_g(v)\pi,
 \tag{13}
\]
because -partial_a(g pi)-partial_v(ag' pi)=a(g+vg'-g'')pi.
It follows that
\[
 \dot f_0(x)=\mathbb E[g(V)\sin(Vx)+g'(V)x\cos(Vx)].
 \tag{14}
\]
Completing the Gaussian square and then integrating by parts gives
\[
 \begin{split}
 H(x)&=\mathbb E[g(V)\sin(Vx)]
       =2^{-1/2}e^{-(1+x^2)/4}\sin(x/2),\\
 U(x):=\dot f_0(x)&=(1+x^2)H(x)+xH'(x).
 \end{split}
 \tag{15}
\]
For any smooth rapidly decreasing odd q, let
j(w)=E[q(X)sin(wX)]. Integration by parts in X proves
\[
 \mathbb E[((1+X^2)q(X)+Xq'(X))\sin(wX)]
 =-2j''(w)-wj'(w).
 \tag{16}
\]
Indeed the transform of (1+X^2)q is j-j'', whereas that of Xq' is
-j''-j-wj'. The sine transform of H is h from (5), by Gaussian square
completion. Equations (15)--(16) give the reported D and dot G_0=-D.

For reference, a second check of the normalization is
\[
 -\dot R_0=\mathbb E[g(V)^2+g'(V)^2]
 =\frac{13e^{-1/3}-3e^{-1}}{18\sqrt3}.
 \tag{17}
\]
The first expectation is (e^{-1/3}-e^{-1})/(2sqrt(3)), and the
second is (2e^{-1/3}+3e^{-1})/(9sqrt(3)), obtained by differentiating
E exp(-V^2+sV)=exp(s^2/6)/sqrt(3).

We also record the bound needed below:
\[
 D(w)\leq C1g(w)\quad(w>0).
 \tag{18}
\]
To verify it, D/h=P=(10-2w^2+5w coth(w/3))/9. With z=w/3,
coth z-z csch^2 z<z follows from z coth z>1. Hence
P'<-7w/27, P(0+)=25/9, P(3)>0 and P(5)<0; the last inequality uses
coth z<1+1/z. Where D is positive, w<5 and
\[
 h/g=\frac{e^{(1+w^2)/6}}{\sqrt3[1+2\cosh(2w/3)]}
 \leq\frac1{\sqrt3}e^{(w^2-4w+1)/6}\leq e/\sqrt3.
\]
The convex quadratic in the last exponent has maximum 1 on [0,5].
Where D is nonpositive, (18) is automatic. This proves (18).

## 3. Exact second derivative

Fix w, set k(v)=K(v,w), Q(v)=k''(v)-k(v)-vk'(v), and phi=ak(v).
Directly from (3),
\[
 L_t\phi=G_tk+a^2G_t'k'+\lambda aQ.
 \tag{19}
\]
At time zero,
\[
 \mathbb E_\pi[\partial_t(L_t\phi)]_{t=0}
 =-\mathbb E[Dk+D'k']=-E(w).
 \tag{20}
\]
To calculate E_pi L_0(L_0 phi), split L_0 into its OU part and
the risk drift g partial_a+ag' partial_v. The OU part has zero
expectation under pi. The risk drift applied to gk+a^2g'k' is odd
in a and also has zero expectation. Its application to lambda aQ
has expectation lambda E[gQ+g'Q']. Consequently
\[
 \left.\frac{d^2}{dt^2}\mathbb E_{\rho_t}\phi\right|_0
 =-E(w)+\lambda\mathbb E\ell_g(V)Q(V).
 \tag{21}
\]
The sign reverses for G. To identify its temperature term, first replace
k by sin(vx). Its Q is
\[
 -(1+x^2)\sin(vx)-vx\cos(vx).
\]
By (13)--(15), integration against ell_g gives
\[
 -[(1+x^2)U(x)+xU'(x)].
\]
Taking its sine transform and using (16) shows
\[
 -\mathbb E\ell_g(V)Q(V)=-2D''(w)-wD'(w)=Z(w).
 \tag{22}
\]
This proves (6). Section 5 justifies the time differentiations for the
specified weak solution class.

## 4. Exact Gaussian formula and tail signs

Applying (12) to D yields E(w)=E[ell_D(V)K(V,w)]. Differentiation of
the explicit D gives
\[
 \ell_D(v)=\frac{e^{-(1+v^2)/3}}{81\sqrt3}
 [(20v^4-177v^2+146)\sinh(v/3)
 +(269v-64v^3)\cosh(v/3)].
 \tag{23}
\]
An exact closed formula for E is as follows. Set
\[
 \begin{split}
 b_\pm&=w\pm\tfrac13,\\
 A(b)&=\tfrac{405}{1024}b^4-\tfrac{297}{16}b^2+\tfrac{1409}{16},\\
 C(b)&=-\tfrac{27}{8}b^3+\tfrac{591}{8}b.
 \end{split}
\]
Then
\[
 E(w)=\frac{e^{-1/3-w^2/2}}{162\sqrt8}
 \left[(A+C)(b_+)e^{3b_+^2/16}
       +(-A+C)(b_-)e^{3b_-^2/16}\right].
 \tag{24}
\]
For completeness, in the Gaussian integral in (23) the required
generating function is
\[
 M(b)=\mathbb E e^{-5V^2/6+bV}=\sqrt{3/8}\,e^{3b^2/16}.
\]
Product-to-sum in (23) gives
\[
 E(w)=\frac{e^{-1/3-w^2/2}}{162\sqrt3}
 \{[20M^{(4)}-177M''+146M](b_+)
  -[20M^{(4)}-177M''+146M](b_-)
  +[269M'-64M'''](b_+)+[269M'-64M'''](b_-)\}.
 \tag{25}
\]
The polynomials multiplying M are exactly A and C, proving (24).
The plus branch dominates by a factor exp(w/4) up to polynomial
factors. Its leading coefficient is
\[
 \frac{405}{162\cdot1024\sqrt8}=\frac5{4096\sqrt2},
\]
and its exponent is
-1/3-w^2/2+3(w+1/3)^2/16=-(5w^2-2w+5)/16.
This proves the first asymptotic in (7).

The positive exponential branch of D is
\[
 \frac{10-2w^2+5w}{18\sqrt3}e^{-(w^2-w+1)/3}.
\]
Applying -2 partial_w^2-w partial_w to this exact branch multiplies
its leading term by -2w^2/9. The other branch is exponentially smaller.
Since D's leading coefficient is -1/(9sqrt(3)), this proves the second
asymptotic in (7), including its positive sign.

Both E and Z are odd analytic functions, while g(w)>0 on w>0 and
g'(0)=exp(-1/2)>0. Thus E/g and Z/g extend continuously to zero.
By (7) both ratios tend to positive infinity at positive infinity:
their Gaussian decay exponents, 5/16 and 1/3, are less than g's 1/2.
Their infima on the positive half-line are finite. Define
\[
 C2=\max(0,-\inf_{w>0}E(w)/g(w))
    +\max(0,-\inf_{w>0}Z(w)/g(w)).
 \tag{26}
\]
This proves (8) uniformly over 0<=lambda<=1.

## 5. A uniform third-order remainder

The estimates in this section also justify all differentiations at zero.
Put r^2=a^2+v^2 and q=1+|a|+|v|. From (4),
\[
 \|\sin-f_{\rho_t}\|_2\leq1,\qquad
 \|G_t^{(j)}\|_\infty\leq(\mathbb EX^{2j})^{1/2}
 \quad(j\geq0).
 \tag{27}
\]
Differentiation in frequency and Cauchy--Schwarz prove the latter
inequality. In particular the bounds for j=0,1 are one. The generator
on V4=(1+r^2)^2 obeys
\[
 L_tV4\leq20V4,\qquad
 \sup_{0\leq t\leq T}\mathbb E_{\rho_t}V4
 \leq13e^{20T}=:M_T.
 \tag{28}
\]
Indeed theta dot drift <=|a|+|av|<=1/2+r^2, grad V4=4(1+r^2)theta,
and Delta V4=8+16r^2. Their sum is at most
10+22r^2+4r^4<=20(1+r^2)^2. Initially E V4=13. Cutoffs and the
assumed local fourth moment bound justify Gronwall. Also q^4<=9V4.

Here is a finite derivative and growth argument with the operator order
specified. For any fixed j,m>=0,
\[
 \sup_{v,w}|\partial_v^m\partial_w^jK(v,w)|
 \leq\mathbb E|X|^{m+j}<\infty.
 \tag{29}
\]
For j=0 this improves to
\[
 |\partial_v^m K(v,w)|
 \leq c_m\delta(w),\qquad
 \delta(w)=\min(|w|,1),\quad
 c_m=\max(\mathbb E|X|^m,\mathbb E|X|^{m+1}).
 \tag{30}
\]
Use |sin(wX)|<=min(|wX|,1). All required constants involve finitely
many Gaussian moments.

If a smooth test and its parameter derivatives through order s are
bounded by C q^m, then its image under L_t and derivatives through
order s-2 are bounded by C' q^{m+1}. This follows term by term from
(3): every derivative of its drift has growth at most q, its diffusion
is constant and bounded, and (27) bounds every needed spatial derivative
of G. This rule retains a multiplicative factor delta(w) whenever the
test bounds contain it. The rule is used only a finite number of times.

To establish the needed temporal coefficient bounds without circularity,
use phi_j(a,v;w)=a partial_w^jK(v,w). The weak equation gives
\[
 \partial_w^j\dot G_t(w)=-\mathbb E_{\rho_t}L_t\phi_j.
 \tag{31}
\]
The test has growth q and L_t phi_j has growth q^2, with constants
uniform in w and lambda by (27),(29). Thus every fixed spatial
derivative of dot G is uniformly bounded on [0,T], by (28).
These derivatives are continuous: the weak identity has a continuous
integrand, since W2 continuity and locally bounded fourth moments imply
convergence of expectations of continuous tests with growth at most
q^2. Coefficient continuity follows from input L2 continuity of f.
The latter follows, for any coupling of rho_t,rho_s, from
\[
 \|f_t-f_s\|_2\leq(\mathbb E|A_t-A_s|^2)^{1/2}
 +(\mathbb EA_s^2)^{1/2}(\mathbb E|V_t-V_s|^2)^{1/2}.
\]
Correlations and their frequency derivatives inherit continuity uniformly
in frequency by Gaussian input Cauchy--Schwarz bounds.

Define the operator derivatives
\[
 \dot L_t=\dot G_t(v)\partial_a+a\dot G_t'(v)\partial_v,
 \qquad
 \ddot L_t=\ddot G_t(v)\partial_a+a\ddot G_t'(v)\partial_v.
 \tag{32}
\]
The first is now well defined, with its coefficients and every fixed
number of spatial derivatives bounded by C_T q. Differentiate (31)
in its integrated weak form to obtain
\[
 \partial_w^j\ddot G_t(w)
 =-\mathbb E_{\rho_t}(L_t^2+\dot L_t)\phi_j.
 \tag{33}
\]
The growth is at most q^3, and (28) bounds its expectation. Hence
ddot G and every fixed spatial derivative are uniformly bounded.
The right side is continuous for the same reason, using uniform
integrability of q^3 from bounded fourth moments. It follows that
dot L is continuously differentiable in time with derivative ddot L,
and (32) has coefficients and any fixed number of spatial derivatives
bounded by C_T q.

One more weak differentiation gives, almost everywhere in time,
\[
 \partial_t^3G_t(w)
 =-\mathbb E_{\rho_t}
 [L_t^3+2L_t\dot L_t+\dot L_tL_t+\ddot L_t]\phi_0.
 \tag{34}
\]
The order of multiplication is composition on the test to the right.
Indeed differentiating L_t^2 gives dot L_t L_t+L_t dot L_t; the
weak equation supplies another L_t dot L_t. This accounts for the
coefficient two in (34).

By (30), phi_0 and all its required derivatives have bound C delta q.
Three applications of the growth rule bound L_t^3 phi_0 by
C_T delta q^4. The next two terms in (34) have bound
C_T delta q^3, and the last has bound C_T delta q^2. Therefore
\[
 |\partial_t^3G_t(w)|\leq C_T\delta(w)
 \quad\hbox{for almost every t in }[0,T],
 \tag{35}
\]
uniformly over lambda and solutions in the stated class.

All weak differentiations above can be performed with smooth parameter
cutoffs first. For (31)--(33) the tests have growth at most q, q^2,
and q^3. Applying one generator raises the growth at most to q^4.
Cutoff errors are bounded by C q^4 times an indicator tending to zero
outside expanding balls. They tend to zero after integration in time:
pointwise dominated convergence for each law and the uniform bound
(28) give dominated convergence in time. Spatial coefficient derivatives
and their time derivatives have the bounds already established before
their use. Time-dependent tests can be approximated in time, or their
integrated identities used directly. Thus (33) is continuous and
absolutely continuous in time with derivative (34); no fifth or sixth
parameter moments are needed. At t=0, (33) recovers (20)--(22).

Taylor's integral formula with (35) proves (9), enlarging the finite
constant to C3(T)>=1 if necessary. In particular it gives a cubic
absolute remainder, not a relative estimate in frequency.

## 6. Positivity and its limitation

Equations (8),(18) give, for the exact quadratic Taylor polynomial,
\[
 g(w)-tD(w)+\tfrac12t^2[E(w)+\lambda Z(w)]
 \geq[1-C1t-C2t^2/2]g(w)\geq\tfrac12g(w).
 \tag{36}
\]
For w>0, sinh w>=w implies
\[
 g(w)\geq e^{-(1+w^2)/2}\min(w,1).
 \tag{37}
\]
If w<=L_3(t), (10) is exactly the condition
C3(T)t^3<=exp(-(1+L_3(t)^2)/2)/4. The remainder in (9) is
therefore at most g(w)/4. This proves (11). Since
L_3(t)^2=6 log(1/t)-O_T(1), it also proves the stated result for
every kappa<sqrt(6).

At any fixed positive time, L_3(t) is finite. These estimates do not
exclude negative residual lobes farther out. They give no restricted
proximal-gap estimate along the full trajectory, no small-risk runtime
bound, and no annealing remainder estimate.
