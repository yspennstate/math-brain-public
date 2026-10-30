# Early checkpoint — unequal-bank rotated witness

Run: `20260923T140355Z-fleet03-B17-QFORM-auto11`  
Status: supporting analytic witness calculation; full QFORM remains OPEN.

Take three bank sizes `m_1,m_2,m_3>=3`. In bank `j`, let
\[
Y_j=m_j^{-1/2}\sum_{k=1}^{m_j}X_{jk},\qquad X_{jk}\sim\mathrm{Unif}[-1/2,1/2]
\]
independently. Let `J=diag(1,1,-1)`, `O\in O(3)`, `B=O^TJO`, and let `R` repeat the physical row `e_j/sqrt(m_j)` in bank `j`. Then `R^TR=I_3`, so `A=RBR^T` has exact nonzero spectrum `{1,1,-1}` and all input densities have cap one.

Using the weighted local Edgeworth lemma proved in fleet04/B17 at
`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
write
\[
g_{m_j}(y)=\gamma_\sigma(y)\Bigl[1-\frac1{20m_j}H_4(y/\sigma)\Bigr]
+O(m_j^{-2})(1+|y|)^{-8},\qquad \sigma^2=1/12.
\]
On the Lorentz cone `z_1^2+z_2^2-z_3^2=0`, put `u_j=O_{3j}^2`. Direct angular/radial averaging gives
\[
\mathbb E_{\rm cone} H_4(Y_j/\sigma)=h(u_j),\qquad
h(u)=\frac{57+6u-39u^2}{32}.
\]
Since `h` is concave on `[0,1]` and `h(0)=57/32`, `h(1)=3/4`,
\[
\boxed{h(u)\ge 3/4\quad(0\le u\le1).}
\]
Therefore the first Edgeworth correction at the cone tip is negative for every orientation and every unequal bank-size profile:
\[
p_Q(0)=3\sqrt2\left[1-\sum_{j=1}^3\frac{h(u_j)}{20m_j}
+O\!\left(\left(\sum_jm_j^{-1}\right)^2\right)\right].
\]
In particular the relative first-order deficit is at least
\[
\frac3{80}\sum_jm_j^{-1}.
\]

For the exact rational partner rotation
\[
O=\frac17\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix},
\]
`u=(9,36,4)/49` and
\[
(h(u_1),h(u_2),h(u_3))=
\left(\frac{17043}{9604},\frac{96897}{76832},\frac{137409}{76832}\right).
\]
Their sum divided by 20 is exactly
\[
\frac1{20}\sum_jh(u_j)=\frac{5295}{21952},
\]
recovering the completed fleet04/B17 equal-bank coefficient. This is the partner result applied at an actual identity, while the new point is positivity bank-by-bank, which rules out an unequal-scale first-order overshoot at zero.

Remaining to finish before publication: write the product-remainder estimate carefully, record continuity scope, and save exact arithmetic verification.
