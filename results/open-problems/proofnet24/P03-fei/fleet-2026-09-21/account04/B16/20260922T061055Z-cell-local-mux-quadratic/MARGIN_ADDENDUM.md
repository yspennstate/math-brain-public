# Margin addendum — convert the lifted-candidate reserve to the owner's comparable gate margin

The OWNER MESSAGE requests reporting the comparable gate margin
\[
c_G=-D_{\Gamma_0}(G;p)/Q_G(p),
\qquad
Q_G(p)=I(G;p)/4-p_{\rm out}(1-p_{\rm out}),
\]
for the base read-once potential `Gamma_0`, rather than comparing raw gate defects across arities.

For the balanced-address MUX in the coordinates of `REPORT.md`,
\[
u=1-q_0-q_1,\qquad v=q_1-q_0,
\]
a direct substitution of the exact biased influences gives
\[
\boxed{
Q_M(u,v)=\frac{1-u^2-v^2}{8}.
}
\tag{A.1}
\]
For the lifted candidate
\[
\Gamma^\dagger=\Gamma_0+a^\dagger z(1-z),
\qquad a^\dagger=0.268204856,
\]
the universal Poincare-currency identity gives
\[
D_{\Gamma^\dagger}=D_{\Gamma_0}+a^\dagger Q_M,
\]
hence
\[
\boxed{
c_M=a^\dagger-\frac{D_{\Gamma^\dagger}}{Q_M}.}
\tag{A.2}
\]

On the single-source-cell same-side region of Theorem 4.1,
\[
D_{\Gamma^\dagger}>R_*p,
\qquad
R_*=
\frac{1114633887638025857}{271020516100000000000},
\qquad p=\frac{1-u}{2}.
\]
Since
\[
Q_M=\frac{1-u^2-v^2}{8}
\le\frac{1-u^2}{8},
\]
we get
\[
\frac{D_{\Gamma^\dagger}}{Q_M}
>
\frac{4R_*}{1+u}
\ge2R_*.
\]
Therefore the OWNER-comparable base-potential margin obeys the uniform strict bound
\[
\boxed{
 c_M
< a^\dagger-2R_*
=
\frac{35229875359185064943}{135510258050000000000}
=
0.2599793983580645\ldots
}
\tag{A.3}
\]
throughout the `rho<=3/20` same-cell theorem region.

Equivalently, relative to the lifted candidate itself, the margin is strictly negative:
\[
-\frac{D_{\Gamma^\dagger}}{Q_M}
< -2R_*
=-0.008225457641935514\ldots .
\tag{A.4}
\]

This conversion is analytic and uses no additional numerical search. It does not claim that `0.259979398...` is sharp; its role is to put the new theorem in the gate-margin units required by the live owner directive.
