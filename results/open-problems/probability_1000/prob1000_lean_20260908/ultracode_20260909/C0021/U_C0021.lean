/-
C0021 (Garban-Steif Exercise VIII.5): revealment exponent of iterated 3-majority.
Certified here: the exact rational facts the memo's bounds rest on.
  * influence identity  I(f)^2 / n = (3/2)^(2k) / 3^k = (3/4)^k   (lower bound on the revealment)
  * D_2 = 393/64 < (5/2)^2      the greedy recursion is not optimal at depth 2
  * D_3 = 15796051/1048576 < 2.4698^3
  * U_4 = 20871140813662641/562949953421312 < 2.4676^4   (exact cost of an explicit depth-4 policy)
  * U_4^3 < D_3^4   i.e. U_4^(1/4) < D_3^(1/3): depth 4 improves on the depth-3 composition bound
-/
import Mathlib

namespace C0021

theorem influence_identity (k : ℕ) : ((3:ℚ)/2)^(2*k) / 3^k = (3/4)^k := by
  rw [pow_mul, ← div_pow]
  norm_num

theorem D2_lt_greedy : (393:ℚ)/64 < (5/2)^2 := by norm_num

theorem D3_bound : (15796051:ℚ)/1048576 < (24698/10000)^3 := by norm_num

theorem U4_bound : (20871140813662641:ℚ)/562949953421312 < (24676/10000)^4 := by norm_num

theorem U4_beats_D3_composition :
    ((20871140813662641:ℚ)/562949953421312)^3 < ((15796051:ℚ)/1048576)^4 := by norm_num

/-- D_k^(1/k) decreasing along the computed values: D_2^3 < D_1^6 and D_3^2 < D_2^3 -/
theorem monotone_roots : ((393:ℚ)/64)^3 < (5/2)^6 ∧ ((15796051:ℚ)/1048576)^2 < ((393:ℚ)/64)^3 := by
  constructor <;> norm_num

end C0021

#print axioms C0021.influence_identity
#print axioms C0021.D2_lt_greedy
#print axioms C0021.D3_bound
#print axioms C0021.U4_bound
#print axioms C0021.U4_beats_D3_composition
#print axioms C0021.monotone_roots
