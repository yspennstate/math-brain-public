# PROB20-14 — append-only correction to 2026-09-16T11-42-00Z report

This note corrects one endpoint sentence in the substantive report

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/runs/2026-09-16/2026-09-16T11-42-00Z__report.md`

creation commit `d000dae9efc9c9defd6c6b0b04dcf7f1dff2e7c1`, exact-readback blob `68352b2aad6f8f1fba7286023a1a6f9970833aa1`.

## Correction

In Section 3, after defining the residual deficit
\[
b'=b+d-1,\qquad N=m-1,
\]
the sentence treating the endpoint `N-b'=N` incorrectly wrote `P_1=\pi=P_0 at zero tilt when appropriate`.

The correct convention is:

- if `b'=0`, the residual target is `S_N=N`, its mean-matched canonical reference is the **zero-tilt law**
  \[
  P_1=\pi,
  \]
  and
  \[
  c_{N,0}:=-\log \pi^{\otimes N}(S_N=N);
  \]
  there is no reason for the original reference `P_0=P_{m,b}` to equal `\pi` when `b>0`;
- if `b'=N`, the residual target is `S_N=0`; use the limiting canonical reference `P_1=\delta_0` and `c_{N,N}=0`.

With this corrected endpoint convention, the exact deletion identity remains
\[
\frac{\mu_{m,b}(d)}{P_{m,b}(d)}
=
\exp\{c_{m,b}-c_{m-1,b+d-1}-(m-1)D(P_1\|P_{m,b})\}.
\]
The proof in the substantive report is unchanged: it is simply the constant likelihood ratio of two exponential tilts on the residual exact-sum slice.

The unresolved tail bridge has `b=o(m)` and `d\to\infty`, `d=o(m)`, so eventually `1\le b'\le N-1`; consequently neither endpoint affects the new cliff certificate or the lacunary construction in Sections 4–5.

No other claim is changed by this correction.  The mathematical status remains **PARTIAL / OPEN**.