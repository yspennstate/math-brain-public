import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Tactic

/-!
Lean check for `parts/atomic.tex`, Proposition `prop:sign-critical`.  The file
proves the determinant-zero core, an `n+2`-column finite pigeonhole version, and
the full arbitrary-`m` statement: if `2 <= m` and `N >= 2 * m - 1`, a sign matrix
has an `m`-row square minor whose first two columns agree or are opposite, hence
determinant zero.
-/

namespace Paper19

open Matrix

lemma eq_neg_of_sign_ne {a b : ℤ}
    (ha : a = 1 ∨ a = -1) (hb : b = 1 ∨ b = -1) (hne : a ≠ b) :
    a = -b := by
  rcases ha with rfl | rfl <;> rcases hb with rfl | rfl <;> simp at hne ⊢

lemma fin_zero_ne_one {n : ℕ} : (0 : Fin (n + 2)) ≠ 1 := by
  intro h
  have hv := congrArg Fin.val h
  simp at hv

theorem det_zero_of_first_two_columns_equal {n : ℕ}
    (A : Matrix (Fin (n + 2)) (Fin (n + 2)) ℤ)
    (h : ∀ i, A i 0 = A i 1) :
    A.det = 0 := by
  apply Matrix.det_zero_of_column_eq (M := A) (i := (0 : Fin (n + 2))) (j := 1)
  · exact fin_zero_ne_one
  · intro k
    exact h k

theorem det_zero_of_first_two_columns_opposite {n : ℕ}
    (A : Matrix (Fin (n + 2)) (Fin (n + 2)) ℤ)
    (h : ∀ i, A i 0 = -A i 1) :
    A.det = 0 := by
  let B : Matrix (Fin (n + 2)) (Fin (n + 2)) ℤ :=
    A.updateCol (0 : Fin (n + 2)) (fun i => A i 0 + A i 1)
  have hBdet : B.det = A.det := by
    change (A.updateCol (0 : Fin (n + 2)) (fun i => A i 0 + A i 1)).det = A.det
    simpa using
      (Matrix.det_updateCol_add_smul_self (A := A)
        (i := (0 : Fin (n + 2))) (j := 1) (c := (1 : ℤ)) fin_zero_ne_one)
  have hBzero : B.det = 0 := by
    apply Matrix.det_eq_zero_of_column_eq_zero (A := B) (j := (0 : Fin (n + 2)))
    intro i
    change A i 0 + A i 1 = 0
    rw [h i]
    simp
  exact hBdet ▸ hBzero

theorem signCritical_nplus2 {N n : ℕ}
    (hN : 2 * (n + 2) - 1 ≤ N)
    (A : Matrix (Fin N) (Fin (n + 2)) ℤ)
    (hA : ∀ i j, A i j = (1 : ℤ) ∨ A i j = (-1 : ℤ)) :
    ∃ rows : Fin (n + 2) ↪ Fin N,
      (A.submatrix rows id).det = 0 := by
  classical
  let E : Finset (Fin N) :=
    Finset.univ.filter (fun i => A i 0 = A i 1)
  let O : Finset (Fin N) :=
    Finset.univ.filter (fun i => ¬ A i 0 = A i 1)
  by_cases hE : n + 2 ≤ E.card
  · obtain ⟨R, hRE, hRcard⟩ := E.exists_subset_card_eq hE
    let e := (Finset.equivFinOfCardEq hRcard).symm
    let rows : Fin (n + 2) ↪ Fin N :=
      { toFun := fun i => (e i : Fin N)
        inj' := by
          intro i j hij
          exact e.injective (Subtype.ext hij) }
    refine ⟨rows, ?_⟩
    apply det_zero_of_first_two_columns_equal
    intro i
    have hmemR : (e i : Fin N) ∈ R := (e i).2
    have hmemE : (e i : Fin N) ∈ E := hRE hmemR
    exact (Finset.mem_filter.mp hmemE).2
  · have hsum :
        E.card + O.card = N := by
      calc
        E.card + O.card
            = (Finset.univ.filter (fun i : Fin N => A i 0 = A i 1)).card
              + (Finset.univ.filter (fun i : Fin N => ¬ A i 0 = A i 1)).card := by
                rfl
        _ = (Finset.univ : Finset (Fin N)).card := by
              exact Finset.card_filter_add_card_filter_not
                (s := (Finset.univ : Finset (Fin N)))
                (p := fun i => A i 0 = A i 1)
        _ = N := by simp
    have hO : n + 2 ≤ O.card := by
      have hEupper : E.card ≤ n + 1 := by omega
      omega
    obtain ⟨R, hRO, hRcard⟩ := O.exists_subset_card_eq hO
    let e := (Finset.equivFinOfCardEq hRcard).symm
    let rows : Fin (n + 2) ↪ Fin N :=
      { toFun := fun i => (e i : Fin N)
        inj' := by
          intro i j hij
          exact e.injective (Subtype.ext hij) }
    refine ⟨rows, ?_⟩
    apply det_zero_of_first_two_columns_opposite
    intro i
    have hmemR : (e i : Fin N) ∈ R := (e i).2
    have hmemO : (e i : Fin N) ∈ O := hRO hmemR
    have hne : A (e i : Fin N) 0 ≠ A (e i : Fin N) 1 :=
      (Finset.mem_filter.mp hmemO).2
    exact eq_neg_of_sign_ne (hA (e i : Fin N) 0) (hA (e i : Fin N) 1) hne

def firstCol {m : ℕ} (hm : 2 ≤ m) : Fin m := ⟨0, by omega⟩

def secondCol {m : ℕ} (hm : 2 ≤ m) : Fin m := ⟨1, by omega⟩

lemma firstCol_ne_secondCol {m : ℕ} (hm : 2 ≤ m) :
    firstCol hm ≠ secondCol hm := by
  intro h
  have hv := congrArg Fin.val h
  simp [firstCol, secondCol] at hv

theorem det_zero_of_first_two_columns_equal_general {m : ℕ} (hm : 2 ≤ m)
    (A : Matrix (Fin m) (Fin m) ℤ)
    (h : ∀ i, A i (firstCol hm) = A i (secondCol hm)) :
    A.det = 0 := by
  apply Matrix.det_zero_of_column_eq (M := A) (i := firstCol hm) (j := secondCol hm)
  · exact firstCol_ne_secondCol hm
  · intro k
    exact h k

theorem det_zero_of_first_two_columns_opposite_general {m : ℕ} (hm : 2 ≤ m)
    (A : Matrix (Fin m) (Fin m) ℤ)
    (h : ∀ i, A i (firstCol hm) = -A i (secondCol hm)) :
    A.det = 0 := by
  let B : Matrix (Fin m) (Fin m) ℤ :=
    A.updateCol (firstCol hm) (fun i => A i (firstCol hm) + A i (secondCol hm))
  have hBdet : B.det = A.det := by
    change (A.updateCol (firstCol hm) (fun i => A i (firstCol hm) + A i (secondCol hm))).det = A.det
    simpa using
      (Matrix.det_updateCol_add_smul_self (A := A)
        (i := firstCol hm) (j := secondCol hm) (c := (1 : ℤ)) (firstCol_ne_secondCol hm))
  have hBzero : B.det = 0 := by
    apply Matrix.det_eq_zero_of_column_eq_zero (A := B) (j := firstCol hm)
    intro i
    change A i (firstCol hm) + A i (secondCol hm) = 0
    rw [h i]
    simp
  exact hBdet ▸ hBzero

theorem signCritical {N m : ℕ} (hm : 2 ≤ m)
    (hN : 2 * m - 1 ≤ N)
    (A : Matrix (Fin N) (Fin m) ℤ)
    (hA : ∀ i j, A i j = (1 : ℤ) ∨ A i j = (-1 : ℤ)) :
    ∃ rows : Fin m ↪ Fin N,
      (A.submatrix rows id).det = 0 := by
  classical
  let E : Finset (Fin N) :=
    Finset.univ.filter (fun i => A i (firstCol hm) = A i (secondCol hm))
  let O : Finset (Fin N) :=
    Finset.univ.filter (fun i => ¬ A i (firstCol hm) = A i (secondCol hm))
  by_cases hE : m ≤ E.card
  · obtain ⟨R, hRE, hRcard⟩ := E.exists_subset_card_eq hE
    let e := (Finset.equivFinOfCardEq hRcard).symm
    let rows : Fin m ↪ Fin N :=
      { toFun := fun i => (e i : Fin N)
        inj' := by
          intro i j hij
          exact e.injective (Subtype.ext hij) }
    refine ⟨rows, ?_⟩
    apply det_zero_of_first_two_columns_equal_general hm
    intro i
    have hmemR : (e i : Fin N) ∈ R := (e i).2
    have hmemE : (e i : Fin N) ∈ E := hRE hmemR
    exact (Finset.mem_filter.mp hmemE).2
  · have hsum :
        E.card + O.card = N := by
      calc
        E.card + O.card
            = (Finset.univ.filter (fun i : Fin N => A i (firstCol hm) = A i (secondCol hm))).card
              + (Finset.univ.filter (fun i : Fin N => ¬ A i (firstCol hm) = A i (secondCol hm))).card := by
                rfl
        _ = (Finset.univ : Finset (Fin N)).card := by
              exact Finset.card_filter_add_card_filter_not
                (s := (Finset.univ : Finset (Fin N)))
                (p := fun i => A i (firstCol hm) = A i (secondCol hm))
        _ = N := by simp
    have hO : m ≤ O.card := by
      have hEupper : E.card ≤ m - 1 := by omega
      omega
    obtain ⟨R, hRO, hRcard⟩ := O.exists_subset_card_eq hO
    let e := (Finset.equivFinOfCardEq hRcard).symm
    let rows : Fin m ↪ Fin N :=
      { toFun := fun i => (e i : Fin N)
        inj' := by
          intro i j hij
          exact e.injective (Subtype.ext hij) }
    refine ⟨rows, ?_⟩
    apply det_zero_of_first_two_columns_opposite_general hm
    intro i
    have hmemR : (e i : Fin N) ∈ R := (e i).2
    have hmemO : (e i : Fin N) ∈ O := hRO hmemR
    have hne : A (e i : Fin N) (firstCol hm) ≠ A (e i : Fin N) (secondCol hm) :=
      (Finset.mem_filter.mp hmemO).2
    exact eq_neg_of_sign_ne
      (hA (e i : Fin N) (firstCol hm))
      (hA (e i : Fin N) (secondCol hm))
      hne

end Paper19
