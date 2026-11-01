# Fully overlapping genuine-product twisted Wiener falsifier

## Claim and scope

There is one fixed orthonormal three-frame \((p,\ell,v)\) in \(\mathbb R^8\), with every physical row leverage strictly below \(1/2\), and a sequence of independent normalized cap-one scalar input laws for which
\[
J(1):=\iint_{\mathbb R^2}
 \left|\mathbb E e^{i(yL+zV+LP)}\right|\,dy\,dz
 \longrightarrow\infty,
\qquad L=\ell\cdot X,\quad P=p\cdot X,\quad V=v\cdot X.
\]
In this frame every \(V\) coordinate also contributes to \(L\) and \(P\); there is no independent \(V\) bank and no source phase or attenuation.

This is a counterexample to the absolute twisted Wiener estimate, **not** to the quadratic-form density conjecture. The last section gives a uniform direct density bound for \(Q=2HL+V^2+2\varepsilon LP\) with an independent cap-one hub \(H\).

## One fixed frame

Fix \(f=(3-\sqrt5)/2\in(1/3,1/2)\), and put
\[
a=\sqrt{f/4},\qquad b=\sqrt{(1-f)/4},\qquad
\Omega=[f(1-f)]^{-1/2},\qquad D=\sqrt{2\pi/\Omega}.
\]
For \(i=1,\ldots,4\), set \((\ell_i,p_i)=(a,b)\); for \(i=5,\ldots,8\), set \((\ell_i,p_i)=(b,-a)\). Let
\[
(\sigma_1,\ldots,\sigma_8)=(+,+,-,-,+,+,-,-),
\qquad v_i=\sigma_i\ell_i.
\]
Then \(\ell,p,v\) are orthonormal: \(\|\ell\|^2=\|p\|^2=\|v\|^2=1\), \(\ell\cdot p=0\), and the plus and minus signs balance within both groups, giving \(v\cdot\ell=v\cdot p=0\). Each row leverage is \((1+f)/4\) in the first group and \((2-f)/4\) in the second, both strictly below \(1/2\).

Choose an infinite sequence of odd Fibonacci denominators \(N=F_{r+2}\) and numerators \(k=F_r\). Then \(\gcd(2k,N)=1\) and \(|f-k/N|\le C/N^2\).

## Independent normalized input laws

Fix a sufficiently small \(\delta>0\), a nonzero \(w\in C_c^\infty((0,\delta))\) with \(0\le w\le1\), and \(\mu=\int w\in(0,1)\). Choose a smooth \(g\) of mass \(1-\mu\), supported in \((0,2)\), with \(0\le g\le1\). Independently give each \(X_i\) the density
\[
F_{i,N}(x)=
 \sum_{j=0}^{N-1} w\!\left(N\left(x-\frac{Dj}{\ell_i}\right)\right)
 +g(x-N^3).
\tag{1}
\]
The comb terms are disjoint for large \(N\), total mass \(\mu\), and height at most \(1\). The remote filler has mass \(1-\mu\), so (1) is a normalized cap-one law.

We first analyze the unnormalized all-comb contribution to the complex \((L,V)\)-density with weight \(e^{iLP}\). A smooth output cutoff will then recover it from the full normalized law.

## Lattice phase and local sector

For comb labels \(j_i\in\{0,\ldots,N-1\}\), write \(X_i=Dj_i/\ell_i+t_i/N\) with \(t_i\in(0,\delta)\), and define
\[
m=\sum_{i=1}^8j_i,\quad n=\sum_{i=1}^8\sigma_i j_i,\quad
K=\sum_{i=1}^4j_i.
\]
The center projections are
\[
L_0=Dm,\qquad V_0=Dn,\qquad
P_0=D\Omega(K-fm).
\]
Indeed \(p_i/\ell_i=\Omega(1-f)\) in the first group and \(-\Omega f\) in the second. As \(D^2\Omega=2\pi\),
\[
e^{iLP}=q_m e^{iR(j,t)},\quad
q_m=e^{-2\pi i f m^2},
\tag{2}
\]
where
\[
R(j,t)=\frac{Dm}{N}(p\cdot t)
 +\frac{D\Omega(K-fm)}{N}(\ell\cdot t)
 +\frac{(\ell\cdot t)(p\cdot t)}{N^2}.
\tag{3}
\]
The center term \(2\pi mK\) has disappeared. Since \(m,K=O(N)\), \(|R(j,t)|\le C\delta\). Fix \(\delta\) so small that \(|R|\le\pi/3\). If one plus-sign and one minus-sign label in the first group are both incremented, then \(m\mapsto m+2\), \(n\) stays fixed, \(K\mapsto K+2\), and (3) changes by \(O(\delta/N)\).

The \((L,V)\) centers are the lattice points \((Dm,Dn)\). Their local widths are \(O(\delta/N)\), so different occupied lattice cells have disjoint supports.

## Global Fourier \(L^\infty\) bound

Let \(h_N\) be the all-comb complex \((L,V)\)-density. With \(\widehat h(y,z)=\iint e^{i(yl+zv)}h(l,v)\,dl\,dv\), change of variables gives
\[
\widehat h_N(y,z)
 =\frac1{N^2}\sum_n e^{iDzn}
   \sum_{\substack{m\\m\equiv n\ (2)}}
    q_m e^{iDym} A_{m,n}(y,z),
\tag{4}
\]
where
\[
A_{m,n}(y,z)=\frac1{N^6}
 \sum_{\substack{j\in\{0,\ldots,N-1\}^8\\
                 \sum j_i=m,\ \sum\sigma_i j_i=n}}
 \int_{\mathbb R^8}\prod_{i=1}^8w(t_i)\,
 e^{iR(j,t)+i(y\ell+zv)\cdot t/N}\,dt.
\tag{5}
\]
There are at most \(N^6\) tuples with given \((m,n)\), so \(|A_{m,n}|\le\mu^8\).

For each fixed \(n\), the allowed \(m\)'s have one parity. Along this parity class,
\[
\sup_{y,z}\sum_m|A_{m+2,n}(y,z)-A_{m,n}(y,z)|\le C.
\tag{6}
\]
To see this, pair a tuple at \((m,n)\) with the tuple obtained by adding \(1\) to \(j_1\) and \(j_3\), whose signs are opposite. The phase change is \(O(\delta/N)\), and the Fourier factor involving \(t\) is identical for the pair. Unmatched boundary tuples have \(j_1\) or \(j_3\) equal to \(0\) or \(N-1\). At fixed \((m,n)\), each such boundary has at most \(N^5\) tuples, so its normalized contribution to one difference is \(O(1/N)\). Matched contributions are also \(O(1/N)\), and there are \(O(N)\) values of \(m\). This proves (6), as well as a uniform supremum bound on \(A_{m,n}\).

Write
\[
q_m=q_m^{(N)}E_m,\quad
q_m^{(N)}=e^{-2\pi i k m^2/N},\quad
E_m=e^{-2\pi i(f-k/N)m^2}.
\]
Because \(|f-k/N|\le C/N^2\) and \(|m|\le8N\),
\[
\sum_m|E_{m+2}-E_m|\le C.
\tag{7}
\]
Thus \(E_mA_{m,n}(y,z)\) has bounded total variation along every fixed-\(n\) parity class.

For \(m=2r+e\) on such a class, \(q_{2r+e}^{(N)}\) is a quadratic chirp in \(r\) modulo \(N\). Its quadratic coefficient is \(4k\), and \(\gcd(8k,N)=1\) since \(N\) is odd and \(\gcd(k,N)=1\). Therefore all its \(N\) discrete Fourier coefficients have modulus \(N^{-1/2}\). Fourier completion and the geometric-sum harmonic estimate imply that every incomplete sum, with any additional linear phase, is bounded by \(C\sqrt N\log(eN)\) on intervals of length \(O(N)\). Abel summation using (6) and (7) makes each inner sum in (4) at most \(C\sqrt N\log(eN)\). There are \(O(N)\) possible \(n\)'s, hence
\[
\|\widehat h_N\|_\infty
 \le C\frac{\log(eN)}{\sqrt N}.
\tag{8}
\]

## Joint \(L^2\) lower bound and normalized law

Let \(\kappa\) be the nonnegative joint density of \((\ell\cdot t,v\cdot t)\) under \(\prod_{i=1}^8w(t_i)\,dt_i\). It exists, is compactly supported, and has mass \(\mu^8\), so \(\|\kappa\|_2\ge c_\delta>0\). Let \(r_{m,n}\) count label tuples with center \((Dm,Dn)\). On each disjoint cell, (2) and \(|R|\le\pi/3\) show that the complex density magnitude is at least half the unphased density
\[
\frac{r_{m,n}}{N^6}
 \kappa\bigl(N(l-Dm),N(v-Dn)\bigr).
\]
There are \(N^8\) total tuples and only \(O(N^2)\) occupied cells, so
\(\sum_{m,n}r_{m,n}^2\ge cN^{14}\). Integrating the disjoint cells gives
\[
\|h_N\|_2^2
 \ge\frac{\|\kappa\|_2^2}{4N^{14}}
       \sum_{m,n}r_{m,n}^2
 \ge c_\delta>0.
\tag{9}
\]
By 2D Plancherel and (8),
\[
\|\widehat h_N\|_1
 \ge \frac{\|\widehat h_N\|_2^2}
           {\|\widehat h_N\|_\infty}
 \ge c_\delta\frac{\sqrt N}{\log(eN)}.
\tag{10}
\]

Let \(h_N^{\rm full}\) be the analogous complex joint density from the full normalized input laws (1). All \(\ell_i>0\). The all-comb part has \(L=O(N)\), while any filler selection has \(L\ge cN^3\). Choose a smooth cutoff \(\chi_N(l)=\chi(l/(C_0N))\), equal to \(1\) on the former and \(0\) on the latter. Then
\(h_N(l,v)=\chi_N(l)h_N^{\rm full}(l,v)\) exactly, and \(\|\widehat\chi_N\|_1=\|\widehat\chi\|_1\) is independent of \(N\). Fourier convolution in \(y\), followed by Young's inequality, yields
\[
\|\widehat h_N^{\rm full}\|_{L^1(dy\,dz)}
 \ge \frac{2\pi}{\|\widehat\chi\|_1}
       \|\widehat h_N\|_{L^1(dy\,dz)}.
\]
But \(\|\widehat h_N^{\rm full}\|_1=J(1)\). Equation (10) proves the claim for one fixed fully overlapping frame and normalized independent cap-one laws, with no input phase or attenuation.

## Why the quadratic-form density still has a direct bound

Add an independent cap-one hub \(H\), and consider \(Q=2HL+V^2+2\varepsilon LP\). Pick physical inputs \(X_1\) and \(X_3\), which have the same \((\ell_i,p_i)=(a,b)\) but opposite \(v_i=\pm a\). Condition all other original inputs and rotate
\[
u=(X_1+X_3)/\sqrt2,\qquad w=(X_1-X_3)/\sqrt2.
\]
The conditional joint density of \((u,w)\) is bounded by \(1\), and it is independent of \(H\). With conditioned constants,
\[
L=\sqrt2a\,u+c_L,\qquad
P=\sqrt2b\,u+c_P,\qquad
V=\sqrt2a\,w+c_V.
\]
Separate translations of \(u,w,H\) turn \(Q\) into \(2tHu+\beta u^2+\lambda w^2\), where \(t=\sqrt2a=\sqrt{f/2}\), \(\lambda=2a^2=f/2\), and \(\beta\) may depend on \(\varepsilon\). The beta-uniform two-light coarea lemma applies with planar cap \(M=1\), giving at every target
\[
\|p_Q\|_\infty
 \le\frac12+\frac{4\sqrt2}{|t|\sqrt\lambda}
 =\frac12+\frac{8\sqrt2}{f}<35.
\]
Thus this construction disproves the proposed absolute Fourier estimate while its quadratic-form output density remains uniformly bounded, even though \(V\) overlaps every original input.
