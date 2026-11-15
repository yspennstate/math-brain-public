# A catapult interval for a sparse three-layer tanh network

The result below is a restricted existence theorem. The architecture has two nonlinear hidden layers, independent paths, mean output normalization, and a noncentered product initialization law. It does not give the maximal convergent learning rate or a theorem for a dense network with Gaussian initialization.

## Statement

For an integer width `m >= 1`, let

\[
 F_\theta(x)=\frac1m\sum_{i=1}^m
 a_i\tanh\bigl(b_i\tanh(c_i x)\bigr).
\]

The first hidden layer has weights `c_i`, the second hidden layer has diagonal weights `b_i`, and the output layer has weights `a_i/m`. The trainable coordinates are `(a_i,b_i,c_i)`, with the factor `1/m` fixed in the output definition. All `3m` coordinates are trained by ordinary simultaneous Euclidean gradient descent. There are no biases or off-diagonal second-layer connections.

The input and label law is the point mass at `(x,y)=(1,0)`, and the loss is

\[
 L(\theta)=\tfrac12 F_\theta(1)^2.
\]

Initialize all coordinates independently, with

\[
 a_i\sim\operatorname{Unif}[7.99,8.01],\qquad
 b_i\sim\operatorname{Unif}[0.499,0.501],\qquad
 c_i\sim\operatorname{Unif}[1.999,2.001].
\]

Write `F_t=F_{theta_t}(1)`, and define the scalar empirical NTK by

\[
 \lambda_t=\|\nabla_\theta F_{\theta_t}(1)\|_2^2.
\]

For every initialization in the indicated product box, simultaneously for every fixed step

\[
 0.9m\leq\eta\leq1.1m,
 \tag{1}
\]

the following statements hold:

1. `37/m < lambda_0 < 39/m`, so `eta lambda_0 > 33.3 > 2`.
2. `L_0 < 6.5` and `L_1 > 19`.
3. For every `t >= 1`,
   \[
   \frac{1-10^{-8}}m<\lambda_t<\frac{1+10^{-8}}m,
   \qquad \eta\lambda_t<1.100000011<2.
   \tag{2}
   \]
4. For every `t >= 1`,
   \[
   |F_{t+1}|\leq\tfrac18|F_t|,
   \qquad L_t\leq64^{-(t-1)}L_1.
   \tag{3}
   \]
   Every parameter has a finite limit, and the limiting loss is zero.

In particular, the interval

\[
 \boxed{\quad 36/\lambda_0\leq\eta\leq40/\lambda_0\quad}
 \tag{4}
\]

also has these properties, since it is contained in (1). All conclusions therefore hold with probability one under the stated law, at every finite width. The curvature in (2) refers to the NTK, not the loss Hessian.

## 1. Path derivatives and the width normalization

For a path parameter `p=(a,b,c)`, put

\[
 u=\tanh c,\qquad v=\tanh(bu),\qquad
 f(p)=av,\qquad q=1-v^2.
\]

The chain rule gives the path gradient

\[
 j(p)=\nabla f(p)
 =\bigl(v,\;a q u,\;a q b(1-u^2)\bigr).
 \tag{5}
\]

Since `F=m^{-1} sum_i f(p_i)`, its gradient in block `p_i` is `j(p_i)/m`. Consequently,

\[
 \lambda=\frac1{m^2}\sum_i\|j(p_i)\|^2,
 \qquad
 p_i^+=p_i-hFj(p_i),\quad h=\eta/m.
 \tag{6}
\]

Thus `h in [0.9,1.1]` is the effective path step. The shared residual `F` appears in every block; the paths are not optimized separately.

## 2. Elementary bounds used below

At initialization,

\[
 .963<u<.966,\qquad .446<v<.450.
 \tag{7}
\]

Here is an exact rational certificate for these transcendental inequalities. For rational `z >= 0`, define

\[
 S_N(z)=\sum_{k=0}^N\frac{z^k}{k!},\qquad
 U_N(z)=S_N(z)+\frac{z^{N+1}}{(N+1)!}
                     \frac1{1-z/(N+2)}.
\]

When `z < N+2`, positivity of the exponential series and the ratio bound on its tail give `S_N(z) < exp(z) <= U_N(z)` for `z>0`. With `N=64`, rational arithmetic gives

\[
\begin{aligned}
 S_{64}(3.998)&>54,& U_{64}(4.002)&<55,\\
 S_{64}(2\cdot.499\cdot.963)&>2.611,&
 U_{64}(2\cdot.501\cdot.966)&<2.634.
\end{aligned}
\]

Using `tanh z=(exp(2z)-1)/(exp(2z)+1)`, the first pair implies the bound on `u`: `53/55 > .963` and `54/56 < .966`. Monotonicity gives `.499*.963 < bu < .501*.966`. The second pair implies the bound on `v`, because `1.611/3.611 > .446` and `1.634/3.634 < .450`.

Also `tanh 1 > 3/4`, since `exp(2)>7`; the exponential series through degree four equals 7 and has a positive tail. Finally,

\[
 e^{27}>10^{11},\qquad 4e^{-27}<10^{-10},\qquad
 72e^{-27}<10^{-8}.
 \tag{8}
\]

For example, the exponential series through degree eight gives `exp(3)>20`, and hence `exp(27)>20^9=512000000000>10^11`. The last two inequalities follow directly. The rational assertions in this section and below are reproduced in `verify.py`, using fractions rather than rounded transcendental evaluations.

## 3. The first update

Set

\[
\begin{aligned}
 A_-&=7.99,&A_+&=8.01,& B_-&=.499,&B_+&=.501,\\
 U_-&=.963,&U_+&=.966,& V_-&=.446,&V_+&=.450,\\
 f_-&=A_-V_-,&f_+&=A_+V_+,\\
 J_-&=A_-(1-V_+^2)U_-,&
 J_+&=A_+(1-V_-^2)U_+,\\
 H_+&=A_+(1-V_-^2)B_+(1-U_-^2).
\end{aligned}
\]

Every initial path output lies between `f_-` and `f_+`, so `f_- < F_0 < f_+`. Every initial `b` derivative lies between `J_-` and `J_+`, and every initial `c` derivative is positive and at most `H_+`. Equations (5) and (6) therefore yield, for each path,

\[
\begin{aligned}
 a_{i,1}&\geq A_--1.1 f_+V_+=6.2057725>6.2,\\
 a_{i,1}&\leq A_+-.9 f_-V_-=6.579595044<6.6,\\
 b_{i,1}&\leq B_+-.9 f_-J_-<-19,\\
 c_{i,1}&\geq1.999-1.1 f_+H_+>1.07.
\end{aligned}
\tag{9}
\]

The latter two rational bounds are, rounded outward, `b_{i,1}<-19.17912` and `c_{i,1}>1.07321`. Bounds on the common `F_0` suffice; equal path parameters are not assumed.

The initial kernel satisfies

\[
 m\lambda_0>J_-^2>37,
 \qquad
 m\lambda_0<V_+^2+J_+^2+H_+^2<39.
 \tag{10}
\]

The lower bound uses just the `b` derivative in (5), and the upper bound uses all three coordinate bounds. Since `h >= .9`, this proves the first assertion of the theorem.

## 4. A saturated region

Consider the convex region of path parameters

\[
 D=\{(a,b,c): |a|\leq16,\ b\leq-18,\ c\geq1\}.
\]

For `p in D`, `u>3/4`, `bu<0`, and

\[
 0<q=\operatorname{sech}^2(bu)
 \leq4e^{-2|b|u}\leq4e^{-3|b|/2}<10^{-10}.
 \tag{11}
\]

The function `s exp(-3s/2)` is decreasing for `s>=18`, since its derivative is `exp(-3s/2)(1-3s/2)<0`. Thus

\[
 |b|q\leq4|b|e^{-3|b|/2}\leq72e^{-27}<10^{-8}.
 \tag{12}
\]

It follows from (5) that throughout `D`,

\[
 |j_a|\leq1,\quad |j_b|\leq16\cdot10^{-10},\quad
 |j_c|\leq16\cdot10^{-8},\quad
 -1<v<-\sqrt{1-10^{-10}}.
 \tag{13}
\]

For any two points `p,p' in D`, the first coordinates of their gradients have the same negative sign. Their product is at least `1-10^{-10}`. The absolute contribution of the other two coordinates to their gradient inner product is bounded by

\[
 256(10^{-20}+10^{-16}).
\]

In particular, the slightly looser uniform bound

\[
 1-10^{-8}<j(p')\cdot j(p)<1+10^{-8}
 \tag{14}
\]

holds, since `2*10^{-10}+256*(10^{-20}+10^{-16})<10^{-8}`. This bound allows signs and magnitudes of different output weights `a` to differ.

By (9), all paths at time 1 lie strictly inside `D`. By (11), their path outputs are negative, with absolute values between `6.2 sqrt(1-10^{-10})` and `6.6`. Therefore

\[
 L_0<\tfrac12 f_+^2=6.496210125<6.5,
 \quad
 19<\tfrac12(6.2)^2(1-10^{-10})<L_1,
 \quad |F_1|<6.6.
 \tag{15}
\]

This proves the loss spike without any simulation.

## 5. Invariance and residual contraction

Let `rho=1/8` and

\[
 S=\frac{1.1\cdot6.6}{1-\rho}=8.297142857\ldots.
\]

Inductively suppose the paths through time `t>=1` lie in `D` and

\[
 |F_s|\leq6.6\rho^{s-1}\qquad(1\leq s\leq t).
 \tag{16}
\]

This holds for `t=1`. The cumulative coordinate changes from time 1 through the update at time `t`, using (6), (13), and the geometric series, are at most

\[
 S,\qquad S\cdot16\cdot10^{-10},\qquad
 S\cdot16\cdot10^{-8}
 \tag{17}
\]

in `a,b,c`, respectively. Using the stricter initial margins in (9), these imply

\[
\begin{aligned}
 |a_{i,t+1}|&<6.6+S<16,\\
 b_{i,t+1}&<-19+S\cdot16\cdot10^{-10}<-18,\\
 c_{i,t+1}&>1.07-S\cdot16\cdot10^{-8}>1.
\end{aligned}
\tag{18}
\]

Thus the new endpoints lie in `D`. Since `D` is convex, the entire simultaneous update segment also lies in `D`. This establishes the domain of the following integral before using it.

Write `p_i(s)=p_{i,t}-s hF_t j(p_{i,t})` for `0<=s<=1`. The fundamental theorem of calculus, applied to the actual network output, gives

\[
\begin{aligned}
 F_{t+1}-F_t
 &=\frac1m\sum_i\int_0^1 j(p_i(s))\cdot
                  (-hF_t j(p_{i,t}))\,ds\\
 &=-hF_t C_t,\\
 C_t&=\frac1m\sum_i\int_0^1j(p_i(s))\cdot j(p_{i,t})\,ds.
\end{aligned}
\tag{19}
\]

By (14), `1-10^{-8}<C_t<1+10^{-8}`. Hence

\[
 |1-hC_t|\leq
 \max\{1-.9(1-10^{-8}),\;1.1(1+10^{-8})-1\}
 =.100000011<\tfrac18.
 \tag{20}
\]

Equations (19) and (20) prove `|F_{t+1}|<=rho|F_t|`, and therefore (16) for `t+1`. This completes the induction, proving invariance and (3) for all time. If a residual is exactly zero, (6) makes every subsequent update zero, and all the same conclusions hold.

## 6. Kernel drop, limiting parameters, and the stated interval

Apply (14) with `p'=p` and sum using (6). This proves the bounds on `lambda_t` in (2) for every `t>=1`. Comparing them with (10) proves the kernel drop. Also, `eta lambda_t=m h lambda_t<1.1(1+10^{-8})<2`.

Each coordinate update has an absolutely summable magnitude by (13), (16), and (6). Every parameter is therefore a Cauchy sequence in the real numbers and has a finite limit. Continuity of the network output and (3) show that the limit has output zero and loss zero.

Finally put `k_0=m lambda_0`. By (10), `37<k_0<39`. If `eta lambda_0 in [36,40]`, then

\[
 .9<36/39\leq h=\frac{\eta\lambda_0}{k_0}
 \leq40/37<1.1.
\]

Thus (4) is contained in (1), as claimed. All estimates hold on the complete initialization box, which has probability one under the specified independent uniform law. There is no exceptional event to estimate.

The proof gives a catapult interval and a lower bound on the supremum of convergent steps. It gives no divergence criterion above that interval, no proof that convergent steps form a single interval, and no identification of `eta_max`.
