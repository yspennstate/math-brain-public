import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.MeasureTheory.Measure.WithDensity
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Typeclasses.NoAtoms
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
The first assertion of Lemma 5.1 of "Quadratic forms with five large singular values have bounded densities"
(repaired text, sha256 90f859b7): if `Y` has density `f` and `a ≠ 0`, then `T = a(Y - m)² + v` has the density
`p_T(z) = (f(m + r) + f(m - r)) / (2√(|a||z - v|)) · 1{(z - v)/a > 0}`, `r = √(|z - v|/|a|)`, whose value at `v` is `0`;
and `p_T(z) ≤ 1/√(|a||z - v|)` when `f ≤ 1`.

The law of `Y` is `Lebesgue.withDensity f`, so the first statement is the equality of measures `lemma51a`. The set
`{y : T ∈ B}` is split at `y = m` (a Lebesgue-null point); on the half-lines `y > m` and `y < m` the map
`y ↦ a(y - m)² + v` is inverted by `z ↦ m ± √((z - v)/a)` on `{(z - v)/a > 0}`, and the one-dimensional change of
variables (`lintegral_image_eq_lintegral_abs_deriv_mul`) turns each half into an integral over `B ∩ {(z - v)/a > 0}`
with Jacobian `1/(2√(|a||z - v|))` (`abs_deriv_sqrt_div`). The bound is `lemma51a_density_le`; its measure form, the
one used with Lemma 2.4 in the proof of Proposition 7.2, is `lemma51a_le`.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

/-- `z ↦ √((z - v)/a)` has derivative `(1/a) / (2√((z - v)/a))` where `(z - v)/a > 0`. -/
theorem hasDerivAt_sqrt_div (a v z : ℝ) (hz : 0 < (z - v) / a) :
    HasDerivAt (fun z => Real.sqrt ((z - v) / a)) ((1 / a) / (2 * Real.sqrt ((z - v) / a))) z := by
  have h1 : HasDerivAt (fun z : ℝ => (z - v) / a) (1 / a) z :=
    ((hasDerivAt_id z).sub_const v).div_const a
  exact h1.sqrt hz.ne'

/-- The Jacobian: `|(1/a) / (2√((z - v)/a))| = 1/(2√(|a||z - v|))` where `(z - v)/a > 0`. -/
theorem abs_deriv_sqrt_div (a v z : ℝ) (hz : 0 < (z - v) / a) :
    |(1 / a) / (2 * Real.sqrt ((z - v) / a))| = 1 / (2 * Real.sqrt (|a| * |z - v|)) := by
  have ha : a ≠ 0 := by
    rintro rfl
    simp at hz
  have hzv : z - v = a * ((z - v) / a) := by field_simp
  have hsq : Real.sqrt (|a| * |z - v|) = |a| * Real.sqrt ((z - v) / a) := by
    rw [hzv, abs_mul, abs_of_pos hz, ← mul_assoc, ← sq, Real.sqrt_mul (sq_nonneg _),
      Real.sqrt_sq (abs_nonneg a)]
    congr 2
    field_simp
  rw [hsq, abs_div, abs_div, abs_one, abs_mul, abs_two, abs_of_pos (Real.sqrt_pos.2 hz), div_div]
  congr 1
  ring

/-- `(z - v)/a = |z - v|/|a|` where `(z - v)/a > 0`. -/
theorem div_eq_abs_div_abs (a v z : ℝ) (hz : 0 < (z - v) / a) : (z - v) / a = |z - v| / |a| := by
  rw [← abs_div, abs_of_pos hz]

/-- The upper branch `z ↦ m + √((z - v)/a)` is injective on `{(z - v)/a > 0}`. -/
theorem injOn_branch_plus (a m v : ℝ) (ha : a ≠ 0) (S : Set ℝ) (hS : S ⊆ {z | 0 < (z - v) / a}) :
    InjOn (fun z => m + Real.sqrt ((z - v) / a)) S := by
  intro z1 h1 z2 h2 h
  have h1' : 0 < (z1 - v) / a := hS h1
  have h2' : 0 < (z2 - v) / a := hS h2
  have h' : Real.sqrt ((z1 - v) / a) = Real.sqrt ((z2 - v) / a) := by
    simpa using h
  have e := (Real.sqrt_inj h1'.le h2'.le).1 h'
  have e2 := (div_left_inj' ha).1 e
  linarith

/-- The lower branch `z ↦ m - √((z - v)/a)` is injective on `{(z - v)/a > 0}`. -/
theorem injOn_branch_minus (a m v : ℝ) (ha : a ≠ 0) (S : Set ℝ) (hS : S ⊆ {z | 0 < (z - v) / a}) :
    InjOn (fun z => m - Real.sqrt ((z - v) / a)) S := by
  intro z1 h1 z2 h2 h
  have h1' : 0 < (z1 - v) / a := hS h1
  have h2' : 0 < (z2 - v) / a := hS h2
  have h' : Real.sqrt ((z1 - v) / a) = Real.sqrt ((z2 - v) / a) := by
    simpa using h
  have e := (Real.sqrt_inj h1'.le h2'.le).1 h'
  have e2 := (div_left_inj' ha).1 e
  linarith

/-- The upper branch maps `{(z - v)/a > 0} ∩ B` onto `{y > m : a(y - m)² + v ∈ B}`. -/
theorem image_branch_plus (a m v : ℝ) (ha : a ≠ 0) (B : Set ℝ) :
    (fun z => m + Real.sqrt ((z - v) / a)) '' ({z | 0 < (z - v) / a} ∩ B)
      = (fun y => a * (y - m) ^ 2 + v) ⁻¹' B ∩ Ioi m := by
  ext y
  simp only [mem_image, mem_inter_iff, mem_setOf_eq, mem_preimage, mem_Ioi]
  constructor
  · rintro ⟨z, ⟨hz, hzB⟩, rfl⟩
    have hs := Real.sq_sqrt hz.le
    have e1 : a * ((z - v) / a) = z - v := by field_simp
    refine ⟨?_, by linarith [Real.sqrt_pos.2 hz]⟩
    have e : a * (m + Real.sqrt ((z - v) / a) - m) ^ 2 + v = z := by
      rw [add_sub_cancel_left, hs, e1]
      ring
    rwa [e]
  · rintro ⟨hyB, hym⟩
    have e : (a * (y - m) ^ 2 + v - v) / a = (y - m) ^ 2 := by
      rw [div_eq_iff ha]
      ring
    refine ⟨a * (y - m) ^ 2 + v, ⟨?_, hyB⟩, ?_⟩
    · rw [e]
      exact pow_pos (sub_pos.2 hym) 2
    · rw [e, Real.sqrt_sq (sub_nonneg.2 hym.le)]
      ring

/-- The lower branch maps `{(z - v)/a > 0} ∩ B` onto `{y < m : a(y - m)² + v ∈ B}`. -/
theorem image_branch_minus (a m v : ℝ) (ha : a ≠ 0) (B : Set ℝ) :
    (fun z => m - Real.sqrt ((z - v) / a)) '' ({z | 0 < (z - v) / a} ∩ B)
      = (fun y => a * (y - m) ^ 2 + v) ⁻¹' B ∩ Iio m := by
  ext y
  simp only [mem_image, mem_inter_iff, mem_setOf_eq, mem_preimage, mem_Iio]
  constructor
  · rintro ⟨z, ⟨hz, hzB⟩, rfl⟩
    have hs := Real.sq_sqrt hz.le
    have e1 : a * ((z - v) / a) = z - v := by field_simp
    refine ⟨?_, by linarith [Real.sqrt_pos.2 hz]⟩
    have e : a * (m - Real.sqrt ((z - v) / a) - m) ^ 2 + v = z := by
      rw [sub_sub_cancel_left, neg_sq, hs, e1]
      ring
    rwa [e]
  · rintro ⟨hyB, hym⟩
    have e : (a * (y - m) ^ 2 + v - v) / a = (m - y) ^ 2 := by
      rw [div_eq_iff ha]
      ring
    refine ⟨a * (y - m) ^ 2 + v, ⟨?_, hyB⟩, ?_⟩
    · rw [e]
      exact pow_pos (sub_pos.2 hym) 2
    · rw [e, Real.sqrt_sq (sub_nonneg.2 hym.le)]
      ring

/-- **Lemma 5.1, the density formula.** If `Y` has density `f` and `a ≠ 0`, then `T = a(Y - m)² + v` has density
`(f(m + r) + f(m - r)) / (2√(|a||z - v|)) · 1{(z - v)/a > 0}` with `r = √(|z - v|/|a|)`; its value at `z = v` is `0`. -/
theorem lemma51a (f : ℝ → ℝ≥0∞) (hf : Measurable f) (a m v : ℝ) (ha : a ≠ 0) :
    (volume.withDensity f).map (fun y => a * (y - m) ^ 2 + v)
      = volume.withDensity ({z | 0 < (z - v) / a}.indicator (fun z =>
          (f (m + Real.sqrt (|z - v| / |a|)) + f (m - Real.sqrt (|z - v| / |a|)))
            * ENNReal.ofReal (1 / (2 * Real.sqrt (|a| * |z - v|))))) := by
  have hφ : Measurable (fun y : ℝ => a * (y - m) ^ 2 + v) := by fun_prop
  have hPm : MeasurableSet {z : ℝ | 0 < (z - v) / a} := measurableSet_lt measurable_const (by fun_prop)
  ext B hB
  rw [Measure.map_apply hφ hB, withDensity_apply _ (hφ hB), withDensity_apply _ hB,
    setLIntegral_indicator hPm]
  have hS : MeasurableSet ({z : ℝ | 0 < (z - v) / a} ∩ B) := hPm.inter hB
  have hSsub : {z : ℝ | 0 < (z - v) / a} ∩ B ⊆ {z | 0 < (z - v) / a} := inter_subset_left
  -- split the `y`-integral at the null point `m`
  have hsplit : ∫⁻ y in (fun y => a * (y - m) ^ 2 + v) ⁻¹' B, f y
      = (∫⁻ y in (fun y => a * (y - m) ^ 2 + v) ⁻¹' B ∩ Ioi m, f y)
        + ∫⁻ y in (fun y => a * (y - m) ^ 2 + v) ⁻¹' B ∩ Iio m, f y := by
    rw [← lintegral_inter_add_diff f _ (measurableSet_Ioi : MeasurableSet (Ioi m))]
    congr 1
    apply setLIntegral_congr
    have e : (fun y => a * (y - m) ^ 2 + v) ⁻¹' B \ Ioi m = (fun y => a * (y - m) ^ 2 + v) ⁻¹' B ∩ Iic m := by
      ext y
      simp [not_lt]
    rw [e]
    exact (Filter.EventuallyEq.refl _ _).inter Iio_ae_eq_Iic.symm
  -- the two branches
  have hplus : ∫⁻ y in (fun y => a * (y - m) ^ 2 + v) ⁻¹' B ∩ Ioi m, f y
      = ∫⁻ z in {z : ℝ | 0 < (z - v) / a} ∩ B,
          ENNReal.ofReal (1 / (2 * Real.sqrt (|a| * |z - v|))) * f (m + Real.sqrt (|z - v| / |a|)) := by
    rw [← image_branch_plus a m v ha B,
      lintegral_image_eq_lintegral_abs_deriv_mul (f' := fun z => (1 / a) / (2 * Real.sqrt ((z - v) / a))) hS
        (fun z hz => ((hasDerivAt_sqrt_div a v z (hSsub hz)).const_add m).hasDerivWithinAt)
        (injOn_branch_plus a m v ha _ hSsub) f]
    apply setLIntegral_congr_fun hS
    intro z hz
    have hz0 : 0 < (z - v) / a := hSsub hz
    dsimp only
    rw [abs_deriv_sqrt_div a v z hz0, div_eq_abs_div_abs a v z hz0]
  have hminus : ∫⁻ y in (fun y => a * (y - m) ^ 2 + v) ⁻¹' B ∩ Iio m, f y
      = ∫⁻ z in {z : ℝ | 0 < (z - v) / a} ∩ B,
          ENNReal.ofReal (1 / (2 * Real.sqrt (|a| * |z - v|))) * f (m - Real.sqrt (|z - v| / |a|)) := by
    rw [← image_branch_minus a m v ha B,
      lintegral_image_eq_lintegral_abs_deriv_mul (f' := fun z => -((1 / a) / (2 * Real.sqrt ((z - v) / a)))) hS
        (fun z hz => ((hasDerivAt_sqrt_div a v z (hSsub hz)).const_sub m).hasDerivWithinAt)
        (injOn_branch_minus a m v ha _ hSsub) f]
    apply setLIntegral_congr_fun hS
    intro z hz
    have hz0 : 0 < (z - v) / a := hSsub hz
    dsimp only
    rw [abs_neg, abs_deriv_sqrt_div a v z hz0, div_eq_abs_div_abs a v z hz0]
  have hmeas : Measurable (fun z : ℝ =>
      ENNReal.ofReal (1 / (2 * Real.sqrt (|a| * |z - v|))) * f (m + Real.sqrt (|z - v| / |a|))) := by
    fun_prop
  rw [hsplit, hplus, hminus, ← lintegral_add_left hmeas]
  apply lintegral_congr
  intro z
  ring

/-- **Lemma 5.1, the bound.** If `f ≤ 1`, the density of `lemma51a` is at most `1/√(|a||z - v|)`. -/
theorem lemma51a_density_le (f : ℝ → ℝ≥0∞) (hf1 : ∀ y, f y ≤ 1) (a m v z : ℝ) :
    {z | 0 < (z - v) / a}.indicator (fun z =>
        (f (m + Real.sqrt (|z - v| / |a|)) + f (m - Real.sqrt (|z - v| / |a|)))
          * ENNReal.ofReal (1 / (2 * Real.sqrt (|a| * |z - v|)))) z
      ≤ ENNReal.ofReal (1 / Real.sqrt (|a| * |z - v|)) := by
  refine (indicator_le_self' (fun _ _ => zero_le _) z).trans ?_
  have h2 : f (m + Real.sqrt (|z - v| / |a|)) + f (m - Real.sqrt (|z - v| / |a|)) ≤ ENNReal.ofReal 2 := by
    rw [show (2 : ℝ) = 1 + 1 by norm_num, ENNReal.ofReal_add zero_le_one zero_le_one, ENNReal.ofReal_one]
    exact add_le_add (hf1 _) (hf1 _)
  calc (f (m + Real.sqrt (|z - v| / |a|)) + f (m - Real.sqrt (|z - v| / |a|)))
        * ENNReal.ofReal (1 / (2 * Real.sqrt (|a| * |z - v|)))
      ≤ ENNReal.ofReal 2 * ENNReal.ofReal (1 / (2 * Real.sqrt (|a| * |z - v|))) := mul_le_mul_right' h2 _
    _ = ENNReal.ofReal (2 * (1 / (2 * Real.sqrt (|a| * |z - v|)))) := (ENNReal.ofReal_mul zero_le_two).symm
    _ = ENNReal.ofReal (1 / Real.sqrt (|a| * |z - v|)) := by
        congr 1
        rcases eq_or_ne (Real.sqrt (|a| * |z - v|)) 0 with h | h
        · rw [h]
          simp
        · field_simp

/-- **Lemma 5.1, measure form.** If `Y` has density `f ≤ 1` and `a ≠ 0`, the law of `a(Y - m)² + v` is at most
Lebesgue measure with density `1/√(|a||z - v|)`. -/
theorem lemma51a_le (f : ℝ → ℝ≥0∞) (hf : Measurable f) (hf1 : ∀ y, f y ≤ 1) (a m v : ℝ) (ha : a ≠ 0) :
    (volume.withDensity f).map (fun y => a * (y - m) ^ 2 + v)
      ≤ volume.withDensity (fun z => ENNReal.ofReal (1 / Real.sqrt (|a| * |z - v|))) := by
  rw [lemma51a f hf a m v ha]
  exact withDensity_mono (Filter.Eventually.of_forall (fun z => lemma51a_density_le f hf1 a m v z))

end QformFiveB
