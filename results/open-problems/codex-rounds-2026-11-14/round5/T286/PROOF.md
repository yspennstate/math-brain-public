# Likelihood-weighted cubic integration by parts

The hidden activation throughout is
\[
 \varphi(z)=(z^3-3z)/\sqrt6,\qquad
 F_W(x)=k^{-1/2}\sum_{i=1}^k\varphi(w_i\cdot x/\sqrt d).
\]
The prior \(P\) has independent standard Gaussian weight coordinates. Inputs have law \(N(0,I_d)\), and all readouts equal one. This result concerns a restricted output channel, with a finite label set \(\mathcal Y\) of cardinality \(q\). Write its probabilities as \(p_y(z)\), and assume
\[
 \sum_y p_y(z)=1,\quad p_y(z)\geq c>0,\quad
 p_y\in C^2(\mathbb R),\quad
 |p_y'|\leq L_1,\quad |p_y''|\leq L_2.
 \tag{1}
\]
Put
\[
 L=\log(1/c),\qquad B=q(L_2L+L_1^2/c).
 \tag{2}
\]
The channel and the constants \(q,c,L_1,L_2\) are fixed as the dimensions grow. All expectations below are over the stated matched model; logarithms are natural.

## 1. Cavity model and statement

Let \(D\) be arbitrary random cavity data and \(Q_D\) a random probability measure on weights satisfying the averaged marginal identity
\[
 \mathbb E_D Q_D=P. \tag{3}
\]
Conditionally on \(D\), draw \(W^0\sim Q_D\). Let \(X,V,U_0\) be independent standard Gaussians, of dimensions \(d,1,1\), independent of \((D,W^0)\). For a fixed \(0<t<1\), set
\[
 a=\sqrt{1-t},\quad b=\sqrt{G(t)},\quad e=\sqrt{t-G(t)},
 \quad 0<G(t)<t,
\]
where \(G\) is differentiable at \(t\). Define
\[
 S_0=aF_{W^0}(X)+bV+eU_0,
 \quad S(W,u)=aF_W(X)+bV+eu,
\]
\[
 Z_y=\int Q_D(dW)\,Du\,p_y(S(W,u)),\qquad
 \dot S_0=a'F_{W^0}(X)+b'V+e'U_0,
 \tag{4}
\]
where \(Du\) denotes standard Gaussian measure. Thus \(c\leq Z_y\leq1\).

For \(u_i=w_i/\sqrt d\), put
\[
 T(W)=k^{-1/2}\sum_i u_i^{\otimes3},\qquad
 v(W)=\sqrt{3/(2k)}\sum_i(\|u_i\|^2-1)u_i,
\]
\[
 C(W,W')=\langle T(W),T(W')\rangle,
 \quad K(W,W')=C(W,W')+v(W)\cdot v(W').
 \tag{5}
\]
Here \(K\) is the actual conditional input covariance. Use subscripts \(00\) and \(0W\) for \((W^0,W^0)\) and \((W^0,W)\).

Define
\[
 I=\mathbb E\sum_y p_y'(S_0)\dot S_0\log Z_y,
 \tag{6}
\]
and, for \(H=K\) or \(C\),
\[
 J_H={1\over2}\mathbb E\sum_y
 (1-H_{00})p_y''(S_0)\log Z_y
 +{1\over2}\mathbb E\sum_y p_y'(S_0)
 {\displaystyle\int Q_D(dW)Du\,[G'(t)-H_{0W}]p_y'(S(W,u))
  \over Z_y}.
 \tag{7}
\]

**Theorem.** With \(\varepsilon,\ell\) defined in Section 2,
\[
 |I-J_K|\leq {B\varepsilon\over2},\qquad
 |I-J_C|\leq {B(\varepsilon+\ell)\over2}.
 \tag{8}
\]
The constants are independent of \(D,Q_D,t,G(t),G'(t)\). If \(k/d\to\gamma\in(0,\infty)\), then \(\varepsilon=O(d^{-1/2})\) and \(\ell=O(d^{-1})\). Uniformity concerns the error in (8), even though the separate terms of (6) can have singular coefficients near an interpolation endpoint. No derivative at an endpoint is asserted. Cases with an identically absent Gaussian offset follow by omitting that offset and its derivative.

In a matched Bayesian model, deleting observation \(\mu\), including its input and its shared scalar \(V_\mu\), gives (3) by the tower property. The unused input \(X_\mu\), shared scalar \(V_\mu\), and latent scalar \(U_\mu\) are independent of these cavity data. Gaussian side observations about the teacher weights may remain in \(D\). Thus (8) applies to the observation contribution in the interpolation of Appendix B.6 cited in Section 7.

## 2. The finite-replica Stein bound

Here are the precise constants and the input identity used below. Set
\[
 M_j=\prod_{h=0}^{j-1}(1+2h/d),\quad
 \rho=M_3-2M_2+M_1,\quad
 \eta=M_6-4M_5+6M_4-4M_3+M_2,
\]
\[
 \delta={M_6\over k}+{k-1\over k}M_3^2
 \left({1\over d}+{3\over d(d+2)}+{15\over d(d+2)(d+4)}\right),
\]
\[
 \beta={9\over4}\left[{\eta\over k}
       +{k-1\over k}(1+2/d)\rho^2\right],\quad
 \ell={3\over2}\rho={3\over d}+{12\over d^2},
\]
\[
 \varepsilon^2=6\delta+
 2\left[2\sqrt\delta+{4\over\sqrt6}(\delta\beta)^{1/4}\right]^2.
 \tag{9}
\]

Suppose \(W^0,\ldots,W^R\) have any joint law with individual marginals \(P\), independently of \(X\). Auxiliary variables may depend on all these weights but are jointly independent of \(X\). There is a matrix \(\Gamma_{ij}(X)\) such that for any weight- and auxiliary-dependent \(C^1\) function \(h\) with uniformly bounded first derivatives,
\[
 \mathbb E_X F_{W^i}(X)h(F(X))
  =\sum_j\mathbb E_X\Gamma_{ij}(X)\partial_jh(F(X)),
 \quad
 \mathbb E_X\Gamma_{ij}=K_{ij},\quad
 \mathbb E|\Gamma_{ij}-K_{ij}|^2\leq\varepsilon^2.
 \tag{10}
\]
In particular, if \(|\partial_jh|\leq A_j\), the error in replacing every \(\Gamma_{ij}\) by \(K_{ij}\), after averaging all variables, is at most \(\varepsilon\sum_j A_j\). This last assertion follows term by term from Cauchy--Schwarz; it has no dependence on the number of replicas except through the displayed sum.

For completeness, the calculation underlying (10) follows. Write \(I_p\) for the Wick polynomial of a symmetric tensor, normalized by
\(\mathbb E I_p(A)I_r(B)=\mathbf1_{p=r}p!\langle A,B\rangle\).
The network has decomposition
\[
 F_{W^i}=I_3(T_i)/\sqrt6+v_i\cdot X.
\]
Let \(H_i(X)_j=I_2((T_i)_{j,\cdot,\cdot})\). For the Gaussian generator \(\mathcal L=\Delta-X\cdot\nabla\), its inverse on the cubic and linear terms multiplies by \(-1/3\) and \(-1\). Ordinary Gaussian integration by parts gives
\[
 \Gamma_{ij}=(H_i/\sqrt6+v_i)\cdot(3H_j/\sqrt6+v_j).
 \tag{11}
\]
Indeed \(\mathbb E(-\mathcal L f)g=\mathbb E\nabla f\cdot\nabla g\); apply this with \(f=-\mathcal L^{-1}F_{W^i}\), \(g=h(F)\), and use the chain rule. Bounded derivatives and polynomial Gaussian moments justify a cutoff approximation.

Multiplying two order-two Wick polynomials gives a fourth-order term, four single contractions and two complete contractions. Consequently
\[
 \Gamma_{ij}-K_{ij}
 ={1\over2}I_4(\operatorname{sym}(T_i\otimes_1T_j))
 +I_2\left(2\operatorname{sym}(T_i\otimes_2T_j)
  +{T_i\otimes_1v_j\over\sqrt6}
  +\sqrt{3/2}\,T_j\otimes_1v_i\right).
 \tag{12}
\]
For a symmetric cubic tensor \(T\), put \(D(T)=\|T\otimes_2T\|^2\). Flattening it as a matrix with one row index and two column indices shows
\(\|T\otimes_1T\|^2=\|T\otimes_2T\|^2\).
Summing indices and applying Cauchy--Schwarz gives, for \(r=1,2\),
\[
 \|T\otimes_rS\|^2\leq\sqrt{D(T)D(S)},\qquad
 \|T\otimes_1v\|^2\leq\sqrt{D(T)}\|v\|^2.
 \tag{13}
\]
For example the first left side is the inner product of the self-contractions of complementary orders; the second is \(v^T(T\otimes_2T)v\), bounded by the matrix Frobenius norm times \(\|v\|^2\).

The prior moments are
\[
 \mathbb E D(T)=\delta,\quad \mathbb E\|v\|^2=\ell,
 \quad \mathbb E\|v\|^4=\beta. \tag{14}
\]
To verify the first formula, write \(q_{ij}=u_i\cdot u_j\). Its unnormalized sum is
\(\sum_{i,j,l,h}q_{ij}^2q_{lh}^2q_{il}q_{jh}\).
Row sign symmetry leaves only the all-equal pattern and three pair partitions. The first contributes \(kM_6\). Each pair partition has \(k(k-1)\) terms; their expectations are respectively \(M_3^2/d\), \(3M_3^2/[d(d+2)]\), and \(15M_3^2/[d(d+2)(d+4)]\). These follow by writing each Gaussian row as its independent radius and uniform direction; the even direction moments are \(1/d,3/[d(d+2)],15/[d(d+2)(d+4)]\). Divide by \(k^2\).

For the other formulas, the independent centered vectors \(z_i=(\|u_i\|^2-1)u_i\) satisfy \(\mathbb E\|z_i\|^2=\rho\), \(\mathbb E\|z_i\|^4=\eta\) and \(\mathbb E z_iz_i^T=(\rho/d)I\). Expanding the squared norm of their sum twice gives
\(\mathbb E\|\sum_i z_i\|^4=k\eta+k(k-1)(1+2/d)\rho^2\).
Multiplying by \((3/(2k))^2\) gives \(\beta\); the second moment gives \(\ell\).

Equations (13)--(14) imply, without joint independence,
\[
 \mathbb E\|T_i\otimes_rT_j\|^2\leq\delta,
 \quad \mathbb E\|T_i\otimes_1v_j\|^2\leq\sqrt{\delta\beta}.
\]
Orthogonality of the two chaoses in (12) bounds their squared norms by \(6\delta\) and
\(2[2\sqrt\delta+(4/\sqrt6)(\delta\beta)^{1/4}]^2\), respectively. This proves (9)--(10). It also proves \(\mathbb E|K_{ij}-C_{ij}|\leq\ell\).
Finally \(d\delta\to1+1/\gamma\), \(d^2\beta\to9\), and
\(\sqrt d\,\varepsilon\to\sqrt{14(1+1/\gamma)}\), by expanding the finite products for \(M_j\).

## 3. The normalized one-sample identity

First prove, for arbitrary real \(a,b,e\),
\[
 \begin{split}
 A_F&:=\mathbb E\sum_y F_{W^0}(X)p_y'(S_0)\log Z_y,\\
 A_F&=a\,\mathbb E\sum_y K_{00}p_y''(S_0)\log Z_y
  +a\,\mathbb E\sum_y p_y'(S_0)
     {\int Q_D(dW)Du\,K_{0W}p_y'(S(W,u))\over Z_y}
  +r,\quad |r|\leq |a|B\varepsilon.
 \end{split}
 \tag{15}
\]

Draw \(R\) additional weights \(W^1,\ldots,W^R\) independently from \(Q_D\) conditional on \(D\), and independent standard \(U_1,\ldots,U_R\). Set
\[
 A_{R,y}(z)={1\over R}\sum_{j=1}^R p_y(az_j+bV+eU_j),
 \quad h_R(z)=\sum_y p_y'(az_0+bV+eU_0)\log A_{R,y}(z).
\]
The teacher is excluded from the empirical denominator. Since \(c\leq A_{R,y}\leq1\),
\[
 |\partial_0h_R|\leq |a|qL_2L,
 \qquad |\partial_jh_R|\leq {|a|qL_1^2\over Rc}\quad(1\leq j\leq R).
 \tag{16}
\]
Their sum is at most \(|a|B\), uniformly in \(R\) and in all weights, data and Gaussian offsets. Also \(|h_R|\leq qL_1L\). Each weight has marginal \(P\) by (3); all are jointly independent of \(X\). Thus (10) applies, giving
\[
 \begin{split}
 \mathbb E F_0h_R(F)
 &=a\,\mathbb E\sum_y K_{00}p_y''(S_0)\log A_{R,y}(F)\\
 &\quad+a\,\mathbb E\sum_y p_y'(S_0)
 {R^{-1}\sum_{j=1}^R K_{0j}p_y'(S_j)\over A_{R,y}(F)}+r_R,
 \quad |r_R|\leq |a|B\varepsilon.
 \end{split}
 \tag{17}
\]

Condition on \(D,W^0,U_0,X,V\). The replica pairs \((W^j,U_j)\) are iid under this conditioning. Their denominators converge almost surely to \(Z_y\). Their numerators converge in \(L^1\) to the integral in (15). Here is the integrability needed for that assertion and for averaging the conditional limit. The kernel \(K\) is positive semidefinite, so
\[
 |K_{0j}|\leq\sqrt{K_{00}K_{jj}}\leq(K_{00}+K_{jj})/2,
 \quad \mathbb E|K_{0j}|\leq\mathbb E_P K(W,W)=M_3+\ell<\infty.
 \tag{18}
\]
For the numerator law of large numbers, truncate \(K_{0j}p_y'(S_j)\) at a deterministic level. The bounded part has sample-mean \(L^1\) error tending to zero. The expectation of the discarded part is independent of \(R\) and tends to zero with the truncation level by (18). This proves unconditional \(L^1\) convergence as well. Division by \(A_{R,y}\geq c\) preserves it: for the limiting numerator \(N_y\), the remaining error is bounded by
\(|N_y||1/A_{R,y}-1/Z_y|\), which tends to zero by dominated convergence with bound \(2|N_y|/c\).

The other terms in (17) converge by dominated convergence: the logarithms are bounded by \(L\), \(K_{00}\) is integrable, and \(F_0\) has finite second moment \(\mathbb E K_{00}\). Taking \(R\to\infty\) proves (15). This passage controls the whole random normalization; it does not fix a replica number depending on \(d\).

## 4. Gaussian offsets and the interpolation coefficient

Write
\[
 A_2=\mathbb E\sum_y p_y''(S_0)\log Z_y,
 \quad A_{11}=\mathbb E\sum_y p_y'(S_0)
 {\int Q_D(dW)Du\,p_y'(S(W,u))\over Z_y}.
\]
Gaussian integration by parts in \(U_0\) gives
\[
 \mathbb E\sum_y U_0p_y'(S_0)\log Z_y=eA_2, \tag{19}
\]
because \(Z_y\) integrates a separate latent \(u\) and is independent of \(U_0\). In \(V\), both the teacher factor and the normalization depend on the same Gaussian, so
\[
 \mathbb E\sum_y Vp_y'(S_0)\log Z_y=b(A_2+A_{11}).
 \tag{20}
\]
These derivatives are bounded by (1) and \(Z_y\geq c\); differentiation under the \(Q_D\) and \(Du\) integrals and Gaussian integration by parts are therefore justified.

Multiply (15), (19), (20) by \(a',e',b'\), respectively. Since
\[
 aa'=-1/2,\quad bb'=G'/2,\quad ee'=(1-G')/2,
\]
the self coefficients sum to \((1-K_{00})/2\), and the replica coefficients sum to \((G'-K_{0W})/2\). The error obeys
\(|a'r|\leq|a'a|B\varepsilon=B\varepsilon/2\).
This proves the first inequality of (8). In particular the factor \(1/\sqrt{1-t}\) has canceled before estimating the error.

By (14), (18) and Cauchy--Schwarz,
\[
 \mathbb E|K_{00}-C_{00}|=\ell,\qquad
 \mathbb E\int Q_D(dW)Du\,|K_{0W}-C_{0W}|\leq\ell.
\]
In the two terms of (7), respectively use \(|p_y''\log Z_y|\leq L_2L\) and \(|p_y'(S_0)p_y'(S(W,u))/Z_y|\leq L_1^2/c\). It follows that \(|J_K-J_C|\leq B\ell/2\), proving the second inequality of (8).

## 5. Relation to the full likelihood and its logarithm

In a matched model let \(Z_-\) be the partition function with observation \(\mu\) removed, and suppose its posterior on weights is \(Q_D\). Other latent variables in that posterior may be integrated out. Restoring observation \(\mu\) gives exactly
\[
 Z_{\rm full}(y)=Z_- Z_y. \tag{21}
\]
For the contribution proportional to the score \(\partial_s\log p_y(S_0)\), averaging its teacher label multiplies this score by \(p_y(S_0)\), leaving \(p_y'(S_0)\). The cavity part of the logarithm disappears pointwise:
\[
 \sum_y p_y'(S_0)\dot S_0\log Z_-=0. \tag{22}
\]
The same cancellation holds with \(p_y''(S_0)\) and a label-independent multiplier, since \(\sum_y p_y''=0\). Thus (6) is exactly the full observation contribution with \(\log Z_{\rm full}\), provided the full model's terms are integrable. For a finite matched data set under (1) and Gaussian side observations that integrability holds. Alternatively the canceled expression (6) is defined directly and always integrable.

Let \(\langle\cdot\rangle_y\) denote the full posterior obtained by tilting \(Q_D(dW)Du\) by \(p_y(S(W,u))/Z_y\). Put \(u_y'=p_y'/p_y\). Label averaging gives the exact equality
\[
 \mathbb E_Y\langle u_Y'(S_0)u_Y'(S(W,u))H_{0W}\rangle_Y
 =\mathbb E\sum_y p_y'(S_0)
 {\int Q_D(dW)Du\,H_{0W}p_y'(S(W,u))\over Z_y}.
 \tag{23}
\]
The self term is similarly the label average of
\((1-H_{00})[p_Y''(S_0)/p_Y(S_0)]\log Z_{\rm full}(Y)\).
Consequently (8) is a quantitative version of the likelihood-weighted passage (158) to (161), with \(g(1)=1\), for this hidden activation and output-channel class. It is an identity estimate under the original model; a claim that the complete posterior field is Gaussian is unnecessary.

For \(n\) observations, average these estimates or integrate them over \(0<t<1\). The error is at most \(B(\varepsilon+\ell)/2\) with normalization \(1/n\), and at most \((n/d^2)B(\varepsilon+\ell)/2\) with normalization \(1/d^2\). This uses only the triangle inequality. No independence across omitted observations or interpolation times is assumed.

## 6. Self term and an explicit channel

The self term in \(J_C\) can also be discarded with a smaller error. Row sign symmetry and Gaussian moments give
\[
 A(d,k):=\mathbb E(C_{00}-1)^2
 =(M_3-1)^2+{M_6-M_3^2\over k}
       +{30(k-1)M_3\over kd^3}. \tag{24}
\]
Indeed \(C_{00}=k^{-1}\sum_i\|u_i\|^6+(2/k)\sum_{i<j}(u_i\cdot u_j)^3\). Different off-diagonal edges and their covariances with the diagonal part vanish by changing one row's sign. An individual edge has sixth moment \(15M_3/d^3\); the diagonal variance is \((M_6-M_3^2)/k\). These observations prove (24). Equation (3) transfers it to the teacher marginal here. Hence
\[
 \left|{1\over2}\mathbb E\sum_y
 (1-C_{00})p_y''(S_0)\log Z_y\right|
 \leq {qL_2L\over2}\sqrt{A(d,k)}=O(d^{-1}). \tag{25}
\]
In particular \(d^2A(d,k)\to36+18/\gamma\). The unbounded full \(\log Z\) does not multiply this estimate, because its cavity part has already canceled.

One output channel satisfying (1) is
\[
 p_{\pm}(z)={1\pm\lambda\tanh z\over2},\qquad 0<\lambda<1.
 \tag{26}
\]
Here \(c=(1-\lambda)/2\), \(L_1=\lambda/2\), and \(L_2=2\lambda/(3\sqrt3)\). To check the last constant, set \(h=\tanh z\); then \(|p_y''(z)|=\lambda|h|(1-h^2)\), maximized at \(|h|=1/\sqrt3\). For \(\lambda=1/2\), (8) yields
\[
 |I-J_C|\leq
 \left({\log4\over3\sqrt3}+{1\over4}\right)(\varepsilon+\ell).
 \tag{27}
\]
The appearance of tanh in (26) describes the output channel; the hidden activation is still cubic.

## 7. Scope and reference

Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore and Rudy Skerk, [*Statistical physics of deep learning: Optimal learning of a multi-layer perceptron near interpolation*, arXiv:2510.24616v5](https://arxiv.org/html/2510.24616v5#A2.SS6), equations (158)--(166), give the interpolation and its remaining assumptions. The finite-replica bound in Section 2 is the preceding session's cubic lemma, rederived here to specify exactly what is used. The new part is the normalized cavity passage (15)--(23) and its uniform error estimate.

This does not prove distinct-replica concentration (166), the existence and appropriate choice of the adaptive interpolation, a variational Bayes-error formula, or any optimization theorem. In particular \(C_{0W}\) in (7) remains a full permutation-invariant cubic kernel, not a trace overlap. The result does not cover hidden ReLU or hidden tanh. A standard Gaussian regression channel, or an unmodified logistic channel with arbitrarily small probabilities, does not satisfy (1). The constants diverge as \(c\downarrow0\); that limit has not been justified. No literature novelty is claimed for the cavity or Stein methods.
