theorem a030_price_conversion (excess influence variance boundary : Nat)
    (coupling : variance * boundary = 2 * influence)
    (lipschitz_charge : excess <= 7 * (variance * boundary)) :
    excess <= 14 * influence := by
  calc
    excess <= 7 * (variance * boundary) := lipschitz_charge
    _ = 14 * influence := by rw [coupling, Nat.mul_assoc.symm]
