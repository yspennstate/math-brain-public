import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

theorem thinning_integrand (b t z : ℝ) :
    -b - (1-b*t)*b*(z-1) = -b*((1-b*t)*z+b*t) := by ring

theorem crossing_partition_bound (n k : ℝ) (hk : 1 ≤ k) (hn : k ≤ n) :
    n*(k-1) ≤ (k-1)*(2*n-k) := by
  have h := mul_nonneg (sub_nonneg.mpr hk) (sub_nonneg.mpr hn)
  nlinarith

theorem repair_scaled_drift (B m z r : ℝ)
    (hB : 4 ≤ B) (hm : 1 ≤ m) (hz : 0 ≤ z) (hr : z ≤ r) :
    2*z*(m-1) - B*m*r/2 ≤ 0 := by
  have hm0 : 0 ≤ m := by linarith
  have hB0 : 0 ≤ B := by linarith
  have h1 : 4*m ≤ B*m := mul_le_mul_of_nonneg_right hB hm0
  have h2 : 4*m*z ≤ B*m*z := mul_le_mul_of_nonneg_right h1 hz
  have h3 : B*m*z ≤ B*m*r :=
    mul_le_mul_of_nonneg_left hr (mul_nonneg hB0 hm0)
  nlinarith
