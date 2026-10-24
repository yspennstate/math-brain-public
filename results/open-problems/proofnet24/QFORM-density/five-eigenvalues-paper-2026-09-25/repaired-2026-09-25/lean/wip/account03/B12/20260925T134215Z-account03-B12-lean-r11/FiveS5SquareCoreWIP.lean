import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.MeasureTheory.Measure.WithDensity

/- account03/B12 WIP for repaired Lemma 5.1.
   UNCOMPILED in this runtime: Lean/lake are not exposed, and installation/remote workflows are forbidden.
   Do not count this file as verified coverage until an actual Lean 4.29.1 / Mathlib 5e932f97 compile. -/

open Real Set MeasureTheory
open scoped ENNReal

namespace QformFiveB

def squareMapB12 (a m v y : ℝ) : ℝ := a * (y - m) ^ 2 + v
def squareSupportB12 (a v : ℝ) : Set ℝ := {z | 0 < (z - v) / a}

noncomputable def squareRightInvB12 (a m v z : ℝ) : ℝ :=
  m + Real.sqrt ((z - v) / a)

noncomputable def squareLeftInvB12 (a m v z : ℝ) : ℝ :=
  m - Real.sqrt ((z - v) / a)

noncomputable def squareInvJacB12 (a v z : ℝ) : ℝ≥0∞ :=
  ENNReal.ofReal |(1 / (2 * Real.sqrt ((z - v) / a))) * (1 / a)|

theorem squareMapB12_measurable (a m v : ℝ) :
    Measurable (squareMapB12 a m v) := by
  unfold squareMapB12
  fun_prop

theorem squareMapB12_preimage_critical (a m v : ℝ) (ha : a ≠ 0) :
    squareMapB12 a m v ⁻¹' ({v} : Set ℝ) = {m} := by
  ext y
  simp only [Set.mem_preimage, Set.mem_singleton_iff]
  constructor
  · intro h
    have hmul : a * (y - m) ^ 2 = 0 := by
      unfold squareMapB12 at h
      linarith
    rcases mul_eq_zero.mp hmul with hzero | hsq
    · exact (ha hzero).elim
    · nlinarith
  · intro h
    subst y
    simp [squareMapB12]

theorem square_source_critical_null_B12 (f : ℝ → ℝ≥0∞) (m : ℝ) :
    (volume.withDensity f) ({m} : Set ℝ) = 0 := by
  exact measure_singleton m

theorem square_pushforward_critical_null_B12
    (f : ℝ → ℝ≥0∞) (a m v : ℝ) (ha : a ≠ 0) :
    ((volume.withDensity f).map (squareMapB12 a m v)) ({v} : Set ℝ) = 0 := by
  rw [Measure.map_apply (squareMapB12_measurable a m v) measurableSet_singleton,
    squareMapB12_preimage_critical a m v ha]
  exact measure_singleton m

theorem hasDerivAt_squareRightInv_B12
    (a m v z : ℝ) (hz : z ∈ squareSupportB12 a v) :
    HasDerivAt (squareRightInvB12 a m v)
      ((1 / (2 * Real.sqrt ((z - v) / a))) * (1 / a)) z := by
  have hpos : 0 < (z - v) / a := by simpa [squareSupportB12] using hz
  have hinner : HasDerivAt (fun x : ℝ => (x - v) / a) (1 / a) z :=
    ((hasDerivAt_id z).sub_const v).div_const a
  have hsqrt := (Real.hasDerivAt_sqrt hpos.ne').comp z hinner
  simpa [squareRightInvB12, add_comm] using hsqrt.const_add m

theorem hasDerivAt_squareLeftInv_B12
    (a m v z : ℝ) (hz : z ∈ squareSupportB12 a v) :
    HasDerivAt (squareLeftInvB12 a m v)
      (-((1 / (2 * Real.sqrt ((z - v) / a))) * (1 / a))) z := by
  have hpos : 0 < (z - v) / a := by simpa [squareSupportB12] using hz
  have hinner : HasDerivAt (fun x : ℝ => (x - v) / a) (1 / a) z :=
    ((hasDerivAt_id z).sub_const v).div_const a
  have hsqrt := (Real.hasDerivAt_sqrt hpos.ne').comp z hinner
  simpa [squareLeftInvB12, sub_eq_add_neg, add_comm] using hsqrt.neg.const_add m


theorem squareMapB12_rightInv
    (a m v z : ℝ) (ha : a ≠ 0) (hz : z ∈ squareSupportB12 a v) :
    squareMapB12 a m v (squareRightInvB12 a m v z) = z := by
  have hpos : 0 < (z - v) / a := by simpa [squareSupportB12] using hz
  have hsqrt : (Real.sqrt ((z - v) / a)) ^ 2 = (z - v) / a :=
    Real.sq_sqrt hpos.le
  unfold squareMapB12 squareRightInvB12
  rw [show m + Real.sqrt ((z - v) / a) - m =
      Real.sqrt ((z - v) / a) by ring, hsqrt]
  field_simp [ha]
  <;> ring

theorem squareMapB12_leftInv
    (a m v z : ℝ) (ha : a ≠ 0) (hz : z ∈ squareSupportB12 a v) :
    squareMapB12 a m v (squareLeftInvB12 a m v z) = z := by
  have hpos : 0 < (z - v) / a := by simpa [squareSupportB12] using hz
  have hsqrt : (Real.sqrt ((z - v) / a)) ^ 2 = (z - v) / a :=
    Real.sq_sqrt hpos.le
  unfold squareMapB12 squareLeftInvB12
  rw [show m - Real.sqrt ((z - v) / a) - m =
      -Real.sqrt ((z - v) / a) by ring, sq_neg, hsqrt]
  field_simp [ha]
  <;> ring

theorem squareRightInvB12_squareMap
    (a m v y : ℝ) (ha : a ≠ 0) (hy : m < y) :
    squareRightInvB12 a m v (squareMapB12 a m v y) = y := by
  have hdiv : (squareMapB12 a m v y - v) / a = (y - m) ^ 2 := by
    unfold squareMapB12
    field_simp [ha]
    <;> ring
  unfold squareRightInvB12
  rw [hdiv, Real.sqrt_sq (sub_nonneg.mpr hy.le)]
  ring

theorem squareLeftInvB12_squareMap
    (a m v y : ℝ) (ha : a ≠ 0) (hy : y < m) :
    squareLeftInvB12 a m v (squareMapB12 a m v y) = y := by
  have hdiv : (squareMapB12 a m v y - v) / a = (y - m) ^ 2 := by
    unfold squareMapB12
    field_simp [ha]
    <;> ring
  unfold squareLeftInvB12
  rw [hdiv, show (y - m) ^ 2 = (m - y) ^ 2 by ring,
    Real.sqrt_sq (sub_nonneg.mpr hy.le)]
  ring

theorem squareRightInvB12_injOn
    (a m v : ℝ) (ha : a ≠ 0) :
    Set.InjOn (squareRightInvB12 a m v) (squareSupportB12 a v) := by
  intro z₁ hz₁ z₂ hz₂ h
  calc
    z₁ = squareMapB12 a m v (squareRightInvB12 a m v z₁) :=
      (squareMapB12_rightInv a m v z₁ ha hz₁).symm
    _ = squareMapB12 a m v (squareRightInvB12 a m v z₂) := by rw [h]
    _ = z₂ := squareMapB12_rightInv a m v z₂ ha hz₂

theorem squareLeftInvB12_injOn
    (a m v : ℝ) (ha : a ≠ 0) :
    Set.InjOn (squareLeftInvB12 a m v) (squareSupportB12 a v) := by
  intro z₁ hz₁ z₂ hz₂ h
  calc
    z₁ = squareMapB12 a m v (squareLeftInvB12 a m v z₁) :=
      (squareMapB12_leftInv a m v z₁ ha hz₁).symm
    _ = squareMapB12 a m v (squareLeftInvB12 a m v z₂) := by rw [h]
    _ = z₂ := squareMapB12_leftInv a m v z₂ ha hz₂

theorem squareRightInvB12_image
    (a m v : ℝ) (ha : a ≠ 0) (t : Set ℝ) :
    squareRightInvB12 a m v '' (t ∩ squareSupportB12 a v) =
      (squareMapB12 a m v ⁻¹' t) ∩ Set.Ioi m := by
  ext y
  constructor
  · rintro ⟨z, ⟨hzt, hzs⟩, rfl⟩
    constructor
    · change squareMapB12 a m v (squareRightInvB12 a m v z) ∈ t
      rw [squareMapB12_rightInv a m v z ha hzs]
      exact hzt
    · have hpos : 0 < (z - v) / a := by simpa [squareSupportB12] using hzs
      have hsqrt : 0 < Real.sqrt ((z - v) / a) := Real.sqrt_pos.2 hpos
      unfold squareRightInvB12
      linarith
  · rintro ⟨hyt, hym⟩
    refine ⟨squareMapB12 a m v y, ⟨hyt, ?_⟩, ?_⟩
    · have hdiv : (squareMapB12 a m v y - v) / a = (y - m) ^ 2 := by
        unfold squareMapB12
        field_simp [ha]
        <;> ring
      simp only [squareSupportB12, Set.mem_setOf_eq]
      rw [hdiv]
      nlinarith
    · exact squareRightInvB12_squareMap a m v y ha hym

theorem squareLeftInvB12_image
    (a m v : ℝ) (ha : a ≠ 0) (t : Set ℝ) :
    squareLeftInvB12 a m v '' (t ∩ squareSupportB12 a v) =
      (squareMapB12 a m v ⁻¹' t) ∩ Set.Iio m := by
  ext y
  constructor
  · rintro ⟨z, ⟨hzt, hzs⟩, rfl⟩
    constructor
    · change squareMapB12 a m v (squareLeftInvB12 a m v z) ∈ t
      rw [squareMapB12_leftInv a m v z ha hzs]
      exact hzt
    · have hpos : 0 < (z - v) / a := by simpa [squareSupportB12] using hzs
      have hsqrt : 0 < Real.sqrt ((z - v) / a) := Real.sqrt_pos.2 hpos
      unfold squareLeftInvB12
      linarith
  · rintro ⟨hyt, hym⟩
    refine ⟨squareMapB12 a m v y, ⟨hyt, ?_⟩, ?_⟩
    · have hdiv : (squareMapB12 a m v y - v) / a = (y - m) ^ 2 := by
        unfold squareMapB12
        field_simp [ha]
        <;> ring
      simp only [squareSupportB12, Set.mem_setOf_eq]
      rw [hdiv]
      nlinarith
    · exact squareLeftInvB12_squareMap a m v y ha hym

theorem measurableSet_squareSupportB12 (a v : ℝ) :
    MeasurableSet (squareSupportB12 a v) := by
  unfold squareSupportB12
  measurability

/-- Branchwise change of variables, valid for an arbitrary (not necessarily continuous) density. -/
theorem square_right_branch_lintegral_B12
    (a m v : ℝ) (ha : a ≠ 0) (t : Set ℝ) (ht : MeasurableSet t)
    (f : ℝ → ℝ≥0∞) :
    (∫⁻ y in (squareMapB12 a m v ⁻¹' t) ∩ Set.Ioi m, f y) =
      ∫⁻ z in t ∩ squareSupportB12 a v,
        squareInvJacB12 a v z * f (squareRightInvB12 a m v z) := by
  rw [← squareRightInvB12_image a m v ha t]
  have h :=
    MeasureTheory.lintegral_image_eq_lintegral_abs_deriv_mul
      (ht.inter (measurableSet_squareSupportB12 a v))
      (fun z hz => (hasDerivAt_squareRightInv_B12 a m v z hz.2).hasDerivWithinAt)
      ((squareRightInvB12_injOn a m v ha).mono Set.inter_subset_right)
      f
  simpa [squareInvJacB12] using h

theorem square_left_branch_lintegral_B12
    (a m v : ℝ) (ha : a ≠ 0) (t : Set ℝ) (ht : MeasurableSet t)
    (f : ℝ → ℝ≥0∞) :
    (∫⁻ y in (squareMapB12 a m v ⁻¹' t) ∩ Set.Iio m, f y) =
      ∫⁻ z in t ∩ squareSupportB12 a v,
        squareInvJacB12 a v z * f (squareLeftInvB12 a m v z) := by
  rw [← squareLeftInvB12_image a m v ha t]
  have h :=
    MeasureTheory.lintegral_image_eq_lintegral_abs_deriv_mul
      (ht.inter (measurableSet_squareSupportB12 a v))
      (fun z hz => (hasDerivAt_squareLeftInv_B12 a m v z hz.2).hasDerivWithinAt)
      ((squareLeftInvB12_injOn a m v ha).mono Set.inter_subset_right)
      f
  simpa [squareInvJacB12, abs_neg] using h

/- Remaining compile target: sum the two branch identities, use the zero singleton,
   simplify squareInvJacB12 to 1/(2*sqrt(|a|*|z-v|)), and then formalize
   the arbitrary interval preimage-length bound. -/

end QformFiveB
