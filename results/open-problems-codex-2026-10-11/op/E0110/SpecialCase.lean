import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

open Finset

-- Cauchy--Schwarz used for every prefix of the discrete covariance estimate.
theorem prefix_cauchy (a : Nat → Real) (n : Nat) :
    (∑ k ∈ range n, a k)^2 ≤ (n : Real) * ∑ k ∈ range n, (a k)^2 := by
  have h := sum_mul_sq_le_sq_mul_sq (s := range n)
    (f := fun _ => (1 : Real)) (g := a)
  simpa using h

-- d=3 check of the general chain quadratic-form identity.
theorem chain_energy_three (x y z : Real) :
    2 * (x^2 + y^2 + z^2 - x*y - y*z) =
      x^2 + (y-x)^2 + (z-y)^2 + z^2 := by ring

-- Exact Morse factorization shift AA* = H_(a-2) + (a-1).
theorem morse_shift (a y : Real) :
    (a-y)^2/4 + y/2 = ((a-2)-y)^2/4 - y/2 + (a-1) := by ring

-- Lower bounds for the partner potential, the small-shape cases.
theorem small_shape_partner (a y : Real) (ha : a ≤ 1) (hy : 0 ≤ y) :
    a^2/4 ≤ (a-y)^2/4 + y/2 := by
  have hm : 0 ≤ (1-a)*y := mul_nonneg (by linarith) hy
  nlinarith [sq_nonneg y]

theorem middle_shape_partner (a y : Real) (hlo : 1 ≤ a) (hhi : a ≤ 2) :
    a/8 ≤ (a-y)^2/4 + y/2 := by
  nlinarith [sq_nonneg (y-(a-1))]

#print axioms prefix_cauchy
#print axioms chain_energy_three
#print axioms morse_shift
#print axioms small_shape_partner
#print axioms middle_shape_partner
