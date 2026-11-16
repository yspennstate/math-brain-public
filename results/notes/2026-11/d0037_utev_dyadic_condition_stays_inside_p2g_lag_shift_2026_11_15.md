---
name: d0037_utev_dyadic_condition_stays_inside_p2g_lag_shift_2026_11_15
description: "[PROVISIONAL] Bradley Q8/Q9 interlaced mixing: does Utev's sum r(2^j)<inf reach past |P|^2 g? No - circle zeros shift r by one lag; f_{1,beta} Utev route closed"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T23:12:53+02:00
  status: provisional
  evidence: ""
---

D0037 / D0036 (Bradley 2005 Questions 9 and 8, interlaced rho*/r* mixing of Gaussian or weakly stationary sequences): Utev's sufficient condition sum_j r(2^j) < inf never reaches a density outside f = |P|^2 g (g continuous, positive). Proved 15 Nov, unrefereed.

Key step (Lemma 1, lag shift): if P has d zeros, all on the unit circle, and log h is integrable, then r_{|P|^2 h}(n) = r_h(n - d) for the ORDINARY past/future coefficient. Reason: the past/future angle is a Hankel form with symbol W/conj(W), W outer; a circle zero multiplies the symbol by c z. Checked numerically on AR(1) times |1-z|^2: finite blocks climb to |a|^(n-1).

Theorem 2: Utev's hypothesis gives HS form; Lemma 1 transfers the dyadic sum to h = exp(u+Hv); Utev gives r*_h -> 0; continuity of v gives r_h(1) < 1 (Helson-Szego after subtracting a trig polynomial); Bradley Thm 6.5(c) gives h continuous positive.

Corollary 3: for f_{m,beta} = |1-z|^(2m) log(2e/|1-z|)^(-beta), sum_j r(2^j) = inf. This closes Route P1 ("verify Utev for the special weight") of the September R14 handoff on D0036. f_{1,beta} itself stays open; every ordinary-coefficient argument sees it exactly like h_beta (shift by one lag), and h_beta has r* = 1 at every lag, so any proof must use the interlaced geometry.

Scar avoided: check referee_reports/2026-11-13/<id>A AND open-problems-repo runs (R08, R14, R15) before starting; the twin problem D0036 had three September runs stuck on the same weight.

Files: 12_cognitive_architecture/math/trio_1011/op/D0037/NOTE.md, CREDITS.md, shift_check.py. What would change this: a flaw in the outer-function form of the past/future angle when h has zeros, or Utev's implication being stated for a different coefficient than r (checked in the survey text, p. 129).


Plain words (how a non-specialist might ask): weakly dependent random sequences; when does dependence die out fast enough for a central limit theorem; correlation at gaps that are powers of two; spectral density of a stationary Gaussian process.
