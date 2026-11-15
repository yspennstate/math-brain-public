# Removing the radial spike from wide ReLU prediction dynamics

The first layer is fixed. A rank-one perturbation estimate closes the remaining dynamical step in the preceding ReLU reductions. Its consequence is an actual realized-risk limit for standard Gaussian inputs and a Gaussian random linear teacher. This limit has at most one minimum.

## 1. A rank-one flow lemma

All vector norms are Euclidean and all matrix norms are operator norms. Let $A$ be a real symmetric $n\times n$ matrix, $a\in\mathbb R^n$, and $\mu>0$. Assume
\[
 \kappa I\preceq A\preceq MI,\qquad 0<\kappa\leq M.
 \tag{1}
\]
Put $B=A+\mu aa^T$ and $H_t(C)=\int_0^t e^{-uC}\,du$. Let $y$ be a random vector satisfying the second-moment bound
\[
 \mathbb E[yy^T]\preceq C_y I.
 \tag{2}
\]
In this lemma $A,a,\mu$ are deterministic. The same conclusions hold conditionally when they are measurable with respect to a sigma field and (2) holds conditionally. Gaussianity is not required.

Define
\[
 z(t)=a^TH_t(B)y,\qquad
 \delta(t)=[H_t(B)-H_t(A)]y.
\]
If $a\ne0$, then
\[
 \mathbb E\sup_{t\geq0}|z(t)|
 \leq\frac{\sqrt{C_y}}{\mu\|a\|}
                  \left(1+\frac M\kappa\right).
 \tag{3}
\]
Moreover, including the case $a=0$,
\[
 \mathbb E\sup_{t\geq0}\|\delta(t)\|
 \leq\frac{\sqrt{C_y}}\kappa\left(1+\frac M\kappa\right),
 \tag{4}
\]
\[
 \mathbb E\sup_{t\geq0}\|\delta'(t)\|
 \leq\sqrt{C_y}\left(1+\frac M\kappa\right)^2.
 \tag{5}
\]
Thus for any deterministic linear map $P$, the left sides of (4), (5), after applying $P$, are bounded by the respective right sides times $\|P\|$. These constants do not grow with the spike eigenvalue.

### Proof

Suppose first $a\ne0$ and write $g=\|a\|$ and $\lambda=\mu g^2>0$. The identity $(B-\lambda I)a=Aa$ gives the exact vector formula
\[
 e^{-tB}a=e^{-\lambda t}a
       -\int_0^t e^{-(t-u)B}Aa\,e^{-\lambda u}\,du.
 \tag{6}
\]
To verify its sign and order, differentiate
$F(u)=e^{-(t-u)B}e^{-\lambda u}a$. Then
$F'(u)=e^{-(t-u)B}(B-\lambda I)a e^{-\lambda u}
=e^{-(t-u)B}Aa e^{-\lambda u}$.
Integrating $F'$ from zero to $t$ proves (6).

Since $B\succeq\kappa I$, (1) and (6) imply
\[
 \|e^{-tB}a\|
 \leq g e^{-\lambda t}
       +Mg\int_0^t e^{-\kappa(t-u)}e^{-\lambda u}\,du.
\]
Both terms are nonnegative. Integrate in $t$ and use Tonelli's theorem on the double integral, with $v=t-u$:
\[
 \begin{aligned}
 \int_0^\infty\|e^{-tB}a\|\,dt
 &\leq\frac g\lambda
       +Mg\int_0^\infty\int_0^\infty
                  e^{-\kappa v}e^{-\lambda u}\,dv\,du\\
 &=\frac g\lambda\left(1+\frac M\kappa\right)
 =\frac1{\mu g}\left(1+\frac M\kappa\right).
 \end{aligned}
 \tag{7}
\]
This bound includes the case $\lambda=\kappa$; no subtraction of decay rates was used.

Symmetry of $B$ gives $z(t)=\int_0^t(e^{-uB}a)^Ty\,du$. For every deterministic vector $v$, Cauchy–Schwarz and (2) give
$\mathbb E|v^Ty|\leq\sqrt{\mathbb E(v^Ty)^2}\leq\sqrt{C_y}\|v\|$.
Consequently
\[
 \mathbb E\sup_{t\geq0}|z(t)|
 \leq\mathbb E\int_0^\infty|(e^{-uB}a)^Ty|\,du
 \leq\sqrt{C_y}\int_0^\infty\|e^{-uB}a\|\,du.
\]
Tonelli applies again, and (7) proves (3). The integral also shows that the supremum is integrable and that $z(t)$ has a limit. Continuity permits taking all suprema over rational times, so there is no measurability issue.

Write $b_B(t)=H_t(B)y$ and $b_A(t)=H_t(A)y$. They solve
$b_B'=y-Bb_B$, $b_A'=y-Ab_A$, with both initial values zero. Subtraction yields
\[
 \delta'=-A\delta-\mu a z(t),\qquad \delta(0)=0,
 \quad
 \delta(t)=-\mu\int_0^t e^{-(t-u)A}a z(u)\,du.
 \tag{8}
\]
It follows pathwise that
\[
 \sup_t\|\delta(t)\|\leq\frac{\mu g}\kappa\sup_t|z(t)|,
 \qquad
 \sup_t\|\delta'(t)\|
 \leq M\sup_t\|\delta(t)\|+\mu g\sup_t|z(t)|.
 \tag{9}
\]
Insert (3). The first estimate gives (4), and the second gives
$\sqrt{C_y}(M/\kappa+1)(1+M/\kappa)$, which is (5). If $a=0$, $B=A$ and $\delta=0$, proving the remaining case.

## 2. Application to the radial ReLU matrix

Let $n,d\to\infty$, $d/n\to\gamma\in(0,\infty)$, and let $X\in\mathbb R^{n\times d}$ have independent standard Gaussian entries. Independently let
\[
 \beta\sim N(0,(E/d)I_d),\quad
 \varepsilon\sim N(0,s^2I_n),\quad y=X\beta+\varepsilon,
 \qquad E,s^2\geq0.
 \tag{10}
\]
Set
\[
 a_i=\|x_i\|/\sqrt d,\quad
 c=\frac14-\frac1{2\pi}>0,\quad
 \mu_d=d\left[\frac{\Gamma(d/2)}{2\sqrt\pi\Gamma((d+1)/2)}\right]^2,
\]
\[
 A=\frac{XX^T}{4d}+cI_n,\quad B=A+\mu_d aa^T,
 \qquad P=\frac{X^T}{4d}.
 \tag{11}
\]
Then for $j=0,1$,
\[
 \sup_{t\geq0}
 \left\|P\,\partial_t^j[H_t(B)-H_t(A)]y\right\|
       =O_{\mathbb P}(n^{-1/2}).
 \tag{12}
\]
In addition, $\sup_t|a^TH_t(B)y|=O_{\mathbb P}(n^{-1/2})$.

Here are the probability details. There are fixed constants $M_0,C_0,P_0>0$ such that, on events $\mathcal E_n$ determined by $X$ and having probability tending to one,
\[
 cI\preceq A\preceq M_0I,\quad
 \mathbb E[yy^T\mid X]=(E/d)XX^T+s^2I\preceq C_0I,
 \quad\|P\|\leq P_0n^{-1/2}.
 \tag{13}
\]
For a direct bound on $X$, take $1/4$-nets of both unit spheres, of cardinalities at most $9^n$ and $9^d$. Approximating the arguments of a bilinear form shows
$\|X\|\leq2\max_{u,v\text{ in nets}}|u^TXv|$. Each fixed bilinear form is standard Gaussian, so
\[
 \mathbb P(\|X\|>6\sqrt{n+d})
 \leq2\exp\{(n+d)(\log9-9/2)\}\longrightarrow0.
\]
Since $n/d$ stays between positive constants, this proves (13). Also
$\mathbb E\|a\|^2=n$ and $\operatorname{Var}(\|a\|^2)=2n/d$, so $\|a\|^2/n\to1$ in probability. The spherical expansion from the preceding kernel lemma gives
$\mu_d=1/(2\pi)+1/(4\pi d)+O(d^{-2})$, so it stays bounded away from zero.

Apply (3)--(5) conditionally on $X$. On $\mathcal E_n$ their constants are fixed and $\|P\|\leq P_0n^{-1/2}$. Conditional Markov's inequality gives, for $j=0,1$ and $L>0$,
\[
 \mathbb P\left(\sup_t\|P\delta^{(j)}(t)\|>Ln^{-1/2}\right)
 \leq\mathbb P(\mathcal E_n^c)+\frac{C_j}{L}.
 \tag{14}
\]
Let first dimensions and then $L$ tend to infinity. This proves (12). The same argument using (3) and $\|a\|\asymp\sqrt n$ proves the radial bound. No independence between $a$ and $X$ has been assumed.

## 3. Consequence for the actual network risk

Consider independent $w_1,\ldots,w_m\sim N(0,I_d)$, independent also of (10) and $X$, and the network
\[
 f_\alpha(x)=\frac1{\sqrt m}\sum_{r=1}^m
       \alpha_r\max(w_r^Tx/\sqrt d,0).
 \tag{15}
\]
Only $\alpha$ is trained, from $\alpha(0)=0$, by full-batch gradient flow for the half-sum loss
$\frac12\sum_i(f_\alpha(x_i)-y_i)^2$. Assume $m/n^2\to\infty$. With an independent test input $x\sim N(0,I_d)$ and centered independent test noise of variance $s^2$, let
\[
 R_m(t)=s^2+\|f_{\alpha(t)}-x^T\beta\|_{L^2(N(0,I_d))}^2.
 \tag{16}
\]
This risk conditions on the realized training data, teacher, and random features; it is not their average.

The two previously established ReLU inputs are as follows. Write $\Phi_{ir}=m^{-1/2}\max(w_r^Tx_i/\sqrt d,0)$ and $K_m=\Phi\Phi^T$.

* Round 4, equation (6): uniformly for $t\geq0$,
  $R_m(t)-s^2-\|PH_t(K_m)y-\beta\|^2=o_{\mathbb P}(1)$.
* Round 5, equation (8):
  $\|K_m-B\|=O_{\mathbb P}(d^{-1/4}+n/\sqrt m)=o_{\mathbb P}(1)$.

These are inputs to this corollary; the new rank-one argument is Sections 1--2. The first input uses the orthogonal decomposition of the ReLU test kernel into $Xx/(4d)$, its radial mean $\mu_d a\|x\|/\sqrt d$, and an even remainder of test-operator norm $O_{\mathbb P}(d^{-1})$. The radial term vanishes under (10). The second input retains the quadratic radial mean and its diagonal; it does not remove the spike in operator norm.

For completeness, the passage between the second input and the new lemma is uniform in time despite the large spike. Since $B\succeq cI$, with probability tending to one also $K_m\succeq(c/2)I$. For symmetric $C,D\succeq\kappa I$, Duhamel's formula gives
\[
 \|e^{-uC}-e^{-uD}\|\leq u e^{-\kappa u}\|C-D\|,
 \quad
 \sup_t\|H_t(C)-H_t(D)\|\leq\kappa^{-2}\|C-D\|.
 \tag{17}
\]
Indeed the exponential difference is an integral over a length-$u$ interval; the two exponential norms multiply to at most $e^{-\kappa u}$. Integrating $u e^{-\kappa u}$ from zero to infinity proves the second inequality. No upper spectral bound is needed in (17).

Because $\|y\|=O_{\mathbb P}(\sqrt n)$ and $\|P\|=O_{\mathbb P}(n^{-1/2})$, (17) and the second input show
\[
 \sup_t\|P[H_t(K_m)-H_t(B)]y\|=o_{\mathbb P}(1).
\]
Combine this with (12) at $j=0$. The predictors $PH_t(K_m)y$, $PH_t(B)y$, and $PH_t(A)y$ are uniformly bounded in probability, since all matrices have a fixed lower gap and $\|P\|\|y\|=O_{\mathbb P}(1)$. Also $\|\beta\|=O_{\mathbb P}(1)$. Applying
$|\|u\|^2-\|v\|^2|\leq\|u-v\|(\|u\|+\|v\|)$ and the first input gives
\[
 \sup_{t\geq0}|R_m(t)-R_0(t)|\xrightarrow{\mathbb P}0,
 \qquad R_0(t)=s^2+\|PH_t(A)y-\beta\|^2.
 \tag{18}
\]
The same reasoning applies to the infinite-width ReLU kernel predictor, using the infinite-width versions of the two inputs.

## 4. Explicit limiting risk

Put $T=X^TX/(4d)$ and
\[
 h_t(\ell)=\frac{1-e^{-(\ell+c)t}}{\ell+c},\qquad
 \theta(t)=PH_t(A)y.
\]
The identity $X^Te^{-tA}=e^{-t(T+cI)}X^T$, proved by the power series, implies
\[
 \theta(t)=h_t(T)\left(T\beta+\frac{X^T\varepsilon}{4d}\right),
 \quad
 \theta(t)-\beta=U_t\beta+V_t\varepsilon,
\]
\[
 U_t=T h_t(T)-I_d,\qquad V_t=\frac1{4d}h_t(T)X^T.
 \tag{19}
\]
Conditional on $X$, the cross term has zero mean and
$\operatorname{Cov}(X^T\varepsilon/(4d))=(s^2/(4d))T$. Hence
\[
 \overline R_X(t):=\mathbb E[R_0(t)\mid X]
 =s^2+\frac1d\operatorname{tr}
       \left[E(I-T h_t(T))^2+\frac{s^2}4 T h_t(T)^2\right].
 \tag{20}
\]

We next justify passing from this conditional mean to the realized risk, including all times. Write
$\beta=\sqrt{E/d}\,g$ and $\varepsilon=s\eta$, where $g,\eta$ are independent standard Gaussian vectors, and put
\[
 Z=(g,\eta),\quad L_t=[\sqrt{E/d}\,U_t\ \ sV_t],\quad Q_t=L_t^TL_t.
\]
On the norm event for $X$ used in (13), (19) and $c>0$ give, with constants independent of time and dimension,
\[
 \sup_t(\|L_t\|+\|L_t'\|)\leq C d^{-1/2},\quad
 \|L_t-L_\infty\|\leq C d^{-1/2}e^{-ct}.
 \tag{21}
\]
For the derivative bound use $h_t'(T)=e^{-t(T+cI)}$; the tail bound follows from
$h_\infty(T)-h_t(T)=(T+cI)^{-1}e^{-t(T+cI)}$.
Therefore $\|Q_t\|\leq C/d$, $\|Q_t'\|\leq C/d$, and
$\|Q_t-Q_\infty\|\leq C e^{-ct}/d$. The dimension of $Q_t$ is $d+n=O(d)$. Gaussian fourth moments yield
\[
 \mathbb E[Z^TQ_tZ\mid X]=\operatorname{tr}Q_t,
 \quad
 \operatorname{Var}(Z^TQ_tZ\mid X)=2\operatorname{tr}Q_t^2\leq C/d.
 \tag{22}
\]
This formula also holds at $t=\infty$.

Fix $U<\infty$ and a mesh size $h>0$. Chebyshev's inequality and a finite union bound give convergence to zero of
$Z^TQ_tZ-\operatorname{tr}Q_t$ at the grid points in $[0,U]$. Between grid points the absolute derivative of this centered expression is at most
$C(\|Z\|^2/d+(d+n)/d)=O_{\mathbb P}(1)$ by (21). Its supremum is therefore bounded by the grid maximum plus $O_{\mathbb P}(h)$. First take dimensions to infinity with $h$ fixed and then $h\downarrow0$.

For $t\geq U$, its difference from the centered expression at infinity is bounded by
$C e^{-cU}(\|Z\|^2/d+(d+n)/d)$. The expression at infinity tends to zero by (22), and $\|Z\|^2/d=O_{\mathbb P}(1)$. Sending $U\to\infty$ after dimensions proves
\[
 \sup_{t\geq0}|R_0(t)-\overline R_X(t)|\xrightarrow{\mathbb P}0.
 \tag{23}
\]

The standard Gaussian sample-covariance theorem gives the weak limit of the empirical eigenvalue law of $T$:
\[
 \ell_\pm=\frac{(1\pm\sqrt\gamma)^2}{4\gamma},\qquad
 \nu_\gamma(d\ell)=(1-\gamma^{-1})_+\delta_0(d\ell)
 +\frac2\pi\frac{\sqrt{(\ell_+-\ell)(\ell-\ell_-)}}\ell
       \mathbf1_{(\ell_-,\ell_+)}\,d\ell.
 \tag{24}
\]
The reference is V. A. Marchenko and L. A. Pastur, *Distribution of eigenvalues for some sets of random matrices*, Mathematics of the USSR-Sbornik 1:4 (1967), 457–483 ([paper page](https://www.mathnet.ru/eng/sm4101)). Specifically, the law of $X^TX/n$ has atom $(1-\gamma^{-1})_+$ and density
$\sqrt{((1+\sqrt\gamma)^2-u)(u-(1-\sqrt\gamma)^2)}/(2\pi\gamma u)$ on its positive interval. Scaling by $n/(4d)\to1/(4\gamma)$ gives exactly (24).

The limiting actual risk is
\[
 \mathcal R(t)=s^2+\int\left[
 E\left(\frac{c+\ell e^{-t(\ell+c)}}{\ell+c}\right)^2
 +\frac{s^2}4\frac{\ell}{(\ell+c)^2}
              (1-e^{-t(\ell+c)})^2\right]\nu_\gamma(d\ell).
 \tag{25}
\]
In particular,
\[
 \boxed{\ \sup_{t\geq0}|R_m(t)-\mathcal R(t)|
                       \xrightarrow{\mathbb P}0.\ }
 \tag{26}
\]
To justify time uniformity of the spectral step, on the norm event the empirical support and the limiting support are in one fixed compact interval. The integrand in (20) is continuous there, including at zero, because $c>0$, and is uniformly Lipschitz in time. Weak convergence and a finite time grid therefore give uniform convergence on $[0,U]$. Its difference from its limit as $t\to\infty$ is uniformly $O(e^{-ct})$ in $\ell$ on that interval. Applying weak convergence also at $t=\infty$ and then sending $U\to\infty$ proves the all-time spectral convergence. Equations (18), (23) prove (26).

## 5. Shape of the limiting curve

The one-minimum profile theorem from the initial predecessor now applies to an actual ReLU risk limit. Here is its sign argument with the constants in (25). Put $b_0=s^2/4$ and $D=b_0-Ec$. Differentiation under the compactly supported integral gives
\[
 F(t):=\frac12\mathcal R'(t)
 =\int_{\ell>0}\frac\ell{\ell+c}
    [D e^{-t(\ell+c)}-(E\ell+b_0)e^{-2t(\ell+c)}]
          \,\nu_\gamma(d\ell).
 \tag{27}
\]
If $E>0,D\leq0$, this is strictly negative at every finite time. If $E=0<s^2$, it is positive for $t>0$. If both vanish the risk is zero.

Suppose $E>0,D>0$. Set $a_0=c+\ell_-$, $a_1=c+\ell_+$, and
\[
 w(k)=\frac2\pi\frac{\sqrt{(a_1-k)(k-a_0)}}k
                   \mathbf1_{(a_0,a_1)}(k),\qquad
 h(k)=D w(k)-\tfrac12(Ek/2+D)w(k/2).
 \tag{28}
\]
Changing variable $k=2(\ell+c)$ in the second term of (27) gives
$F(t)=\int e^{-kt}h(k)\,dk$. If $a_1\leq2a_0$, the supports immediately show that $h$ is nonnegative then nonpositive, with strict signs on intervals. If $2a_0<a_1$, the ratio of the subtracted term to $w(k)$ on the overlap is
\[
 Q(k)=(Ek/2+D)
 \sqrt{\frac{a_1-k/2}{a_1-k}\frac{k/2-a_0}{k-a_0}}.
 \tag{29}
\]
The two rational factors have respective derivatives
$a_1/[2(a_1-k)^2]>0$ and $a_0/[2(k-a_0)^2]>0$. Since $a_0\geq c>0$, $Q$ increases strictly from zero to infinity. There is a unique $r$ in the overlap with $Q(r)=D$. This gives $h\geq0$ below $r$ and $h\leq0$ above $r$. In the disjoint-support case choose any separator $r\in[a_1,2a_0]$ instead.

In both cases
\[
 (e^{rt}F(t))'=\int(r-k)e^{(r-k)t}h(k)\,dk>0.
 \tag{30}
\]
The strict inequality follows from the strict signs on intervals. Also
$F(0)=-E\int k w(k)\,dk<0$. Choose $u<r$ such that $H=\int_{k\leq u}h(k)\,dk>0$, and set $N=\int_{k>r}|h(k)|\,dk$. Then
$F(t)\geq H e^{-ut}-N e^{-rt}>0$ eventually. Thus $F$ has exactly one zero $t_*>0$; (30) at that zero gives $F'(t_*)>0$.

Consequently, for $E>0$ the limit is strictly decreasing when $s^2/4\leq Ec$, and has exactly one nondegenerate interior minimum when $s^2/4>Ec$. It never has an interior local maximum. This classifies the limiting curve; (26) alone does not assert the number of finite-sample critical points.

## 6. Independent checks and scope

**The endpoint inverse check.** Direct multiplication gives
\[
 B^{-1}=A^{-1}
 -\frac{\mu A^{-1}aa^TA^{-1}}{1+\mu a^TA^{-1}a}.
 \tag{31}
\]
Thus $B^{-1}a=A^{-1}a/(1+\mu a^TA^{-1}a)$, of norm $O(n^{-1/2})$ when $\|a\|\asymp\sqrt n$ and $\mu$ stays positive. This independently checks the scale in (3). Furthermore $A^{-1}-B^{-1}$ is positive semidefinite of rank at most one, with norm at most $1/\kappa$, since it is bounded above by $A^{-1}$. Therefore (2) implies
$\mathbb E\|\delta(\infty)\|^2\leq C_y/\kappa^2$, independently confirming the order-one coefficient scale in (4). This endpoint calculation does not replace the all-time proof.

**An exactly diagonal check.** Take $A=\kappa I$, $a=\sqrt n\,e_1$, and $y_1\sim N(0,1)$. Then
\[
 z(t)=\sqrt n\,\frac{1-e^{-(\kappa+\mu n)t}}{\kappa+\mu n}\,y_1,
\]
\[
 \delta(t)=\left[
 \frac{1-e^{-(\kappa+\mu n)t}}{\kappa+\mu n}
 -\frac{1-e^{-\kappa t}}\kappa\right]y_1e_1,
\quad
 \delta'(t)=[e^{-(\kappa+\mu n)t}-e^{-\kappa t}]y_1e_1.
 \tag{32}
\]
These formulas verify the sign in (8), the order $n^{-1/2}$ for $z$, and the order-one all-time bounds for $\delta,\delta'$. They also give $\delta(0)=\delta'(0)=0$, as required.

The moment assumption cannot be replaced by $\|y\|=O(\sqrt n)$ alone in this general lemma. In (32), instead choose $y=a$ and $P=n^{-1/2}I$. Then $P\delta(\infty)\to-\kappa^{-1}e_1$. Here $yy^T$ has norm $n$, violating (2); the projection no longer makes the spike effect vanish.

**Risk constants checked from the ODE.** Equation (19) also solves
$\theta'=-(T+cI)\theta+X^Ty/(4d)$, $\theta(0)=0$. Differentiating squared error at zero and averaging gives
\[
 \overline R_X'(0)=-\frac{2E}{d}\operatorname{tr}T,
 \quad
 \overline R_X''(0)=\frac1d\operatorname{tr}
          [4ET^2+2EcT+(s^2/2)T].
 \tag{33}
\]
The noise term comes from twice its forcing variance $(s^2/(4d))T$; the signal terms come from $\theta'(0)=T\beta+X^T\varepsilon/(4d)$ and $\theta''(0)=-(T+cI)\theta'(0)$. These match direct differentiation of (25). Independently,
$\mathbb E\operatorname{tr}(X^TX)=nd$ and
$\mathbb E\operatorname{tr}((X^TX)^2)=nd(n+d+1)$, by splitting
$\sum_{i,j}(x_i^Tx_j)^2$ into diagonal and off-diagonal terms. Therefore the limiting moments are
$\int\ell\,d\nu_\gamma=1/(4\gamma)$ and
$\int\ell^2\,d\nu_\gamma=(1+\gamma)/(16\gamma^2)$, giving
\[
 \mathcal R'(0)=-\frac E{2\gamma},\qquad
 \mathcal R''(0)=\frac{E(1+\gamma)}{4\gamma^2}
                   +\frac{Ec}{2\gamma}+\frac{s^2}{8\gamma}.
 \tag{34}
\]
The first moment also follows from the semicircle-area integral in (24), independently checking its scale. These checks fix the coefficient $s^2/4$ in (25).

**Why no full-risk derivative assertion follows.** The first-derivative estimate (12) concerns the linear prediction. In the diagonal example above, the radial squared contribution $r_n(t)=\mu^2 z(t)^2$ obeys $\sup_t r_n(t)=O_{\mathbb P}(1/n)$, but for fixed $\tau>0$,
\[
 r_n'(\tau/n)
 =\frac{2\mu^2n}{\kappa+\mu n}
       (1-e^{-(\kappa+\mu n)\tau/n})e^{-(\kappa+\mu n)\tau/n}y_1^2
 \quad\Longrightarrow\quad
 2\mu(1-e^{-\mu\tau})e^{-\mu\tau}\chi_1^2.
 \tag{35}
\]
This nonvanishing limit shows the failure of that implication even for an explicit radial component. It is a check on the inference, not a claim that the diagonal example is the Gaussian network. The second derivative of the linear prediction can also be large: $\delta''(0)=-\mu aa^Ty$.

The proof covers zero signal, zero noise, $\gamma=1$, and nontrivial null spaces of $X$, because every inverse used has the fixed gap $c$. At zero eigenvalue the integrand in (25) is $E$; for $\gamma>1$ its atom contributes the unlearned signal $E(1-\gamma^{-1})$. If $E=s^2=0$, both the network and the risk vanish. Time is for the half-sum loss; averaged-loss time $u$ corresponds to $t=u/n$.

Only the rank-one estimate is new to this derivation; the two nonlinear kernel inputs and the MP one-minimum argument have been identified explicitly. There is no claim of novelty over general kernel-regression theory. The result does not cover proportional width, training both layers, nonzero output initialization, anisotropic inputs, nonlinear teachers, a positive double-descent construction, or a peak time. The all-time risk limit does not rule out additional small extrema at dimension-dependent times, and no convergence of the full network risk derivatives is asserted.
