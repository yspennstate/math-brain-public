import Mathlib.Data.Bool.Basic

-- true = healthy, false = infected; these are exactly the FA-1f constraints.
def faConstraint (left right : Bool) : Bool := (!left) || (!right)
def eastConstraint (left : Bool) : Bool := !left
def indicator (b : Bool) : Nat := if b then 1 else 0

-- This is the pointwise finite step in the Dirichlet-form comparison.
theorem east_le_fa :
    forall left right : Bool,
      indicator (eastConstraint left) <= indicator (faConstraint left right) := by
  decide +kernel

-- In infection coordinates, (0,1,0) <= (1,1,0). The center can recover
-- only in the second configuration: the death-rate monotonicity fails.
theorem isolated_cannot_recover : faConstraint true true = false := by
  decide +kernel

theorem adjacent_can_recover : faConstraint false true = true := by
  decide +kernel

-- More generally adding an infection cannot disable the constraint,
-- so it can enable recovery as well as infection.
theorem adding_left_infection_enables :
    forall right : Bool, faConstraint false right = true := by
  decide +kernel
