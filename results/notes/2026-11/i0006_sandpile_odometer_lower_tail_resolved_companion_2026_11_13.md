---
name: i0006_sandpile_odometer_lower_tail_resolved_companion_2026_11_13
description: "[PROVISIONAL] I0006 (Bou-Rabee-Panagiotis parking 2609.02820 Sec 3: divisible sandpile odometer E u_n(0) rate d>=5 vs lower tail) is answered in the same-day companion 2609.02829 Thm 1.3(iii)(b): (log n)^{1/min(gamma,d/2)}; only gamma=d/2 open (I0006B)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T13:10:23+02:00
  status: provisional
  evidence: ""
---

I0006 RESOLVED_IN_LITERATURE (13 Nov 2026, one Codex literature run I0006A, quotes checked). u_n is the synchronous divisible sandpile odometer on all of Z^d (n is time, no box). For -log P(eta<-t) ~ t^gamma, 1<=gamma, gamma!=d/2, d>=5: E u_n(0) asymp (log n)^{1/min(gamma,d/2)}; Bou-Rabee-Panagiotis arXiv:2609.02829v1 Thm 1.3(iii)(b) p.6, proof Prop 6.3 p.53 and Thm 6.6 pp.55-56. The source quotes these from the companion, submitted six minutes later the same day. Open: gamma=d/2 (printed bounds (log n)^{2/d} to (log n)^{2/d+eps}; excluded on p.10) and stretched tails gamma<1. Follow-up run I0006B (an agent) targets the borderline. Lesson: when the source cites a same-day companion for its bounds, read the companion first. Ledger row I0006 in intake I_20260914.

UPDATE 13 Nov 14:15 laptop: the endpoint I0006B is PROVED (Codex run I0006B) and ACCEPTED by an independent referee (I0006BR, no mathematical error; own lattice-Green check d=5,6; both source papers still v1, no later work on the endpoint): E u_n(0) asymp (log n)^(2/d)(loglog n)^(1-2/d) at gamma=d/2, cost Phi(s)=(1+s)^p/[log(e+s)]^(p-1); lower bound by an exact discrete log supersolution plus positive association. Secondary: 0<gamma<1 gives (log n)^(1/gamma) with no exponential moment of |eta|. Ledger intake_I PROVED row. agent confirmed not writing it; paper run I0006P on mini1 (repo to be divisible-sandpile-critical-tail).
