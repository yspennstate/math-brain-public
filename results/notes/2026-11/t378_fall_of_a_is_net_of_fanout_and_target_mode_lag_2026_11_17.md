---
name: t378_fall_of_a_is_net_of_fanout_and_target_mode_lag_2026_11_17
description: "[PROVISIONAL] T378 mean-field SGD: why the slaved drift of the aligned mass A was 10x the real fall - a deterministic lag of v in the target-quadratic mode cancels ~90 pct"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T03:31:17+02:00
  status: provisional
  evidence: ""
---

T378 (two-layer ReLU, He_2 target, one-pass mean-field SGD, m 512). Slaving v to v*(W) on the stiff modes predicts the aligned mass A = sum |w_j|^2 (u_j.theta)^4 falls ten times faster than it does (d32 s4, n 1e8 to 3.16e8: slaved -150.9, actual -14.4). The noise-free population flow from the same state gives -14.96 (step size independent), so this is not SGD noise. The gap sits in one mode, the target-quadratic stiff mode (lambda 31.9, the smallest stiff eigenvalue): v under-fits it by a relative 7e-4 (m(v-v*)_q = -0.063 of 87.1), the He_2 left in the residual pulls aligned neurons back to theta, and that cancels about 90 pct of the fan-out. Lesson: in this model W is not slow next to the slowest stiff v mode, so a slaved (adiabatic) reduction is wrong at leading order; reduce on (W, v_q) with the lag term. A batch-size control is void if the batch is drawn as one block from the same generator: B 256 then sees the same sample stream as B 32. Status: provisional; next check is whether the lag equals -(dv*_q/dtau)/lambda_q. Record: 06_math_research/frontier/rows/T378/DOSSIER.md section 17 Nov 03:2x, commit 7af62818; scripts runs/long/lemmaF_mf_ode.py, lemmaF_lagmode.py.
