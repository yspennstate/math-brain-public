import Lean

theorem narrow_tail17 (m : Nat) : 16 * m + 17 ≤ 17 * 2 ^ m := by
  induction m with
  | zero => decide
  | succ m ih =>
      calc
        16 * (m + 1) + 17 ≤ (17 * 2 ^ m) * 2 := by omega
        _ = 17 * 2 ^ (m + 1) := by rw [Nat.pow_succ, Nat.mul_assoc]

theorem signed_reset_account (root oldLeaf freshLeaf release : Int)
    (h : root = release + oldLeaf) :
    release + freshLeaf = root + (freshLeaf - oldLeaf) := by omega
