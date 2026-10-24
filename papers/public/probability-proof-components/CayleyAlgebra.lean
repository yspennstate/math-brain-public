import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
Algebraic components only. L denotes an arbitrary real comparison logarithm;
specializing L to log d gives the paper's identities. No graph, Markov law,
Fourier completeness, or probabilistic limit is formalized in this file.
-/
namespace AbelianCutoffAlgebra

theorem nonzero_jump_generator (N D pi ident : ℝ) (hN : N - 1 ≠ 0) (hD : D ≠ 0) :
    ((N - 1) / D) * ((N * pi - ident) / (N - 1) - ident) =
      (N / D) * (pi - ident) := by
  field_simp [hN, hD]
  <;> ring

def degree (d m N : ℝ) := d * (m - 1) + N - 1

theorem cube_sector_gap (d m N a : ℝ) (hD : degree d m N ≠ 0) :
    1 - ((d - 2 * a) * (m - 1) - 1) / degree d m N =
      (2 * a * (m - 1) + N) / degree d m N := by
  unfold degree at *
  field_simp [hD]
  <;> ring

theorem auxiliary_sector_gap (d m N : ℝ) (hD : degree d m N ≠ 0) :
    1 - (-d + N - 1) / degree d m N = d * m / degree d m N := by
  unfold degree at *
  field_simp [hD]
  <;> ring

theorem mixed_sector_gap (d m N a : ℝ) (hD : degree d m N ≠ 0) :
    1 - (-(d - 2 * a) - 1) / degree d m N =
      (degree d m N + d - 2 * a + 1) / degree d m N := by
  unfold degree at *
  field_simp [hD]
  <;> ring

theorem first_cube_gap (d m N : ℝ) (hd : d ≠ 0) (hD : degree d m N ≠ 0) :
    (2 * (m - 1) + N) / degree d m N =
      2 * (d * (m - 1) / degree d m N) / d + N / degree d m N := by
  field_simp [hd, hD]
  <;> ring

theorem gap_times_comparison_scale (d alpha beta L : ℝ) (hd : d ≠ 0)
    (ha : alpha ≠ 0) :
    (2 * alpha / d + beta) * (d * L / (4 * alpha)) =
      L / 2 + beta * (d * L / (4 * alpha)) := by
  field_simp [hd, ha]
  <;> ring

theorem reset_times_comparison_scale (d m N L : ℝ) (hd : d ≠ 0)
    (hm : m - 1 ≠ 0) (hD : degree d m N ≠ 0) :
    (N / degree d m N) * (d * L / (4 * (d * (m - 1) / degree d m N))) =
      N * L / (4 * (m - 1)) := by
  field_simp [hd, hm, hD]
  <;> ring

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

end AbelianCutoffAlgebra

#print axioms AbelianCutoffAlgebra.nonzero_jump_generator
#print axioms AbelianCutoffAlgebra.cube_sector_gap
#print axioms AbelianCutoffAlgebra.auxiliary_sector_gap
#print axioms AbelianCutoffAlgebra.mixed_sector_gap
#print axioms AbelianCutoffAlgebra.first_cube_gap
#print axioms AbelianCutoffAlgebra.gap_times_comparison_scale
#print axioms AbelianCutoffAlgebra.reset_times_comparison_scale
#print axioms AbelianCutoffAlgebra.sector_numerator_comparison
