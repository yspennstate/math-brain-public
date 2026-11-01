import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- The scalar step in the Rayleigh quotient comparison, for every test function.
theorem transfer_poincare
    (c gamma vp vq ep eq : ℝ)
    (hc : 0 ≤ c) (hg : 0 ≤ gamma)
    (hv : vp ≤ c * vq) (henergy : ep = c * eq)
    (hq : gamma * vq ≤ eq) : gamma * vp ≤ ep := by
  have h1 := mul_le_mul_of_nonneg_left hv hg
  have h2 := mul_le_mul_of_nonneg_left hq hc
  nlinarith

-- The exact two-flow discrepancy on the edge 001--011 in Q_3 minus 000.
theorem uniform_flow_discrepancy :
    (1 : ℚ) / 7 * (1 / (2 * 2)) ≠ 1 / 7 * (1 / (2 * 3)) := by
  norm_num

-- Degree-weighted detailed balance for that edge (total degree is 18).
theorem degree_weighted_flow :
    (2 : ℚ) / 18 * (1 / (2 * 2)) = 3 / 18 * (1 / (2 * 3)) := by
  norm_num

-- In the attached-subcube family, the branch has stationary mass at most 1/3.
-- Here h >= 2 represents 2^r, n-1 = k+r, and r >= 1.
theorem branch_mass_denominator
    (k r h : ℝ) (hk : 0 ≤ k) (hr : 1 ≤ r) (hh : 2 ≤ h) :
    3 * (k + 1) ≤ (k + r) * h + k + 2 := by
  have hprod := mul_nonneg (sub_nonneg.mpr hh) (show 0 ≤ k + r by linarith)
  nlinarith
