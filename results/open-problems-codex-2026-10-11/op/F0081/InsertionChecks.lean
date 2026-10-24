import Mathlib.Data.Int.Basic
import Lean.Elab.Tactic.Omega

-- Nonnegative integer changes whose total charge is one form one atom.
theorem one_atom_changes (a b c : Nat) (h : a + b + c = 1) :
    Or (And (a = 1) (And (b = 0) (c = 0)))
       (Or (And (a = 0) (And (b = 1) (c = 0)))
           (And (a = 0) (And (b = 0) (c = 1)))) := by
  omega

-- Restricting a nonnegative unit mass to a window gives zero or one.
theorem window_unit_change (k : Nat) (h : k <= 1) :
    Or (k = 0) (k = 1) := by omega

-- The square in the Poisson variance integrand equals the increment.
theorem integer_unit_square (k : Int) (h0 : 0 <= k) (h1 : k <= 1) :
    k * k = k := by
  have h : Or (k = 0) (k = 1) := by omega
  rcases h with h | h
  all_goals subst k; rfl
