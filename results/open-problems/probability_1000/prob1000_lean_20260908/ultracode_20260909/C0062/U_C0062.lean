import Mathlib

/-!
C0062 (Romik, Section 1.18: the maximal-dimension Young diagram).

The hook shape (c+1, 1^b) has (c+b).choose b standard Young tableaux; moving its
top-right box to a new last row gives the hook (c, 1^(b+1)) with (c+b).choose (b+1)
tableaux.  The exact ratio of the two counts is c/(b+1) = (lambda_1 - 1)/l(lambda),
so the move increases the dimension exactly when lambda_1 >= l(lambda) + 2.
We certify the binomial identity and the resulting strict inequality.
-/

theorem hook_move_ratio (c b : ℕ) :
    (c + b).choose (b + 1) * (b + 1) = (c + b).choose b * c := by
  have h := Nat.choose_succ_right_eq (c + b) b
  rw [h, Nat.add_sub_cancel]

theorem hook_move_increases (c b : ℕ) (h : b + 2 ≤ c) :
    (c + b).choose b < (c + b).choose (b + 1) := by
  have key := hook_move_ratio c b
  have pos : 0 < (c + b).choose b := Nat.choose_pos (by omega)
  nlinarith [key, pos, h, Nat.zero_le b]

theorem hook_move_tie (b : ℕ) :
    (b + 1 + b).choose b = (b + 1 + b).choose (b + 1) := by
  have key := hook_move_ratio (b + 1) b
  have pos : 0 < (b + 1 + b).choose b := Nat.choose_pos (by omega)
  nlinarith [key, pos]

#print axioms hook_move_ratio
#print axioms hook_move_increases
#print axioms hook_move_tie
