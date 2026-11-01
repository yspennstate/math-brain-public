# Owner-margin translation for the zero-credit MUX collar

The proof in `REPORT.md` establishes
\[
D_{\Gamma^\dagger}(M;t,q_0,q_1)>\frac1{128}
\]
throughout either zero-credit collar, with
\[
\Gamma^\dagger=\Gamma_0+a^\dagger p(1-p),
\qquad a^\dagger=0.268204856.
\]

The exact MUX Poincare denominator from the source identities is
\[
W_M:=\frac{I(M)}4-p_{\rm out}(1-p_{\rm out})
=\frac{V_t(V_{q_0}+V_{q_1})}{16}.
\]
In this collar `t` and one data bias are interior and within `2^-15` of `1/2`, so `W_M>0`; universally `V_u<=1`, hence
\[
0<W_M\le\frac18.
\]

For the owner's comparable gate-margin normalization relative to `Gamma_0`,
\[
c_M=-\frac{D_{\Gamma_0}(M)}{W_M}
=a^\dagger-\frac{D_{\Gamma^\dagger}(M)}{W_M}.
\]
Therefore the proved slack implies the uniform margin bound
\[
\boxed{
c_M<a^\dagger-\frac{1/128}{1/8}
=a^\dagger-\frac1{16}
=0.205704856.}
\]

Thus every MUX in the new collar asks for at least `1/16` less quadratic lift than the current live lift. This is a restricted-family margin statement only; it does not establish the minimum/maximum margin over arbitrary gates and does not prove FEI.
