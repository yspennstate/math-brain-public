import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

-- For the cubic case use epsilon=r^5, coefficient cutoff r^2,
-- and W cutoff 1/r^2. This checks the real algebra only.
theorem coefficient_cutoff_cubic (r W d s : ℝ)
    (hW : 0 < W) (hcut : W * r^2 ≤ 1)
    (hd : r^2 ≤ d) (hs : d ≤ s * W) : r^4 ≤ s := by
  have hsmall : r^4 * W ≤ r^2 := by
    calc
      r^4 * W = r^2 * (W * r^2) := by ring
      _ ≤ r^2 * 1 := mul_le_mul_of_nonneg_left hcut (sq_nonneg r)
      _ = r^2 := by ring
  have hchain : r^4 * W ≤ s * W := le_trans hsmall (le_trans hd hs)
  exact (mul_le_mul_iff_left₀ hW).mp (by simpa only [mul_comm] using hchain)

theorem cubic_gaussian_exponent (r : ℝ) :
    (r^5)^2 = r^2 * (r^4)^2 := by ring

#print axioms coefficient_cutoff_cubic
#print axioms cubic_gaussian_exponent
