# The first Hoeffding projection: boundary exclusion and an upper bound

Let Q=[0,1]^2. Let T(S) be the length of the shortest closed Euclidean
tour through a finite nonempty sample S, with T({x})=0 and a two-point
tour traversing its segment twice. Repeated locations do not change the
optimum. Let L_n=T({X_1,...,X_n}) for independent uniform points in Q.
All variances below refer to total length in the fixed square.

For S consisting of n-1 independent uniform points, define

\[
 d(x;S)=T(S\cup\{x\})-T(S),\qquad
 U_n(x)=\sqrt n\,\mathbb E_S d(x;S),\qquad
 \mu_n=\int_Q U_n(x)\,dx.
 \tag{1}
\]

The order-one Hoeffding energy is

\[
 V_{n,1}=n\operatorname{Var}(\mathbb E[L_n\mid X_1]).
 \tag{2}
\]

For 0<a<1/2 put

\[
 I_a=[a,1-a]^2,\qquad b_a=|Q\setminus I_a|=4a-4a^2,
\]

and define

\[
 \delta_n(a)=\sqrt{\frac n{n-1}}-1+
 \frac{2\sqrt n}{(n-1)a}\exp\left(-\frac{(n-1)a^2}{2}\right),
 \qquad n\ge2.
 \tag{3}
\]

Also set

\[
 \varepsilon_n=2\sqrt2\left\{
       \sqrt{\frac n{n-1}}-1+\frac{8\sqrt n}{n-1}\right\}.
 \tag{3a}
\]

**Theorem.** For n>=2 the following statements hold.

1. The first-order energy is exactly
   \(V_{n,1}=\operatorname{Var}(U_n(X))\), for X uniform in Q, and
   \(0\le U_n(x)\le2\sqrt2\) everywhere.
2. Uniformly for x in I_a, \(U_n(x)\le1+\delta_n(a)\). Consequently,

\[
 V_{n,1}\le\mu_n(1-\mu_n)
                +2\sqrt2\,\delta_n(a)+8b_a.
 \tag{4}
\]

3. If X_a is uniform in I_a and
   \(W_{n,a}=\operatorname{Var}(U_n(X_a))\), then

\[
 |V_{n,1}-W_{n,a}|\le8b_a,
 \qquad
 \int_{Q\setminus I_a}(U_n(x)-\mu_n)^2\,dx\le8b_a.
 \tag{5}
\]

4. An estimate without a chosen strip width is

\[
 V_{n,1}\le\mu_n(1-\mu_n)+\varepsilon_n,
 \qquad \varepsilon_n=O(n^{-1/2}).
 \tag{5a}
\]

In particular, for sufficiently large n set
\(a_n=\sqrt{8\log(n)/n}\). Then b_{a_n}->0,
\(\delta_n(a_n)\to0\), and

\[
 \begin{split}
 V_{n,1}&\le\mu_n(1-\mu_n)+O(n^{-1/2}),\\
 \limsup_{n\to\infty}V_{n,1}&\le\frac14,\qquad
 V_{n,1}-W_{n,a_n}\longrightarrow0.
 \end{split}
 \tag{6}
\]

The boundary exclusion in (5) also holds for every sequence of strip
widths tending to zero; the particular choice a_n is needed only for
the uniform interior upper bound with a vanishing error.

## 1. Insertion and the exact projection

Deleting x from an optimal tour through S union {x}, then shortcutting
its neighbors, proves d(x;S)>=0. At a nearest point y in S, append the
detour y,x,y to an optimal base tour. Shortcut repeated vertices. If
R(x;S)=min_{y in S}|x-y|, this proves

\[
 0\le d(x;S)\le2R(x;S).
 \tag{7}
\]

This argument includes a singleton base. The expectation of the base
tour is independent of the conditioned point, so

\[
 \mathbb E[L_n\mid X_1=x]=\mathbb E L_{n-1}
                              +\frac{U_n(x)}{\sqrt n}.
 \tag{8}
\]

Centering (8) proves (2) equals Var(U_n(X)). Integrating (8) also gives
the useful exact identity

\[
 \mu_n=\sqrt n\,(\mathbb E L_n-\mathbb E L_{n-1}).
 \tag{9}
\]

No limit of this difference is asserted.

For any x in Q and 0<=r<=sqrt(2), the homothetic square
x+(r/sqrt(2))(Q-x) lies in Q intersect B(x,r) and has area r^2/2.
Independence therefore gives, for 0<=t<=2,

\[
 \mathbb P(R(x;S)^2>t)\le(1-t/2)^{n-1}.
\]

Integrating gives E R(x;S)^2<=2/n. By (7) and Cauchy--Schwarz,

\[
 0\le U_n(x)\le2\sqrt n\,\mathbb E R(x;S)
       \le2\sqrt{n\mathbb E R(x;S)^2}\le2\sqrt2.
 \tag{10}
\]

In particular 0<=mu_n<=2sqrt(2). Every bound in (10) holds at the
edges and corners as well as in the interior.

## 2. A uniform interior range

Fix x in I_a. For 0<=r<=a the entire disk B(x,r) lies in Q, and
pi r^2<1 because a<1/2. Thus

\[
 \mathbb P(R(x;S)>r)=(1-\pi r^2)^{n-1}
                      \le e^{-\pi(n-1)r^2}.
 \tag{11}
\]

For a<=r<=sqrt(2), the homothetic-square bound instead gives

\[
 \mathbb P(R(x;S)>r)\le e^{-(n-1)r^2/2}.
 \tag{12}
\]

For larger r the probability is zero. Integrating these tails and
extending the two upper integrals to infinity gives

\[
 \begin{split}
 U_n(x)
 &\le 2\sqrt n\left\{
     \int_0^a e^{-\pi(n-1)r^2}\,dr
     +\int_a^\infty e^{-(n-1)r^2/2}\,dr\right\}\\
 &\le \sqrt{\frac n{n-1}}+
       \frac{2\sqrt n}{(n-1)a}e^{-(n-1)a^2/2}
   =1+\delta_n(a).
 \end{split}
 \tag{13}
\]

Here the first full Gaussian integral is 1/(2sqrt(n-1)). For the
second integral use r/a>=1 on [a,infinity), obtaining

\[
 \int_a^\infty e^{-(n-1)r^2/2}\,dr
 \le\frac1a\int_a^\infty r e^{-(n-1)r^2/2}\,dr
 =\frac{e^{-(n-1)a^2/2}}{(n-1)a}.
\]

Since U_n is nonnegative, (13) implies U_n^2<=(1+delta_n(a))U_n
on I_a. On its complement (10) implies U_n^2<=8. Consequently

\[
 \begin{split}
 V_{n,1}
 &=\int_Q U_n^2-\mu_n^2\\
 &\le(1+\delta_n(a))\int_{I_a}U_n+8b_a-\mu_n^2\\
 &\le(1+\delta_n(a))\mu_n+8b_a-\mu_n^2\\
 &\le\mu_n(1-\mu_n)+2\sqrt2\,\delta_n(a)+8b_a.
 \end{split}
 \tag{14}
\]

This is (4).

To prove the stronger integrated estimate (5a), let s(x) be the
distance from x to the boundary of Q, and put

\[
 A_n=\sqrt{n/(n-1)},\qquad
 D_n(x)=2\sqrt n\int_{s(x)}^\infty e^{-(n-1)r^2/2}\,dr.
\]

The same split-tail calculation as in (13), now splitting at s(x)
and retaining the unbounded tail integral, gives
U_n(x)<=A_n+D_n(x). This also holds when s(x)=0 or 1/2.
As A_n>=1, it follows that

\[
 (U_n(x)-1)_+\le A_n-1+D_n(x).
\]

For every r>=0 the set of x with s(x)<=r has area at most 4r.
For r<=1/2 its exact area is 4r-4r^2; for r>=1/2 its area is 1.
Tonelli's theorem therefore gives

\[
 \begin{split}
 \int_Q D_n(x)\,dx
 &=2\sqrt n\int_0^\infty e^{-(n-1)r^2/2}
                      |\{x:s(x)\le r\}|\,dr\\
 &\le8\sqrt n\int_0^\infty r e^{-(n-1)r^2/2}\,dr
 =\frac{8\sqrt n}{n-1}.
 \end{split}
 \tag{14a}
\]

For 0<=u<=2sqrt(2), one has
u^2-u=u(u-1)<=2sqrt(2)(u-1)_+. Integrating this inequality for U_n
and subtracting mu_n^2 proves

\[
 V_{n,1}\le\mu_n(1-\mu_n)
       +2\sqrt2\left(A_n-1+\frac{8\sqrt n}{n-1}\right).
\]

This is (5a), and its error is O(n^{-1/2}).

## 3. Removing a boundary strip

Write p=1-b_a and let m_I=E[U_n(X_a)]. Both m_I and mu_n belong
to [0,2sqrt(2)], by (10). The same range bound gives

\[
 \int_{Q\setminus I_a}(U_n(x)-\mu_n)^2\,dx\le8b_a.
 \tag{15}
\]

For the comparison of variances, the conditional-variance decomposition
with respect to the event X in I_a gives

\[
 V_{n,1}\ge p W_{n,a}.
 \tag{16}
\]

For the opposite direction, center at m_I rather than at the global
mean. The mean minimizes squared error, so

\[
 V_{n,1}\le\int_Q(U_n(x)-m_I)^2\,dx
        \le pW_{n,a}+8b_a.
 \tag{17}
\]

Also W_{n,a}<=8 by (10). Subtracting W_{n,a} from (16)-(17)
therefore bounds the difference below by -8b_a and above by 8b_a.
Together with (15), this proves (5). This step makes no assumption
that the mean near the boundary agrees with the interior mean.

## 4. An explicit shrinking strip

For a_n=sqrt(8 log(n)/n), eventually a_n<1/2. Since n>=2,

\[
 e^{-(n-1)a_n^2/2}
 =n^{-4(n-1)/n}\le n^{-2},\qquad
 \frac{\sqrt n}{(n-1)a_n}
 =\frac{n}{(n-1)\sqrt{8\log n}}
 \le\frac{2}{\sqrt{8\log n}}.
 \tag{18}
\]

Moreover, by rationalizing the square root,

\[
 \sqrt{\frac n{n-1}}-1
 =\frac{1/(n-1)}{\sqrt{n/(n-1)}+1}
 \le\frac1{2(n-1)}.
\]

It follows that

\[
 \delta_n(a_n)\le\frac1{2(n-1)}
              +\frac{4n^{-2}}{\sqrt{8\log n}},\qquad
 b_{a_n}\le4\sqrt{\frac{8\log n}{n}}.
 \tag{19}
\]

Equations (5), (5a), and (19) prove (6), using
mu(1-mu)=1/4-(mu-1/2)^2<=1/4. Neither a limit of mu_n nor a
limit of U_n has been used.

## 5. Consequence for the total variance

For completeness, define the other Hoeffding components by

\[
 h_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}
           \mathbb E[L_n\mid X_B],\qquad
 V_{n,j}=\sum_{|A|=j}\mathbb E h_A^2.
\]

Integrating h_A in a coordinate belonging to A gives zero, by pairing
the two corresponding terms. This proves orthogonality for different
supports. Inclusion-exclusion gives L_n=sum_A h_A, hence
Var(L_n)=sum_{j>=1}V_{n,j}. Put E_n=sum_{j>=1}jV_{n,j}.
All energies are nonnegative, so

\[
 2\operatorname{Var}(L_n)
 \le V_{n,1}+E_n.
 \tag{20}
\]

The verified predecessor result is limsup E_n<=K, where

\[
 \begin{split}
 F(c)&=c^2+\frac4\pi e^{-\pi c^2}
                  -2c\operatorname{erfc}(\sqrt\pi c),\\
 c_*&=\arg\min_{c\ge0}F(c),\qquad
 K=F(c_*)-\frac{\pi c_*^4}{256}e^{-9\pi c_*^2}.
 \end{split}
 \tag{21}
\]

Here erfc(t)=(2/sqrt(pi)) integral_t^infinity exp(-s^2) ds.
This bound is established in round 4's PROOF.md, with the recheck in
LOG.md and AUDIT.md here. Combining (6), (20), and that bound yields

\[
 \boxed{\displaystyle
 \limsup_{n\to\infty}\operatorname{Var}(L_n)
             \le\frac{K+1/4}{2}.}
 \tag{22}
\]

This is strictly smaller than K. To check the strict comparison without
numerical optimization, let Z have tail exp(-pi z^2). For every c>=0,
the pointwise endpoint envelope H_c(Z)=max(c^2,(2Z-c)^2) is at least
(Z-c)^2+Z^2: the average of its two arguments is exactly this quantity.
As F(c)=E H_c(Z), E Z=1/2 and E Z^2=1/pi give

\[
 F(c)\ge\operatorname{Var}(Z)+\mathbb E Z^2
       =\frac2\pi-\frac14.
\]

Writing t=9pi c^2 gives

\[
 \frac{\pi c^4}{256}e^{-9\pi c^2}
   =\frac{t^2e^{-t}}{20736\pi}
   \le\frac1{5184\pi e^2}.
\]

The last inequality follows by differentiating t^2 exp(-t), whose
maximum for t>=0 is 4/e^2. Thus, using pi<22/7, pi>1, and e>1,

\[
 K>\frac7{11}-\frac14-\frac1{5184}
   >\frac14.
\]

The final rational inequality follows from 3/22>1/5184. Therefore
(K+1/4)/2<K, as claimed. No decimal value or comparison with the best
published variance upper bound is asserted.

## Scope

The boundary part of the first-order energy is negligible even for a
shrinking strip. The variance-limit conjecture still requires additional
information: these estimates do not prove that the interior profiles
U_n become constant or that their variances converge. In particular,
(9) and a first-order law for E L_n alone do not justify taking a limit
of the normalized consecutive difference mu_n. The upper bound (22)
does not establish convergence of Var(L_n).

The original question appears in Sourav Chatterjee,
*A general method for lower bounds on fluctuations of random variables*,
arXiv:1706.04290v3, Section 3, problem (2),
https://arxiv.org/html/1706.04290v3.
