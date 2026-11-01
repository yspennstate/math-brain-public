import Lean.Elab.Tactic.Omega

-- Scalar numerator identity only, not the Fourier or affine theorem.
theorem bank_numerator (D K : Int) :
    D + (-D + 4 * (1-K)) = 4 * (1-K) := by
  omega
