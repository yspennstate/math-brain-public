import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

open scoped BigOperators

-- A finite even-power instance of the interpolation step.
-- No native computation, sorry, or extra axiom is used.
theorem finite_interpolation_square {I : Type*} (s : Finset I)
    (f : I -> Real) (U : Real)
    (h : ∀ i ∈ s, (f i)^2 <= U^2) :
    (∑ i ∈ s, (f i)^4) <= U^2 * (∑ i ∈ s, (f i)^2) := by
  calc
    (∑ i ∈ s, (f i)^4) <= ∑ i ∈ s, U^2 * (f i)^2 := by
      apply Finset.sum_le_sum
      intro i hi
      calc
        (f i)^4 = (f i)^2 * (f i)^2 := by ring
        _ <= U^2 * (f i)^2 :=
          mul_le_mul_of_nonneg_right (h i hi) (sq_nonneg (f i))
    _ = U^2 * (∑ i ∈ s, (f i)^2) := by
      rw [Finset.mul_sum]

def movingWedge (x1 x2 y1 y2 : Real) : Real := x1*y2-x2*y1

-- One full rerooted lap adds c to the global area coordinate.
theorem reroot_terminal_area (A c g1 g2 : Real) :
    (A+c)-A-(1/2 : Real)*movingWedge g1 g2 g1 g2 = c := by
  unfold movingWedge
  ring
