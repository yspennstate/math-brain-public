# Finite-​P-support Fourier receiver for the canonical rank-three form

Date: 2026-09-23. Status: **proved scoped theorem; the unrestricted product-source problem remains open**.

## Statement

Use the Fourier convention \(\widehat g(\xi)=\int e^{-i\xi\cdot x}g(x)\,dx\). Let \(H\) have density \(f_H\) with \(0\le f_H\le1\). Independently of \(H\), let \(A=(L_A,V_A,P_A)\) and \(B=(L_B,V_B,P_B)\) be independent random vectors with probability densities \(a,b\) on \(\mathbb R^3\), satisfying \(\|a\|_\infty\le M_A\), \(\|b\|_\infty\le M_B\). Suppose \(P_A\) and \(P_B\) are supported, respectively, on arbitrary measurable sets \(E_A,E_B\subset\mathbb R\) of finite Lebesgue measures \(R_A,R_B\). The sets need not be intervals or bounded.

Put \((L,V,P)=A+B\). For **every** \(\varepsilon\in\mathbb R\), the quadratic random variable
\[
Q=2HL+V^2+2\varepsilon LP
\]
has a bounded continuous density satisfying
\[
\boxed{\ \|p_Q\|_\infty\le 3(R_A R_B M_A M_B)^{1/3}.\ }
\]
There is no dependence on \(\varepsilon\), on the locations or geometry of \(E_A,E_B\), or on support/moments/regularity of \(f_H\).

The bank laws can, in particular, be genuine product-source projections; the proof requires only independence of the two *banks* and their full three-dimensional density caps. The extra hypothesis is finite measure of the bankwise \(P\)-supports. This hypothesis is not available in the original unrestricted problem.

## Step 1: a planar slice Wiener bound

Write \(F=a*b\), the three-dimensional density of \((L,V,P)\). For almost every \(p\), set
\[
F_p(l,v)=F(l,v,p),\quad
a_p(l,v)=a(l,v,p),\quad b_p(l,v)=b(l,v,p).
\]
Define the nonnegative slice Fourier integral
\[
\mathcal B(F)=\int_{\mathbb R}dp\int_{\mathbb R^2}
  |\widehat{F_p}(\xi)|\,d\xi .
\]
For almost every \(\xi\in\mathbb R^2\), three-dimensional convolution and Fubini give
\[
\widehat{F_p}(\xi)=
\int_{\mathbb R}\widehat{a_u}(\xi)\widehat{b_{p-u}}(\xi)\,du
=(\widehat{a_\cdot}(\xi)*_p\widehat{b_\cdot}(\xi))(p).
\]
This is legitimate even for rough bank densities: \(|\widehat{a_p}(\xi)|\le\int a_p\), and integration of the latter over \(p\) is one; likewise for \(b\). Young's \(L^1(\mathbb R_p)\) inequality, then Cauchy–Schwarz on the finite-measure \(P\)-supports, gives
\[
\begin{aligned}
\mathcal B(F)
&\le\int_{\mathbb R^2}
 \|\widehat{a_\cdot}(\xi)\|_{L^1_p}
 \|\widehat{b_\cdot}(\xi)\|_{L^1_p}\,d\xi\\
&\le \sqrt{R_A R_B}
\left(\int_{\mathbb R^2}\int_{\mathbb R}
 |\widehat{a_p}(\xi)|^2\,dp\,d\xi\right)^{1/2}
\left(\int_{\mathbb R^2}\int_{\mathbb R}
 |\widehat{b_p}(\xi)|^2\,dp\,d\xi\right)^{1/2}\\
&=(2\pi)^2\sqrt{R_A R_B}\,\|a\|_2\|b\|_2
\le (2\pi)^2\sqrt{R_A R_B M_A M_B}.
\end{aligned}
\]
The equality is planar Plancherel at fixed \(p\), integrated in \(p\); the last inequality uses probability mass one and the density caps.

## Step 2: signed hub integration and Fresnel decay

Fix \(p\), and temporarily insert the Gaussian cutoff \(e^{-\eta(l^2+v^2)}\), \(\eta>0\), in the \((l,v)\)-integral defining the characteristic function. Since \(\widehat{F_p}\in L^1(\mathbb R^2)\) for almost every \(p\), planar Fourier inversion is valid. The \(v\)-integral obeys the standard complex Gaussian estimate
\[
\left|\int_{\mathbb R}e^{-(\eta-it)v^2+i\xi_v v}\,dv\right|
\le\sqrt{\pi/|t|}\qquad(t\ne0).
\]
For the \(l\)-integral, including the independent hub and with \(c=\varepsilon p\), positivity and \(f_H\le1\) give
\[
\begin{aligned}
&\left|\int_{\mathbb R} f_H(h)
 \int_{\mathbb R}e^{-\eta l^2+i(\xi_l+2t(h+c))l}\,dl\,dh\right|\\
&\qquad\le\int_{\mathbb R}
 \sqrt{\pi/\eta}\,
 e^{-(\xi_l+2t(h+c))^2/(4\eta)}\,dh
=\frac{\pi}{|t|}.
\end{aligned}
\]
Consequently, Fourier inversion with its \((2\pi)^{-2}\) factor yields, uniformly in \(\eta,p,c\),
\[
|I_{p,\eta}(t)|
\le \frac{1}{4\sqrt\pi}|t|^{-3/2}
\|\widehat{F_p}\|_1.
\]
Integrate in \(p\), use \(\mathcal B(F)<\infty\), and let \(\eta\downarrow0\). On the physical probability space the cutoff increases pointwise to one and the integrands are dominated by the probability density, so dominated convergence gives
\[
|\phi_Q(t)|\le \frac{\mathcal B(F)}{4\sqrt\pi}|t|^{-3/2}
\quad(t\ne0).
\]
This step retains the *signed* Fourier inversion of the arbitrary rough hub density. Taking \(|\widehat f_H|\) instead would lose uniformity.

Finally \(|\phi_Q(t)|\le1\). Let \(K=\mathcal B(F)/(4\sqrt\pi)\). Split the inversion integral at the optimized threshold \(T=K^{2/3}\):
\[
\begin{aligned}
\|p_Q\|_\infty
&\le\frac1{2\pi}\int_{\mathbb R}\min(1,K|t|^{-3/2})\,dt\\
&=\frac1\pi\left(T+K\int_T^\infty t^{-3/2}\,dt\right)
=\frac3\pi K^{2/3}\\
&\le 3(R_A R_B M_A M_B)^{1/3}.
\end{aligned}
\]
Since \(\phi_Q\in L^1\), inversion gives a bounded continuous density.

## Bank-local phase robustness

The same bound holds for
\[
Q^*=2HL+V^2+2\varepsilon LP+\rho_H(H)
+\rho_A(\Omega_A)+\rho_B(\Omega_B),
\]
where \(\Omega_A,\Omega_B\) are the underlying independent bank random objects whose projections are \(A,B\), and \(\rho_H,\rho_A,\rho_B\) are arbitrary real measurable functions of only their indicated independent sources. In particular, these phases may be rough and depend on \(t\) through their factors \(e^{it\rho_i}\).

Indeed, at each Fourier frequency \(t\), push forward \(e^{it\rho_A}\) times the law of \(\Omega_A\) to a complex bank density \(a_t\); conditional expectation gives \(|a_t|\le a\) almost everywhere, so \(\|a_t\|_2\le\|a\|_2\) and its \(P\)-support remains in \(E_A\). The analogous assertions hold for \(b_t\). The complex light density \(a_t*b_t\) has the same slice Wiener estimate as above, while the hub factor \(f_H(h)e^{it\rho_H(h)}\) has modulus at most one. The Gaussian \(l\)-integral is bounded by its absolute Gaussian integral against this hub factor. Thus every estimate in Steps 1–2 is uniform in \(t\) and the three local phases, and the same Fourier inversion bound follows. This does **not** permit a phase coupling the two banks or coupling a bank back to the hub beyond the displayed canonical terms.

## Rényi-tail extension

The finite-\(P\)-support assumption can be weakened quantitatively. Partition the \(P\)-axis into unit intervals \(I_k=[k,k+1)\), \(k\in\mathbb Z\), and let
\[
m_{A,k}=\Pr(P_A\in I_k),\qquad
m_{B,j}=\Pr(P_B\in I_j).
\]
If \(\sum_k m_{A,k}^{2/3}<\infty\) and \(\sum_j m_{B,j}^{2/3}<\infty\), then, including arbitrary bank-local phases as above,
\[
\boxed{\quad
\|p_{Q^*}\|_\infty
\le 3(M_A M_B)^{1/3}
\left(\sum_k m_{A,k}^{2/3}\right)
\left(\sum_j m_{B,j}^{2/3}\right).
\quad}
\]
To prove this, restrict bank \(A\) to \(P_A\in I_k\) and bank \(B\) to \(P_B\in I_j\). These are subprobability densities of masses \(\alpha=m_{A,k}\) and \(\beta=m_{B,j}\), with unchanged pointwise caps and unit \(P\)-support measures. The two characteristic-function bounds for this pair are
\[
|\phi_{k,j}(t)|\le\alpha\beta,\qquad
|\phi_{k,j}(t)|\le
\pi^{3/2}\sqrt{M_A M_B\alpha\beta}\,|t|^{-3/2}.
\]
Optimizing the Fourier inversion split as in Step 2 gives
\(\|p_{k,j}\|_\infty\le3(M_A M_B)^{1/3}(\alpha\beta)^{2/3}\).
The full output law is the positive sum of the independent bank-bin pair laws, so summing the bounds proves the claim. The criterion includes some unbounded and highly fragmented \(P\)-supports; the two Rényi sums can diverge for admissible laws, so it does not settle the unrestricted problem.

## Optional exact shear for \(\beta\ne0\)

For \(\varepsilon\ne0\), set \(P'=P+\beta L/(2\varepsilon)\). Then
\(2HL+\beta L^2+V^2+2\varepsilon LP=2HL+V^2+2\varepsilon LP'\).
The preceding theorem applies **only if** each sheared bank coordinate
\(P'_i=P_i+\beta L_i/(2\varepsilon)\) has support of finite measure \(R'_i\), with the bound using \(R'_A,R'_B\). The shear has determinant one, so the three-dimensional density caps remain \(M_A,M_B\). Finite support measure of \(P_i\) alone does not imply a controlled support measure for \(P'_i\) when \(L_i\) is unrestricted.

## Scope and remaining gap

The theorem permits bank-local dependence of \(L_i,V_i,P_i\), arbitrary fragmentation of the hub and bank laws, and arbitrary \(\varepsilon\). It proves a uniform density bound whenever the two bankwise \(P\)-supports have finite measure with controlled \((R_A R_B M_A M_B)^{1/3}\). In the full RMT/QFORM problem the original-coordinate supports are unrestricted and the projected \(P_i\)-supports can have infinite measure. The slice Wiener integral \(\mathcal B(F)\) is then not controlled by bank density caps alone, and this report does not settle the full problem.
