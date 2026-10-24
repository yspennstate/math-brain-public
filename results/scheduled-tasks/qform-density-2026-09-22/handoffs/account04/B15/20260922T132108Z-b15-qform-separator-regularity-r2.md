# account04/B15 handoff — conditional separator smoothing

**Run:** 20260922T132108Z-b15-qform-separator-regularity-r2  
**Programme:** QFORM-DENSITY-3EIG-20260922, revision 2026-09-22.5  
**Status:** ESSENTIAL-STEP-APPLIED / FULL TARGET OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

Canonical source:

- repository: yspennstate/math-open-problems
- commit: 657566d3f5026e672f5cbe6b8c03fe63766bf0fb
- path: proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T132108Z-b15-qform-separator-regularity-r2/REPORT.md
- report blob: 81545c48302ae524a50d8fd7cf3aa3f2c6c971f8

Assigned partner actually applied:

- account01/B15
- yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553
- proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260922T120320Z-account01-B15-qform/REPORT.md

## New theorem

In the original independent coordinates, suppose
\[
 A=\begin{pmatrix}
 B&0&E\\
 0&D&F\\
 E^T&F^T&G
 \end{pmatrix},
\]
where \(B\) is an invertible symmetric block of order \(d=3\) or \(4\), and
\[
 x_J\mapsto x_J^TDx_J+2x_J^TFX_K
\]
is nonconstant almost surely. The latter holds in particular if \(D\ne0\) or \(F\ne0\).

Then \(Q=X^TAX\) has a density \(p_Q\in C_0(\mathbb R)\), so it is bounded and uniformly continuous, with
\[
 \|p_Q\|_\infty\le
 \begin{cases}
 (2\pi+3\sqrt3)/\sigma_{\min}(B),&d=3,\\
 (4\pi+8)/\sigma_{\min}(B),&d=4.
 \end{cases}
\]

Proof: condition on \(X_K=z\). The \(I\)- and \(J\)-summands remain independent. Account01/B15 bounds the affine quadratic on \(I\) uniformly in \(z\). The \(J\)-summand is a nonconstant affine quadratic and therefore has an \(L^1\) density. Their convolution is in \(C_0\), has the same height bound, and averaging over \(z\) preserves continuity and vanishing at infinity by dominated convergence. No uniform conditional modulus is needed.

This strictly extends the earlier \(A=B\oplus D\) branch: \(E,F,G\) may now be arbitrary. The exact separator \(A_{I,J}=0\) is the remaining structural hypothesis.

## Boundary and correction

The full universal constant remains open. The bound retains \(\sigma_{\min}(B)^{-1}\), and a fully dense \(A\) may have no suitable separator. The fresh account01/B15 event QFORM-LOCAL-CROSSBLOCK-DICHOTOMY-FALSE was consumed: the local-block/cross-block alternatives are not exhaustive, so this theorem must not be promoted into a universal dichotomy.

Next implication: find an \(A\)-independent conditional height mechanism that covers mixed localized/diffuse matrices without a well-conditioned fixed principal block or an exact coordinate separator. Continuity for the fully dense case remains separate.
