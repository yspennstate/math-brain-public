---
name: p0434_heavy_traffic_upper_bound_passed_an_independent_read_2026_11_08
description: "[VERIFIED] P0434 8 Nov 04:4x: 637c11d8's heavy-traffic bound R <= 2 sqrt(e*)/(1+sqrt(e*)) (reduction Lemmas A-E + Steps 0-3) passed e05f1f39's read with its own SOAP code; one write-up gap (final hull slope 1)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:36:29-05:00
  status: provisional
  evidence: ""
---

Status: verified (independent read plus independent code), 8 Nov 2026 04:4x EST, an agent for an agent.

The heavy-traffic upper bound for P0434 (M-SERPT vs Gittins, unit atom plus t-small atoms, t -> 0): R -> J_MS/J_G <= q = 2 sqrt(e*)/(1 + sqrt(e*)), e* the largest mean residual over corners. Files: ~/codex_fleet/runs/own_p0434/reduction_agent.md, proof_reduced_agent.md; my audit audit_upper_e05f.md and indep_check_e05f.py (+ check2, check3, .out) in the same folder.

What I checked by hand: every lemma and step. Step 3's one-vertex inequality is an equality at gamma = sqrt(e*) D*, so the step is tight. Lemma A does not depend on which denominator SOAP puts on the later old intervals (their numerators are O(t)).

Measured with code that shares nothing with soap.py: Lemma A for M-SERPT, gap 4.2e-3, 4.2e-4, 4.2e-5, 4.2e-6 at t = 1e-5..1e-8 (O(t)); min over all record sets = hull integral to 4e-16 (300 laws); 2000 random laws, 374 trivial (no corner with e > 1, R = q = 1), largest R/q on the other 1626 was 0.99929.

Trap I nearly fell into: the first run printed max R/q = 1.000000 and it looked like random laws reached the extremal bound. They were the trivial laws where both sides are 1. Split trivial cases out before reading a max ratio.

Gap in the write-up: Lemma E shows slopes <= 1 but not that the final slope is exactly 1; z + min_p(D_p - z_p) is a convex minorant of S, which closes it. Not checked: SOAP Thm 5.5 and Gittins optimality (cited), sharpness family. Related: [[p0434_mserpt_lower_bound_2u_over_1_plus_u_passed_a_second_audit_2026_11_08]], [[p0434_heavy_traffic_reduces_to_a_staircase_hull_inequality_2026_11_08]].
