import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

-- Characteristic polynomial of the first two rows of B B^T.
theorem laguerre_two_by_two (x d e c : Real) :
    (x - d^2) * (x - (e^2 + c^2)) - (d*c)^2 =
      x^2 - (d^2 + e^2 + c^2)*x + d^2*e^2 := by
  ring

-- Trace(T^4) for T = [[u,b],[b,v]], from squaring T first.
theorem quartic_trace_identity (u v b : Real) :
    (u^2 + b^2)^2 + (v^2 + b^2)^2 + 2*(b*(u+v))^2 =
      u^4 + v^4 + 4*b^2*(u^2 + u*v + v^2) + 2*b^4 := by
  ring
