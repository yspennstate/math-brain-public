# PROB20-16 additive notation/algebra correction for the 22:24 stuck report

This artifact corrects three display typos in the immutable report
`runs/2026-09-16/2026-09-16T22-24-00Z__report.md` created at commit
`8e13acc52266273d04b7905c3634a43164b4fb3d`. The historical report is not overwritten.
No mathematical conclusion of the run changes.

1. In equation (3.2), the lower-left matrix entry printed as `\nu_2`; it should be `u_2`:

\[
W(u)=\sqrt{ac\rho}
\begin{pmatrix}
2u_1&u_2\\
u_2&0
\end{pmatrix}.
\]

2. In Section 4, the first conditional Bernoulli coordinate printed as `\nu`; it should be the variable `u` used in equations (4.2)--(4.4):

\[
u=x+\frac{s}{1-y}=P(X_1=1\mid X_2=0),\qquad
v=x-\frac{s}{y}=P(X_1=1\mid X_2=1).
\]

3. In the proposed next special case `c=1/2`, equation (7.3) omitted the factor arising from

\[
\left(\tfrac12 S_0^{-1}+\tfrac12 S_1^{-1}\right)^{-1}
=2(S_0^{-1}+S_1^{-1})^{-1}.
\]

With

\[
W_{1/2}(u)=\frac{\sqrt{\rho}}2
\begin{pmatrix}2u_1&u_2\\u_2&0\end{pmatrix},
\]

the exact `c=1/2` blocker is

\[
\boxed{
8\left\langle W_{1/2}(u),
(S_0^{-1}+S_1^{-1})^{-1}W_{1/2}(u)\right\rangle
\ge 2u^\top G u.
}
\]

Equivalently,

\[
4\left\langle W_{1/2}(u),
(S_0^{-1}+S_1^{-1})^{-1}W_{1/2}(u)\right\rangle
\ge u^\top G u.
\]

The exact blocker (3.1)/(7.1), the B1 channel identities, the B6 infinitesimal determinant identity, and the B15 rational route-failure certificate are unchanged.
