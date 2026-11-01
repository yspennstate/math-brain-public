import Mathlib

-- Auxiliary chord only; no claim of formalizing Gibbs or the FEI bridge.
theorem quadratic_chord (A B C x y t : ℝ) (hA : 0 ≤ A)
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    A * (t*x+(1-t)*y)^2 + B*(t*x+(1-t)*y) + C ≤
      t*(A*x^2+B*x+C)+(1-t)*(A*y^2+B*y+C) := by
  have h : 0 ≤ A*t*(1-t)*(x-y)^2 :=
    mul_nonneg (mul_nonneg (mul_nonneg hA ht0) (sub_nonneg.mpr ht1))
      (sq_nonneg (x-y))
  nlinarith [h]
