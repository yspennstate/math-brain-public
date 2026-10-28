import Mathlib.Tactic

-- Uncompiled: memory admission was held. This only formalizes the scalar
-- terminal-price implication; Fourier identities and finite partitions remain
-- separate prose/certificate obligations.
theorem mixed_terminal_price
    (W U r k kp ig ce : ℝ)
    (hr : 0 ≤ r) (hsource : ce ≤ 4 * ig)
    (hfull : 2 - U - r * (k + kp + 7) + r * (ig - ce / 4) ≤ W) :
    2 - U - r * (k + kp + 7) ≤ W := by
  have hgap : 0 ≤ ig - ce / 4 := by linarith
  have hpaid : 0 ≤ r * (ig - ce / 4) := mul_nonneg hr hgap
  linarith
