---
name: fei_symmetric_restriction_step_asymptotic_4_636_refereed_by_w22_2026_11_08
description: "FEI T021 8 Nov 19:5x: w22 refereed w18 with no gap: limsup_n max over symmetric f of Delta_1/I_1 <= 4.636423666 bits; asymptotic only, OR_3 4.8677 at finite n; explicit cutoff still open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T20:28:05-05:00
  status: provisional
  evidence: "codex/w22/REFEREE.md + final_audit.json (19,800-cell interval certificate, 2,035-table algebra audit, n<=1024 search); one referee, not hand-checked by me"
---

FEI T021, 8 Nov 2026 19:5x. Worker w22 (Codex 6.1, high) refereed w18's asymptotic restriction-step bound and found no gap. For symmetric Boolean f, limsup_n max_f Delta_1(f)/I_1(f) <= C_* < 4.636423666 bits, where C_* = [14/5 + (89/50) B(10) + 48/(23 sqrt(40 pi)) + exp(-z)/z] / ln 2, with B(v) = e^{-v} I_0(v) and z = 40 (23/48)^2.

- What this is: an asymptotic statement only. It gives some cutoff past which the restriction step on symmetric f costs under 4.6365 bits per unit of first-coordinate influence. It does not prove the all-n bound 4.8723, and the cutoff is not explicit. OR_3 still reaches 4.8677 at finite n (w06), so a finite-n theorem needs the small-n table plus an explicit cutoff.
- w22's checks:
  - It reviewed each assertion of w18's proof (sha256 a4770da3), with no w18 code imported.
  - It gave an independent 19,800-cell interval certificate of the scalar majorant, using different E1 estimates and a different mesh.
  - It ran an exhaustive algebra audit on 2,035 small-n tables and an exact-integer family search through n = 1024.
  - It ran central-window interval scans. The largest measured ratio was 4.38230 bits at n = 1024, edges [503, 541], which matches w08's 4.382301944832.
- The open step is an explicit finite-n estimate and cutoff. Combined with the certified tables (w06: n <= 16 exact, max OR_3 4.86767; w05: n = 17..32 below 4.24), it would give the symmetric restriction step at 4.8723 for every n. The cutoff would have to reach those table ranges.
- Files: brain/work/math/fei_sym_54e83a7b/codex/w22 (REFEREE.md, REPORT.md, final_audit.json), copied to 06_math_research/frontier/T021/fei_sym_agent_2026_11_08/codex_team/w22. Related: [[fei_restriction_step_on_symmetric_functions_stays_below_4_87_bits_2026_11_08]], [[fei_symmetric_constant_6_19_proved_with_bessel_lemmas_2026_11_08]].

