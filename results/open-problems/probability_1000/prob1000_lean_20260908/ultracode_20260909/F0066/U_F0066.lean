/-
F0066 (Janson 2012, Conjecture 20.6 / published 21.6): W(T_n)/sqrt n -> infinity
when nu = 1 and sigma^2 = infinity.  The conjecture is proved in the literature
(Addario-Berry, Brandenberger, Hamdan, Kerriou, EJP 27 (2022), Section 5; and
independently via Addario-Berry, Donderwinkel, Theorem 19 plus the pigeonhole
step below).  This file certifies only that elementary step:

  a rooted tree with n vertices, height H and width W satisfies n <= (H+1) * W,

stated abstractly: if the level sizes l_0, ..., l_H are each at most W and sum to n,
then n <= (H+1) * W.  Hence H = o(sqrt n) forces W >= n/(H+1) >> sqrt n.
-/
import Mathlib

open Finset

/-- Level counts `l : Fin (H+1) → ℕ`, each at most `W`, summing to `n`, force `n ≤ (H+1) * W`. -/
theorem levels_bound_vertices (H W n : ℕ) (l : Fin (H + 1) → ℕ)
    (hW : ∀ i, l i ≤ W) (hn : ∑ i, l i = n) : n ≤ (H + 1) * W := by
  have h := Finset.sum_le_card_nsmul (Finset.univ : Finset (Fin (H + 1))) l W
    (fun i _ => hW i)
  simpa [hn, Finset.card_univ, Fintype.card_fin, smul_eq_mul] using h

/-- The form used in the memo: `W ≥ n / (H+1)` (natural-number division, floor). -/
theorem width_ge_vertices_div_levels (H W n : ℕ) (l : Fin (H + 1) → ℕ)
    (hW : ∀ i, l i ≤ W) (hn : ∑ i, l i = n) : n / (H + 1) ≤ W := by
  have h := levels_bound_vertices H W n l hW hn
  exact Nat.div_le_of_le_mul (by simpa [Nat.mul_comm] using h)

#print axioms levels_bound_vertices
#print axioms width_ge_vertices_div_levels
