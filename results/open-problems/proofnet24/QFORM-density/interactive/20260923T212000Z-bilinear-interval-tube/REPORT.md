# Two-bank bilinear interval-tube estimate with an exactly linear hub

Date: 2026-09-23. Status: **proved scoped interval estimate**, insufficient for the full bounded-density conjecture.

## Statement

Let A=(L_A,V_A) and B=(L_B,V_B) be independent random vectors on R² with probability densities a,b bounded by M_A,M_B. Let H be any independent random variable; a density assumption on H is not needed for the first bound. Let
\[
C=\begin{pmatrix}a_0&b_0\\c_0&2\end{pmatrix}
\]
have arbitrary real entries apart from \(C_{VV}=2\), and let \(R_A(A),R_B(B)\) be arbitrary real measurable bank-local phases. Put
\[
L=L_A+L_B,\qquad
F=A^{\mathsf T}CB+R_A(A)+R_B(B),\qquad Q=2HL+F.
\]
There is a numerical constant K such that, for every \(r,\delta>0\) and every interval I of length \(\delta\),
\[
\boxed{\quad
\Pr\{|L|\le r,\ F\in I\}
\le K\sqrt{M_AM_B}\,r\sqrt\delta .
\quad}\tag{1}
\]
The same bound holds with F replaced by Q, uniformly in the law of the independent H:
\[
\Pr\{|L|\le r,\ Q\in I\}
\le K\sqrt{M_AM_B}\,r\sqrt\delta .
\tag{2}
\]
Both statements remain valid if \(|L|\le r\) is replaced by any measurable L-set of length at most \(2r\), including a dyadic shell \(r\le |L|\le2r\) after replacing r by 2r. There is no support, moment, smoothness, or marginal-density-cap assumption beyond the two planar bank caps.

If additionally H has a probability density bounded by one, then conditioning on the banks gives
\[
\Pr\{Q\in I\}\le
K\sqrt{M_AM_B}\,r\sqrt\delta+\frac{\delta}{2r}
\quad(r>0),
\]
and optimization yields a universal \(O((M_AM_B)^{1/4}\delta^{3/4})\) interval estimate. This exponent is weaker than the required \(O(\delta)\), and in product-source settings with a capped L marginal, the elementary \(O(\delta\log(1/\delta))\) hub estimate is stronger.

## Bilinear interval lemma for subprobabilities

Let p(v),q(w) be nonnegative subprobability densities of masses \(\alpha,\beta\) and caps \(M_A,M_B\). For arbitrary real measurable \(u(v),z(w)\), set
\[
T=2vw+u(v)+z(w)
\]
under the product subprobability measure \(p(v)q(w)dv,dw\). Then every interval J of length \(\delta\) obeys
\[
\int p(v)q(w)\mathbf 1_J(2vw+u(v)+z(w))\,dv,dw
\le K_0\sqrt{M_AM_B\alpha\beta\delta}.
\tag{3}
\]

To verify (3), let \(\Phi(t)\) be the characteristic transform of this finite measure. With \(\widehat g(\xi)=\int e^{-i\xi x}g(x)dx\), Plancherel and Cauchy–Schwarz for the kernel \(e^{2itvw}\) give
\[
|\Phi(t)|
\le\sqrt{\frac{\pi}{|t|}}\,
\|p\|_2\|q\|_2
\le\sqrt{\frac{\pi M_AM_B\alpha\beta}{|t|}},
\qquad t\ne0.
\tag{4}
\]
The local phases only multiply p and q by unit-modulus factors, so (4) is uniform in u,z. A nonnegative Fejér-type majorant of \(\mathbf1_J\), with Fourier support \(|t|\le1/\delta\) and pointwise size at most a numerical multiple of \(\delta\) times its normalized kernel, gives
\[
\mu(J)\le K_1\delta
\int_{-1/\delta}^{1/\delta}|\Phi(t)|dt
\le K_0\sqrt{M_AM_B\alpha\beta\delta}.
\]
The singularity \(|t|^{-1/2}\) is integrable at zero. This argument works for rough and unbounded subprobability densities by L2 Plancherel and Tonelli.

## Proof of the tube estimate

For almost every l,m, set
\[
\alpha(l)=\int a(l,v)dv,\qquad
\beta(m)=\int b(m,w)dw.
\]
These are nonnegative L1 functions of total mass one. At fixed \(L_A=l,L_B=m\), the cross phase is
\[
a_0lm+b_0lw+c_0vm+2vw+R_A(l,v)+R_B(m,w).
\]
The first term is constant; the terms linear in v or w can be absorbed into the arbitrary bank-local offsets in (3). The planar slice densities \(a(l,\cdot),b(m,\cdot)\) retain caps \(M_A,M_B\) and have submasses \(\alpha(l),\beta(m)\). Therefore (3) bounds their contribution to F∈I by
\[
K_0\sqrt{M_AM_B\delta}\,
\sqrt{\alpha(l)\beta(m)}.
\]
Integrate over \(|l+m|\le r\). By Cauchy–Schwarz,
\[
(\sqrt\alpha*\sqrt\beta)(s)
\le\|\sqrt\alpha\|_2\|\sqrt\beta\|_2=1
\]
for every s (with the harmless reflection appropriate to l+m). The interval \(|s|\le r\) has length 2r, so (1) holds with \(K=2K_0\). For fixed h, the extra term \(2h(l+m)\) merely translates the target interval at each l,m; (3) is uniform in that translation. Integrate h against any independent probability law to obtain (2).

If H has a density at most one, then on \(|L|>r\), conditional on A,B the map \(h\mapsto2hL+F\) gives interval probability at most \(\delta/(2|L|)\le\delta/(2r)\). This proves the displayed global \(\delta^{3/4}\) consequence.

## Why this does not yield a bounded density

To bound a density at a fixed output s by conditioning on a cap-one H, the relevant expression on a dyadic shell \(|L|\asymp r\) contains
\[
\frac1{2|L|}
f_H\!\left(\frac{s-F}{2L}\right).
\]
A cap-one hub may be the indicator of an arbitrary measurable set of measure one. At fixed l,m, its preimage in the F variable can be highly fragmented, with total Lebesgue measure proportional to r. Estimate (3) applies to **one interval** and does not control such arbitrary measurable sets: summing its square-root bounds across many tiny components can diverge. An arbitrary-measurable-target version of (3) with a positive power of the target measure would give a summable dyadic gain, but that stronger bilinear-offset inequality remains unproved. Combining (2) with the ordinary hub conditioning estimate leaves a logarithmic or worse scale loss rather than the required O(\delta) small-ball bound.
