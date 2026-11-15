# Escape from a small residual under unbiased middle-layer signs

## Statement

For an integer width m, consider

\[
 F_\theta(x)=\frac1m\sum_{i=1}^m a_i\tanh z_i(x),\qquad
 z_i(x)=\frac1{\sqrt m}\sum_{j=1}^m B_{ij}\tanh(c_jx).
 \tag{1}
\]

There are no biases or tied parameters. All m²+2m coordinates (a,B,c)
are trained by simultaneous Euclidean gradient descent with constant
step eta on L(theta)=F_theta(1)²/2. The data law is the point mass at
(1,0). Initialize independently

\[
 \begin{split}
 a_i&\sim\operatorname{Unif}[7.99,8.01],\qquad
 c_j\sim\operatorname{Unif}[1.999,2.001],\\
 B_{ij}&=S_{ij}U_{ij}/\sqrt m,\qquad
 U_{ij}\sim\operatorname{Unif}[.999,1.001],\qquad
 \Pr(S_{ij}=1)=\Pr(S_{ij}=-1)=\tfrac12.
 \end{split}
 \tag{2}
\]

All displayed random variables are mutually independent. The middle
layer is centered; the other two layers retain positive initialization.
The factors in (1) are fixed architectural normalizations, and B is
the Euclidean trainable coordinate.

Write W_ij=sqrt(m)B_ij, F_t=F_theta_t(1), and
lambda_t=||grad_theta F_theta_t(1)||². Set r=1/50 and

\[
 N_m=\min\{n\in\mathbb Z_{\geq0}:40^n\geq m^4/50\}.
 \tag{3}
\]

For every m>=200000, there is an event of probability at least

\[
 1-2m e^{-m/5000}-2e^{-m^2/400000}-\frac{143}{m^2}
 >1-4\cdot10^{-9}
 \tag{4}
\]

on which the following statements hold simultaneously for every
constant eta in [.9m,1.1m]. The stopping time

\[
 \tau=\min\{t\geq0:|F_t|\geq r\}
 \tag{5}
\]

exists, and

\[
 \begin{gathered}
 m^{-4}\leq|F_0|<r,\qquad 1\leq\tau\leq N_m,\\
 40|F_t|\leq|F_{t+1}|\leq69|F_t|,\quad
 F_tF_{t+1}<0\qquad(0\leq t<\tau),\\
 .02\leq|F_\tau|<1.38,\qquad
 \frac{50}{m}<\lambda_t<\frac{63}{m}\qquad(0\leq t\leq\tau).
 \end{gathered}
 \tag{6}
\]

In particular L_{t+1}>=1600L_t before exit and eta lambda_0>45>2.
Here N_m=O(log m), and N_200000=13.

Every iterate through time tau belongs to the convex set

\[
 \mathcal T(W_0)=\{
 7.9\leq a_i\leq8.1,\quad1.97\leq c_j\leq2.03,\quad
 |W_{ij}-W_{ij,0}|\leq.2\text{ for all }i,j\}.
 \tag{7}
\]

There is also a common displacement b_t, defined by

\[
 b_t=-7.53\sum_{s=0}^{t-1}(\eta/m)F_s,
 \tag{8}
\]

such that, for 0<=t<=tau,

\[
 \max_{i,j}|W_{ij,t}-W_{ij,0}-b_t|
 <\frac{121}{16250}<.0075.
 \tag{9}
\]

Thus both row and column averages are displaced by the same b_t up
to .0075. No concentration condition on initial columns is imposed.

This is an early escape theorem. It does not assert a subsequent kernel
drop, convergence of the loss, or a maximal stable learning rate.

## 1. Exact gradients and update

At the training input define

\[
 u_j=\tanh c_j,\quad r_j=1-u_j^2,\quad
 z_i=\frac1m\sum_jW_{ij}u_j,\quad
 v_i=\tanh z_i,\quad q_i=1-v_i^2,
\]

and

\[
 A_i=v_i,\qquad D_{ij}=a_iq_iu_j,\qquad
 C_j=\frac{r_j}{m}\sum_i a_iq_iW_{ij}.
 \tag{10}
\]

Differentiating (1) in its actual coordinates gives

\[
 \partial_{a_i}F=A_i/m,\qquad
 \partial_{B_{ij}}F=D_{ij}/(m\sqrt m),\qquad
 \partial_{c_j}F=C_j/m.
 \tag{11}
\]

For example, partial_{c_j}F equals
r_j sum_i a_i q_i B_ij/(m sqrt(m)), which is C_j/m.
Writing h=eta/m, the exact simultaneous update is

\[
 a_i^+=a_i-hFA_i,\qquad
 W_{ij}^+=W_{ij}-hFD_{ij},\qquad
 c_j^+=c_j-hFC_j.
 \tag{12}
\]

For two arbitrary parameter vectors theta,theta', direct summation of
(11) gives

\[
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 =\frac1m\sum_i A_i'A_i
  +\frac1{m^2}\sum_{ij}D_{ij}'D_{ij}
  +\frac1m\sum_j C_j'C_j.
 \tag{13}
\]

All inner products below use this Euclidean metric in (a,B,c).

## 2. Row event and a uniform tube estimate

Let

\[
 E_m=\left\{\left|\frac1m\sum_jS_{ij}\right|\leq.02
               \text{ for every row }i\right\}.
 \tag{14}
\]

On E_m, since |W_ij,0-S_ij|<=.001 and |W_ij,0|<=1.001,

\[
 |\operatorname{mean}_j W_{ij,0}|\leq.021,\qquad
 \operatorname{mean}_j|W_{ij,0}|\leq1.001.
 \tag{15}
\]

The elementary inequalities

\[
 \tanh(1.97)>.96,\qquad \tanh(2.03)<.97
 \tag{16}
\]

hold. Consequently .96<u_j<.97 throughout T(W_0). Write
u_j=.965+e_j with |e_j|<.005. For every point in that tube,

\[
 \begin{split}
 |z_i|
 &\leq .965|\operatorname{mean}_jW_{ij,0}|
       +.005\operatorname{mean}_j|W_{ij,0}|
       +\operatorname{mean}_j|W_{ij}-W_{ij,0}|\,|u_j|\\
 &\leq .965\cdot.021+.005\cdot1.001+.2\cdot.97\\
 &=.21927<.225.
 \end{split}
 \tag{17}
\]

At initialization the same estimate without its final term gives
|z_i,0|<=.02527. The inequality |tanh z|<=|z| follows by integrating
0<tanh'(z)<=1 from zero, so |A_i|<.225 throughout the tube.
Also |W_ij|<=1.201 there. Equation (10) now implies

\[
 \begin{split}
 d_-&:=7.9(1-.225^2)\,.96=7.20006<D_{ij}<8.1\cdot.97=7.857=:d_+,\\
 |C_j|&<(1-.96^2)\,8.1\cdot1.201=.76268304=:c_*.
 \end{split}
 \tag{18}
\]

The C bound uses absolute values in the column sum and makes no column
concentration assumption. The interval for D is positive, even when the
entries of W have both signs.

For any two points in T(W_0), (13) therefore gives

\[
 \begin{split}
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 &>d_-^2-.225^2-c_*^2>51.2085>50,\\
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 &<d_+^2+.225^2+c_*^2<62.3648<63.
 \end{split}
 \tag{19}
\]

In the first and third terms of (13), the factors can have opposite
signs; the negative allowances in (19) include this possibility.

For exact certificates for (16), set
S_n(x)=sum_{k=0}^n x^k/k!, for rational x>=0. If x<n+2, bounding
the ratios of successive omitted terms by x/(n+2) gives

\[
 S_n(x)\leq e^x\leq S_n(x)+
 \frac{x^{n+1}}{(n+1)!}\frac1{1-x/(n+2)}=:U_n(x).
 \tag{20}
\]

The increasing function (s-1)/(s+1) applied to S_100(2x),U_100(2x)
encloses tanh x. Substitution of x=1.97 and 2.03 proves (16) by
rational comparisons. The other decimal constants in (17)--(19) are
exact rational expressions; `verify_bootstrap.py` checks them without
floating-point comparisons.

## 3. Bootstrap until escape

Assume E_m and 0<|F_0|<r. Initially theta_0 belongs to T(W_0).
Suppose theta_0,...,theta_t belong to the tube, |F_s|<r for s<=t,
and every previous step has amplified |F_s| by at least 40. Then

\[
 \sum_{s=0}^t h|F_s|
 \leq1.1|F_t|\sum_{j=0}^t40^{-j}
 <\frac{1.1r}{1-1/40}=\frac{22}{975}=:S_*.
 \tag{21}
\]

For t=0 no previous amplification is required, and the same inequality
holds. Summing (12) over these steps, using (18), bounds the movement
from theta_0 through the next endpoint by

\[
 \begin{array}{ll}
 |a_{i,t+1}-a_{i,0}|<.225S_*=33/6500<.005077,\\
 |W_{ij,t+1}-W_{ij,0}|<d_+S_*=28809/162500<.177287,\\
 |c_{j,t+1}-c_{j,0}|<c_*S_*<.017210.
 \end{array}
 \tag{22}
\]

The initial a interval is [7.99,8.01], the initial c interval is
[1.999,2.001], and .177287<.2. These bounds put theta_{t+1} strictly
inside T(W_0). This proves endpoint containment without using the
amplification of the step under consideration.

The tube is convex in the actual (a,B,c) coordinates: its W constraints
are affine rescalings of B constraints. Hence the full segment
theta(s)=theta_t-s eta F_t grad F(theta_t), 0<=s<=1, lies in the tube.
The fundamental theorem of calculus and (19) give exactly

\[
 F_{t+1}=F_t(1-hK_t),\qquad
 K_t=m\int_0^1\langle\nabla F(\theta(s)),\nabla F(\theta_t)\rangle\,ds,
 \quad50<K_t<63.
 \tag{23}
\]

Since .9<=h<=1.1,

\[
 44<hK_t-1<68.3.
 \tag{24}
\]

Thus the next residual has the opposite sign and its magnitude is
between 40 and 69 times the previous magnitude. This completes the
induction for every step whose starting residual has magnitude below r.

If |F_0|>=m^{-4} and no exit has occurred by N_m, the induction gives
|F_{N_m}|>=40^{N_m}m^{-4}>=r, a contradiction. Therefore
1<=tau<=N_m. Its last step begins below r and amplifies by less than
69, so r<=|F_tau|<69r=1.38. All endpoints through exit belong to the
tube. Taking theta'=theta_t in (19) proves the kernel assertion in (6).

Finally, (18) implies 7.2<D_ij<7.86, whence |D_ij-7.53|<.33.
For any t<=tau, sum the W update to obtain

\[
 W_{ij,t}-W_{ij,0}-b_t
 =-\sum_{s=0}^{t-1}hF_s(D_{ij,s}-7.53).
 \tag{25}
\]

Its absolute value is less than .33S_*=121/16250<.0075. This proves
(9). Averaging (25) over any row or column preserves this bound.

## 4. Probability of the initial conditions

### Row concentration

For a centered sign S, log E exp(tS) has value and first derivative
zero at t=0. Its second derivative is a tilted variance of a variable
in [-1,1], which is at most 1. Integrating twice gives
E exp(tS)<=exp(t²/2). Independence and Markov's inequality imply

\[
 \Pr\left(\operatorname{mean}_{j}S_{ij}>.02\right)
 \leq\exp(-.02tm+mt^2/2).
\]

Choose t=.02 and repeat for -S. A union bound over m rows gives

\[
 \Pr(E_m^c)\leq2m\exp(-m/5000).
 \tag{26}
\]

### An upper bound for the initial residual

Condition on all initial a and c. The m² initial W variables remain
independent, with symmetric laws supported in [-1.001,1.001]. Reversing
every W in one row reverses the sign of that row's tanh output, so
E[F_0|a,c]=0. Changing just W_ij alters F_0 by at most

\[
 d_m=\frac{2\cdot1.001\cdot8.01}{m^2}=\frac{16.03602}{m^2},
 \tag{27}
\]

because partial_{W_ij}F=a_i q_i u_j/m² has absolute value at most
8.01/m², throughout that change.

Here is the bounded-difference inequality needed for these independent
variables. Reveal them successively and use the conditional expectation
martingale of F_0. The martingale difference corresponding to a
coordinate has conditional mean zero and range of length at most d_m:
averaging over the same unrevealed coordinates preserves the coordinate
oscillation bound. If X has mean zero and range length d, the second
derivative of log E exp(tX) is at most d²/4. Indeed, under any tilted
law, variance is bounded by the expected squared distance from the
midpoint of that range, which is at most d²/4. Integration twice gives
E exp(tX)<=exp(t²d²/8). Conditional iteration over the martingale
differences and optimization of Markov's inequality yield

\[
 \Pr(|F_0|\geq r\mid a,c)
 \leq2\exp\left(-\frac{2r^2}{m^2d_m^2}\right)
 =2\exp\left(-\frac{2r^2m^2}{16.03602^2}\right).
 \tag{28}
\]

Since 16.03602²<320 and r=.02, this is at most
2 exp(-m²/400000). The estimate is uniform in a,c and hence holds
unconditionally.

### Excluding an excessively small residual

Condition on every initial variable except U_11, including all signs.
If the conditioned signs belong to E_m, they do so for every value
of U_11 in its interval. The initial preactivation estimate in Section 2
holds on that entire interval. Differentiation with respect to U_11 gives

\[
 \left|\frac{dF_0}{dU_{11}}\right|
 =\frac{a_1u_1q_1}{m^2}
 \geq\frac{7.99\cdot.96(1-.02527^2)}{m^2}
 >\frac7{m^2}.
 \tag{29}
\]

Its sign is S_11, so the conditional function is strictly monotone.
For any s>0, the preimage of [-s,s] therefore has length at most
2sm²/7. The uniform interval for U_11 has length .002. Thus

\[
 \Pr(E_m\text{ and }|F_0|<s)
 \leq\frac{1000}{7}sm^2<143sm^2.
 \tag{30}
\]

Taking s=m^{-4} gives the last failure term in (4). This conditioning
argument includes every other coordinate's fluctuations and does not
assume independence after conditioning on the output.

The union of (26), (28), and (30) proves that E_m and
m^{-4}<=|F_0|<r hold with the probability in (4). On that one event,
Section 3 is deterministic and uniform in h in [.9,1.1]. No union over
learning rates is needed.

At m=200000, the three failure terms are bounded above by

\[
 (400000+2)e^{-40}+143/(200000)^2<4\cdot10^{-9},
 \tag{31}
\]

using e^{40}>2·10^{17}, which follows from S_100(40) in (20).
Each term decreases for larger m: the derivative of m e^{-m/5000}
is negative when m>5000, and the other terms decrease directly.
Also 40^{12}<(200000)^4/50<=40^{13}. This proves the numerical
probability and time assertions.

## Scope

The unbiased middle-layer law (2) differs from the earlier biased law
only in the sign probabilities. The result supplies a controlled
multi-step amplification and a common weight displacement before the
residual reaches a fixed window. By (22), each W entry keeps its initial
sign through exit: its initial magnitude is at least .999 and it moves
by less than .177287. In particular, a region requiring every W entry
to be negative has not been reached. The NTK remains large through this
window; a drop has not been proved. No claim about the trajectory after
tau, convergence, divergence, eta_max, centered output or input layers,
or nontrivial data follows from this theorem.
