theorem A015_incidence_ratio (s k : Nat) (h : s <= k) :
    s * (k + 1) <= (s + 1) * k := by
  simpa [Nat.mul_add, Nat.add_mul, Nat.mul_comm] using
    Nat.add_le_add_left h (s * k)

theorem A015_nonempty_owners (a : List Nat)
    (h : forall x, x in a -> 1 <= x) : a.length <= a.sum := by
  induction a with
  | nil => simp
  | cons x xs ih =>
    have hx : 1 <= x := h x (by simp)
    have hs : forall y, y in xs -> 1 <= y := by
      intro y hy
      exact h y (by simp [hy])
    have hi := ih hs
    simpa [List.length_cons, List.sum_cons, Nat.add_comm] using
      Nat.add_le_add hx hi
