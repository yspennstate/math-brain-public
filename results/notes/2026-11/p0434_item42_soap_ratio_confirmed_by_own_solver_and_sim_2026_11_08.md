---
name: p0434_item42_soap_ratio_confirmed_by_own_solver_and_sim_2026_11_08
description: "[VERIFIED] P0434 8 Nov 07:4x: 637c11d8's item 42 (M-SERPT/Gittins = 1.0580537 on {1, 1+3/40000, 9/4}, rho 1-511/5000, above S2 and 2u/(1+u)) reproduced exactly by an independent SOAP solver and by a 4x2e6-job CRN simulation (mean 1.05802, SE 0.00016)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:48:12-05:00
  status: provisional
  evidence: ""
---

An independent check of route item 42 by an agent on 8 Nov 2026, files at 06_math_research/frontier/P0434/audit_agent_2026_11_08 (AUDIT_W3EXACT.md, soap_indep_e05f.py, sim_crn_e05f.py), brain-repo main e76f27f9. (1) Exact SOAP written from the definitions without reading soapsym gave the same rational 3603245628507169277452152326763/3405541372448168038224798422263. (2) An event-driven M/G/1 simulation on common random numbers, which does not use the SOAP theorem, gave ratios 1.05838, 1.05762, 1.05813 and 1.05796 over 4 seeds of 2e6 jobs: mean 1.05802 against the exact 1.05805, about 14 standard errors above 2u/(1+u) = 1.05573. So the conjecture sup = max(S2, 2u/(1+u)) is false near K = 9/4. The mechanism: Gittins rank collapses to about 0 on the age band [0.9995, m), so a job that reaches age 1 finishes at once under Gittins, while M-SERPT's ranks there are 1.08625 and 1.08628, nearly tied, and arrivals preempt it. Not checked: that this point is the maximiser, or K other than 9/4. A simulation-loop lesson from the same check: landing a served job's age as a + (t - now) at a piece end can round to just below the end and loop forever on zero-length steps; set the age to the end exactly. Links: [[p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08]], [[p0434_mserpt_lower_bound_2u_over_1_plus_u_passed_a_second_audit_2026_11_08]].
