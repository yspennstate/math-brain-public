---
name: a_decision_signature_changed_while_the_soap_ratio_did_not_2026_11_08
description: "[VERIFIED] P0434 8 Nov 09:1x: along the M-SERPT tie the run_float decision signature changed at m - 1 = 3e-9 on all 64 lines, yet the region's closed form matched soap.ratio to 2.4e-15 up to m - 1 = 0.01; region validity must be tested by value agreement, not signature equality"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T09:12:36-05:00
  status: provisional
  evidence: ""
---

Route item 57 (commit dbb78438, w3mstep2_agent.out). The first check compared every line's signature with one base point's and called all 64 lines invalid at their first point; the second compared each line with itself and still saw changes at once, because the signature records decisions that never reach the mean response. Value agreement with soap.ratio (gap < 1e-8) is the test: 64/64 lines to m - 1 = 0.01, broken past that. How to apply: in any region-validity claim on P0434 (items 36-40, 56-58) quote the value gap, not signature equality. Links: [[p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08]]
