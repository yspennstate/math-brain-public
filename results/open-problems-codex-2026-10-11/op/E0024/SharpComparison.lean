import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-- Sharp shear bound, with k encoded algebraically to avoid square-root tactics. -/
theorem shear_bound (a b d c k : ℝ) (hk : 1 < k)
    (hrel : (k - 1)^2 = k * c^2) (hd : d^2 ≤ c^2 * a^2) :
    a^2 + (b+d)^2 ≤ k * (a^2+b^2) := by
  have hka : (k-1)^2*a^2 = k*c^2*a^2 := by rw [hrel]
  have hpos : 0 ≤ k * (c^2*a^2-d^2) :=
    mul_nonneg (by linarith) (by linarith)
  have hid : (k-1)*(k*(a^2+b^2)-(a^2+(b+d)^2)) =
      ((k-1)*b-d)^2 + (k-1)^2*a^2-k*d^2 := by ring
  have hprod : 0 ≤ (k-1)*(k*(a^2+b^2)-(a^2+(b+d)^2)) := by
    nlinarith only [hid, hka, hpos, sq_nonneg ((k-1)*b-d)]
  have : 0 ≤ k*(a^2+b^2)-(a^2+(b+d)^2) :=
    nonneg_of_mul_nonneg_right hprod (by linarith : 0 < k-1)
  linarith

theorem shear_comparison (a b d c k : ℝ) (hk : 1 < k)
    (hrel : (k - 1)^2 = k * c^2) (hd : d^2 ≤ c^2 * a^2) :
    a^2 + (b+d)^2 ≤ k*(a^2+b^2) ∧
    a^2+b^2 ≤ k*(a^2+(b+d)^2) := by
  constructor
  · exact shear_bound a b d c k hk hrel hd
  · have hn : (-d)^2 ≤ c^2*a^2 := by nlinarith only [hd]
    have h := shear_bound a (b+d) (-d) c k hk hrel hn
    simpa using h

#print axioms shear_bound
#print axioms shear_comparison
