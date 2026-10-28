import Mathlib.Tactic

-- Scalar bank step only. It does not formalize Fourier coefficients, KL or FEI.
theorem anchor_bank_drop (n a b : Real) (hn : 2 <= n) (hb : 0 <= b) :
    (n - 1) * a - (n - 2) * (a - b) >= a - b := by
  have h : 0 <= (n - 1) * b := mul_nonneg (by linarith) hb
  nlinarith

#print axioms anchor_bank_drop
