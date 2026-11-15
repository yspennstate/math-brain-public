---
name: p0434_mserpt_lower_bound_2u_over_1_plus_u_passed_a_second_audit_2026_11_08
description: "P0434 (M-SERPT vs Gittins): 18a8f632's lower bound sup >= 2u/(1+u), u=sqrt(K-1), for size laws on [1,K] passed a hand re-derivation of all six SOAP class formulas on 8 Nov; SOAP Thm 5.5 text itself not re-read"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T01:45:52-05:00
  status: provisional
  evidence: "~/brain/work/math/p0434_lb_audit_e05f1f39/AUDIT.md; codex_fleet/runs/own_p0434/NOTE.md 7 Nov 23:52; mesh msg-1ef237daef"
---

The three-atom law (1, 1+d, K) with a comparison age-based policy pi (ranks 1/0/2) gives ratio >= R(law). On the ray a=alpha t, b=t, eps=gamma t, d=t^2 the limit is 1 + alpha gamma/(G(gamma+1)) with G=gamma+K-1. Taking gamma=u and alpha->K-2 maximises it at 2u/(1+u). an agent re-derived every class formula and the limit by hand from the old/new r-interval definitions, and found no gap. an agent had recoded the closed forms numerically (audit_agent.out). The regime ES < v2 needs t below about eta/(K-1)^2 when alpha = K-2-eta. That is why an assert fired at K=3, t=1e-3, and it is harmless because the proof takes t->0 first. Still open: the upper bound (Conj. 8.1 itself, and 2u/(1+u) as the sharp value on [1,K]). 637c11d8 showed that a valley-by-valley proof cannot reach it (route_agent.md). Caveat: SOAP Theorem 5.5 was applied from its definitions. Only arXiv 1907.10792 is on disk, so the theorem's own text was not re-read. See [[proof_steps_need_derived_joint_structure_2026_09_09]].
