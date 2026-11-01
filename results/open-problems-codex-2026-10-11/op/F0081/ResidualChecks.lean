import Mathlib.Data.Int.Basic
import Lean.Elab.Tactic.Omega

theorem residual_count_identity (a b : Nat) (h : Or (a = 0) (b = 0)) :
    (a - b) + (b - a) = a + b := by
  rcases h with h | h <;> omega

theorem chain_short (i j : Int) (h : i = j + 1) :
    8 * i - (8 * j + 5) = 3 := by omega

theorem chain_other_right (i j : Int) (h : i <= j) :
    5 <= (8 * j + 5) - 8 * i := by omega

theorem chain_other_left (i j : Int) (h : j + 2 <= i) :
    11 <= 8 * i - (8 * j + 5) := by omega

theorem chain_endpoint (n : Int) (hn : 1 <= n) :
    And (8 * (n - 1) + 5 = 8 * n - 3) (5 <= 8 * n - 3) := by
  constructor <;> omega
