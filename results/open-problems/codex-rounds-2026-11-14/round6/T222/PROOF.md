# A tradeoff between insertion energy and the first projection

Let Q=[0,1]^2. For a finite nonempty set S, let T(S) be the length
of a shortest closed Euclidean tour through S. A singleton has tour
length zero; a two-point tour traverses its segment twice. Let
L_n=T({X_1,...,X_n}) for independent uniform points in Q.
All lengths and variances refer to the fixed unit square.

For A contained in [n], define

\[
 h_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}
              \mathbb E[L_n\mid X_B],\qquad
 V_{n,j}=\sum_{|A|=j}\mathbb E h_A^2,\qquad
 E_n=\sum_{j=1}^n jV_{n,j}.
 \tag{1}
\]

Let S be an independent sample of n-1 uniform points and put

\[
 \begin{split}
 Y_n(x,S)&=\sqrt n\,[T(S\cup\{x\})-T(S)],\\
 U_n(x)&=\mathbb E_S Y_n(x,S),\qquad
 m_n(S)=\int_Q Y_n(x,S)\,dx,\\
 \mu_n&=\int_Q U_n(x)\,dx=\mathbb E_S m_n(S),\qquad
 W_n=\operatorname{Var}_S(m_n(S)).
 \end{split}
 \tag{2}
\]

For c>=0 define

\[
 F(c)=c^2+\frac4\pi e^{-\pi c^2}
                -2c\operatorname{erfc}(\sqrt\pi c),\qquad
 \operatorname{erfc}(t)=\frac2{\sqrt\pi}
                            \int_t^\infty e^{-s^2}\,ds.
 \tag{3}
\]

Let c_*>0 be the unique minimizer of F on [0,infinity), and put
\(\kappa=F(c_*)\), \(\alpha=e/4\). These c_* and kappa agree with
round 3's constants. In particular 0<alpha<1.

**Theorem.** There is a nonnegative deterministic sequence d_n tending
to zero, depending only on nearest-distance distributions, such that
for every n>=2,

\[
 \boxed{
 E_n+W_n+\alpha V_{n,1}
       +(1+\alpha)(\mu_n-c_*)^2\le\kappa+d_n.}
 \tag{4}
\]

Consequently, with no hypothesis about convergence of mu_n or V_{n,1},

\[
 \boxed{\displaystyle
 \limsup_n\operatorname{Var}(L_n)
 \le \frac\kappa2+\frac{1-\alpha}{8}
       -\frac{1-\alpha^2}{4}(c_*-1/2)^2.}
 \tag{5}
\]

In particular the simpler upper bound

\[
 \limsup_n\operatorname{Var}(L_n)
 \le \frac\kappa2+\frac{1-e/4}{8}
 \tag{6}
\]

is strictly smaller than round 5's bound (K+1/4)/2, where

\[
 K=\kappa-\eta(c_*),\qquad
 \eta(c)=\frac{\pi c^4}{256}e^{-9\pi c^2}.
 \tag{7}
\]

These assertions are upper bounds. They do not establish convergence of
the unscaled variance or identify a limiting variance.

## 1. Exact variance identities and geometric bounds

Integrating h_A over any coordinate in A gives zero: pair its defining
terms with and without that coordinate. Therefore distinct supports are
orthogonal. Inclusion-exclusion also gives L_n=sum_A h_A. Integrating
out X_i removes exactly the terms whose supports contain i. It follows
that

\[
 \operatorname{Var}(L_n)=\sum_j V_{n,j},\qquad
 E_n=\sum_i\mathbb E\operatorname{Var}(L_n\mid X_{-i})
     =\mathbb E_S\operatorname{Var}_X(Y_n(X,S)\mid S).
 \tag{8}
\]

The factor n in the sum of conditional variances is absorbed by the
sqrt(n) in Y_n. The expectation of T(S) is independent of a conditioned
query point, so

\[
 \mathbb E[L_n\mid X_1=x]
       =\mathbb E L_{n-1}+n^{-1/2}U_n(x).
\]

Consequently

\[
 V_{n,1}=\operatorname{Var}_X U_n(X),\qquad
 \mu_n=\sqrt n(\mathbb E L_n-\mathbb E L_{n-1}).
 \tag{9}
\]

No limit of this consecutive difference is used.

Write R(x,S)=min_{y in S}|x-y| and Z_n(x,S)=sqrt(n)R(x,S).
Shortcutting a removed point proves insertion cost is nonnegative.
Appending the closed detour y,x,y at a nearest point y and shortcutting
repeated vertices proves

\[
 0\le Y_n(x,S)\le2Z_n(x,S).
 \tag{10}
\]

For any x in Q and 0<=r<=sqrt(2), the square
x+(r/sqrt(2))(Q-x) lies in Q intersect B(x,r) and has area r^2/2.
Thus

\[
 \mathbb E_S R(x,S)^2\le
       \int_0^2(1-t/2)^{n-1}\,dt=\frac2n,
 \qquad 0\le U_n(x)\le2\sqrt2.
 \tag{11}
\]

This includes boundary points. In particular all the variances in (2)
are finite.

## 2. An envelope limit uniform over bounded spatial centers

For every real c and z>=0 set

\[
 H_c(z)=\max\{c^2,(2z-c)^2\}.
 \tag{12}
\]

Convexity of the squared distance to c implies, whenever 0<=y<=2z,

\[
 (y-c)^2\le H_c(z).
 \tag{13}
\]

Let Z have survival function P(Z>r)=exp(-pi r^2), r>=0.
Integrating its survival function gives E Z=1/2 and
E Z^2=integral_0^infinity 2r exp(-pi r^2)dr=1/pi.
For c>=0 the envelope is constant up to c and then has derivative
8r-4c. Thus

\[
 \begin{split}
 \mathbb E H_c(Z)
 &=c^2+\int_c^\infty(8r-4c)e^{-\pi r^2}\,dr\\
 &=c^2+\frac4\pi e^{-\pi c^2}
                  -2c\operatorname{erfc}(\sqrt\pi c)=F(c).
 \end{split}
\]

Here integral_c^infinity r exp(-pi r^2)dr equals
exp(-pi c^2)/(2pi), and integral_c^infinity exp(-pi r^2)dr equals
erfc(sqrt(pi)c)/2. Extend F to negative c by

\[
 F(c)=c^2-2c+4/\pi,\qquad c<0.
 \tag{14}
\]

Indeed H_c(Z)=(2Z-c)^2 for c<0, so (14) is again E H_c(Z).

Define

\[
 p_n(x,r)=\mathbb P_S(Z_n(x,S)>r),\qquad p(r)=e^{-\pi r^2}.
\]

For every fixed interior x and fixed r, eventually the disk
B(x,r/sqrt(n)) lies in Q. Independence then gives

\[
 p_n(x,r)=(1-\pi r^2/n)^{n-1}\longrightarrow p(r).
 \tag{15}
\]

The displayed binomial expression is used only for sufficiently large
n. Uniformly in all x, r>=0 and n>=2 the homothetic-square bound gives

\[
 0\le p_n(x,r)\le e^{-r^2/4}.
 \tag{16}
\]

For r^2<=2n use (1-r^2/(2n))^{n-1}<=exp(-r^2/4);
for r^2>2n the probability is zero.

For each fixed M>0 put

\[
 D_n(M)=\int_Q\int_0^\infty(8r+4M)
                   |p_n(x,r)-p(r)|\,dr\,dx.
 \tag{17}
\]

The integrand converges to zero for almost every (x,r), by (15).
It is bounded by 2(8r+4M)exp(-r^2/4), an integrable function on
Q times [0,infinity). Dominated convergence therefore proves

\[
 D_n(M)\longrightarrow0.
 \tag{18}
\]

To see why this controls centers that vary with x and n, use the exact
tail formula

\[
 H_c(z)=c^2+\int_0^z k_c(r)\,dr,\qquad
 k_c(r)=(8r-4c)\mathbf1_{\{r>\max(c,0)\}}.
 \tag{19}
\]

For c<0 the indicator equals one for all r>0. For c>=0 the envelope
is constant up to c, then has derivative 8r-4c. In both cases
0<=k_c(r)<=8r+4M whenever |c|<=M. Tonelli's theorem and subtraction
of the two tail formulas imply

\[
 \left|\mathbb E_S H_c(Z_n(x,S))-F(c)\right|
 \le\int_0^\infty(8r+4M)|p_n(x,r)-p(r)|\,dr.
 \tag{20}
\]

Hence for any measurable deterministic centers c_n:Q->[-M,M],

\[
 \int_Q\mathbb E_S H_{c_n(x)}(Z_n(x,S))\,dx
       \le\int_Q F(c_n(x))\,dx+D_n(M).
 \tag{21}
\]

No convergence of c_n is required. This is stronger than substituting
an n-dependent center into a pointwise convergence statement. The
boundary is included in the integrated error (17).

## 3. Curvature and the adaptive center

For c>=0, differentiation of (3) gives

\[
 F'(c)=2c-4ce^{-\pi c^2}-2\operatorname{erfc}(\sqrt\pi c),
 \qquad F''(c)=2+8\pi c^2e^{-\pi c^2}.
 \tag{22}
\]

The extension (14) has F''=2, and the first two derivatives agree at
zero. Thus F is twice continuously differentiable on the real line.
Since t exp(-t)<=1/e for t>=0,

\[
 2\le F''(c)\le2+8/e=2+2/\alpha,\qquad c\in\mathbb R.
 \tag{23}
\]

Also F'(0)=-2 and F'(c) tends to infinity as c tends to infinity.
Strict convexity gives a unique minimizer c_*>0, determined by

\[
 c_*=2c_*e^{-\pi c_*^2}
                  +\operatorname{erfc}(\sqrt\pi c_*).
 \tag{24}
\]

The right side is E[2Z 1_{Z>c_*}], which is strictly less than
2 E Z=1 because c_*>0. In particular 0<c_*<1.

The upper second-derivative bound and F'(c_*)=0 imply, for every real v,

\[
 F(c_*+v)\le\kappa+(1+1/\alpha)v^2.
 \tag{25}
\]

For completeness, Taylor's formula with integral remainder expresses
the difference on the left minus kappa as
v^2 integral_0^1 (1-t)F''(c_*+tv)dt. Equation (23) bounds that
integral by 1+1/alpha, for either sign of v.

Set

\[
 a_n(x)=U_n(x)-c_*,\qquad
 c_n(x)=c_*-\alpha a_n(x),\qquad
 M=(1+\alpha)c_*+2\alpha\sqrt2.
 \tag{26}
\]

By (11), |c_n(x)|<=M for every x and n. Negative centers cause no
problem because F was extended in (14). Equations (10), (13), (21)
and (25) give

\[
 \mathbb E_{X,S}(Y_n(X,S)-c_n(X))^2
 \le\kappa+(\alpha^2+\alpha)\int_Q a_n(x)^2\,dx+D_n(M).
 \tag{27}
\]

On the other hand, expanding the square and using
E_S[Y_n(x,S)-c_*]=a_n(x) yields exactly

\[
 \mathbb E(Y_n-c_n(X))^2
   =\mathbb E(Y_n-c_*)^2
                +(2\alpha+\alpha^2)\int_Q a_n(x)^2\,dx.
 \tag{28}
\]

Subtracting the common terms in (27)-(28) proves

\[
 \mathbb E(Y_n-c_*)^2
           +\alpha\int_Q(U_n(x)-c_*)^2\,dx
       \le\kappa+D_n(M).
 \tag{29}
\]

The two variance decompositions, with their different conditionings, are

\[
 \begin{split}
 \mathbb E(Y_n-c_*)^2
      &=E_n+W_n+(\mu_n-c_*)^2,\\
 \int_Q(U_n-c_*)^2
      &=V_{n,1}+(\mu_n-c_*)^2.
 \end{split}
 \tag{30}
\]

For the first identity condition on S and use (8); for the second
use (9). Equations (29)-(30) prove (4), with d_n=D_n(M).

## 4. Consequence for the total tour variance

Nonnegativity of the interaction energies implies

\[
 2\operatorname{Var}(L_n)\le E_n+V_{n,1}.
 \tag{31}
\]

We also need round 5's mean-sensitive first-projection bound. Here is
a derivation to specify the error used below. Write s(x) for the distance
to the boundary of Q and A_n=sqrt(n/(n-1)). The full-disk nearest-distance
tail up to s(x), and the homothetic-square tail above s(x), give

\[
 U_n(x)\le A_n+2\sqrt n\int_{s(x)}^\infty
                                e^{-(n-1)r^2/2}\,dr.
\]

The area of {x:s(x)<=r} is at most 4r, so Tonelli gives

\[
 \int_Q(U_n-1)_+\le A_n-1+\frac{8\sqrt n}{n-1}.
\]

For 0<=u<=2sqrt(2), u^2-u<=2sqrt(2)(u-1)_+. Therefore

\[
 V_{n,1}\le\mu_n(1-\mu_n)+\varepsilon_n,\qquad
 \varepsilon_n=2\sqrt2\left(A_n-1+\frac{8\sqrt n}{n-1}\right)
                  \longrightarrow0.
 \tag{32}
\]

The estimate holds even if mu_n exceeds one. From (4), (31), W_n>=0
and (32), because 1-alpha>0,

\[
 \begin{split}
 2\operatorname{Var}(L_n)
 &\le\kappa+(1-\alpha)\mu_n(1-\mu_n)
           -(1+\alpha)(\mu_n-c_*)^2
           +d_n+(1-\alpha)\varepsilon_n.
 \end{split}
 \tag{33}
\]

The elementary series gives
e=2+sum_{k>=2}1/k! <2+sum_{k>=2}2^{1-k}=3, as k!>=2^{k-1}
with strict inequality for k>=3. Hence 0<alpha<1.
To maximize the quadratic in mu_n, put t=mu_n-1/2 and b=c_*-1/2.
Then

\[
 \begin{split}
 &(1-\alpha)\mu_n(1-\mu_n)
                         -(1+\alpha)(\mu_n-c_*)^2\\
 &\quad=\frac{1-\alpha}{4}
       -2\left(t-\frac{1+\alpha}{2}b\right)^2
       -\frac{1-\alpha^2}{2}b^2\\
 &\quad\le\frac{1-\alpha}{4}-\frac{1-\alpha^2}{2}b^2.
 \end{split}
 \tag{34}
\]

This maximum over all real mu_n is valid without convergence or any
restriction on its subsequential limits. Equations (18), (33)-(34)
prove (5); dropping the final nonpositive term proves (6).

## 5. Strict comparison with the preceding upper bound

For t=9pi c^2, the deficit in (7) equals

\[
 \eta(c)=\frac{t^2e^{-t}}{20736\pi}
                      \le\frac1{5184\pi e^2}.
 \tag{35}
\]

Here t^2 exp(-t) has maximum 4/e^2, as its derivative is
t(2-t)exp(-t). The difference between round 5's upper bound and the
simpler bound (6) is exactly

\[
 \frac{K+1/4}{2}
       -\left(\frac\kappa2+\frac{1-e/4}{8}\right)
       =\frac e{32}-\frac{\eta(c_*)}{2}
       \ge\frac e{32}-\frac1{10368\pi e^2}>0.
 \tag{36}
\]

The final strict inequality follows already from e>1 and pi>1:
the positive term exceeds 1/32, and the subtracted term is less than
1/10368. Thus (5) also strictly improves the preceding bound.

## Scope and source

The new constraint couples the insertion energy to the first projection
and retains the variance of the averaged insertion cost. None of the
terms on its left is proved to converge. The tradeoff does not establish
interior homogeneity, convergence of
any fixed-order energy, or uniqueness of subsequential variance limits.
No comparison with the best published variance upper bound is claimed.

Sourav Chatterjee, *A general method for lower bounds on fluctuations
of random variables*, arXiv:1706.04290v3, Section 3, problem (2),
https://arxiv.org/html/1706.04290v3, states the variance-limit problem.
