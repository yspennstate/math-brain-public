import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Algebra only: the analytic and probabilistic claims are proved in ATTEMPT.md.
theorem favorable_direction (a b e₁ e₂ K : ℝ)
    (h₁ : e₁ ≤ K) (h₂ : e₂ ≤ K) :
    min (a - b + e₁) (b - a + e₂) ≤ K := by
  by_cases h : a ≤ b
  · exact le_trans (min_le_left _ _) (by linarith)
  · exact le_trans (min_le_right _ _) (by linarith)

theorem hessian_tail_threshold (d s : ℝ) :
    d - s - 3 < -1 ↔ d - 2 < s := by
  constructor <;> intro h <;> linarith

theorem riesz_laplacian_positive (d s : ℝ)
    (hs : 0 < s) (hband : d - 2 < s) :
    0 < s * (s + 2 - d) := by
  exact mul_pos hs (by linarith)
