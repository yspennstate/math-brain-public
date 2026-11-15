# Small Gaussian biases at simultaneous critical initialization

All matrices and vectors below are real. Haar matrices are distributed on the full orthogonal group. Expectations use probability measures.

## 1. The statement

Let \(O_l\in O(n)\) be independent Haar matrices and let \(\xi_l\sim N(0,I_n)\) be independent of each other and of the matrices. Consider

\[
h_l=\tanh(gO_lh_{l-1}+\sqrt b\,\xi_l),\qquad
J_l=g\operatorname{diag}(\operatorname{sech}^2(gO_lh_{l-1}+\sqrt b\,\xi_l))O_lJ_{l-1},
\quad J_0=I_n.                                                     \tag{1}
\]

The gain and bias variance are deterministic and identical at all layers. The Jacobian differentiates the input with all weights and biases held fixed.

Define

\[
\mu_G(a)=\mathbb E\operatorname{sech}^4(\sqrt aG),\qquad
A_G(a)=\mathbb E\tanh^2(\sqrt aG),\qquad G\sim N(0,1).
\tag{2}
\]

**Theorem.** Suppose \(n,L=L(n)\to\infty\), \(a=a_n>0\), and

\[
La^2+La/n\longrightarrow0.
\tag{3}
\]

Set

\[
g^2=\mu_G(a)^{-1},\qquad b=a-g^2A_G(a),\qquad
\|h_0\|^2/n=A_G(a),
\tag{4}
\]

with any deterministic direction for \(h_0\). Then \(b>0\), and the empirical squared-singular-value measure of the ordinary Jacobian satisfies

\[
W_2\left(\frac1n\sum_{i=1}^n\delta_{s_i(J_L)^2},\delta_1\right)
\xrightarrow{\mathbb P}0.
\tag{5}
\]

The parameters satisfy exactly the Gaussian mean-field equations
\(g^2\mu_G(a)=1\) and \(g^2A_G(a)+b=a\). These equations specify the initialization; they do not assert exact finite-width stationarity.

More generally, the conclusion holds whenever, eventually,

\[
0\leq b\leq14a^3,\quad |\log(g^2)-2a|\leq15a^2,\quad
\left|\frac{g^2\|h_0\|^2}{na}-1\right|\leq14a^2.
\tag{6}
\]

The proof also shows, with

\[
q_l=g^2\|h_{l-1}\|^2/n,\qquad
\mu_n(q,b)=\mathbb E_{u,\xi}\operatorname{sech}^4(\sqrt{nq}\,u_1+\sqrt b\,\xi_1),
\quad S_L=\prod_{l=1}^L g^2\mu_n(q_l,b),
\tag{7}
\]

that \(\max_{l\leq L+1}|q_l/a-1|\to0\) and \(S_L\to1\) in probability. The vector \(u\) is uniform on \(S^{n-1}\), independent of \(\xi\). The number \(q_l\) is the signal variance before adding the new bias. The scalar \(S_L\) is an auxiliary quantity, with no change to (1).

This theorem concerns vanishing target variance. It gives no full limiting density, fixed-positive-variance theorem, or control of extreme singular values.

## 2. Scalar and moment bounds

For every real \(x\),

\[
0\leq\tanh^2x-x^2+\frac23x^4\leq\frac{17}{45}x^6,
\qquad
0\leq\operatorname{sech}^4x-1+2x^2\leq\frac73x^4.
\tag{8}
\]

To prove the first inequality take \(x\geq0\) and put \(t=x-\tanh x\). Since \(t=\int_0^x\tanh^2s\,ds\), one has \(0\leq t\leq x^3/3\). Hence
\(0\leq x^2-\tanh^2x\leq(2/3)x^4\), and integration gives
\(0\leq x^3/3-t\leq2x^5/15\). The first remainder in (8) equals
\(2x(x^3/3-t)+t^2\), between zero and \((4/15+1/9)x^6\). Evenness handles negative \(x\). The second remainder is
\(2(x^2-\tanh^2x)+\tanh^4x\), which proves both its bounds.

Let \(Z\) have \(\mathbb EZ^2=r\) and \(\mathbb EZ^4\leq3r^2\). For \(r\leq1/4\), (8) implies

\[
1-2r\leq\mu:=\mathbb E\operatorname{sech}^4Z\leq1,
\qquad |\log\mu+2r|\leq15r^2.
\tag{9}
\]

Indeed \(0\leq\mu-1+2r\leq7r^2\). If \(s=-\log\mu\), then \(s\leq-\log(1-2r)\leq4r\), and
\(0\leq s-(1-e^{-s})\leq s^2/2\), by integrating \(1-e^{-t}\leq t\). This proves (9).

For a uniform sphere vector the exact moments are

\[
\mathbb E\prod_i u_i^{2k_i}
=\frac{\prod_i(2k_i-1)!!}{n(n+2)\cdots(n+2\sum_i k_i-2)}.
\tag{10}
\]

Write a standard Gaussian vector as its independent radius and direction. Gaussian integration by parts gives the numerator coordinate moments and the radial moment in the denominator, proving (10). Odd moments vanish by sign symmetry.

For \(z_i=\sqrt{nq}\,u_i+\sqrt b\,\xi_i\), put \(r=q+b\). Expanding each even power, using independence, and comparing each spherical even moment with its Gaussian counterpart gives

\[
\mathbb Ez_i^2=r,\quad \mathbb Ez_i^4\leq3r^2,\quad
\mathbb Ez_i^6\leq15r^3,\quad \mathbb Ez_i^8\leq105r^4.
\tag{11}
\]

All coefficients of the surviving even powers are nonnegative, so the comparisons are valid term by term. More exactly,

\[
\mathbb Ez_i^4=\frac{3n}{n+2}q^2+6qb+3b^2,
\qquad
\mathbb E_\xi z_i^4=q^2y_i^2+6qby_i+3b^2
\leq3r^2(1+y_i^2),\quad y_i=nu_i^2.
\tag{12}
\]

For the last inequality first bound the polynomial by \(3(qy_i+b)^2\), then use \(qy_i+b\leq r\max(1,y_i)\).

## 3. The critical bias is nonnegative and small

A Gaussian variance inequality needed here follows directly from integration by parts. For independent standard normals \(G,H\), define \(G_t=\sqrt tG+\sqrt{1-t}H\) and
\(F(t)=\mathbb E f(G)f(G_t)\). For smooth bounded \(f\) with bounded derivatives, differentiating and integrating by parts separately in \(G,H\) gives

\[
F'(t)=\frac1{2\sqrt t}\mathbb E f'(G)f'(G_t),\qquad0<t<1.
\]

In detail, differentiating produces factors \(G/(2\sqrt t)\) and \(-H/(2\sqrt{1-t})\). Integration by parts in the first gives the displayed derivative term plus \(\tfrac12\mathbb E f(G)f''(G_t)\); integration by parts in the second cancels that latter term. Cauchy–Schwarz bounds the remaining expectation by \(\mathbb Ef'(G)^2\). Integrating, with \(\int_0^1(2\sqrt t)^{-1}dt=1\), yields
\(\operatorname{Var}f(G)\leq\mathbb Ef'(G)^2\). Bounded derivatives justify the endpoint limits and the integrable derivative bound.

Take \(f(G)=\tanh(\sqrt aG)\), whose mean is zero. Then
\(A_G(a)\leq a\mu_G(a)\), proving \(b\geq0\). The inequality is strict for \(a>0\): \(f'(G)\) is nonconstant, so at \(t=0\) its two independent copies satisfy
\(\mathbb Ef'(G)f'(H)<\mathbb Ef'(G)^2\). Continuity makes the integrated upper bound strict on a nonempty interval of positive \(t\). Thus \(b>0\). By (8),

\[
A_G(a)=a-2a^2+R_A,\quad 0\leq R_A\leq\frac{17}{3}a^3,
\qquad \mu_G(a)=1-2a+R_\mu,\quad0\leq R_\mu\leq7a^2.
\]

Consequently, for \(a\leq1/4\),

\[
0\leq b=\frac{a\mu_G(a)-A_G(a)}{\mu_G(a)}
=\frac{aR_\mu-R_A}{\mu_G(a)}\leq14a^3.
\tag{13}
\]

Equation (9) verifies the gain condition in (6). The input choice in (4) gives \(q_1=a-b\), hence \(|q_1/a-1|\leq14a^2\). Thus (4) implies (6).

## 4. A one-layer estimate with derivative-dependent gates and biases

Condition on the preceding network. Let \(X\succeq0\), \(e=h/\|h\|\), \(B=OXO^\top\), \(u=Oe\), and define

\[
A_{ii}=\frac{\operatorname{sech}^4(z_i)}{\mu_n(q,b)},\quad
X'=A^{1/2}BA^{1/2},\quad T=\operatorname{Tr}X,\quad Q=\operatorname{Tr}X^2,
\quad\alpha=e^\top Xe,\quad\gamma=e^\top X^2e.
\]

The following estimates hold for \(n\geq3\) and \(r=q+b\leq1/4\):

\[
\mathbb E\operatorname{Tr}X'
=T-\frac{4q}{n+2}(n\alpha-T)+R_1,\quad |R_1|\leq640r^2T,
\tag{14}
\]

\[
\mathbb E\operatorname{Tr}(X'^2)
=Q-\frac{8q}{n+2}(n\gamma-Q)+R_2,\quad |R_2|\leq3328r^2Q.
\tag{15}
\]

The expectation averages the fresh Haar matrix and the independent fresh bias. No gate-weight independence is assumed.

To prove them let \(\mu=\mu_n(q,b)\), \(\Delta=A-I\), \(C_{ii}=2(1-y_i)\), and \(R=A-I-qC\). From (8), write
\(\operatorname{sech}^4z_i=1-2z_i^2+\epsilon_i\), where
\(0\leq\epsilon_i\leq(7/3)z_i^4\). If \(\bar\epsilon=\mathbb E\epsilon_i\), then
\(\mu=1-2r+\bar\epsilon\), \(\bar\epsilon\leq7r^2\), and \(\mu\geq1/2\). Since \(\mathbb E_\xi z_i^2=qy_i+b\),

\[
\mathbb E_\xi R_{ii}
=\frac{2q(1-y_i)(1-\mu)+\mathbb E_\xi\epsilon_i-\bar\epsilon}{\mu}.
\]

Thus, using (12),

\[
|\mathbb E_\xi R_{ii}|
\leq8r^2(1+y_i)+\frac{14}{3}\mathbb E_\xi z_i^4+14r^2
\leq r^2(36+8y_i+14y_i^2)
\leq40r^2(1+y_i^2).
\tag{16}
\]

The final inequality uses \(8y\leq4+4y^2\). Also \(|\Delta_{ii}|\leq4(z_i^2+r)\), because both \(1-\operatorname{sech}^4z_i\leq2z_i^2\) and \(1-\mu\leq2r\). Therefore

\[
\mathbb E_\xi\Delta_{ii}^2
\leq32(\mathbb E_\xi z_i^4+r^2)
\leq128r^2(1+y_i^2).
\tag{17}
\]

For any fixed \(Y\succeq0\), the row moments (10), after rotating \(e\) to the first coordinate, give

\[
\mathbb E\sum_i y_i(OYO^\top)_{ii}
=\frac n{n+2}(\operatorname{Tr}Y+2e^\top Ye),
\tag{18}
\]

\[
\mathbb E\sum_i(1+y_i^2)(OYO^\top)_{ii}
=\operatorname{Tr}Y+
\frac{n^2(3\operatorname{Tr}Y+12e^\top Ye)}{(n+2)(n+4)}
\leq16\operatorname{Tr}Y.
\tag{19}
\]

For clarity, the fourth row moments weight the first diagonal entry by 3 and each other diagonal entry by 1; the sixth row moments weight them by 15 and 3, respectively. Odd row monomials vanish. This proves both identities by summing rows, without independence of rows.

Expand the first trace as \(T+q\operatorname{Tr}(CB)+\operatorname{Tr}(RB)\). Equation (18) gives \(\mathbb E\operatorname{Tr}(CB)=-4(n\alpha-T)/(n+2)\); (16),(19) bound the last term by \(40\cdot16r^2T\). This proves (14).

For the second trace expand

\[
\operatorname{Tr}(ABAB)=Q+2q\operatorname{Tr}(CB^2)
+2\operatorname{Tr}(RB^2)+\operatorname{Tr}(\Delta B\Delta B).
\]

The linear term follows from (18) with \(Y=X^2\). Symmetry of \(B\) and \(2|st|\leq s^2+t^2\) give, pointwise,
\(|\operatorname{Tr}(\Delta B\Delta B)|\leq\sum_i\Delta_{ii}^2(B^2)_{ii}\).
Apply (16),(17),(19) to the remainders to obtain
\((2\cdot40+128)16r^2Q=3328r^2Q\). This proves (15).

Put \(Z=\operatorname{Tr}(X-I)^2/n\). Combining (14),(15), the linear correction to \(\mathbb EZ\) is

\[
\frac{8q}{n+2}\left\{\frac{Q-T}{n}-(\gamma-\alpha)\right\}.
\]

Writing \(E=X-I\), one has \(\gamma-\alpha=e^\top(E^2+E)e\geq-1/4\) by completing the square, and
\((Q-T)/n\leq Z+\sqrt Z\). Since \(\sqrt Z\leq(Z+1)/2\), the linear term is at most \(q(12Z+6)/(n+2)\). The remainder is at most
\(r^2(3328Q/n+1280T/n)\). Finally \(Q/n\leq2Z+2\) and \(T/n\leq3/2+Z/2\). We have proved

\[
\mathbb E[Z'\mid\text{past}]
\leq\left(1+\frac{12q}{n+2}+7296(q+b)^2\right)Z
+\frac{6q}{n+2}+8576(q+b)^2.
\tag{20}
\]

## 5. Forward-radius drift and second moments

For explicit bounds assume hereafter

\[
n\geq64,\qquad0<a\leq1/16384,
\tag{21}
\]

and (6). These conditions hold eventually under (3). Elementary exponential remainder bounds give

\[
g^2\leq2,\quad |g^2-1|\leq4a,\quad
|g^2-1-2a|\leq32a^2.
\tag{22}
\]

Indeed for \(\lambda=\log(g^2)\) one has \(|\lambda|\leq(5/2)a\), and
\(|e^\lambda-1-\lambda|\leq\lambda^2e^{|\lambda|}/2\). Together with \(|\lambda-2a|\leq15a^2\), these inequalities give (22) at (21).

At a step with \(q\in[a/2,2a]\), the exact new radius and relative increment are

\[
q'=\frac{g^2}{n}\sum_i\tanh^2z_i,\qquad U=\frac{q'-q}{q},\qquad d(q)=\mathbb EU.
\tag{23}
\]

Then, with \(c_n=2n/(n+2)\),

\[
|d(q)-(2a-c_nq)|\leq300a^2,\quad |d(q)|\leq7a,
\qquad \mathbb EU^2\leq12000a^2.
\tag{24}
\]

Here and below all one-step expectations condition on the preceding network. The law depends on that network only through \(q\).

For the drift, (8),(11),(12) give

\[
\mathbb E(q'/g^2)=q+b-c_nq^2-4qb-2b^2+R_F,
\qquad0\leq R_F\leq\frac{17}{3}(q+b)^3.
\tag{25}
\]

In subtracting \(2a-c_nq\) from \(d(q)\), the six error bounds, in units of \(a^2\), are respectively

\[
32,\quad16,\quad56,\quad1,\quad1,\quad153.
\tag{26}
\]

They correspond to \(g^2-1-2a\), \(-(g^2-1)c_nq\), \(g^2b/q\), \(-4g^2b\), \(-2g^2b^2/q\), and \(g^2R_F/q\). To verify the small terms, \(4g^2b\leq112a^3\leq a^2\) and \(2g^2b^2/q\leq1568a^5\leq a^2\). For the last term use \(b/q\leq28a^2\leq1/2\), so
\(g^2R_F/q\leq(34/3)(3/2)^3q^2\leq153a^2\). The sum of (26) is 259, less than 300. Also \(2a+c_nq+300a^2\leq7a\), proving the first two claims in (24).

For the second moment put \(v=n^{-1}\sum_i z_i^2\) and \(H=v-n^{-1}\sum_i\tanh^2z_i\). Then

\[
0\leq H\leq\frac{2}{3n}\sum_i z_i^4,\quad
\mathbb E(v-q)^2=b^2+\frac{4qb+2b^2}{n}
\leq3b^2+\frac{4qb}{n},
\quad \mathbb EH^2\leq\frac{140}{3}(q+b)^4.
\tag{27}
\]

For the middle identity condition on \(u\) in
\(v=q+2\sqrt{qb/n}\,u\cdot\xi+(b/n)\|\xi\|^2\). The linear and centered quadratic Gaussian terms are uncorrelated. For the last bound use the square of an average at most the average of squares, then (11).

Since \(q'-q=(g^2-1)q+g^2(v-q)-g^2H\), the square of a sum of three terms is at most three times the sum of their squares. Therefore

\[
\mathbb EU^2\leq48a^2+36(b/q)^2+48b/(nq)
+560(q+b)^4/q^2.
\tag{28}
\]

The four terms are at most \(48a^2,a^2,21a^2,11340a^2\): use \(b/q\leq28a^2\), \(n\geq64\), and \((q+b)^4/q^2\leq(3/2)^4q^2\leq(81/4)a^2\). Their sum is at most \(12000a^2\), completing (24). These are global moment estimates; no individual bias coordinate is bounded.

## 6. A stopped forward-radius bound

Put \(x_k=q_{k+1}/a-1\), so \(|x_0|\leq14a^2\). Stop at its first exit from \((-1/2,1)\), including the exit step, and freeze afterwards. A step is active precisely when no previous exit has occurred. Its conditional drift is
\(B(x)=(1+x)d(a(1+x))\). On active steps \(|B(x)|\leq14a\).

Let \(r_0=8/n+600a\). Equation (24) shows \(B(x)\leq0\) for \(x\geq r_0\) and \(B(x)\geq0\) for \(x\leq-r_0\) within the active interval. For the upper sign use
\(2-c_n(1+r_0)=4/(n+2)-c_nr_0\), \(c_n\geq1\); for the lower sign use \(2-c_n(1-r_0)=4/(n+2)+c_nr_0\). The error \(300a\) is absorbed by \(r_0\).

Write the stopped process as \(\bar x_k=x_0+\sum_{j<k}\bar B_j+M_k\), with \(M_0=0\). The active indicator is measurable before drawing the new matrix and bias; hence \(M\) is a martingale. From (24), its one-step variance is at most \(4\cdot12000a^2\), and so

\[
\mathbb EM_L^2\leq48000La^2,\qquad
\mathbb P\{\max_{k\leq L}|M_k|>\delta\}
\leq48000La^2/\delta^2.
\tag{29}
\]

The last inequality follows by stopping the square submartingale at its first crossing of \(\delta^2\). Orthogonality of martingale differences gives the first inequality.

Pathwise,

\[
\max_{k\leq L}|\bar x_k|\leq r_0+14a+2\max_{k\leq L}|M_k|.
\tag{30}
\]

To see this, if \(\bar x_k>r_0\), take the last preceding index \(j\) at which \(\bar x_j\leq r_0\). It exists because \(|x_0|\leq r_0\). The next drift is at most \(14a\); every later drift is nonpositive or frozen. Thus \(\bar x_k\leq r_0+14a+M_k-M_j\). The same argument at the last index with \(\bar x_j\geq-r_0\) proves the lower bound. This includes a possible exit jump.

For \(0<\delta\leq1/16\), (21) gives
\(8/n+614a+2\delta<1/2\). Thus on \(\max|M_k|\leq\delta\), no exit occurs and

\[
\max_{l\leq L+1}|q_l/a-1|\leq\varepsilon,
\qquad \varepsilon=8/n+614a+2\delta.
\tag{31}
\]

The radii are positive almost surely. If \(b>0\), the fresh preactivation vector has a density and is not zero; if \(b=0\), a nonzero input stays nonzero because tanh vanishes only at zero. Thus every ratio used on active steps is defined.

## 7. Removing the scalar normalization

Let \(U_l=(q_{l+1}-q_l)/q_l\) at active steps. Define a second martingale and a nonnegative error sum by

\[
N_k=\sum_{l\leq k}\mathbf1_{\mathrm{active},l}(U_l-d(q_l)),\qquad
V_k=\sum_{l\leq k}\mathbf1_{\mathrm{active},l}U_l^2.
\]

Equation (24) yields

\[
\mathbb EN_L^2\leq12000La^2,\qquad \mathbb EV_L\leq12000La^2.
\tag{32}
\]

For \(\eta>0\), except on an event of probability at most

\[
\frac{60000La^2}{\delta^2}+\frac{12000La^2}{\eta},
\tag{33}
\]

there is no radius exit, \(|N_L|\leq\delta\), and \(V_L\leq\eta\). This combines (29), the terminal second-moment inequality for \(N_L\), and Markov's inequality for \(V_L\).

On no exit, \(q_{l+1}/q_l\in[1/4,4]\). Taylor's theorem for \(\log t\), whose second derivative has absolute value at most 16 on this interval, gives

\[
\left|\sum_{l=1}^LU_l-\log(q_{L+1}/q_1)\right|\leq8V_L.
\tag{34}
\]

For \(s(q)=\log(g^2)+\log\mu_n(q,b)\), (9),(6) and \(q+b\leq3a\) give

\[
|s(q)-(2a-2q)|\leq152a^2,\qquad
|s(q)-d(q)|\leq\frac{8a}{n+2}+452a^2.
\tag{35}
\]

For the first inequality, \(15a^2+2b+15(q+b)^2\leq152a^2\). For the second combine (24) with \((2-c_n)q=4q/(n+2)\).

By (31) and \(|q_1/a-1|\leq14a^2\),
\(|\log(q_{L+1}/q_1)|\leq2\varepsilon+28a^2\). This uses \(|\log y|\leq2|y-1|\) for \(|y-1|\leq1/2\). Since
\(\log S_L=\sum s(q_l)\), equations (32)–(35) prove

\[
|\log S_L|\leq K,
\quad K=\frac{16}{n}+1228a+28a^2+5\delta+8\eta
+\frac{8La}{n+2}+452La^2,
\tag{36}
\]

with exceptional probability (33). In particular \(S_L\to1\) under (3), taking \(\delta=(La^2)^{1/4}\), \(\eta=(La^2)^{1/2}\). The same choice in (31) proves the asserted uniform radius convergence.

## 8. Accumulation of the Jacobian estimate

Freeze the normalized Gram process just after the radius exits, so it applies the gate of Section 4 exactly on the active steps of Section 6, and applies an identity step afterwards. Its initial matrix is \(I_n\); let its final distortion be \(Z_L^{\mathrm{stop}}\). The decision to apply a gate is measurable from the past. On an active step \(q\leq2a\), \(q+b\leq3a\); on a frozen step the distortion is unchanged. Hence (20) implies

\[
\mathbb EZ_L^{\mathrm{stop}}\leq B_Le^{A_L},\qquad
A_L=\frac{24La}{n+2}+65664La^2,\qquad
B_L=\frac{12La}{n+2}+77184La^2.
\tag{37}
\]

For completeness, iterating a recursion \(z_{k+1}\leq(1+\alpha)z_k+\beta\) from zero gives \(z_L\leq\beta\sum_{j=0}^{L-1}(1+\alpha)^j\leq L\beta e^{L\alpha}\). In (20) use \(\alpha=24a/(n+2)+9\cdot7296a^2\), \(\beta=12a/(n+2)+9\cdot8576a^2\), which proves (37). Active normalized gate entries are at most 2 by (9), so all finite-depth moments needed in this iteration exist.

On no radius exit, this process is exactly \(J_LJ_L^\top/S_L\), by dividing the ordinary recursion (1) by the scalar factors in (7). Markov's inequality and (37) give \(\mathbb P(Z_L^{\mathrm{stop}}>t)\leq B_Le^{A_L}/t\). On the intersection with the event in (36), the Frobenius triangle inequality gives

\[
W_2\left(\frac1n\sum_i\delta_{s_i(J_L)^2},\delta_1\right)
\leq e^K\sqrt t+e^K-1.
\]

The left side equals \(n^{-1/2}\|J_LJ_L^\top-I\|_F\), since coupling to a point mass is unique. Thus the following finite-size bound holds under (6),(21), for \(0<\delta\leq1/16\), \(\eta,t>0\):

\[
\mathbb P\left\{W_2\left(\frac1n\sum_i\delta_{s_i(J_L)^2},\delta_1\right)
>e^K\sqrt t+e^K-1\right\}
\leq\frac{60000La^2}{\delta^2}+\frac{12000La^2}{\eta}
+\frac{B_Le^{A_L}}{t}.
\tag{38}
\]

Under (3), \(a\to0\) and \(A_L,B_L\to0\). Take \(\delta=(La^2)^{1/4}\), \(\eta=(La^2)^{1/2}\), and \(t=(B_Le^{A_L})^{1/2}\), with \(\delta\leq1/16\) eventually. Both the threshold and probability in (38) tend to zero, proving (5) under (6). Section 3 then proves the stated critical-initialization theorem (4).

The empirical singular-value measure itself also converges to \(\delta_1\), since \(|\sqrt\lambda-1|\leq|\lambda-1|\) for \(\lambda\geq0\). No bound on the largest or smallest singular value follows from (38).
