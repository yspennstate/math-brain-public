import Mathlib.Algebra.Order.BigOperators.Group.Finset

open scoped BigOperators

/-- The cardinality bound used in repairing a random reservoir. -/
theorem reservoir_repair_card_bound {V : Type*} [DecidableEq V]
    (R B : Finset V) (W : V → Finset V) (k : ℕ)
    (hW : ∀ v ∈ B, (W v).card ≤ k) :
    (R ∪ B.biUnion W).card ≤ R.card + k * B.card := by
  have hsum : (∑ v ∈ B, (W v).card) ≤ k * B.card := by
    calc
      (∑ v ∈ B, (W v).card) ≤ ∑ _v ∈ B, k := Finset.sum_le_sum hW
      _ = k * B.card := by simp [Nat.mul_comm]
  exact (Finset.card_union_le R (B.biUnion W)).trans
    (Nat.add_le_add_left (Finset.card_biUnion_le.trans hsum) R.card)

#print axioms reservoir_repair_card_bound
