import Init

-- Only the natural-width consequence of the analytic lower bound is formalized.
-- This theorem does not assert the entropy or curvature bound itself.
theorem width_growth (K : Nat) :
    exists m : Nat, 2 <= m /\ K < m + 2 := by
  refine Exists.intro (K + 2) (And.intro ?_ ?_)
  · exact Nat.le_add_left 2 K
  · exact Nat.lt_of_lt_of_le (Nat.lt_succ_self K)
      (Nat.succ_le_succ (Nat.le_add_right K 3))
