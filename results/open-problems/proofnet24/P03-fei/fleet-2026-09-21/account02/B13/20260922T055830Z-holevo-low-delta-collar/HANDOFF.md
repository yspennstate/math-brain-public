# Source-bound handoff: two-channel Holevo collar for campaign A

Source report:
`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T055830Z-holevo-low-delta-collar/REPORT.md`

Live fixed candidate:
\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger=\Gamma_0+0.268204856\,u(1-u).
\]

## New exact identities / inequalities

For a physical pivot of bias \(t\), with actual Boolean children
\(f_0,f_1\), disagreement \(\delta\), child square-spectral laws
\(P,Q\), residual spectral label \(S\), and parent pivot-spectral bit
\(J\),

\[
\mathcal L_{\Gamma,j}
=
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(qr_0+tr_1)
+\delta[\Gamma(t)+h_2(V_t)]
-I(B;S)-H(J\mid S).
\]

The cancellation is exact.

Boolean signed overlap gives
\[
\sum_S a_Sb_S=1-2\delta.
\]
Absolute-amplitude pure-state lifting plus Holevo/data processing gives
\[
I(B;S)\le
h_2\!\left(
\frac{1-\sqrt{1-4V_t\delta(1-\delta)}}2
\right),
\]
and
\[
H(J\mid S)\le h_2(V_t\delta).
\]

Hence for arbitrary actual Boolean children
\[
\mathcal L_{\Gamma,j}\ge
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(qr_0+tr_1)
+\delta[\Gamma(t)+h_2(V_t)]
-\chi_t(\delta)-h_2(V_t\delta).
\]

## New live-candidate collar

If both children are balanced, \(0<\delta\le1/4\), and
\[
u=\min(t,1-t)\le2^{-10}\delta^9,
\]
then
\[
\mathcal L_{\Gamma^\dagger,j}>0.
\]

Applying the completed account04/B13
`20260922T051245Z-biased-joint-credit-collar` theorem for
\(\delta\ge1/4\), every balanced-child pivot in a minimum-essential-arity,
global-bias-minimizing counterexample obeys

\[
\delta\ge1/4\Rightarrow u>2^{-15},
\]
\[
0<\delta\le1/4\Rightarrow u>2^{-10}\delta^9.
\]

The case \(\delta=0\) is inessential.

## Critical-core refinement

A false fixed candidate admits a minimum-essential-arity
composition-prime gate and an interior global bias minimizer.  For every
physical pivot, if \(d_0,d_1\ge0\) are the two child slacks and
\(\mathcal L_j\) is local gluing, then
\[
\mathcal L_j<0,\qquad
\mathcal L_j\le -\min(t,1-t)|d_1-d_0|.
\]

This secant statement is derivative-free and valid at piecewise-linear
knots of the source potential.

## Scope

Full FEI remains open.  The unpaid regions are intermediate pivot
biases and unequal child output measures.  The next source-exact use is
to combine the secant constraint with the all-child lower envelope while
retaining the actual potential Jensen term.

Checker:
`verify_holevo_collar.py`

Archived output:
`verification.txt`
