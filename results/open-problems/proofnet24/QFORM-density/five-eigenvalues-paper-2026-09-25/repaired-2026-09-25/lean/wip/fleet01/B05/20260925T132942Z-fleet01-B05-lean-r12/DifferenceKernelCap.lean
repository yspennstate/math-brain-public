import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.Tactic

/-!
WIP for repaired Lemma 3.3, source lines 231--241:
the pointwise cap on the convolution kernel proposed as the density of Y - Y'.

Exact paper source:
  yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa
  paper.tex blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a

This file has NOT been compiled in this runtime. Do not count it as verified
until it compiles against Mathlib 5e932f97 with no sorry/admit/new axiom
and an axiom log is recorded.
-/

open MeasureTheory

namespace QformFiveB

/-- If f is nonnegative and pointwise at most one, the candidate difference
kernel is bounded by the total mass of f. This is the inequality used in the
first sentence of the proof of Lemma 3.3. -/
theorem difference_kernel_le_mass
    (f : ℝ → ℝ)
    (hf0 : ∀ y, 0 ≤ f y)
    (hf1 : ∀ y, f y ≤ 1)
    (hfint : Integrable f)
    (x : ℝ) :
    (∫ y, f (x + y) * f y) ≤ ∫ y, f y := by
  apply integral_mono_of_nonneg
  · exact Filter.Eventually.of_forall fun y =>
      mul_nonneg (hf0 (x + y)) (hf0 y)
  · exact hfint
  · exact Filter.Eventually.of_forall fun y =>
      mul_le_of_le_one_left (hf0 y) (hf1 (x + y))

/-- Probability-density specialization of `difference_kernel_le_mass`. -/
theorem difference_kernel_le_one
    (f : ℝ → ℝ)
    (hf0 : ∀ y, 0 ≤ f y)
    (hf1 : ∀ y, f y ≤ 1)
    (hfint : Integrable f)
    (hmass : (∫ y, f y) = 1)
    (x : ℝ) :
    (∫ y, f (x + y) * f y) ≤ 1 := by
  calc
    (∫ y, f (x + y) * f y) ≤ ∫ y, f y :=
      difference_kernel_le_mass f hf0 hf1 hfint x
    _ = 1 := hmass

end QformFiveB
