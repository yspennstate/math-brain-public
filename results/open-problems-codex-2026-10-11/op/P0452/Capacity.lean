import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Finite deterministic capacity estimate in SECOND_ATTEMPT.md Section 4.
theorem retained_capacity_product (a n delta u v : Real)
    (ha : 0 ≤ a) (hn : 0 ≤ n) (hd : 4 * delta ≤ a)
    (hu : a * n - 2 * delta * n ≤ u)
    (hv : a * n - 2 * delta * n ≤ v) :
    (a * n)^2 / 4 ≤ u * v := by
  have hbase : 0 ≤ a * n / 2 := by
    have hmul := mul_nonneg ha hn
    nlinarith
  have hscaled : 0 ≤ (a - 4 * delta) * n := by
    apply mul_nonneg
    nlinarith
    exact hn
  have hleft : a * n / 2 ≤ u := by nlinarith
  have hright : a * n / 2 ≤ v := by nlinarith
  have hu0 : 0 ≤ u := le_trans hbase hleft
  have hp := mul_le_mul hleft hright hbase hu0
  nlinarith [hp]
