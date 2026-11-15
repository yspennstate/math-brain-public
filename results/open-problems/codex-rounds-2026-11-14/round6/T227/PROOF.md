# Loss growth followed by convergence for unbiased middle-layer signs

## Statement

For an integer width \(m\), consider
\[
 F_\theta(x)=\frac1m\sum_{i=1}^m a_i\tanh z_i(x),\qquad
 z_i(x)=\frac1{\sqrt m}\sum_{j=1}^mB_{ij}\tanh(c_jx).
 \tag{1}
\]
All \(m^2+2m\) coordinates \((a,B,c)\) are separately trained by
simultaneous Euclidean gradient descent with constant step \(\eta\) on
\(L(\theta)=F_\theta(1)^2/2\). There are no biases or tied parameters.
The data law is the point mass at \((1,0)\). Set
\(W_{ij}=\sqrt m B_{ij}\), \(h=\eta/m\), \(F_t=F_{\theta_t}(1)\),
and \(\lambda_t=\|\nabla_\theta F_{\theta_t}(1)\|^2\).

The new deterministic assertion is as follows. For every finite initial
parameter vector and every \(0<\eta<2m\),
\[
 \sum_{t=0}^\infty F_t^2
 \leq \frac{m^{-1}\sum_i a_{i,0}^2}{h(2-h)},\qquad
 F_t\longrightarrow0,\qquad L_t\longrightarrow0.
 \tag{2}
\]
No hypothesis on subsequent hidden-layer motion is needed.

In particular, initialize all variables independently by
\[
 \begin{split}
 a_i&\sim\operatorname{Unif}[7.99,8.01],\qquad
 c_j\sim\operatorname{Unif}[1.999,2.001],\\
 W_{ij}&=S_{ij}U_{ij},\qquad U_{ij}\sim\operatorname{Unif}[.999,1.001],
 \qquad \Pr(S_{ij}=1)=\Pr(S_{ij}=-1)=\tfrac12.
 \end{split}
 \tag{3}
\]
For every \(m\geq200000\), with probability at least
\[
 1-2m e^{-m/5000}-2e^{-m^2/400000}-\frac{143}{m^2}
 >1-4\cdot10^{-9},
 \tag{4}
\]
the following hold simultaneously for every fixed
\(\eta\in[.9m,1.1m]\). There is a first time
\(\tau=\min\{t:|F_t|\geq .02\}\) satisfying
\[
 \begin{gathered}
 m^{-4}\leq |F_0|<.02,\qquad
 1\leq\tau\leq N_m:=\min\{n:40^n\geq m^4/50\},\\
 F_tF_{t+1}<0,\qquad 40|F_t|\leq |F_{t+1}|\leq69|F_t|
 \quad(0\leq t<\tau),\\
 .02\leq |F_\tau|<1.38,\qquad
 50/m<\lambda_t<63/m\quad(0\leq t\leq\tau).
 \end{gathered}
 \tag{5}
\]
The conclusions (5) are the preceding escape lemma. The continuation is
\[
 \boxed{\quad
 \sum_{t=0}^\infty L_t\leq\frac{71289}{2200}<32.405,
 \qquad L_t\longrightarrow0.
 \quad}
 \tag{6}
\]
Thus the loss rises by a factor at least 1600 at every step before
\(\tau\), at an initial effective step \(\eta\lambda_0>45>2\), and
subsequently converges to zero. This conclusion covers every overshoot
in (5). It does not assert that the subsequent loss is monotone.

For every positive integer \(T\), (6) also gives
\[
 \frac1T\sum_{t=0}^{T-1}L_t\leq\frac{71289}{2200T},\qquad
 \min_{0\leq t<T} L_t\leq\frac{71289}{2200T}.
 \tag{7}
\]
These are an average-loss bound and a best-iterate bound, not a pointwise
rate for \(L_T\). The probability event is common to all stated steps;
uniform convergence in the step parameter is not asserted.

## 1. Exact output-layer energy identity

At time \(t\), let \(v_{i,t}=\tanh z_i(1)\), and put
\[
 E_t=\frac1m\sum_i a_{i,t}^2,\qquad
 Q_t=\frac1m\sum_i v_{i,t}^2.
 \tag{8}
\]
Since \(\partial F/\partial a_i=v_i/m\), simultaneous Euclidean
gradient descent gives exactly
\[
 a_{i,t+1}=a_{i,t}-hF_t v_{i,t}.
 \tag{9}
\]
Every quantity on the right is evaluated before the update. Expanding
the square and summing (9) gives
\[
 \begin{split}
 E_{t+1}
 &=E_t-\frac{2hF_t}{m}\sum_i a_{i,t}v_{i,t}
       +\frac{h^2F_t^2}{m}\sum_i v_{i,t}^2\\
 &=E_t-2hF_t^2+h^2F_t^2Q_t\\
 &=E_t-h(2-hQ_t)F_t^2.
 \end{split}
 \tag{10}
\]
The middle equality uses the actual pre-update network output
\(m^{-1}\sum_i a_{i,t}v_{i,t}=F_t\). It makes no assumption about
\(v_{i,t+1}\), the future NTK, or the hidden-layer gradients.

For completeness, the identity has an independent orthogonal derivation.
Write \(a=(a_i)_i\), \(v=(v_i)_i\). Equation (9) is
\[
 a^+=\left(I-\frac h m vv^\top\right)a.
 \tag{11}
\]
If \(Q=0\), then \(v=0\), \(F=0\), and (10) is immediate. Otherwise
decompose
\[
 a=a_\perp+\frac FQ v,\qquad a_\perp^\top v=0.
\]
The update fixes \(a_\perp\) and multiplies the component parallel to
\(v\) by \(1-hQ\). Hence
\[
 E=\frac{\|a_\perp\|^2}{m}+\frac{F^2}{Q},\qquad
 E^+=\frac{\|a_\perp\|^2}{m}+(1-hQ)^2\frac{F^2}{Q}.
\]
Subtracting proves (10) again, since
\(((1-hQ)^2-1)/Q=-2h+h^2Q\).

## 2. Global convergence

For every finite real \(z\), \(|\tanh z|<1\); in particular
\(0\leq Q_t\leq1\). If \(0<h<2\), (10) implies
\[
 E_{t+1}\leq E_t-h(2-h)F_t^2\leq E_t.
 \tag{12}
\]
All finite iterates exist: at a finite parameter vector, (1) and all its
first derivatives are finite, so one simultaneous update is finite.
Induction defines every iterate at every finite time. No uniform bound
on hidden parameters is needed for this induction.

Sum (12) for \(t=0,\ldots,T-1\). Since \(E_T\geq0\),
\[
 h(2-h)\sum_{t=0}^{T-1}F_t^2\leq E_0-E_T\leq E_0.
 \tag{13}
\]
The partial sums on the left increase and are bounded. They therefore
converge to a finite sum. If \(F_t\) did not tend to zero, some
\(\varepsilon>0\) would satisfy \(|F_t|\geq\varepsilon\) at infinitely
many times, making the sum of squares infinite. This contradiction proves
(2). Since \(L_t=F_t^2/2\), the loss also tends to zero.

The proof is deterministic and applies to any sequence of bounded
pre-update features with the update (9). In particular it applies when
every hidden coordinate is updated simultaneously, as in (1). It also
applies to any deeper architecture whose final hidden features are
bounded by one and whose output has the same mean normalization.

For (3), \(E_0\leq 8.01^2=64.1601\). Throughout \(.9\leq h\leq1.1\),
\[
 h(2-h)=1-(h-1)^2\geq .99.
\]
Thus (13) gives
\[
 \sum_{t=0}^\infty F_t^2\leq\frac{64.1601}{.99}
 =\frac{71289}{1100},
\]
which proves (6); summing only the first \(T\) losses proves (7).
More precisely, telescoping the exact identity also gives
\[
 E_T+\sum_{t=0}^{T-1}h(2-hQ_t)F_t^2=E_0.
 \tag{14}
\]
This identity can be checked along a trajectory without estimating any
hidden-layer derivatives.

## 3. Escape lemma and its probability event

Here are the estimates establishing the inherited claim (5), to make its
application independent of an unstated continuation assumption. Define
\[
 \begin{split}
 u_j&=\tanh c_j,& r_j&=1-u_j^2,\\
 z_i&=\frac1m\sum_jW_{ij}u_j,&v_i&=\tanh z_i,&q_i&=1-v_i^2,\\
 A_i&=v_i,& D_{ij}&=a_iq_i u_j,&
 C_j&=\frac{r_j}{m}\sum_i a_iq_i W_{ij}.
 \end{split}
 \tag{15}
\]
Direct differentiation in \((a,B,c)\), not \((a,W,c)\), gives
\[
 \partial_{a_i}F=A_i/m,\quad
 \partial_{B_{ij}}F=D_{ij}/(m\sqrt m),\quad
 \partial_{c_j}F=C_j/m.
 \tag{16}
\]
Thus the exact auxiliary-coordinate updates are
\[
 a_i^+=a_i-hFA_i,\qquad W_{ij}^+=W_{ij}-hFD_{ij},\qquad
 c_j^+=c_j-hFC_j.
 \tag{17}
\]
For arbitrary two parameter vectors, direct summation of (16) gives
\[
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 =\frac1m\sum_i A_i'A_i+
   \frac1{m^2}\sum_{ij}D_{ij}'D_{ij}+
   \frac1m\sum_j C_j'C_j.
 \tag{18}
\]

Let \(\mathcal R_m\) be the event that every row sign average has absolute
value at most .02. On this event,
\(|\operatorname{mean}_jW_{ij,0}|\leq.021\) and
\(\operatorname{mean}_j|W_{ij,0}|\leq1.001\). Consider the convex tube
\[
 7.9\leq a_i\leq8.1,\quad 1.97\leq c_j\leq2.03,\quad
 |W_{ij}-W_{ij,0}|\leq.2.
 \tag{19}
\]
The elementary bounds \(.96<\tanh(1.97)\) and
\(\tanh(2.03)<.97\) imply \(.96<u_j<.97\) in this tube. Write
\(u_j=.965+e_j\), \(|e_j|<.005\). Then
\[
 |z_i|\leq .965\cdot.021+.005\cdot1.001+.2\cdot.97
 =.21927<.225.
 \tag{20}
\]
At initialization the same calculation omits the final term and gives
\(|z_{i,0}|\leq.02527\). Since \(|\tanh z|\leq|z|\), throughout
(19) we have
\[
 \begin{split}
 |A_i|&<.225,\qquad |W_{ij}|\leq1.201,\\
 d_-:=7.9(1-.225^2)\,.96&=7.20006<D_{ij}<7.857=:d_+,\\
 |C_j|&<(1-.96^2)\,8.1\cdot1.201=.76268304=:c_*.
 \end{split}
 \tag{21}
\]
Equation (18) consequently implies, for two arbitrary points of the tube,
\[
 \begin{split}
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 &>d_-^2-.225^2-c_*^2
 =51.2085535840963584>50,\\
 m\langle\nabla F(\theta'),\nabla F(\theta)\rangle
 &<d_+^2+.225^2+c_*^2
 =62.3647594195036416<63.
 \end{split}
 \tag{22}
\]
The signs of the first and third terms in (18) are unrestricted, which
accounts for their negative allowances in the lower bound.

Suppose \(0<|F_0|<r:=.02\). Inductively, if the iterates through time
\(t\) lie in the tube, \(|F_s|<r\) for \(s\leq t\), and every
previous step amplified the residual by at least 40, then
\[
 \sum_{s=0}^t h|F_s|
 <1.1r\sum_{j=0}^\infty40^{-j}=\frac{22}{975}=:S_*.
 \tag{23}
\]
At \(t=0\) no previous amplification is required. Summing (17) with
(21) bounds the displacement of the next endpoint from initialization by
\[
 .225S_*<.005077\quad\text{in }a,\qquad
 d_+S_*<.177287\quad\text{in }W,\qquad
 c_*S_*<.017210\quad\text{in }c.
 \tag{24}
\]
These put the endpoint strictly in (19). By convexity, its whole update
segment is in the tube. Only now apply the fundamental theorem of calculus
and (22), obtaining
\[
 F_{t+1}=F_t(1-hK_t),\qquad
 K_t=m\int_0^1\langle\nabla F(\theta_t-s\eta F_t\nabla F(\theta_t)),
                                  \nabla F(\theta_t)\rangle\,ds,
 \quad 50<K_t<63.
 \tag{25}
\]
For \(.9\leq h\leq1.1\), \(44<hK_t-1<68.3\), proving the
claimed alternating amplification between 40 and 69. This closes the
induction until the first exit. If additionally \(|F_0|\geq m^{-4}\),
failure to exit by \(N_m\) would imply
\(|F_{N_m}|\geq40^{N_m}m^{-4}\geq r\), a contradiction. The last
step starts below \(r\), so \(|F_\tau|<69r=1.38\). Taking equal
vectors in (22) gives the NTK bounds through exit.

It remains to bound the probability of the initial hypotheses. A centered
sign satisfies \(\mathbb E e^{tS}\leq e^{t^2/2}\): the log moment
generating function and its first derivative vanish at zero, while its
second derivative is a tilted variance bounded by 1. Integrating twice
proves the assertion. Independence, Markov's inequality with \(t=.02\),
the negative tail, and a union over rows give
\[
 \Pr(\mathcal R_m^c)\leq2m e^{-m/5000}.
 \tag{26}
\]

Condition on all \(a,c\). The \(m^2\) middle weights remain independent,
and row reversal implies \(\mathbb E[F_0\mid a,c]=0\). Changing one
\(W_{ij}\) changes \(F_0\) by at most
\(d_m=2\cdot1.001\cdot8.01/m^2=16.03602/m^2\), because
\(|\partial_{W_{ij}}F|\leq8.01/m^2\). The bounded-difference estimate is
\[
 \Pr(|F_0|\geq r\mid a,c)
 \leq2\exp\left(-\frac{2r^2}{m^2d_m^2}\right)
 \leq2e^{-m^2/400000}.
 \tag{27}
\]
To obtain the first inequality without further assumptions, reveal the
independent weights one at a time. Each difference of the conditional
expectation martingale has conditional mean zero and range length at
most \(d_m\). A mean-zero variable of range length \(d\) has log moment
generating function at most \(t^2d^2/8\): its second derivative is a
tilted variance bounded by \(d^2/4\), followed by two integrations.
Conditional iteration and optimization of Markov's inequality give the
first bound in (27). The last uses \(16.03602^2<320\) and \(r=.02\).

Finally, condition on every initial variable except \(U_{11}\), including
all signs. On \(\mathcal R_m\), the initial preactivation bound holds on
the entire remaining interval, and
\[
 \left|\frac{dF_0}{dU_{11}}\right|
 =\frac{a_1u_1q_1}{m^2}
 \geq\frac{7.99\cdot.96(1-.02527^2)}{m^2}
 >\frac7{m^2}.
 \tag{28}
\]
The derivative has constant sign \(S_{11}\). Thus the preimage of
\([-s,s]\) has length at most \(2sm^2/7\). Since \(U_{11}\) is
uniform on an interval of length .002, and the row event depends only on
the conditioned signs,
\[
 \Pr(\mathcal R_m\text{ and }|F_0|<s)\leq\frac{1000}{7}sm^2
 <143sm^2.
 \tag{29}
\]
Take \(s=m^{-4}\) and combine (26)--(29). This proves (4) and the common
initial event used in (5). At \(m=200000\), its failure bound is below
\((400000+2)e^{-40}+143/(200000)^2<4\cdot10^{-9}\). Each term
decreases for larger \(m\). Also \(40^{12}<(200000)^4/50\leq40^{13}\),
so \(N_{200000}=13\).

All decimals above denote exact rationals. The transcendental comparisons
can be certified by
\[
 S_n(x)=\sum_{k=0}^n\frac{x^k}{k!},\qquad
 S_n(x)\leq e^x\leq S_n(x)+
 \frac{x^{n+1}}{(n+1)!}\frac1{1-x/(n+2)}
 \quad(0\leq x<n+2).
 \tag{30}
\]
The upper bound follows by bounding the successive ratios in the omitted
tail by \(x/(n+2)\). With \(n=72\), apply (30) at 3.94, 4.06, and
40, and use the increasing function \((s-1)/(s+1)\), to verify the two
tanh bounds and the probability comparison. The remaining comparisons are
rational. `recheck_escape.py` implements them and independently audits the
metric in literal Euclidean coordinates.

## 4. What the continuation does and does not settle

Combining Sections 2 and 3 proves loss growth and eventual zero loss for
the centered middle-layer law. No continuation estimate is required on
\(W,c\), and no exit value in (5) is omitted. The output energy also
gives \(|F_t|^2\leq E_tQ_t\leq E_0\) by Cauchy--Schwarz, so
\(|F_t|\leq8.01\) along these trajectories.

The zero label is essential to (10). For label \(y\), write
\(R_t=F_t-y\); then the same expansion instead yields
\[
 E_{t+1}-E_t=-2hR_tF_t+h^2R_t^2Q_t,
\]
which need not be negative. For example, \(a=0\) and a nonzero bounded
feature give \(F=0\), and a nonzero label makes the next output energy
positive. Thus (2) is not a theorem for arbitrary labels.

The number \(2m\) is the boundary of this sufficient general estimate.
For fixed features \(v_i=1\), the output update is exactly
\(F_{t+1}=(1-h)F_t\): at \(h=2\), nonzero residuals alternate without
decay, and at \(h>2\) they diverge. This shows that the open interval
\(0<h<2\) cannot be enlarged for arbitrary bounded feature sequences.
These fixed features do not give a divergence example for the trained
tanh architecture (1), so they do not identify its \(\eta_{\max}\).

There is no proved NTK drop after \(\tau\), no assertion of monotonic
loss after \(\tau\), no pointwise convergence rate, and no proof that
all parameters converge. The exact identity controls output energy and
the sum of squared residuals; it does not bound the sum of absolute
residuals. For the stated model, every \(0<\eta<2m\) converges in loss,
so any supremum of convergent learning rates is at least \(2m\). Neither
convergence at the endpoint nor divergence above it follows. A maximal
step, an NTK reduction theorem, and nonzero-label data remain separate
questions.
