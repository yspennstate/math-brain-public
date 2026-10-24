# Fixed-twist obstruction for two independent planar banks

A joint density cap for each of two independent banks does not control their twisted Fourier integral. This is a counterexample to a possible intermediate estimate, **not** to the original-product conjecture.

Use \(\widehat f(\xi)=\int e^{i\xi x}f(x)\,dx\).

**Proposition.** For every even \(N\ge2\) there are independent planar random vectors \((A,B),(C,D)\), each with joint density at most \(1\), and modulus-one bank phases \(\omega_1(A),\omega_2(C)\), such that
\[
\iint_{\mathbb R^2}\left|
\mathbb E\,\omega_1(A)\omega_2(C)
e^{i[y(A+C)+z(B+D)+AC]}\right|\,dy\,dz
\ge c\frac{\sqrt N}{\log(eN)}.
\]

**Proof.** Fix \(w\in C_c^\infty([-1,1])\) with \(w\ge0,\int w=1,\|w\|_\infty\le1\). Set
\[
d_N=\sqrt{2\pi(1+N^{-1})},\qquad
\rho_N(x)=\sum_{j=0}^{N-1}w(N(x-jd_N)).
\]
Its \(N\) supports are disjoint, so \(\rho_N\le1\) and \(\int\rho_N=1\). Give both banks density \(\rho_N(a)w(b)\), and take \(\omega_1(a)=e^{ia^2/2}\), \(\omega_2(c)=e^{ic^2/2}\). Since \(a^2/2+c^2/2+ac=(a+c)^2/2\), the twisted transform factors as
\[
\widehat h_N(y)\widehat w(z)^2,\qquad
h_N(s)=e^{is^2/2}(\rho_N*\rho_N)(s).
\]
Thus the asserted integral is \(2\pi\|w\|_2^2\|\widehat h_N\|_1\).

Put \(\psi=w*w\), and \(r_m=\#\{(j,k):0\le j,k<N,\ j+k=m\}\). Then
\[
\rho_N*\rho_N(s)=\sum_{m=0}^{2N-2}\frac{r_m}{N}\psi(N(s-md_N)).
\tag{1}
\]
The supports in (1) are disjoint, and \(\sum_mr_m^2=(2N^3+N)/3\). Hence
\[
\|h_N\|_2^2=\frac{\|\psi\|_2^2}{N^3}\sum_mr_m^2
\ge \frac23\|\psi\|_2^2.
\tag{2}
\]
Differentiation of (1), using \(|s|\le C N\) on its support, gives \(\|h_N'\|_2\le C_wN\). Plancherel therefore gives a fixed \(K_w\) such that
\[
\int_{|y|\le K_wN}|\widehat h_N(y)|^2dy\ge c_w>0.
\tag{3}
\]

For \(|y|\le K_wN\), substituting \(s=md_N+t/N\) into (1) gives
\[
\widehat h_N(y)=\frac1N\sum_{m=0}^{2N-2}
a_m(y)e^{i\pi m^2/N+i(\pi+yd_N)m},
\quad
a_m(y)=\frac{r_m}{N}\int\psi(t)
e^{i(d_Nm+y)t/N+it^2/(2N^2)}dt.
\tag{4}
\]
The triangular sequence \(r_m/N\) and compact support of \(\psi\) show, uniformly for \(|y|\le K_wN\),
\[
\max_m|a_m(y)|+\sum_m|a_{m+1}(y)-a_m(y)|\le C_w.
\tag{5}
\]

For even \(N\), \(q_m=e^{i\pi m^2/N}\) is \(N\)-periodic, and all its \(N\) discrete Fourier coefficients have modulus \(N^{-1/2}\): expand the squared coefficient and sum the character in one index, which vanishes unless the index difference is \(0\pmod N\). Expanding \(q\) in Fourier series and bounding each resulting geometric sum by a Dirichlet kernel gives, for every real \(\theta\) and every interval \(I\subset\{0,\ldots,2N-2\}\),
\[
\left|\sum_{m\in I}e^{i\pi m^2/N+i\theta m}\right|
\le C\sqrt N\log(eN).
\tag{6}
\]
Indeed, the sum of the moduli of geometric sums over the \(N\) equally spaced frequency translates is \(O(N\log(eN))\). Abel summation of (4), using (5) and (6), yields
\[
\sup_{|y|\le K_wN}|\widehat h_N(y)|
\le C_w\log(eN)/\sqrt N.
\tag{7}
\]
Equations (3) and (7) imply
\(\|\widehat h_N\|_1\ge c_w\sqrt N/\log(eN)\), as required.

**Boundary of the result.** These are capped *bank* densities and phases separated by bank. The construction supplies no diffuse orthonormal original-coordinate projection. In the direct four-coordinate embedding \(L=(A+C)/\sqrt2,V=(B+D)/\sqrt2\), the \(A,C\) rows already have leverage \(1/2\); nonzero \(P\) coefficients on them would violate the row-leverage gate. Splitting each bank variable into several original inputs avoids that immediate gate but makes \(e^{iA^2/2}\) and \(e^{iC^2/2}\) nonseparable in the original inputs. The genuine-product twisted Wiener question remains open.
