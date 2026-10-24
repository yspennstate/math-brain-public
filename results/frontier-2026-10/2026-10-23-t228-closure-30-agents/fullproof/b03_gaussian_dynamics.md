# T357: Gaussian tanh random features beyond one GD step

Author: B03. Date: 2026-10-24. This file does not modify the frozen followup notes.

**Status.** Theorem 6 assembles a complete arbitrary fixed finite-horizon theorem for the original Gaussian tanh random-feature GD model, using the explicit recursion in B01 and the exact calibration transfer in B04. Sections 1–6 prove the structural lemmas; Section 8 verifies the dynamical-universality matrix hypotheses; Section 9 supplies the exact causal AMP embedding and overlap comparison. The theorem covers every finite positive aspect ratio and every fixed positive step size. It does not claim an arbitrary-ratio infinite-time or unbounded-stopping result. Independent matrix, recursion, and analytic-transfer checks are recorded in the companion files.

## 1. Model and normalization

Use the Gaussian model in `followup/T357_gaussian_first_step_attempt.md`: inputs $X_i\sim N(0,I_d)$, a deterministic unit teacher $\theta$, conditionally independent labels $Y_i\mid X_i\sim\mathrm{Bernoulli}(\sigma(\beta\theta^\top X_i))$, fixed finite $\beta\ge0$, and independent feature rows $W_j\sim N(0,I_d/d)$. Let $n/d\to\alpha>0,m/d\to\gamma>0$, $\phi=\tanh$, $H_{ij}=\phi(W_j^\top X_i)$, and $K=HH^\top/m$.

Write the score as $S_t(x)=(b^t)^\top h(x)$, where $b^t=a^t/\sqrt m$ in the old network convention. Mean-loss GD with output-weight step $cd$ is exactly

\[
b^0=0,\quad u^t=Hb^t,\quad r^t=Y-\sigma(u^t),\quad
b^{t+1}=b^t+\frac{\lambda_d}{m}H^\top r^t,
\qquad\lambda_d=\frac{cd}{n}\longrightarrow\frac c\alpha. \tag{1.1}
\]

Consequently $u^{t+1}=u^t+\lambda_dKr^t$. All statements below allow any fixed $c>0$, except the explicit small-step conclusion in Proposition 3. The horizon $T$ is a fixed integer independent of dimension. No claim concerns $T_d\to\infty$.

Define
\[
a=\mathbb E[G\phi(G)],\quad v=\mathbb E\phi(G)^2,\quad
\nu=v-a^2>0,
\quad A(q)=\mathbb E\phi'(\sqrt qG).
\tag{1.2}
\]
Strict positivity of $\nu$ follows because tanh is not a scalar multiple of its input in Gaussian $L^2$.

## 2. Uniform feature-matrix bounds

Conditional on $F$, whose rows are $W_j^\top$, the rows of $H$ are independent centered random vectors. For any unit $v_0\in\mathbb R^m$, the function $x\mapsto v_0^\top\phi(Fx)$ is $\|F\|_{\rm op}$-Lipschitz and odd. Gaussian concentration therefore gives
\[
\mathbb E[\exp(sv_0^\top h(X))\mid F]
\le \exp(s^2\|F\|_{\rm op}^2/2).
\tag{2.1}
\]
For a unit $u_0\in\mathbb R^n$, conditional independence gives the same bound for $u_0^\top Hv_0$. Taking $1/4$-nets of the two unit spheres and using the standard net inequality proves
\[
\|H\|_{\rm op}=O_P(\sqrt d),\qquad
\|K\|_{\rm op}=O_P(1). \tag{2.2}
\]
The failure probabilities at sufficiently large fixed constants decay exponentially in $d$. The same net argument for the Gaussian matrices proves $\|F\|_{\rm op}=O_P(1)$ and $\|X\|_{\rm op}=O_P(\sqrt d)$, again with exponential tails. Integrating these bounds shows that all fixed moments of the corresponding normalized norms are uniformly bounded.

The elementary proof above does not infer a bounded spectral norm merely from entrywise boundedness.

## 3. Delocalization along every fixed finite GD path

**Theorem 1.** For each fixed $T<\infty$,
\[
\max_{0\le t\le T}\|b^t\|_2=O_P(1),\qquad
\max_{0\le t\le T}\|b^t\|_\infty
=O_P\!\left(\sqrt{\frac{\log d}{d}}\right). \tag{3.1}
\]
The first bound has uniformly bounded fixed moments. The proof uses the same reused training sample at every step.

**Proof.** Since $\|r^t\|_2\le\sqrt n$, (1.1) gives directly
\[
\|b^t\|_2\le \frac{T\lambda_d}{m}\|H\|_{\rm op}\sqrt n=O_P(1). \tag{3.2}
\]

For the coordinate bound, denote feature column $j$ by $h_j$, replace that column by zero, and retain the denominator $m$. Write $K^{-j}=K-h_jh_j^\top/m$, and let $u^{-j,t},r^{-j,t}$ be the corresponding GD scores and residuals. The matrices satisfy $0\preceq K^{-j}\preceq K$.

Conditional on $X,Y,F_{-j}$, the vector $r^{-j,t}$ is independent of $W_j$, bounded in Euclidean norm by $\sqrt n$, and
\[
G\mapsto (r^{-j,t})^\top\phi(XG/\sqrt d)
\]
is odd and $\|X\|_{\rm op}\sqrt{n/d}$-Lipschitz for $G\sim N(0,I_d)$. Its conditional mean is zero. Gaussian concentration followed by a union bound over $j\le m,t<T$, on $\|X\|_{\rm op}\le C\sqrt d$, therefore yields
\[
\max_{j,t<T}|h_j^\top r^{-j,t}|=O_P(\sqrt{d\log d}). \tag{3.3}
\]
The conditioning here is essential: later residuals in the original model are not independent of $W_j$.

Set $e^{j,t}=u^t-u^{-j,t}$. Since sigmoid is $1/4$-Lipschitz,
\[
\|e^{j,t+1}\|_2
\le\left(1+\frac{\lambda_d\|K\|_{\rm op}}4\right)\|e^{j,t}\|_2
+\frac{\lambda_d\|h_j\|_2}{m}|h_j^\top r^{-j,t}|. \tag{3.4}
\]
We have $e^{j,0}=0$ and $\|h_j\|_2\le\sqrt n$. On the simultaneous high-probability bounds (2.2) and (3.3), iteration for fixed $T$ gives
\[
\max_{j,t\le T}\|e^{j,t}\|_2=O_P(\sqrt{\log d}). \tag{3.5}
\]
Thus
\[
|h_j^\top r^t|
\le|h_j^\top r^{-j,t}|+\tfrac14\sqrt n\,\|e^{j,t}\|_2
=O_P(\sqrt{d\log d})
\]
uniformly over the finitely many times and all features. Summing (1.1) over time and dividing by $m$ proves the second assertion in (3.1). ∎

## 4. Joint fresh-test Gaussian approximation for the entire finite path

Let $\mathcal E_d$ contain the features and training sample, and define the exact conditional covariances
\[
A_{t,d}=\mathbb E_X[(\theta^\top X)S_t(X)\mid\mathcal E_d],\qquad
Q_{st,d}=\mathbb E_X[S_s(X)S_t(X)\mid\mathcal E_d]. \tag{4.1}
\]
Write $C_d$ for the covariance matrix of $(\theta^\top X,S_1(X),\ldots,S_T(X))$. All means are zero by oddness.

**Theorem 2.** For fixed $T$, in bounded-Lipschitz distance,
\[
d_{\rm BL}\!\left(
\mathcal L((\theta^\top X,S_1(X),\ldots,S_T(X))\mid\mathcal E_d),
N(0,C_d)\right)\longrightarrow0\quad\text{in probability}. \tag{4.2}
\]
This is a Gaussian approximation whose covariance is allowed to depend on the realized network. It does not assert that $C_d$ has a deterministic limit.

**Proof.** Fix real $u,v_1,\ldots,v_T$, put $b=\sum_tv_tb^t$, and let
\[
f(x)=u\theta^\top x+b^\top\phi(Fx).
\]
Then $\mathbb Ef(X)=0$, and globally
\[
\|\nabla f\|_2\le L:=|u|+\|F\|_{\rm op}\|b\|_2=O_P(1),
\quad
\|\nabla^2 f\|_{\rm op}\le
\varepsilon:=\|\phi''\|_\infty\|F\|_{\rm op}^2\|b\|_\infty=o_P(1).
\tag{4.3}
\]

Here is a self-contained normal-approximation argument. For the Gaussian Ornstein–Uhlenbeck semigroup $P_s$, set
\[
U_f(x)=\int_0^\infty e^{-s}P_s\nabla f(x)\,ds,
\qquad T_f(x)=\nabla f(x)\cdot U_f(x).
\]
Gaussian integration by parts, or integration of $\frac d{ds}P_sf$, gives for smooth bounded $g$
\[
\mathbb E[f(X)g(f(X))]=\mathbb E[T_f(X)g'(f(X))],
\quad\mathbb ET_f=\mathbb Ef^2=:q.
\tag{4.4}
\]
The semigroup derivative identity gives $\|U_f\|_\infty\le L$ and $\|DU_f\|_{\rm op,\infty}\le\varepsilon/2$, whence $\|\nabla T_f\|_2\le3L\varepsilon/2$. Gaussian Poincaré yields
\[
\mathbb E|T_f-q|\le\tfrac32L\varepsilon. \tag{4.5}
\]
For $\psi(t)=\mathbb Ee^{itf(X)}$, (4.4) gives $\psi'(t)=-tq\psi(t)-t\mathbb E[(T_f-q)e^{itf(X)}]$. Solving this scalar differential equation and using $q\ge0$ gives
\[
|\psi(t)-e^{-qt^2/2}|\le\tfrac34t^2L\varepsilon. \tag{4.6}
\]
No lower bound on $q$ is needed.

The conditional covariance matrices are tight because (4.3) and Poincaré bound all diagonal entries. Every subsequence admits a further subsequence on which the bounds in (4.3) hold almost surely and $C_d$ converges along further deterministic realizations in a compact set. Applying (4.6) to a countable dense collection of coefficient vectors, tightness and the characteristic-function criterion identifies every conditional subsequential limit with the corresponding Gaussian covariance limit. This proves (4.2). ∎

The old covariance-operator lemma applies uniformly to these data-dependent weights because their Euclidean norms are tight:
\[
A_{t,d}=a\theta^\top F^\top b^t+o_P(1),
\quad
Q_{st,d}=a^2(F^\top b^s)^\top(F^\top b^t)+\nu(b^s)^\top b^t+o_P(1). \tag{4.7}
\]
Indeed the exact first formula is $A_{t,d}=\theta^\top F^\top D_A b^t$, where $D_A=\operatorname{diag}(A(\|W_j\|^2))$, and $\|D_A-aI\|_{\rm op}\to0$. The exact second formula is $Q_{st,d}=(b^s)^\top\Sigma_Fb^t$.

For any subsequence on which $(A_{t,d},Q_{st,d})$ converges in probability to deterministic limits, Theorem 2 supplies the full joint finite-time Gaussian test-law limit on that subsequence. With fresh labels, apply the common Markov kernel $Y\mid Z\sim\mathrm{Bernoulli}(\sigma(\beta Z))$.

The total-variation and exact-calibration strengthening is proved separately in `fullproof/b04_calibration_transfer.md`; its conditions are furnished by Theorem 1 together with a nonvanishing coefficient norm, for example Proposition 3 below.

## 5. A rigorous nondegeneracy condition

Put $\rho_\beta=\mathbb E\sigma'(\beta G)>0$. This is positive for every fixed finite $\beta$.

**Proposition 3.**
\[
\|b^1\|_2^2\ge\frac{c^2v\rho_\beta}{\alpha\gamma}+o_P(1). \tag{5.1}
\]
If $\lambda_d\|K\|_{\rm op}\le4$, then pathwise
\[
\|b^t\|_2\ge\tfrac12\|b^1\|_2\quad\text{for every integer }t\ge1. \tag{5.2}
\]
In particular a sufficiently small, fixed positive $c$ makes (5.2) hold with probability tending to one. At every fixed positive time in this regime, the teacher-orthogonal fresh-score variance is bounded away from zero in probability.

**Proof.** Conditional on $X,F$, write $R=Y-1/2=\mu+\epsilon$, where $\mu_i=\sigma(\beta Z_i)-1/2$, independent centered $\epsilon_i$ have variance $D_{ii}=\sigma'(\beta Z_i)$, and $D$ is diagonal. Since
\[
\|b^1\|_2^2=\frac{\lambda_d^2}{m}R^\top KR,
\]
expanding the quadratic form and using independence and bounded fourth moments gives
\[
\operatorname{Var}(R^\top KR\mid X,F)
\le C\{\operatorname{tr}(K^2)+\|K\mu\|_2^2\}
\le Cn\|K\|_{\rm op}^2. \tag{5.3}
\]
Thus $\|b^1\|_2^2=\lambda_d^2m^{-1}(\mu^\top K\mu+\operatorname{tr}KD)+o_P(1)$. The first term is nonnegative. Conditional on $F$, the row quantities $D_{ii}K_{ii}$ are iid, bounded, and have mean
\[
\frac1m\sum_j\mathbb E_X[\sigma'(\beta\theta^\top X)\phi(W_j^\top X)^2].
\]
Uniformly over $j$, $\|W_j\|^2\to1$ and $\theta^\top W_j\to0$. Continuity of bounded Gaussian expectations therefore makes this mean tend to $v\rho_\beta$. The conditional LLN proves $n^{-1}\operatorname{tr}KD\to v\rho_\beta$, yielding (5.1).

For (5.2), let $L(b)=\sum_i\ell(Y_i,h_i^\top b)$, $g_0=\nabla L(0)=-H^\top R$, and $\eta=\lambda_d/m$. Its gradient is $\|H\|_{\rm op}^2/4$-Lipschitz. Under the displayed step condition, descent gives $L(b^t)\le L(b^1)\le L(0)-\eta\|g_0\|^2/2$. Convexity gives $L(b^t)\ge L(0)+g_0^\top b^t$. Combining these and Cauchy–Schwarz yields $\|b^t\|\ge\eta\|g_0\|/2=\|b^1\|/2$. Finally, the exact Hermite decomposition implies
\[
Q_{tt,d}-A_{t,d}^2\ge(\nu-o_P(1))\|b^t\|_2^2, \tag{5.4}
\]
uniformly for the fixed-time path. ∎

## 6. Teacher-coordinate removal is operator-small

Rotate coordinates so that $\theta=e_1$. Write $X_i=(z_i,x_i)$ and $W_j=(t_j,f_j)$, with $x_i\in\mathbb R^{d-1}$, $f_j\in\mathbb R^{d-1}$. Let $V$ have rows $f_j^\top$, $U_{ij}=x_i^\top f_j$, $H^0=\phi(U)$. The vectors $z,t$, the noise matrix $H^0$, and label randomness conditional on $z$ have the required independence: $H^0$ is independent of $(z,t,Y)$.

**Proposition 4.** For any fixed proportional number of rows, including training rows together with an additional proportional block of test rows,
\[
\left\|\frac{H-H^0-a zt^\top}{\sqrt m}\right\|_{\rm op}\longrightarrow0
\quad\text{in probability}. \tag{6.1}
\]

**Proof.** Taylor's theorem gives
\[
H-H^0-a zt^\top
=\operatorname{diag}(z)[\phi'(U)-a\mathbf1\mathbf1^\top]\operatorname{diag}(t)+R,
\quad |R_{ij}|\le C z_i^2t_j^2. \tag{6.2}
\]
The remainder satisfies
\[
\|R\|_F^2\le C\Big(\sum_i z_i^4\Big)\Big(\sum_jt_j^4\Big)=O_P(1),
\]
so $\|R\|_{\rm op}/\sqrt m=o_P(1)$.

Conditional on $V$, the centered rows of the derivative matrix $\phi'(U)$ are independent. The same concentration-and-net proof as in Section 2 applies with Lipschitz constant $\|\phi''\|_\infty\|V\|_{\rm op}$; hence the centered matrix has operator norm $O_P(\sqrt d)$. Its row mean minus $a\mathbf1$ is the vector $\delta_j=A(\|f_j\|^2)-a$. Bounded $A'$ and $\mathbb E(\|f_j\|^2-1)^2=O(d^{-1})$ give $\|\delta\|_2=O_P(1)$. Thus
\[
\|\phi'(U)-a\mathbf1\mathbf1^\top\|_{\rm op}=O_P(\sqrt d).
\]
Finally $\|z\|_\infty=O_P(\sqrt{\log d})$ and $\|t\|_\infty=O_P(\sqrt{\log d/d})$, so the first matrix in (6.2), after division by $\sqrt m$, is $O_P(\log d/\sqrt d)=o_P(1)$. ∎

This is an operator-norm statement for the normalized *feature matrix*, not just for its population covariance. If $A,\widetilde A$ have bounded operator norm and $\|A-\widetilde A\|_{\rm op}=o_P(1)$, finite-time logistic GD in the parameter $w=\sqrt m b$, with normalized scores $Aw$, differs by $o_P(\sqrt m)$ in coefficient norm and $o_P(\sqrt n)$ in score norm. To verify, subtract the two recursions, use $1/4$-Lipschitzness of sigmoid, $\|r\|\le\sqrt n$, and $\|w^t\|=O_P(\sqrt m)$, and iterate the resulting linear inequality for fixed $T$.

## 7. Source audit and the route not yet certified here

Primary sources were opened on 2026-10-24. The following notes distinguish inspected theorem assumptions from merely relevant titles.

1. [Gerbelot et al., arXiv:2210.06591v3](https://arxiv.org/html/2210.06591v3), Theorem 2 and assumptions A1–A7: the iterated matrix has iid Gaussian entries; iterate width is finite. Applying this directly with $H=\tanh(XF^\top)$ fails the matrix assumption. Taking all feature coordinates as an index vector instead makes the width extensive. A separate universality reduction is required.
2. [Nishiyama–Imaizumi, arXiv:2602.06320v2](https://arxiv.org/html/2602.06320v2), Assumption 2.1 and Section 2: their model has independent design entries and studies stochastic gradient flow. The paper expressly does not prove exact high-dimensional SGD–SGF equivalence. It cannot itself justify the present discrete RF-GD path.
3. [Fan–Wang, arXiv:2601.21093v3](https://arxiv.org/html/2601.21093v3), revised 21 October 2026: Assumption 2.2(a) keeps the student and teacher index dimensions fixed; Assumption 2.1 uses sublinear minibatches. The extensive random-feature hidden layer and the discrete full-batch trajectory here do not directly satisfy that setup.
4. [Hu–Lu, arXiv:2009.07669v3](https://arxiv.org/pdf/2009.07669): the basic object is the regularized optimizer. Assumption A.5 requires a strongly convex regularizer. Its Gaussian-equivalence theorem is not a finite-time unregularized-GD theorem.
5. [Wang–Zhong–Fan, arXiv:2206.13037v5](https://arxiv.org/html/2206.13037v5), Definition 2.20, Proposition D.1(b), Theorem 2.22 and Lemma D.9: this is the useful prospective route. It requires signed-permutation invariance, the complete limiting diagonal distribution, uniform small offdiagonal entries for generated polynomial matrices, bounded operator norm, independent side information, and regular AMP nonlinearities. Singular state covariances require a justified perturbation argument. The paper's tensor-network result supports polynomial first-order iterations; passing to logistic dynamics must be justified through its AMP embedding/approximation argument rather than asserted from matching spectral laws.
6. [Louart–Liao–Couillet, arXiv:1702.05419v2](https://arxiv.org/pdf/1702.05419), Theorem 2: after conditioning on $V$, take their Gaussian matrix to be the perpendicular data and their bounded deterministic input matrix to be $V^\top$. Tanh is Lipschitz and all three dimensions are proportional. Their spectral deterministic equivalent depends on the feature covariance. Our Hermite operator estimate reduces this covariance to $a^2VV^\top+\nu I$, which is the covariance of $aXV^\top+\sqrt\nu G$. This establishes a spectral candidate; spectral matching alone is insufficient for dynamics.
7. [Gorini et al., arXiv:2604.11729v1](https://arxiv.org/html/2604.11729v1): Section 1.3 explicitly discusses polynomial versus Lipschitz first-order methods. Its general polynomial results do not remove the required logistic approximation step automatically.

The next proof obligations are concrete:

* Prove that $A_0=H^0/\sqrt m$ satisfies Proposition D.1(b)'s simultaneous entrywise bounds for every fixed matrix power. A promising self-contained argument clips the operator norms of the base Gaussian matrices and of $A_0$, then applies Gaussian concentration to each polynomial matrix entry; clipping makes its global Lipschitz constant $O(d^{-1/2})$. Sign symmetry gives zero offdiagonal means; permutation symmetry identifies diagonal means.
* Combine that lemma with the inspected spectral theorem to identify the diagonal distribution with the bi-orthogonally invariant surrogate $A_G=(aXV^\top+\sqrt\nu G)/\sqrt m$.
* Give the causal AMP embedding of the masked logistic GD recursion for $A_0+(a/\sqrt m)zt^\top$, with finite Gaussian perturbations if needed, and verify all nondegeneracy and polynomial-density hypotheses. The rank-one scalar coefficients are empirical overlaps and must also be controlled.
* Append a proportional independent test block and set its training mask to zero. This avoids incorrectly trying to recover test covariance from the singular-value law of the training matrix alone.
* Supply a finite-dimensional Gaussian-query recursion for the three independent Gaussian matrices in $A_G$, then prove the resulting deterministic test-path covariance limit. Theorem 2 and B04's TV theorem would then deliver exact risks and calibration. A limiting optimizer over all training times needs an additional argument beyond any fixed horizon.

These obligations were the initial audit checklist. Sections 8–9 and the companion B01/B04 proofs now close the fixed-horizon items, as assembled in Theorem 6. The separate unbounded-time obligation remains subject to the explicitly restricted B02 extension.

## 8. The perpendicular RF matrix satisfies generalized invariance

This section closes the first two matrix proof obligations in Section 7. The AMP embedding and state-evolution identification remain separate obligations.

Let $N/d\to\delta>0$ be the total number of rows, $p=d-1$, $X\in\mathbb R^{N\times p}$ have independent standard Gaussian entries, and $G\in\mathbb R^{m\times p}$ be an independent standard Gaussian matrix. Set
\[
V=G/\sqrt d,\qquad
A_0=\frac1{\sqrt m}\phi(XV^\top),\qquad r=N/m\to\delta/\gamma.
\tag{8.1}
\]
For the almost-sure source-theorem application below, choose the standard product construction in which the full data-array sequence is independent of the full feature-array sequence, and different dimensions may be taken independent. This choice is harmless for the final in-probability conclusions, which depend only on the per-dimension laws. It avoids conditioning on an entire feature sequence that could encode data from another dimension under an adversarial cross-dimension coupling.

**Theorem 5 (matrix hypothesis verification).** The matrix $A_0$ has the rectangular generalized-invariance property used by Wang–Zhong–Fan, with the same limiting diagonal distribution as
\[
A_G=\frac{aXV^\top+\sqrt\nu\,E}{\sqrt m},
\tag{8.2}
\]
where $E$ is an independent standard Gaussian $N\times m$ matrix. In particular:

1. The operator norm is eventually bounded by a deterministic constant.
2. The singular-value distribution has a deterministic compactly supported limit, identical to that of (8.2), and its second moment is positive.
3. For every fixed integer $k\ge0$ and every $\epsilon>0$, the following inequalities hold eventually almost surely (with positive powers used for the first two lines):
\[
\max_i\left|((A_0A_0^\top)^k)_{ii}-\frac1N\operatorname{tr}(A_0A_0^\top)^k\right|
+\max_{i\ne j}|((A_0A_0^\top)^k)_{ij}|
\le m^{-1/2+\epsilon},
\tag{8.3}
\]
\[
\max_i\left|((A_0^\top A_0)^k)_{ii}-\frac1m\operatorname{tr}(A_0^\top A_0)^k\right|
+\max_{i\ne j}|((A_0^\top A_0)^k)_{ij}|
\le m^{-1/2+\epsilon},
\tag{8.4}
\]
\[
\max_{i,j}|((A_0A_0^\top)^kA_0)_{ij}|\le m^{-1/2+\epsilon}.
\tag{8.5}
\]
4. It is invariant under independent signed permutations of its rows and columns.

**Proof of the uniform entry estimates.** For a matrix $B$, let $\mathcal P_R(B)$ denote its Frobenius-metric projection onto the closed convex set $\{C:\|C\|_{\rm op}\le R\}$. This map clips singular values at $R$ and is Frobenius-nonexpansive. It commutes with left and right orthogonal transformations.

Fix sufficiently large deterministic constants $C_X,C_G,C_A$, and define
\[
\bar X=\mathcal P_{C_X\sqrt d}(X),\quad
\bar G=\mathcal P_{C_G\sqrt d}(G),\quad
B=\mathcal P_{C_A}\!\left(\frac1{\sqrt m}\phi(\bar X\bar G^\top/\sqrt d)\right).
\tag{8.6}
\]
The exponential norm bounds in Section 2 show $B=A_0$ outside an event of probability at most $C e^{-cd}$. Thus $B=A_0$ eventually almost surely. This explicit clipping step avoids the invalid inference that a derivative bound only on a nonconvex high-probability set is automatically a global Lipschitz bound.

For any two base inputs, the product inequality and the scalar Lipschitz property of tanh give
\[
\|B(X,G)-B(X',G')\|_F
\le\frac C{\sqrt m}\big(\|X-X'\|_F+\|G-G'\|_F\big)
\le\frac {C'}{\sqrt d}\|(X,G)-(X',G')\|_F.
\tag{8.7}
\]
Because $\|B\|_{\rm op}\le C_A$, each scalar entry of $(BB^\top)^k$, $(B^\top B)^k$, or $(BB^\top)^kB$ is a globally $C_k$-Lipschitz function of $B$ in Frobenius norm. This follows by telescoping products; for example
\[
\|(BB^\top)^k-(B'B'^\top)^k\|_F
\le 2k C_A^{2k-1}\|B-B'\|_F.
\]
Consequently each such scalar entry is $C_k'/\sqrt d$-Lipschitz in the independent standard Gaussian base entries.

Oddness of tanh and equivariance of all clipping maps imply that $B$ is invariant under row and column signed permutations. Therefore every offdiagonal entry of $(BB^\top)^k$ or $(B^\top B)^k$ has expectation zero; all diagonal entries in a given block have the same expectation; and all entries of $(BB^\top)^kB$ have expectation zero. Gaussian concentration and a union bound over $O(d^2)$ entries give, for any fixed $\eta>0$, failure probability at most
\[
C_kd^2\exp(-c_k d^{2\eta})
\]
for the assertion that every entry differs from its expectation by at most $d^{-1/2+\eta}$. This sequence is summable. The difference between a diagonal expectation and the realized average trace is bounded by the same maximum diagonal error. Choose $\eta<\epsilon$ and absorb fixed constants and dimension ratios. Borel–Cantelli and $B=A_0$ eventually prove (8.3)–(8.5), simultaneously for the countable collection of integer $k$ and rational positive $\epsilon$. Arbitrary positive $\epsilon$ follows by decreasing it to a rational number.

**Proof of spectral matching.** Let
\[
\Sigma_V=\mathbb E_x[\phi(Vx)\phi(Vx)^\top],\qquad
C_V=a^2VV^\top+\nu I_m.
\]
The old covariance proof strengthens to almost sure operator convergence here:
\[
\|\Sigma_V-C_V\|_{\rm op}\to0. \tag{8.8}
\]
Indeed Gaussian norm and spherical-inner-product tails imply, eventually almost surely,
\[
\max_j|\|f_j\|^2-1|=O(\sqrt{\log d/d}),\qquad
\max_{j\ne k}\frac{|f_j^\top f_k|}{\|f_j\|\|f_k\|}
=O(\sqrt{\log d/d}).
\]
The offdiagonal higher-odd-Hermite remainder has operator norm at most its maximal absolute row sum, hence at most $C m(\log d/d)^{3/2}=o(1)$. The diagonal remainder and linear Hermite coefficient converge uniformly, proving (8.8).

Condition on any realization of the sequence $V$ satisfying these bounds. The inspected Louart–Liao–Couillet spectral theorem applies to $\phi(XV^\top)$, since $V^\top$ is bounded in operator norm, tanh is Lipschitz, and all dimensions are proportional. It gives the same spectral deterministic equivalent as a Gaussian sample matrix with row covariance $\Sigma_V$. A Gaussian coupling and
\[
\|\Sigma_V^{1/2}-C_V^{1/2}\|_{\rm op}
\le\|\Sigma_V-C_V\|_{\rm op}^{1/2}
\]
replace $\Sigma_V$ by $C_V$ without changing the limiting spectral law. Conditional on $V$, (8.2) has exactly Gaussian independent rows with covariance $C_V/m$. Fubini's theorem transfers this conditional almost-sure conclusion to the joint model.

The empirical eigenvalue law of $VV^\top$ tends to the Marchenko–Pastur law with aspect $\gamma$, so the empirical law of $C_V$ tends to its image under $x\mapsto\nu+a^2x$. The fixed-point description in the spectral theorem consequently has a deterministic limit. More explicitly, if $H$ is that image law, the feature-side squared-singular law is characterized for $\zeta>0$ by
\[
\delta_\zeta=\int\frac{t}{\zeta+rt/(1+\delta_\zeta)}\,dH(t),\qquad
m(-\zeta)=\int\frac1{\zeta+rt/(1+\delta_\zeta)}\,dH(t).
\tag{8.9}
\]
The positive solution is unique: divide its defining equation by $1+\delta_\zeta$ to obtain $\delta_\zeta/(1+\delta_\zeta)=\int t/[\zeta(1+\delta_\zeta)+rt]\,dH(t)$, whose left side is strictly increasing and right side decreasing. The bound $0\le\delta_\zeta\le(\sup\operatorname{supp}H)/\zeta$ makes continuity under weak convergence of uniformly compactly supported covariance laws immediate by subsequences. The deterministic operator bounds turn weak spectral convergence into convergence of every fixed spectral moment. Also $m^{-1}\operatorname{tr}(A_0^\top A_0)\to r v>0$. **Normalization for the AMP source:** its singular-value law $D$ is padded to the row dimension $N$, whereas (8.9) is normalized to the feature dimension $m$. For $k\ge1$, $\mathbb E[D^{2k}]=r^{-1}\int\lambda^k\,d\mu_{\rm feature}(\lambda)$; in particular $\mathbb E D^2=v$, not $rv$. The aspect ratio is $r=N/m$. As an additional normalization check, $\mathbb E D^4=v^2+r(v^2+a^4\gamma)$, so the singular-value law is nonconstant. This also supplies the positive-variance singular-law hypothesis used by the AMP degeneracy-removal argument.

Finally (8.2) is bi-orthogonally invariant: Gaussian left multiplication of $X,E$ and Gaussian right multiplication of $V,E$ preserve their joint law. The independently signed-permutation representation required by the generalized-invariance definition follows by taking an independent copy of $A_0$ and multiplying it by independent uniform signed permutations. The law is unchanged, and these permutations can be independent of any side information already independent of $A_0$. Items 1–4 are precisely the sufficient matrix conditions of the inspected Proposition D.1(b), which identifies the limiting diagonal distribution. ∎

Theorem 5 does not infer dynamics from an empirical spectral law. It verifies the additional entrywise-polynomial and independence hypotheses needed by a dynamical universality theorem. Combined with Proposition 4, the residual issue is the finite-time algorithmic embedding, rather than an unchecked Gaussian-equivalence conjecture for the RF matrix.

Independent check: B06 audited Sections 1–6 and the Section 8 matrix proof on 2026-10-24. Its cross-dimension conditioning precision was incorporated: the almost-sure source application now explicitly uses a product construction. B05 separately verified the LLC source assumptions and spectral comparison and identified the row-versus-feature singular-law convention; that normalization clarification was incorporated above.

## 9. Causal embedding of the rank-one logistic recursion in rectangular AMP

This section supplies the exact algorithmic embedding and the deterministic-overlap comparison. The Gaussian query/state recursion and the covariance-degeneracy regularization are detailed independently by B04/B01. The present formulas specify their normalization and show that no extra universality for arbitrary empirical scalar coefficients is being assumed.

Use a proportional block of additional test inputs, for example $N=2n$, and the deterministic row mask $M_i=1$ for the $n$ training rows and $0$ for the test rows. Set
\[
\pi=n/N=1/2,\quad r=N/m\to2\alpha/\gamma,\quad
\lambda= c/\alpha,\quad s=a\sqrt\gamma,\quad v=\sqrt d\,t.
\tag{9.1}
\]
Here the letter $v$ denotes the feature-side teacher vector only within this section; the scalar feature moment in earlier sections remains $\mathbb E\tanh(G)^2$. Write $w_t=\sqrt m\,b^t$. Proposition 4 reduces the normalized feature matrix to
\[
D=A_0+\frac{s}{m}zv^\top.
\]
The small differences between $(\lambda_d,s_d,r_d)$ and their limits are harmless by the same finite-time stability estimate. The exact resulting physical iteration is
\[
q_t^{\rm emp}=m^{-1}v^\top w_t,\quad
S_t=A_0w_t+s q_t^{\rm emp}z,\quad
r_t=M\odot[Y-\sigma(S_t)],
\tag{9.2}
\]
\[
\rho_t^{\rm emp}=N^{-1}z^\top r_t,\qquad
w_{t+1}=w_t+\lambda[A_0^\top r_t+s r\rho_t^{\rm emp}v],\qquad w_0=0.
\tag{9.3}
\]
The side vectors $(M,z,Y)$ and $v$ are independent of $A_0$. Their empirical laws converge to $(M,Z,Y)$ and $V$, where $M\sim\mathrm{Bernoulli}(\pi)$ is independent of $(Z,Y)$, $Z,V$ are standard Gaussian, and $Y\mid Z\sim\mathrm{Bernoulli}(\sigma(\beta Z))$. Gaussian and bounded side variables have all moments. Polynomial density follows, for example, by splitting the two finite coordinates $M,Y$ and using polynomial density under the Gaussian measure; their joint law is dominated by a constant times Gaussian measure times counting measure.

Let $a_{th},b_{th}$ be the deterministic rectangular-AMP correction coefficients prescribed by the row-normalized singular law in Theorem 5. The AMP has column fields $Z_t^{\rm A}$, row fields $Y_t^{\rm A}$, feature iterates $Q_t$, and residual iterates $R_t$:
\[
Z_t^{\rm A}=A_0^\top R_t-\sum_{h<t}b_{th}Q_h,\qquad
Y_t^{\rm A}=A_0Q_t-\sum_{h\le t}a_{th}R_h.
\tag{9.4}
\]
Initialize $Q_0=0$ and $R_1=M\odot(Y-1/2)$. Define its nonlinearities recursively by
\[
Q_t=Q_{t-1}+\lambda\left[Z_t^{\rm A}+\sum_{h<t}b_{th}Q_h+s r\rho_{t-1}V\right],
\tag{9.5}
\]
\[
R_{t+1}=M\left[Y-\sigma\!\left(Y_t^{\rm A}+\sum_{h\le t}a_{th}R_h+s q_tZ\right)\right],
\tag{9.6}
\]
where
\[
\rho_{t-1}=\mathbb E[Z R_t],\qquad q_t=\mathbb E[VQ_t]
\tag{9.7}
\]
are taken in the limiting AMP law. Each $Q_h$ in (9.5) is already a deterministic function of the past column fields and feature-side information, and each $R_h$ in (9.6) is already a deterministic function of past row fields and sample-side information. Thus these are legitimate memory-dependent coordinatewise nonlinearities.

**Causality.** Before the $t$th column update, the law of $R_t$ and hence $\rho_{t-1}$ are already known. The column field law and (9.5) then determine $Q_t$ and $q_t$. Only after this does (9.6) define $R_{t+1}$. Consequently the overlap definitions introduce no circular fixed point at a time step. The source's AMP covariance and correction-coefficient prescriptions follow the same alternating order.

**Regularity.** At a fixed horizon, (9.5) is affine in its Gaussian-field arguments. Equation (9.6) is recursively globally Lipschitz in its Gaussian-field arguments because $0\le M\le1$ and $\|\sigma'\|_\infty\le1/4$. To meet a theorem requiring definitions on the entire Euclidean side-information space, replace the formal arguments $M,Y$ by their projections onto $[0,1]$; this changes no observed value and keeps the Lipschitz constants uniform in the side arguments. All functions have at most polynomial growth. The Bernoulli sampling threshold is not an update nonlinearity: the already generated label is supplied as side information.

**Exact cancellation.** Substituting (9.4) into (9.5) cancels all $b_{th}$ corrections. Substituting (9.4) into (9.6) cancels all $a_{th}$ corrections. Thus the finite-dimensional AMP trajectory is exactly logistic GD with the scalar overlaps frozen to (9.7). These identities are algebraic and do not use a limit.

**Deterministic-overlap freezing.** Suppose the source theorem is applied to this AMP, or first to its regularized version with fresh side Gaussian perturbations as in the companion proof. Let $(\bar w_t,\bar r_t)$ denote its frozen-overlap physical iterates. Joint empirical $W_2$ convergence gives
\[
\epsilon^q_t:=|m^{-1}v^\top\bar w_t-q_t|\to0,
\qquad
\epsilon^\rho_t:=|N^{-1}z^\top\bar r_t-\rho_t|\to0,
\tag{9.8}
\]
since both products are continuous with quadratic growth. Define
\[
e_t=\|w_t-\bar w_t\|_2/\sqrt m,\quad
h_t=\|r_t-\bar r_t\|_2/\sqrt N,\quad
V_m=\|v\|_2/\sqrt m,\quad Z_N=\|z\|_2/\sqrt N.
\]
On $\|A_0\|_{\rm op}\le C$, Cauchy–Schwarz and sigmoid's derivative bound give
\[
h_t\le\frac14\left[\left(C/\sqrt r+sZ_NV_m\right)e_t+sZ_N\epsilon^q_t\right],
\tag{9.9}
\]
\[
e_{t+1}\le e_t+\lambda\left[\left(C\sqrt r+s rV_mZ_N\right)h_t+s rV_m\epsilon^\rho_t\right].
\tag{9.10}
\]
We have $e_0=0$, $V_m,Z_N\to1$, and finitely many times. Induction using (9.8) proves $\max_{t\le T}(e_t+h_t)\to0$ in probability. Differences in dimension-dependent constants add only $o_P(1)$ terms. Therefore the adaptive-overlap physical iteration has exactly the same finite-time empirical limit as the frozen AMP.

This comparison is independent of whether the source's remark on empirical Onsager coefficients includes the rank-one overlaps: it proves the required replacement directly. B05 independently checked (9.9)–(9.10) and the causal indexing.

## 10. Assembled finite-horizon theorem and its boundary

The preceding inputs, the explicit recursion in `fullproof/b01_GD_state_evolution_check.md`, and the total-variation theorem in `fullproof/b04_calibration_transfer.md` now close the arbitrary fixed finite-horizon Gaussian model. B03 independently reviewed B01's causal recursion, the query-block cancellation, positive-definiteness induction, overlap comparison, and first-step check; B04 independently checked its primary-source covariance formulas. B05/B06 independently checked the matrix inputs above.

**Theorem 6 (original Gaussian tanh GD, each fixed finite horizon).** Fix $\alpha,\gamma,c\in(0,\infty)$, $0\le\beta<\infty$, and a fixed integer $T$. Run the original model (1.1). Compute $q_{1:T},\Sigma_T$ by B01's explicit recursion (16), with $s=a\sqrt\gamma$, and put
\[
A_t=sq_t,\qquad Q_{st}=s^2q_sq_t+(\Sigma_T)_{st}.
\]
Then $\Sigma_T$ is positive definite. Conditional on the realized features and training sample, the joint fresh-test law converges weakly in probability to
\[
\bigl(Z,S_1,\ldots,S_T,Y\bigr),\qquad
S_t=A_tZ+G_t,
\quad G_{1:T}\sim N(0,\Sigma_T),\quad G\perp Z,
\quad Y\mid Z\sim\mathrm{Bernoulli}(\sigma(\beta Z)).
\tag{10.1}
\]
For every $1\le t\le T$, the conditional law of $(Z,S_t,Y)$ in fact converges in total variation in probability. The exact, unbinned, model-conditional calibration error converges in probability and every finite $L^p$ to
\[
C_t=\mathbb E_{S\sim N(0,Q_{tt})}|g_t(S)-\sigma(S)|,
\quad
 g_t(x)=\mathbb E_H\sigma\!\left(\beta\left[\frac{A_t}{Q_{tt}}x+
 \sqrt{\frac{(\Sigma_T)_{tt}}{Q_{tt}}}\,H\right]\right).
\tag{10.2}
\]
Its population logistic risk converges in $L^1$ to
\[
R_t=\mathbb E_G\log\left(2\cosh\left(\frac{\sqrt{Q_{tt}}G}{2}\right)\right)-\kappa A_t,
\qquad
\kappa=\mathbb E[Z(\sigma(\beta Z)-1/2)].
\tag{10.3}
\]
All these convergences are uniform over the finite index set $\{1,\ldots,T\}$. At time zero, $C_0=0$ and $R_0=\log2$ exactly.

**Assembly proof.** Theorem 5 and the side-information/regularity checks in Section 9 verify WZF's matrix and algorithm assumptions. B01's positive-definiteness induction verifies all of its nonsingularity assumptions without perturbation, for every $c>0$. The AMP embedding cancels the memory corrections exactly; (9.9)–(9.10) remove frozen-overlap dependence; Proposition 4 and finite-time operator stability restore the actual tanh features. On a mask-zero test row all residual iterates vanish, so the limiting score is exactly $sq_tZ+G_t$, proving (10.1) for appended test rows.

Conditional on the original training environment those appended rows are independent fresh inputs. Conditional LLNs for bounded observables therefore yield the claimed conditional test-law convergence. For the covariance identification, Gaussian concentration gives
$\mathbb E_X|S_t(X)|^4\le C\|F\|_{\rm op}^4\|b^t\|_2^4=O_P(1)$; hence conditional variances of the appended empirical quadratic averages are $O_P(N^{-1})$. This identifies the realized-model covariance limit with $Q$, including teacher covariances $A$.

Theorem 1 supplies coefficient delocalization. Since B01 proves $(\Sigma_T)_{tt}>0$, B04's deterministic smoothing theorem upgrades each conditional pair to total variation. Adding the fresh label is a common Markov kernel and contracts total variation. B04's signed-measure inequality then proves (10.2). Gaussian integration gives (10.3); uniform second-moment bounds for the scores imply uniform integrability of logistic losses and conditional risks, so the convergence is in $L^1$. Finite unions give the stated uniformity over $t\le T$. ∎

For clarity, $C_t>0$ at every positive finite time. If $\beta=0$, the regression curve is $1/2$ and the score is nondegenerate. If $\beta>0$ and $A_t\le0$, monotonicity prevents $g_t$ from equaling the increasing sigmoid. If $A_t>0$, dominated convergence gives
\[
1-g_t(x)\sim
\exp\!\left[-\frac{\beta A_t}{Q_{tt}}x+
\frac{\beta^2(\Sigma_T)_{tt}}{2Q_{tt}}\right]
\quad(x\to\infty).
\]
Equality with $1-\sigma(x)\sim e^{-x}$ would require both $\beta A_t/Q_{tt}=1$ and $(\Sigma_T)_{tt}=0$, contradicting positive definiteness. Continuity and the everywhere-positive score density turn nonidentity into strictly positive calibration error.

For any training-dependent stopping time $\tau_d\in\{0,\ldots,T\}$, the realized population risk and calibration are approximated, in probability, by $R_{\tau_d}$ and $C_{\tau_d}$. If the deterministic finite-grid risk has a unique minimizer, every minimizer of the realized population risk on that grid converges to it in probability. Minimizing calibration alone includes the exact zero-score solution at time zero. No monotonicity of the risk or calibration curve is asserted.

This theorem concerns every fixed finite horizon, at arbitrary positive finite aspect ratios and step size. It does not, by itself, identify an infinite-time limit or optimize over an unbounded stopping horizon. The companion `fullproof/b02_uniform_time_GD.md` gives an additional all-time result under its explicitly stated sample-ratio and small-step assumptions; those hypotheses must remain visible whenever that extension is used.
