# A genuine-product counterexample to linear twisted Wiener control

## Statement and scope

Let \(X_1,\ldots,X_6\) be independent real random variables with probability densities bounded by \(1\). Let \(P=p\cdot X\), \(L=\ell\cdot X\), and \(V=v\cdot X\), where \(p,\ell,v\) are orthonormal and every physical row has leverage \(p_i^2+\ell_i^2+v_i^2\le1/2\). Define
\[
J(\tau)=\iint_{\mathbb R^2}
 \left|\mathbb E e^{i(yL+zV+\tau PL)}\right|\,dy\,dz.
\]
There is no universal bound \(J(\tau)\le C(1+|\tau|)\) under these hypotheses: the construction below has \(J(1)\to\infty\). In fact it uses \(\tau=1\), six original independent cap-one inputs, and **no input phases or attenuation**.

This refutes a proposed absolute Fourier route to the quadratic-form density problem. It does **not** refute the output-density conjecture. Here \(V\) occupies an independent physical bank, so the already established independent-\(V\)-bank half-potential theorem bounds the density of \(2HL+V^2+2\varepsilon LP\) when an independent capped hub \(H\) is added.

Use \(\widehat g(y)=\int e^{iys}g(s)\,ds\).

## The frame and original input laws

Let \(N\ge3\) be odd, \(k=(N-1)/2\), and
\[
f=\frac{k}{N},\quad a=\sqrt{\frac f2},\quad
b=\sqrt{\frac{1-f}{2}},\quad
\Omega=\frac1{\sqrt{f(1-f)}},\quad
D=\sqrt{\frac{2\pi}{\Omega}}.
\]
Set
\[
\ell=(a,a,b,b,0,0),\qquad
p=(b,b,-a,-a,0,0),\qquad
v=(0,0,0,0,2^{-1/2},2^{-1/2}).
\]
These columns are orthonormal. Each of the six rows has leverage exactly \(1/2\).

Choose a small fixed \(\delta>0\) and a nonzero \(w\in C_c^\infty((0,\delta))\), \(0\le w\le1\). Write \(\mu=\int w\in(0,1)\). Choose \(g\in C_c^\infty((0,2))\) with \(0\le g\le1\) and \(\int g=1-\mu\). For \(1\le i\le4\) define
\[
F_{i,N}(x)=
 \sum_{j=0}^{N-1}w\!\left(N\left(x-\frac{Dj}{\ell_i}\right)\right)
 +g(x-N^3).
\tag{1}
\]
For sufficiently large \(N\), all supports in (1) are disjoint. Each \(F_{i,N}\) is a probability density bounded by \(1\): its comb has mass \(\mu\), and the remote filler has mass \(1-\mu\). Let \(X_1,\ldots,X_4\) have these independent laws. Give \(X_5,X_6\) any independent smooth compactly supported probability densities bounded by \(1\), for example a common such density \(g_0\). All six inputs are genuine normalized cap-one probability laws.

The structured event is the one on which all of \(X_1,\ldots,X_4\) come from their comb terms. Its probability is \(\mu^4>0\). We will analyze its unnormalized contribution and then extract it from the full law without any source cutoff.

## Resonance on the tooth centers

For a comb choice \(j=(j_1,\ldots,j_4)\in\{0,\ldots,N-1\}^4\), write
\[
X_i=\frac{D j_i}{\ell_i}+\frac{t_i}{N},
\qquad t_i\in(0,\delta),
\quad m=\sum_{i=1}^4j_i,\quad K=j_1+j_2.
\]
The ratios \(p_i/\ell_i\) equal \(\Omega(1-f)\) for \(i=1,2\) and \(-\Omega f\) for \(i=3,4\). Hence
\[
L=Dm+\frac{\ell\cdot t}{N},\qquad
P=D\Omega(K-fm)+\frac{p\cdot t}{N}.
\]
Since \(D^2\Omega=2\pi\) and \(f=k/N\),
\[
e^{iLP}=q_m e^{iR(j,t)},\qquad
q_m=e^{-2\pi i k m^2/N},
\tag{2}
\]
where
\[
R(j,t)=\frac{Dm}{N}(p\cdot t)
       +\frac{D\Omega(K-fm)}{N}(\ell\cdot t)
       +\frac{(\ell\cdot t)(p\cdot t)}{N^2}.
\tag{3}
\]
Indeed the omitted center term is \(2\pi mK\). Uniformly in \(N,j,t\), \(|R(j,t)|\le C\delta\). Fix \(\delta\) small enough that \(|R|\le\pi/3\). Also, if \(j\) is replaced by \(j+e_1\) while both are allowed,
\[
|R(j+e_1,t)-R(j,t)|\le C\delta/N.
\tag{4}
\]
These bounds hold because \(m,K=O(N)\), and \(a,b,D,\Omega\) stay in compact positive ranges for all odd \(N\ge3\).

## Fourier \(L^\infty\) bound for the structured contribution

Let \(h_N\) be the complex \(L\)-density contributed by the all-comb event, including the phase \(e^{iLP}\). Direct change of variables \(x_i=Dj_i/\ell_i+t_i/N\) gives
\[
\widehat h_N(y)=\frac1N\sum_{m=0}^{4N-4}
q_m e^{iyDm} A_m(y),
\tag{5}
\]
where
\[
A_m(y)=\frac1{N^3}
\sum_{\substack{j\in\{0,\ldots,N-1\}^4\\\sum j_i=m}}
\int_{\mathbb R^4}\prod_{i=1}^4w(t_i)
   e^{iR(j,t)+i(y/N)\ell\cdot t}\,dt.
\tag{6}
\]
The number of tuples with a prescribed sum is at most \(N^3\), so \(\sup_{m,y}|A_m(y)|\le\mu^4\). More importantly,
\[
\sup_y\sum_{m=0}^{4N-5}|A_{m+1}(y)-A_m(y)|\le C_\delta.
\tag{7}
\]
To prove (7), shift the first label \(j_1\mapsto j_1+1\) to pair interior tuples at level \(m\) with those at level \(m+1\). The unmatched tuples have \(j_1=N-1\) or \(j_1=0\); for either fixed value there are at most \(N^2\) tuples of a given sum, contributing \(O(N^2/N^3)=O(1/N)\) to each difference. In every matched pair the \(y\)-factor in (6) is unchanged, and (4) bounds the phase change by \(O(\delta/N)\). Normalizing the at-most \(N^3\) matched tuples gives another \(O(1/N)\). There are fewer than \(4N\) values of \(m\), proving (7), uniformly for **all** \(y\).

The quadratic sequence \(q_m\) is \(N\)-periodic, and its discrete Fourier coefficients all have modulus \(N^{-1/2}\). Indeed, with \(k=(N-1)/2\), \(\gcd(2k,N)=1\); expanding the squared modulus of a Fourier coefficient reduces its off-diagonal terms to \(\sum_{n=0}^{N-1}e^{-2\pi i(2k)d n/N}=0\) for \(d\ne0\bmod N\). Fourier completion and the \(L^1\) bound for the Dirichlet kernel yield
\[
\sup_{\theta\in\mathbb R}
\sup_{\substack{I\subset\{0,\ldots,4N-4\}\\I\text{ interval}}}
\left|\sum_{m\in I}q_m e^{i\theta m}\right|
\le C\sqrt N\log(eN).
\tag{8}
\]
For clarity, expanding \(q_m=\sum_{r=0}^{N-1}c_r e^{2\pi irm/N}\) gives \(|c_r|=N^{-1/2}\). The sum over \(r\) of the moduli of interval geometric sums at the equally spaced shifts \(\theta+2\pi r/N\) is \(O(N\log(eN))\) for intervals of length at most \(4N\), proving (8).

Abel summation of (5), using (7) and (8), now gives the **global** bound
\[
\|\widehat h_N\|_\infty\le C_\delta\frac{\log(eN)}{\sqrt N}.
\tag{9}
\]

## Fourier \(L^2\) lower bound

Let \(\kappa\) be the density of \(\ell\cdot t\) under the finite product measure \(\prod_{i=1}^4w(t_i)\,dt_i\). It is nonnegative, compactly supported, and has total mass \(\mu^4\), so \(\|\kappa\|_2>0\) uniformly in \(N\) (the coefficients \(\ell_i\) stay bounded away from zero). Put \(r_m=\#\{j\in\{0,\ldots,N-1\}^4:\sum j_i=m\}\).

The \(L\)-peaks centered at distinct \(Dm\) have disjoint supports, since their widths are \(O(\delta/N)\). On the \(m\)th peak, (2) and the choice \(|R|\le\pi/3\) imply pointwise that the magnitude of the complex density is at least half of the unphased density
\[
\frac{r_m}{N^3}\kappa\bigl(N(s-Dm)\bigr).
\]
There are \(N^4\) tuples and fewer than \(4N\) possible sums; Cauchy-Schwarz gives \(\sum_m r_m^2\ge N^7/4\). Therefore
\[
\|h_N\|_2^2
\ge\frac{\|\kappa\|_2^2}{4N^7}\sum_mr_m^2
\ge\frac{\|\kappa\|_2^2}{16}
=:c_\delta>0.
\tag{10}
\]
Plancherel and (9) give
\[
\|\widehat h_N\|_1
\ge\frac{\|\widehat h_N\|_2^2}{\|\widehat h_N\|_\infty}
\ge c_\delta\frac{\sqrt N}{\log(eN)}.
\tag{11}
\]

## Removing the filler without attenuating the inputs

Let \(h_N^{\rm full}\) be the complex \(L\)-density for the full normalized laws (1), still with phase \(e^{iLP}\). All \(\ell_i\) are positive. The all-comb contribution is supported in \(L=O(N)\), while any selection involving at least one remote filler has \(L\ge cN^3\). Choose a fixed \(\chi\in C_c^\infty(\mathbb R)\) and a constant \(C_0\) such that \(\chi_N(s)=\chi(s/(C_0N))\) equals \(1\) on the all-comb support and \(0\) on all filler-containing supports, for all sufficiently large \(N\). Thus
\[
h_N=\chi_N h_N^{\rm full},\qquad
\|\widehat{\chi_N}\|_1=\|\widehat\chi\|_1.
\]
The product-convolution formula implies
\[
\|\widehat h_N\|_1
\le(2\pi)^{-1}\|\widehat\chi\|_1
             \|\widehat h_N^{\rm full}\|_1.
\tag{12}
\]
This is a proof device applied to the **output** density; it does not alter any original input or insert a phase/attenuation in the definition of \(J\).

Finally \(V=(X_5+X_6)/\sqrt2\) is independent of \((P,L)\). If \(X_5,X_6\) have the same smooth density \(g_0\), then
\[
J(1)=\|\widehat h_N^{\rm full}\|_1
      \int_{\mathbb R}|\widehat g_0(z/\sqrt2)|^2\,dz
=2\pi\sqrt2\,\|g_0\|_2^2\,
  \|\widehat h_N^{\rm full}\|_1.
\]
Combining this with (11) and (12) proves \(J(1)\ge c\sqrt N/\log(eN)\).

## Interpretation

This falsifies the proposed linear twisted Wiener estimate even for the genuine orthonormal product frame at maximal allowed row leverage and with no separate source phases. The highly separated original-coordinate combs make the phase \(LP\) a quadratic Gauss chirp in the projected \(L\)-label. Fourier absolute values discard cancellation that remains available in the quadratic-form density problem.

In this example \(V\) is an independent physical bank. Consequently the independent-\(V\)-bank half-Riesz receiver already gives a uniform output-density bound for the canonical leakage form \(2HL+V^2+2\varepsilon LP\) with an independent cap-one hub \(H\). The counterexample closes this particular absolute-Fourier strategy, not the original density question.
