import Lean

theorem profile_tail_bound (m : Nat) : 8 * m + 25 ≤ 25 * 2 ^ m := by
  induction m with
  | zero => decide
  | succ m ih =>
      calc
        8 * (m + 1) + 25 ≤ (25 * 2 ^ m) * 2 := by omega
        _ = 25 * 2 ^ (m + 1) := by rw [Nat.pow_succ, Nat.mul_assoc]

theorem one_bank_transport (rootI leafI spentI rootCE leafCE release : Int)
    (hi : rootI = leafI + spentI) (hc : rootCE = leafCE + release) :
    leafI - leafCE = rootI - rootCE - spentI + release := by
  omega
