# Round 516 corrected two-scale scalar residual inequalities

Round 515 changes the interpretation of the scalar model.  Here is the
correct two-scale version of the residual calculation.

Fix
\[
  \alpha=0.99,\qquad \theta=z,\qquad C=2,
\]
and put
\[
  a_q(z)=Cqz^2w_*^2.
\]
In the parent norm \(\mathcal B_\alpha\), a recursive child atom controlled
in \(\mathcal B_\theta\) has span inventory
\[
  P_c=\frac{\theta/\alpha}{1-\theta/\alpha},
\]
while a root-column vertical atom has inventory
\[
  P_v=\frac{z/\alpha}{1-z/\alpha}.
\]
The monotone trace transform, with no consecutive vertical atoms, is therefore
\[
  H_q^{\theta,\alpha}(z)
  =
  \frac{
    a_q(z)P_c+P_v+a_q(z)P_cP_v
  }{
    1-a_q(z)P_c(1+P_v)
  }.
\]
For \(\theta=z\), this agrees numerically with the Round 510 monotone values,
but now the child span factor is correctly interpreted as \(\theta/\alpha\),
not as an extra path-length \(z\) inside a same-scale norm.

For neutral reversal bubbles, there is no parent endpoint span to divide out.
The two leg inventories are
\[
  A_0=a_q(z)\frac{\theta}{1-\theta},
  \qquad
  V_0=\frac{z}{1-z},
\]
and the no-vertical-vertical rule gives
\[
  D_q^{\theta}(z)
  =
  (A_0+V_0)^2-V_0^2.
\]

At \(z=M_q^{-1}\), the residual cases give:
\[
\begin{array}{c|c|c|c|c}
q & z & a_q(z) & H_q^{z,0.99}(z) & H_q^{z,0.99}(z)/(1-D_q^z(z))\\
\hline
2 & 0.387584\ldots & 0.272910\ldots & 1.309916\ldots & 1.742953\ldots\\
3 & 0.355151\ldots & 0.301081\ldots & 1.114926\ldots & 1.411562\ldots\\
4 & 1/3 & 0.32 & 0.996553\ldots & 1.223666\ldots\\
5 & 0.309017\ldots & 0.303928\ldots & 0.818365\ldots & 0.951638\ldots\\
6 & 0.289898\ldots & 0.288490\ldots & 0.701502\ldots & 0.788235\ldots
\end{array}
\]
All final values are \(<C=2\).

Thus the scalar residual calculation is sound as a two-scale estimate:
\[
  \mathcal B_{\theta=z}\to\mathcal B_{\alpha=0.99}.
\]
The remaining analytic issue is how to chain or bootstrap such estimates so
that control at the stronger scale \(\theta=z\) is available.  One possible
route is an analytic norm integrating a range of span scales; another is a
finite-step induction over scales
\[
  z=\alpha_0<\alpha_1<\cdots<\alpha_m<1
\]
where each packet transform maps \(\mathcal B_{\alpha_i}\) into
\(\mathcal B_{\alpha_{i+1}}\) with constants that remain below the chosen
packet fugacity.
