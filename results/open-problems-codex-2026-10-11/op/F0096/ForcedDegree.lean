import Mathlib.Data.Finset.Card

/- A degree-four vertex whose incident edges are all forced cannot
   belong to a spanning cubic subgraph. The graph argument supplies
   the inclusion of its four neighbors in the subgraph neighbor set. -/
theorem forced_four_excludes_cubic {α : Type*} [DecidableEq α]
    (originalNeighbors cubicNeighbors : Finset α)
    (forced : originalNeighbors ⊆ cubicNeighbors)
    (degree_four : originalNeighbors.card = 4)
    (degree_three : cubicNeighbors.card = 3) : False := by
  have h := Finset.card_le_card forced
  rw [degree_four, degree_three] at h
  exact (by decide : ¬ (4 ≤ 3)) h
