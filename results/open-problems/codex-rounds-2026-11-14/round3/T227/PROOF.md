# A catapult interval with a fully connected second hidden layer

## Statement

For every integer `m>=1`, consider the network

\[
 F_\theta(x)=\frac1m\sum_{i=1}^m a_i\tanh z_i(x),\qquad
 z_i(x)=\frac1{\sqrt m}\sum_{j=1}^m B_{ij}\tanh(c_jx).
 \tag{1}
\]

Both hidden layers use tanh. The second hidden layer is fully connected to
the first. All `m^2+2m` real coordinates `a_i,B_ij,c_j` are trained, without
biases or tying, by simultaneous Euclidean gradient descent

\[
 \theta_{t+1}=\theta_t-\eta\nabla L(\theta_t),\qquad
 L(\theta)=\tfrac12F_\theta(1)^2.
 \tag{2}
\]

The input and label law is the point mass at `(1,0)`. Independently initialize

\[
 \begin{split}
 a_i&\sim\operatorname{Unif}[7.99,8.01],\\
 B_{ij}&\sim\operatorname{Unif}[.499/\sqrt m,.501/\sqrt m],\\
 c_j&\sim\operatorname{Unif}[1.999,2.001].
 \end{split}
 \tag{3}
\]

The factors in (1) are fixed parts of the network. In particular, it is `B`,
not `sqrt(m)*B`, that is trained in the Euclidean metric. This is a
noncentered initialization with mean output normalization.

Write `F_t=F_{theta_t}(1)` and let
`lambda_t=||grad_theta F_{theta_t}(1)||_2^2`, the scalar empirical NTK.
For every point in the initialization box, simultaneously for every
constant learning rate

\[
 .9m\leq\eta\leq1.1m,
 \tag{4}
\]

the following hold:

1. `37/m < lambda_0 < 39/m`, hence `eta*lambda_0>33.3>2`.
2. `L_0<6.5` and `L_1>19`.
3. For every `t>=1`,
   \[
   \frac{1-10^{-8}}m<\lambda_t<\frac{1+10^{-8}}m,
   \qquad |F_{t+1}|\leq\tfrac18|F_t|.
   \tag{5}
   \]
4. Every parameter converges to a finite limit, and
   `L_t<=64^{-(t-1)}L_1 -> 0` for `t>=1`.

Thus these conclusions also hold throughout the interval

\[
 \boxed{36/\lambda_0\leq\eta\leq40/\lambda_0}.
 \tag{6}
\]

The conclusions have probability one under (3), at every finite width.
This proves an interval of loss growth followed by convergence and an NTK
drop for the dense architecture (1). It does not identify a maximal
learning rate or establish a divergence regime. The NTK is not the loss
Hessian.

## 1. Gradients in the full parameter space

Use `W_ij=sqrt(m)*B_ij` only as auxiliary coordinates for estimates. At the
training input, set

\[
 u_j=\tanh c_j,\quad r_j=1-u_j^2,\quad
 z_i=\frac1m\sum_jW_{ij}u_j,\quad
 v_i=\tanh z_i,\quad q_i=1-v_i^2.
\]

Define

\[
 A_i=v_i,\qquad D_{ij}=a_iq_iu_j,\qquad
 C_j=\frac{r_j}m\sum_i a_iq_iW_{ij}.
 \tag{7}
\]

Differentiating (1) in the actual trainable coordinates gives

\[
 \frac{\partial F}{\partial a_i}=\frac{A_i}m,\qquad
 \frac{\partial F}{\partial B_{ij}}=\frac{D_{ij}}{m\sqrt m},\qquad
 \frac{\partial F}{\partial c_j}=\frac{C_j}m.
 \tag{8}
\]

For the last identity, the derivative passes through every second-layer
neuron:

\[
 \frac{\partial F}{\partial c_j}
 =\frac{r_j}{m\sqrt m}\sum_i a_iq_iB_{ij}
 =\frac{r_j}{m^2}\sum_i a_iq_iW_{ij}.
\]

Let `h=eta/m`. Equations (2) and (8) give the exact update

\[
 a_i^+=a_i-hFA_i,\qquad
 W_{ij}^+=W_{ij}-hFD_{ij},\qquad
 c_j^+=c_j-hFC_j.
 \tag{9}
\]

Although the update for `W` looks like that for `a`, ordinary Euclidean
GD in the coordinates `(a,W,c)` would be different. Equation (9) follows
from Euclidean GD in `(a,B,c)`.

For two parameter vectors `theta,theta'`, (8) implies

\[
\begin{split}
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 &=\frac1m\sum_i A_i'A_i
   +\frac1{m^2}\sum_{i,j}D_{ij}'D_{ij}
   +\frac1m\sum_j C_j'C_j.
\end{split}
 \tag{10}
\]

In particular, taking equal vectors gives `m*lambda`. The second term
has `m^2` entries and coefficient `m^{-2}`, not `m^{-1}`.

## 2. Elementary numerical bounds

The following inequalities have rational certificates:

\[
 .963<\tanh c<.966\quad(1.999\leq c\leq2.001),
 \tag{11}
\]

\[
 .446<\tanh z<.450
 \quad(.499\cdot.963\leq z\leq.501\cdot.966),
 \tag{12}
\]

\[
 \tanh1>3/4,\qquad 4e^{-27}<10^{-10}.
 \tag{13}
\]

For completeness, let
`S_N(x)=sum_{k=0}^N x^k/k!`. For rational `0<x<N+2`, the ratios
between successive omitted terms are at most `x/(N+2)`, so

\[
 S_N(x)<e^x\leq S_N(x)
 +\frac{x^{N+1}}{(N+1)!}\frac1{1-x/(N+2)}=:U_N(x).
 \tag{14}
\]

Exact rational arithmetic at `N=64` gives

\[
 \begin{array}{ll}
 S_{64}(3.998)>54,&U_{64}(4.002)<55,\\
 S_{64}(2\cdot.499\cdot.963)>2.611,&
 U_{64}(2\cdot.501\cdot.966)<2.634.
 \end{array}
\]

Since `(s-1)/(s+1)` is increasing for `s>0`, applying it to these
exponential bounds proves (11) and (12):
`53/55>.963`, `54/56<.966`, `1.611/3.611>.446`, and
`1.634/3.634<.450`. The degree-four exponential sum at 2 is 7,
with a positive tail, which proves `tanh1>3/4`. The degree-eight
sum at 3 exceeds 20. Hence `e^{27}>20^9=512000000000` and
`4e^{-27}<10^{-10}`. All these rational assertions are checked in
`verify_dense.py`. The independent recheck uses argument reduction and
repeated squaring instead of the degree-64 calculation.

## 3. Entry into saturation and the loss spike

Put

\[
\begin{array}{llll}
 a_-=7.99,&a_+=8.01,&b_-=.499,&b_+=.501,\\
 u_-=.963,&u_+=.966,&v_-=.446,&v_+=.450,
\end{array}
\]

and define

\[
\begin{split}
 f_-&=a_-v_-,&f_+&=a_+v_+,\\
 J_-&=a_-(1-v_+^2)u_-,&
 J_+&=a_+(1-v_-^2)u_+,\\
 H_+&=a_+(1-v_-^2)b_+(1-u_-^2).
\end{split}
 \tag{15}
\]

Initially `b_-<=W_ij<=b_+`. Thus (11) gives
`b_-u_-<z_i<b_+u_+`, and (12) applies to every row. It follows that

\[
 f_-<F_0<f_+,\quad v_-<A_i<v_+,\quad
 J_-<D_{ij}<J_+,\quad 0<C_j<H_+.
 \tag{16}
\]

The bound on `C_j` follows from its column average in (7). It does not
assume identical rows, columns, or neurons.

For `h in [.9,1.1]`, equations (9) and (16) give, at every index,

\[
\begin{split}
 a_{i,1}&>a_--1.1f_+v_+=6.2057725>6.2,\\
 a_{i,1}&<a_+-.9f_-v_-=6.579595044<6.6,\\
 W_{ij,1}&>b_--1.1f_+J_+>-25,\\
 W_{ij,1}&<b_+-.9f_-J_-<-19,\\
 c_{j,1}&>1.999-1.1f_+H_+>1.07.
\end{split}
 \tag{17}
\]

The displayed inequalities involving 25, 19, and 1.07 are exact rational
inequalities, not assumptions about a symmetric trajectory.

Also, substituting (16) into (10) with equal vectors gives

\[
 m\lambda_0>J_-^2>37,\qquad
 m\lambda_0<v_+^2+J_+^2+H_+^2<39.
 \tag{18}
\]

Thus the initial NTK bounds are unchanged despite the `m^2` trainable
middle-layer connections.

## 4. Uniform cross-gradient estimate in the saturated region

Consider the following convex set in the actual parameter space:

\[
 \mathcal D_m=\{
 |a_i|\leq16,\quad -26\leq\sqrt m B_{ij}\leq-18,
 \quad c_j\geq1\text{ for all }i,j\}.
 \tag{19}
\]

Let `epsilon=10^{-10}`. For every point in this set,
`3/4<u_j<1` and `W_ij<=-18`. Consequently

\[
 z_i=\frac1m\sum_jW_{ij}u_j<-13.5,
 \quad 0<q_i=\operatorname{sech}^2z_i
 \leq4e^{-2|z_i|}<4e^{-27}<\epsilon.
 \tag{20}
\]

Every `v_i` is negative and satisfies
`sqrt(1-epsilon)<|v_i|<1`. From (7), the bounded entries of `W` give

\[
 |A_i|\leq1,\qquad |D_{ij}|\leq16\epsilon,\qquad
 |C_j|\leq\frac1m\sum_i16\epsilon\,26=416\epsilon.
 \tag{21}
\]

The last bound controls the shared first-layer derivatives. Bounding
each `W_ij` below as well as above avoids an uncontrolled column sum.

For any two vectors `theta,theta'` in `D_m`, each `A_i'A_i` lies
strictly between `1-epsilon` and 1. Regardless of the signs of the
output weights, the absolute value of the remaining terms of (10) is
at most

\[
 E=(16\epsilon)^2+(416\epsilon)^2
   =173312\cdot10^{-20}.
 \tag{22}
\]

In particular `epsilon+E<10^{-8}`. Therefore

\[
 1-10^{-8}<m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 <1+10^{-8}\qquad(\theta,\theta'\in\mathcal D_m).
 \tag{23}
\]

Equation (17) places `theta_1` strictly in `D_m`. Applying (20) there
and using `6.2<a_{i,1}<6.6`, all summands in `F_1` are negative, and

\[
 6.2\sqrt{1-\epsilon}<|F_1|<6.6.
\]

On the other hand `|F_0|<f_+`. Thus

\[
 L_0<\tfrac12f_+^2=6.496210125<6.5,
 \quad L_1>\tfrac12(6.2)^2(1-\epsilon)>19.
 \tag{24}
\]

This proves the first-step loss rise.

## 5. Invariance and convergence

Let `rho=1/8` and

\[
 S=\frac{1.1\cdot6.6}{1-\rho}=
 \frac{1452}{175}=8.297142857\ldots.
 \tag{25}
\]

Suppose inductively that, through time `t>=1`, all iterates belong to
`D_m`, and `|F_s|<=6.6 rho^{s-1}` for `1<=s<=t`. This holds at `t=1`.
Using the exact updates (9) and derivative bounds (21), the total
coordinate changes from time 1 through the update at time `t` are at
most

\[
 S\quad\hbox{in each }a_i,\qquad
 16\epsilon S\quad\hbox{in each }W_{ij},\qquad
 416\epsilon S\quad\hbox{in each }c_j.
 \tag{26}
\]

Combining these with the strict entrance bounds (17) gives

\[
\begin{split}
 |a_{i,t+1}|&<6.6+S<16,\\
 W_{ij,t+1}&>-25-16\epsilon S>-26,\\
 W_{ij,t+1}&<-19+16\epsilon S<-18,\\
 c_{j,t+1}&>1.07-416\epsilon S>1.
\end{split}
 \tag{27}
\]

Hence the next endpoint is in `D_m`. By convexity, the simultaneous
update segment is in `D_m` as well. This is established before applying
the cross-gradient estimate to that segment.

In the original Euclidean coordinates set
`theta(s)=theta_t-s eta F_t grad F(theta_t)` for `0<=s<=1`.
The fundamental theorem of calculus yields exactly

\[
\begin{split}
 F_{t+1}-F_t
 &=-\eta F_t\int_0^1
 \langle\nabla F(\theta(s)),\nabla F(\theta_t)\rangle\,ds\\
 &=-hF_t K_t,\\
 K_t&=m\int_0^1
 \langle\nabla F(\theta(s)),\nabla F(\theta_t)\rangle\,ds.
\end{split}
 \tag{28}
\]

By (23), `1-10^{-8}<K_t<1+10^{-8}`. Since `.9<=h<=1.1`,

\[
 |1-hK_t|\leq
 \max\{1-.9(1-10^{-8}),\,1.1(1+10^{-8})-1\}
 =.100000011<\rho.
 \tag{29}
\]

Equations (28) and (29) prove `|F_{t+1}|<=rho|F_t|`, completing
the induction. A zero residual freezes all coordinates by (9), so it
introduces no exceptional case.

Taking `theta'=theta_t` in (23) proves (5)'s kernel estimate. Equations
(9), (21), and the geometric residual bound show that every coordinate
has absolutely summable updates. There are finitely many coordinates
at each width, so all parameters have finite limits. The residual tends
to zero, giving the claimed limiting loss and the geometric loss bound.
In particular `eta*lambda_t<1.1(1+10^{-8})<2` for all `t>=1`.

Finally write `k_0=m*lambda_0`. Equation (18) gives `37<k_0<39`.
If `36<=eta*lambda_0<=40`, then

\[
 .9<\frac{36}{39}\leq h=
 \frac{\eta\lambda_0}{k_0}\leq\frac{40}{37}<1.1.
\]

This proves the inclusion of (6) in (4). All estimates hold throughout
the full product box, proving the probability-one statement.

## Scope

This extends the sparse parallel-path certificate to a fully connected
middle layer with independently initialized, separately trained weights.
The proof uses neither equality of neurons nor an invariant subspace of
tied weights. The initialization remains positive and narrowly
concentrated, and the data law has one zero-label example. The proof does
not extend to centered Gaussian initialization, general data, or a full
three-regime phase diagram. No maximal learning rate follows from the
upper endpoint of the certified interval.
