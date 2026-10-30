import Mathlib.Tactic

-- Only the algebraic implication in equation (5), not the Fourier theorem.
theorem power_source_ceiling (t d k b c : ℝ) (hd : 0 < d)
    (hl : t * d - k ≤ c) (hc : c ≤ b) : t ≤ (b + k) / d := by
  apply (le_div_iff₀ hd).2
  linarith
