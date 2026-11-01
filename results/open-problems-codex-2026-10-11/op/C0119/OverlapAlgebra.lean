import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

-- Only the algebraic deductions are formalized, not the Gaussian analysis
-- or the published polymer variance theorems.

theorem normalized_overlap_bound (n b q v : ℝ)
    (hn : 0 < n) (hb : 0 < b) (h : b * q ≤ v) :
    q / n ≤ v / (n * b) := by
  apply (div_le_div_iff₀ hn (mul_pos hn hb)).2
  have hm := mul_le_mul_of_nonneg_left h (le_of_lt hn)
  nlinarith

theorem low_temperature_baseline (n beta c q : ℝ)
    (hn : 0 < n) (hbeta : 0 < beta)
    (h : beta * (n - q) ≤ c * n) :
    1 - c / beta ≤ q / n := by
  apply (le_div_iff₀ hn).2
  have hcancel : beta * (c / beta) = c := by
    field_simp [ne_of_gt hbeta]
  have hmul : beta * ((1 - c / beta) * n) ≤ beta * q := by
    rw [← mul_assoc, mul_sub, mul_one, hcancel, sub_mul]
    nlinarith
  have hnonpos : beta * ((1 - c / beta) * n - q) ≤ 0 := by
    rw [mul_sub]
    exact sub_nonpos.mpr hmul
  by_contra hnot
  have hpos : 0 < beta * ((1 - c / beta) * n - q) :=
    mul_pos hbeta (sub_pos.mpr (lt_of_not_ge hnot))
  exact (not_lt_of_ge hnonpos) hpos

theorem same_environment_probability_floor (c p : ℝ)
    (hc : c < 2) (h : c ≤ c / 2 + (1 - c / 2) * p) :
    c / (2 - c) ≤ p := by
  apply (div_le_iff₀ (by linarith : 0 < 2 - c)).2
  nlinarith
