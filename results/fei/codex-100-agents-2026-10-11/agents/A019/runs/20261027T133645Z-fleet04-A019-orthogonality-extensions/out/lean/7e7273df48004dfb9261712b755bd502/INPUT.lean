-- Core Lean only. This certifies the exact scalar debt identity after clearing
-- the common positive dyadic reach. It does not certify Fourier or tree laws.
theorem essentialDebt (k m : Nat) (hk : 4 ≤ k) :
    (k - 4) * m + 4 * m = k * m := by
  rw [← Nat.add_mul, Nat.sub_add_cancel hk]
