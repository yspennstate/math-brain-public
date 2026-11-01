import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

theorem two_component_defect (u v x y : Real) :
    (u^2 + v^2)*(x^2 + y^2) - (u*x + v*y)^2 = (u*y-v*x)^2 := by
  ring

theorem unit_two_component_cs (u v x y : Real) (h : u^2 + v^2 = 1) :
    (u*x + v*y)^2 <= x^2 + y^2 := by
  have hi := two_component_defect u v x y
  rw [h, one_mul] at hi
  apply sub_nonneg.mp
  rw [hi]
  exact sq_nonneg _

theorem complementary_gram_diagonal (p previous q : Real) :
    p*(1-q) + (1-previous)*q + (1-p)*(1-q) + previous*q = 1 := by
  ring

theorem laguerre_two_by_two_again (x d e c : Real) :
    (x-d^2)*(x-(e^2+c^2)) - (d*c)^2 =
      x^2 - (d^2+e^2+c^2)*x + d^2*e^2 := by
  ring

theorem quartic_trace_identity_again (u v b : Real) :
    (u^2+b^2)^2 + (v^2+b^2)^2 + 2*(b*(u+v))^2 =
      u^4+v^4+4*b^2*(u^2+u*v+v^2)+2*b^4 := by
  ring
