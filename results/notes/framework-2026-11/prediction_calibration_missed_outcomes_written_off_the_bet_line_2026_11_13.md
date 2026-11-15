---
name: prediction_calibration_missed_outcomes_written_off_the_bet_line_2026_11_13
description: "[VERIFIED] Calibration checker listed 20 resolved bets as unscoreable (one id 'p=0.7'): it read outcomes only on the bet line; outcomes on indented lines, separate 'pNNN RESOLVED' lines and '-> MISS' bullets were dropped. Fixed 13 Nov (md5 961e4d73, origin 48b33cab): 280->293 scored, 4 truly unscoreable; selftest had been red on live-data drift, now on fixtures."
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T00:04:12+02:00
  status: verified
  evidence: "commit 48b33cab; scratchpad pcc_diff.py (13 additions, nothing else moved)"
---

Found by an agent on 13 Nov 23:4x. The evening dream log printed 20 bets as RESOLVED BUT UNSCOREABLE, and one of the ids was "p=0.7". prediction_calibration_check.py read the outcome only from the checkbox line itself. But the ledger often writes resolutions elsewhere:
- on the indented line under the bet ("  - outcome: MISS (SWS 08-17)", "  - Resolved hit (07-20 SWS)");
- on a separate checked line ("- [x] p228 RESOLVED MISS ...", "- [x] p209 resolved YES ...");
- on a plain bullet under a REM heading ("- p226 -> MISS (p=0.60)").

One bet was written "- [x] p=0.7 [infra] ..." with no id and no "p:" field.

Before the fix: scored 280, unscoreable 20. After: scored 293, unscoreable 4. A diff over the whole ledger found exactly 13 bets added and nothing else moved; each attribution was checked by eye (p157-p178, p52-p56, p226, the p=0.7 line). The four still unscoreable have no hit or miss anywhere: p37 is "retired, never-armed", and p175, p162 and p223 were checked off without an outcome. Live md5 961e4d73, on origin as GraphQL commit 48b33cab.

Second fault in the same file: --selftest was already failing before the change. Its positive controls asserted that the live owner cells were overconfident, the ledger had recalibrated to a gap of about -0.07, and the controls failed. That tests the data, not the code. The controls now run on fixed fixtures, plus a parser fixture for each outcome form; the live counts are printed, not tested.

Lesson for any checker: a selftest anchored to live data goes red when the world improves. Test the logic on fixtures and report the live state separately. When resolving a bet, write "| outcome:hit|miss | on:<date>" on the bet line itself; the parser now reads the other forms, but that is the canonical one.

