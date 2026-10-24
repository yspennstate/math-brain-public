import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- Algebraic generator bound only; Ito and the Markov argument are in prose.
theorem fractional_generator_bound (b p x y z : ℝ)
    (hb : 0 ≤ b) (hp : 0 ≤ p)
    (hx : x ≤ 1) (hy : -1 ≤ y) (hz : -1 ≤ z) :
    p * ((p - 1) + p * x - b / 2 * (y + z)) ≤
      -p * (1 - b - 2 * p) := by
  have hpx : p * x ≤ p := by
    simpa using mul_le_mul_of_nonneg_left hx hp
  have hyz : 0 ≤ y + z + 2 := by linarith
  have hprod : 0 ≤ b * (y + z + 2) := mul_nonneg hb hyz
  have hterm : -(b / 2) * (y + z) ≤ b := by nlinarith
  have hinner : (p - 1) + p * x - b / 2 * (y + z) ≤
      2 * p - 1 + b := by linarith
  calc
    p * ((p - 1) + p * x - b / 2 * (y + z)) ≤
        p * (2 * p - 1 + b) := mul_le_mul_of_nonneg_left hinner hp
    _ = -p * (1 - b - 2 * p) := by ring
