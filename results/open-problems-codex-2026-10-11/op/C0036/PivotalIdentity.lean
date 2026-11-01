import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

-- Algebra only: this does not formalize determinant expansions or the local theorem.
theorem pivotal_identity_scaled (t a0 a1 alpha beta : ℝ)
    (ha : alpha = (1-t)*a0 + t*a1) (hb : beta = a1-a0) :
    alpha - t*beta = a0 := by
  rw [ha, hb]
  ring

theorem pivotal_numerator_nonneg (t a0 a1 alpha beta : ℝ)
    (ha : alpha = (1-t)*a0 + t*a1) (hb : beta = a1-a0)
    (h0 : 0 ≤ a0) : 0 ≤ alpha - t*beta := by
  rw [pivotal_identity_scaled t a0 a1 alpha beta ha hb]
  exact h0

theorem symmetric_pivotal_numerator (t a0 a1 b0 b1 alpha eta beta : ℝ)
    (ha : alpha = (1-t)*a0 + t*a1) (he : eta = (1-t)*b0 + t*b1)
    (hb1 : beta = a1-a0) (hb2 : beta = b1-b0) :
    alpha + eta - 2*t*beta = a0 + b0 := by
  have h1 := pivotal_identity_scaled t a0 a1 alpha beta ha hb1
  have h2 := pivotal_identity_scaled t b0 b1 eta beta he hb2
  nlinarith [h1, h2]
