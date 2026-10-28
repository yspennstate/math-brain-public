import Mathlib
theorem a047_owner_obstruction (S A e CE I : ℚ) (ledger : S - (A + e) = 4 * I - CE) (excess : 4 * I < CE) : S < A + e := by linarith
#print axioms a047_owner_obstruction
