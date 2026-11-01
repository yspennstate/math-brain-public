import Lean.Elab.Tactic.Omega
import Mathlib.Tactic.Ring
import Mathlib.Data.Rat.Defs

namespace C0100Dirichlet
-- A forbidden subset can be lowered without exceeding the stable cutoff.
theorem forbidden_lowering (height insideDegree : ℤ)
    (h : height < insideDegree) : height + 4 - insideDegree ≤ 3 := by
  omega

-- Lowering a site whose Laplacian is negative is likewise admissible.
theorem single_site_lowering (height : ℤ) (h : height ≤ -1) :
    height + 4 ≤ 3 := by
  omega

-- The strip barrier has exact cutoff-3 discrete Laplacian.
theorem strip_barrier_laplacian (x n : ℚ) :
    (3/2 : ℚ)*(x+1)*(x+1-n) + (3/2 : ℚ)*(x-1)*(x-1-n)
      - 2*((3/2 : ℚ)*x*(x-n)) = 3 := by
  ring

-- Kernel evaluation of every possible finite inside-degree.
theorem lowering_table : ∀ k : Fin 5,
    ((k.val : ℤ)-1) + 4 - (k.val : ℤ) = 3 := by
  decide +kernel
end C0100Dirichlet
