import Std

-- Common integer denominators represent exact finite-cube energies.
-- This certifies only the6/11 rounding step, not entropy or norm geometry.
theorem grouped_payment_sharp (energy first summed : Nat)
    (reverse_triangle : 9 * first <= 16 * energy)
    (tail_energy : 32 * summed <= 33 * first) :
    6 * summed <= 11 * energy := by
  omega
