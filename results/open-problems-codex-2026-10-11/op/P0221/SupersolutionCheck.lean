import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- Exact pair identity behind both reciprocal-component supersolutions.
theorem reciprocal_pair_identity (x y : ℝ) (hx : 0 < x) (hy : 0 < y) :
    x*y*(1/x+1/y-1/(x+y))^2 = x/y+y/x+x*y/(x+y)^2 := by
  have hxy : x+y ≠ 0 := ne_of_gt (by linarith)
  field_simp [ne_of_gt hx, ne_of_gt hy, hxy]
  <;> ring

-- Expansion of the corrected supersolution's verification remainder.
theorem corrected_remainder (q k T r w : ℝ) :
    (q-k+T)+2*(k-1-r)+w-(q+k-2) = T-2*r+w := by
  ring

theorem remainder_pair_square (x y n : ℝ)
    (hx : 0 < x) (hy : 0 < y) (hn : 0 < n) :
    x*y/(x+y)^2 - 2*(x*y/(x+y))/n + x*y/n^2 =
    x*y*(1/(x+y)-1/n)^2 := by
  have hxy : x+y ≠ 0 := ne_of_gt (by linarith)
  field_simp [ne_of_gt hn, hxy]
  <;> ring

theorem remainder_pair_nonnegative (x y n : ℝ)
    (hx : 0 < x) (hy : 0 < y) (hn : 0 < n) :
    0 ≤ (2/n^2)*x*y*(1/(x+y)-1/n)^2 := by
  positivity

theorem singleton_rate_identity (y : ℝ) (hy : 0 < y) :
    y*(1+1/y-1/(1+y)) = y+1/(y+1) := by
  have h1 : 1+y ≠ 0 := ne_of_gt (by linarith)
  have h2 : y+1 ≠ 0 := ne_of_gt (by linarith)
  field_simp [ne_of_gt hy,h1,h2]
  <;> ring

example : (2:ℚ)-1/20 = 39/20 := by norm_num
