import Mathlib.Data.Finset.Card

/- Finite counting counterpart of the small-ball volume obstruction.
   This checks only the cardinality step, not continuum stability. -/
theorem no_full_territory_in_small_ball
    {A : Type*} [DecidableEq A] (territory ball : Finset A) (appetite : Nat)
    (contained : territory ⊆ ball)
    (sated : territory.card = appetite)
    (small : ball.card < appetite) : False := by
  have enough : appetite ≤ ball.card := sated ▸ Finset.card_le_card contained
  exact (Nat.not_lt_of_ge enough) small

theorem capacity_obstruction_forces_short_assignment
    {A : Type*} [DecidableEq A] {D : Type*} [LinearOrder D]
    (territory ball : Finset A) (appetite : Nat) (distance radius : D)
    (sated : territory.card = appetite)
    (small : ball.card < appetite)
    (stability_implication : radius < distance → territory ⊆ ball) :
    distance ≤ radius := by
  apply le_of_not_gt
  intro longer
  exact no_full_territory_in_small_ball territory ball appetite
    (stability_implication longer) sated small
