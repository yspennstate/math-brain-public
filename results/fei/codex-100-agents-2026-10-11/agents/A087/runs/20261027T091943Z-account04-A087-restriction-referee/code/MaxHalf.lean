import Lean.Elab.Tactic.Omega

theorem A087MaxHalf (a b c d : Nat) (h1 : a <= 2*c) (h2 : b <= 2*d) : max a b <= 2 * max c d := by
  omega
