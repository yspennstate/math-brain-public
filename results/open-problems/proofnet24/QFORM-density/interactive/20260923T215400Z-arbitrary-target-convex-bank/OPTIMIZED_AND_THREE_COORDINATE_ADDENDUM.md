# Optimized hub cutoff and a three-coordinate correlated-\(P_B\) extension

Date: 2026-09-23 UTC. This is an addendum to [REPORT.md](REPORT.md).

## Universal cutoff calculation

Use the same setup as the main report, except suppose merely that the fixed-\(L\) residual measures satisfy
\[
 \mu_l(E)\le C\sqrt{|E|}\quad\text{for every Borel }E,
 \qquad\int_{\mathbb R}\mu_l(\mathbb R)\,dl=1,
 \tag{A1}
\]
with \(C\) independent of \(l\). Let the independent hub density satisfy \(0\le f_H\le1\), \(\int f_H=1\), and set \(Q=2HL+R_L\). The density formula and the level sets \(F_u=\{h:f_H(h)>u\}\) are as in the main report. For any \(r>0\), applying (A1) to \(s-2lF_u\) gives
\[
 p_Q(s)\le
 \underbrace{\frac{C}{\sqrt2}\int_{|l|<r}|l|^{-1/2}\,dl
      \int_0^1\sqrt{|F_u|}\,du}_{\le\,2\sqrt2\,C\sqrt r}
 +\underbrace{\int_{|l|\ge r}\frac{\mu_l(\mathbb R)}{2|l|}\,dl}_{\le\,1/(2r)}.
 \tag{A2}
\]
Since \(\int_0^1|F_u|du=1\), Cauchy--Schwarz gives \(\int_0^1\sqrt{|F_u|}du\le1\). Choosing \(r=(2\sqrt2 C)^{-2/3}\) proves
\[
 \|p_Q\|_\infty\le3C^{2/3}.
 \tag{A3}
\]
In the planar bank-linear theorem of the main report, \(C=2M_B\), so its bound improves to
\[
 \|p_Q\|_\infty\le3\cdot2^{2/3}M_B^{2/3}.
 \tag{A4}
\]
This uses only the cap \(g_B\le M_B\); bank \(A\) remains arbitrary. Constants (A3)--(A4) are valid for every fragmented cap-one hub density.

## A genuinely three-coordinate bank with arbitrary correlated \(P_B\)

Let bank \(B\) consist of exactly three independent original-coordinate inputs \(X_1,X_2,X_3\), each having an arbitrary density bounded by one. Let
\[
 L_B=\ell\cdot X,\qquad V_B=v\cdot X,\qquad P_B=p\cdot X,
 \qquad \ell,v\in\mathbb R^3,\quad\|\ell\|_2=\|v\|_2=1,\quad\ell\cdot v=0,
 \tag{A5}
\]
where \(p\in\mathbb R^3\) is arbitrary. The law of \(P_B\) is generally correlated with \((L_B,V_B)\); no conditional density assumption is imposed. Let independent bank \(A=(L_A,V_A,P_A)\) have any probability law and let the independent hub \(H\) have a density bounded by one. For any real \(\beta,\varepsilon\), the canonical quadratic
\[
 Q=2H(L_A+L_B)+\beta(L_A+L_B)^2+(V_A+V_B)^2
   +2\varepsilon(L_A+L_B)(P_A+P_B)
 \tag{A6}
\]
has a density with
\[
 \|p_Q\|_\infty\le3(2\sqrt6)^{2/3}=3\sqrt[3]{24}<8.66.
 \tag{A7}
\]
The bound is uniform in \(p,\beta,\varepsilon\) and the arbitrary \(A\)-bank law.

**Proof of fixed-\(L\) estimate.** Choose \(k\) with \(|\ell_k|\ge1/\sqrt3\); write \(i,j\) for the other indices. On the physical slice \(L_B=b\), solve
\[
 X_k=\frac{b-\ell_iX_i-\ell_jX_j}{\ell_k}.
 \tag{A8}
\]
After substitution, \(V_B=c_b+w_iX_i+w_jX_j\), where
\[
 w_h=v_h-\frac{v_k\ell_h}{\ell_k},\qquad h\in\{i,j\}.
 \tag{A9}
\]
The orthogonality \(\ell\cdot v=0\) gives \(\|w\|_2^2\ge\|v\|_2^2=1\): indeed, with \(c=v_k/\ell_k\), one has \(v=(w_i,w_j,0)+c\ell\), after embedding \(w\) in the non-\(k\) coordinates, and \(c=-w\cdot\ell\); therefore \(1=\|w\|_2^2-c^2\). Choose \(h\in\{i,j\}\) with \(|w_h|\ge1/\sqrt2\), and denote the remaining free index by \(h'\).

For fixed \(b,X_{h'}\), fixed full \(A\)-bank state, and fixed total \(L=l\), the residual output in (A6) is a degree-two polynomial of \(X_h\) whose quadratic coefficient is \(w_h^2\). The \(P_B\) term is linear in \(X_h\), regardless of \(p\). Completing the square and applying the inverse-image bound (4) of the main report yields an \(X_h\)-preimage of any Borel output set \(E\) of length at most \(2\sqrt{|E|}/|w_h|\). The slice Jacobian is \(1/|\ell_k|\), while the \(X_h,X_k\) densities are at most one and the \(X_{h'}\) density integrates to one. Hence the unnormalized conditional output measure at every \(b\) obeys
\[
 \mu_b(E)\le\frac{2}{|\ell_k||w_h|}\sqrt{|E|}
 \le2\sqrt6\sqrt{|E|}.
 \tag{A10}
\]
The right side is independent of the full \(A\)-bank state, so integrate the latter to obtain (A1) with \(C=2\sqrt6\). The total slice masses integrate to one by Fubini. Apply (A3) to conclude (A7). \(\square\)

This proof genuinely uses original-coordinate independence. A three-dimensional joint cap on \((L_B,V_B,P_B)\), without the original product representation, does not imply (A10). When \(B\) has many diffuse physical coordinates, selecting three of them can make \(|\ell_k||w_h|\) arbitrarily small; (A10) then loses a uniform constant. The unrestricted correlated-\(P_B\) bank remains open.
