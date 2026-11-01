# r13 correction — coloured endpoint score notation

This correction preserves the already-committed `REPORT.md` rather than silently overwriting it.

In Section 6, equation (22) contains a sign-placement typo in the displayed coloured endpoint score. The correct score for a coloured matching `(rho,epsilon)` is

\[
\sum_{\alpha=1}^3\left(\epsilon_\alpha K_{\alpha,\rho(\alpha)}+\frac12X_{\alpha,\rho(\alpha)}\right),
\qquad \epsilon_\alpha\in\{+1,-1\},
\]

with an even number of `epsilon_alpha=-1` for the 24 genuine `S_4`/`SO(6)` endpoints. Equivalently, a plus channel has coefficient `K+X/2` and a minus channel has coefficient `-K+X/2`, exactly as stated correctly in equation (8) and used by `verify_odd_weyl.py`.

No theorem, exact enumeration, counterexample, outcome label, or remaining implication changes.
