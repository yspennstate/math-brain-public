import Mathlib

theorem w340_dpp_atom_product (a b : ℝ) :
    (a * b) * ((1 - a) * (1 - b)) =
      (a * (1 - b)) * ((1 - a) * b) := by
  ring
