---
name: p0434_fixed_law_heavy_traffic_ratio_tends_to_one_2026_11_08
description: "P0434 8 Nov 17:2x: for any fixed discrete law T_MS/T_G -> 1 as rho -> 1 (same blow-up classes k >= first argmax of mean residual life, same coefficient); 3000 laws 0 failures; ratios near 2 need load-dependent laws"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:28:45-05:00
  status: provisional
  evidence: "kstar_check.out, pushed 186f2349"
---

P0434 (M-SERPT vs Gittins, Conj. 8.1 T_MS <= 2 T_G), 8 Nov 17:2x, an agent. For any FIXED discrete size law,
T_MS/T_G -> 1 as rho -> 1.

Why: in the SOAP formula (split.py) rank falls inside each piece, so residence stays bounded and only waiting blows
up, and only for classes k >= k*, k* the first piece whose left-end rank is the overall maximum. Their leading term is
(1 - rho) p_k T_k -> p_k E[S^2] / (2 E[(S - s_{k*-1})^+]) under either policy. M-SERPT's left ranks are the running
max of the mean residual life MRL; Gittins's rank is <= MRL everywhere (Delta = infinity) and equals MRL where MRL is
at its maximum over later ages (MRL(a) = E[min(S-a,D)] + P(S>a+D) MRL(a+D)). So k* is the first argmax of MRL for both
and the leading coefficients agree class by class.

Measurement: kstar_check.py, 3000 random laws (seed 72), 0 failures of k*_MS = k*_G = first argmax MRL; 60 laws at
1 - rho = 1e-8, coefficient formula within 4.2e-5 relative, |T_MS/T_G - 1| <= 9.3e-8. Files in
codex_fleet/runs/own_p0434 (NOTE.md section 17:2x), pushed 186f2349.

How to apply: a heavy-traffic check on a fixed law says nothing about Conj. 8.1; the ratios near 2 (tie family 1.9886)
need laws built for each load. The earlier gain_rate/gain_coef results (G-/T_G -> 0) are this fixed-law fact. Any
heavy-traffic lemma for the route has to be uniform over load-dependent laws, as in 637c11d8's R bound.
Related: [[p0434_gross_loss_stays_under_gittins_time_and_is_tight_2026_11_08]], [[p0434_heavy_traffic_upper_bound_passed_an_independent_read_2026_11_08]].

