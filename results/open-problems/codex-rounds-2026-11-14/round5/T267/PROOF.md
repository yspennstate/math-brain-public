# The centered quadratic training Gram and the ReLU training kernel

The first layer is fixed. The result supplies the training-kernel approximation missing from the preceding ReLU test-risk reduction. The radial rank-one term remains in the comparison dynamics. No deterministic limiting risk curve or double-descent assertion is proved here.

## 1. Statements

Let $u_1,\ldots,u_n$ be independent uniform points on $S^{d-1}$, $d\geq2$. Write $G_{ij}=u_i^Tu_j$, $J=\mathbf1\mathbf1^T$, and
\[
 B=G\circ G-\frac Jd-\left(1-\frac1d\right)I_n.
 \tag{1}
\]
Thus $B_{ii}=0$ and $B_{ij}=(u_i^Tu_j)^2-1/d$ for $i\ne j$. Define
\[
 D=\frac{(d-1)(d+2)}2,\qquad
 \lambda=\frac2{d(d+2)},\qquad r=1-\frac1d,
\]
\[
 v=\lambda r=\frac{2(d-1)}{d^2(d+2)},\qquad
 \kappa_4=\frac{12(d-1)(5d^2-13d+12)}
 {d^4(d+2)(d+4)(d+6)}.
 \tag{2}
\]
For an integer $k\geq1$, $(n)_k=n(n-1)\cdots(n-k+1)$, with value zero for $k>n$.

**Quadratic Gram theorem.** There is the exact identity
\[
 \mathbb E\operatorname{tr} B^4
  =(n)_4D\lambda^4+2(n)_3v^2+(n)_2\kappa_4.
 \tag{3}
\]
In particular, if $d/n\to\gamma\in(0,\infty)$, then
\[
 d\,\mathbb E\operatorname{tr} B^4\longrightarrow\frac8{\gamma^3},
 \qquad \|B\|_{\rm op}=O_{\mathbb P}(d^{-1/4})=o_{\mathbb P}(1).
 \tag{4}
\]
The displayed rate is an upper bound, not a sharp asymptotic for $\|B\|$.

Now let $n,d\to\infty$, and let $x_1,\ldots,x_n$ be independent $N(0,I_d)$ vectors, with $d/n\to\gamma\in(0,\infty)$. Let $X$ have rows $x_i^T$, and put
\[
 a_i=\|x_i\|/\sqrt d,\quad D_a=\operatorname{diag}(a_i),\quad
 a=(a_i)_{i=1}^n,\quad u_i=x_i/\|x_i\|,\quad L=\frac{XX^T}{4d}.
\]
For $\sigma(z)=\max(z,0)$ let
\[
 (K_\infty)_{ij}=\mathbb E_{w\sim N(0,I_d)}
       [\sigma(w^Tx_i/\sqrt d)\sigma(w^Tx_j/\sqrt d)].
\]
Define
\[
 c_0=\frac1{2\pi},\quad c_2=\frac1{4\pi},\quad
 c=\frac14-\frac1{2\pi}>0,\qquad
 \mu_d=d\left[\frac{\Gamma(d/2)}{2\sqrt\pi\Gamma((d+1)/2)}\right]^2.
 \tag{5}
\]

**ReLU training-kernel consequence.** Both approximations hold in operator norm:
\[
 \left\|K_\infty-L-\mu_d aa^T
             -\left(\frac14-\mu_d\right)D_a^2\right\|
       =O_{\mathbb P}(d^{-1/4}),
 \tag{6}
\]
\[
 \|K_\infty-K_*\|=O_{\mathbb P}(d^{-1/4}),
 \qquad K_*=L+\mu_d aa^T+cI_n.
 \tag{7}
\]
The matrix retained in (6) has exactly the same diagonal as $K_\infty$. One can replace $\mu_d$ in (7) by $c_0+c_2/d$, with additional error $O_{\mathbb P}(d^{-1})$. Replacing it by $c_0$ alone is in general invalid in operator norm.

For $w_1,\ldots,w_m\sim N(0,I_d)$ independent of each other and of $X$, let
\[
 \Phi_{ir}=m^{-1/2}\sigma(w_r^Tx_i/\sqrt d),\qquad K_m=\Phi\Phi^T.
\]
If $m/n^2\to\infty$, then
\[
 \|K_m-K_*\|=O_{\mathbb P}(d^{-1/4}+n/\sqrt m)=o_{\mathbb P}(1).
 \tag{8}
\]

## 2. Covariance of traceless quadratic features

Let $\mathcal H$ be the real vector space of traceless symmetric $d\times d$ matrices, with inner product $\langle A,C\rangle=\operatorname{tr}(AC)$. Its dimension is $D$ in (2). Put
\[
 Q(u)=uu^T-I_d/d\in\mathcal H.
\]
Then
\[
 \mathbb E Q(u)=0,\quad
 \|Q(u)\|_F^2=r,\quad
 \langle Q(u),Q(v)\rangle=(u^Tv)^2-1/d.
 \tag{9}
\]
The norm identity follows by expanding $(uu^T-I_d/d)^2$ and taking its trace.

For a standard Gaussian $g=S U$, its radius $S$ is independent of its uniform direction $U$, with $\mathbb E S^4=d(d+2)$. The Gaussian fourth moment gives
\[
 \mathbb E[U_iU_jU_kU_l]
   =\frac{\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}
                         +\delta_{il}\delta_{jk}}{d(d+2)}.
\]
Consequently, for $A,C\in\mathcal H$,
\[
 \mathbb E[\langle A,Q(U)\rangle\langle C,Q(U)\rangle]
    =\frac{2\operatorname{tr}(AC)}{d(d+2)}
    =\lambda\langle A,C\rangle.
 \tag{10}
\]
Thus the covariance operator of $Q(U)$ on $\mathcal H$ is $\lambda I_{\mathcal H}$. Its trace is $D\lambda=r$, consistent with (9).
In particular, for two independent directions,
\[
 \mathbb E\langle Q(u),Q(v)\rangle^2=\lambda r=v.
 \tag{11}
\]
Conditioning on either direction gives the same value, since its feature norm is deterministic.

## 3. Exact fourth trace

Expand
\[
 \operatorname{tr}B^4
   =\sum_{i,j,k,l}B_{ij}B_{jk}B_{kl}B_{li}.
 \tag{12}
\]
A nonzero term has $i\ne j$, $j\ne k$, $k\ne l$ and $l\ne i$. There are only three types.

If all four indices are distinct, write $q_i=Q(u_i)$. Conditioning on $q_i,q_k$ and integrating the independent $q_j,q_l$, equation (10) gives
\[
 \mathbb E[B_{ij}B_{jk}B_{kl}B_{li}\mid q_i,q_k]
       =\lambda^2\langle q_i,q_k\rangle^2.
\]
Its expectation is $\lambda^2v=D\lambda^4$. There are $(n)_4$ ordered index choices.

With exactly three distinct indices, either $i=k$ or $j=l$, but not both. In the first case the term is $B_{ij}^2B_{il}^2$. Conditional on $q_i$, the two other features are independent, and each square has conditional mean $\lambda\|q_i\|^2=v$. Thus its expectation is $v^2$. The other pattern has the same value. There are $2(n)_3$ such terms.

With exactly two distinct indices, necessarily $i=k$, $j=l$, and the term is $B_{ij}^4$. There are $(n)_2$ terms, each with expectation
\[
 \mathbb E(U_1^2-1/d)^4
 =\frac{105}{d(d+2)(d+4)(d+6)}
  -\frac{60}{d^2(d+2)(d+4)}
  +\frac{18}{d^3(d+2)}-\frac3{d^4}
 =\kappa_4.
 \tag{13}
\]
Here rotational invariance permits fixing one direction. The spherical moments used are
\[
 \mathbb E U_1^{2k}
   =\frac{(2k-1)!!}{d(d+2)\cdots(d+2k-2)}.
 \tag{14}
\]
They follow by writing $g_1=S U_1$, using independence, and dividing the Gaussian moment $(2k-1)!!$ by $\mathbb E S^{2k}=d(d+2)\cdots(d+2k-2)$. Expansion of the fourth power gives the first equality in (13). Putting its terms over a common denominator gives numerator
$60d^3-216d^2+300d-144=12(d-1)(5d^2-13d+12)$, proving the second equality.

These three cases exhaust (12) and prove (3). Their orders for $n\asymp d$ are respectively $O(d^{-2})$, $O(d^{-1})$, $O(d^{-2})$. More precisely,
\[
 D\lambda^4\sim8d^{-6},\qquad v^2\sim4d^{-4},\qquad
 \kappa_4\sim60d^{-4}.
\]
Since $n/d\to1/\gamma$, only the three-distinct-index contribution survives after multiplication by $d$, and its limit is $8/\gamma^3$.

The matrix $B$ is symmetric, so $\|B\|^4\leq\operatorname{tr}B^4$. For every $\epsilon>0$,
\[
 \mathbb P(\|B\|>\epsilon)
   \leq\frac{(n)_4D\lambda^4+2(n)_3v^2+(n)_2\kappa_4}{\epsilon^4}.
 \tag{15}
\]
Taking first fixed $\epsilon$ proves convergence to zero. Taking $\epsilon=M d^{-1/4}$ and then $M\to\infty$ proves the rate in (4). No entrywise independence of $B$ is assumed.

## 4. ReLU kernel expansion, including the diagonal

For unit directions of correlation $z$, Gaussian integration in their two-dimensional span gives
\[
 \mathbb E_w\sigma(w^Tu)\sigma(w^Tv)
    =\frac z4+\psi(z),\qquad
 \psi(z)=\frac{\sqrt{1-z^2}+z\arcsin z}{2\pi}.
 \tag{16}
\]
For example, with angle $\theta=\arccos z$, the two-dimensional Gaussian has uniform angle and squared radius of mean two. Integration of
$\pi^{-1}\cos\varphi\cos(\varphi-\theta)$ over $[\theta-\pi/2,\pi/2]$ gives
$[\sin\theta+(\pi-\theta)\cos\theta]/(2\pi)$, which is (16). Positive homogeneity supplies the factors $a_i a_j$.

Set $\eta(z)=\psi(z)-c_0-c_2z^2$. Since
$\psi''(z)=1/[2\pi\sqrt{1-z^2}]$, its even Taylor coefficients of degree at least two are positive. At $z=1$, $\psi(1)=1/4$. It follows, by summing the positive series up to the endpoint, that
\[
 0\leq\eta(z)\leq C_4 z^4\quad(-1\leq z\leq1),\qquad
 C_4=\frac14-c_0-c_2=\frac{\pi-3}{4\pi}.
 \tag{17}
\]
Indeed $z^{2k}\leq z^4$ for $k\geq2$. Define $\bar\eta_d=\mathbb E\eta(U_1)$. Equations (14), (17) imply
\[
 0\leq\bar\eta_d\leq\frac{3C_4}{d(d+2)},\qquad
 \mu_d=c_0+\frac{c_2}{d}+\bar\eta_d.
 \tag{18}
\]
To verify that this angular mean equals the gamma expression in (5), let $w=S V$, with $V$ uniform on the sphere. For $h_d=\mathbb E(U_1)_+$, averaging the ReLU covariance over an independent direction $U$ gives $\mathbb E S^2\,h_d^2=dh_d^2$; the odd term in (16) averages to zero. Integration of the spherical coordinate density gives
$h_d=\Gamma(d/2)/[2\sqrt\pi\Gamma((d+1)/2)]$. This proves (18) with precisely the stated $\mu_d$.

Let $F$ have zero diagonal and entries $F_{ij}=\eta(G_{ij})$ for $i\ne j$. The off-diagonal eighth moment gives
\[
 \mathbb E\|F\|_F^2
 \leq C_4^2\frac{105n(n-1)}{d(d+2)(d+4)(d+6)}
       =O(d^{-2}).
 \tag{19}
\]
Therefore $\|F\|\leq\|F\|_F=O_{\mathbb P}(d^{-1})$. Using (1), (16), (17), with $\eta(1)=C_4$, gives the exact decomposition
\[
 K_\infty=L+\left(c_0+\frac{c_2}{d}\right)aa^T
   +\left(c-\frac{c_2}{d}\right)D_a^2
   +c_2D_a B D_a+D_a F D_a.
 \tag{20}
\]
This identity retains every diagonal contribution. In particular, the quadratic term contributes both $aa^T/d$ and $(1-1/d)D_a^2$.

Subtracting the comparison matrix in (6) from (20) leaves
\[
 c_2D_a B D_a+D_a F D_a
               -\bar\eta_d(aa^T-D_a^2).
 \tag{21}
\]
For Gaussian inputs, their directions have the distribution used in Sections 2--3, and
\[
 \max_i|a_i^2-1|=O_{\mathbb P}(\sqrt{\log d/d}),\qquad
 \|a\|^2=O_{\mathbb P}(n).
 \tag{22}
\]
For the first bound, use
$\mathbb P(|\|x_i\|^2/d-1|>\delta)\leq2e^{-d\delta^2/8}$ for $0<\delta<1$, obtained from the chi-square moment generating function and Chernoff's inequality, and then take a union bound. For the second bound, $\mathbb E\|a\|^2=n$, or use the first bound. Combining (4), (18), (19), (21), (22) proves (6). For instance, the last term in (21) has norm at most
$3C_4(\|a\|^2+\|D_a\|^2)/[d(d+2)]=O_{\mathbb P}(d^{-1})$.

Finally,
\[
 \left(\frac14-\mu_d\right)D_a^2-cI
   =c(D_a^2-I)- (\mu_d-c_0)D_a^2.
\]
Its norm is $O_{\mathbb P}(\sqrt{\log d/d}+d^{-1})=o_{\mathbb P}(d^{-1/4})$, proving (7). Also (18) gives
$\|(\mu_d-c_0-c_2/d)aa^T\|=O_{\mathbb P}(n/d^2)=O_{\mathbb P}(d^{-1})$.

## 5. Finite width and the retained-spike flow

Conditional on $X$, the features are independent across $r$. For two jointly Gaussian preactivations of variances $a_i^2,a_j^2$, Cauchy--Schwarz and $\mathbb E(G_+)^4=3/2$ give
\[
 \mathbb E[\sigma(w^Tx_i/\sqrt d)^2\sigma(w^Tx_j/\sqrt d)^2]
       \leq\frac32a_i^2a_j^2.
\]
Variance is at most raw second moment, so summation over entries gives
\[
 \mathbb E_W\|K_m-K_\infty\|_F^2
       \leq\frac3{2m}\left(\sum_i a_i^2\right)^2.
 \tag{23}
\]
Conditional Markov's inequality and (22) imply
$\|K_m-K_\infty\|=O_{\mathbb P}(n/\sqrt m)$. This proves (8).

Here is a consequence for the previous risk reduction that still retains the spike. Let the network be
\[
 f_{\alpha}(x)=m^{-1/2}\sum_{r=1}^m\alpha_r\sigma(w_r^Tx/\sqrt d),
\]
with only $\alpha$ trained, from zero, by gradient flow for the half-sum squared loss. Let
$E,s^2\geq0$, $\beta\sim N(0,(E/d)I_d)$, $\varepsilon\sim N(0,s^2I_n)$, mutually independent and independent of $X,W$, and $y=X\beta+\varepsilon$. Define $H_t(A)=\int_0^t e^{-uA}\,du$ and the actual realized test risk
$R_m(t)=s^2+\|f_{\alpha(t)}-x^T\beta\|_{L^2(N(0,I_d))}^2$. Under the same width condition, the round 4 theorem gives
\[
 \sup_{t\geq0}\left|R_m(t)-s^2-
       \left\|\frac{X^TH_t(K_m)y}{4d}-\beta\right\|^2\right|
       \xrightarrow{\mathbb P}0.
 \tag{24}
\]
This quoted result is the one independently checked in LOG.md; the training-kernel proof through (23) does not depend on it.

Since $K_*\succeq cI$, (8) gives $K_m\succeq(c/2)I$ with probability tending to one. For any symmetric $A,C\succeq\kappa I$, Duhamel's formula and contraction give, without an upper bound on either spectrum,
\[
 \|e^{-uA}-e^{-uC}\|\leq u e^{-\kappa u}\|A-C\|,
 \qquad
 \sup_{t\geq0}\|H_t(A)-H_t(C)\|
       \leq\kappa^{-2}\|A-C\|.
 \tag{25}
\]
Indeed the exponential difference is an integral over $0\leq v\leq u$ of products of exponentials with one factor $A-C$; their norms multiply to at most $e^{-\kappa u}$. Integrating in $u$ proves the second inequality.
For Gaussian $X$, $\|X\|=O_{\mathbb P}(\sqrt d)$; one proof uses $1/4$-nets with at most $9^n$ and $9^d$ points and the standard Gaussian tail of each bilinear form, giving $\|X\|\leq6\sqrt{n+d}$ with probability tending to one. Also $\mathbb E\|y\|^2=n(E+s^2)$. Equations (8), (25) therefore give
\[
 \sup_{t\geq0}\left\|\frac{X^T}{4d}
                [H_t(K_m)-H_t(K_*)]y\right\|=o_{\mathbb P}(1).
\]
Each comparison parameter has bounded norm in probability uniformly in time, since $\|H_t\|\leq2/c$ on these events, and $\|\beta\|=O_{\mathbb P}(1)$. The difference-of-squares inequality applied to (24) proves
\[
 \sup_{t\geq0}\left|R_m(t)-s^2-
       \left\|\frac{X^TH_t(K_*)y}{4d}-\beta\right\|^2\right|
       \xrightarrow{\mathbb P}0.
 \tag{26}
\]
The same consequence holds at infinite width, using (7) and the infinite-width version of (24). Equation (26) replaces the nonlinear training kernel, but does not delete its radial spike. It is not the earlier Marchenko--Pastur risk formula.

## 6. Independent checks and failed simplifications

**A second enumeration of the fourth trace.** Use $\operatorname{tr}B^4=\sum_{i,k}(B^2_{ik})^2$. The terms $i=k$ give $(n)_2\kappa_4+(n)_3v^2$ by expanding $(\sum_{j\ne i}B_{ij}^2)^2$. For $i\ne k$, equal intermediate indices give another $(n)_3v^2$, and unequal intermediate indices give $(n)_4D\lambda^4$. This independently checks the factor two in (3). For $n=2$, the trace is exactly $2B_{12}^4$; for $n=3$, (3) gives $6\kappa_4+12v^2$, agreeing with the direct expansion of a symmetric zero-diagonal three-by-three matrix.

For a separate scalar check of the covariance constants, direct spherical moments give
$v=\operatorname{Var}(U_1^2)=3/[d(d+2)]-1/d^2$. Dividing by the squared feature norm $r$ recovers $\lambda=2/[d(d+2)]$. The space dimension is independently $d(d+1)/2-1=(d-1)(d+2)/2$, and its product with $\lambda$ is $r$. Thus the four-distinct-index term can equally be written $\lambda^3r$ or $D\lambda^4$.

**A second calculation of $\kappa_4$.** The variable $Z=U_1^2$ has beta density proportional to $z^{-1/2}(1-z)^{(d-3)/2}$, with parameters $\alpha=1/2$, $\beta=(d-1)/2$. Write $q=\alpha+\beta=d/2$, $\mu=\alpha/q=1/d$, and $M_k=\mathbb E(Z-\mu)^k$. Integration by parts against this density gives
\[
 \mathbb E[Z(1-Z)f'(Z)]=\mathbb E[(qZ-\alpha)f(Z)].
\]
The boundary term vanishes for polynomial $f$ because $z^\alpha(1-z)^\beta$ vanishes at both endpoints, including when $d=2$. With $f(z)=(z-\mu)^{k-1}$ this becomes
\[
 (q+k-1)M_k=(k-1)[\mu(1-\mu)M_{k-2}+(1-2\mu)M_{k-1}].
\]
Starting with $M_0=1,M_1=0$ gives
\[
 M_2=v,\qquad M_3=\frac{8(d-1)(d-2)}{d^3(d+2)(d+4)},
\]
and
\[
 M_4=\frac{12(d-1)[(d-1)(d+4)+4(d-2)^2]}
 {d^4(d+2)(d+4)(d+6)}=\kappa_4.
\]
This derivation uses a centered-moment recurrence instead of the raw-moment expansion in (13). At $d=2$, independently $Z-1/2=\cos(2\theta)/2$ for uniform $\theta$, so $M_4=(1/16)(3/8)=3/128$, exactly (2).

The same integration-by-parts identity, applied to $f(z)=z^{k-1}$, gives $(q+k-1)\mathbb E Z^k=(\alpha+k-1)\mathbb E Z^{k-1}$. At $k=1,2,3,4$ it yields $\mathbb E U_1^8=105/[d(d+2)(d+4)(d+6)]$, independently checking the Gaussian-radius derivation of the constant 105 in (19).

**Kernel and time-filter constants.** For a scalar $G\sim N(0,1)$, independently $c_0=(\mathbb E G_+)^2=1/(2\pi)$ and the linear coefficient is $1/4$ from $G_+=(G+|G|)/2$. The separate expansions $\sqrt{1-z^2}=1-z^2/2+O(z^4)$ and $z\arcsin z=z^2+O(z^4)$ give $c_2=1/(4\pi)$. The retained bulk diagonal constant can also be calculated as the total feature second moment minus the constant and odd-linear contributions: $c=1/2-c_0-1/4$. These checks agree with (17), (20). At $t=\infty$, the independent inverse identity $A^{-1}-C^{-1}=A^{-1}(C-A)C^{-1}$ gives the same $\kappa^{-2}$ bound as (25). The finite-time estimate in (25) is stronger than this endpoint check and is the one used in (26).

**The quadratic Frobenius shortcut fails.** Equation (11) gives
\[
 \mathbb E\|B\|_F^2=(n)_2v\longrightarrow2/\gamma^2.
\]
In fact this is also convergence in probability: distinct unordered edge squares have zero covariance, even when they share one endpoint, because their conditional means are the same constant $v$. Hence
$\operatorname{Var}(\|B\|_F^2)=2(n)_2(\kappa_4-v^2)=O(d^{-2})$. A Frobenius argument cannot prove $\|B\|\to0$, although the fourth trace can.

**The radial coefficient needs its quadratic correction.** Since
$\|a\|^2/n\to1$ in probability (its variance is $2n/d$ before dividing by $n^2$), (18) implies
\[
 \|(\mu_d-c_0)aa^T\|=(\mu_d-c_0)\|a\|^2
       \xrightarrow{\mathbb P}\frac{c_2}{\gamma}>0.
\]
Thus the operator approximation $K_\infty\approx L+c_0aa^T+cI$ fails. Indeed (7) and the reverse triangle inequality show the norm of that difference tends to $c_2/\gamma$. The correction is small entrywise but not in operator norm. Also $aa^T$ cannot be replaced by $J$ without a new argument. This proof makes no such replacement.

**Diagonal check.** The diagonal of $L$ is $a_i^2/4$. The remaining retained diagonal in (6) is $\mu_d a_i^2+(1/4-\mu_d)a_i^2=a_i^2/4$. Their sum is $a_i^2/2$, the independent identity $\mathbb E\sigma(N(0,a_i^2))^2=a_i^2/2$. Dropping the quadratic diagonal would leave a fixed error $c_2$ at unit radius; dropping the whole nonlinear diagonal would leave $c$.

The approximation is specific to isotropic Gaussian inputs, fixed first-layer weights, and the sufficient width condition above. Neither (7) nor (26) justifies removing $\mu_d aa^T$ from the dynamics. That term has an eigenvalue of order $n$ and is correlated with the design through $a$. Operator-norm perturbation by deleting it is not small. Its effect on realized risk and derivatives must be treated using the stated random labels and a separate dynamical argument. No feature-learning or positive double-descent result follows from this training-kernel lemma.
