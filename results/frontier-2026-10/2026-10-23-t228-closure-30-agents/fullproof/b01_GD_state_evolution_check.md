# Explicit finite-time state evolution for the original Gaussian RF logistic GD

Independent derivation and normalization audit — 2026-10-23 (America/New_York).

**Conclusion.** The finite-time recursion below describes ordinary full-batch output-weight gradient descent. The AMP memory coefficients are added and subtracted in an auxiliary representation and cancel from the physical update. For the spectral law proved in B03, every rectangular free cumulant has a closed expression, so the recursion uses only finite triangular matrix inverses and Gaussian expectations. Its covariance matrices are positive definite at every fixed time when the step size is positive. No added algorithmic noise or change from GD to AMP is required. The first-step test signal and variance agree exactly with the separately audited formulas.

This report relies on B03's Proposition 4 (the teacher-spike decomposition) and Theorem 5 (the generalized-invariance and spectral hypotheses), whose statements are in `fullproof/b03_gaussian_dynamics.md`. Those matrix inputs are being independently audited by B05/B06. The statements here concern each fixed finite horizon; they do not exchange the limits in dimension and training time.

**Finite-horizon theorem.** In the Gaussian tanh model of Section 1, for each fixed integer $T\ge1$, each fixed $c>0$, and every $\alpha,\gamma>0$ and finite $\beta\ge0$, the actual GD sequence (1) has the deterministic state evolution (11)–(16). In probability, its training empirical path distribution converges in $W_2$ to the scalar training law (12) conditioned on $M=1$, and
\[
(b^s)^\top b^t\longrightarrow(\Gamma_T)_{st}\qquad(1\le s,t\le T).
\]
Conditional on the training data and random features, the joint law of a fresh teacher coordinate and fresh score path converges weakly, with convergence of all second moments, to
\[
\left(Z_\star,s q_1Z_\star+G_1,\ldots,s q_TZ_\star+G_T\right),
\qquad G_{1:T}\sim N(0,\Sigma_T),\quad G_{1:T}\perp Z_\star.
\]
Thus the realized test covariances converge to (18). Every $\Omega_t$ and $\Sigma_t$ in the recursion is positive definite. Sections 2–8 prove this theorem from the stated B03 matrix results and the inspected WZF theorem.

## 1. Model, dimensions, and the physical update

Let $X_i\sim N(0,I_d)$, let $\theta$ be a deterministic unit vector, and let
\[
Y_i\mid X_i\sim\operatorname{Bernoulli}(\sigma(\beta\theta^\top X_i)),
\qquad \sigma(x)=(1+e^{-x})^{-1},\quad 0\le\beta<\infty.
\]
There are $n$ training examples and $m$ independent random features $W_j\sim N(0,I_d/d)$, with
\[
n/d\to\alpha>0,\qquad m/d\to\gamma>0,\qquad
H_{ij}=\tanh(W_j^\top X_i).
\]
Write
\[
a=\mathbb E[G\tanh G],\qquad v=\mathbb E[\tanh^2G],\qquad
\nu=v-a^2>0,\quad G\sim N(0,1).
\]
Strict positivity follows because $\tanh G$ is not a scalar multiple of $G$ in Gaussian $L^2$.

In B03's normalization, $w^t=\sqrt m\,b^t$, $A=H/\sqrt m$, and a mean-loss GD step of size $cd$ gives
\[
w^0=0,\qquad w^{t+1}=w^t+\lambda_d A^\top r^t,
\quad r^t=M\odot(Y-\sigma(Aw^t)),\quad \lambda_d=cd/n\to\lambda=c/\alpha.
\tag{1}
\]
Here a proportional independent query block is appended to the rows, and $M_i=1$ on training rows and $M_i=0$ on query rows. If the total number of rows is $N$, set
\[
N/d\to\delta>\alpha,\qquad r=N/m\to\delta/\gamma,
\qquad p=n/N\to\alpha/\delta.
\tag{2}
\]
The common choice $N=2n$ gives $p=1/2$, $\delta=2\alpha$. No result depends on that choice.

Rotate $\theta$ to the first coordinate. Let $z_i=\theta^\top X_i$ and $h_j=\sqrt d\,\theta^\top W_j$. Then $z_i,h_j$ are standard normal, and B03's decomposition is
\[
A=A_0+\frac{s_d}{m}zh^\top+E_d,
\quad s_d=a\sqrt{m/d}\to s=a\sqrt\gamma,
\quad \|E_d\|_{\rm op}=o_{\mathbb P}(1).
\tag{3}
\]
The perpendicular matrix $A_0$ is independent of $(z,Y,M,h)$. For the exact spike matrix $A_0+s_dzh^\top/m$, the physical GD update is
\[
Q_t=Q_{t-1}+\lambda_d\left[A_0^\top R_t+s_d r_d\ell_t^{(d)}h\right],
\quad R_{t+1}=M\odot\left[Y-\sigma(A_0Q_t+s_dq_t^{(d)}z)\right],
\tag{4}
\]
where $Q_t=w^t$, $R_t=r^{t-1}$,
\[
q_t^{(d)}=m^{-1}h^\top Q_t,\qquad
\ell_t^{(d)}=N^{-1}z^\top R_t,\qquad r_d=N/m.
\]
In particular the column spike coefficient is $s r\ell_t$, not $s\ell_t$.

## 2. The RF rectangular cumulants have a closed form

Let $\mu_k$ be the limiting **row-normalized** moments
\[
\mu_k=\lim N^{-1}\operatorname{tr}(A_0A_0^\top)^k.
\]
The squared singular-value law is padded with zeros to $N$ values when necessary. B03's comparison Gaussian matrix has independent rows conditional on its feature covariance, whose limiting covariance law is
\[
\mathcal H=\mathcal L(\nu+a^2 L),\qquad L\sim\operatorname{MP}_{\gamma},
\quad \mathbb EL=1.
\]
Let $M(z)=\sum_{k\ge1}\mu_kz^k$ and $M_{\mathcal H}(z)=\sum_{k\ge1}(\int t^k\,d\mathcal H(t))z^k$. The spectral fixed point in B03, expanded at infinity, gives the formal-power-series identity
\[
rM(z)=M_{\mathcal H}\big(rz(1+M(z))\big).
\tag{5}
\]
For completeness, writing $m_F(-\zeta)$ for the feature-side Stieltjes transform and $e_\zeta$ for B03's auxiliary scalar, its fixed point implies
$r e_\zeta/(1+e_\zeta)=1-\zeta m_F(-\zeta)$.
Since the feature moment series is $rM$, substitution $z=-1/\zeta$ gives
$e_\zeta=-M/(1+M)$ and then (5).

The ordinary free $R$-transform of $\mathcal H$ is
\[
R_{\mathcal H}^{\rm ord}(u)=\nu+\frac{a^2}{1-a^2\gamma u}.
\]
Equivalently,
\[
M_{\mathcal H}(w)=w(1+M_{\mathcal H}(w))
\left[\nu+\frac{a^2}{1-a^2\gamma w(1+M_{\mathcal H}(w))}\right].
\]
Combine this identity with (5), and set $t=z(1+M)(1+rM)$. Since $r\gamma=\delta$, this yields
\[
M(z)=\nu t+\frac{a^2t}{1-a^2\delta t}.
\tag{6}
\]
Fan's rectangular moment/cumulant identity is $M(z)=R_{\rm rect}(z(1+M(z))(1+rM(z)))$. Therefore
\[
\boxed{R_{\rm rect}(t)=\nu t+\frac{a^2t}{1-a^2\delta t},\qquad
\kappa_2=v,\quad\kappa_{2k}=a^{2k}\delta^{k-1}\ (k\ge2).}
\tag{7}
\]
This is a formal-series identity; no convergence radius or small-step condition is needed. In particular
\[
\mu_1=v,\qquad
\mu_2=(1+r)v^2+\delta a^4
=v^2+r(v^2+a^4\gamma),\qquad \kappa_4=\delta a^4.
\tag{8}
\]

## 3. Exact finite-dimensional memory and covariance formulas

Use $R_t$ for the scalar row residual and $Q_t$ for the scalar column iterate. The centered row and column Gaussian fields will be $G_t$ and $Z_t$, respectively. Their covariance matrices are $\Sigma_t$ and $\Omega_t$. The teacher scalar is denoted $Z_\star$, and the independent column teacher coordinate is $H_\star$.

Define the $t\times t$ matrices
\[
\Delta_t=(\mathbb E[R_iR_j])_{i,j\le t},\quad
\Gamma_t=(\mathbb E[Q_iQ_j])_{i,j\le t},
\]
\[
(\Phi_t)_{ij}=\mathbb E\left[\frac{\partial R_i}{\partial G_j}\right]
\quad(j<i),\qquad
(\Psi_t)_{ij}=\mathbb E\left[\frac{\partial Q_i}{\partial Z_j}\right]
\quad(j\le i),
\tag{9}
\]
and put zero in the remaining entries. Thus $\Phi_t$ is strictly lower triangular and $\Psi_t$ is lower triangular. All derivatives hold the deterministic recursion coefficients fixed.

Our coefficient matrices $\mathsf A_t=(a_{ij})$ and $\mathsf B_t=(b_{ij})$ are **lower** triangular. They are the transposes of Fan's displayed upper-triangular matrices $A_t,B_t$. Set $h_0=a^2\delta$. Then the explicit formulas are
\[
\boxed{\begin{aligned}
\mathsf A_t&=\nu\Psi_t+a^2\Psi_t(I-h_0\Phi_t\Psi_t)^{-1},\\
\mathsf B_t&=r\nu\Phi_t+ra^2\Phi_t(I-h_0\Psi_t\Phi_t)^{-1},\\
\Sigma_t&=\nu\Gamma_t+a^2(I-h_0\Psi_t\Phi_t)^{-1}
\left[\Gamma_t+h_0\Psi_t\Delta_t\Psi_t^\top\right]
(I-h_0\Psi_t\Phi_t)^{-\top},\\
\Omega_t&=r\nu\Delta_t+ra^2(I-h_0\Phi_t\Psi_t)^{-1}
\left[\Delta_t+h_0\Phi_t\Gamma_t\Phi_t^\top\right]
(I-h_0\Phi_t\Psi_t)^{-\top}.
\end{aligned}}
\tag{10}
\]
Every inverse is a finite polynomial: $\Phi_t\Psi_t$ and $\Psi_t\Phi_t$ are strictly lower triangular, so $(I-h_0L)^{-1}=\sum_{j=0}^{t-1}h_0^jL^j$.

Here is an explicit check against the primary-source formulas. With $L=\Phi\Psi$ and $K=\Psi\Phi$, Fan's covariance coefficients, in our notation, are
\[
\Theta^{(j)}=\sum_{i=0}^jL^i\Delta(L^\top)^{j-i}
+\sum_{i=0}^{j-1}L^i\Phi\Gamma\Phi^\top(L^\top)^{j-1-i},
\]
\[
\Xi^{(j)}=\sum_{i=0}^jK^i\Gamma(K^\top)^{j-i}
+\sum_{i=0}^{j-1}K^i\Psi\Delta\Psi^\top(K^\top)^{j-1-i}.
\]
The second sums are empty for $j=0$. His prescriptions give
$\Sigma=\sum_{j\ge0}\kappa_{2j+2}\Xi^{(j)}$,
$\Omega=r\sum_{j\ge0}\kappa_{2j+2}\Theta^{(j)}$,
$\mathsf A=\sum_{j\ge0}\kappa_{2j+2}\Psi(\Phi\Psi)^j$, and
$\mathsf B=r\sum_{j\ge0}\kappa_{2j+2}\Phi(\Psi\Phi)^j$.
Inserting (7) and summing the two finite geometric series proves (10). In particular no additional factor of $r$ belongs inside either covariance bracket.

## 4. Causal recursion and its implementation without circular definitions

Let
\[
Z_\star,H_\star\sim N(0,1),\quad
Y\mid Z_\star\sim\operatorname{Bernoulli}(\sigma(\beta Z_\star)),
\quad M\sim\operatorname{Bernoulli}(p),
\]
with $M$ independent of $(Z_\star,Y)$ and $H_\star$ on the separate column probability space. Initialize
\[
R_1=M(Y-1/2),\qquad Q_0=0,\qquad q_0=0.
\]
For $t=1,2,\ldots$, carry out the following operations.

1. From the already defined row functions $R_{1:t}(G_{1:t-1},Z_\star,Y,M)$ and $\Sigma_{t-1}$, compute $\Delta_t$, $\Phi_t$, and $\ell_t=\mathbb E[Z_\star R_t]$.
2. Embed the previous $\Psi_{t-1},\Gamma_{t-1}$ in $t\times t$ matrices with zero last row/column. Compute $\mathsf B_t,\Omega_t$ from (10). Their values do not depend on the missing current column function: the last column of $\Phi_t$ is zero, so $\Phi_t\Psi_t$ and $\Phi_t\Gamma_t\Phi_t^\top$ only use previous column information.
3. Let $Z_{1:t}\sim N(0,\Omega_t)$ independently of $H_\star$, consistently with previous stages. Define
\[
Q_t=Q_{t-1}+\lambda\left[Z_t+\sum_{j<t}b_{tj}Q_j+s r\ell_tH_\star\right],
\qquad q_t=\mathbb E[H_\star Q_t].
\tag{11}
\]
4. Compute the current derivative row of $\Psi_t$ and $\Gamma_t$, then compute $\mathsf A_t,\Sigma_t$ using (10). Let $G_{1:t}\sim N(0,\Sigma_t)$ independently of $(Z_\star,Y,M)$. Define
\[
S_t=G_t+\sum_{j\le t}a_{tj}R_j+s q_tZ_\star,
\qquad R_{t+1}=M(Y-\sigma(S_t)).
\tag{12}
\]

All column functions are linear. More precisely,
\[
Q_{1:t}=\Psi_tZ_{1:t}+q_{1:t}H_\star,\qquad
\Gamma_t=\Psi_t\Omega_t\Psi_t^\top+q_{1:t}q_{1:t}^\top,
\tag{13}
\]
and their coefficients can be calculated without integration:
\[
(\Psi_t)_{tj}=(\Psi_{t-1})_{t-1,j}
+\lambda\mathbf1_{\{j=t\}}+\lambda\sum_{k<t}b_{tk}(\Psi_{t-1})_{kj},
\]
\[
q_t=q_{t-1}+\lambda\sum_{j<t}b_{tj}q_j+\lambda s r\ell_t,
\tag{14}
\]
where nonexistent entries at $t=1$ are zero. In particular every diagonal entry of $\Psi_t$ equals $\lambda$.

For the row derivatives, differentiate the already explicit scalar recursion:
\[
\frac{\partial R_{t+1}}{\partial G_j}
=-M\sigma'(S_t)\left[\mathbf1_{\{j=t\}}
+\sum_{k\le t}a_{tk}\frac{\partial R_k}{\partial G_j}\right],\quad j\le t.
\tag{15}
\]
Thus the remaining computations are finite-dimensional Gaussian integrals and a Bernoulli average; there is no unknown limiting quantity outside the recursion.

## 5. Query-block size cancels exactly

The apparent dependence on $\delta$ in (7)–(12) is only a bookkeeping choice. Let $R^{\rm tr}_t$ be the row recursion conditioned on $M=1$. Define
\[
\widehat\Delta_t=\alpha(\mathbb E[R_i^{\rm tr}R_j^{\rm tr}])_{i,j\le t},\qquad
\widehat\Phi_t=\alpha(\mathbb E[\partial_{G_j}R_i^{\rm tr}])_{i,j\le t},
\qquad \widehat\ell_t=\alpha\mathbb E[Z_\star R_t^{\rm tr}].
\]
Since $R_t=0$ when $M=0$,
\[
\widehat\Delta_t=\delta\Delta_t,\qquad
\widehat\Phi_t=\delta\Phi_t,\qquad \widehat\ell_t=\delta\ell_t.
\]
Define $T_t=(I-a^2\Psi_t\widehat\Phi_t)^{-1}$ and
$U_t=(I-a^2\widehat\Phi_t\Psi_t)^{-1}$. Then (10) becomes
\[
\boxed{\begin{aligned}
\mathsf A_t&=\nu\Psi_t+a^2\Psi_tU_t,\\
\mathsf B_t&=\gamma^{-1}\left[\nu\widehat\Phi_t+a^2\widehat\Phi_tT_t\right],\\
\Sigma_t&=\nu\Gamma_t+a^2T_t\left[\Gamma_t+a^2\Psi_t\widehat\Delta_t\Psi_t^\top\right]T_t^\top,\\
\Omega_t&=\gamma^{-1}\left\{\nu\widehat\Delta_t+a^2U_t
\left[\widehat\Delta_t+a^2\widehat\Phi_t\Gamma_t\widehat\Phi_t^\top\right]U_t^\top\right\}.
\end{aligned}}
\tag{16}
\]
Replace $s r\ell_t$ in (11) by $(s/\gamma)\widehat\ell_t$ and use $M=1$ in the training scalar recursion. This is an entirely $\delta$-free prescription, depending only on $(\alpha,\gamma,\beta,c,a,\nu)$.

On a query row $M=0$, every $R_j$ is zero. The physical test path is therefore
\[
\boxed{S_t^{\rm test}=s q_tZ_\star+G_t,\qquad
G_{1:T}\sim N(0,\Sigma_T)\text{ independently of }Z_\star.}
\tag{17}
\]
Its deterministic teacher/score overlaps are
\[
\mathcal A_t=s q_t,\qquad
\mathcal Q_{st}=s^2q_sq_t+(\Sigma_T)_{st}.
\tag{18}
\]
Equation (16) proves algebraically that these quantities are independent of the number of appended queries.

## 6. Positive definiteness: no regularization or algorithm change

Suppose $c>0$. Equations (10) imply
\[
\Omega_t\succeq r\nu\Delta_t,\qquad \Sigma_t\succeq\nu\Gamma_t.
\tag{19}
\]
Initially $\Delta_1=p/4>0$. If $\Delta_t\succ0$, then $\Omega_t\succ0$. Since $\Psi_t$ is triangular with diagonal $\lambda>0$, (13) gives $\Gamma_t\succ0$, hence $\Sigma_t\succ0$.

To continue the induction, suppose $R_{t+1}$ were in the linear span of $R_1,\ldots,R_t$ almost surely. Condition on $(Z_\star,Y,M,G_1,\ldots,G_{t-1})$. On the event $M=1$ of positive probability, all previous residuals are fixed. But the conditional variance of $G_t$ is positive because $\Sigma_t\succ0$, and
\[
R_{t+1}=Y-\sigma\left(G_t+\sum_{j\le t}a_{tj}R_j+s q_tZ_\star\right)
\]
is a strictly monotone nonconstant function of that conditional Gaussian. This is impossible. Therefore $\Delta_{t+1}\succ0$. Induction establishes positive definiteness at every finite stage, including the uninformative-teacher case $\beta=0$.

The case $c=0$ is immediate from (1): every score is zero. It need not be passed through a theorem requiring nonsingular covariances.

## 7. Why this is ordinary GD, including adaptive overlaps

For any fixed deterministic arrays $a_{tj},b_{tj}$, introduce fields
\[
\mathbf Z_t=A_0^\top\mathbf R_t-\sum_{j<t}b_{tj}\mathbf Q_j,
\qquad
\mathbf G_t=A_0\mathbf Q_t-\sum_{j\le t}a_{tj}\mathbf R_j.
\]
Using (11) and (12) coordinatewise adds these same terms back. With empirical teacher overlaps, the resulting algorithm is identically (4), at every finite dimension. This algebra does not impose an Onsager correction on GD.

For the theorem application, first use the deterministic scalar overlaps $q_t,\ell_t$ of (11)–(12). The resulting auxiliary AMP has coordinatewise nonlinearities, so WZF applies. Its empirical overlaps converge to $q_t,\ell_t$ by its joint $W_2$ convergence with the teacher side information. Then compare it with the empirical-overlap recursion (4).

Here are explicit bounds closing that comparison. Normalize errors by
$e^Q_t=\|Q_t^{\rm GD}-Q_t^{\rm aux}\|/\sqrt m$ and
$e^R_t=\|R_t^{\rm GD}-R_t^{\rm aux}\|/\sqrt N$.
On events where $\|A_0\|_{\rm op}$, $\|h\|/\sqrt m$, $\|z\|/\sqrt N$, and the fixed dimension ratios are bounded, Cauchy–Schwarz gives
\[
|q_t^{\rm GD}-q_t|\le C e^Q_t+
|m^{-1}h^\top Q_t^{\rm aux}-q_t|,
\]
\[
|\ell_t^{\rm GD}-\ell_t|\le C e^R_t+
|N^{-1}z^\top R_t^{\rm aux}-\ell_t|.
\]
The two trailing terms tend to zero. The physical updates and $\operatorname{Lip}(\sigma)=1/4$ then imply
\[
e^Q_t\le e^Q_{t-1}+C e^R_t+o_{\mathbb P}(1),\qquad
e^R_{t+1}\le C e^Q_t+o_{\mathbb P}(1).
\tag{20}
\]
The initial error is zero, so both errors vanish at every fixed time. Replacing $s_d,\lambda_d,r_d$ by their limits only adds vanishing terms of the same kind.

Finally, $\|E_d\|_{\rm op}=o_{\mathbb P}(1)$ in (3) transfers this conclusion to the **actual tanh RF matrix**. At fixed time $\|Q_t\|/\sqrt m=O_{\mathbb P}(1)$ and $\|R_t\|/\sqrt N\le1$. Thus every occurrence of $E_dQ_t$ or $E_d^\top R_t$ is $o_{\mathbb P}(1)$ in the relevant normalized norm, and the same finite induction proves convergence of actual-GD iterates and score vectors.

The appended queries never enter the update, since their mask is zero. Conditional on the training data and features, their score paths are iid fresh-test paths. A conditional law of large numbers for bounded Lipschitz functions therefore converts empirical query convergence into convergence in probability of the conditional fresh-test law to (17). Quadratic observables also converge: the fixed-time operator bounds and Gaussian Lipschitz concentration give bounded conditional fourth moments in probability, so the conditional variance of their query averages is $O_{\mathbb P}(1/N)$. Consequently the realized fresh-test covariance in B03 converges to (18).

## 8. Source hypotheses and indexing audit

The directly inspected primary sources are:

- Zhou Fan, *Approximate Message Passing algorithms for rotationally invariant matrices*, Annals of Statistics 50(1), 197–224 (2022), [arXiv:2008.11892v5](https://arxiv.org/pdf/2008.11892). Section 2.4 gives the rectangular cumulant convention. Section 5.1, equations (5.7)–(5.13), gives the memory/covariance prescription. Corollary 5.4 addresses degeneracy for the invariant comparison ensemble.
- Tianhao Wang, Xinyi Zhong, and Zhou Fan, *Universality of Approximate Message Passing algorithms and tensor networks*, Annals of Applied Probability 34(4), 3943–3994 (2024), [arXiv:2206.13037v5](https://arxiv.org/html/2206.13037v5). The applicable result is Theorem 2.22 with Assumption 2.17, algorithm (2.14), and prescriptions (D.4)–(D.5). Proposition D.1(b) supplies the matrix criterion checked in B03.

The application checks are as follows.

| Requirement | Verification |
|---|---|
| Generalized-invariant matrix with invariant comparison law | B03 Theorem 5, applied to the perpendicular RF matrix with all training/query rows present |
| Independent initialization and side information | $A_0$ is independent of $z,Y,M,h$ after teacher-coordinate separation |
| Nonzero initial AMP second moment | $R_1=M(Y-1/2)$ and $\mathbb ER_1^2=p/4$; zero GD weights do not mean zero AMP initialization |
| All side-information moments and polynomial density | Gaussian teacher coordinates and bounded labels/masks have exponential moments; their polynomial algebra is dense in $L^2$ |
| Coordinatewise continuous, polynomial-growth, Lipschitz functions | Column functions are linear; row functions are finite compositions of sigmoid and affine functions with deterministic coefficients |
| Uniform Lipschitz constants over side information | Extend the mask off $\{0,1\}$ by the smooth bounded function $\sin^2(\pi x/2)$; this leaves actual iterates unchanged and keeps row derivatives uniformly bounded |
| Eventual operator bound and positive spectral second moment | B03 Theorem 5; $\mathbb ED^2=v>0$ |
| Nonsingular $\Omega_t,\Sigma_t$ | The direct induction in Section 6 |
| Empirical teacher-overlap dependence | Apply the theorem to deterministic overlaps first, then use (20) |
| Fixed time and consistent finite aspect ratios | Every statement fixes $T$ before $d\to\infty$; deterministic parameter replacements are handled by (20) |
| Fresh-test extraction | Mask-zero appended rows, (17), and the conditional law of large numbers |

The source notation uses a matrix with “$m$ rows and $n$ columns.” Here these correspond to $N$ rows and $m$ features, so its aspect parameter is $r=\delta/\gamma$, **not** the RF ratio $\gamma=m/d$. The zero padding in Section 2 is essential when $N>m$.

## 9. Exact first-step validation

Put
\[
\mu=\mathbb E[Z_\star(\sigma(\beta Z_\star)-1/2)].
\]
Using the query-independent recursion (16),
\[
\widehat\Delta_{11}=\alpha/4,\quad \widehat\Phi_{11}=0,
\quad \widehat\ell_1=\alpha\mu,\quad
\Omega_{11}=\frac{\alpha v}{4\gamma},\quad \Psi_{11}=\lambda.
\]
Consequently
\[
Q_1=\lambda Z_1+\frac{ca\mu}{\sqrt\gamma}H_\star,
\quad q_1=\frac{ca\mu}{\sqrt\gamma},\quad
\Gamma_{11}=\frac{c^2v}{4\alpha\gamma}+\frac{c^2a^2\mu^2}{\gamma}.
\]
The forward memory coefficient is $a_{11}=\lambda v$. It vanishes from a test score because $R_1=0$ on the test block. The Gaussian residual variance is
\[
\begin{aligned}
\Sigma_{11}
&=v\Gamma_{11}+a^4\lambda^2\widehat\Delta_{11}\\
&=c^2\left[\frac{\mu^2a^2v}{\gamma}
+\frac{a^4+v^2/\gamma}{4\alpha}\right].
\end{aligned}
\]
Since $s q_1=ca^2\mu$, the fresh-test law is exactly
\[
\boxed{S_1^{\rm test}=ca^2\mu\,Z_\star+	au_1G,\qquad
\tau_1^2=c^2\left[\frac{\mu^2a^2v}{\gamma}
+\frac{a^4+v^2/\gamma}{4\alpha}\right],}
\tag{21}
\]
with $G$ independent standard normal. This reproduces both terms of the audited first-step variance. Omitting $\kappa_4=\delta a^4$ would incorrectly remove $c^2a^4/(4\alpha)$; forgetting the mask-zero query block would incorrectly retain the training self term $\lambda v(Y-1/2)$.

## 10. Review status

B04 independently compared (10) with Fan's primary-source equations and checked the positive-definiteness induction. B03 independently checked the causal construction, all four query-ratio cancellations, the overlap comparison, the query extraction, and the all-order cumulant derivation; its separate three-Gaussian query calculation also agrees with (21). B05 independently checked the cumulant derivation and the B03 spectral/source hypotheses. These reviewers found no gap in the stated finite-horizon conclusion. The matrix input remains explicitly B03 Theorem 5 and its teacher-spike decomposition. No statement here asserts novelty of the original AMP theorem or a uniform-in-time GD limit.
