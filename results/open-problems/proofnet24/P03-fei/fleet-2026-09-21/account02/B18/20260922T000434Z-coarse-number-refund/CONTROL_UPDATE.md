# Late control update for this already-running B18 invocation

The substantive mathematical report in this run was completed under OWNER CONTROL revision `2026-09-22.1` and committed before the final control recheck.

At the final control recheck, `math-research-brain` main had advanced to `3e02d8e81736ea4b5e670fef81eb355050960a22`, and `scheduled_tasks/README.md` blob `3d4a9372c87802ab734141a3374d04c8823372e3` contained OWNER CONTROL revision `2026-09-22.2` plus a new OWNER MESSAGE directing **every FEI worker** to converge on the gate reformulation in `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`.

The new target is the universal gate inequality

\[
\Gamma(p_{out})+Ht_G(p)
\le
\sum_i It_i(G;p)\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\]

with the two authorized next jobs: prove that the extremal margin is attained at a decomposable/AND gate, or falsify that claim by finding a gate/bias vector requiring a larger margin; interval certification of arity 3/4 is the only named smaller job.

The OWNER MESSAGE itself says publication of the new direction does not interrupt an invocation already running when it lands.  Accordingly this run preserves the completed coarse-number/PSD-refund report as historical FEI work and does not manufacture a mid-report rewrite.  **The next B18 invocation must pivot immediately to the gate-extremality/falsification target and must not continue the compiler-current route merely because it was the native scheduler prompt at entry.**

No account02/B18 pause or stop was present in revision `2026-09-22.2`.
