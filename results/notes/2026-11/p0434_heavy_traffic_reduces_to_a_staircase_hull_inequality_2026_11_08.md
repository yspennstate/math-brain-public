---
name: p0434_heavy_traffic_reduces_to_a_staircase_hull_inequality_2026_11_08
description: "[PROVISIONAL] P0434 (M-SERPT vs Gittins on [1,K]) 8 Nov: near a unit atom, the order-1/t cost is a path integral over the work/completions staircase; Gittins = convex minorant, M-SERPT = slope-to-end records"
metadata:
  node_type: memory
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T01:17:04-05:00
  status: provisional
  evidence: ""
  modified: 2026-11-08T07:13:19.583Z
---

Regime: mass 1 at size 1, masses t*m_k at s_k in (1,K], eps = gamma*t, t -> 0. SOAP Thm 5.5's denominator uses only the first old and first new intervals, so a policy enters only through the record ages of its running-max rank. With x = completions and y = work past age 1, 2tT = int dx/(gamma+W-y)^2 along ray(slope 1) -> chosen staircase corners -> end. Inserting corner G into chord PQ changes cost by phi_P phi_G phi_Q dx dx (slope_PG - slope_GQ), which is gamma-free, so Gittins is the convex minorant. M-SERPT takes records of the slope to the end. Checked against soap.mean_T at t=1e-7 on 12 random laws (rel err 5e-7..1.1e-3); the 3-atom family gives 2u/(1+u) to 9 digits; a Nelder-Mead search (1-4 atoms) found nothing above 2u/(1+u). The upper bound in this regime is one geometric inequality, not yet proved, and the regime does not cover laws without a heavy bottom atom. Files: ~/codex_fleet/runs/own_p0434/route_agent.md item 7, reduced_agent.py/.out, reduced_search_agent.*. Related [[p0434]].

8 Nov 01:3x (route item 9). Sharper conjecture in this regime: R <= 2 sqrt(e*)/(1 + sqrt(e*)), e* = the largest mean residual life at ages >= 1 (e* <= K - 1 gives 2u/(1+u)). Proved when Gittins' first vertex is v* (the corner of largest e) and every M-SERPT vertex sits at v*'s depth (an atom cluster just below h*, any law above). Equality holds along that whole case at gamma/D* = sqrt e*, and an optimizer found it at h* = 1.337, K = 3. 6000 random laws and a 54-run Nelder-Mead found nothing above it. Two dead ends: the gamma-by-gamma form of the bound fails (+0.024), and the part beyond v* taken alone reaches 1.47 times the bound, so an induction has to carry the shared chord term D*/(gamma gamma'). Still open: corners beyond v* at greater depth. Files split_agent.*, estar_agent.*, estar_search_agent.*. Scope, measured with the exact evaluator: the e* form holds only at leading order. A general law (K=3, mass 1e-3 at 2.003, eps 0.026) beats it by 6.9e-5 at t=1e-3, an O(t) term that changes sign by t=1e-4. Never quote it as a finite-load bound. 01:47 (route item 10, proof written out, checked on 4399 laws): any policy's depth-at-width satisfies z_H(D) <= (2 - 1/e*) z_MS(D). So R <= (2 - 1/e*)^2 < 4 is PROVED in the reduced regime. Pointwise envelopes alone cannot give the sharp bound: the relaxed problem reaches 2.39 at e*=9. 02:1x (route item 12): the gamma-wise bound fails even taken as the max over every corner of the two-atom value F(e_c, gamma/D_c): a 5-atom K=10 law (witness in gwise4d_agent.py) gives R 1.248504 by soap.mean_T at t=1e-8 against 1.245258, with the sup bound 1.3476 intact. Any proof has to work with the sup over gamma or with several corners at once.
