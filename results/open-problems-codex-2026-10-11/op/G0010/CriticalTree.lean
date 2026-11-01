import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- One-step algebraic estimate used in the total-progeny MGF induction.
-- This checks only the displayed polynomial inequality, not the probabilistic theorem.
theorem mgf_increment (r y : ℝ) (hr0 : 0 ≤ r) (hr : r ≤ 1 / 80)
    (hy0 : 0 ≤ y) (hy : y ≤ r / 32) :
    r ^ 2 / 128 + 10 * r ^ 2 * y + 2 * y ^ 2 ≤ r ^ 2 / 64 := by
  have hr2 : 0 ≤ r ^ 2 := sq_nonneg r
  have hyc : y ≤ 1 / 2560 := by linarith
  have hsquare : y ^ 2 ≤ r ^ 2 / 1024 := by
    have hminus : 0 ≤ r / 32 - y := by linarith
    have hplus : 0 ≤ r / 32 + y := by linarith
    nlinarith [mul_nonneg hminus hplus]
  have hprod : r ^ 2 * y ≤ r ^ 2 / 2560 := by
    nlinarith [mul_nonneg hr2 (show 0 ≤ 1 / 2560 - y by linarith)]
  nlinarith

-- The band interval used by the rare-growth lower bound stays inside the next band.
theorem next_band (j z w : ℝ) (hj : 1 ≤ j)
    (hz : z ≤ 4 * j ^ 2) (hw : w ≤ 2 * j) :
    max z ((j + 1) ^ 2) + w ≤ 4 * (j + 1) ^ 2 := by
  have ha : (j + 1) ^ 2 ≤ 4 * j ^ 2 := by nlinarith
  have hm : max z ((j + 1) ^ 2) ≤ 4 * j ^ 2 := max_le hz ha
  nlinarith
