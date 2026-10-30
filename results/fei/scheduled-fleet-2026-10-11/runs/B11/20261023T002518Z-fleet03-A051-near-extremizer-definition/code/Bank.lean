import Mathlib

-- Scalar conservation step only; this is not the Fourier theorem.
namespace A051
theorem reset_bank (H I Hc Ic p rho K : Real)
    (h : I = p + rho + Ic) :
    (H - K * I) + (K * Ic - Hc) = H - Hc - K * (p + rho) := by
  rw [h]
  ring
end A051
