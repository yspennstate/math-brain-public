import Mathlib.Tactic

-- Reviewed statement for the two-child signed entropy telescope only.
-- Not compiled: the fresh campaign memory admission returned exit 1.
theorem signed_two_child_telescope
    (h h0 h1 ce0 ce1 d0 d1 : Real)
    (a0 : ce0 = h0 + d0) (a1 : ce1 = h1 + d1) :
    h - (h0 + h1) / 2 + (ce0 + ce1) / 2 = h + (d0 + d1) / 2 := by
  linarith
