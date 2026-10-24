import Mathlib.Analysis.Real.Sqrt
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- The exact perspective-action splitting identity.
theorem perspective_split (d1 d2 h1 h2 : ℝ)
    (h1d : 0 < d1) (h2d : 0 < d2) :
    h1 ^ 2 / (2 * d1) + h2 ^ 2 / (2 * d2) -
      (h1 + h2) ^ 2 / (2 * (d1 + d2)) =
    (d2 * h1 - d1 * h2) ^ 2 / (2 * d1 * d2 * (d1 + d2)) := by
  have hn1 : d1 ≠ 0 := ne_of_gt h1d
  have hn2 : d2 ≠ 0 := ne_of_gt h2d
  have hn3 : d1 + d2 ≠ 0 := ne_of_gt (add_pos h1d h2d)
  field_simp
  <;> ring

-- Algebraic cubic consequence of the occupancy lower bound.
theorem swept_cubic (w D M : ℝ) (hw : 0 ≤ w) (hD : 0 ≤ D)
    (hlarge : 8 * D ≤ w)
    (hbound : (w ^ 2 / 16) * (w / 2 - 2 * D) ≤ M) :
    w ^ 3 ≤ 64 * M := by
  have hfactor : 0 ≤ w / 4 - 2 * D := by linarith
  have hp : 0 ≤ w ^ 2 * (w / 4 - 2 * D) :=
    mul_nonneg (sq_nonneg w) hfactor
  nlinarith

theorem root_upper_0 : Real.sqrt (11022273 / 3125000 : ℝ) < 1878064792 / 1000000000 := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ 11022273 / 3125000 by norm_num)
  have hn := Real.sqrt_nonneg (11022273 / 3125000 : ℝ)
  nlinarith

theorem root_upper_1 : Real.sqrt (1794829 / 800000 : ℝ) < 1497843868 / 1000000000 := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ 1794829 / 800000 by norm_num)
  have hn := Real.sqrt_nonneg (1794829 / 800000 : ℝ)
  nlinarith

theorem root_lower_2 : 1574493331 / 1000000000 < Real.sqrt (9916117 / 4000000 : ℝ) := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ 9916117 / 4000000 by norm_num)
  have hn := Real.sqrt_nonneg (9916117 / 4000000 : ℝ)
  nlinarith

theorem root_lower_3 : 1801502667 / 1000000000 < Real.sqrt (162270593 / 50000000 : ℝ) := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ 162270593 / 50000000 by norm_num)
  have hn := Real.sqrt_nonneg (162270593 / 50000000 : ℝ)
  nlinarith

theorem different_euclidean_choice :
    Real.sqrt (11022273/3125000 : ℝ) + Real.sqrt (1794829/800000 : ℝ) <
    Real.sqrt (9916117/4000000 : ℝ) + Real.sqrt (162270593/50000000 : ℝ) := by
  have h0 := root_upper_0
  have h1 := root_upper_1
  have h2 := root_lower_2
  have h3 := root_lower_3
  linarith

theorem different_quadratic_choice :
    ((611/1000 : ℝ) - (67/500)) ^ 2 / (2 * ((4719/2000) - (859/1000))) + ((187/1250 : ℝ) - (293/2000)) ^ 2 / (2 * ((2737/1000) - (1871/2000))) < ((187/1250 : ℝ) - (67/500)) ^ 2 / (2 * ((2737/1000) - (859/1000))) + ((611/1000 : ℝ) - (293/2000)) ^ 2 / (2 * ((4719/2000) - (1871/2000))) := by
  norm_num

#print axioms perspective_split
#print axioms swept_cubic
#print axioms different_euclidean_choice
#print axioms different_quadratic_choice
