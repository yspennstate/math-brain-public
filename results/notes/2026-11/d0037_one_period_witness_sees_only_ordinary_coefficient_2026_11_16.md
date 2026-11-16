---
name: d0037_one_period_witness_sees_only_ordinary_coefficient_2026_11_16
description: "[PROVISIONAL] D0037 Bradley interlaced mixing: can a periodic one-block-per-half-period witness push r* above r? No: liminf c >= r_f(g+1) and c <= (2r_f(g+1)+eps_p)/(1-eps_p); numbers at p=2^20 decay with lag (0.168/0.130/0.109 at lags 4/16/64)"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:58:54+02:00
  status: provisional
  evidence: ""
---

Proposition 4 and Corollary 5 in the private repository, 12_cognitive_architecture/math/trio_1011/op/D0037/NOTE.md. For f = |1-z|^2 h_beta, the best one-period witness (one S-block and one T-block per period p, shifted by p/2) at gap g satisfies liminf_p c(p,g) >= r_f(g+1) (needs only sum|fhat| < inf and r_f(n)->0) and c(p,g) <= (2 r_f(g+1)+eps_p)/(1-eps_p), eps_p = tau(p/2)/lam_min(T_{p/2}(f)). Corollary: if eps_p->0 then sup_p c -> 0 as g grows, so such witnesses cannot disprove the conjecture. Not covered: several alternations per period, shapes changing across scales, non-periodic patterns (R14 handoff section 4.2). Matrix-free LOBPCG (periodic_lobpcg.py) reaches p=2^20 in minutes: lag 4 0.1684, lag 16 0.1304, lag 64 0.1089; free a,b equals a=b everywhere checked. Status provisional: ours, not refereed, literature not searched beyond the R14 notes. **Why:** closes the cheapest periodic route for D0037. **How to apply:** a new D0037 witness attempt must vary the shape across scales or alternate several times per period.
