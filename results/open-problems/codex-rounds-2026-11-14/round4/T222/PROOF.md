# A strict improvement from spatial continuity of insertion costs

Let Q=[0,1]^2. For n independent uniform points in Q, let L_n be the
length of a shortest closed Euclidean tour. A singleton tour has length
zero; a two-point tour has twice the distance between its points. For
A contained in [n], put

\[
 h_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}
       \mathbb E[L_n\mid X_B],\qquad
 V_{n,j}=\sum_{|A|=j}\mathbb E h_A^2,\qquad
 E_n=\sum_{j=1}^n jV_{n,j}.
\]

Define, for c>=0,

\[
 F(c)=c^2+\frac4\pi e^{-\pi c^2}
             -2c\operatorname{erfc}(\sqrt\pi c),
 \qquad
 \operatorname{erfc}(t)=\frac2{\sqrt\pi}
                         \int_t^\infty e^{-s^2}\,ds.
 \tag{1}
\]

Let c_*>0 be the unique minimizer of F on [0,infinity), and write
kappa=F(c_*). For c>0 set

\[
 \eta(c)=\frac{\pi c^4}{256}e^{-9\pi c^2}.
 \tag{2}
\]

**Theorem.** For each fixed c>0,

\[
 \limsup_{n\to\infty}E_n\le F(c)-\eta(c).
 \tag{3}
\]

In particular, with K=kappa-eta(c_*),

\[
 \limsup_n E_n\le K<\kappa.
 \tag{4}
\]

These statements concern the exact optimal tour and do not assert that
its unscaled variance converges.

## 1. Conditional variance and spatial continuity

For a nonempty finite sample S, write T(S) for its optimal tour length,
and set

\[
 d(x;S)=T(S\cup\{x\})-T(S),\qquad
 R(x;S)=\min_{y\in S}|x-y|.
\]

Removing a point from a tour and shortcutting its neighbors gives
d(x;S)>=0. Adding the detour y,x,y at a nearest point y of a base
tour, and shortcutting repeated vertices, gives

\[
 0\le d(x;S)\le2R(x;S).
 \tag{5}
\]

This also holds when S is a singleton. Moving a tour vertex from x to z
changes each of its two incident edge lengths by at most |x-z|.
Applying this to an optimal tour and reversing x,z proves

\[
 |d(x;S)-d(z;S)|\le2|x-z|.
 \tag{6}
\]

One may regard tours as tours through a labeled list, allowing repeated
locations. Shortcutting shows that this gives the same optimum as the
set definition. Thus (6) holds also when x or z belongs to S.

The components h_A are orthogonal: integrating over any coordinate in A
annihilates h_A, by pairing terms in its defining sum. Also
L_n=sum_A h_A by inclusion-exclusion. It follows that

\[
 \operatorname{Var}(L_n)=\sum_j V_{n,j},\qquad
 E_n=\sum_{i=1}^n\mathbb E\operatorname{Var}(L_n\mid X_{-i}).
\]

Indeed, integrating out X_i removes exactly the components whose
supports contain i; their squared norms sum to the conditional-variance
expectation. Summing counts a support A exactly |A| times.
If S consists of n-1 independent uniform points and X is an independent
uniform point, symmetry and constancy of T(S) given S give

\[
 E_n=n\mathbb E\operatorname{Var}_X(d(X;S)\mid S).
 \tag{7}
\]

For fixed S,n,c define functions on Q by

\[
 u(x)=\sqrt n\,d(x;S),\quad r(x)=\sqrt n\,R(x;S),\quad
 H_c(r)=\max\{c^2,(2r-c)^2\},\quad
 q(x)=H_c(r(x))-(u(x)-c)^2.
 \tag{8}
\]

By (5) and convexity of the squared distance to c, q(x)>=0. Since the
conditional mean minimizes squared error, (7) yields

\[
 E_n\le \mathbb E H_c(\sqrt n R(X;S))
             -\mathbb E\int_Q q(x)\,dx.
 \tag{9}
\]

We will bound the second term below.

## 2. A deficit around each isolated base point

Fix c>0 and put e=(1,0). Call y in S admissible if

\[
 y\in Q_{n,c}:=[3c/\sqrt n,1-3c/\sqrt n]^2,
 \qquad |y-z|>3c/\sqrt n\quad(z\in S,\ z\ne y).
 \tag{10}
\]

We use this definition only for n>36c^2. Let N=N(S) count the
admissible points, and define the two open disks

\[
 A_y=B\left(y+\frac{5c}{8\sqrt n}e,
                    \frac{c}{8\sqrt n}\right),\qquad
 B_y=B\left(y+\frac{11c}{8\sqrt n}e,
                    \frac{c}{8\sqrt n}\right).
 \tag{11}
\]

Both lie in Q and within B(y,3c/(2sqrt(n))). Every other base point
is more than 3c/sqrt(n) from y, so y is a nearest point throughout
these disks: if |x-y|<3c/(2sqrt(n)), the triangle inequality gives
|x-z|>3c/sqrt(n)-|x-y|>|x-y|.
Consequently

\[
 \frac c2\le r(a)\le\frac{3c}4\quad(a\in A_y),\qquad
 \frac{5c}4\le r(b)\le\frac{3c}2\quad(b\in B_y).
 \tag{12}
\]

For a in A_y the first branch of H_c applies, and (5) implies
u(a)<=2r(a)<=3c/2. Therefore

\[
 q(a)=u(a)(2c-u(a))\ge\frac c2u(a).
 \tag{13}
\]

For b in B_y the second branch applies, and

\[
 \begin{split}
 q(b)&=(2r(b)-u(b))(2r(b)+u(b)-2c)\\
     &\ge\frac c2(2r(b)-u(b)),
 \end{split}
 \tag{14}
\]

because the first factor is nonnegative and the second is at least
2r(b)-2c>=c/2. The centers of the two disks are 3c/(4sqrt(n))
apart; adding their two radii gives
|a-b|<=c/sqrt(n). Equation (6) gives u(b)-u(a)<=2c, so

\[
 u(a)+2r(b)-u(b)\ge\frac{5c}2-2c=\frac c2.
\]

Combining (13) and (14), for every such pair,

\[
 q(a)+q(b)\ge\frac{c^2}4.
 \tag{15}
\]

The disks have equal area alpha=pi c^2/(64n). Integrate (15) over
A_y times B_y and divide by alpha. This proves

\[
 \int_{A_y}q+\int_{B_y}q\ge
       \frac{\pi c^4}{256n}.
 \tag{16}
\]

Different admissible sites have distance greater than 3c/sqrt(n).
Their open disks of radius 3c/(2sqrt(n)) are disjoint. The two disks
in (11) for a single site are disjoint as well. Since q is nonnegative
on the rest of Q, we may sum (16) without overcounting:

\[
 \int_Q q(x)\,dx\ge\frac{\pi c^4}{256n}N(S).
 \tag{17}
\]

This bound uses only (5), (6), and the stated isolation condition.

## 3. Expected count and a finite-sample bound

For a specified one of the n-1 sample points to be admissible, its
location y must lie in Q_{n,c}, of area (1-6c/sqrt(n))^2. For such a
y the entire disk B(y,3c/sqrt(n)) lies in Q and has area
9pi c^2/n. The remaining n-2 points must all avoid it. Independence
therefore gives, for n>36c^2 and n>=2,

\[
 \mathbb E N=(n-1)
       (1-6c/\sqrt n)^2
       (1-9\pi c^2/n)^{n-2}.
 \tag{18}
\]

The base of the last power is positive, since 9pi c^2/n<pi/4<1.
Combining (9), (17), and (18) gives the explicit finite-sample estimate

\[
 \begin{split}
 E_n\le{}&\mathbb E H_c(\sqrt n R(X;S))\\
 &-\frac{\pi c^4}{256}\frac{n-1}{n}
       (1-6c/\sqrt n)^2
       (1-9\pi c^2/n)^{n-2}.
 \end{split}
 \tag{19}
\]

No independence between the admissibility events for different sites
is needed in (18); only linearity of expectation is used.

## 4. Passing to the limit

For any x in Q and 0<=s<=sqrt(2), the square
x+(s/sqrt(2))(Q-x) has area s^2/2 and is contained in Q intersect
B(x,s). For Z_n=sqrt(n)R(X;S), this implies, uniformly in x and n>=2,

\[
 \mathbb P(Z_n>t\mid X=x)\le e^{-t^2/4}\quad(t\ge0).
 \tag{20}
\]

For t^2<=2n use the bound
(1-t^2/(2n))^{n-1}<=exp(-t^2/4); for larger t the probability is
zero. For each fixed interior x and t, the disk B(x,t/sqrt(n)) lies
in Q for sufficiently large n, giving

\[
 \mathbb P(Z_n>t\mid X=x)
 =(1-\pi t^2/n)^{n-1}\longrightarrow e^{-\pi t^2}.
\]

Integrating over x gives the same unconditional limit. The boundary has
area zero, and (20) controls the integrals uniformly near it. The function
H_c is constant on [0,c], with derivative 8t-4c on (c,infinity).
Thus

\[
 \mathbb E H_c(Z_n)=c^2+
       \int_c^\infty(8t-4c)\mathbb P(Z_n>t)\,dt.
\]

The integrable bound (8t+4c)exp(-t^2/4) permits dominated convergence.
Evaluation of the limiting integral gives

\[
 \mathbb E H_c(Z_n)\longrightarrow
 c^2+\frac4\pi e^{-\pi c^2}
            -2c\operatorname{erfc}(\sqrt\pi c)=F(c).
 \tag{21}
\]

The factor multiplying pi c^4/256 in the second line of (19)
converges to exp(-9pi c^2). This proves (3).

Finally,

\[
 F'(c)=2c-4ce^{-\pi c^2}-2\operatorname{erfc}(\sqrt\pi c),
 \qquad F''(c)=2+8\pi c^2e^{-\pi c^2}>0.
\]

Since F'(0)=-2 and F'(c) tends to infinity, F has a unique minimizer
c_*>0. Equivalently,

\[
 c_*=2c_*e^{-\pi c_*^2}+\operatorname{erfc}(\sqrt\pi c_*).
\]

Applying (3) at this fixed c_* proves (4), with strictness because
eta(c_*)>0. There is no interchange of minimization and limit.

## 5. Consequences and scope

Set V_{n,j}=0 for j>n. Nonnegativity of the energies gives, for m>=0,

\[
 \limsup_n\sum_{j>m}V_{n,j}\le\frac{K}{m+1}.
\]

For two n-point samples formed by independently retaining each point
with probability rho and otherwise replacing it uniformly, let C_n(rho)
be the covariance of their optimal tour lengths. Integrating a component
over any refreshed coordinate gives zero, so orthogonality gives
C_n(rho)=sum_j rho^j V_{n,j}. Since 1-rho^j<=j(1-rho),

\[
 \limsup_n(\operatorname{Var}(L_n)-C_n(\rho))\le K(1-\rho),
 \qquad 0\le\rho\le1.
\]

In particular limsup Var(L_n)<=K. These are stricter constants in the
earlier reduction. Neither convergence of V_{n,j} for fixed j nor
convergence of C_n(rho) for fixed rho is established. No value of a
limiting variance is proposed. Spatial continuity of the insertion cost
does not assert spatial localization of the changes in an optimal tour.

The variance-limit question is Section 3, problem (2), in Sourav
Chatterjee, *A general method for lower bounds on fluctuations of random
variables*, arXiv:1706.04290v3,
https://arxiv.org/html/1706.04290v3.
