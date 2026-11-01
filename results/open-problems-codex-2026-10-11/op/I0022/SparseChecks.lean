import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- The cubic energy contributed by a non-maximal supported degree.
theorem lower_degree_cube (d k : ℝ) (hd : 0 ≤ d) (hk : 0 ≤ k)
    (hgap : 3*d ≤ k) : d^3 ≤ k^2*d/9 := by
  have hp : 0 ≤ (k - 3*d) * (k + 3*d) * d :=
    mul_nonneg (mul_nonneg (by linarith) (by linarith)) hd
  nlinarith

-- Keeping the full degree budget gives an 8/9 gap per missing maximum hub.
theorem energy_gap (t q h e : ℝ) (ht : 0 ≤ t) (hh : h ≤ q - 1)
    (he : e ≤ h*t + (q-h)*t/9) : e ≤ q*t - 8*t/9 := by
  have hp : 0 ≤ (q-h-1)*t := mul_nonneg (by linarith) ht
  nlinarith

-- Ordered triples of distinct leaves using both hub groups.
theorem mixed_triple_count (A B : ℝ) :
    (A+B)*(A+B-1)*(A+B-2) - A*(A-1)*(A-2) - B*(B-1)*(B-2)
      = 3*A*B*(A+B-2) := by
  ring

theorem scaling_cannot_match (a r : ℝ) (h2 : 2*a = r) (h3 : 3*a = r) :
    r = 0 := by
  linarith
