import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic

theorem signed_disagreement (n z : ℝ)
    (hn : -1 ≤ n) (hn' : n ≤ 1) (hz : -1 ≤ z) (hz' : z ≤ 1) :
    |n-z| ≤ 1-n*z := by
  apply abs_le.mpr
  constructor
  · have h := mul_nonneg (by linarith : 0 ≤ 1+n) (by linarith : 0 ≤ 1-z)
    nlinarith
  · have h := mul_nonneg (by linarith : 0 ≤ 1-n) (by linarith : 0 ≤ 1+z)
    nlinarith
