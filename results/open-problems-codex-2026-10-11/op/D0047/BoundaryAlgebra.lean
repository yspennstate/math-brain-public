import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- Each differentiated entrance equation determines just one new jet.
theorem triangular_jet_step (A v d lower : ℝ) (hA : A ≠ 0) :
    A * (v - d) + lower = 0 ↔ v = d - lower / A := by
  field_simp [hA]
  constructor <;> intro h <;> nlinarith

-- sigma(r)=-a*r satisfies the bulk sigma-PV polynomial expression.
theorem linear_sigma_branch (a r : ℝ) :
    (r * (0 : ℝ)) ^ 2 +
      4 * (r * (-a) - (-a * r)) *
        (r * (-a) - (-a * r) + (-a) ^ 2) = 0 := by
  ring
