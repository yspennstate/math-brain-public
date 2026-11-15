# A test-risk reduction for uncentered ReLU random features

Only the output layer is trained. The result removes the nonlinear test-kernel terms while retaining the original training kernel in the flow. It does not identify a deterministic limiting risk curve or its extrema.

## 1. Model and statements

Let $n,d,m\to\infty$, with $d/n\to\gamma\in(0,\infty)$ and $m/n^2\to\infty$. Independently sample $x_1,\ldots,x_n,w_1,\ldots,w_m\sim N(0,I_d)$, and let $X$ have rows $x_i^T$. Put
\[
 \sigma(z)=\max(z,0),\qquad
 f_a(x)=\frac1{\sqrt m}\sum_{r=1}^m a_r\sigma(w_r^Tx/\sqrt d).
\]
Train $a$ from zero by gradient flow for $\frac12\sum_i(f_a(x_i)-y_i)^2$. Let $\beta,\varepsilon$ be independent of each other and of $X,W$, with
\[
 \beta\sim N(0,(E/d)I_d),\qquad
 \varepsilon\sim N(0,s^2I_n),\qquad y=X\beta+\varepsilon,
 \quad E,s^2\geq0.
\]
The realized test risk is
\[
 R_m(t)=s^2+\|f_{a(t)}-x^T\beta\|_{L^2(N(0,I_d))}^2.
\]
The test noise in this definition is independent, centered, and has variance $s^2$.

Define
\[
 \Phi_{ir}=m^{-1/2}\sigma(w_r^Tx_i/\sqrt d),\quad K_m=\Phi\Phi^T,
 \quad H_t(K)=\int_0^t e^{-uK}\,du,\quad b_m(t)=H_t(K_m)y.
 \tag{1}
\]
These definitions of $H_t$ apply also to singular matrices. Introduce the test kernel
\[
 k_m(x)_i=\frac1m\sum_r\sigma(w_r^Tx_i/\sqrt d)\sigma(w_r^Tx/\sqrt d),
 \quad k_\infty(x)_i=\mathbb E_W k_m(x)_i,
\]
and the training kernel $K_\infty=(k_\infty(x_j)_i)_{ij}$. For any vector-valued function $k$, write $\mathcal T_k b=k(x)^Tb$, a map from $\mathbb R^n$ to Gaussian $L^2$.

For nonzero training points put
\[
 a_i=\|x_i\|/\sqrt d,\quad u_i=x_i/\|x_i\|,\quad
 a=(a_i)_{i=1}^n,\quad a(x)=\|x\|/\sqrt d.
\]
Zero training points have probability zero and may be omitted. For $U$ uniform on $S^{d-1}$, define
\[
 h_d=\mathbb E(U_1)_+
   =\frac{\Gamma(d/2)}{2\sqrt\pi\,\Gamma((d+1)/2)},\qquad
 \mu_d=d h_d^2.
 \tag{2}
\]
Here and below $d\geq2$ suffices.

**Test-operator lemma.** There is an exact decomposition
\[
 k_\infty(x)=\frac{Xx}{4d}+\mu_d a\,a(x)+e_X(x).
 \tag{3}
\]
Every component of $e_X$ is even in $x$ and orthogonal to $a(x)$ in Gaussian $L^2$. In particular it is also orthogonal to every linear function. Set
\[
 C_4=\frac{\pi-3}{4\pi}>0.
\]
For every fixed nonzero training design,
\[
 \|\mathcal T_{e_X}\|_{\rm op}
 \leq \frac1{4\pi}\sqrt{\frac2{d(d+2)}}\frac{\|X\|_{\rm op}}{\sqrt d}
 +C_4\sqrt{\frac{105\sum_i a_i^2}{d(d+2)(d+4)(d+6)}}.
 \tag{4}
\]
For the Gaussian design this is $O_{\mathbb P}(d^{-1})$. Also
\[
 \mu_d=\frac1{2\pi}+\frac1{4\pi d}+O(d^{-2}).
 \tag{5}
\]

**Flow consequence.** With the finite-width model above,
\[
 \sup_{t\geq0}\left|
 R_m(t)-s^2-
 \left\|\frac{X^Tb_m(t)}{4d}-\beta\right\|^2
 \right|\xrightarrow{\mathbb P}0.
 \tag{6}
\]
The same assertion holds with $m=\infty$, $K_m$ replaced by $K_\infty$, and the predictor defined as $k_\infty(x)^TH_t(K_\infty)y$.

The matrix in $b_m(t)$ in (6) is the **original nonlinear training kernel**. Replacing it with $XX^T/(4d)+cI$ is not a conclusion of this result. Thus (6) is a test-risk reduction, not a deterministic equivalent for $R_m$.

## 2. The exact ReLU kernel and its angular mean

For unit vectors $u,v$, write $\rho=u^Tv$ and $\theta=\arccos\rho$. A standard Gaussian projected onto their plane has polar representation $R(\cos\varphi,\sin\varphi)$, with $\varphi$ uniform on $[0,2\pi)$, independent of $R$, and $\mathbb E R^2=2$. The two positive half-planes intersect on $[\theta-\pi/2,\pi/2]$. Consequently
\[
 \mathbb E_w\sigma(w^Tu)\sigma(w^Tv)
 =\frac1\pi\int_{\theta-\pi/2}^{\pi/2}
        \cos\varphi\cos(\varphi-\theta)\,d\varphi
 =\frac{\sin\theta+(\pi-\theta)\cos\theta}{2\pi}.
\]
The last equality follows by integrating
$\cos\varphi\cos(\varphi-\theta)=[\cos\theta+\cos(2\varphi-\theta)]/2$.
The formula extends to $\rho=\pm1$ by continuity. Equivalently,
\[
 k_\infty(x)_i=a_i a(x)
  \left[\frac{u_i^Tu}{4}+\psi(u_i^Tu)\right],\quad
 u=x/\|x\|,
\]
\[
 \psi(z)=\frac{\sqrt{1-z^2}+z\arcsin z}{2\pi}.
 \tag{7}
\]
The first term is exactly $x_i^Tx/(4d)$. The function $\psi$ is even. Its values and derivatives give
\[
 \psi(0)=\frac1{2\pi}=:c_0,\quad
 \psi'(0)=0,\quad
 \psi''(z)=\frac1{2\pi\sqrt{1-z^2}}.
\]
Expanding $(1-z^2)^{-1/2}$ and integrating twice yields
\[
 \psi(z)=c_0+\sum_{j\geq1}c_{2j}z^{2j},\quad
 c_2=\frac1{4\pi},\quad c_4=\frac1{48\pi},\quad c_{2j}>0.
 \tag{8}
\]
The expansion holds initially for $|z|<1$. Positivity and monotone convergence at $z=1$, where $\psi(1)=1/4$, show that
\[
 \sum_{j\geq1}c_{2j}=\frac14-c_0,
 \quad
 0\leq r(z):=\psi(z)-c_0-c_2z^2\leq C_4 z^4
       \quad(-1\leq z\leq1).
 \tag{9}
\]
Indeed the sum of the coefficients from degree four onward is
$1/4-c_0-c_2=(\pi-3)/(4\pi)=C_4$.

The angular mean of $\psi(u_i^TU)$ is independent of $u_i$. It is $\mu_d$ in (2). To see this without an asymptotic expansion, use $w=S V$, with $V$ uniform on the sphere and independent of $S$, $\mathbb E S^2=d$. Average the left side of the kernel identity over $U$:
\[
 \mathbb E_{U,w}\sigma(w^Tu_i)\sigma(w^TU)
 =\mathbb E_S S^2\,
   \mathbb E_V[\sigma(V^Tu_i)\mathbb E_U\sigma(V^TU)]
 =d h_d^2.
\]
The odd term has angular mean zero. The density of $U_1$ is
$\Gamma(d/2)(1-z^2)^{(d-3)/2}/[\sqrt\pi\Gamma((d-1)/2)]$ on $(-1,1)$.
Integrating $z$ times this density on $(0,1)$, using the substitution $v=1-z^2$, proves the formula for $h_d$ in (2).

For later use the spherical moments are
\[
 \mathbb E U_1^2=\frac1d,\quad
 \mathbb E U_1^4=\frac3{d(d+2)},\quad
 \mathbb E U_1^8=\frac{105}{d(d+2)(d+4)(d+6)}.
 \tag{10}
\]
One derivation is to write a standard Gaussian as $S U$. Independence of $S,U$, the Gaussian even moments, and
$\mathbb E S^{2j}=d(d+2)\cdots(d+2j-2)$ give (10). Taking expectations in (9) now gives the explicit bound
\[
 0\leq\mu_d-c_0-c_2/d\leq\frac{3C_4}{d(d+2)},
 \tag{11}
\]
which proves (5) without a gamma-ratio asymptotic.

## 3. The centered quadratic test operator

Write $G_{ij}=u_i^Tu_j$, $D_a=\operatorname{diag}(a_i)$ and $J=\mathbf1\mathbf1^T$. Define
\[
 q_i(x)=a_i a(x)\left[(u_i^Tu)^2-\frac1d\right].
\]
The Gaussian radius $a(x)$ and its direction $u$ are independent, and $\mathbb E a(x)^2=1$. Rotational symmetry gives, for unit $v,w$,
\[
 \mathbb E[(v^TU)^2(w^TU)^2]
 =\frac{1+2(v^Tw)^2}{d(d+2)}.
 \tag{12}
\]
For example, apply the Gaussian fourth-moment identity
$\mathbb E[(v^Tg)^2(w^Tg)^2]=1+2(v^Tw)^2$ to $g=S U$ and divide by $\mathbb E S^4=d(d+2)$.
Subtracting $1/d^2$ gives the exact covariance
\[
 \mathbb E_x q(x)q(x)^T
 =\frac2{d(d+2)}D_a\left(G\circ G-\frac Jd\right)D_a.
 \tag{13}
\]
Here $\circ$ means entrywise product. The matrix $G\circ G-J/d$ is positive semidefinite: it is the Gram matrix of the traceless symmetric matrices $u_i u_i^T-I_d/d$ under the Frobenius inner product. Since $J/d$ is also positive semidefinite,
\[
 0\preceq D_a(G\circ G-J/d)D_a
 \preceq D_a(G\circ G)D_a.
\]
Set $P=D_aGD_a=XX^T/d$. Then $D_a(G\circ G)D_a=P\circ G$, and
\[
 \|P\circ G\|_{\rm op}\leq\|P\|_{\rm op}.
 \tag{14}
\]
For a direct proof, write $G=\sum_{k=1}^d v_kv_k^T$ using the coordinate columns of the $u_i$. If $V_k=\operatorname{diag}(v_k)$, then
$P\circ G=\sum_k V_kPV_k$. For any $b$, the absolute value of its quadratic form is at most
$\|P\|\sum_k\|V_k b\|^2=\|P\|\|b\|^2$, since each $u_i$ has unit norm. This proves (14).
Equations (13)--(14) imply
\[
 \|\mathcal T_q\|_{\rm op}
 \leq\sqrt{\frac2{d(d+2)}}\frac{\|X\|_{\rm op}}{\sqrt d}.
 \tag{15}
\]

Put $\bar r_d=\mathbb E r(U_1)$ and
\[
 v_i(x)=a_i a(x)[r(u_i^Tu)-\bar r_d].
\]
Subtracting a mean can only decrease variance. Thus (9)--(10) give
\[
 \|\mathcal T_v\|_{\rm HS}^2
 =\sum_i a_i^2\operatorname{Var}(r(U_1))
 \leq C_4^2\sum_i a_i^2\,
       \frac{105}{d(d+2)(d+4)(d+6)}.
 \tag{16}
\]
The decomposition $e_X=c_2q+v$, and the triangle inequality, prove (3)--(4). Both $q_i,v_i$ are even. Their inner products with $a(x)$ vanish because their angular means are zero and $\mathbb E a(x)^2=1$. This proves the exact orthogonality assertion.

For Gaussian training inputs, $\|X\|_{\rm op}=O_{\mathbb P}(\sqrt d)$ and $\sum_i a_i^2=O_{\mathbb P}(n)$, with $n\asymp d$. The first summand in (4) is therefore $O_{\mathbb P}(d^{-1})$, and the second is $O_{\mathbb P}(d^{-3/2})$.
The matrix norm bound follows, for instance, from $1/4$-nets of the unit spheres in dimensions $n,d$ with at most $9^n,9^d$ points. Each fixed bilinear form $v^TXu$ is standard Gaussian; a union bound gives $\|X\|\leq6\sqrt{n+d}$ with probability tending to one. The bound on $\sum_i a_i^2$ follows from its mean $n$ and variance $2n/d$.

For arbitrary $b\in\mathbb R^n$ and $\beta\in\mathbb R^d$, orthogonality gives the exact identity
\[
 s^2+\|k_\infty(x)^Tb-x^T\beta\|_{L^2}^2
 =s^2+\left\|\frac{X^Tb}{4d}-\beta\right\|^2
      +\mu_d^2(a^Tb)^2+\|\mathcal T_{e_X}b\|_{L^2}^2.
 \tag{17}
\]
No independence of $b$ and the data is required.

## 4. A spectral gap without discarding the quadratic training term

The following estimates are needed only to apply the test lemma to all training times. Entrywise powers of a Gram matrix are positive semidefinite: $G^{\circ k}$ is the Gram matrix of $u_i^{\otimes k}$. Equations (7)--(8) give
\[
 K_\infty=c_0 aa^T+A_\infty,\quad
 A_\infty=D_a\left[\frac14G+\sum_{j\geq1}c_{2j}G^{\circ2j}\right]D_a.
 \tag{18}
\]
Every matrix in the sum is positive semidefinite. Schur contraction (14), applied to the correlation matrix $G^{\circ(2j-1)}$, gives
\[
 \|D_aG^{\circ2j}D_a\|\leq\|XX^T/d\|.
\]
It follows that
\[
 \|A_\infty\|\leq(1/2-c_0)\|X\|^2/d=O_{\mathbb P}(1).
 \tag{19}
\]
There is also a fixed lower gap. The directions $u_i$ are independent uniform unit vectors, so
\[
 \mathbb E\|G^{\circ4}-I_n\|_F^2
 =\frac{105n(n-1)}{d(d+2)(d+4)(d+6)}=O(d^{-2}).
 \tag{20}
\]
Hence $G^{\circ4}=I+o_{\mathbb P}(1)$ in operator norm. Also
$\max_i|a_i^2-1|\to0$ in probability: the Gaussian chi-square bound
$\mathbb P(|\|x_i\|^2/d-1|>\delta)\leq2e^{-d\delta^2/8}$ for $0<\delta<1$, followed by a union bound, suffices. Retaining just the positive degree-four term in (18) gives, with probability tending to one,
\[
 A_\infty\succeq c_4 D_aG^{\circ4}D_a\succeq\frac{c_4}4 I_n.
 \tag{21}
\]
No approximation of the degree-two training matrix by a scalar matrix has been made.

## 5. Finite-width estimates and uniform coefficient bounds

Conditional on $X$, independence across features and the Gaussian ReLU fourth moment imply
\[
 \mathbb E_W\|K_m-K_\infty\|_F^2
 \leq\frac{3}{2m}\left(\sum_i a_i^2\right)^2.
 \tag{22}
\]
Indeed, for a joint Gaussian pair of preactivations with marginal variances $a_i^2,a_j^2$, Cauchy--Schwarz bounds the second moment of their ReLU product by
$\sqrt{(3a_i^4/2)(3a_j^4/2)}=3a_i^2a_j^2/2$. Variance is at most this raw second moment. Sum over $i,j$ and divide by $m$.

There is a sharper test-sampling estimate:
\[
 \mathbb E_W\|\mathcal T_{k_m-k_\infty}\|_{\rm HS}^2
 \leq\frac{d+2}{4dm}\sum_i a_i^2.
 \tag{23}
\]
To verify it, integrate one feature's raw second moment over $x$ first. Conditional on $w$,
$\mathbb E_x\sigma(w^Tx/\sqrt d)^2=\|w\|^2/(2d)$.
Rotating $x_i$ to the first coordinate, sign symmetry gives
\[
 \mathbb E_w[\sigma(w^Tx_i/\sqrt d)^2\|w\|^2]
 =\frac{a_i^2}2\mathbb E[w_1^2\|w\|^2]
 =\frac{a_i^2(d+2)}2.
\]
Multiplying by $1/(2d)$ and summing the variances proves (23).
Thus, under the stated width condition,
\[
 \|K_m-K_\infty\|=o_{\mathbb P}(1),\quad
 \|\mathcal T_{k_m-k_\infty}\|_{\rm op}
       =O_{\mathbb P}(\sqrt{n/m})=o_{\mathbb P}(n^{-1/2}).
 \tag{24}
\]
Let $A_m=K_m-c_0aa^T$. From (19), (21), and (24), there are fixed $\kappa,M>0$ such that, on events of probability tending to one,
\[
 \kappa I\preceq A_m\preceq MI,\qquad
 K_m\succeq\kappa I,\qquad \|a\|^2\asymp n.
 \tag{25}
\]
For example $\kappa=c_4/8$ is valid for sufficiently large dimensions on these events. The same holds for $A_\infty,K_\infty$.

Since $\mathbb E\|y\|^2=n(E+s^2)$, uniformly for $t\geq0$,
\[
 \|b_m(t)\|\leq\kappa^{-1}\|y\|=O_{\mathbb P}(\sqrt n).
 \tag{26}
\]
The radial coefficient is uniformly bounded as well. Direct multiplication verifies the rank-one inverse identity
\[
 K_m^{-1}a=\frac{A_m^{-1}a}{1+c_0 a^TA_m^{-1}a}.
\]
By (25), its norm is at most
\[
 \frac{\kappa^{-1}\|a\|}{1+(c_0/M)\|a\|^2}=O(n^{-1/2}).
 \tag{27}
\]
The spectral theorem gives $\|H_t(K_m)a\|\leq\|K_m^{-1}a\|$, since $H_t(K_m)= (I-e^{-tK_m})K_m^{-1}$ and the exponential factor is a contraction. Therefore
\[
 \sup_{t\geq0}|a^Tb_m(t)|
 \leq\|y\|\|K_m^{-1}a\|=O_{\mathbb P}(1).
 \tag{28}
\]

The output-layer ODE is $\dot a=-\Phi^T(\Phi a-y)$. Its solution from zero is $a(t)=\Phi^TH_t(K_m)y$: differentiation gives $\Phi^Te^{-tK_m}y$, and substituting the proposed solution into the ODE gives the same expression because $K_mH_t(K_m)=I-e^{-tK_m}$. Multiplication by the test feature vector therefore gives $f_{a(t)}=\mathcal T_{k_m}b_m(t)$. The test estimates (4), (24) and coefficient bound (26) imply
\[
 \sup_{t\geq0}\left\|f_{a(t)}-
   x^T\frac{X^Tb_m(t)}{4d}-\mu_d a(x)a^Tb_m(t)\right\|_{L^2}
 =O_{\mathbb P}(d^{-1/2}+n/\sqrt m)=o_{\mathbb P}(1).
 \tag{29}
\]
The retained predictor is uniformly $O_{\mathbb P}(1)$ in $L^2$: its linear part is bounded by $\|X\|\|b_m\|/(4d)$ and its radial part by (28), since $\|a(x)\|_{L^2}=1$. Also $\|\beta\|=O_{\mathbb P}(1)$. The inequality
$|\|g\|^2-\|h\|^2|\leq\|g-h\|(\|g\|+\|h\|)$ and odd/even orthogonality now prove
\[
 \sup_{t\geq0}\left|R_m(t)-s^2-
 \left\|\frac{X^Tb_m(t)}{4d}-\beta\right\|^2
 -\mu_d^2(a^Tb_m(t))^2\right|\xrightarrow{\mathbb P}0.
 \tag{30}
\]
At infinite width the error in this display is nonnegative and $O_{\mathbb P}(d^{-1})$, by (17), (4), and (26).

## 6. The radial contribution vanishes for the stated labels

Conditional on $X,W$, $y$ is centered Gaussian with covariance
\[
 C_y=(E/d)XX^T+s^2I_n,
 \qquad\|C_y\|=O_{\mathbb P}(1).
\]
On the events above with fixed bounds, $Z_t=a^TH_t(K_m)y$ is a centered Gaussian variable satisfying
\[
 \operatorname{Var}(Z_t\mid X,W)
 \leq\|C_y\|\|H_t(K_m)a\|^2\leq C/n
       \quad\text{for every }t\geq0.
 \tag{31}
\]
All constants can be fixed on events of arbitrarily high probability; this is sufficient for the probability statements below.

For completeness uniformity over an unbounded time interval follows from an explicit grid, without an interchange of limits. Let $T_n=2\kappa^{-1}\log n$ and take a grid of spacing at most $n^{-3}$ on $[0,T_n]$, including both endpoints. It has $O(n^3\log n)$ points. The Gaussian tail bound and a union bound in (31) give
\[
 \max_{t\text{ on grid}}|Z_t|
       =O_{\mathbb P}(\sqrt{\log n/n}).
\]
Between grid points,
\[
 |Z_t'|=|a^Te^{-tK_m}y|\leq\|a\|\|y\|=O_{\mathbb P}(n),
\]
so the interpolation error is $O_{\mathbb P}(n^{-2})$. For $t\geq T_n$,
\[
 |Z_t-Z_\infty|
 \leq e^{-\kappa t}\|K_m^{-1}a\|\|y\|
 =O_{\mathbb P}(n^{-2}),
 \quad Z_\infty=a^TK_m^{-1}y.
\]
The same bound holds at $T_n$, so the entire tail is bounded by $|Z_{T_n}|+O_{\mathbb P}(n^{-2})$. Consequently
\[
 \sup_{t\geq0}|a^Tb_m(t)|
 =O_{\mathbb P}(\sqrt{\log n/n})=o_{\mathbb P}(1).
 \tag{32}
\]
Equations (30), (32) prove (6). The argument for infinite width is identical after conditioning on $X$ only.

## 7. Independent checks and limits of the statement

The coefficient $1/4$ in the linear test kernel also follows directly from $\sigma(z)=(z+|z|)/2$. For correlated centered Gaussian preactivations the odd-even cross terms vanish under simultaneous sign reversal, so their product expectation is one quarter of their covariance plus one quarter of the absolute-product expectation.

There are two independent checks of the spherical covariance (13). First, for $i=j$ it reads
$\operatorname{Var}(U_1^2)=2(d-1)/[d^2(d+2)]$, which equals $3/[d(d+2)]-1/d^2$ from (10). Second, for $u_i\perp u_j$ it reads $-2/[d^2(d+2)]$, which equals $\mathbb E U_1^2U_2^2-1/d^2$. The latter mixed moment is $1/[d(d+2)]$, obtained by squaring $\sum_k U_k^2=1$ and using (10). These checks fix both the factor two and the centering $J/d$.

The constants $c_2=1/(4\pi)$ and $c_4=1/(48\pi)$ can be re-derived by expanding $\sqrt{1-z^2}$ and $z\arcsin z$ separately. Their quadratic coefficients add to $-1/2+1=1/2$; their quartic coefficients add to $-1/8+1/6=1/24$, followed by division by $2\pi$. At $z=1$, the total kernel is $1/4+\psi(1)=1/2$, the independent Gaussian moment $\mathbb E(G_+)^2$. At zero angular correlation it is $c_0$, equal to $(\mathbb E G_+)^2$. The exact formula (2) and the separate moment bound (11) agree on the first two radial coefficients.

The number 105 in (10), (16), and (20) is $7\cdot5\cdot3\cdot1$, the eighth moment of a standard Gaussian. Independently, substituting $v=z^2$ into the density of $U_1$ gives
$\mathbb E U_1^{2j}=\Gamma(j+1/2)\Gamma(d/2)/[\sqrt\pi\Gamma(d/2+j)]$, which yields the same denominator and 105 at $j=4$.

For (23), a separate radial calculation gives
$\mathbb E_w\sigma(w^Tu_i)^2\|w\|^2=\mathbb E S^4\,\mathbb E(V^Tu_i)_+^2=d(d+2)/(2d)=(d+2)/2$, agreeing with the coordinate derivation. For (22), the diagonal raw second moment is exactly $3a_i^4/2$, so its constant cannot be improved by that particular raw-moment argument.

Omitting the radial term from the **operator** approximation is invalid. For $b=a/\|a\|$, (3) and orthogonality show that $\|\mathcal T_{k_\infty-Xx/(4d)}b\|_{L^2}\geq\mu_d\|a\|$, which is of order $\sqrt n$, not $o(n^{-1/2})$. Its eventual disappearance from (6) uses both the flow's large radial training eigenvalue and the centered Gaussian teacher/noise law. An arbitrary coefficient vector need not have this property. Likewise the quadratic Hilbert--Schmidt norm alone is too weak: from (13) its square is $2(d-1)\sum_i a_i^2/[d^2(d+2)]$, of order $d^{-1}$. The operator argument (14) is what improves its squared size to $O_{\mathbb P}(d^{-2})$.

As a test of the label assumption, take instead the deterministic radial labels $y=a$ at infinite width. Write $z=a^TA_\infty^{-1}a$. By (19), (21), $z\asymp n$. The same inverse identity gives $a^TK_\infty^{-1}y=z/(1+c_0z)\to1/c_0$. Thus the radial prediction does not vanish for these labels. This case is outside the stated teacher law and shows why a bound on $\|y\|$ alone would not justify Section 6.

The scale in (27) is also checked by diagonalizing $A_m=Q\operatorname{diag}(\lambda_j)Q^T$. If $v=Q^Ta$, the squared norm is
$[\sum_j v_j^2/\lambda_j^2]/[1+c_0\sum_j v_j^2/\lambda_j]^2$. With all $\lambda_j\in[\kappa,M]$ and $\sum_jv_j^2\asymp n$, numerator and denominator have orders $n$ and $n^2$, respectively. This independently checks the extra factor $n^{-1/2}$ used in the radial variance bound.

Zero signal and zero noise cause no division by their values. If both vanish, the flow and the risk vanish identically. The estimates hold for every fixed positive aspect ratio, including $\gamma=1$. No inverse of $XX^T$ is used; the kernel gap is supplied by the positive fourth-order term. The first layer is fixed throughout. Time is for the half-sum loss; for the averaged loss replace $t$ here by the averaged-loss time divided by $n$.

The result neither proves nor refutes epoch-wise double descent. It leaves the nonlinear training kernel inside $H_t(K_m)$. In particular, the degree-two training Gram matrix has only been bounded, not replaced by a diagonal correction plus a radial term. Controlling that replacement and the effect of the large radial eigenvalue on the remaining dynamics is required before the previous Marchenko--Pastur risk formula can be used for ReLU. No risk-derivative approximation, proportional-width theorem, feature-learning theorem, or peak-time asymptotic is asserted.
