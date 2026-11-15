# A centered insertion bound for the interaction energy

Let Q=[0,1]^2, and let X_1,...,X_n be independent uniform points of Q.
Write L_n for the length of the shortest closed Euclidean tour. A singleton
has length zero, and a tour through two points has twice their distance.
All lengths refer to the fixed square Q.

For A contained in [n], define

\[
 g_A=\mathbb E[L_n\mid X_A],\qquad
 h_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}g_B,
 \qquad
 V_{n,j}=\sum_{|A|=j}\mathbb E h_A^2\quad(1\le j\le n).
\]

Set V_{n,j}=0 for j>n, and put E_n=\sum_{j\ge1}jV_{n,j}.
Define

\[
 \operatorname{erfc}(t)=\frac2{\sqrt\pi}\int_t^\infty e^{-s^2}\,ds,
 \qquad
 F(c)=c^2+\frac4\pi e^{-\pi c^2}
             -2c\operatorname{erfc}(\sqrt\pi c),\quad c\ge0,
 \qquad
 \kappa=\min_{c\ge0}F(c).
 \tag{1}
\]

**Theorem.** The minimum in (1) has a unique minimizer c_*>0, determined
by

\[
 c_*=2c_*e^{-\pi c_*^2}+\operatorname{erfc}(\sqrt\pi c_*).
 \tag{2}
\]

For n>=2, E_n<=8, and

\[
 \limsup_{n\to\infty}E_n\le\kappa
 \le F(1/\sqrt\pi)
 <\frac{1+8/(3e)}\pi<\frac2\pi<\frac4\pi.
 \tag{3}
\]

In particular, for every integer m>=0,

\[
 \limsup_{n\to\infty}\sum_{j>m}V_{n,j}
 \le\frac\kappa{m+1}.
 \tag{4}
\]

If C_n(rho) is the covariance between optimal tour lengths of two n-point
samples formed by independently retaining each original point with
probability rho and otherwise replacing it uniformly, then

\[
 \limsup_{n\to\infty}
 \bigl(\operatorname{Var}(L_n)-C_n(\rho)\bigr)
 \le\kappa(1-\rho),\qquad 0\le\rho\le1.
 \tag{5}
\]

These bounds do not assert convergence of the variance or identify its
conjectured limit.

## 1. Orthogonal decomposition and deletion

All variables are square integrable since L_n<=n sqrt(2). Pairing the
terms indexed by B and B union {i} shows that, for i in A,
integrating h_A over X_i gives zero. Distinct h_A are therefore orthogonal:
if A and B differ, integrate their product over a coordinate in their
symmetric difference. Inclusion-exclusion also gives

\[
 L_n=\sum_{A\subseteq[n]}h_A,
 \qquad h_\varnothing=\mathbb E L_n.
\]

Consequently Var(L_n)=sum_{j>=1}V_{n,j}. Conditioning on X_{-i}
removes precisely the components indexed by sets containing i, so

\[
 \mathbb E\operatorname{Var}(L_n\mid X_{-i})
   =\sum_{A:i\in A}\mathbb E h_A^2.
\]

Summing in i counts each set A exactly |A| times. Symmetry gives

\[
 E_n=n\mathbb E\operatorname{Var}_X(d(X;S)\mid S),
 \quad
 d(x;S)=T(S\cup\{x\})-T(S),
 \tag{6}
\]

where S consists of n-1 independent uniform points and X is independent
uniform in Q. The notation Var_X means variance over X with S fixed.
The equality holds because T(S) is constant given S.

Let R(x,S) be the distance from x to its nearest point in S.
Deleting x from an optimal tour and shortcutting its neighbors proves
d(x;S)>=0. From an optimal tour of S, append the closed detour y,x,y at
a nearest point y. Shortcut repeated vertices to obtain a tour through
S union {x} of no greater length. A singleton S has the same detour
formula directly. Thus

\[
 0\le d(x;S)\le2R(x,S).
 \tag{7}
\]

There is no assumption that the optimal tour changes only locally.

## 2. A finite-n bound with a nonzero center

Fix c>=0. The conditional mean minimizes mean squared error over
constants, so

\[
 n\operatorname{Var}_X(d(X;S)\mid S)
 \le\mathbb E_X[(\sqrt n\,d(X;S)-c)^2\mid S].
\]

For 0<=u<=a, convexity of u maps to (u-c)^2 gives

\[
 (u-c)^2\le\max\{c^2,(a-c)^2\}.
\]

Apply this with u=sqrt(n)d and a=2sqrt(n)R, then average (6). With
Z_n=sqrt(n)R(X,S), this proves the exact finite-n inequality

\[
 E_n\le\mathbb E H_c(Z_n),
 \qquad H_c(z)=\max\{c^2,(2z-c)^2\}
             =c^2+4z(z-c)\mathbf1_{\{z>c\}}.
 \tag{8}
\]

For c=0 this recovers E_n<=4n E R^2.

## 3. The nearest-distance limit, including the boundary

For fixed x in Q and 0<=r<=sqrt(2), the set

\[
 x+\frac r{\sqrt2}(Q-x)
\]

lies in Q intersect B(x,r), by convexity and the diameter bound for Q.
Its area is r^2/2. Independence of the points in S implies

\[
 \mathbb P(R(x,S)^2>u)\le(1-u/2)^{n-1},\quad 0\le u\le2.
\]

Integration yields E[R(x,S)^2]<=2/n, uniformly in x, and therefore
E_n<=8.

For almost every fixed x (every interior x), and each fixed r>=0,
the disk of radius r/sqrt(n) lies in Q for all sufficiently large n.
Consequently

\[
 \mathbb P(Z_n>r\mid X=x)
  =(1-\pi r^2/n)^{n-1}\longrightarrow e^{-\pi r^2}.
\]

The expression on the left is used only once the disk lies in Q.
Dominated convergence in x gives P(Z_n>r)->exp(-pi r^2).
Moreover, uniformly in x and n>=2,

\[
 \mathbb P(Z_n>r\mid X=x)
 \le e^{-r^2/4},\quad r\ge0.
 \tag{9}
\]

Indeed, for r^2<=2n use (1-r^2/(2n))^{n-1}
<=exp(-(n-1)r^2/(2n))<=exp(-r^2/4). For r^2>2n the
probability is zero. This bound handles the entire boundary strip and
the unbounded scaled distances.

Since H_c is constant on [0,c] and has derivative 8r-4c on (c,infinity),
Tonelli's theorem gives

\[
 \mathbb E H_c(Z_n)
 =c^2+\int_c^\infty(8r-4c)\mathbb P(Z_n>r)\,dr.
 \tag{10}
\]

On this interval the integrand is nonnegative and at most
(8r+4c)exp(-r^2/4), an integrable function. Thus (9), (10), and
dominated convergence prove

\[
 \lim_{n\to\infty}\mathbb E H_c(Z_n)
 =c^2+\int_c^\infty(8r-4c)e^{-\pi r^2}\,dr=F(c).
 \tag{11}
\]

In the last equality, the integrals of r exp(-pi r^2) and
exp(-pi r^2) are exp(-pi c^2)/(2pi) and
erfc(sqrt(pi)c)/2, respectively. These yield exactly the coefficients
4/pi and -2c in (1).

Equations (8), (11) show limsup E_n<=F(c) for every fixed c>=0.

## 4. Optimization and an explicit strict improvement

Differentiating (1) gives

\[
 F'(c)=2c-4ce^{-\pi c^2}-2\operatorname{erfc}(\sqrt\pi c),
 \qquad F''(c)=2+8\pi c^2e^{-\pi c^2}>0.
 \tag{12}
\]

Here erfc'(t)=-(2/sqrt(pi))exp(-t^2). We have F'(0)=-2,
and F'(c) tends to infinity with c. Hence there is exactly one zero of
F', it is positive, it is the global minimizer, and it obeys (2).
Taking c=c_* in (11) proves the first inequality in (3).

For an explicit comparison take c=1/sqrt(pi). Put
I=integral_1^infinity exp(-t^2)dt. Integration by parts gives

\[
 I=\frac1{2e}-\frac12\int_1^\infty\frac{e^{-t^2}}{t^2}\,dt
   >\frac1{2e}-\frac12 I.
\]

The strict inequality holds because t^{-2}<1 on (1,infinity).
Thus I>1/(3e) and erfc(1)>2/(3e sqrt(pi)). Substitution gives

\[
 F(1/\sqrt\pi)
 =\frac{1+4/e}\pi-\frac2{\sqrt\pi}\operatorname{erfc}(1)
 <\frac{1+8/(3e)}\pi<\frac2\pi.
\]

The final strict inequality uses e>1+1+1/2+1/6=8/3.
No numerical approximation is needed for (3).

## 5. Consequences for the earlier reduction

Nonnegativity of the Hoeffding energies gives

\[
 \sum_{j>m}V_{n,j}\le\frac{E_n}{m+1}.
\]

This proves (4). Under independent retention with probability rho,
the conditional expectation of h_A evaluated on the modified sample,
given the original sample, is rho^{|A|}h_A. If any coordinate in A
is refreshed, its integral is zero; otherwise the component is unchanged.
Orthogonality therefore gives

\[
 C_n(\rho)=\sum_{j\ge1}\rho^j V_{n,j},\qquad
 0\le\operatorname{Var}(L_n)-C_n(\rho)
 \le(1-\rho)E_n.
\]

This proves (5). In particular limsup Var(L_n)<=kappa. If the
fixed-order energies converge to v_j, the earlier truncation argument
still gives convergence of the variance to sum_j v_j, with the improved
bound sum_j j v_j<=kappa. For the latter assertion, pass to the limit
in each finite weighted sum and then increase the truncation index.
Neither fixed-order convergence nor uniqueness of a subsequential
variance limit follows from these inequalities.

## 6. Sharpness for the scalar envelope information

The following observation specifies a limitation of this bound. Let Z
have tail P(Z>z)=exp(-pi z^2), z>=0. Among all jointly distributed
(Z,Y) satisfying 0<=Y<=2Z almost surely, the largest possible Var(Y)
is exactly kappa.

Indeed, for every such Y and every c>=0,

\[
 \operatorname{Var}(Y)\le\mathbb E(Y-c)^2
 \le\mathbb E H_c(Z)=F(c).
\]

For the reverse inequality set Y_*=2Z 1_{Z>c_*}.
Using the tail of Z,

\[
 \mathbb E[Z\mathbf1_{\{Z>c\}}]
 =ce^{-\pi c^2}+\frac12\operatorname{erfc}(\sqrt\pi c).
\]

Equation (2) therefore says E Y_*=c_*. For z<=c_* the farther
endpoint from c_* in [0,2z] is 0, and for z>c_* it is 2z.
Thus (Y_*-c_*)^2=H_{c_*}(Z) almost surely, and
Var(Y_*)=F(c_*)=kappa. This establishes sharpness for this scalar
constraint alone. It does not assert that a TSP insertion cost attains
this distribution, or that further geometry cannot improve (3).

## Reference and scope

Sourav Chatterjee, *A general method for lower bounds on fluctuations
of random variables*, arXiv:1706.04290, Section 3, problem (2),
https://arxiv.org/html/1706.04290v3, poses the variance-limit question.
The bound above concerns the optimal planar tour in the fixed square.
The constant kappa bounds the interaction energy; it is not a proposed
value for the conjectured variance limit. No comparison with the best
published upper variance constant is asserted.
