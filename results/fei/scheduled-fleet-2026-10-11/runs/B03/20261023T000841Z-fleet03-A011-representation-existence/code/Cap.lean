import Lean.Elab.Tactic.Omega

theorem a011_dyadic_cap (q : Nat) (hq : 2 ≤ q) :
    4 * (q+1) ≤ 3 * 2^q := by
  induction q, hq using Nat.le_induction with
  | base => decide
  | succ q hq ih =>
    calc
      4 * (q+1+1) ≤ 2 * (4 * (q+1)) := by omega
      _ ≤ 2 * (3 * 2^q) := Nat.mul_le_mul_left 2 ih
      _ = 3 * 2^(q+1) := by
        simp [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

#print axioms a011_dyadic_cap
