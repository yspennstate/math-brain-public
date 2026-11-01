import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
Exact algebraic components of the unweighted Abelian Cayley counterexample.
This file does not formalize the Cayley graph, its Markov semigroup, the Fourier
basis, or the limiting total-variation profile. No whole source theorem is claimed.
-/
namespace AbelianCutoff

/-- Entrywise identity converting uniform nonzero jumps into a reset generator. -/
theorem nonzero_jump_generator (N D pi ident : ℝ) (hN : N - 1 ≠ 0) (hD : D ≠ 0) :
    ((N - 1) / D) * ((N * pi - ident) / (N - 1) - ident) =
      (N / D) * (pi - ident) := by
  field_simp
  <;> ring

def degree (d m N : ℝ) := d * (m - 1) + N - 1

/-- Gap of a nontrivial cube character and trivial auxiliary character. -/
theorem cube_sector_gap (d m N a : ℝ) (hD : degree d m N ≠ 0) :
    1 - ((d - 2 * a) * (m - 1) - 1) / degree d m N =
      (2 * a * (m - 1) + N) / degree d m N := by
  unfold degree at *
  field_simp
  <;> ring

/-- Gap in the trivial-cube, nontrivial-auxiliary sector. -/
theorem auxiliary_sector_gap (d m N : ℝ) (hD : degree d m N ≠ 0) :
    1 - (-d + N - 1) / degree d m N = d * m / degree d m N := by
  unfold degree at *
  field_simp
  <;> ring

/-- Gap when both characters are nontrivial. -/
theorem mixed_sector_gap (d m N a : ℝ) (hD : degree d m N ≠ 0) :
    1 - (-(d - 2 * a) - 1) / degree d m N =
      (degree d m N + d - 2 * a + 1) / degree d m N := by
  unfold degree at *
  field_simp
  <;> ring

theorem first_cube_gap (d m N : ℝ) (hd : d ≠ 0) (hD : degree d m N ≠ 0) :
    (2 * (m - 1) + N) / degree d m N =
      2 * (d * (m - 1) / degree d m N) / d + N / degree d m N := by
  field_simp
  <;> ring

/-- The product condition diverges through log(d)/2 once the gap is identified. -/
theorem gap_times_comparison_scale (d alpha beta : ℝ) (hd : d ≠ 0)
    (ha : alpha ≠ 0) :
    (2 * alpha / d + beta) * (d * Real.log d / (4 * alpha)) =
      Real.log d / 2 + beta * (d * Real.log d / (4 * alpha)) := by
  field_simp
  <;> ring

/-- Exact reset intensity on the cube comparison time scale. -/
theorem reset_times_comparison_scale (d m N : ℝ) (hd : d ≠ 0)
    (hm : m - 1 ≠ 0) (hD : degree d m N ≠ 0) :
    (N / degree d m N) *
      (d * Real.log d / (4 * (d * (m - 1) / degree d m N))) =
      N * Real.log d / (4 * (m - 1)) := by
  field_simp
  <;> ring

/-- Exact sufficient comparisons for the first cube mode to be slowest. -/
theorem sector_numerator_comparison (d m N a : ℝ)
    (ha : 1 ≤ a) (hm : 1 ≤ m) (had : a ≤ d)
    (haux : 2 * (m - 1) + N ≤ d * m)
    (hmixed : 2 * (m - 1) + N ≤ degree d m N - d + 1) :
    (2 * (m - 1) + N ≤ 2 * a * (m - 1) + N) ∧
    (2 * (m - 1) + N ≤ d * m) ∧
    (2 * (m - 1) + N ≤ degree d m N + d - 2 * a + 1) := by
  refine ⟨?_, haux, ?_⟩
  · nlinarith [mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hm)]
  · linarith

end AbelianCutoff

#print axioms AbelianCutoff.nonzero_jump_generator
#print axioms AbelianCutoff.cube_sector_gap
#print axioms AbelianCutoff.auxiliary_sector_gap
#print axioms AbelianCutoff.mixed_sector_gap
#print axioms AbelianCutoff.first_cube_gap
#print axioms AbelianCutoff.gap_times_comparison_scale
#print axioms AbelianCutoff.reset_times_comparison_scale
#print axioms AbelianCutoff.sector_numerator_comparison
