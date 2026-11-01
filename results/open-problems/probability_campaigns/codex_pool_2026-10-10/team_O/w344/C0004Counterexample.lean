/- Three equally likely outcomes have T=(1,2,3), U=(1,0,1).
The first equality clears the denominators in E[T U]=E[T]E[U].
The inequality clears the denominators in
P(T=2,U=1) != P(T=2)P(U=1). This certifies only this arithmetic
step; the translation to random measures is proved in the prose report. -/
theorem mean_equality_and_dependence :
    ((1 + 2 + 3) * (1 + 0 + 1) : Nat) =
      3 * (1 * 1 + 2 * 0 + 3 * 1) ∧
    (0 : Nat) ≠ 1 * 2 := by
  decide
