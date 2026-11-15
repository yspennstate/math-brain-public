# Strictly subcritical endpoints in the zero-target rectangle

Let $m\geq d+1$, $d\geq1$, and train both layers of

\[
f_{a,W}(x)=a^TWx,\qquad L_b(a,W)=\tfrac12\|W^Ta-b\|^2
\]

by simultaneous gradient descent with step $\eta>0$. This is the population square loss for $x\sim N(0,I_d)$, with labels $b^Tx$. It is also an exact full-batch loss on the examples $x_j=\sqrt d\,e_j$, with labels $\sqrt d\,b_j$, averaged over $j$. All $m(d+1)$ parameters are trainable.

Set $A=\sqrt\eta\,a$, $U=\sqrt\eta\,W$. For zero target the scaled update is independent of $\eta$:

\[
A^+=A-Uv,\qquad U^+=U-Av^T,\qquad v=U^TA. \tag{1}
\]

Write

\[
q=\|A\|^2,\quad C=U^TU,\quad h=\|v\|^2,\quad
H=C+qI_d,\quad Z=[A\ U],
\]

and define the open rectangle

\[
\mathcal R=\{Z:q<2,\ \lambda_{\max}(C)<2\}. \tag{2}
\]

## Theorem

For every starting point in \(\mathcal R\), \(q_t,C_t\) converge and \(v_t\to0\). Put

\[
S_\infty=q_\infty+\lambda_{\max}(C_\infty),\qquad
D_t=\det[v_t,C_tv_t,\ldots,C_t^{d-1}v_t].
\]

The following deterministic implication holds, including at equality:

\[
S_\infty\geq2\quad\Longrightarrow\quad
D_T=0\text{ for some finite }T. \tag{3}
\]

Each set \(\{Z_0:D_T=0\}\) is the zero set of a nonzero polynomial. Consequently, for any jointly absolutely continuous initialization law,

\[
\mathbb P\{Z_0\in\mathcal R,\ S_\infty\geq2\}=0. \tag{4}
\]

For almost every starting point in \(\mathcal R\), the parameters converge to a full-column-rank global minimizer, with an eventual geometric rate, and

\[
0<\lambda_{\min}(H_\infty)\leq S_\infty<2. \tag{5}
\]

In original parameters the endpoint sharpness is \(S_\infty/\eta<2/\eta\). Neither the gap below 2 nor the geometric rate is asserted to be uniform over \(\mathcal R\).

### 1. Exact recurrences and monotonicity

Expansion of (1) gives

\[
\begin{split}
q^+&=q-2h+v^TCv,\\
C^+&=C-(2-q)vv^T,\\
v^+&=(I-C-qI+hI)v. \tag{6}
\end{split}
\]

For example, the last identity follows by multiplying
\((U^T-vA^T)(A-Uv)\), and using \(U^TA=v\) and \(A^TUv=h\).
Let \(c_0=\lambda_{\max}(C_0)<2\). If \(q_t\leq q_0\) and \(0\preceq C_t\preceq C_0\), then

\[
q_{t+1}\leq q_t-(2-c_0)h_t,\qquad
0\preceq C_{t+1}\preceq C_t. \tag{7}
\]

Here positivity of \(C_{t+1}\) follows independently from its definition as \(U_{t+1}^TU_{t+1}\), and the upper bound uses \(q_t<2\). Induction proves (7) for all times. Therefore

\[
\sum_{t=0}^\infty h_t\leq\frac{q_0}{2-c_0}<\infty,
\qquad v_t\longrightarrow0. \tag{8}
\]

The nonnegative decreasing scalar \(q_t\) converges. Every quadratic form of \(C_t\) decreases and is bounded below. Applying polarization to coordinate vectors proves convergence of every entry of \(C_t\), hence convergence in norm. In particular \(C_t\succeq C_\infty\). Also

\[
\|Z_t\|_F^2\leq M:=q_0+\operatorname{tr}C_0. \tag{9}
\]

An alternative form of the residual update is essential. Put

\[
\alpha=2-q\in(0,2],\qquad \theta=(1-q)(1-h).
\]

Since \(C^+v=Cv-\alpha h v\), (6) becomes

\[
C^+=C-\alpha vv^T,\qquad v^+=(\theta I-C^+)v. \tag{10}
\]

### 2. Residual weight in a top spectral cluster

Here is a matrix lemma that also allows repeated eigenvalues within the cluster.

Let \(B\) be real symmetric, \(u\in\mathbb R^d\), \(\alpha\geq0\), and \(B(s)=B-s\alpha uu^T\), \(0\leq s\leq1\). Suppose the largest \(k\) eigenvalues are separated from the other eigenvalues by at least \(\delta>0\) for every \(s\), where \(1\leq k<d\). Let \(P(s)\) be the orthogonal projector onto those \(k\) eigenspaces, and let \(h=\|u\|^2\). Then

\[
\|P(1)u\|\geq
\exp(-\alpha h/\delta)\|P(0)u\|. \tag{11}
\]

To justify differentiation even with internal eigenvalue multiplicities, work locally in \(s\). Choose a complex contour enclosing precisely the top cluster, at positive distance from the spectrum. The spectral theorem gives

\[
P(s)=\frac{1}{2\pi i}\oint(zI-B(s))^{-1}\,dz.
\]

Indeed diagonalizing \(B(s)\) reduces the integral to integrals of \((z-\lambda)^{-1}\), which equal 1 for enclosed eigenvalues and 0 for the others. The inverse is continuously differentiable while the contour avoids the spectrum, so differentiating under this finite contour integral proves that \(P(s)\) is continuously differentiable. The local formulas agree on overlaps and cover \([0,1]\).

Differentiate \(P^2=P\) and \([B(s),P]=0\). At a fixed \(s\), choose any orthonormal eigenbasis of \(B(s)\), and let \(u_i\) be the coordinates of the fixed vector \(u\) in that basis. The first differentiated identity says that both diagonal blocks of \(\dot P\), for the decomposition into the cluster and its complement, vanish. The second identity gives, for \(i\) in the cluster and \(j\) outside it,

\[
(\lambda_i-\lambda_j)\dot P_{ij}=-\alpha u_i u_j.
\]

It follows that \(b(s):=\|P(s)u\|^2=u^TP(s)u\) obeys

\[
\begin{split}
\dot b(s)
&=-2\alpha\sum_{i\leq k<j}
\frac{u_i^2u_j^2}{\lambda_i-\lambda_j}\\
&\geq-\frac{2\alpha}{\delta}
\left(\sum_{i\leq k}u_i^2\right)
\left(\sum_{j>k}u_j^2\right)
\geq-\frac{2\alpha h}{\delta}\,b(s). \tag{12}
\end{split}
\]

Multiplying by \(\exp(2\alpha hs/\delta)\) and integrating proves
\(b(1)\geq e^{-2\alpha h/\delta}b(0)\). Taking square roots gives (11), including when \(b(0)=0\). If \(k=d\), take \(P=I\); no projector estimate or gap is needed.

### 3. An endpoint at or above 2 forces a finite loss of cyclicity

Suppose \(S_\infty\geq2\). Order the eigenvalues of \(C_\infty\) decreasingly, let \(c_*=\lambda_1(C_\infty)\), and let \(k\) be its multiplicity. Thus

\[
q_\infty+c_*\geq2. \tag{13}
\]

If \(k<d\), put \(\delta=(c_*-\lambda_{k+1}(C_\infty))/2>0\). For all sufficiently large \(t\), norm convergence and eigenvalue continuity give

\[
\lambda_{k+1}(C_t)\leq c_*-\delta.
\]

For every \(s\in[0,1]\),

\[
C_t\succeq C_t-s\alpha_t v_tv_t^T
\succeq C_{t+1}\succeq C_\infty.
\]

The variational characterization of ordered eigenvalues then gives

\[
\lambda_k(C_t-s\alpha_tv_tv_t^T)\geq c_*,\qquad
\lambda_{k+1}(C_t-s\alpha_tv_tv_t^T)\leq c_*-\delta. \tag{14}
\]

Thus the lemma applies to this whole segment. Let \(P_t\) project onto the largest \(k\) eigenspaces of \(C_t\), and put \(a_t=\|P_tv_t\|\). Equation (11) gives

\[
\|P_{t+1}v_t\|\geq e^{-2h_t/\delta}a_t. \tag{15}
\]

For \(k=d\), put \(P_t=I\) and replace the exponential by 1.

For \(j\leq k\), let \(\lambda_j^+=\lambda_j(C_{t+1})\). Since \(q_t\geq q_\infty\), \(\lambda_j^+\geq c_*\), and \(|1-q_t|\leq1\), (13) implies

\[
\lambda_j^+-\theta_t
=\lambda_j^++q_t-1+(1-q_t)h_t
\geq1-h_t. \tag{16}
\]

Choose a finite \(T\) large enough that the preceding cluster estimates hold and \(h_t\leq1/2\) for all \(t\geq T\). On the top cluster every multiplier of \(\theta_t I-C_{t+1}\) has absolute value at least \(1-h_t\). Since \(P_{t+1}\) commutes with \(C_{t+1}\), (10), (15), and (16) yield

\[
a_{t+1}\geq(1-h_t)e^{-2h_t/\delta}a_t\qquad(t\geq T). \tag{17}
\]

For \(0\leq h\leq1/2\),
\(\log(1-h)=-\int_0^h(1-x)^{-1}dx\geq-2h\). Iterating (17) consequently gives

\[
a_t\geq a_T\exp\left[-(2+2/\delta)
\sum_{j=T}^{t-1}h_j\right]. \tag{18}
\]

For \(k=d\), the same bound holds with coefficient 2. The sum is finite by (8). But \(a_t\leq\|v_t\|\to0\). Hence \(a_T=0\).

The projector \(P_T\) is nonzero and commutes with \(C_T\). Thus

\[
P_TC_T^jv_T=C_T^jP_Tv_T=0\qquad(j\geq0).
\]

All the columns defining \(D_T\) lie in the proper subspace \(\ker P_T\). Therefore \(D_T=0\), proving (3). This argument did not require parameter convergence or preservation of augmented rank.

### 4. The finite loss of cyclicity has probability zero

For any symmetric \(C\), define \(Q(C,v)=[v,Cv,\ldots,C^{d-1}v]\). If \(C^+=C-\alpha vv^T\), induction on \(j\) gives

\[
(C^+)^jv=C^jv+\sum_{\ell<j}b_{j\ell}C^\ell v.
\]

Multiplication by \(C^+\) preserves the leading term and adds only lower powers of \(C\) applied to \(v\). Thus the change from \(Q(C,v)\) to \(Q(C^+,v)\) is triangular with diagonal entries 1, and their determinants agree, even when they are singular. Equation (10) gives

\[
Q(C^+,v^+)=(\theta I-C^+)Q(C^+,v).
\]

Taking determinants proves the exact identity

\[
D_{t+1}=\det(\theta_t I-C_{t+1})D_t. \tag{19}
\]

All finite iterates are polynomials in the entries of \(Z_0\). For each fixed \(t\), the factor \(\det(\theta_t I-C_{t+1})\) is a nonzero polynomial: at \(Z_0=0\), every iterate vanishes, \(\theta_t=1\), and the factor equals 1.

The initial polynomial \(D_0\) is also nonzero. For a witness, take \(U_{0,j}=j e_j\), \(1\leq j\leq d\), and \(A_0=e_{d+1}+\sum_{j=1}^d e_j\). Then \(C_0=\operatorname{diag}(1^2,\ldots,d^2)\), \(v_{0,j}=j\), and the Vandermonde determinant gives

\[
D_0=\left(\prod_{j=1}^d j\right)
\prod_{1\leq i<j\leq d}(j^2-i^2)\ne0. \tag{20}
\]

The witness need not lie in \(\mathcal R\); it establishes a polynomial identity on the whole parameter space. By (19), each \(D_T\) is a finite product of nonzero polynomials, and hence is a nonzero polynomial.

For completeness, a nonzero polynomial has a Lebesgue-null zero set. Induct on the number of variables. The one-variable assertion follows from finiteness of roots. For more variables, expand in the last variable. The set where every coefficient vanishes is contained in the zero set of one nonzero coefficient, and is null by induction. Outside that exceptional set, each fiber has finitely many roots. Fubini on bounded boxes proves the assertion. A countable union over \(T\) remains null. Combining this with (3) proves (4), without any invertibility assumption on the gradient-descent map.

### 5. Positivity and an eventual geometric rate

The other exceptional sets used here are initial augmented rank deficiency and a finite occurrence of \(h_t=1\). They too are polynomial zero sets. A square minor of \(Z_0\) is a nonzero polynomial when \(m\geq d+1\). For fixed \(t\), the polynomial \(h_t-1\) equals \(-1\) at \(Z_0=0\), so is nonzero. Thus outside a null set, \(Z_0\) has full column rank, \(h_t\ne1\) for all finite \(t\), and all \(D_t\ne0\).

Define

\[
K(v)=\begin{pmatrix}0&v^T\\v&0\end{pmatrix},\qquad G_t=Z_t^TZ_t.
\]

Then \(Z_{t+1}=Z_t(I-K(v_t))\). The eigenvalues of \(K(v)\) are \(\|v\|,-\|v\|\), and \(d-1\) zeros. Consequently

\[
\det G_{t+1}=\det G_t(1-h_t)^2. \tag{21}
\]

Choose \(T_0\) with \(h_t\leq1/2\) for all \(t\geq T_0\). Every determinant before \(T_0\) is positive, and

\[
\det G_t\geq\det G_{T_0}
\exp\left[-4\sum_{j=T_0}^\infty h_j\right]>0
\qquad(t\geq T_0). \tag{22}
\]

Taking the minimum of this bound and the finitely many earlier determinants gives a uniform bound \(D>0\). By (9), every eigenvalue of \(G_t\) is at most \(M\). Therefore \(G_t\succeq\mu I\), with \(\mu=D/M^d>0\), since \(\det G_t\leq\lambda_{\min}(G_t)M^d\). Principal submatrices give \(q_t\geq\mu\), \(C_t\succeq\mu I\), and hence \(H_\infty\succeq2\mu I\).

Equation (4) gives \(S_\infty<2\) outside the cyclicity exceptions. Choose

\[
\kappa=\tfrac12\min\{\lambda_{\min}(H_\infty),
2-S_\infty,1\}>0.
\]

Since \(H_t\to H_\infty\) and \(h_t\to0\), there is a finite \(T_1\) such that
\(\kappa I\preceq H_t\preceq(2-\kappa)I\) and \(h_t\leq\kappa/2\) for every \(t\geq T_1\). Equation (6) then implies

\[
\|v_{t+1}\|\leq(1-\kappa/2)\|v_t\|. \tag{23}
\]

Moreover, by (1),

\[
\|Z_{t+1}-Z_t\|_F^2
=v_t^TC_tv_t+q_th_t\leq M\|v_t\|^2. \tag{24}
\]

The geometric series in (23) makes the parameter increments summable. If \(\rho=1-\kappa/2<1\), their tail is bounded by

\[
\|Z_t-Z_\infty\|_F
\leq \frac{\sqrt M\,\|v_{T_1}\|}{1-\rho}\rho^{t-T_1}
\qquad(t\geq T_1). \tag{25}
\]

Continuity gives \(U_\infty^TA_\infty=0\); this is a global minimizer. Passing to the limit in \(G_t\succeq\mu I\) proves full column rank at the endpoint.

At a zero-residual point, the scaled loss Hessian is \(J^TJ\), where
\(J(\dot A,\dot U)=U^T\dot A+\dot U^TA\). Direct composition gives \(JJ^T=C+qI\). The positive eigenvalues of \(J^TJ\) and \(JJ^T\) agree: multiplication by \(J^T\) or \(J\) sends a positive-eigenvalue eigenvector to a nonzero eigenvector with the same eigenvalue. Thus its top eigenvalue is \(S_\infty\). The original Hessian is \(\eta^{-1}\) times this Hessian. This proves (5) and the sharpness assertion.

## Consequence for a fixed nonzero target

Fix a starting point in \(\mathcal R\) outside the preceding null set, and let \(z_*=(A_*,U_*)\) be its zero-target endpoint. Write \(S_*=q_*+\lambda_{\max}(C_*)<2\). For every fixed \(b\), the original initialization \((a_0,W_0)=\eta^{-1/2}(A_0,U_0)\) converges to a global minimizer for all sufficiently small \(\eta>0\), and its endpoint satisfies

\[
\eta\lambda_{\max}(\nabla^2L_b(a_\infty,W_\infty))
\leq (2+S_*)/2<2. \tag{26}
\]

Here the threshold for \(\eta\) can depend on the initial point and on \(b\).

To prove this, put \(y=\eta b\), \(v=U^TA\), and \(r=v-y\). The exact scaled update is \(A^+=A-Ur\), \(U^+=U-Ar^T\), and direct multiplication gives

\[
r^+=[I-H+(v^Tr)I]r. \tag{27}
\]

Since the eigenvalues of \(H(z_*)\) lie strictly between 0 and 2, choose \(k>0\) and a closed ball \(\|z-z_*\|\leq R\) on which

\[
kI\preceq H(z)\preceq(2-k)I,\quad
q+\lambda_{\max}(C)\leq(2+S_*)/2,\quad \|z\|\leq B.
\]

Such a ball exists by continuity, after first choosing \(0<k<\min\{\lambda_{\min}(H(z_*)),2-S_*,1\}\). Choose \(e>0\) with \((e+1)e\leq k/2\) and \(2Be/k\leq R/4\).
If \(\|y\|\leq1\), \(\|z-z_*\|\leq R/4\), and \(\|r\|\leq e\), then while the iterates remain in this ball, \(\|v\|\leq e+1\) and (27) gives \(\|r^+\|\leq(1-k/2)\|r\|\). Each parameter step has norm at most \(B\|r\|\). The sum of these bounds is at most \(2Be/k\leq R/4\). Induction therefore keeps every iterate within \(R/2\) of \(z_*\), makes the residual decrease geometrically, and proves parameter convergence to zero residual. This justifies the assumed ball condition at every finite step.

The zero-target trajectory reaches \(\|z_T(0)-z_*\|<R/8\) and \(\|v_T(0)\|<e/4\) at a finite time \(T\). Its finite iterates are continuous functions of \(y\). For all sufficiently small \(\|y\|\), the perturbed point at time \(T\) has \(\|z_T(y)-z_*\|\leq R/4\), \(\|r_T(y)\|\leq e\), and \(\|y\|\leq1\). The local argument applies. At zero residual the original Hessian again has output Gram \(\eta^{-1}(C+qI)\), proving (26).

## Gaussian endpoint probabilities

Let the scaled entries of \(Z_0\) be independent \(N(0,\tau^2)\), with fixed \(\tau>0\). Equivalently the original entries have law \(N(0,\tau^2/\eta)\). The rectangle \(\mathcal R\) has positive probability because it contains a neighborhood of zero. For zero target, at every \(\eta>0\), almost surely conditional on \(\mathcal R\) the endpoint exists and

\[
\mathbb P\{\eta\lambda_{\max}(\nabla^2L_0(a_\infty,W_\infty))\geq2
\mid\mathcal R\}=0. \tag{28}
\]

In particular a positive-probability endpoint atom at the critical value is excluded, not merely an atom above it.

More generally, fix any \(b\) and any deterministic \(w(\eta)\geq0\) with \(w(\eta)\to0\). Let \(E_\eta\) be convergence in parameter space to a global minimizer with
\(|\eta\lambda_{\max}(\nabla^2L_b)-2|\leq w(\eta)\). Couple all learning rates by the same scaled Gaussian draw. For almost every draw in \(\mathcal R\), (26) gives a fixed positive gap below 2 for all sufficiently small \(\eta\). Thus \(\mathbf1_{E_\eta\cap\mathcal R}\to0\) pointwise almost surely. Bounded convergence along every sequence \(\eta\downarrow0\) yields

\[
\mathbb P(E_\eta\cap\mathcal R)\longrightarrow0,\qquad
\limsup_{\eta\downarrow0}\mathbb P(E_\eta)
\leq\mathbb P(\mathcal R^c)
=\mathbb P\{q_0\geq2\text{ or }\lambda_{\max}(C_0)\geq2\}. \tag{29}
\]

The convergence and endpoint events are measurable: convergence is a countable Cauchy condition on continuous finite iterates, and the loss and Hessian are continuous at the resulting limit. The absolute endpoint window \(|\lambda_{\max}-2/\eta|\leq\varepsilon(\eta)\), with \(\varepsilon(\eta)\to0\), is covered by \(w(\eta)=\eta\varepsilon(\eta)\). No quantitative rate for (29) is asserted.

## Exceptional endpoints really occur

The round-4 exact one-step landing has \(q_0=c_0=17/9\), \(v_0=(5/3,0,\ldots,0)\), and endpoint sharpness \(256/81>2\). It has \(D_1=0\). It is consistent with (3).

There are also supercritical endpoints without a finite zero residual. Take \(d\geq2\), \(m\geq d+1\),

\[
A_0=e_1,\quad U_{0,1}=\tfrac14(e_1+e_2),\quad
U_{0,2}=\tfrac65e_3,\quad
U_{0,j}=\tfrac1{10}e_{j+1}\ (3\leq j\leq d).
\]

This has full augmented rank, \(q_0=1\), \(c_0=36/25<2\), and only the first residual coordinate is nonzero. The other columns remain fixed and orthogonal to the active two-dimensional plane. Directly from (1), at time 1 the active variables have

\[
q_1=113/128,\qquad c_{1,\mathrm{active}}=1/16,\qquad
v_{1,\mathrm{active}}=-1/64.
\]

The active sum \(q_1+c_{1,\mathrm{active}}=121/128<1\) decreases thereafter. Its scalar residual multiplier \(1-q_t-c_{t,\mathrm{active}}+h_t\) is strictly positive for every \(t\geq1\), so no later residual is zero. Monotonicity of the active \(c_t\) gives

\[
\sum_{t\geq1}h_t
\leq\frac{c_{1,\mathrm{active}}}{2-q_1}=\frac8{143}.
\]

Since \(q_{t+1}\geq q_t-2h_t\),

\[
q_\infty\geq\frac{113}{128}-\frac{16}{143}
=\frac{14111}{18304},\qquad
S_\infty\geq\frac{14111}{18304}+\frac{36}{25}>2. \tag{30}
\]

The spectator column is invisible to the residual from the start, so \(D_0=0\). The augmented determinant stays positive: initially \(h_0=1/16\), and the active sum bound gives \(h_t<1\) thereafter; (8), (21), and (22) apply. The positive lower output-spectrum bound in the active block, together with its upper bound \(121/128<2\), gives geometric residual and parameter convergence by the argument of (23)--(25). Thus (30) is an actual limiting endpoint. This example shows why deterministic strict subcriticality requires exclusion of exact invisible modes, not just exclusion of finite-time landing. It embeds in \(m=16,d=8\).

## Scope

The new conclusion is strict subcriticality, including exclusion of critical equality, almost surely in the whole rectangle (2). It also gives an eventual geometric rate and extends the earlier small-target persistence argument to almost every point of that rectangle. The complement of the rectangle remains unclassified. There is no theorem here about nonlinear activations, random finite Gaussian sample covariances, or a sustained edge residence phase. No initialization-uniform spectral gap, convergence rate, or finite-\(\eta\) probability bound for nonzero targets is proved. These results do not settle the original network edge-of-stability problem.
