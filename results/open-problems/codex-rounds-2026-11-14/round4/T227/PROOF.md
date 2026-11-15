# A catapult interval with independent signs in a dense hidden layer

## Statement

Fix an integer width m. Consider the two-hidden-layer network

\[
 F_\theta(x)=\frac1m\sum_{i=1}^m a_i\tanh z_i(x),\qquad
 z_i(x)=\frac1{\sqrt m}\sum_{j=1}^m B_{ij}\tanh(c_jx).
 \tag{1}
\]

There are no biases. All m²+2m coordinates (a,B,c) are separately trained
by simultaneous Euclidean gradient descent with constant step eta on

\[
 L(\theta)=\tfrac12 F_\theta(1)^2.
 \tag{2}
\]

Thus the input and label law is the point mass at (1,0). The factors in
(1) are fixed parts of the architecture; B, rather than sqrt(m)B, is
the Euclidean trainable middle-layer coordinate.

Independently initialize all coordinates by

\[
\begin{split}
 a_i&\sim\operatorname{Unif}[7.99,8.01],\qquad
 c_j\sim\operatorname{Unif}[1.999,2.001],\\
 B_{ij}&=\frac{S_{ij}U_{ij}}{\sqrt m},\qquad
 U_{ij}\sim\operatorname{Unif}[.999,1.001],\\
 \Pr(S_{ij}=1)&=\tfrac34,\qquad \Pr(S_{ij}=-1)=\tfrac14.
\end{split}
\tag{3}
\]

All S, U, a, c are mutually independent. In particular, there is no shared
sign variable and no tying. This law is noncentered: E[sqrt(m)B_ij]=1/2.

Let F_t=F_{theta_t}(1) and let lambda_t=||grad_theta F_t||² denote the
scalar empirical NTK. For every m>=20000, with probability at least

\[
 1-4m\exp(-m/800),
 \tag{4}
\]

simultaneously for every fixed eta in [.9m,1.1m], the following hold:

\[
 \frac{34}m<\lambda_0<\frac{43}m,\qquad
 L_0<8<16<L_1,
 \tag{5}
\]

and for every t>=1,

\[
 \frac{1-10^{-6}}m<\lambda_t<\frac{1+10^{-6}}m,
 \qquad |F_{t+1}|\leq\tfrac18|F_t|.
 \tag{6}
\]

Every parameter converges to a finite limit, and
L_t<=64^{-(t-1)}L_1 tends to zero. For m>=20000 the success probability
in (4) is greater than 1-2×10^{-6}. The initial effective step obeys
eta lambda_0>30.6>2, while eta lambda_t<1.1000011<2 for t>=1.
The interval is a sufficient convergence interval; its upper endpoint
is not asserted to be maximal.

The new assertion relative to the positive dense initialization is the
high-probability entrance certificate for the independent mixed-sign law
(3). The data and outer-layer laws remain restricted as stated.

## 1. A simultaneous row and column event

Define the event

\[
 \mathcal E_m=\left\{
 .45\leq\frac1m\sum_jS_{ij}\leq.55\ (\text{every }i),\quad
 .45\leq\frac1m\sum_iS_{ij}\leq.55\ (\text{every }j)
 \right\}.
 \tag{7}
\]

Here is a direct concentration proof. For one sign S, put
phi(t)=log E exp(t(S-1/2)). Then phi(0)=phi'(0)=0, and phi''(t)
is the variance of S under the exponentially tilted law. Since S takes
values -1 and 1, that variance is at most 1. Integrating twice gives
phi(t)<=t²/2 for every real t. For each row of independent signs,
Markov's inequality, with t=.05, gives

\[
 \Pr\left(\frac1m\sum_j(S_{ij}-1/2)\geq.05\right)
 \leq\exp(-.05tm+mt^2/2)=\exp(-m/800).
 \tag{8}
\]

Applying the same argument to -S gives the lower-tail bound. The
columns have the same bound. A union bound over the 2m rows and columns
and their two tails yields

\[
 \Pr(\mathcal E_m^c)\leq4m\exp(-m/800).
 \tag{9}
\]

Row and column events need not be independent. For m>800, the derivative
of m exp(-m/800) is exp(-m/800)(1-m/800)<0. Also e^{25}>4×10^{10},
so at m=20000 the right side of (9) is less than 2×10^{-6}.

Write W_ij=sqrt(m)B_ij as auxiliary coordinates. Deterministically,
|W_ij-S_ij|<=.001 and |W_ij|<=1.001. On E_m, every row average
and every column average of W belongs to [.449,.551]. Every row and
column average of |W| is at most 1.001. These properties hold for every
choice of the amplitudes U in their support.

## 2. Gradients and the Euclidean metric

At x=1 set

\[
 u_j=\tanh c_j,\quad r_j=1-u_j^2,\quad
 z_i=\frac1m\sum_jW_{ij}u_j,\quad v_i=\tanh z_i,\quad q_i=1-v_i^2,
\]

and define

\[
 A_i=v_i,\quad D_{ij}=a_iq_iu_j,\quad
 C_j=\frac{r_j}{m}\sum_i a_iq_iW_{ij}.
 \tag{10}
\]

The derivatives in the actual trainable coordinates are

\[
 \partial_{a_i}F=A_i/m,\qquad
 \partial_{B_{ij}}F=D_{ij}/(m\sqrt m),\qquad
 \partial_{c_j}F=C_j/m.
 \tag{11}
\]

For example,
partial_{c_j}F=r_j sum_i a_iq_iB_ij/(m sqrt(m))=C_j/m.
With h=eta/m, the exact simultaneous update is therefore

\[
 a_i^+=a_i-hFA_i,\qquad W_{ij}^+=W_{ij}-hFD_{ij},\qquad
 c_j^+=c_j-hFC_j.
 \tag{12}
\]

For two parameter vectors theta,theta', direct summation of (11) gives

\[
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 =\frac1m\sum_i A_i'A_i+rac1{m^2}\sum_{ij}D_{ij}'D_{ij}
   +\frac1m\sum_j C_j'C_j.
 \tag{13}
\]

In particular the middle term averages over m² entries. Equation (12)
describes Euclidean training in (a,B,c), not in (a,W,c).

## 3. Numerical inequalities with rational certificates

All terminating decimals below are exact rational numbers. Put

\[
\begin{array}{lll}
 a_-=7.99,&a_+=8.01,\\
 u_-=.96395,&u_+=.96410,&\bar u=.964025,\quad d_u=.000075,\\
 v_-=.407,&v_+=.487,\\
 w_-=.449,&w_+=.551,&M_W=1.001.
\end{array}
\tag{14}
\]

The following strict inequalities hold:

\[
 u_-<\tanh c<u_+\quad(1.999\leq c\leq2.001),
 \tag{15}
\]

\[
 v_-<\tanh z<v_+\quad
 (\bar u w_--d_uM_W\leq z\leq\bar u w_++d_uM_W),
 \tag{16}
\]

\[
 \tanh(.8)>.66,\qquad 4e^{-19.8}<2\cdot10^{-8},\qquad
 e^{25}>4\cdot10^{10}.
 \tag{17}
\]

For an explicit certificate, define
S_N(x)=sum_{k=0}^N x^k/k! for x>=0. When x<N+2, the ratios of
successive omitted terms are at most x/(N+2). Hence

\[
 S_N(x)\leq e^x\leq
 S_N(x)+\frac{x^{N+1}}{(N+1)!}\frac1{1-x/(N+2)}=:U_N(x).
 \tag{18}
\]

For x>0 the left inequality is strict. The map g(s)=(s-1)/(s+1)
is increasing on s>0, so g(S_80(2z)) and g(U_80(2z)) give rational
lower and upper bounds on tanh(z) for the positive arguments used here.
Substituting the two endpoints in (15), the two endpoints
0.43277215 and 0.53125285 in (16), and .8 in (17), proves (15)--(17).
The remaining exponential inequalities follow by substituting 19.8
and 25 into S_80. The exact comparisons in (18) and every rational
comparison below are implemented in `verify_signs.py`.

## 4. Entrance under mixed signs

Assume E_m. Initially, write each u_j as bar u+e_j, where
|e_j|<d_u by (15). For each row,

\[
 z_i=\bar u\frac1m\sum_j W_{ij}+\frac1m\sum_j W_{ij}e_j.
\]

Section 1 bounds the first average between w_- and w_+ and the error
in absolute value by d_u M_W. Thus (16) applies to every v_i.
In particular all u_j,v_i and a_i are initially positive. Define

\[
\begin{split}
 f_-&=a_-v_-,& f_+&=a_+v_+,\\
 k_-&=a_-(1-v_+^2),& k_+&=a_+(1-v_-^2),\\
 \bar k&=(k_-+k_+)/2,&d_k&=(k_+-k_-)/2,\\
 D_-&=k_-u_-,&D_+&=k_+u_+,\\
 H&=(1-u_-^2)(\bar k w_++d_k M_W).
\end{split}
\tag{19}
\]

Then f_-<F_0<f_+ and D_-<D_ij<D_+. To bound the shared first-layer
derivative, set k_i=a_iq_i. Each k_i belongs to (k_-,k_+), so for
each column

\[
 \left|\frac1m\sum_i k_i W_{ij}\right|
 \leq\bar k\left|\frac1m\sum_i W_{ij}\right|
       +\frac1m\sum_i|k_i-\bar k|\,|W_{ij}|
 \leq\bar k w_++d_k M_W.
 \tag{20}
\]

Multiplication by 0<r_j<1-u_-² gives |C_j|<H. This estimate permits
arbitrary dependence of the realized k_i on the signs in W. It uses a
signed column average only for the constant part bar k, and controls
the variation separately.

For h in [.9,1.1], the exact update (12) now gives

\[
\begin{split}
 a_{i,1}&>a_--1.1f_+v_+=5.900303941>5.8,\\
 a_{i,1}&<a_+-.9f_-v_-=6.818818041<6.9,\\
 W_{ij,1}&\geq-M_W-1.1f_+D_+>-29,\\
 W_{ij,1}&\leq M_W-.9f_-D_-<-16,\\
 c_{j,1}&>1.999-1.1f_+H>.84.
\end{split}
\tag{21}
\]

For clarity, the last three unrounded rational values are respectively
-28.648607298330236987, -16.1944410093411523435, and a number
greater than .84007454789. All inequalities are uniform in all signs
and amplitudes satisfying E_m, and in the whole step interval.

Taking theta'=theta in (13) at initialization also gives

\[
 m\lambda_0>D_-^2>34,
 \qquad m\lambda_0<v_+^2+D_+^2+H^2<43.
 \tag{22}
\]

The rational endpoints before the final simplification are greater than
34.51908 and less than 41.82529, respectively. Also

\[
 L_0<\tfrac12f_+^2=7.60839337845<8.
 \tag{23}
\]

## 5. A convex saturated region

Set epsilon=2×10^{-8} and delta=10^{-6}. Consider the convex set
in the actual Euclidean parameter space

\[
 \mathcal D_m=\{\ |a_i|\leq18,\quad
 -30\leq\sqrt m B_{ij}\leq-15,\quad c_j\geq.8\ \}.
 \tag{24}
\]

Here and below the constraints hold for all indices. For theta in D_m,
(17) gives u_j>.66. Since every W_ij<=-15,

\[
 z_i< -9.9,\qquad
 0<q_i=\operatorname{sech}^2z_i\leq4e^{-2|z_i|}
 <4e^{-19.8}<\epsilon.
 \tag{25}
\]

Thus -1<v_i<-sqrt(1-epsilon), and from (10),

\[
 |A_i|\leq1,\qquad |D_{ij}|\leq18\epsilon,\qquad
 |C_j|\leq540\epsilon.
 \tag{26}
\]

For the last bound, r_j<=1 and each of the m summands has absolute
value at most 18 epsilon·30. No condition on the sign of a_i is needed.

For theta,theta' in D_m, the product A_i'A_i belongs to (1-epsilon,1).
By (13), the absolute total contribution of the other two terms is
at most (18 epsilon)²+(540 epsilon)². Since

\[
 \epsilon+(18\epsilon)^2+(540\epsilon)^2
 =2.01167696\cdot10^{-8}<\delta,
\]

we obtain the uniform full-space estimate

\[
 1-\delta<m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 <1+\delta\qquad(\theta,\theta'\in\mathcal D_m).
 \tag{27}
\]

By (21), theta_1 belongs to D_m and all a_i,1 are positive. Therefore
all summands in F_1 are negative, and (25) gives

\[
 5.8\sqrt{1-\epsilon}<|F_1|<6.9.
\]

Consequently

\[
 L_1>\tfrac12(5.8)^2(1-\epsilon)=16.8199996636>16.
 \tag{28}
\]

Together with (23), this proves the loss spike.

## 6. Invariance, contraction and parameter limits

Let rho=1/8 and

\[
 S_* =\frac{1.1\cdot6.9}{1-\rho}=\frac{1518}{175}.
 \tag{29}
\]

Suppose inductively that theta_s belongs to D_m and
|F_s|<=6.9 rho^{s-1} for 1<=s<=t. The base case follows from
(21) and (28). Using (12) and (26), the total change from time 1
through the update at time t is bounded by S_* in every a coordinate,
18 epsilon S_* in every W coordinate, and 540 epsilon S_* in every
c coordinate. Hence the next endpoint satisfies

\[
\begin{split}
 |a_{i,t+1}|&<6.9+S_*=15.5742857142857\ldots<18,\\
 W_{ij,t+1}&>-29-18\epsilon S_*>-30,\\
 W_{ij,t+1}&<-16+18\epsilon S_*<-15,\\
 c_{j,t+1}&>.84-540\epsilon S_*>.8399>.8.
\end{split}
\tag{30}
\]

These inequalities establish membership of theta_{t+1} in D_m before
any use of contraction for that step. Convexity then puts the entire
simultaneous update segment in D_m.

In the original Euclidean coordinates define
theta(s)=theta_t-s eta F_t grad F(theta_t), for 0<=s<=1. The
fundamental theorem of calculus yields

\[
 F_{t+1}-F_t=-hF_t K_t,\qquad
 K_t=m\int_0^1\langle\nabla F(\theta(s)),\nabla F(\theta_t)\rangle\,ds.
 \tag{31}
\]

Equation (27) bounds K_t between 1-delta and 1+delta. Therefore

\[
 |1-hK_t|\leq
 \max\{1-.9(1-\delta),\ 1.1(1+\delta)-1\}
 =.1000011<\rho.
 \tag{32}
\]

This proves |F_{t+1}|<=rho|F_t| and completes the induction. A zero
residual freezes all coordinates and causes no exception. Taking equal
vectors in (27) proves the NTK bounds in (6). The residual contraction
gives the stated loss bound. Equations (12), (26), and the convergent
geometric series imply that the updates of every coordinate are absolutely
summable. For every finite width, every coordinate therefore has a finite
limit. Continuity gives output zero at that limit.

All these conclusions hold on the same event E_m for every eta in
the stated interval, without an eta-dependent exceptional set.
Combining this deterministic conclusion with (9) proves (4)--(6).

## Scope

This establishes a high-probability catapult interval for a dense deep
nonlinear architecture under a product law allowing independent negative
middle-layer weights. It does not identify eta_max, prove divergence,
cover centered initialization, or address a nontrivial data law. The
curvature statements concern the empirical NTK, not the loss Hessian.
