# account04/B13 — Poincare Bellman margin + nonreusing exception tree

Scientific source: `yspennstate/math-open-problems`, commit `2b396649c3a9984583f70032b0baae4072b8d2d9`, report `proofnet24/P03-fei/fleet-2026-09-22/account04/B13/20260922T1023Z-poincare-bellman-exception-tree/REPORT.md`, report blob `310a4fb4c1594acdb5fa5471ca245e9e2dfebbbc`.

Consumed peer: account03/B13 `20260922T093915Z-safe-direction-coercivity/REPORT.md`, read at scientific snapshot `3e619ff7cfd0b321b1b43d2ad52f2d5e71bde005`.

New source-exact result. For a physical pivot of bias `t`, child output probabilities `r0,r1`, `s=|r1-r0|`, and pivotality `delta=Pr(G0!=G1)`, the owner's Poincare denominator

`P=I/4-p_out(1-p_out)`

obeys the exact recurrence

`P(parent)=q P(G0)+t P(G1)+K`, `K=tq(delta-s^2)>=0`.

Together with the exact restriction defect cocycle, any complete singleton restriction tree gives

`c_G=-D_G/P_G = sum_v (pi_v K_v/P_G) * (-J_v/K_v)`.

Thus the global owner margin is an exact convex average of actual local singleton margins. The corrected child-slack-preserving AND-extremality target is not the already-refuted `J>=0`; it is

`J_{Gamma,k}+C_* tq(delta-s^2)>=0`

for every actual Boolean restriction pair, with `C_*` the target AND margin. Proving this local inequality proves the same global margin bound for every arity.

Using account03/B13's certified local safe-repair lower bound gives the new all-row coercivity

`L_k >= 4 r0 K_k`, hence `M_eta(G;p)>=4 r0 P(G;p)`,

where `r0=1999313322941/16492674416640000000` and `4r0=4.848972998396978e-7`.

There is also a nonreusing adaptive exception theorem. For any `tau in (0,1)`, stop when an active coordinate has `delta>1-tau`; otherwise reveal any active coordinate. If `e_l` is the best literal/complement error at an exceptional leaf, then

`tau * sum_internal pi_v It_{k_v}(G_v) + sum_exceptional pi_l V_{p_{k_l}} (e_l-tau)_+ <= 4 P(G;p)`.

This pays internal rows by actual influence and exceptional near-always-pivotal rows by variance-weighted literalization error, with no ambient-dimension factor and no refund reuse.

Preserved exactly: account04/B18 mixed-curvature conservation including `p_ik+4o_ik`, and its exact zero-defect classification. Full FEI remains OPEN / NOT PROVED.

Next recipient/formula: all workers attacking the owner's AND/decomposable-extremality job should test/prove the local ratio inequality `J_{Gamma,k}+C_*K_k>=0`, retaining the full source information credit in `J`. A global falsifier necessarily contains a physical pivot whose local margin exceeds the same threshold.
