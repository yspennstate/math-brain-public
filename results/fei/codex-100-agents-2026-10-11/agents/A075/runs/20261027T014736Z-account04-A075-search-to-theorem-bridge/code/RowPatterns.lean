theorem two_padding (a b : Bool) :
    [!a, !b] ≠ [!a, b] ∧ [!a, !b] ≠ [a, b] ∧ [!a, b] ≠ [a, b] := by
  cases a <;> cases b <;> decide

theorem three_columns (a b c : Bool) :
    [!a, !a, a] ≠ [!b, b, b] ∧
    [!a, !a, a] ≠ [c, c, c] ∧ [!b, b, b] ≠ [c, c, c] := by
  cases a <;> cases b <;> cases c <;> decide

#print axioms two_padding
#print axioms three_columns
