import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.Tactic

/-!
The first assertion of Lemma 3.3 of "Quadratic forms with five large singular values have bounded densities"
(repaired text, sha256 90f859b7): if `Y` and `Y'` are independent and `Y` has a density bounded by one, then `Y - Y'` has
a density bounded by one.

A law has a density bounded by one exactly when it is at most Lebesgue measure, so the statement is
`Law(Y - Y') ≤ Lebesgue` given `Law(Y) ≤ Lebesgue`, for any law of `Y'`: by Tonelli and the translation invariance of
Lebesgue measure, `P(Y - Y' ∈ B) = ∫ P(Y ∈ B + y') dν(y') ≤ ∫ |B + y'| dν(y') = |B|`. (The paper computes the density
`∫ f(x + y) f(y) dy ≤ ‖f‖_∞ ‖f‖_1`; only the bound on the law of `Y` is needed.)
-/

open MeasureTheory Set

namespace QformFiveB

/-- **Lemma 3.3, the difference.** `Law(Y) ≤ Lebesgue` and `Y'` independent give `Law(Y - Y') ≤ Lebesgue`. -/
theorem diff_density_le_one (μ ν : Measure ℝ) [SFinite μ] [IsProbabilityMeasure ν] (hμ : μ ≤ volume) :
    (μ.prod ν).map (fun p : ℝ × ℝ => p.1 - p.2) ≤ volume := by
  rw [Measure.le_iff]
  intro B hB
  have hm : Measurable (fun p : ℝ × ℝ => p.1 - p.2) := measurable_fst.sub measurable_snd
  rw [Measure.map_apply hm hB, Measure.prod_apply_symm (hm hB)]
  calc ∫⁻ y', μ ((fun y => (y, y')) ⁻¹' ((fun p : ℝ × ℝ => p.1 - p.2) ⁻¹' B)) ∂ν
      ≤ ∫⁻ y', volume ((fun y => (y, y')) ⁻¹' ((fun p : ℝ × ℝ => p.1 - p.2) ⁻¹' B)) ∂ν :=
        lintegral_mono (fun y' => hμ _)
    _ = ∫⁻ _y', volume B ∂ν := by
        congr 1
        funext y'
        have e : (fun y => (y, y')) ⁻¹' ((fun p : ℝ × ℝ => p.1 - p.2) ⁻¹' B) = (fun y => y + -y') ⁻¹' B := by
          ext y
          simp [sub_eq_add_neg]
        rw [e, measure_preimage_add_right]
    _ = volume B := by simp

end QformFiveB
