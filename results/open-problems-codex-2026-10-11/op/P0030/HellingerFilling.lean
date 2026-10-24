import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Key finite induction step in the one-way Kakutani proof.
theorem product_deficiency_step (a b : ℝ) (ha : a ≤ 1) (hb : b ≤ 1) :
    1 - a * b ≤ (1 - a) + (1 - b) := by
  nlinarith [mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hb)]

-- Finite source-mass conservation, used orbitwise in the filling proof.
theorem filling_source_step (source accepted : ℝ)
    (hacc : 0 ≤ accepted) (hbound : accepted ≤ source) :
    0 ≤ source - accepted ∧ source - accepted ≤ source := by
  constructor <;> linarith

-- If two residual masses start equal and consume equal accepted mass,
-- their masses remain equal. This is the finite conservation induction.
theorem filling_equal_mass (source target accepted : ℝ)
    (heq : source = target) :
    source - accepted = target - accepted := by
  linarith
