import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Real scalar algebra only; no assertion about stochastic processes is formalized.
theorem square_add_bound (u v : Real) :
    (u + v)^2 <= 2*u^2 + 2*v^2 := by
  nlinarith [sq_nonneg (u-v)]

theorem energy_denominator_bound (a b u v D C : Real)
    (hreal : (a+b)^2 <= D*a^2)
    (him : v^2 <= C*a^2) (hD : 0 <= D) (hC : 0 <= C) :
    (a+b)^2 + (u+v)^2 <= (D+2*C+2)*(a^2+u^2) := by
  have hsum := square_add_bound u v
  have hmul : 0 <= (D+2*C)*u^2 :=
    mul_nonneg (by linarith) (sq_nonneg u)
  nlinarith [sq_nonneg a]

theorem norm_transfer_bound (a b u v C : Real)
    (hreal : a^2 <= (a+b)^2)
    (him : v^2 <= C*(a+b)^2) (hC : 0 <= C) :
    a^2+u^2 <= (2*C+2)*((a+b)^2+(u+v)^2) := by
  have hmul : 0 <= C*(u+v)^2 := mul_nonneg hC (sq_nonneg (u+v))
  nlinarith [sq_nonneg (u+2*v), sq_nonneg (a+b)]

#print axioms square_add_bound
#print axioms energy_denominator_bound
#print axioms norm_transfer_bound
