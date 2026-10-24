import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic

-- The exponent identity behind arbitrarily small mixed Hessian entries.
theorem coefficient_exponents (a b : ℕ) :
    2 * ((a + 1)^2 + (b + 1)^2) + 4 =
      (a + 2)^2 + a^2 + (b + 2)^2 + b^2 := by
  ring

-- Exact two-species dual-cone reaction estimate.
theorem triangular_reaction_bound
    (a p₁ p₂ f₁ f₂ c s : ℝ)
    (hp₂ : 0 ≤ p₂) (horder : a * p₂ ≤ p₁)
    (hf₁ : f₁ ≤ c * s) (hf₂ : a * f₁ + f₂ ≤ c * s) :
    p₁ * f₁ + p₂ * f₂ ≤ (p₁ - a * p₂ + p₂) * (c * s) := by
  have h₁ := mul_le_mul_of_nonneg_left hf₁ (sub_nonneg.mpr horder)
  have h₂ := mul_le_mul_of_nonneg_left hf₂ hp₂
  nlinarith

-- Absorption of one mixed term into the diagonal gradient energy.
theorem mixed_absorption (x y : ℝ) : 2 * x * y ≤ x^2 + y^2 := by
  nlinarith [sq_nonneg (x - y)]
