import Mathlib.Tactic
import Mathlib.Data.Finset.Max
import Mathlib.LinearAlgebra.Matrix.Rank

/-!
B20 draft toward the exact strict form of repaired Proposition 6.4 (paper.tex L568-L585).

STATUS: UNCOMPILED IN THIS RUNTIME.
The runtime has neither `lean` nor `lake`, and remote workflows are forbidden by the owner.
Do not count this file as Lean-verified until it is compiled in the pinned project and its
`#print axioms` output is checked.

This draft isolates the strict no-pivot bound that the current public QformFive3.lean weakens
to a non-strict `≤ 5/48` bound.
-/

namespace QformFiveStrictDraft

/-- Repaired paper L532-L534, strict form:
no pivot implies every off-diagonal entry has absolute value strictly below 5/48. -/
theorem nopivot_entry_strict {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ)
    (hd : ∀ i, |A i i| < 1 / 12)
    (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256)
    (i j : Fin n) (hij : i ≠ j) : |A i j| < 5 / 48 := by
  have hi := hd i
  have hj := hd j
  have hgi : 0 < (1 / 12 : ℝ) - |A i i| := sub_pos.mpr hi
  have hgj : 0 < (1 / 12 : ℝ) - |A j j| := sub_pos.mpr hj
  have hgap : 0 < ((1 / 12 : ℝ) - |A i i|) * ((1 / 12 : ℝ) - |A j j|) :=
    mul_pos hgi hgj
  have habsprod : |A i i| * |A j j| < (1 / 12 : ℝ) ^ 2 := by
    nlinarith [abs_nonneg (A i i), abs_nonneg (A j j)]
  have hprod : A i i * A j j < (1 / 12 : ℝ) ^ 2 := by
    calc
      A i i * A j j ≤ |A i i * A j j| := le_abs_self _
      _ = |A i i| * |A j j| := abs_mul _ _
      _ < (1 / 12 : ℝ) ^ 2 := habsprod
  have hdetlo : -(1 / 256 : ℝ) < A i i * A j j - A i j ^ 2 :=
    (abs_lt.mp (hp i j hij)).1
  have hsq : A i j ^ 2 < (5 / 48 : ℝ) ^ 2 := by
    norm_num at hprod hdetlo ⊢
    nlinarith
  rw [abs_lt]
  constructor <;> nlinarith [sq_nonneg (A i j)]

/-- Finite-dimensional compactness step used explicitly at paper L577:
there is a single strict off-diagonal bound a < 5/48.
The inserted zero makes the finite set nonempty even when n = 0. -/
theorem exists_uniform_offdiag_lt {n : ℕ} (A : Matrix (Fin n) (Fin n) ℝ)
    (hd : ∀ i, |A i i| < 1 / 12)
    (hp : ∀ i j, i ≠ j → |A i i * A j j - A i j ^ 2| < 1 / 256) :
    ∃ a : ℝ, 0 ≤ a ∧ a < 5 / 48 ∧ ∀ i j, i ≠ j → |A i j| ≤ a := by
  let S : Finset ℝ :=
    insert 0 (Finset.univ.image (fun p : Fin n × Fin n => |A p.1 p.2|))
  have hS : S.Nonempty := by
    refine ⟨0, ?_⟩
    simp [S]
  let a : ℝ := S.max' hS
  refine ⟨a, ?_, ?_, ?_⟩
  · exact Finset.le_max' S 0 (by simp [S])
  · rw [a, Finset.max'_lt_iff]
    intro y hy
    simp only [S, Finset.mem_insert, Finset.mem_image] at hy
    rcases hy with rfl | ⟨p, -, rfl⟩
    · norm_num
    · by_cases hij : p.1 = p.2
      · rw [hij]
        exact lt_trans (hd p.2) (by norm_num)
      · exact nopivot_entry_strict A hd hp p.1 p.2 hij
  · intro i j hij
    exact Finset.le_max' S |A i j| (by simp [S])

end QformFiveStrictDraft
