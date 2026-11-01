import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

-- These are algebraic auxiliaries only, not a formal circular-law theorem.
theorem radius_deficit (s r t : ℝ) (hs : s ≤ 2)
    (hr0 : 0 ≤ r) (hr1 : r ≤ 1)
    (ht : t = s * (1-r) * (1+r)) : t / 4 ≤ 1-r := by
  have hprod : s * (1+r) ≤ 4 := by
    calc
      s * (1+r) ≤ 2 * (1+r) :=
        mul_le_mul_of_nonneg_right hs (by linarith)
      _ ≤ 4 := by linarith
  have h := mul_le_mul_of_nonneg_right hprod (show 0 ≤ 1-r by linarith)
  nlinarith [h]

theorem threshold_boundary (eps : ℝ) (he : eps < 2/3) :
    2*eps < (2+eps)/2 := by linarith

theorem triangle_margin (v err d : ℝ) (hv : 0 ≤ v)
    (herr : err ≤ v/200) (hd : v/32-err ≤ d) : v/64 ≤ d := by
  linarith

theorem radial_margin (v err d : ℝ) (hv : 0 ≤ v)
    (herr : err ≤ v/200) (hd : v/6-err ≤ d) : v/8 ≤ d := by
  linarith

theorem rectangle_margin (r t h : ℝ) (hr0 : 0 < r) (hr1 : r ≤ 1)
    (ht : t/4 ≤ 1-r) (hh : (1/r-1)/8 ≤ h) : t/32 ≤ h := by
  have hrinv : 1-r ≤ 1/r-1 := by
    have hsq : 0 ≤ (1-r)^2 := sq_nonneg (1-r)
    have hmul : r*(1/r) = 1 := mul_div_cancel₀ 1 (ne_of_gt hr0)
    have hpos : 0 ≤ r * ((1/r-1)-(1-r)) := by nlinarith [hmul]
    have : 0 ≤ (1/r-1)-(1-r) := (mul_nonneg_iff_of_pos_left hr0).mp hpos
    linarith
  linarith
