-- Core-only finite ledger cancellation. This does not certify the real-valued
-- Fourier identities, logarithm estimates, or the full composition theorem.
theorem A044_two_level_terminal (x y terminal : Nat) :
    ((x + y) + terminal) - terminal = x + y :=
  Nat.add_sub_cancel (x + y) terminal
