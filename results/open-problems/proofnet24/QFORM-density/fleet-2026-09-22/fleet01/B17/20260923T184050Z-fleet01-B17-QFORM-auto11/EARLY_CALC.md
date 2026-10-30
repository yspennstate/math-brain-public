SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T18:40:50Z.
attacking: second-order sharp asymptotics for exact dense three-bank cube frames, with orientation dependence through the Householder core.

# Early substantive calculation

Full QFORM remains OPEN. Continuity for the unrestricted target is separate. This calculation stays in original-coordinate product variables and does not use the refuted arbitrary-joint coarea bound, conditional-density moment gates, pointwise stationary-phase bounds, or independence after spectral rotation.

For each bank set

\[
S_{j,m}=m^{-1/2}\sum_{k=1}^m U_{jk},\qquad U_{jk}\stackrel{ind}{\sim}{\rm Unif}[-1/2,1/2].
\]

Let `sigma^2=1/12`, `Z_{j,m}=S_{j,m}/sigma`, and for `u in S^2` let

\[
B_u=I_3-2uu^T,\qquad Q_{m,u}=S_m^T B_uS_m.
\]

The physical synthesis matrix has `m` rows `e_j/sqrt(m)` in each bank, so `A_{m,u}=C_mB_uC_m^T` has exact nonzero spectrum `{1,1,-1}` for every finite `m`.

The standardized one-bank characteristic function is

\[
\psi_m(t)=\operatorname{sinc}(\sqrt3t/\sqrt m)^m.
\]

Using

\[
\log(\operatorname{sinc}z)=-z^2/6-z^4/180-z^6/2835+O(z^8),
\]

one gets

\[
\psi_m(t)=e^{-t^2/2}\left[1-\frac{t^4}{20m}
+\frac1{m^2}\left(-\frac{t^6}{105}+\frac{t^8}{800}\right)
+O(m^{-3})\right].
\]

Fourier inversion therefore gives the local Edgeworth expansion

\[
f_m(z)=\phi(z)\left[1-\frac{H_4(z)}{20m}
+\frac1{m^2}\left(\frac{H_6(z)}{105}+\frac{H_8(z)}{800}\right)\right]
+O(m^{-3})
\]

with a polynomial-Gaussian weighted remainder (the full report will record the standard small/intermediate/far Fourier split justifying cone integration).

Put `x_j=u_j^2`, `sum x_j=1`, `e2=sum_{i<j}x_ix_j`, `e3=x_1x_2x_3`. Under the normalized Gaussian null-cone measure of `z^TB_uz=0`, direct circle-moment calculation gives

\[
E H_4(Z_j)=\frac3{32}(19+2x_j-13x_j^2),
\]

\[
E H_6(Z_j)=-\frac{15}{128}(19x_j^3-111x_j^2+45x_j+63),
\]

\[
E H_8(Z_j)=\frac{105}{2048}(611x_j^4-492x_j^3-1902x_j^2+1044x_j+867),
\]

and, for `i!=j` with `x=x_i,y=x_j`,

\[
E[H_4(Z_i)H_4(Z_j)]
=\frac3{2048}\bigl(21385x^2y^2-3690x^2y-951x^2-3690xy^2-11412xy+1566x-951y^2+1566y+2601\bigr).
\]

Consequently

\[
\frac{p_{Q_{m,u}}(0)}{3\sqrt2}
=1-\frac{3(59-13\sum_jx_j^2)}{640m}
+\frac{c_2(u)}{m^2}+O(m^{-3}),
\]

where

\[
c_2(u)=\frac{449085e_2^2-125514e_2-337380e_3-17411}{2867200}.
\]

The first correction is always at most `-69/(320m)`. Moreover

\[
c_2(u)\le-\frac{17411}{2867200}<0.
\]

For the second inequality, subtract the vertex value: its numerator is

\[
3(149695e_2^2-41838e_2-112460e_3).
\]

If `e2<=41838/149695`, this is nonpositive immediately. If `e2` is larger, Schur gives `e3>=(4e2-1)/9`; the resulting convex quadratic

\[
(1347255e_2^2-826382e_2+112460)/9
\]

is negative at both endpoints `41838/149695` and `1/3`, hence throughout that interval. Equality in the `c2` comparison occurs only at a coordinate vertex.

For the genuinely dense balanced Householder core `u=(1,1,1)/sqrt3`, every entry of the finite physical matrix is nonzero and

\[
\boxed{\frac{p_{Q_m}(0)}{3\sqrt2}
=1-\frac{41}{160m}-\frac{3511}{460800m^2}+O(m^{-3}).}
\]

Thus the exact dense finite product family approaches the known obstruction `3sqrt(2)` from below, with two explicit negative corrections. This already reinforces `C_univ>=3sqrt(2)` and constrains any proposed finite-orientation overshoot mechanism.
