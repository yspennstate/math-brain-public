# Readback clarification

This file records two notation/source clarifications to `REPORT.md`; neither changes Theorem 4.1 or its constants.

1. In the Fannes--Audenaert estimate (4.15), the symbol in
   \[
   h_2(\theta)\le \theta\log_2(\mathrm e/\theta)
   \]
   is **Euler's number** `\mathrm e`, not the perturbation variable `e=q_0-1/2` introduced in (4.4). Thus the subsequent bound uses `\mathrm e<3` and gives `5\mathrm e<15`.

2. The nonnegativity in Lemma 3.3 is source-supported, not an extra assumption: the same pinned h96 envelope used by the A lead has
   \[
   G(x)-4.9096x\ge2.229>0
   \]
   on the small side. Therefore `Gamma_0>=0`, the quadratic lift is nonnegative, and hence `B(s)=Gamma^dagger(s)+h_2(V_s)>=0`. The upper bound `B(s)<9` in the report is unchanged.

The arithmetic checker and the certified final margin `9/8192>1/1000` are unchanged.
