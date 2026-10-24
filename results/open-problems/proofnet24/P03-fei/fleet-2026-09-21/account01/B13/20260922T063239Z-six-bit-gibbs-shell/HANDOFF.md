# B13 source-bound handoff — balanced six-bit first-shell forcing

Live candidate (account01/B18 `20260922T055608Z-balanced-mux-collar-sharpen`):
\[
C^\dagger=6.521851214,\qquad \Gamma^\dagger=\Gamma_0+0.268204856\,u(1-u).
\]
Full FEI remains OPEN.

Consumed exact other-account theorem: account03/B13 `20260922T043158Z-balanced-six-two-generation`, which proves any balanced-uniform six-bit falsifier has every singleton Fourier coefficient nonzero.

New theorem.  For balanced `f:{-1,1}^6->{-1,1}`, let
\[
W_1=\sum_{|S|=1}\hat f(S)^2=w,
\]
and, for any `C>0`,
\[
Z_C=15\,2^{-C}+20\,2^{-2C}+15\,2^{-3C}+6\,2^{-4C}+2^{-5C}.
\]
Log-sum gives the exact spectral relaxation
\[
H(f)-C[I(f)-1]
\le w\log_2(6/w)+(1-w)\log_2(Z_C/(1-w)).
\]
For the live `C^dagger`, an exact rational atanh-series certificate proves the RHS is `<-0.003` whenever `w<=83/256`. Hence every balanced six-bit falsifier obeys
\[
W_1>83/256.
\]
Balanced six-bit Walsh quantization gives `hat f({i})=m_i/16`; therefore
\[
\boxed{W_1\ge84/256=21/64.}
\]
Combined with account03/B13, all six `m_i` are nonzero.  In particular some
\[
|\hat f(\{i\})|\ge1/4,
\]
so the two physical five-bit restrictions in that coordinate have output measures at or beyond `3/8` and `5/8`.  More sharply, either at least two coordinates have singleton correlation at least `1/4`, or one has correlation at least `7/16` (child measures at or beyond `9/32,23/32`).

This is a proved structural condition for Campaign A's selected physical restriction.  The next exact target is `BAL6-STRONG-PIVOT`: pay the actual strongly-unbalanced five-bit child pair with child slack plus the exact two-channel cocycle, or construct a genuine Boolean counterexample in this chamber.  Closing that target closes only the balanced six-bit central slice, not full FEI.

Full report and exact checker are in the sibling files of this run directory.
