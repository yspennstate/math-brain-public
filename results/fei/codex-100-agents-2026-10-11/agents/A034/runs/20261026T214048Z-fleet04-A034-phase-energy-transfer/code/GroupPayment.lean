import Std

-- All physical derivative energies on a finite uniform cube have a common
-- integer denominator.  This is precisely the final factor-two rounding
-- in section 3; it does not formalize the norm estimates or entropy proof.
theorem grouped_payment (energy first summed : Nat)
    (reverse_triangle : 9 * first <= 16 * energy)
    (tail_energy : 32 * summed <= 33 * first) :
    summed <= 2 * energy := by
  omega
