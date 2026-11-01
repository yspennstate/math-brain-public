# Failure of sub-\(L^2\) Fourier control for an independent bilinear product

**Scope.** The statement below concerns the characteristic function of \(HL\) for independent one-dimensional, density-at-most-one random variables. It disproves a proposed uniform \(L^p\) shortcut for \(p<2\). It does **not** disprove the rank-three quadratic-form density conjecture.

## Proposition

For every \(1\leq p<2\),
\[
\sup_{\substack{H,L\ \mathrm{independent}\\
 \|f_H\|_\infty,\|f_L\|_\infty\leq1}}
 \int_{\mathbb R}\big|\mathbb E e^{2itHL}\big|^p\,dt
 =\infty.
\]
The supremum remains infinite if \(H,L\) are identically distributed and their densities are supported in the fixed interval \([1,4]\). More precisely, for the densities constructed below, there are constants \(c>0,N_0\) such that
\[
\big|\mathbb E e^{itH_NL_N}\big|\geq cN^{-1/2}
 \quad\text{for all }t\in[N/3,N/2],\quad N\geq N_0.
\]
The factor \(2\) in the first display only rescales the frequency.

## Explicit admissible densities

For integers \(N\geq6\), define
\[
J_N=\int_1^4\cos(N\log x)\,dx,\qquad
b_N=(3+J_N)^{-1},\qquad
f_N(x)=b_N(1+\cos(N\log x))\mathbf1_{[1,4]}(x).
\]
Then \(f_N\geq0\) and \(\int f_N=1\). Also
\[
|J_N|
 \leq \left|\int_1^4 x^{iN}\,dx\right|
 =\left|\frac{4^{1+iN}-1}{1+iN}\right|
 \leq\frac5{\sqrt{1+N^2}}.
\]
In particular \(3+J_N>2\) for \(N\geq6\), so \(f_N\leq2b_N<1\). Let \(H_N,L_N\) be independent with this density. Notice \(b_N\to1/3\).

## Exact product-density decomposition

Let \(Z_N=H_NL_N\), with density \(g_N\). For \(z\in[1,16]\), set
\[
a(z)=\max\{0,\log(z/4)\},\quad
d(z)=\min\{\log4,\log z\},\quad
c(z)=d(z)-a(z).
\]
Thus \(c(z)=\log z\) on \([1,4]\), \(c(z)=\log(16/z)\) on \([4,16]\), and \(c=0\) outside \([1,16]\). Changing variables \(h=e^u\) in the product-density formula gives
\[
g_N(z)=b_N^2\int_{a(z)}^{d(z)}
 [1+\cos(Nu)][1+\cos(N(\log z-u))]\,du.
\]
Use \(\cos A\cos B=\tfrac12\cos(A+B)+\tfrac12\cos(A-B)\). The terms with phases \(Nu\), \(N(\log z-u)\), and \(2Nu-N\log z\) have integrals of absolute size at most \(2/N,2/N,1/(2N)\), respectively, for every pair of integration endpoints. Therefore
\[
g_N(z)=b_N^2c(z)\bigl(1+\tfrac12\cos(N\log z)\bigr)+b_N^2r_N(z),
 \qquad |r_N(z)|\leq 5/N,
\]
where \(r_N\) is supported in \([1,16]\). This identity exposes a coherent log-periodic oscillation of fixed amplitude in the product density.

## Uniform stationary-phase lower bound

Write \(\Phi_N(t)=\mathbb E e^{-itZ_N}\). Define
\[
C(t)=\int_1^{16}c(z)e^{-itz}\,dz,\qquad
I_\pm(t)=\int_1^{16}c(z)e^{\pm iN\log z-itz}\,dz.
\]
The decomposition above reads
\[
\Phi_N(t)=b_N^2\left[C(t)+\tfrac14 I_+(t)+
                         \tfrac14 I_-(t)+R_N(t)\right],
 \qquad |R_N(t)|\leq75/N.
\]

Fix \(t\in[N/3,N/2]\), put \(\lambda=t/N\in[1/3,1/2]\), and let \(z_*=1/\lambda=N/t\in[2,3]\). Since \(c\) is compactly supported and piecewise \(C^1\), integration by parts on \([1,4]\) and \([4,16]\) gives \(|C(t)|=O(N^{-1})\). The phase of \(I_-\) is \(-N(\log z+\lambda z)\), whose derivative never vanishes on \([1,16]\); the same piecewise integration by parts gives \(|I_-(t)|=O(N^{-1})\), uniformly in \(\lambda\).

The phase of \(I_+\) is \(N(\log z-\lambda z)\). It has its unique stationary point \(z_*\in[2,3]\), where its second derivative is \(-N/z_*^2\). A smooth cutoff supported in \((3/2,7/2)\), equal to one on \([2,3]\), isolates this stationary point. Ordinary one-dimensional stationary phase on that cutoff, followed by piecewise integration by parts on its complement, is uniform for \(\lambda\in[1/3,1/2]\) and gives
\[
I_+(t)
=c(z_*)z_*\sqrt{\frac{2\pi}{N}}\,
 e^{\,i[N\log z_*-N-\pi/4]}+O(N^{-1}).
\]
All implied constants are absolute: the cutoff keeps the stationary point a fixed distance from \(1,4,16\), and the phase derivative on the complementary support has a fixed positive lower bound after division by \(N\). Since \(c(z_*)z_*=z_*\log z_*\geq2\log2\), it follows for all sufficiently large \(N\) that
\[
|\Phi_N(t)|\geq cN^{-1/2}
\quad\text{uniformly for }t\in[N/3,N/2].
\]
Complex conjugation changes \(e^{-itZ_N}\) to \(e^{itZ_N}\) without changing its modulus. Consequently
\[
\int_{\mathbb R}|\mathbb E e^{itH_NL_N}|^p\,dt
 \geq (N/6)c^p N^{-p/2}
 =\frac{c^p}{6}N^{1-p/2}\longrightarrow\infty
 \quad (p<2).
\]
Replacing \(t\) with \(2t\) proves the proposition as stated.

## Relevance and limit

An attempted route to the quadratic density bound would combine an \(L^{3/2}\) estimate for the bilinear factor \(\mathbb E e^{2itHL}\) with a complementary Fourier estimate for a square term. The proposition rules out any distribution-uniform \(L^p\) estimate for that bilinear factor when \(p<2\), even for independent original variables and compactly supported cap-one laws.

It says nothing about the density of \(2HL+V^2\), much less the target \(2(H+\varepsilon W)L+V^2\): the square term and the signed interaction of their Fourier phases can supply cancellation absent from the isolated bilinear-factor norm. The entire result is independent of any affine coefficient or conditional law in the broader QFORM problem.


## Sharp \(L^2\) endpoint and a physical-space comparison

The preceding failure has the precise threshold \(p=2\). For any independent cap-one \(H,L\), let \(g\) denote the density of \(HL\). Expanding \(\|g\|_2^2\) and changing variables in one product-density factor yields
\[
\begin{aligned}
\|g\|_2^2
&=\iint f_H(h)f_H(h')\,\frac1{|h'|}
 \int f_L(\ell)f_L((h/h')\ell)\,d\ell\,dh\,dh'\\
&\leq \iint \frac{f_H(h)f_H(h')}
                    {\max\{|h|,|h'|\}}\,dh\,dh'.
\end{aligned}
\]
Indeed the inner integral is at most both \(1\) (using \(f_L\leq1\)) and \(|h'|/|h|\) (changing variables and again using \(f_L\leq1\)). Put \(\rho(r)=f_H(r)+f_H(-r)\), \(r>0\), and \(F(R)=\int_0^R\rho(r)\,dr\). As \(\rho\leq2\), \(F(R)\leq2R\), and consequently
\[
\|g\|_2^2\leq
 2\int_0^\infty \rho(R)\frac{F(R)}R\,dR\leq4.
\]
Equality holds when both variables are uniform on \([-1/2,1/2]\): then \(g(z)=2\log(1/(4|z|))\) for \(0<|z|<1/4\), whose squared integral is \(4\). Plancherel in the convention \(\widehat g(t)=\int e^{-itz}g(z)\,dz\) thus gives the **sharp** bound
\[
\int_{\mathbb R}|\mathbb E e^{itHL}|^2\,dt\leq8\pi
\quad\left(\text{or }\
 \int_{\mathbb R}|\mathbb E e^{2itHL}|^2\,dt\leq4\pi\right).
\]
Since characteristic functions have modulus at most one, they also have uniform \(L^p\) bounds for every \(p\geq2\).

The physical-space product density is nevertheless bounded in \(L^r\) for **every finite** \(r\). Splitting the product-density integral over \(|h|\geq1\), \(|z|\leq|h|<1\), and \(|h|<|z|\) gives
\[
g(z)\leq 2+2\log(1/|z|)\quad(0<|z|\leq1),
 \qquad g(z)\leq2\quad(|z|\geq1).
\]
For the last region substitute \(\ell=z/h\) to bound its integral by \(\int_{|\ell|>1}f_L(\ell)/|\ell|\,d\ell\leq1\). The same partition with \(|z|\geq1\) gives the second estimate. Integrability of every finite power of the logarithm near zero, and \(g^r\leq2^{r-1}g\) off \([-1,1]\), finish the claim. Uniform \(L^r\) control of a density for all finite \(r\) does not imply uniform \(L^p\) control of its Fourier transform for \(p<2\).
