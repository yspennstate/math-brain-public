# Reusing the balancing character: equivalence barrier and exact slice surcharge

All logarithms are base two. Fix a genuine Boolean function
\(q:\{-1,1\}^n\to\{-1,1\}\) and an existing coordinate \(x\). Put

\[
r=\chi_xq,\qquad \widetilde{\mathcal T}_x(q)=A(r),
\]

where \(A(r)(z,u)=1\) for \(z=+1\) and \(A(r)(z,u)=r(u)\) for
\(z=-1\). Only the selector \(z\) is fresh.

## 1. Exact equivalence barrier

Multiplication by \(\chi_x\) is an involution:

\[
\chi_x(\chi_xq)=q.
\]

Consequently

\[
\{\widetilde{\mathcal T}_x(q):q\text{ Boolean}\}
=\{A(r):r\text{ Boolean}\}. \tag{1}
\]

Indeed, for a prescribed \(r\), choose \(q=\chi_xr\). Then
\(\widetilde{\mathcal T}_x(q)=A(r)\). Restricting the fresh selector gives

\[
A(r)|_{z=+1}=1,\qquad A(r)|_{z=-1}=r. \tag{2}
\]

Thus the restriction closure of the left-hand family over arbitrary cores
contains every genuine Boolean function. Replacing the fresh balancing
coordinate in the prior transfer by an arbitrary existing coordinate is not
a proper-class extension: with restriction closure it is already the
universal problem.

## 2. Exact character-multiplication identities

Write

\[
W_x(q)=U(\chi_xq)-U(q).
\]

For \(j\ne x\), let \(x_j\) denote the surviving index of \(x\) after
restricting coordinate \(j\), and define

\[
\mathcal D_xW(q)=W_x(q)+\sum_{j\ne x}
\left(W_x(q)-\frac{W_{x_j}(q_{j,+})+W_{x_j}(q_{j,-})}{2}\right). \tag{3}
\]

Spectrally, multiplication by \(\chi_x\) toggles membership of \(x\):
\(\widehat r(S)=\widehat q(S\triangle\{x\})\). Therefore

\[
B(r)=B(q),\qquad I(r)-I(q)=1-2\operatorname{Inf}_x(q). \tag{4}
\]

For \(j\ne x\), restriction commutes with multiplication by \(\chi_x\).
For \(j=x\), the restrictions of \(r\) differ from the corresponding
restrictions of \(q\) only by output signs, which do not change \(U\).
Subtracting the definitions of \(G(r)\) and \(G(q)\) gives

\[
G(r)-G(q)=\mathcal D_xW(q). \tag{5}
\]

Since \(M=G-B\), (4)--(5) imply the complete signed slice identity

\[
\boxed{
L_{c,\eta}(\chi_xq)-L_{c,\eta}(q)
=\mathcal D_xW(q)+(1+\eta)W_x(q)
-c\bigl(1-2\operatorname{Inf}_x(q)\bigr).
} \tag{6}
\]

No upper-set, influence, or restriction term is omitted.

## 3. Substitution into the accepted activation recurrence

For a Boolean core \(s\), denote the exact activation remainder by

\[
\mathcal E_{c,\eta}(s)=D_R(s)+(2+\eta)R(\mathbb Es)
-B_z(\mathbb Es)-\sum_iC_i(\mathbb Es,\widehat s(\{i\})^2)
-c\frac{1-\mathbb Es}{2}. \tag{7}
\]

The accepted identity is
\(L(A(s))=L(s)/2+\mathcal E_{c,\eta}(s)\). Setting
\(s=\chi_xq\) and using (6) yields

\[
\boxed{
L_{c,\eta}(\widetilde{\mathcal T}_x(q))-rac12L_{c,\eta}(q)
=\mathcal E_{c,\eta}(\chi_xq)
+\frac12\left[\mathcal D_xW(q)+(1+\eta)W_x(q)
-c(1-2\operatorname{Inf}_x(q))\right].
} \tag{8}
\]

Equation (8) is the smallest exact unpaid inequality for this attempted
freshness removal. It transports the entire \(x\)-containing Fourier slice;
it does not use the refuted nonnegative singleton-only payment.

## 4. Exact failure of half-contraction

The direct analogue of the fresh-character contraction is false for every
\(c>0\). Take \(q=\chi_x\). Then \(\chi_xq=1\), so
\(\widetilde{\mathcal T}_x(q)=A(1)=1\). Hence

\[
L_{c,\eta}(\widetilde{\mathcal T}_x(q))=0,
\qquad L_{c,\eta}(q)=-c,
\]

and therefore

\[
L_{c,\eta}(\widetilde{\mathcal T}_x(q))
-\frac12L_{c,\eta}(q)=\frac c2>0. \tag{9}
\]

Thus a valid reused-coordinate theorem must preserve the nonpositive cone
with a terminal zero reserve (for example, a bound by
\(\max\{0,L(q)/2\}\)); it cannot retain the previous strict
half-contraction.

This is a route obstruction, not a counterexample to GU or FEI.
