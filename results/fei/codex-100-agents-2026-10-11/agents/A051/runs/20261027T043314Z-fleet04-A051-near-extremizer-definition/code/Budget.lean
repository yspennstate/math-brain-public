import Mathlib

theorem a051_shifted_budget (H I sigma t R Hbar K eps L : Real)
    (hI : I = sigma + t + R) (hL : L = H - Hbar) :
    (H - (K+eps)*I) + ((K+eps)*t-Hbar) + (K+eps)*R = L-(K+eps)*sigma := by
  rw [hI, hL]
  ring

theorem a051_occupied_budget (D S C R v W rest cap : Real)
    (h : D + S + C*R + v*W + rest = cap)
    (hD : 0 < D) (hS : 0 <= S) (hC : 0 <= C)
    (hR : 0 <= R) (hrest : 0 <= rest) (hv : 0 < v) :
    W < cap / v := by
  apply (lt_div_iff₀ hv).2
  nlinarith [mul_nonneg hC hR]
