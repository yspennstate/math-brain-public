import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- Constant weight rescaling cancels in a finite normalized Gibbs law.
theorem normalized_weight_rescaling {I : Type*} (S : Finset I)
    (w : I → Real) (c : Real) (hc : c ≠ 0)
    (hZ : Finset.sum S w ≠ 0) (i : I) :
    (c * w i) / (Finset.sum S (fun j => c * w j)) =
      w i / (Finset.sum S w) := by
  simp only [← Finset.mul_sum]
  field_simp [hc, hZ] <;> ring

theorem exp_energy_shift (b E C : Real) :
    Real.exp (-b * (E + C)) = Real.exp (-b * C) * Real.exp (-b * E) := by
  rw [← Real.exp_add]
  congr 1
  ring

#print axioms normalized_weight_rescaling
#print axioms exp_energy_shift
