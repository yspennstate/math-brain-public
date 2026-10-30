# Addendum — later same-run candidate correction

A later compatible FEI handoff arrived after `REPORT.md` had been committed and read back:

- fleet01/B16, `20260922T0912Z-tilted-quartic-strong-prime-refutation`, scientific report commit `ac14ec35cc17f2aefa93a638db148d43582309f2`.

It **refutes** fleet03/B12's `TILTED-QUARTIC-GATE-REPAIR-v1` candidate on the genuine composition-prime 18-input Numaro gate at
\[
p_1=223/456,\qquad p_2=\cdots=p_{18}=1/2,
\]
with
\[
D_{\Gamma^*}<-0.020406.
\]
Therefore the phrase “current proposed center” in Section 4 of `REPORT.md` is historical by the end of this invocation: \(C_*=6.538805311222222\ldots\) is **not** a live universal candidate center.

This does not alter Theorems 1.1 or 2.1. They hold for **every finite center \(C\)** and for arbitrary symmetric potentials on the balanced-uniform suspension face.

The same fleet01/B16 handoff proves that any repair restricted to the already-proved safe \(\eta_*\) ray must have
\[
\lambda>0.30111139168944795\ldots,
\qquad
\Gamma(1/2)>6.558444612295593\ldots
\]
merely to pay that one source. Applying the no-loss theorem at the boundary value
\[
C=6.558444612295593
\]
still shows that retaining only \(99\%\) of \(K_{\rm occ}\) fails on the one-point-defect suspension; the stable closed form is already negative at \(m=260\):
\[
\frac{B_{\rm inf}^{C}+0.99K_{\rm occ}}{I(g_{260})}
=
-0.00173824650158\ldots<0.
\]
For any larger but finite center the same failure occurs at some later finite \(m\), by Theorem 2.1.

Thus the target-level candidate moved during this run (`Gamma*` is refuted), while the mechanism-level conclusion sharpened rather than weakened:

> **Any finite-cap all-gate repair, including future Bellman/safe-ray replacements, must preserve the dependence KL to additive influence scale on sparse suspensions. No fixed multiplicative fraction of the KL is universally enough.**

Full FEI remains OPEN.
