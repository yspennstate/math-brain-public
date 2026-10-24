# Gaussian tanh random features: a first-GD-step joint limit

Author: A26. Date: 2026-10-23. Status: **complete proof of the first-step joint CLT and its two-test-replica extension, independently audited PASS by A28**. The audit is recorded separately in T357_gaussian_first_step_independent_review.md. The replica extension proves concentration of bounded population test statistics and population logistic risk over training data and random features. This is a new followup and changes no frozen report. It does not prove a full GD trajectory theorem, exact convergence of conditional calibration error, or an almost-sure conditional limit.

## 1. Model and normalization

For each dimension, let $X_0,X_1,\ldots,X_n$ be independent $N(0,I_d)$ inputs, let $\theta_d$ be deterministic with $\|\theta_d\|=1$, and put $Z_i=\theta_d^\top X_i$. Conditional on the inputs, independently draw

\[
Y_i\sim\operatorname{Bernoulli}(\sigma(\beta Z_i)),\qquad
R_i=Y_i-\tfrac12,\qquad \beta\ge0.
\]

The fresh test label $Y_0$ is not used in training. Let $W_1,\ldots,W_m$ be independent $N(0,I_d/d)$ vectors, independent of the data. Write $\phi=\tanh$, $h_j(x)=\phi(W_j^\top x)$, and

\[
K_m(x,x')=\frac1m\sum_{j=1}^m h_j(x)h_j(x').
\]

One exact network convention is

\[
f_a(x)=\frac1{\sqrt m}\sum_{j=1}^m a_j h_j(x).
\]

Train only its output weights from $a=0$, using the **mean** logistic loss and learning rate $cd$, with fixed $c>0$. Direct differentiation gives

\[
a_j^1=\frac{cd}{n\sqrt m}\sum_{i=1}^nR_i h_j(X_i),\qquad
S_{1,d}=f_{a^1}(X_0)=\frac{cd}{n}\sum_{i=1}^nR_iK_m(X_0,X_i). \tag{1}
\]

Equation (1) is the invariant normalization used below. With the unnormalized readout $\sum_j a_jh_j$, the equivalent mean-loss step is $cd/m$. With readout $m^{-1}\sum_j a_jh_j$, it is $cdm$. These conventions must not be mixed.

Assume

\[
n/d\longrightarrow\alpha\in(0,\infty),\qquad
m/d\longrightarrow\gamma\in(0,\infty).
\]

Define, for a standard normal $G$,

\[
a_1=\mathbb E[G\phi(G)]=\mathbb E[\phi'(G)],\qquad
v=\mathbb E[\phi(G)^2],\qquad
\nu=v-a_1^2,
\]
\[
\kappa=\mathbb E[G\{\sigma(\beta G)-\tfrac12\}]
=\beta\mathbb E[\sigma'(\beta G)]. \tag{2}
\]

For tanh, $a_1=1-v>0$ and $\nu\ge0$. Throughout this note $v$ is the **full** feature second moment, not the nonlinear Hermite residual $\nu$. Confusing these gives the wrong finite-width variance.

## 2. The theorem

**Theorem.** Under the model above, jointly over the random features, training sample, and fresh test input,

\[
(Z_0,S_{1,d})\ \Longrightarrow\
\left(Z,\;c a_1^2\kappa Z+c\tau G\right), \tag{3}
\]

where $Z,G$ are independent standard normal variables and

\[
\boxed{\quad
\tau^2=\frac{\kappa^2a_1^2v}{\gamma}
+\frac{a_1^4+v^2/\gamma}{4\alpha}.
\quad} \tag{4}
\]

The convergence in (3) is **annealed**: it averages over training data and random features. The following stronger statement also holds. For two independent fresh test inputs, with independent fresh labels conditional on their teacher scores and with the **same** training sample and features, the corresponding two triples $(Z_0,S_{1,d},Y_0)$ converge jointly to independent copies of the limit above. Consequently, for every bounded measurable test function that is continuous almost surely under that limit, its population test expectation conditional on the realized trained network converges in $L^2$ over training data and random features to the deterministic limiting expectation. This is a conditional test-law conclusion **in probability**, not an almost-sure quenched assertion. Section 8 proves the replica extension and spells out its quantifiers.

In particular, the covariance matrix of the limit is

\[
\begin{pmatrix}
1 & c a_1^2\kappa\\
c a_1^2\kappa &
c^2a_1^4\kappa^2+
c^2\kappa^2a_1^2v/\gamma+
c^2(a_1^4+v^2/\gamma)/(4\alpha)
\end{pmatrix}. \tag{5}
\]

Moreover, $\sup_d\mathbb E S_{1,d}^2<\infty$. The conditional population logistic risk of the realized trained network converges in $L^1$ over training data and random features to the risk of (3); in particular its expectation converges. Adding the fresh label gives joint convergence to $Y\mid Z\sim\operatorname{Bernoulli}(\sigma(\beta Z))$, conditionally independent of $G$ given $Z$.

The three residual-variance contributions are:

| Contribution to $\tau^2$ | Origin |
|---|---|
| $a_1^4/(4\alpha)$ | Training-sample noise remaining at infinite width |
| $\kappa^2a_1^2v/\gamma$ | Finite-width fluctuation of the population first-step signal |
| $v^2/(4\alpha\gamma)$ | Additional training noise caused by finite width |

The proof below conditions on the features and test input before averaging over the training examples. In that decomposition the first and third rows appear together as one conditional training variance. No assertion that individual higher-Hermite feature coordinates are independent is used.

## 3. Gaussian tools used in the proof

All uses are finite-dimensional.

1. **Odd Hermite covariance identity.** If $(G_1,G_2)$ are standard jointly Gaussian with correlation $\rho$, expansion in orthonormal Hermite polynomials gives
   \[
   \mathbb E[f(G_1)g(G_2)]=\sum_{\ell\ge0}f_\ell g_\ell\rho^\ell.
   \]
   For odd functions, only odd degrees occur. After removing degree one, Cauchy–Schwarz bounds the remainder by $|\rho|^3\|f\|_2\|g\|_2$.
2. **Gaussian Poincaré inequality.** For a centered differentiable $L$-Lipschitz function $f$ of a standard Gaussian vector, $\mathbb Ef^2\le L^2$. Applying Poincaré again to $f^2$ yields
   \[
   \mathbb Ef^4=\operatorname{Var}(f^2)+(\mathbb Ef^2)^2
   \le4L^2\mathbb Ef^2+L^4\le5L^4. \tag{6}
   \]
   The Poincaré inequality follows directly by comparing Hermite coefficients of $f$ and its gradient.
3. **Elementary Gaussian matrix estimates.** If $F$ has rows $W_j^\top$, then $\|F\|_{\rm op}=O_P(1)$ and its fixed moments are uniformly bounded when $m/d$ is bounded. A net argument proves this: for fixed unit $u,v$, $u^\top Fv$ is normal with variance $1/d$; take $1/4$-nets of the two unit spheres and use their exponential cardinality and the Gaussian tail. Also
   \[
   \max_{j\le m}|\|W_j\|^2-1|\to0
   \]
   in probability, by a chi-square Chernoff bound and a union bound.
4. The ordinary triangular-array CLT can be applied conditionally when the conditional variance converges and the sum of conditional fourth moments tends to zero. Equivalently, expand the conditional characteristic functions and multiply them; the fourth-moment bound controls the Taylor remainder.

These are the only general probabilistic ingredients. The model-specific mean and variance limits are established next.

## 4. Feature covariance: higher Hermite terms vanish in operator norm

Let

\[
\Sigma_F=\mathbb E_X[h(X)h(X)^\top],\qquad
q_j=\|W_j\|^2,\qquad
A(q)=\mathbb E[\phi'(\sqrt q\,G)],\quad
V(q)=\mathbb E[\phi(\sqrt q\,G)^2].
\]

**Lemma 1.**

\[
\left\|\Sigma_F-\{a_1^2FF^\top+\nu I_m\}\right\|_{\rm op}\to0
\quad\text{in probability}. \tag{7}
\]

**Proof.** Conditional on $F$, $(W_j^\top X,W_\ell^\top X)$ is Gaussian. Its degree-one Hermite covariance is

\[
A(q_j)A(q_\ell)\,W_j^\top W_\ell.
\]

For $j\ne\ell$, the remaining covariance has absolute value at most
$|\rho_{j\ell}|^3$, with $\rho_{j\ell}=W_j^\top W_\ell/\sqrt{q_jq_\ell}$. Independent uniform directions on the sphere satisfy

\[
\mathbb E|\rho_{j\ell}|^6=\frac{15}{d(d+2)(d+4)}.
\]

Therefore the squared Frobenius norm of the off-diagonal remainder has expectation at most

\[
\frac{15m(m-1)}{d(d+2)(d+4)}=O(d^{-1}).
\]

Thus the off-diagonal remainder vanishes in operator norm. The diagonal is represented exactly by
$V(q_j)-q_jA(q_j)^2$. Uniform concentration of the row norms makes this converge uniformly to $\nu$ and $A(q_j)$ uniformly to $a_1$. Combining this with $\|F\|_{\rm op}=O_P(1)$ proves (7). ∎

This lemma is where oddness matters: a degree-two remainder would not have the same simple vanishing Frobenius bound.

## 5. Exact test-feature quadratic form

Let $h=h(X_0)$. Then

\[
\frac d{m^2}h^\top\Sigma_Fh
\ \longrightarrow\ a_1^4+\frac{v^2}{\gamma}
\quad\text{in probability}. \tag{8}
\]

To prove this, put $r=\|X_0\|/\sqrt d$ and $u=X_0/\|X_0\|$. Conditional on $X_0$, write

\[
W_j=\frac1{\sqrt d}(G_ju+g_{j,\perp}),\qquad
h_j=\phi(rG_j),
\]

where the $G_j$ and the orthogonal Gaussian vectors are independent. Consequently,

\[
\|F^\top h\|^2
\ \stackrel{\rm law}{=}\
\frac1d\left(\sum_jG_jh_j\right)^2
+\frac1d\left(\sum_jh_j^2\right)\chi^2_{d-1}, \tag{9}
\]

where the chi-square variable is independent of the $G_j$, conditional on $X_0$. The law of large numbers, $r\to1$, and chi-square concentration imply

\[
\frac d{m^2}\|F^\top h\|^2\to a_1^2+\frac v\gamma,\qquad
\frac d{m^2}\|h\|^2\to\frac v\gamma. \tag{10}
\]

The error in using (7) is at most
$d\|h\|^2m^{-2}\,o_P(1)=o_P(1)$ because $|h_j|\le1$. Substitute (10):

\[
a_1^2(a_1^2+v/\gamma)+\nu v/\gamma
=a_1^4+v^2/\gamma.
\]

In particular, replacing the actual RF covariance by only its linear Hermite term would omit part of the finite-width training noise.

## 6. Population first-step signal and its finite-width CLT

Define the exact one-feature response

\[
B(w)=\mathbb E_X[(\sigma(\beta\theta_d^\top X)-\tfrac12)
                 \phi(w^\top X)].
\]

Conditionally on $F,X_0$, the training-averaged score is

\[
M_d=\mathbb E[S_{1,d}\mid F,X_0]
=\frac{cd}{m}\sum_j h_j B(W_j). \tag{11}
\]

Let $t_j=\theta_d^\top W_j$. Applying the odd Hermite identity to the teacher link and feature gives

\[
B(W_j)=\kappa A(q_j)t_j+\varepsilon_j,\qquad
|\varepsilon_j|\le\frac12\left|\frac{t_j}{\sqrt{q_j}}\right|^3. \tag{12}
\]

The bound follows because the teacher link has $L^2$ norm at most $1/2$, the feature has $L^2$ norm at most one, and their Gaussian correlation is $t_j/\sqrt{q_j}$. The event $q_j=0$ has probability zero. By the same spherical moment identity,
$\mathbb E(t_j/\sqrt{q_j})^6=15/[d(d+2)(d+4)]$. Cauchy–Schwarz for the feature average therefore gives

\[
\mathbb E\left|\frac{cd}{m}\sum_jh_j\varepsilon_j\right|^2
\le c^2d^2\,\mathbb E\varepsilon_1^2=O(d^{-1}),
\]

so the remainder in (11) tends to zero in $L^2$ without any exceptional-row-norm restriction.

The radial coefficient may also be replaced by $a_1$:

\[
\frac d m\sum_jh_jt_j\{A(q_j)-a_1\}\to0
\quad\text{in }L^2. \tag{13}
\]

Here is the needed cancellation; a maximum-error bound alone would be insufficient. Gaussian variance differentiation gives
$A'(q)=\frac12\mathbb E[\phi'''(\sqrt qG)]$, which is bounded for tanh. Thus
$\mathbb E[t_j^2\{A(q_j)-a_1\}^2]=O(d^{-2})$; explicitly,
$\mathbb E[t_j^2(q_j-1)^2]=(2d+8)/d^3$.
Conditional on $X_0=x$, Gaussian integration by parts yields

\[
\mathbb E_W[t\{A(q)-a_1\}\phi(W^\top x)]
=\frac1d\mathbb E_W[
2tA'(q)\phi(W^\top x)
+(\theta_d^\top x)\{A(q)-a_1\}\phi'(W^\top x)].
\]

Its magnitude is $O((1+|\theta_d^\top x|)d^{-3/2})$. Conditional independence across $j$ now proves (13).

Therefore

\[
M_d=c\kappa a_1 T_d+o_{L^2}(1),\qquad
T_d=\frac d m\sum_j t_j\phi(W_j^\top X_0). \tag{14}
\]

For completeness the limit of $T_d$ can be computed without a generic RF Gaussian-equivalence assertion. Conditional on $X_0=x$, put $z=\theta_d^\top x$ and $r=\|x\|/\sqrt d$. The decomposition along $u=x/\|x\|$ gives independent standard normals $G_j,H_j$ such that

\[
t_j=\frac1{\sqrt d}\left[
\frac z{\|x\|}G_j+
\sqrt{1-z^2/\|x\|^2}\,H_j\right].
\]

It follows that

\[
T_d=
\frac z r\,\frac1m\sum_jG_j\phi(rG_j)
+\frac{\sqrt d}{m}\sqrt{1-z^2/\|x\|^2}
       \sum_jH_j\phi(rG_j). \tag{15}
\]

Conditionally on $x,G_1,\ldots,G_m$, the second term is exactly Gaussian, with variance

\[
\frac d{m^2}(1-z^2/\|x\|^2)\sum_j\phi(rG_j)^2\to v/\gamma.
\]

The first term tends to $a_1Z_0$. Hence

\[
(Z_0,M_d)\Longrightarrow
\left(Z,\;ca_1^2\kappa Z+
c\kappa a_1\sqrt{v/\gamma}\,G_{\rm width}\right), \tag{16}
\]

with independent standard normals. The finite-width signal fluctuation is present even as $\alpha\to\infty$.

Also $\sup_d\mathbb EM_d^2<\infty$. One can see this directly from (14): conditional on $X_0=x$, the variance of $T_d$ is at most $d/m$, while
$|\mathbb E[T_d\mid X_0=x]|\le|\theta_d^\top x|\,\|\phi'\|_\infty$ by Gaussian integration by parts.

## 7. Conditional training CLT and independence

Conditional on $F,X_0$, set

\[
\xi_i=R_iK_m(X_0,X_i)
-\mathbb E[R_iK_m(X_0,X_i)\mid F,X_0].
\]

These variables are iid and centered. The identity $R_i^2=1/4$ holds exactly, despite the informative teacher. Thus

\[
\operatorname{Var}(S_{1,d}-M_d\mid F,X_0)
=\frac{c^2d^2}{n}\left[
\frac1{4m^2}h^\top\Sigma_Fh-
\left(\frac{M_d}{cd}\right)^2\right]
\to\frac{c^2}{4\alpha}(a_1^4+v^2/\gamma). \tag{17}
\]

The subtracted term is $M_d^2/n=o_P(1)$.

For the conditional Lyapunov estimate, view $K(X)=K_m(X_0,X)$ as a function of the Gaussian training input. It is odd and centered, and has Lipschitz constant at most

\[
L_F=\frac{\|F\|_{\rm op}\|\phi'\|_\infty\|h\|}{m}
\le\frac{\|F\|_{\rm op}}{\sqrt m}.
\]

By (6), $\mathbb E[K(X)^4\mid F,X_0]\le5L_F^4$.
Since $|R_i|=1/2$, centering changes this bound by only an absolute factor. Consequently,

\[
\sum_{i=1}^n\mathbb E\left[
\left|\frac{cd}{n}\xi_i\right|^4\middle|F,X_0\right]
=O_P\!\left(\frac{d^4}{n^3m^2}\right)=O_P(d^{-1})\to0. \tag{18}
\]

The conditional CLT gives the following stronger form needed for independence: for every fixed real $s$,

\[
\mathbb E[e^{is(S_{1,d}-M_d)}\mid F,X_0]
\ \longrightarrow\
\exp\!\left[-\frac{s^2c^2}{8\alpha}(a_1^4+v^2/\gamma)\right]
\]

in probability. Since these characteristic functions are bounded, convergence also holds in $L^1$. Multiplying by any bounded function of $(Z_0,M_d)$ and taking expectations proves asymptotic independence of the training Gaussian from the joint limit in (16). Adding the independent variances proves (3)–(5).

Finally, the conditional training variance is bounded in expectation by

\[
\frac{c^2d^2}{4n}\mathbb E K(X)^2
\le\frac{c^2d^2}{4nm}\mathbb E\|F\|_{\rm op}^2=O(1).
\]

Together with the $L^2$ bound for $M_d$, this proves $\sup_d\mathbb ES_{1,d}^2<\infty$. Logistic loss is continuous and bounded by $\log2+|S_{1,d}|$, so it is uniformly integrable. The risk-transfer claim follows. The test-label claim follows by conditioning on $Z_0$, because its conditional success probability is the bounded continuous function $\sigma(\beta Z_0)$. ∎

## 8. Two independent test points with shared training and features

Let $X_0^{(1)},X_0^{(2)}$ be independent fresh $N(0,I_d)$ inputs, independent of the common training sample and $F$. Write $h_a=h(X_0^{(a)})$, $Z_a=\theta_d^\top X_0^{(a)}$, $S_d^{(a)}=f_{a^1}(X_0^{(a)})$, and $M_d^{(a)}=\mathbb E[S_d^{(a)}\mid F,X_0^{(1)},X_0^{(2)}]$. The last expectation is only over training data. The two fresh labels $Y_0^{(1)},Y_0^{(2)}$ are independent given their teacher scores and are not used in training.

**Replica theorem.**

\[
\bigl(Z_a,S_d^{(a)},Y_0^{(a)}\bigr)_{a=1,2}
\ \Longrightarrow\
\bigl(Z_a,\;c a_1^2\kappa Z_a+c\tau G_a,\;Y_a\bigr)_{a=1,2}, \tag{19}
\]

where $(Z_1,G_1,Y_1)$ and $(Z_2,G_2,Y_2)$ are independent triples, $Z_a,G_a$ are independent standard normals, and
$Y_a\mid Z_a\sim\operatorname{Bernoulli}(\sigma(\beta Z_a))$ independently of $G_a$ given $Z_a$.

### 8.1 Cross-covariance of the training noise

The needed cross quadratic form vanishes:

\[
C_d=\frac d{m^2}h_1^\top\Sigma_Fh_2\longrightarrow0
\quad\text{in probability}. \tag{20}
\]

Indeed, conditional on $F$, the vectors $h_1,h_2$ are independent and centered, each with covariance $\Sigma_F$. Hence the exact identity

\[
\mathbb E[C_d^2\mid F]
=\frac{d^2}{m^4}\operatorname{tr}(\Sigma_F^4)
\le\frac{d^2}{m^3}\|\Sigma_F\|_{\rm op}^4 \tag{21}
\]

holds. Lemma 1 gives $\|\Sigma_F\|_{\rm op}=O_P(1)$, and $d^2/m^3=O(d^{-1})$. Conditional Chebyshev on the event $\|\Sigma_F\|_{\rm op}\le B$, followed by first $d\to\infty$ and then $B\to\infty$, proves (20). No assumption that the two feature vectors are independent without conditioning on $F$ is made.

Conditionally on $F,X_0^{(1)},X_0^{(2)}$, the vector training summands are iid. Their score cross-covariance is

\[
\operatorname{Cov}(S_d^{(1)}-M_d^{(1)},S_d^{(2)}-M_d^{(2)}
\mid F,X_0^{(1)},X_0^{(2)})
=\frac{c^2d}{4n}C_d-\frac{M_d^{(1)}M_d^{(2)}}n
\longrightarrow0. \tag{22}
\]

Each diagonal conditional variance has limit (17). For any fixed real coefficients $u_1,u_2$, the linear-combination kernel
$u_1K_m(X_0^{(1)},X)+u_2K_m(X_0^{(2)},X)$ is odd and has Lipschitz constant at most
$\|F\|_{\rm op}(|u_1|+|u_2|)/\sqrt m$. The fourth-moment calculation (18) applies unchanged. Cramér–Wold therefore proves a conditional bivariate Gaussian limit with independent coordinates, each having variance $c^2(a_1^4+v^2/\gamma)/(4\alpha)$. Its conditional characteristic function converges in probability and in $L^1$ to that deterministic Gaussian characteristic function. In particular, the limiting training-noise vector is independent of the limiting population-mean vector and teacher scores.

### 8.2 Cross-covariance of the finite-width population fluctuations

The $L^2$ approximation (14) applies to each of the two test inputs, so it suffices to study

\[
T_d^{(a)}=\frac d m\sum_{j=1}^m
(\theta_d^\top W_j)\phi(W_j^\top X_0^{(a)}),\qquad a=1,2.
\]

Condition on $X_0^{(1)}=x_1,X_0^{(2)}=x_2$. The feature rows are iid. For one row, write
$H=\sqrt d\,\theta_d^\top W$ and $U_a=W^\top x_a$. This is a centered Gaussian triple with

\[
\operatorname{Var}H=1,\quad
\operatorname{Var}U_a=\|x_a\|^2/d,\quad
\operatorname{Cov}(H,U_a)=z_a/\sqrt d,\quad
\operatorname{Cov}(U_1,U_2)=x_1^\top x_2/d. \tag{23}
\]

For the random fresh inputs, their norms divided by $\sqrt d$ tend to one, $x_1^\top x_2/d\to0$, and $z_a/\sqrt d\to0$ in probability. Thus this conditional Gaussian triple tends in distribution to three independent standard normals. Since $\phi$ is bounded and the marginal $H$ is standard normal in every dimension, the quantities $H^2\phi(U_a)\phi(U_b)$ are uniformly integrable. Consequently, in probability over the test inputs,

\[
d\,\mathbb E_W[
(\theta_d^\top W)^2\phi(W^\top x_a)\phi(W^\top x_b)]
\longrightarrow v\,\mathbf1_{\{a=b\}}. \tag{24}
\]

Gaussian integration by parts gives the exact conditional row mean

\[
\mathbb E_W[(\theta_d^\top W)\phi(W^\top x_a)]
=\frac{z_a}{d}\,A(\|x_a\|^2/d). \tag{25}
\]

After multiplying the sample average by $d$, these means converge to $a_1z_a$. The product of the row means contributes $o_P(1)$ to the covariance of $T_d$, since it is multiplied by $d^2/m$ and $z_1,z_2=O_P(1)$. Equations (24)–(25) therefore imply that the centered conditional covariance matrix of $(T_d^{(1)},T_d^{(2)})$ converges to $(v/\gamma)I_2$.

For any fixed linear combination of the two coordinates, boundedness of $\phi$ and $\mathbb E(\theta_d^\top W)^4=3/d^2$ give a fourth-moment Lyapunov bound

\[
m\left(\frac d m\right)^4 O(d^{-2})
=O(d^2/m^3)=O(d^{-1}). \tag{26}
\]

The conditional feature-row CLT thus yields

\[
(Z_1,Z_2,M_d^{(1)},M_d^{(2)})
\Longrightarrow
(Z_1,Z_2,\;
c a_1^2\kappa Z_1+c\kappa a_1\sqrt{v/\gamma}\,G_{w,1},\;
c a_1^2\kappa Z_2+c\kappa a_1\sqrt{v/\gamma}\,G_{w,2}), \tag{27}
\]

where $Z_1,Z_2,G_{w,1},G_{w,2}$ are independent standard normals; each limiting population mean has the displayed dependence on its respective teacher score. The independence follows from convergence in $L^1$ of the conditional characteristic functions to a constant, exactly as in Section 7.

Combining (22), (27), and the conditional training CLT proves the score part of (19). Conditioning the fresh labels on $(Z_1,Z_2)$ proves its label part. ∎

### 8.3 Conditional population statistics and risk

Let $\mathcal T_d$ denote the sigma-field generated by the training sample and features. For a fixed bounded measurable function $f(z,s,y)$ whose discontinuity set has probability zero under the limiting triple $(Z,S,Y)$, define

\[
Q_d(f)=\mathbb E[f(Z_0,S_{1,d},Y_0)\mid\mathcal T_d],
\qquad Q(f)=\mathbb E f(Z,S,Y).
\]

The one-test CLT gives $\mathbb E Q_d(f)\to Q(f)$. Conditional independence of the two fresh tests gives

\[
\mathbb E Q_d(f)^2
=\mathbb E[
f(Z_1,S_d^{(1)},Y_0^{(1)})f(Z_2,S_d^{(2)},Y_0^{(2)})]
\longrightarrow Q(f)^2 \tag{28}
\]

by (19). Thus

\[
Q_d(f)\longrightarrow Q(f)\quad\text{in }L^2
\text{ over training data and features}. \tag{29}
\]

Here $f$ is real-valued; the complex case follows by separating real and imaginary parts. Statement (29) is for each fixed admissible $f$. It asserts neither simultaneous convergence for all measurable $f$ nor total-variation convergence of the conditional test laws.

For logistic loss $\ell(y,s)=\log(1+e^s)-ys$, apply (29) first to $\min\{\ell,B\}$. The already established bound $\sup_d\mathbb E S_{1,d}^2<\infty$, together with $0\le\ell\le\log2+|s|$, implies

\[
\sup_d\mathbb E[\ell(Y_0,S_{1,d})
\mathbf1_{\{\ell(Y_0,S_{1,d})>B\}}]=O(B^{-1}). \tag{30}
\]

The same bound holds for the limit. Truncation, (29), and the triangle inequality therefore give the stronger risk conclusion

\[
\mathbb E\left|
\mathbb E[\ell(Y_0,S_{1,d})\mid\mathcal T_d]
-\mathbb E\ell(Y,S)\right|\longrightarrow0. \tag{31}
\]

In particular the realized network's population logistic risk converges in probability to the deterministic Gaussian-model risk. This conclusion uses the replica theorem; the one-test annealed CLT alone would not justify it.

## 9. Checks, interpretation, and remaining work

Several coefficient checks do not require any simulation.

- As $\gamma\to\infty$, the score becomes the first-step linear-kernel statistic, with residual variance $c^2a_1^4/(4\alpha)$.
- As $\alpha\to\infty$, finite-width signal noise $c^2\kappa^2a_1^2v/\gamma$ remains.
- For pure-noise labels, $\kappa=0$, but both training-noise terms remain.
- Formally substituting the linear activation constants $a_1=v=1$ gives residual variance $c^2\{\kappa^2/\gamma+(1+1/\gamma)/(4\alpha)\}$, matching the direct Wishart calculation. The bounded-activation proof above is for tanh; this check is not an appeal to that proof for an unbounded activation.
- At $\beta=2$, $\sigma(2z)-1/2=\tfrac12\tanh z$, so $\kappa=a_1/2$ exactly.

The limit in (3) has a logistic-normal conditional calibration curve. With $A=ca_1^2\kappa$ and $Q=A^2+c^2\tau^2$ it is

\[
\mathbb E[Y\mid S=s]=
\mathbb E_G\sigma\!\left(\beta\left[
\frac A Qs+\sqrt{1-A^2/Q}\,G\right]\right). \tag{32}
\]

Equation (32) describes the **limiting Gaussian model**. The two-replica result proves conditional test-law convergence in the precise bounded-observable sense (29). It does not by itself establish convergence of the finite-dimensional conditional calibration curves or their $L^1$ errors.

A bounded-statistic consequence is available without convergence of those conditional calibration curves. Write $P_d=\sigma(S_{1,d})$, and define the population calibration error of the realized predictor by

\[
\mathrm{CE}_d(\mathcal T_d)=
\mathbb E\!\left[
\left|\mathbb E[Y_0\mid P_d,\mathcal T_d]-P_d\right|
\middle|\mathcal T_d\right].
\]

Because sigmoid is one-to-one, every measurable witness $w(S_{1,d})$ is measurable with respect to $P_d$. Hence, for every fixed measurable $w$ with $|w|\le1$,

\[
\mathrm{CE}_d(\mathcal T_d)\ge
\left|\mathbb E[(Y_0-\sigma(S_{1,d}))w(S_{1,d})
\mid\mathcal T_d]\right|. \tag{33}
\]

Take, for example, $w(s)=\operatorname{sign}(s)$. The limiting score has a positive variance and no mass at zero, so (29) applies and proves that, for every $\varepsilon>0$,

\[
\mathbb P\!\left\{
\mathrm{CE}_d(\mathcal T_d)\ge
\left|\mathbb E[(Y-\sigma(S))\operatorname{sign}(S)]\right|
-\varepsilon\right\}\longrightarrow1. \tag{34}
\]

More generally let $g(s)$ be the continuous limiting calibration curve in (32). The continuous bounded witnesses
$w_k(s)=\tanh(k\{g(s)-\sigma(s)\})$ satisfy

\[
\mathbb E[(Y-\sigma(S))w_k(S)]
\longrightarrow\mathbb E|g(S)-\sigma(S)|
=:\mathrm{CE}_\infty. \tag{35}
\]

For any $\varepsilon>0$, choose a fixed sufficiently large $k$ and then apply (29) and (33). This yields

\[
\mathbb P\{\mathrm{CE}_d(\mathcal T_d)
\ge\mathrm{CE}_\infty-\varepsilon\}\longrightarrow1. \tag{36}
\]

The order is fixed $k$ first, then $d\to\infty$; no uniform-in-$k$ limit is assumed. Thus the Gaussian-model calibration error is a rigorous **lower bound in probability**, not a claimed exact limit. A separate consequence note is being developed by A29, including evaluation of the signed statistic and positivity of the limiting calibration gap.

The remaining mathematical work includes full calibration-functional convergence, an almost-sure conditional test-law version if desired, and more than one GD step. At later steps the weights depend nonlinearly on the same feature matrix and labels; the conditional iid decomposition used here no longer applies in this form. None of those gaps should be filled by labeling a static ridge Gaussian-equivalence calculation as a proof of the GD trajectory.
