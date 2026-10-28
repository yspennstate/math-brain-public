theorem same_original_bank
    (controllerCost controllerBank seedCost seedBank weight : Nat)
    (hc : controllerCost ≤ controllerBank)
    (hs : seedCost ≤ seedBank) :
    controllerCost + weight * seedCost ≤ controllerBank + weight * seedBank :=
  Nat.add_le_add hc (Nat.mul_le_mul_left weight hs)
