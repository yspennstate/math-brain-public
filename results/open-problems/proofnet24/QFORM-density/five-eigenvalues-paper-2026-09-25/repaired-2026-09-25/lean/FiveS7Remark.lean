import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Real.Sqrt
import Mathlib.Data.Fintype.Option
import Mathlib.Data.Fintype.Prod

/-!
Remark 7.4 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): four eigenvalues without pivots need not give a third large singular value in any off-diagonal
block.

`A` is the direct sum of two copies of `[[0, wᵀ], [w, 0]]` with `w = N^{-1/2}(1, …, 1) ∈ ℝ^N`, indexed by
`Bool × Option (Fin N)`: the copy, then `none` for the centre and `some k` for the `k`-th leaf.

* `A_symm`, `A_diag`, `A_no_pivot`: `A` is symmetric with zero diagonal, and every principal `2 × 2` minor has modulus
  at most `1/N`, so for `N > 256` there is no pivot (`η = 1/12`, `ζ = 1/256`).
* `A_mulVec_V`, `V_dot_other`, `V_centre`: the vectors `(1, ±w)` on either copy are eigenvectors with eigenvalues `±1`;
  the two for each sign have disjoint supports, so `1` and `-1` each have multiplicity at least two.
* `A_eq_W_mul_Z`, `A_rank_le`: `A = W Z` through a four-element index, so `rank A ≤ 4` and there is no other nonzero
  eigenvalue.
* `block_eq_U_mul_V`, `block_rank_le`: for every partition `I = {P}`, `J = {¬P}`, the block `A_{I,J}` factors through
  `Bool` (each copy contributes only to the row or the column of its centre), so `rank A_{I,J} ≤ 2`.
* `theta_three_eq_zero`, `E3_eq_zero`: every `Θ(T) = det(M_T M_Tᵀ)` with `|T| = 3` vanishes, so
  `E_3(A_{I,J}) = ∑_{|T| = 3} Θ(T) = 0`.
-/

open Matrix Finset

namespace QformFiveB

namespace Remark74

variable (N : ℕ)

/-- One copy of `[[0, wᵀ], [w, 0]]`; `none` is the centre. -/
noncomputable def starEntry : Option (Fin N) → Option (Fin N) → ℝ
  | none, none => 0
  | none, some _ => 1 / Real.sqrt N
  | some _, none => 1 / Real.sqrt N
  | some _, some _ => 0

/-- The direct sum of two copies. -/
noncomputable def A : Matrix (Bool × Option (Fin N)) (Bool × Option (Fin N)) ℝ :=
  Matrix.of fun p q => if p.1 = q.1 then starEntry N p.2 q.2 else 0

theorem A_apply (p q : Bool × Option (Fin N)) :
    A N p q = if p.1 = q.1 then starEntry N p.2 q.2 else 0 := rfl

theorem starEntry_comm (x y : Option (Fin N)) : starEntry N x y = starEntry N y x := by
  rcases x with _ | a <;> rcases y with _ | b <;> rfl

theorem A_symm : (A N)ᵀ = A N := by
  ext p q
  rw [transpose_apply, A_apply, A_apply]
  by_cases h : p.1 = q.1
  · rw [if_pos h.symm, if_pos h, starEntry_comm]
  · rw [if_neg (fun h' => h h'.symm), if_neg h]

theorem A_isHermitian : (A N).IsHermitian := by
  unfold Matrix.IsHermitian
  rw [conjTranspose_eq_transpose_of_trivial, A_symm]

/-- The diagonal vanishes. -/
theorem A_diag (p : Bool × Option (Fin N)) : A N p p = 0 := by
  rcases p with ⟨b, _ | a⟩ <;> simp [A_apply, starEntry]

theorem starEntry_sq_le (x y : Option (Fin N)) : starEntry N x y ^ 2 ≤ 1 / (N : ℝ) := by
  have h1 : (1 / Real.sqrt N) ^ 2 = 1 / (N : ℝ) := by
    rw [div_pow, one_pow, Real.sq_sqrt (Nat.cast_nonneg N)]
  have h0 : (0 : ℝ) ≤ 1 / (N : ℝ) := by positivity
  rcases x with _ | a <;> rcases y with _ | b
  · simp only [starEntry]; rw [zero_pow two_ne_zero]; exact h0
  · simp only [starEntry]; rw [h1]
  · simp only [starEntry]; rw [h1]
  · simp only [starEntry]; rw [zero_pow two_ne_zero]; exact h0

/-- **No pivot.** For `N > 256`: `|a_ii| < η = 1/12` and `|a_ii a_jj - a_ij²| ≤ 1/N < ζ = 1/256`. -/
theorem A_no_pivot (hN : 256 < N) :
    (∀ p, |A N p p| < 1 / 12) ∧
      (∀ p q, p ≠ q → |A N p p * A N q q - A N p q ^ 2| < 1 / 256) := by
  have hN' : (256 : ℝ) < N := by exact_mod_cast hN
  refine ⟨fun p => by rw [A_diag]; norm_num, fun p q _ => ?_⟩
  rw [A_diag, A_diag, zero_mul, zero_sub, abs_neg, abs_of_nonneg (sq_nonneg _)]
  have hle : A N p q ^ 2 ≤ 1 / (N : ℝ) := by
    rw [A_apply]
    split_ifs
    · exact starEntry_sq_le N _ _
    · rw [zero_pow two_ne_zero]; positivity
  exact lt_of_le_of_lt hle (one_div_lt_one_div_of_lt (by norm_num) hN')

/-- Row `(b, centre)` of `A u`. -/
theorem A_mulVec_centre (u : Bool × Option (Fin N) → ℝ) (b : Bool) :
    (A N *ᵥ u) (b, none) = ∑ k : Fin N, 1 / Real.sqrt N * u (b, some k) := by
  simp only [mulVec, dotProduct, Fintype.sum_prod_type, Fintype.sum_option, Fintype.sum_bool, A_apply]
  cases b <;> simp [starEntry]

/-- Row `(b, leaf a)` of `A u`. -/
theorem A_mulVec_leaf (u : Bool × Option (Fin N) → ℝ) (b : Bool) (a : Fin N) :
    (A N *ᵥ u) (b, some a) = 1 / Real.sqrt N * u (b, none) := by
  simp only [mulVec, dotProduct, Fintype.sum_prod_type, Fintype.sum_option, Fintype.sum_bool, A_apply]
  cases b <;> simp [starEntry]

/-- `(1, s w)` on one copy. -/
noncomputable def starVec (s : ℝ) : Option (Fin N) → ℝ
  | none => 1
  | some _ => s / Real.sqrt N

/-- The vector `(1, s w)` on copy `b`, zero on the other copy. -/
noncomputable def V (b : Bool) (s : ℝ) : Bool × Option (Fin N) → ℝ :=
  fun p => if p.1 = b then starVec N s p.2 else 0

theorem V_centre (b : Bool) (s : ℝ) : V N b s (b, none) = 1 := by
  simp [V, starVec]

/-- **Eigenvectors.** `A (1, s w) = s (1, s w)` on each copy when `s² = 1`. -/
theorem A_mulVec_V (hN : 0 < N) (b : Bool) (s : ℝ) (hs : s ^ 2 = 1) :
    A N *ᵥ V N b s = s • V N b s := by
  have hNr : (N : ℝ) ≠ 0 := by exact_mod_cast hN.ne'
  have hss : Real.sqrt N * Real.sqrt N = N := Real.mul_self_sqrt (Nat.cast_nonneg N)
  funext p
  rcases p with ⟨bp, _ | a⟩
  · rw [A_mulVec_centre]
    by_cases h : bp = b
    · subst h
      have hv : ∀ k : Fin N, V N bp s (bp, some k) = s / Real.sqrt N := fun k => by simp [V, starVec]
      simp only [hv, Pi.smul_apply, V_centre, smul_eq_mul, mul_one, Finset.sum_const, Finset.card_univ,
        Fintype.card_fin, nsmul_eq_mul]
      rw [div_mul_div_comm, one_mul, hss]
      field_simp
    · have hv : ∀ k : Fin N, V N b s (bp, some k) = 0 := fun k => by simp [V, h]
      have hc : V N b s (bp, none) = 0 := by simp [V, h]
      simp only [hv, mul_zero, Finset.sum_const_zero, Pi.smul_apply, hc, smul_eq_mul]
  · rw [A_mulVec_leaf]
    by_cases h : bp = b
    · subst h
      have hv : V N bp s (bp, some a) = s / Real.sqrt N := by simp [V, starVec]
      simp only [V_centre, Pi.smul_apply, hv, smul_eq_mul]
      rw [← mul_div_assoc, ← sq, hs, mul_one]
    · have hv : V N b s (bp, some a) = 0 := by simp [V, h]
      have hc : V N b s (bp, none) = 0 := by simp [V, h]
      simp only [hc, hv, mul_zero, Pi.smul_apply, smul_eq_mul]

/-- Eigenvectors on different copies are orthogonal (disjoint supports). -/
theorem V_dot_other (b b' : Bool) (hb : b ≠ b') (s s' : ℝ) : V N b s ⬝ᵥ V N b' s' = 0 := by
  simp only [dotProduct, Fintype.sum_prod_type]
  refine Finset.sum_eq_zero (fun q1 _ => Finset.sum_eq_zero (fun q2 _ => ?_))
  by_cases h1 : q1 = b
  · subst h1
    simp [V, hb]
  · simp [V, h1]

/-- The factor `W` of `A = W Z`: columns `e_{centre b}` and `A e_{centre b}`. -/
noncomputable def W : Matrix (Bool × Option (Fin N)) (Bool × Bool) ℝ :=
  Matrix.of fun p bt => if bt.2 then (if p = (bt.1, none) then 1 else 0) else A N p (bt.1, none)

/-- The factor `Z` of `A = W Z`. -/
noncomputable def Z : Matrix (Bool × Bool) (Bool × Option (Fin N)) ℝ :=
  Matrix.of fun bt q => if bt.2 then A N (bt.1, none) q else (if q = (bt.1, none) then 1 else 0)

/-- `A = ∑_b (e_{c_b} a_bᵀ + a_b e_{c_b}ᵀ) = W Z`. -/
theorem A_eq_W_mul_Z : A N = W N * Z N := by
  ext ⟨bp, xp⟩ ⟨bq, xq⟩
  simp only [mul_apply, Fintype.sum_prod_type, Fintype.sum_bool, W, Z, of_apply]
  cases bp <;> cases bq <;> rcases xp with _ | a <;> rcases xq with _ | c <;> simp [A_apply, starEntry]

/-- `rank A ≤ 4`: the eigenvalues `1, 1, -1, -1` are all the nonzero ones. -/
theorem A_rank_le : (A N).rank ≤ 4 := by
  rw [A_eq_W_mul_Z]
  calc (W N * Z N).rank ≤ (W N).rank := rank_mul_le_left _ _
    _ ≤ Fintype.card (Bool × Bool) := rank_le_card_width _
    _ = 4 := by simp

section Block

variable (P : Bool × Option (Fin N) → Prop) [DecidablePred P]

/-- The off-diagonal block `A_{I,J}` for `I = {P}`, `J = {¬P}`. -/
noncomputable def block : Matrix {x // P x} {x // ¬P x} ℝ :=
  (A N).submatrix (Subtype.val : {x // P x} → _) (Subtype.val : {x // ¬P x} → _)

/-- Left factor: a copy whose centre lies in `I` contributes the row of its centre. -/
noncomputable def U : Matrix {x // P x} Bool ℝ :=
  Matrix.of fun i b => if P (b, none) then (if (i : Bool × Option (Fin N)) = (b, none) then 1 else 0)
    else A N i (b, none)

/-- Right factor: a copy whose centre lies in `J` contributes the column of its centre. -/
noncomputable def Vb : Matrix Bool {x // ¬P x} ℝ :=
  Matrix.of fun b j => if P (b, none) then A N (b, none) j
    else (if (j : Bool × Option (Fin N)) = (b, none) then 1 else 0)

/-- `A_{I,J} = U V` through `Bool`. -/
theorem block_eq_U_mul_V : block N P = U N P * Vb N P := by
  ext i j
  have hA : block N P i j = (W N * Z N) (i : Bool × Option (Fin N)) (j : Bool × Option (Fin N)) := by
    rw [← A_eq_W_mul_Z]; rfl
  rw [hA, mul_apply, mul_apply, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl (fun b _ => ?_)
  rw [Fintype.sum_bool]
  simp only [W, Z, U, Vb, of_apply, if_true]
  by_cases hb : P (b, none)
  · have hj : ¬((j : Bool × Option (Fin N)) = (b, none)) := fun h => j.2 (h ▸ hb)
    rw [if_pos hb, if_pos hb, if_neg hj]
    simp
  · have hi : ¬((i : Bool × Option (Fin N)) = (b, none)) := fun h => hb (h ▸ i.2)
    rw [if_neg hb, if_neg hb, if_neg hi]
    simp

/-- `rank A_{I,J} ≤ 2` for every partition. -/
theorem block_rank_le : (block N P).rank ≤ 2 := by
  rw [block_eq_U_mul_V]
  calc (U N P * Vb N P).rank ≤ (U N P).rank := rank_mul_le_left _ _
    _ ≤ Fintype.card Bool := rank_le_card_width _
    _ = 2 := Fintype.card_bool

/-- `Θ(T) = det(M_T M_Tᵀ) = 0` for `|T| = 3`, `M = A_{I,J}`. -/
theorem theta_three_eq_zero (T : Finset {x // P x}) (hT : T.card = 3) :
    ((block N P).submatrix ((↑) : T → {x // P x}) id *
      ((block N P).submatrix ((↑) : T → {x // P x}) id)ᵀ).det = 0 := by
  have hrank : ((block N P).submatrix ((↑) : T → {x // P x}) id *
      ((block N P).submatrix ((↑) : T → {x // P x}) id)ᵀ).rank ≤ 2 := by
    calc ((block N P).submatrix ((↑) : T → {x // P x}) id *
          ((block N P).submatrix ((↑) : T → {x // P x}) id)ᵀ).rank
        ≤ ((block N P).submatrix ((↑) : T → {x // P x}) id).rank := rank_mul_le_left _ _
      _ ≤ (block N P).rank := rank_submatrix_le _ (Equiv.refl _) _
      _ ≤ 2 := block_rank_le N P
  by_contra hdet
  have hunit : IsUnit ((block N P).submatrix ((↑) : T → {x // P x}) id *
      ((block N P).submatrix ((↑) : T → {x // P x}) id)ᵀ) :=
    (isUnit_iff_isUnit_det _).mpr (isUnit_iff_ne_zero.mpr hdet)
  have h3 := rank_of_isUnit _ hunit
  rw [Fintype.card_coe, hT] at h3
  omega

/-- **Remark 7.4.** `E_3(A_{I,J}) = ∑_{|T| = 3} Θ(T) = 0` for every partition. -/
theorem E3_eq_zero :
    ∑ T ∈ (univ : Finset {x // P x}).powersetCard 3,
      ((block N P).submatrix ((↑) : T → {x // P x}) id *
        ((block N P).submatrix ((↑) : T → {x // P x}) id)ᵀ).det = 0 :=
  Finset.sum_eq_zero (fun T hT => theta_three_eq_zero N P T (Finset.mem_powersetCard.mp hT).2)

end Block

end Remark74

end QformFiveB
