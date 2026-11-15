# A realized-risk limit for wide sine random features

The result below supplies a network-to-spectral-risk reduction for one nonlinear activation. It is a negative special case for epoch-wise double descent, not a construction of double descent. The first layer is fixed throughout.

## 1. Model and theorem

Let $n,d,m\to\infty$, with
\[
 d/n\to\gamma\in(0,\infty),\qquad m/n^2\to\infty.
\tag{1}
\]
Let $x_1,\ldots,x_n,w_1,\ldots,w_m$ be independent standard Gaussian vectors in $\mathbb R^d$. Independently take
\[
 \beta\sim N(0,(E/d)I_d),\qquad
 \varepsilon\sim N(0,s^2I_n),\qquad y=X\beta+\varepsilon,
\tag{2}
\]
where $E,s^2\geq0$, and the rows of $X$ are $x_i^T$. Consider the two-layer network
\[
 f_a(x)=m^{-1/2}\sum_{r=1}^m a_r\sin(w_r^Tx/\sqrt d).
\tag{3}
\]
Train only $a$, from $a(0)=0$, by gradient flow for
\[
 L(a)=\frac12\sum_{i=1}^n(f_a(x_i)-y_i)^2.
\tag{4}
\]
Thus time in this note is $1/n$ times the time for gradient flow of the averaged loss $L/n$. There is no explicit regularization.

The actual test risk, conditional on the realized training inputs, weights, teacher, and training noise, is
\[
 R_{n,d,m}(t)=\mathbb E_{x,\varepsilon_*}
  [(f_{a(t)}(x)-x^T\beta-\varepsilon_*)^2]
 =s^2+\|f_{a(t)}-x^T\beta\|_{L^2(N(0,I_d))}^2,
\tag{5}
\]
where $x\sim N(0,I_d)$ and $\varepsilon_*\sim N(0,s^2)$ are independent of training.

Set
\[
 q=e^{-1},\qquad
 c=\frac{1-e^{-2}}2-e^{-1}=q(\sinh1-1)>0,
\tag{6}
\]
and
\[
 \ell_\pm=\frac q\gamma(1\pm\sqrt\gamma)^2,\qquad
 \nu(d\ell)=(1-\gamma^{-1})_+\delta_0(d\ell)
 +\frac{\sqrt{(\ell_+-\ell)(\ell-\ell_-)}}{2\pi q\ell}
       \mathbf1_{(\ell_-,\ell_+)}\,d\ell.
\tag{7}
\]
This is a probability measure. Define
\[
 R(t)=s^2+\int\left[
 E\left(\frac{c+\ell e^{-(\ell+c)t}}{\ell+c}\right)^2
 +q s^2\frac{\ell}{(\ell+c)^2}(1-e^{-(\ell+c)t})^2
 \right]\nu(d\ell).
\tag{8}
\]

**Theorem.** Under (1)--(4), for $j=0,1,2$,
\[
 \sup_{t\geq0}|R_{n,d,m}^{(j)}(t)-R^{(j)}(t)|
       \xrightarrow{\mathbb P}0.
\tag{9}
\]
In particular this is a limit of realized-sample risk, not only its teacher/noise average. The limiting curve has the following complete classification:

* If $E>0$ and $q s^2\leq Ec$, it is strictly decreasing at all finite times.
* If $E>0$ and $q s^2>Ec$, it has exactly one critical point $t_*>0$, a nondegenerate minimum.
* If $E=0<s^2$, it is strictly increasing for $t>0$; if both are zero, it is constant.

Thus the limiting risk in this special case has no interior local maximum. No peak time exists for this model. When the unique minimum exists, on every fixed interval $[0,U]$ with $U>t_*$, the finite-network risk has exactly one critical point with probability tending to one, and that point converges to $t_*$. Additional finite-network extrema with times tending to infinity are not excluded by (9).

## 2. Elementary Gaussian estimates

Write
\[
 r_i=\|x_i\|^2/d,\quad Z=XX^T/d,\quad
 D=\operatorname{diag}(e^{-r_i/2}).
\]
The following bounds will be used:
\[
 \max_i|r_i-1|=o_{\mathbb P}(1),\qquad
 \|X\|_{\rm op}=O_{\mathbb P}(\sqrt d),\qquad
 \max_{i\ne j}|Z_{ij}|\leq1\quad\text{with probability tending to one}.
\tag{10}
\]
For completeness, the chi-square moment generating function is
$\mathbb E e^{u\|x_i\|^2}=(1-2u)^{-d/2}$ for $u<1/2$.
Chernoff's inequality and the elementary logarithm bounds give
$\mathbb P(|r_i-1|>\delta)\leq2e^{-d\delta^2/8}$, $0<\delta<1$.
A union bound with $\delta=\sqrt{24\log d/d}$ proves the first assertion in (10).

For the second assertion, take $1/4$-nets of the unit spheres in dimensions $n,d$, each with at most $9^n,9^d$ elements. Approximating both arguments in a bilinear form gives
$\|X\|_{\rm op}\leq2\max_{u,v\text{ in the nets}}|u^TXv|$.
Each fixed $u^TXv$ is standard normal. A union bound therefore gives
\[
 \mathbb P(\|X\|_{\rm op}>6\sqrt{n+d})
 \leq2\exp\{(n+d)(\log9-9/2)\}\to0.
\]
Since $n/d$ stays bounded, this proves the claim. Finally, conditional on $x_i$, $Z_{ij}\sim N(0,r_i/d)$ for $j\ne i$. On $r_i\leq2$,
$\mathbb P(|Z_{ij}|>1\mid x_i)\leq2e^{-d/4}$.
Another union bound proves the last assertion.

Conditioning the sixth moment in the same way gives the exact identity
\[
 \mathbb E Z_{ij}^6
  =\frac{15\,d(d+2)(d+4)}{d^6},\qquad i\ne j.
\tag{11}
\]
Here the factor 15 is the sixth moment of a standard normal, and
$\mathbb E\|x_i\|^6=d(d+2)(d+4)$.

## 3. Training kernel at infinite width

Let $\phi_w(x)=\sin(w^Tx/\sqrt d)$. The Gaussian characteristic function and
$\sin u\sin v=(\cos(u-v)-\cos(u+v))/2$ give the exact identity
\[
 k_\infty(x,z)=\mathbb E_w[\phi_w(x)\phi_w(z)]
 =e^{-(\|x\|^2+\|z\|^2)/(2d)}\sinh(x^Tz/d).
\tag{12}
\]
Let $K_\infty=(k_\infty(x_i,x_j))_{ij}$, and define
\[
 K_0=qXX^T/d+cI_n.
\tag{13}
\]
We claim
\[
 \|K_\infty-K_0\|_{\rm op}=o_{\mathbb P}(1).
\tag{14}
\]
Off the diagonal, subtract $DZD$. For $|z|\leq1$, the power series for $\sinh$ gives
$|\sinh z-z|\leq C|z|^3$ with an absolute finite $C$.
The exponential factors in (12) are at most one. On the last event in (10), the squared Frobenius norm of the off-diagonal remainder is consequently at most
$C^2\sum_{i\ne j}Z_{ij}^6$.
By (11) its expectation before restricting to that event is
\[
 C^2\frac{15n(n-1)d(d+2)(d+4)}{d^6}=O(d^{-1}).
\]
Markov's inequality and (10) show that this remainder is $o_{\mathbb P}(1)$ in operator norm.

On the diagonal,
\[
 (K_\infty)_{ii}=e^{-r_i}\sinh r_i=(1-e^{-2r_i})/2,
\]
so the diagonal of $K_\infty-DZD$ equals
\[
 c(r_i)=(1-e^{-2r_i})/2-r_ie^{-r_i}.
\]
Continuity and (10) give $\max_i|c(r_i)-c(1)|=o_{\mathbb P}(1)$, with $c(1)=c$. Also
\[
 \|DZD-qZ\|_{\rm op}
 \leq\|D-\sqrt qI\|_{\rm op}\|Z\|_{\rm op}
          (\|D\|_{\rm op}+\sqrt q)=o_{\mathbb P}(1).
\]
This proves (14). In particular $K_\infty$ has its spectrum in a fixed interval $[c/2,M]$ with probability tending to one, for a sufficiently large fixed $M$.

## 4. Test kernel in the required operator norm

For a vector-valued function $k(x)\in\mathbb R^n$, denote by $\mathcal T_k:\mathbb R^n\to L^2(N(0,I_d))$ the map
$b\mapsto k(x)^Tb$.
Its Hilbert--Schmidt norm satisfies
$\|\mathcal T_k\|_{\rm HS}^2=\mathbb E_x\|k(x)\|^2$, and its operator norm is no larger.
Put $k_0(x)=qXx/d$, and let $k_\infty(x)$ be (12) evaluated against the training points. Then
\[
 \|\mathcal T_{k_0}\|_{\rm op}=q\|X\|_{\rm op}/d
       =O_{\mathbb P}(d^{-1/2}),
\tag{15}
\]
and the sharper approximation needed for prediction is
\[
 \|\mathcal T_{k_\infty-k_0}\|_{\rm op}
       =o_{\mathbb P}(d^{-1/2}).
\tag{16}
\]

To prove it, write $r=\|x\|^2/d$, $a(x)=e^{-r/2}$, and $z_i=x_i^Tx/d$. The linear part of $k_\infty(x)$ is $a(x)DXx/d$. Its difference from $qXx/d$ splits as
\[
 (a(x)-\sqrt q)DXx/d+\sqrt q(D-\sqrt qI)Xx/d.
\tag{17}
\]
The second term has operator norm at most
$\sqrt q\|D-\sqrt qI\|_{\rm op}\|X\|_{\rm op}/d=o_{\mathbb P}(d^{-1/2})$.
For the first, rotational invariance gives
\[
 \mathbb E_x[(a(x)-\sqrt q)^2xx^T]=\tau_d I_d,
 \quad \tau_d=\mathbb E[(e^{-r/2}-e^{-1/2})^2r].
\]
Since $u\mapsto e^{-u/2}$ is $1/2$-Lipschitz on $[0,\infty)$,
\[
 \tau_d\leq\tfrac14\mathbb E[r(r-1)^2]
 =\frac1{2d}+\frac2{d^2}.
\tag{18}
\]
The equality uses $\mathbb E r^2=1+2/d$ and $\mathbb E r^3=1+6/d+8/d^2$. Thus the first operator in (17) has norm at most
$\sqrt{\tau_d}\|DX\|_{\rm op}/d=O_{\mathbb P}(d^{-1})$.

It remains to bound the nonlinear remainder, with components
$a(x)e^{-r_i/2}(\sinh z_i-z_i)$.
Conditional on $X$, $z_i\sim N(0,v_i)$, $v_i=r_i/d$. For $Z_v\sim N(0,v)$,
\[
 \mathbb E(\sinh Z_v-Z_v)^2
 =\frac{e^{2v}-1}{2}-2ve^{v/2}+v=O(v^3),\quad 0\leq v\leq1.
\tag{19}
\]
The identity follows from Gaussian exponential moments; the constant and first two Taylor coefficients vanish, so the final bound is uniform on this compact interval. Since $a(x)e^{-r_i/2}\leq1$, on $\max_i r_i\leq2$ the squared Hilbert--Schmidt norm of this remainder is at most
$C\sum_i(r_i/d)^3\leq8Cn/d^3=O(d^{-2})$.
It therefore has operator norm $O(d^{-1})$. Together with (17)--(18), this proves (16).

The operator estimate in (18) is essential: a Hilbert--Schmidt estimate on the entire radial linear error would not suffice after multiplication by a label vector of norm of order $\sqrt n$.

## 5. Finite width

Let $\Phi_{ir}=m^{-1/2}\phi_{w_r}(x_i)$, so
\[
 K_m=\Phi\Phi^T,\qquad
 k_m(x)_i=m^{-1}\sum_{r=1}^m\phi_{w_r}(x_i)\phi_{w_r}(x).
\]
Conditional on $X$, independence of the weights and $|\phi_w|\leq1$ yield
\[
 \mathbb E_W\|K_m-K_\infty\|_F^2\leq n^2/m,
\quad
 \mathbb E_W\|\mathcal T_{k_m-k_\infty}\|_{\rm HS}^2\leq n/m.
\tag{20}
\]
These follow by summing the variances of the independent empirical averages in each entry; the second estimate also integrates over the independent test input. Consequently
\[
 \|K_m-K_0\|_{\rm op}=o_{\mathbb P}(1),\qquad
 \sqrt n\|\mathcal T_{k_m-k_0}\|_{\rm op}=o_{\mathbb P}(1).
\tag{21}
\]
For the second statement, (20) bounds the finite-width part by $O_{\mathbb P}(n/\sqrt m)=o_{\mathbb P}(1)$ after multiplication by $\sqrt n$; (16) bounds the infinite-width part. All spectra of $K_m,K_0$ therefore lie in $[c/2,M]$, and
$\|\mathcal T_{k_m}\|_{\rm op}=O_{\mathbb P}(d^{-1/2})$, with probability tending to one.

## 6. Gradient flow and uniform time control

For a positive definite matrix $A$, let
\[
 H_t(A)=\int_0^t e^{-uA}\,du.
\]
Solving $\dot a=-\Phi^T(\Phi a-y)$, $a(0)=0$, gives
\[
 f_m(t,x)=k_m(x)^TH_t(K_m)y.
\tag{22}
\]
Indeed $a(t)=\Phi^TH_t(K_m)y$ solves that differential equation and initial condition. Define the comparison predictor
\[
 f_0(t,x)=k_0(x)^TH_t(K_0)y.
\tag{23}
\]
On matrices with spectra in $[\kappa,M]$, $\kappa=c/2>0$, the following bounds are uniform in $t\geq0$: for $j=0,1,2$,
\[
 \|\partial_t^jH_t(A)\|_{\rm op}\leq C,\qquad
 \|\partial_t^jH_t(A)-\partial_t^jH_t(B)\|_{\rm op}
       \leq C\|A-B\|_{\rm op}.
\tag{24}
\]
Here and below $C$ may depend on fixed parameters but not dimensions or time. For verification,
$\partial_tH_t(A)=e^{-tA}$, $\partial_t^2H_t(A)=-Ae^{-tA}$, and Duhamel's identity gives
\[
 \|e^{-uA}-e^{-uB}\|_{\rm op}
 \leq u e^{-\kappa u}\|A-B\|_{\rm op}.
\]
Integrating this bound proves the $j=0$ Lipschitz estimate with constant $\kappa^{-2}$; for $j=1$, use $\sup_{u\geq0}ue^{-\kappa u}<\infty$. For $j=2$, split $Ae^{-tA}-Be^{-tB}=(A-B)e^{-tA}+B(e^{-tA}-e^{-tB})$. These prove all assertions in (24).

Also $\|y\|=O_{\mathbb P}(\sqrt n)$: for example $\mathbb E\|y\|^2=n(E+s^2)$. Combining (21)--(24),
\[
 \sup_{t\geq0}\|\partial_t^jf_m(t,\cdot)
                 -\partial_t^jf_0(t,\cdot)\|_{L^2}
       =o_{\mathbb P}(1),\quad j=0,1,2.
\tag{25}
\]
Explicitly, the left side is bounded by
\[
 C\|\mathcal T_{k_m-k_0}\|_{\rm op}\|y\|
 +C\|\mathcal T_{k_0}\|_{\rm op}\|K_m-K_0\|_{\rm op}\|y\|.
\]
Both terms tend to zero. The same estimates bound the $L^2$ norms of the predictors and their first two derivatives uniformly by $O_{\mathbb P}(1)$. The teacher has $L^2$ norm $\|\beta\|=O_{\mathbb P}(1)$.

For any twice differentiable predictor $f(t)$ in $L^2$, with teacher $g=x^T\beta$,
\[
 R_f'=2\langle f-g,f'\rangle,\qquad
 R_f''=2\|f'\|^2+2\langle f-g,f''\rangle.
\tag{26}
\]
Cauchy--Schwarz, (25), and the uniform norm bounds transfer (25) to risk and its first two derivatives. Thus it remains to identify the limiting realized risk of $f_0$.

## 7. Linear comparison risk and concentration

Put $T=qX^TX/d$. The identity
$X^TH_t(qXX^T/d+cI)=H_t(T+cI)X^T$
follows first for the matrix exponential by its power series and then by integration. Consequently $f_0(t,x)=x^T\theta(t)$, where
\[
 \dot\theta=-(T+cI)\theta+qX^Ty/d,\qquad \theta(0)=0.
\tag{27}
\]
This ridge in the comparison dynamics comes from the nonlinear kernel diagonal; it was not added to (4).

Write $h_t(\ell)=(1-e^{-(\ell+c)t})/(\ell+c)$. Then
\[
 \theta-\beta=A_t\beta+B_t\varepsilon,
\quad A_t=T h_t(T)-I_d,
\quad B_t=(q/d)h_t(T)X^T.
\tag{28}
\]
In particular, averaging only at this step over (2), conditional on $X$, gives exactly
\[
 \overline R_X(t)=s^2+\frac1d\operatorname{tr}
 \left[E(I-T h_t(T))^2+q s^2 T h_t(T)^2\right].
\tag{29}
\]
The noise coefficient follows from
\[
 \operatorname{Cov}(qX^T\varepsilon/d\mid X)
    =(q^2s^2/d^2)X^TX=(q s^2/d)T.
\tag{30}
\]

It is necessary to show that (29) is also the realized-risk limit. Let $z\in\mathbb R^{d+n}$ be standard Gaussian, independent of $X$, and set
\[
 L_t=[\sqrt{E/d}\,A_t\quad s B_t].
\]
Then $R_0(t)-s^2=z^TL_t^TL_tz$, where $R_0=s^2+\|\theta-\beta\|^2$. On the event $\|X\|\leq C\sqrt d$, for $0\leq j\leq3$,
\[
 \sup_{t\geq0}\|\partial_t^jL_t\|_{\rm op}\leq C/\sqrt d.
\tag{31}
\]
For $j=0$ this follows from $c>0$, $\|T\|\leq C$, and $\|X\|\leq C\sqrt d$. For $j\geq1$, use
$\partial_t^jh_t(T)=(-1)^{j-1}(T+cI)^{j-1}e^{-t(T+cI)}$.

For $j=0,1,2$, let
\[
 Q_j(t)=\sum_{a=0}^j\binom ja
             (\partial_t^aL_t)^T\partial_t^{j-a}L_t.
\]
It is symmetric, $\|Q_j\|_{\rm op}\leq C/d$, and its dimension is $d+n=O(d)$, so $\operatorname{tr}Q_j^2\leq C/d$. Gaussian fourth moments give exactly
\[
 \mathbb E_z[z^TQ_jz]=\operatorname{tr}Q_j,
 \qquad \operatorname{Var}_z(z^TQ_jz)=2\operatorname{tr}Q_j^2\leq C/d.
\tag{32}
\]
Thus $R_0^{(j)}(t)-\overline R_X^{(j)}(t)\to0$ in probability at every fixed $t$. For uniformity on $[0,U]$, apply (32) to a finite grid. Equation (31), also for $j=3$, bounds the time derivatives of these quadratic forms by $C\|z\|^2/d=O_{\mathbb P}(1)$; the corresponding trace derivatives are bounded by a fixed constant. The grid error is therefore $O_{\mathbb P}(\text{mesh size})$. First let dimensions tend to infinity for a fixed grid, then let its mesh size tend to zero. This proves uniform convergence on $[0,U]$.

To pass to all times, (28) has a limit $L_\infty$, and
\[
 \|L_t-L_\infty\|_{\rm op}\leq C d^{-1/2}e^{-ct},
 \quad \|\partial_t^jL_t\|_{\rm op}\leq C d^{-1/2}e^{-ct},\quad 1\leq j\leq3.
\tag{33}
\]
The first bound follows by integrating the exponential tail of $h_t$; the others follow from its displayed derivatives. Hence, uniformly for $t\geq U$,
\[
 |R_0(t)-R_0(\infty)|\leq C(\|z\|^2/d)e^{-cU},
 \quad |R_0^{(j)}(t)|\leq C(\|z\|^2/d)e^{-cU},\quad j=1,2,
\]
and the same bounds hold for conditional expectations with $\|z\|^2/d$ replaced by $(d+n)/d$. The quadratic-form bound (32) applies at $t=\infty$ too. Since $\|z\|^2/d=O_{\mathbb P}(1)$, sending $U\to\infty$ after dimensions tend to infinity proves
\[
 \sup_{t\geq0}|R_0^{(j)}(t)-\overline R_X^{(j)}(t)|
      \xrightarrow{\mathbb P}0,\quad j=0,1,2.
\tag{34}
\]

## 8. Spectral limit

The only random-matrix limit used here is the standard Gaussian Marchenko--Pastur theorem: if $X\in\mathbb R^{n\times d}$ has independent standard normal entries and $d/n\to\gamma>0$, the empirical eigenvalue measure of $X^TX/n$ converges weakly, in probability, to the probability law with atom $(1-\gamma^{-1})_+$ at zero and density
\[
 \frac{\sqrt{((1+\sqrt\gamma)^2-u)(u-(1-\sqrt\gamma)^2)}}{2\pi\gamma u}
 \mathbf1_{((1-\sqrt\gamma)^2,(1+\sqrt\gamma)^2)}(u).
\]
This is the classical sample-covariance theorem of V. A. Marchenko and L. A. Pastur, *Distribution of eigenvalues for some sets of random matrices*, Math. USSR-Sb. 1:4 (1967), 457--483 ([paper page](https://www.mathnet.ru/eng/sm4101)). No random-feature universality or concentration hypothesis is invoked.

Scaling eigenvalues by $qn/d\to q/\gamma$ gives (7) for $T=qX^TX/d$. Its empirical spectral support is contained in a common compact interval with probability tending to one by (10). On that interval the integrands in (29) and their first two time derivatives are continuous in $\ell,t$, since $c>0$. Weak convergence gives convergence for each fixed $t$. Uniformity on any compact time interval follows from uniform bounds on one more time derivative and a finite grid, exactly as above. The integrands converge uniformly in $\ell$ to their $t=\infty$ values at rate $O(e^{-ct})$, with the derivatives tending uniformly to zero. Weak convergence at $t=\infty$ and these tail bounds therefore give
\[
 \sup_{t\geq0}|\overline R_X^{(j)}(t)-R^{(j)}(t)|
       \xrightarrow{\mathbb P}0,\quad j=0,1,2.
\tag{35}
\]
The identity $1-\ell h_t(\ell)=(c+\ell e^{-(\ell+c)t})/(\ell+c)$ converts (29) into (8). Equations (25)--(26), (34), and (35) prove (9).

## 9. Shape of the limiting risk

Here is the earlier density-ratio argument with the sine scaling retained. Put $B=q s^2$, $A=B-Ec$, $k=\ell+c$. Differentiating (8) gives
\[
 \tfrac12R'(t)=\int_{\ell>0}\frac\ell{\ell+c}
 \left[Ae^{-kt}-(Ek+A)e^{-2kt}\right]\nu(d\ell).
\tag{36}
\]
If $E>0,A\leq0$, the integrand is strictly negative on the positive spectral interval: $Ek+A=E\ell+B>0$. If $E=0$, (36) is positive for $s^2>0,t>0$ and zero for zero noise. This proves the corresponding classifications.

Suppose $E>0,A>0$, set $a=c+\ell_-$, $b=c+\ell_+$, and define
\[
 w(k)=\frac1{2\pi q}\frac{\sqrt{(b-k)(k-a)}}k
                \mathbf1_{(a,b)}(k),
\quad
 h(k)=Aw(k)-\tfrac12(Ek/2+A)w(k/2).
\tag{37}
\]
The atom at zero contributes no derivative. Changing variables in the second term of (36) gives
$F(t):=R'(t)/2=\int e^{-kt}h(k)\,dk$.
If $b\leq2a$, $h$ is positive on $(a,b)$, negative on $(2a,2b)$, and has one change of sign, with any separating point in $[b,2a]$.

If $2a<b$, the ratio of the subtracted density to $w(k)$, on $2a<k<b$, is
\[
 Q(k)=(Ek/2+A)
 \sqrt{\frac{b-k/2}{b-k}\frac{k/2-a}{k-a}}.
\tag{38}
\]
The derivatives of the two rational factors are
$b/(2(b-k)^2)>0$ and $a/(2(k-a)^2)>0$.
Here $a\geq c>0$. Thus $Q$ is strictly increasing from zero to infinity, so there is a unique $r\in(2a,b)$ with $Q(r)=A$. On the overlap $h=w(A-Q)$, and on the remaining supports its signs are again positive first and negative last. In either case there is a separator $r$ with
$h\geq0$ below $r$, $h\leq0$ above $r$, with strict inequalities on intervals of positive length on each side. Therefore
\[
 \frac d{dt}(e^{rt}F(t))
   =\int(r-k)e^{(r-k)t}h(k)\,dk>0.
\tag{39}
\]
Also $F(0)=-E\int k w(k)\,dk<0$. Choose $u<r$ so
$H=\int_{k\leq u}h(k)\,dk>0$, and let $N=\int_{k>r}|h(k)|\,dk$. Then
$F(t)\geq H e^{-ut}-Ne^{-rt}>0$ for all sufficiently large $t$.
Consequently $F$ has exactly one zero $t_*$, and at that zero (39) gives $F'(t_*)>0$. This proves the nondegenerate-minimum assertion.

Finally, fix $U>t_*$. Choose a neighborhood of $t_*$ inside $(0,U)$ on which $R''$ is bounded below by a positive constant. On the compact complement in $[0,U]$, $|R'|$ has a positive lower bound, with its known negative/positive signs. The uniform first- and second-derivative convergence in (9) gives exactly one finite-network zero in that neighborhood and none in its complement, with probability tending to one. Making the neighborhood arbitrarily small proves convergence of the zero to $t_*$.

## 10. Independent checks and limitations

The leading linear kernel coefficient can be obtained independently from Gaussian integration by parts: for $G\sim N(0,1)$,
$\mathbb E[G\sin G]=\mathbb E[\cos G]=e^{-1/2}$.
Its square is $q=e^{-1}$. Also
$\mathbb E\sin^2G=(1-e^{-2})/2$, so subtracting the degree-one energy gives precisely $c$ in (6). This checks both kernel constants without expanding (12).

The noise coefficient in (8) has an independent short-time check. Equation (27) gives $\dot\theta(0)=T\beta+qX^T\varepsilon/d$. Direct expansion of $s^2+\|\theta-\beta\|^2$, after averaging, gives
\[
 \overline R_X'(0)=-2E\operatorname{tr}T/d,
\quad
 \overline R_X''(0)=\frac1d\operatorname{tr}
       (4ET^2+2EcT+2q s^2T).
\tag{40}
\]
The same expressions result by twice differentiating the two terms in (8). In particular the first two spectral moments are
\[
 \int\ell\,d\nu=q/\gamma,
\qquad \int\ell^2\,d\nu=q^2(1+\gamma)/\gamma^2.
\tag{41}
\]
For a direct matrix check, $\mathbb E\operatorname{tr}(X^TX)=nd$ and
$\mathbb E\operatorname{tr}((X^TX)^2)=nd(n+d+1)$: expand the trace as $\sum_{i,j}(x_i^Tx_j)^2$, whose diagonal terms have expectation $d(d+2)$ and off-diagonal terms $d$. Scaling by $q/d$ gives (41). Thus
\[
 R'(0)=-2Eq/\gamma,
\quad
 R''(0)=4Eq^2(1+\gamma)/\gamma^2+2Ecq/\gamma+2q^2s^2/\gamma.
\]
The $q s^2$ factor in (8), rather than $s^2$ or $q^2s^2$, is required by these two independent derivations.

The cubic test estimate has a further cancellation check: in (19) the coefficients of $v$ are $1-2+1=0$, those of $v^2$ are $1-1=0$, and the coefficient of $v^3$ is $2/3-1/4=5/12$. This equals $\mathbb E Z_v^6/36=15v^3/36$, as predicted by $\sinh z-z=z^3/6+O(z^5)$.

For a second check of (11), independence across coordinates gives the exact moment generating function
\[
 \mathbb E e^{u x_i^Tx_j/d}=(1-u^2/d^2)^{-d/2},\qquad |u|<d.
\]
The coefficient of $u^6$, multiplied by $6!$, is
$6!(d/2)(d/2+1)(d/2+2)/(3!d^6)=15d(d+2)(d+4)/d^6$.
For a second check of the radial estimate, differentiating
$\mathbb E e^{-ar}=(1+2a/d)^{-d/2}$ gives
\[
 \tau_d=(1+2/d)^{-d/2-1}
       -2e^{-1/2}(1+1/d)^{-d/2-1}+e^{-1}
       =\frac{e^{-1}}{2d}+O(d^{-2}).
\]
The last expansion is the Taylor expansion of the logarithms at $1/d=0$. Its sign and order agree with (18), while (18) itself supplies the dimension-uniform upper bound used in the proof.

The case $\gamma>1$ retains the atom at zero; it contributes constant signal risk $E(1-\gamma^{-1})$. At $\gamma=1$ the continuous density is singular at zero, but $c>0$ makes all filters continuous and bounded there. Zero noise gives strict decrease for positive signal. At zero signal the derivative vanishes at $t=0$, so its minimum is a boundary minimum. These cases do not require a limiting inverse of $T$.

This theorem uses a Gaussian random linear teacher, zero output initialization, bounded sine activation, an output-only flow, and the sufficient width condition $m/n^2\to\infty$. It does not establish the same limit for $m/n\to\infty$ alone, for proportional width, for a nonzero random output initialization, for ReLU, or for feature learning. The diagonal correction in the kernel produces an effective ridge only in the comparison predictor; the original network remains unregularized. Uniform absolute derivative convergence does not control the sign of exponentially small derivatives at dimension-dependent late times. Neither a double-descent example nor the peak-time asymptotic requested in T267 follows.
