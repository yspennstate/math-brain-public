import Lean.Elab.Tactic.Omega

theorem residual_two_bit_inversion (a b c d : Int)
    (h0 : a = 0) (hn : a + b + c + d = 0)
    (hx : b + d = 0) (hy : c + d = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 := by
  omega
