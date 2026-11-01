import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.NonIntegrable
import Mathlib.Tactic

/-!
B14 WIP for Lemma 5.3 of the repaired five-singular-value paper.

Source pin:
  paper.tex @ 4e530247ec0ef4101a6e5ecf621bd35a969c42aa
  blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a

Target: formalize the "extremal indicator" one-sided tail estimate in
paper.tex lines 436--438 without invoking a general bathtub/rearrangement
theorem.

IMPORTANT: this file has not been compiled in this runtime.  It contains
no sorry/admit/new axiom, but it receives no formal-verification credit
until it is built in the pinned Lean 4.29.1 / Mathlib 5e932f97 environment.
-/

open Real Set MeasureTheory intervalIntegral

namespace QformFiveB

/--
Pointwise dual certificate for the positive hyperbola tail.

For m>0, y>m and 0<=a<=1, put lambda=1/(m+1).  On m<y<=m+1,
the excess over a/y is (1-a)(1/y-lambda)>=0.  For y>m+1,
1/y<=lambda.
-/
theorem hyperbola_tail_dual_pointwise
    (m y a : ℝ) (hm : 0 < m) (hy : m < y)
    (ha0 : 0 ≤ a) (ha1 : a ≤ 1) :
    a / y ≤
      (1 / (m + 1)) * a +
        (if y ≤ m + 1 then (1 / y - 1 / (m + 1)) else 0) := by
  have hy0 : 0 < y := lt_trans hm hy
  have hm1 : 0 < m + 1 := by linarith
  by_cases hle : y ≤ m + 1
  · rw [if_pos hle]
    have hrec : 0 ≤ 1 / y - 1 / (m + 1) := by
      exact sub_nonneg.mpr (one_div_le_one_div_of_le hy0 hle)
    have hprod : 0 ≤ (1 - a) * (1 / y - 1 / (m + 1)) :=
      mul_nonneg (sub_nonneg.mpr ha1) hrec
    have hid :
        (1 / (m + 1)) * a + (1 / y - 1 / (m + 1)) - a / y =
          (1 - a) * (1 / y - 1 / (m + 1)) := by
      ring
    linarith
  · rw [if_neg hle, add_zero]
    have hgt : m + 1 < y := lt_of_not_ge hle
    have hrec : 1 / y ≤ 1 / (m + 1) :=
      one_div_le_one_div_of_le hm1 (le_of_lt hgt)
    calc
      a / y = a * (1 / y) := by ring
      _ ≤ a * (1 / (m + 1)) := mul_le_mul_of_nonneg_left hrec ha0
      _ = (1 / (m + 1)) * a := by ring

/--
The only explicit integral needed by the dual-certificate proof.
It replaces a general rearrangement/bathtub theorem.
-/
theorem hyperbola_tail_certificate_integral
    (m : ℝ) (hm : 0 < m) :
    (∫ y in m..m + 1, (1 / y - 1 / (m + 1))) =
      Real.log ((m + 1) / m) - 1 / (m + 1) := by
  have hm1 : 0 < m + 1 := by linarith
  have hmle : m ≤ m + 1 := by linarith
  have hzero : 0 ∉ Set.uIcc m (m + 1) := by
    rw [Set.uIcc_of_le hmle]
    intro h
    linarith [h.1]
  have hinv0 :
      IntervalIntegrable (fun y : ℝ => y⁻¹) MeasureTheory.volume m (m + 1) := by
    exact (intervalIntegrable_inv_iff).2 (Or.inr hzero)
  have hinv :
      IntervalIntegrable (fun y : ℝ => 1 / y) MeasureTheory.volume m (m + 1) := by
    simpa [one_div] using hinv0
  have hconst :
      IntervalIntegrable (fun _ : ℝ => 1 / (m + 1)) MeasureTheory.volume m (m + 1) :=
    continuous_const.intervalIntegrable _ _
  calc
    (∫ y in m..m + 1, (1 / y - 1 / (m + 1))) =
        (∫ y in m..m + 1, 1 / y) -
          (∫ y in m..m + 1, (1 / (m + 1) : ℝ)) := by
            exact intervalIntegral.integral_sub hinv hconst
    _ = Real.log ((m + 1) / m) - 1 / (m + 1) := by
          rw [integral_one_div_of_pos hm hm1, integral_const_on_unit_interval]

/-- The ratio appearing after integration is exactly 1+1/m. -/
theorem hyperbola_tail_ratio (m : ℝ) (hm : 0 < m) :
    (m + 1) / m = 1 + 1 / m := by
  field_simp [hm.ne']
  ring

/-- In the paper's range m>=1, the finite-interval cost is at most log 2. -/
theorem hyperbola_tail_log_le_log_two (m : ℝ) (hm : 1 ≤ m) :
    Real.log ((m + 1) / m) ≤ Real.log 2 := by
  have hm0 : 0 < m := lt_of_lt_of_le zero_lt_one hm
  have hnum : 0 < m + 1 := by linarith
  have hratio0 : 0 < (m + 1) / m := div_pos hnum hm0
  have hratio : (m + 1) / m ≤ 2 := by
    rw [div_le_iff₀ hm0]
    linarith
  exact log_le_log hratio0 hratio

/-!
NEXT FORMAL STEP (not yet claimed):

Integrate hyperbola_tail_dual_pointwise over Set.Ioi m against the
cap-one density f.  The lambda*f term costs at most lambda because the
one-sided mass is at most one.  The conditional term is supported on
Ioc m (m+1) and is exactly hyperbola_tail_certificate_integral.
Therefore

  ∫ y in Set.Ioi m, f y / y
    <= log ((m+1)/m)
    <= log 2   (m>=1).

The negative half-line follows by reflection.  Once this is compiled,
the remaining Lemma 5.3 obligations are the 2D branch
change-of-variables/density theorem and the critical-level null step.
-/

end QformFiveB
