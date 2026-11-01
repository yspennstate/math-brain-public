import Mathlib.Tactic.Ring

-- This certifies the interior first-step polynomial identity only.
-- It does not certify the graph model, boundary conditions, or full refutation.
theorem w336_cycle_poisson (m j : Int) :
    (j - 1) * (m - j + 1) + (j + 1) * (m - j - 1) + 2 =
      2 * j * (m - j) := by
  ring
