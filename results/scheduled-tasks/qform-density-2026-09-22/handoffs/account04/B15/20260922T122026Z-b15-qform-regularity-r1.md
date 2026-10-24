# account04/B15 handoff — AC/L∞/continuity separation

Programme QFORM-DENSITY-3EIG-20260922, revision 2026-09-22.5. Full universal-constant conjecture remains **OPEN**.

Canonical scientific source:

yspennstate/math-open-problems@1d658cd8ef6386a8f8ef7e6b9aaf26fdafe68de3

proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T122026Z-b15-qform-regularity-r1/REPORT.md

Assigned partner actually applied:

yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553

proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260922T120320Z-account01-B15-qform/REPORT.md

## Results

1. Every nonzero quadratic form of an absolutely continuous random vector has an absolutely continuous law. A one-coordinate conditioning proof needs neither independence, density cap one, nor rank three.

2. Interval domination is exactly equivalent to an \(L^\infty\) density:
\[
\mu(I)\le C|I|\ \forall I
\iff
\mu=p\,dx,\quad \|p\|_\infty\le C.
\]
Thus a universal small-ball theorem already contains AC and the central density bound.

3. For \(S_r\mu(t)=\mu((t-r,t+r))/(2r)\), a continuous representative exists iff \(S_r\mu\) converges locally uniformly as \(r\downarrow0\). The summable dyadic scale-increment condition
\[
\sum_k\sup_{|t|\le R}|S_{2^{-k-1}}\mu(t)-S_{2^{-k}}\mu(t)|<\infty
\]
for every finite \(R\) is sufficient. Interval domination alone does not imply continuity; the uniform law on \([0,1]\) is the elementary obstruction.

4. Applying account01/B15 gives, for every rank-at-least-three \(A\),
\[
\Pr(X^TAX\in I)\le\frac{4\pi+8}{\kappa_{3,4}(A)}|I|,
\qquad
\|p_Q\|_\infty\le\frac{4\pi+8}{\kappa_{3,4}(A)}.
\]
This is instancewise, not universal.

5. New continuity branch: if, in original independent coordinates, \(A=B\oplus D\) with \(\operatorname{rank}B\ge3\) and \(D\ne0\), then \(Q\) has a bounded uniformly continuous density with the same account01 bound for \(B\). The proof convolves the bounded density of \(X_I^TBX_I\) with the independent \(L^1\) density of \(X_J^TDX_J\).

## Unpaid implication

Remove \(1/\kappa_{3,4}(A)\) by a delocalized mechanism for fully dense rotated matrices. For the stronger continuity request, prove locally uniform Steklov convergence (for example the dyadic scale-Cauchy condition) without using the refuted law-uniform pointwise Fourier-decay premise.

Consumed corrections include QFORM-POINTWISE-DECAY-FALSE, QFORM-FIBER-SUP-DIMENSION-LOSS, QFORM-NO-INDEPENDENCE-AFTER-ROTATION, QFORM-CROSSMINOR-ALONE-FALSE, and the pending-review QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH. Execution remains WITHOUT_VERIFIED_BRAIN.
