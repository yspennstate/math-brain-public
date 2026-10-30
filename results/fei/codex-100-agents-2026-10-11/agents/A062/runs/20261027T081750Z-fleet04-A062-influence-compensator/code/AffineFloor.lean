def affineFloorSum : List Nat → Nat
  | [] => 0
  | x :: xs => affineFloorSum xs + x

theorem affine_floor_aggregation (d : Nat) (xs : List Nat)
    (h : ∀ x ∈ xs, d ≤ x) : xs.length * d ≤ affineFloorSum xs := by
  induction xs with
  | nil => exact Nat.le_refl 0
  | cons x xs ih =>
    have hx : d ≤ x := h x (by simp)
    have ht : ∀ y ∈ xs, d ≤ y := by
      intro y hy
      exact h y (by simp [hy])
    simpa only [List.length_cons, Nat.succ_mul, affineFloorSum] using
      Nat.add_le_add (ih ht) hx
