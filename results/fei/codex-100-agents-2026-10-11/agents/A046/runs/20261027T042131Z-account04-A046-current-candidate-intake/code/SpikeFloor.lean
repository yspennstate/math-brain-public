import Mathlib

-- Only the cleared numerator in d_t derivative, not the KL theorem.
theorem spike_floor_derivative_numerator (u t : Real) :
  (1-t)*(t+u*(1-t))-t*(1-t)*(1-u)=u*(1-t) := by
  ring

-- The same original owner after a signed admission.
theorem spike_floor_same_owner (B C U sigma : Real) :
  B-(C+sigma)-U=(B-C-U)-sigma := by
  ring
