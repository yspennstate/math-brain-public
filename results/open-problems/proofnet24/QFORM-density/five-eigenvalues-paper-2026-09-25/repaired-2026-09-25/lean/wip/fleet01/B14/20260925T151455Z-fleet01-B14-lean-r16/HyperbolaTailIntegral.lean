import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.NonIntegrable
import Mathlib.MeasureTheory.Integral.SetToL1
import Mathlib.Tactic

/-!
B14 WIP for Lemma 5.3 of the repaired five-singular-value paper.

Source pin:
  paper.tex @ 4e530247ec0ef4101a6e5ecf621bd35a969c42aa
  blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a

This file advances the still-unformalized "extremal indicator" estimate in
paper.tex lines 443--445. It replaces a general bathtub/rearrangement theorem
by an explicit dual certificate.

IMPORTANT FORMAL-CREDIT STATUS:
  This runtime has no Lean/lake/elan executable and the owner forbids installing
  a new toolchain or launching a remote workflow. Therefore this file is
  UNCOMPILED WIP and receives NO Lean-verification credit until it is built in
  the pinned Lean 4.29.1 / Mathlib 5e932f97 environment with no sorry/admit/new
  axiom and an accepted #print axioms log.

The only intentionally exposed routine side hypothesis in the integrated
theorem is IntegrableOn of the compactly-supported certificate term. A
follow-up compile pass should discharge it from the same finite-interval
calculus used in hyperbola_tail_certificate_setIntegral_R16.
-/

open Real Set MeasureTheory intervalIntegral

namespace QformFiveB

/-- Compactly-supported correction in the dual certificate. -/
def hyperbolaTailExtraR16 (m y : ℝ) : ℝ :=
  if y ≤ m + 1 then (1 / y - 1 / (m + 1)) else 0

/--
Pointwise dual certificate. For m>0, y>m and 0<=a<=1,

  a/y <= lambda*a + 1_{m<y<=m+1}(1/y-lambda),

with lambda=1/(m+1).
-/
theorem hyperbola_tail_dual_pointwise_R16
    (m y a : ℝ) (hm : 0 < m) (hy : m < y)
    (ha0 : 0 ≤ a) (ha1 : a ≤ 1) :
    a / y ≤ (1 / (m + 1)) * a + hyperbolaTailExtraR16 m y := by
  have hy0 : 0 < y := lt_trans hm hy
  have hm1 : 0 < m + 1 := by linarith
  by_cases hle : y ≤ m + 1
  · simp only [hyperbolaTailExtraR16, if_pos hle]
    have hrec : 0 ≤ 1 / y - 1 / (m + 1) := by
      exact sub_nonneg.mpr (one_div_le_one_div_of_le hy0 hle)
    have hprod : 0 ≤ (1 - a) * (1 / y - 1 / (m + 1)) :=
      mul_nonneg (sub_nonneg.mpr ha1) hrec
    have hid :
        (1 / (m + 1)) * a + (1 / y - 1 / (m + 1)) - a / y =
          (1 - a) * (1 / y - 1 / (m + 1)) := by
      ring
    linarith
  · simp only [hyperbolaTailExtraR16, if_neg hle, add_zero]
    have hgt : m + 1 < y := lt_of_not_ge hle
    have hrec : 1 / y ≤ 1 / (m + 1) :=
      one_div_le_one_div_of_le hm1 (le_of_lt hgt)
    calc
      a / y = a * (1 / y) := by ring
      _ ≤ a * (1 / (m + 1)) := mul_le_mul_of_nonneg_left hrec ha0
      _ = (1 / (m + 1)) * a := by ring

/-- The finite interval integral appearing in the dual certificate. -/
theorem hyperbola_tail_certificate_interval_R16
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

/--
Set-integral form of the compact certificate. This is the exact object needed
when integrating over the positive half-line.
-/
theorem hyperbola_tail_certificate_setIntegral_R16
    (m : ℝ) (hm : 0 < m) :
    (∫ y in Set.Ioi m, hyperbolaTailExtraR16 m y) =
      Real.log ((m + 1) / m) - 1 / (m + 1) := by
  have hmle : m ≤ m + 1 := by linarith
  let g : ℝ → ℝ := fun y => 1 / y - 1 / (m + 1)
  have hcongr : ∀ y ∈ Set.Ioi m,
      hyperbolaTailExtraR16 m y = (Set.Ioc m (m + 1)).indicator g y := by
    intro y hy
    by_cases hle : y ≤ m + 1
    · have hmem : y ∈ Set.Ioc m (m + 1) := ⟨hy, hle⟩
      simp [hyperbolaTailExtraR16, g, hle, hmem]
    · have hnot : y ∉ Set.Ioc m (m + 1) := by
        intro h
        exact hle h.2
      simp [hyperbolaTailExtraR16, g, hle, hnot]
  rw [setIntegral_congr_fun measurableSet_Ioi hcongr,
      setIntegral_indicator measurableSet_Ioc]
  have hinter : Set.Ioi m ∩ Set.Ioc m (m + 1) = Set.Ioc m (m + 1) := by
    ext y
    simp only [Set.mem_inter_iff, Set.mem_Ioi, Set.mem_Ioc]
    constructor
    · intro h
      exact h.2
    · intro h
      exact ⟨h.1, h⟩
  rw [hinter, ← intervalIntegral.integral_of_le hmle]
  simpa [g] using hyperbola_tail_certificate_interval_R16 m hm

/--
Integrated one-sided cap-one tail estimate, modulo only the routine
IntegrableOn certificate side condition.

This is precisely the analytic inequality used in Lemma 5.3 after the
monotone original-coordinate substitution. The assumptions match that use:
f is nonnegative, f<=1, its one-sided mass is <=1, and all integrals are on
the original physical coordinate.
-/
theorem hyperbola_tail_integral_le_R16
    (f : ℝ → ℝ) (m : ℝ) (hm : 0 < m)
    (hf0 : ∀ y ∈ Set.Ioi m, 0 ≤ f y)
    (hf1 : ∀ y ∈ Set.Ioi m, f y ≤ 1)
    (hf : IntegrableOn f (Set.Ioi m))
    (hquot : IntegrableOn (fun y => f y / y) (Set.Ioi m))
    (hextra : IntegrableOn (hyperbolaTailExtraR16 m) (Set.Ioi m))
    (hmass : (∫ y in Set.Ioi m, f y) ≤ 1) :
    (∫ y in Set.Ioi m, f y / y) ≤ Real.log ((m + 1) / m) := by
  have hlam : 0 ≤ (1 / (m + 1) : ℝ) := by positivity
  have hmajor :
      IntegrableOn
        (fun y => (1 / (m + 1)) * f y + hyperbolaTailExtraR16 m y)
        (Set.Ioi m) :=
    (hf.const_mul (1 / (m + 1))).add hextra
  have hpoint : ∀ y ∈ Set.Ioi m,
      f y / y ≤ (1 / (m + 1)) * f y + hyperbolaTailExtraR16 m y := by
    intro y hy
    exact hyperbola_tail_dual_pointwise_R16 m y (f y) hm hy (hf0 y hy) (hf1 y hy)
  have hmono :
      (∫ y in Set.Ioi m, f y / y) ≤
        ∫ y in Set.Ioi m, ((1 / (m + 1)) * f y + hyperbolaTailExtraR16 m y) :=
    setIntegral_mono_on hquot hmajor measurableSet_Ioi hpoint
  have heval :
      (∫ y in Set.Ioi m,
          ((1 / (m + 1)) * f y + hyperbolaTailExtraR16 m y)) =
        (1 / (m + 1)) * (∫ y in Set.Ioi m, f y) +
          (Real.log ((m + 1) / m) - 1 / (m + 1)) := by
    rw [integral_add (hf.const_mul (1 / (m + 1))) hextra,
        integral_const_mul,
        hyperbola_tail_certificate_setIntegral_R16 m hm]
  calc
    (∫ y in Set.Ioi m, f y / y)
        ≤ (1 / (m + 1)) * (∫ y in Set.Ioi m, f y) +
            (Real.log ((m + 1) / m) - 1 / (m + 1)) := by
          rw [← heval]
          exact hmono
    _ ≤ (1 / (m + 1)) * 1 +
          (Real.log ((m + 1) / m) - 1 / (m + 1)) := by
          exact add_le_add_right (mul_le_mul_of_nonneg_left hmass hlam) _
    _ = Real.log ((m + 1) / m) := by ring

/-- In the paper's range m>=1, the positive-tail cost is at most log 2. -/
theorem hyperbola_tail_log_le_log_two_R16 (m : ℝ) (hm : 1 ≤ m) :
    Real.log ((m + 1) / m) ≤ Real.log 2 := by
  have hm0 : 0 < m := lt_of_lt_of_le zero_lt_one hm
  have hnum : 0 < m + 1 := by linarith
  have hratio0 : 0 < (m + 1) / m := div_pos hnum hm0
  have hratio : (m + 1) / m ≤ 2 := by
    rw [div_le_iff₀ hm0]
    linarith
  exact log_le_log hratio0 hratio

/-!
NEXT FORMAL STEPS, in order:

1. Compile this file in Lean 4.29.1 / Mathlib 5e932f97 and repair API drift.
2. Discharge the hextra side condition directly from compact support in Ioc m (m+1).
3. Derive hquot from IntegrableOn f on Ioi m and m>0, using abs(f(y)/y) <= abs(f(y))/m.
4. Add the reflected negative-tail theorem.
5. Formalize the two-dimensional hyperbola branch change of variables / density
   pushforward, reusing the already-compiled hyperbola_jacobian.
6. Formalize the critical-level null/no-atom step and assemble exact Lemma 5.3.

Do not mark Lemma 5.3 verified until all six steps compile and the final theorem
matches paper.tex lines 423--449.
-/

end QformFiveB
