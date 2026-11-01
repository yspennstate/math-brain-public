import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

-- Only the exact algebraic certificate; the probability proof is in ATTEMPT.md.
theorem isolated_origin_at_critical :
    (1 / 2 : ℚ) * (1 - (1 / 2 : ℚ)) ^ 6 = (1 / 128 : ℚ) := by
  norm_num

theorem printed_exponent : (2 : ℚ) + (-2 / 3 : ℚ) = (4 / 3 : ℚ) := by
  norm_num

theorem critical_singleton_positive : (0 : ℚ) < (1 / 128 : ℚ) := by
  norm_num

#print axioms isolated_origin_at_critical
#print axioms printed_exponent
#print axioms critical_singleton_positive
