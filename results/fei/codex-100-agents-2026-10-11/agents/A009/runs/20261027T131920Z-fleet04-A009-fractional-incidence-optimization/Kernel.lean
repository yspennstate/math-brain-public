import Mathlib.Tactic

-- This source formalizes one key square identity only. No successful
-- compilation, all-dimensional theorem or prose fidelity is asserted.
theorem triangle_square_identity (a b c : Real) :
    (a*b+a*c+b*c)^2 - 3*(a+b+c)*(a*b*c) =
      ((a*b-a*c)^2+(a*b-b*c)^2+(a*c-b*c)^2)/2 := by
  ring
