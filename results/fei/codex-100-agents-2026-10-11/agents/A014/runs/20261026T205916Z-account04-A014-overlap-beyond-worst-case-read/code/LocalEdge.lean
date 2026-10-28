theorem local_edge_lengths :
    13 ^ 8 < 2 * 12 ^ 8 ∧ 104 < 3 * 64 ∧ 52 < 64 := by decide

theorem component_mass_expansion (a b c d : Nat) :
    (a+b)*(c+d)=a*c+a*d+b*c+b*d := by
  simp [Nat.add_mul, Nat.mul_add, Nat.add_assoc]
