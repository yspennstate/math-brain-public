import Std.Tactic

-- Only the finite sum-count step, not the entropy theorem or its translation.
theorem repair_sum (r : Nat) (xs : List Nat)
    (h : forall x, x ∈ xs -> r ≤ x) : xs.length * r ≤ xs.sum := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    have hx : r ≤ x := h x (by simp)
    have ht : xs.length * r ≤ xs.sum := ih (by
      intro y hy
      exact h y (by simp [hy]))
    simp only [List.length_cons, List.sum_cons, Nat.succ_mul]
    omega
