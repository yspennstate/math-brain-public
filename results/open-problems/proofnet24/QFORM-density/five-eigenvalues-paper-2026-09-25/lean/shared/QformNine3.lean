import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Data.Finset.Powerset

/-!
Third group of formal checks for "Quadratic forms with nine large eigenvalues have bounded densities":
the rank count of Lemma 6.3 and the counting behind Lemma 6.5.
-/

open Finset

namespace QformNine

/-- A diagonal 0/1 matrix supported on a set U has rank at most the size of U. -/
theorem rank_indicator_le {n : ℕ} (U : Finset (Fin n)) :
    (Matrix.diagonal (fun i => if i ∈ U then (1:ℝ) else 0)).rank ≤ U.card := by
  rw [Matrix.rank_diagonal]
  have h : Fintype.card {i // (if i ∈ U then (1:ℝ) else 0) ≠ 0} = U.card := by
    rw [Fintype.card_subtype]
    congr 1
    ext i
    simp
  omega

/-- Rank is subadditive: rank(A + B) <= rank A + rank B. -/
theorem mrank_add_le {n : ℕ} (A B : Matrix (Fin n) (Fin n) ℝ) : (A + B).rank ≤ A.rank + B.rank := by
  unfold Matrix.rank
  rw [Matrix.mulVecLin_add]
  calc Module.finrank ℝ ↥(LinearMap.range (A.mulVecLin + B.mulVecLin))
      ≤ Module.finrank ℝ ↥(LinearMap.range A.mulVecLin ⊔ LinearMap.range B.mulVecLin) :=
        Submodule.finrank_mono (LinearMap.range_add_le _ _)
    _ ≤ Module.finrank ℝ ↥(LinearMap.range A.mulVecLin) + Module.finrank ℝ ↥(LinearMap.range B.mulVecLin) :=
        Submodule.finrank_add_le_finrank_add_finrank _ _

/-- Lemma 6.3, the rank count: if R - P vanishes outside the rows of a set Tr and the columns of a set Sc,
each of size at most r, and P has rank at most r, then R has rank at most 3r. -/
theorem rank_three_r {n r : ℕ} (R P : Matrix (Fin n) (Fin n) ℝ) (Tr Sc : Finset (Fin n))
    (hP : P.rank ≤ r) (hT : Tr.card ≤ r) (hS : Sc.card ≤ r)
    (hsupp : ∀ i j, (R - P) i j ≠ 0 → i ∈ Tr ∨ j ∈ Sc) : R.rank ≤ 3 * r := by
  let DT := Matrix.diagonal (fun i => if i ∈ Tr then (1:ℝ) else 0)
  let DS := Matrix.diagonal (fun i => if i ∈ Sc then (1:ℝ) else 0)
  let X := DT * (R - P)
  let Y := (R - P - X) * DS
  have hXY : R - P - X = Y := by
    ext i j
    simp only [Y, X, DT, DS, Matrix.mul_diagonal, Matrix.diagonal_mul, Matrix.sub_apply]
    by_cases hi : i ∈ Tr
    · simp [hi]
    · by_cases hj : j ∈ Sc
      · simp [hi, hj]
      · have h0 : (R - P) i j = 0 := by
          by_contra hne
          rcases hsupp i j hne with h | h
          · exact hi h
          · exact hj h
        rw [Matrix.sub_apply] at h0
        simp [hi, hj, h0]
  have hR : R = P + X + Y := by rw [← hXY]; abel
  have hXr : X.rank ≤ r := le_trans (Matrix.rank_mul_le_left _ _) (le_trans (rank_indicator_le Tr) hT)
  have hYr : Y.rank ≤ r := le_trans (Matrix.rank_mul_le_right _ _) (le_trans (rank_indicator_le Sc) hS)
  have h1 : (P + X + Y).rank ≤ (P + X).rank + Y.rank := mrank_add_le _ _
  have h2 : (P + X).rank ≤ P.rank + X.rank := mrank_add_le _ _
  rw [hR]
  omega

/-- Lemma 6.5, the count: for disjoint S and T in an n-element set, exactly 2^(n - |S| - |T|) subsets I contain S
and are disjoint from T; so a uniformly random partition puts S in I and T in its complement with probability
2^(-|S|-|T|), which is 4^(-k) when |S| = |T| = k. -/
theorem cut_count {n : ℕ} (S T : Finset (Fin n)) (hST : Disjoint S T) :
    ((Finset.univ : Finset (Fin n)).powerset.filter (fun I => S ⊆ I ∧ Disjoint T I)).card
      = 2 ^ (n - S.card - T.card) := by
  set F := (Finset.univ : Finset (Fin n)) \ (S ∪ T) with hF
  have hcardF : F.card = n - S.card - T.card := by
    rw [hF, Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ, Fintype.card_fin,
      Finset.card_union_of_disjoint hST]
    omega
  rw [← hcardF, ← Finset.card_powerset]
  apply Finset.card_nbij' (fun I => I \ S) (fun J => J ∪ S)
  · intro I hI
    simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_powerset] at hI ⊢
    obtain ⟨_, _, hTI⟩ := hI
    intro x hx
    rw [Finset.mem_sdiff] at hx
    rw [hF, Finset.mem_sdiff, Finset.mem_union]
    refine ⟨Finset.mem_univ x, ?_⟩
    rintro (h | h)
    · exact hx.2 h
    · exact Finset.disjoint_left.mp hTI h hx.1
  · intro J hJ
    simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_powerset] at hJ ⊢
    refine ⟨Finset.subset_univ _, Finset.subset_union_right, ?_⟩
    rw [Finset.disjoint_left]
    intro x hxT hx
    rw [Finset.mem_union] at hx
    rcases hx with h | h
    · have hxF := hJ h
      rw [hF, Finset.mem_sdiff, Finset.mem_union] at hxF
      exact hxF.2 (Or.inr hxT)
    · exact Finset.disjoint_left.mp hST h hxT
  · intro I hI
    simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_powerset] at hI
    exact Finset.sdiff_union_of_subset hI.2.1
  · intro J hJ
    simp only [Finset.mem_coe, Finset.mem_powerset] at hJ
    ext x
    simp only [Finset.mem_sdiff, Finset.mem_union]
    constructor
    · rintro ⟨h | h, hxS⟩
      · exact h
      · exact absurd h hxS
    · intro hx
      refine ⟨Or.inl hx, ?_⟩
      intro hxS
      have hxF := hJ hx
      rw [hF, Finset.mem_sdiff, Finset.mem_union] at hxF
      exact hxF.2 (Or.inl hxS)

end QformNine
