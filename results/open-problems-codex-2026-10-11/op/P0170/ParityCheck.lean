import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Finset.Card

abbrev evenParity3 (x : Fin 3 → Bool) : Prop :=
  Bool.xor (Bool.xor (x 0) (x 1)) (x 2) = false

theorem parity3_card :
    ((Finset.univ : Finset (Fin 3 → Bool)).filter evenParity3).card = 4 := by
  decide +kernel

theorem parity3_pair_marginals :
    ∀ (i j : Fin 3), i ≠ j → ∀ (a b : Bool),
      ((Finset.univ : Finset (Fin 3 → Bool)).filter
        (fun x => evenParity3 x ∧ x i = a ∧ x j = b)).card = 1 := by
  decide +kernel

abbrev evenParity5 (x : Fin 5 → Bool) : Prop :=
  Bool.xor (Bool.xor (Bool.xor (Bool.xor (x 0) (x 1)) (x 2)) (x 3)) (x 4) = false

theorem parity5_card :
    ((Finset.univ : Finset (Fin 5 → Bool)).filter evenParity5).card = 16 := by
  decide +kernel

theorem parity5_first_four_marginal :
    ∀ (a b c d : Bool),
      ((Finset.univ : Finset (Fin 5 → Bool)).filter
        (fun x => evenParity5 x ∧ x 0 = a ∧ x 1 = b ∧ x 2 = c ∧ x 3 = d)).card = 1 := by
  decide +kernel
