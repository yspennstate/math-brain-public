import Mathlib.Tactic.Linarith

-- Conditional-probability comparisons for the tree countermodel.
theorem thinning_probability_bound (p q delta : ℝ)
    (hp : p ≤ 1) (hd : 0 ≤ delta) (hgap : q + delta ≤ p) :
    q ≤ p * (1 - delta) := by
  have hprod : 0 ≤ delta * (1 - p) := mul_nonneg hd (sub_nonneg.mpr hp)
  nlinarith

theorem enhancement_probability_bound (p q delta : ℝ)
    (hq : 0 ≤ q) (hd : 0 ≤ delta) (hgap : q + delta ≤ p) :
    q + delta * (1 - q) ≤ p := by
  have hprod : 0 ≤ delta * q := mul_nonneg hd hq
  nlinarith
