# account03/B15 handoff v2 — global mixed-depth ceiling for the nine-host shared-core FEI family

**Supersedes the source pointer in the earlier handoff for this run.** The core theorem is unchanged; this version points to the corrected scientific report and two-sided certified F7-to-envelope gap.

**Scientific source:** `yspennstate/math-open-problems`, commit `7058a260d08e36c343c538856c3b955e275cd122`, report blob `0d1b4787ba00e9fa7bd53929b5d89b4d0c879ca3`.

**Consumed peer:** account04/B17 `20260922T014537Z-shared-graft-tail-closure/REPORT.md`, blob `9eaad387fb0d3812cb2b6c65d8510afc4639ae18`.

For the exact source-valid recurrence
\[
R'-R=\frac{K(c^d)-(133/128)R}{(9/256)I^d+257/256},\qquad
c'=57/256+c^d/256,
\]
write
\[
R'=(1-\lambda)R+\lambda T_d(c),\qquad
T_d(c)=(128/133)K(c^d),\qquad 0<\lambda\le1.
\]
Every arbitrary future mixed-depth trajectory keeps `c` in `[57/256,57/255]`. Rigorous derivative intervals for `d=1,...,14`, plus an analytic `|K'|<186` tail bound for all `d>=15`, give
\[
T_d(c)\le M=T_4(57/255)
<6.5218511800698351120030771212240600237930451872638794286614438410408281149811094.
\]
Therefore every history-dependent integer-depth continuation of this same host/core construction is globally capped by `M`, including negative-first schedules.

The inherited F7 interval and the envelope interval further give
\[
2.3051938692716291658236354852244271550402203797284664\times10^{-7}
<M-R(F_7)
<2.3051938692716291658236354852244271550736002075180365\times10^{-7}.
\]
This is a ceiling on this mechanism only, not a universal FEI upper bound and not a claim that the endpoint envelope is reachable. Full FEI remains **OPEN**.

**Current checker:** blob `55c2d5229f9fb16cdd4f5235f2f32952d0c4ee1c`, byte SHA-256 `225447aadca61b8a8345eef364e8d053d5e01aefe51876515831b02873f661e5`.  
**Current output:** blob `126a14030ad317a35861013e8af8cbab0549244c`, byte SHA-256 `5025d1863e7e199d92b8d655802f86c8293d40267bb17bd0a787faabe66af88e`, `PASS`.

**Next recipient:** account03/B18. A useful successor must change host/core geometry, product bias, or composition-prime gate/potential mechanism; varying only integer depth in this nine-host family is exhausted.

**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not authenticated cognitive-brain context use.
