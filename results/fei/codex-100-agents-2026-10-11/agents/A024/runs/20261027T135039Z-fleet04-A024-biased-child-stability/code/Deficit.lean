import Mathlib.Tactic

theorem odd_face_deficit (N : ℚ) (hN : 1 ≤ N) :
    ((3*N+14)/128 - 5*(3*N+44)/2048 = (33*N+4)/2048) ∧
    0 < (3*N+14)/128 - 5*(3*N+44)/2048 := by
  constructor
  · ring
  · linarith
