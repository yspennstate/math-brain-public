import Mathlib.Tactic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.DotProduct
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Matrix.Block
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Real.StarOrdered

/-!
Lemma 2.6 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): for a real symmetric `A = [[B, C], [Cᵀ, D]]` with `B` (`k × k`) invertible and
`S = D - Cᵀ B⁻¹ C`, `N_S(t) ≥ N_A(t) - k` for every `t > 0`, where `N_M(t)` counts the eigenvalues of `M`, with
multiplicity, of modulus at least `t`.

The proof here does not use `A⁻¹`, interlacing or the perturbation step of the paper. Take the `N = N_A(t)`
orthonormal eigenvectors `Φ` of `A` with eigenvalues of modulus at least `t`. For a vector `a` with
`(A Φ a)_top = B x + C y = 0` (where `Φ a = (x, y)`) one has `x = -B⁻¹ C y` and `A Φ a = (0, S y)`, so
`‖S y‖ = ‖A Φ a‖ ≥ t ‖a‖ ≥ t ‖y‖`, and `y ≠ 0` unless `a = 0`. Adding the conditions `R y = 0` for a matrix `R` of
rank less than `N - k` leaves a nonzero `a`, so `s_{N-k}(S) ≥ t` in the approximation-number form (`schur_sqapprox`);
`card_abs_eig_of_sqapprox` turns that into `N - k` eigenvalues of `S` of modulus at least `t`.

`nsq`, `exists_ker`, `rank_add_le'`, `incl1`, `incl2`, `eigU_*` and `eigenframe` are taken over, with their proofs,
from `lean/QformFive3.lean` (Section 6), so that this file compiles on its own.
-/

open Matrix Finset

namespace QformFiveB

section Toolkit

variable {ι κ μ : Type*} [Fintype ι] [Fintype κ] [Fintype μ]

/-- The squared Euclidean norm. -/
def nsq (v : ι → ℝ) : ℝ := v ⬝ᵥ v

theorem nsq_nonneg (v : ι → ℝ) : 0 ≤ nsq v :=
  Finset.sum_nonneg (fun i _ => mul_self_nonneg (v i))

theorem nsq_zero : nsq (0 : ι → ℝ) = 0 := by simp [nsq]

theorem nsq_elim (u : ι → ℝ) (v : κ → ℝ) : nsq (Sum.elim u v) = nsq u + nsq v := by
  simp [nsq, dotProduct, Fintype.sum_sum_type]

/-- A matrix with orthonormal columns preserves norms. -/
theorem nsq_mulVec_orth [DecidableEq κ] (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (v : κ → ℝ) :
    nsq (Φ *ᵥ v) = nsq v := by
  unfold nsq
  rw [dotProduct_mulVec, ← mulVec_transpose, mulVec_mulVec, hΦ, one_mulVec]

/-- The rank of a sum is at most the sum of the ranks. -/
theorem rank_add_le' (A B : Matrix μ κ ℝ) : (A + B).rank ≤ A.rank + B.rank := by
  unfold Matrix.rank
  rw [Matrix.mulVecLin_add]
  exact (Submodule.finrank_mono (LinearMap.range_add_le _ _)).trans
    (Submodule.finrank_add_le_finrank_add_finrank _ _)

/-- A matrix of rank less than the number of its columns has a nonzero kernel vector. -/
theorem exists_ker (R : Matrix μ κ ℝ) (h : R.rank < Fintype.card κ) :
    ∃ v : κ → ℝ, v ≠ 0 ∧ R *ᵥ v = 0 := by
  have hrn := LinearMap.finrank_range_add_finrank_ker (Matrix.mulVecLin R)
  rw [Module.finrank_fintype_fun_eq_card] at hrn
  have hr : R.rank = Module.finrank ℝ (LinearMap.range R.mulVecLin) := rfl
  have hpos : 0 < Module.finrank ℝ (LinearMap.ker R.mulVecLin) := by omega
  have hne : LinearMap.ker R.mulVecLin ≠ ⊥ := by
    intro hb
    rw [hb, finrank_bot] at hpos
    exact lt_irrefl _ hpos
  obtain ⟨v, hv, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hne
  exact ⟨v, hv0, by simpa using hv⟩

/-- Inclusion of the first summand. -/
def incl1 (I J : Type*) [DecidableEq I] [DecidableEq J] : Matrix (I ⊕ J) I ℝ :=
  Matrix.of fun a i => if a = Sum.inl i then 1 else 0

/-- Inclusion of the second summand. -/
def incl2 (I J : Type*) [DecidableEq I] [DecidableEq J] : Matrix (I ⊕ J) J ℝ :=
  Matrix.of fun a j => if a = Sum.inr j then 1 else 0

/-- `incl1 u + incl2 w = 0` forces `u = 0` and `w = 0`. -/
theorem incl_split [DecidableEq ι] [DecidableEq κ] (u : ι → ℝ) (w : κ → ℝ)
    (h : incl1 ι κ *ᵥ u + incl2 ι κ *ᵥ w = 0) : u = 0 ∧ w = 0 := by
  constructor
  · funext i
    have := congrFun h (Sum.inl i)
    simpa [incl1, incl2, Matrix.mulVec, dotProduct, ite_mul] using this
  · funext j
    have := congrFun h (Sum.inr j)
    simpa [incl1, incl2, Matrix.mulVec, dotProduct, ite_mul] using this

end Toolkit

section Spectral

variable {n : Type*} [Fintype n] [DecidableEq n]

theorem real_star_eq_transpose (M : Matrix n n ℝ) : star M = Mᵀ := by
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_eq_transpose_of_trivial]

theorem eigU_orth (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ * (hA.eigenvectorUnitary : Matrix n n ℝ) = 1 := by
  have h := Unitary.coe_star_mul_self hA.eigenvectorUnitary
  rw [real_star_eq_transpose] at h
  exact h

theorem eigU_orth' (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ) * (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ = 1 := by
  have h := Unitary.coe_mul_star_self hA.eigenvectorUnitary
  rw [Unitary.coe_star, real_star_eq_transpose] at h
  exact h

/-- The spectral theorem in the form `A U = U diag(λ)`. -/
theorem eigU_eigen (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    A * (hA.eigenvectorUnitary : Matrix n n ℝ)
      = (hA.eigenvectorUnitary : Matrix n n ℝ) * diagonal hA.eigenvalues := by
  ext i j
  have h := congrFun (hA.mulVec_eigenvectorBasis j) i
  simp only [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul] at h
  rw [Matrix.mul_diagonal, Matrix.mul_apply]
  simp only [IsHermitian.eigenvectorUnitary_apply]
  rw [h, mul_comm]

/-- `k` eigenvalues of modulus at least `t` give `k` orthonormal eigenvectors. -/
theorem eigenframe (A : Matrix n n ℝ) (hA : A.IsHermitian) (k : ℕ) (t : ℝ)
    (hk : k ≤ Fintype.card {j // t ≤ |hA.eigenvalues j|}) :
    ∃ (Φ : Matrix n (Fin k) ℝ) (lam : Fin k → ℝ),
      Φᵀ * Φ = 1 ∧ A * Φ = Φ * diagonal lam ∧ ∀ c, t ≤ |lam c| := by
  obtain ⟨f⟩ : Nonempty (Fin k ↪ {j // t ≤ |hA.eigenvalues j|}) :=
    Function.Embedding.nonempty_of_card_le (by simpa using hk)
  obtain ⟨emb, hemb, hS⟩ : ∃ emb : Fin k → n, Function.Injective emb ∧ ∀ c, t ≤ |hA.eigenvalues (emb c)| :=
    ⟨fun c => (f c).val, Subtype.val_injective.comp f.injective, fun c => (f c).property⟩
  refine ⟨(hA.eigenvectorUnitary : Matrix n n ℝ).submatrix id emb, hA.eigenvalues ∘ emb, ?_, ?_, ?_⟩
  · ext c d
    have h := congrFun (congrFun (eigU_orth A hA) (emb c)) (emb d)
    simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.submatrix_apply, id_eq] at h ⊢
    rw [h]
    simp [Matrix.one_apply, hemb.eq_iff]
  · ext i c
    have h := congrFun (congrFun (eigU_eigen A hA) i) (emb c)
    rw [Matrix.mul_diagonal, Matrix.mul_apply] at h
    rw [Matrix.mul_diagonal, Matrix.mul_apply]
    simp only [Matrix.submatrix_apply, id_eq, Function.comp_apply]
    exact h
  · intro c
    exact hS c

/-- `s_d(S) ≥ t`, as an approximation number and in squared form: every `R` of rank less than `d` leaves a nonzero
`v` with `t² ‖v‖² ≤ ‖(S - R) v‖²`. -/
def SqApprox (d : ℕ) (t : ℝ) (S : Matrix n n ℝ) : Prop :=
  ∀ R : Matrix n n ℝ, R.rank < d → ∃ v : n → ℝ, v ≠ 0 ∧ t ^ 2 * nsq v ≤ nsq ((S - R) *ᵥ v)

/-- For a real symmetric `S`, `s_d(S) ≥ t > 0` in the approximation-number form gives at least `d` eigenvalues of
modulus at least `t` (the symmetric counterpart of `card_eig_of_approx` in `lean/QformFive3.lean`). -/
theorem card_abs_eig_of_sqapprox (S : Matrix n n ℝ) (hS : S.IsHermitian) (d : ℕ) (t : ℝ) (ht : 0 < t)
    (h : SqApprox d t S) : d ≤ Fintype.card {i // t ≤ |hS.eigenvalues i|} := by
  by_contra hlt
  push_neg at hlt
  obtain ⟨U, hUU, hUU', hSU⟩ : ∃ U : Matrix n n ℝ,
      Uᵀ * U = 1 ∧ U * Uᵀ = 1 ∧ S * U = U * diagonal hS.eigenvalues :=
    ⟨_, eigU_orth _ hS, eigU_orth' _ hS, eigU_eigen _ hS⟩
  obtain ⟨μ, hμ⟩ : ∃ μ : n → ℝ, μ = hS.eigenvalues := ⟨_, rfl⟩
  rw [← hμ] at hSU hlt
  obtain ⟨s, hs⟩ : ∃ s : n → ℝ, s = fun i => if t ≤ |μ i| then 1 else 0 := ⟨_, rfl⟩
  have hrankP : (S * (U * diagonal s * Uᵀ)).rank < d := by
    have h1 : (S * (U * diagonal s * Uᵀ)).rank ≤ (diagonal s).rank :=
      (rank_mul_le_right _ _).trans ((rank_mul_le_left _ _).trans (rank_mul_le_right _ _))
    have h2 : (diagonal s).rank = Fintype.card {i // s i ≠ 0} := Matrix.rank_diagonal s
    have h3 : Fintype.card {i // s i ≠ 0} = Fintype.card {i // t ≤ |μ i|} := by
      apply Fintype.card_congr
      refine Equiv.subtypeEquivRight (fun i => ?_)
      rw [hs]
      by_cases hi : t ≤ |μ i| <;> simp [hi]
    omega
  obtain ⟨v, hv0, hv⟩ := h (S * (U * diagonal s * Uᵀ)) hrankP
  obtain ⟨y, hy⟩ : ∃ y : n → ℝ, y = Uᵀ *ᵥ v := ⟨_, rfl⟩
  obtain ⟨z, hz⟩ : ∃ z : n → ℝ, z = diagonal (fun i => 1 - s i) *ᵥ y := ⟨_, rfl⟩
  have hvU : U *ᵥ y = v := by rw [hy, mulVec_mulVec, hUU', one_mulVec]
  have hmat : S - S * (U * diagonal s * Uᵀ) = S * U * diagonal (fun i => 1 - s i) * Uᵀ := by
    have hd : diagonal (fun i => 1 - s i) = 1 - diagonal s := by
      ext i j
      by_cases hij : i = j
      · subst hij; simp
      · simp [Matrix.one_apply, hij]
    rw [hd, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one]
    simp only [Matrix.mul_assoc, hUU', Matrix.mul_one]
  have hvec : (S - S * (U * diagonal s * Uᵀ)) *ᵥ v = S *ᵥ (U *ᵥ z) := by
    rw [hmat, ← mulVec_mulVec, ← mulVec_mulVec, ← mulVec_mulVec, ← hy, ← hz]
  have hB : nsq (S *ᵥ (U *ᵥ z)) = ∑ i, (μ i * z i) * (μ i * z i) := by
    rw [mulVec_mulVec, hSU, ← mulVec_mulVec, nsq_mulVec_orth U hUU]
    simp only [nsq, dotProduct, mulVec_diagonal]
  have hC : nsq v = ∑ i, y i * y i := by
    rw [← hvU, nsq_mulVec_orth U hUU y]; rfl
  have hzi : ∀ i, z i = (1 - s i) * y i := by
    intro i; rw [hz, mulVec_diagonal]
  have hterm : ∀ i, 0 ≤ t ^ 2 * (y i * y i) - (μ i * z i) * (μ i * z i) := by
    intro i
    rw [hzi i, hs]
    by_cases hi : t ≤ |μ i|
    · simp only [if_pos hi]
      nlinarith [mul_self_nonneg (y i), sq_nonneg t]
    · simp only [if_neg hi]
      push_neg at hi
      have h1 := mul_self_lt_mul_self (abs_nonneg (μ i)) hi
      rw [abs_mul_abs_self] at h1
      nlinarith [mul_nonneg (sub_nonneg.mpr h1.le) (mul_self_nonneg (y i))]
  have hy0 : y ≠ 0 := by
    intro h0
    apply hv0
    rw [← hvU, h0, mulVec_zero]
  obtain ⟨j0, hj0⟩ : ∃ j, y j ≠ 0 := by
    by_contra hc
    push_neg at hc
    exact hy0 (funext hc)
  have hpos : 0 < t ^ 2 * (y j0 * y j0) - (μ j0 * z j0) * (μ j0 * z j0) := by
    rw [hzi j0, hs]
    have hyy : 0 < y j0 * y j0 := mul_self_pos.mpr hj0
    by_cases hi : t ≤ |μ j0|
    · simp only [if_pos hi]
      nlinarith [mul_pos (pow_pos ht 2) hyy]
    · simp only [if_neg hi]
      push_neg at hi
      have h1 := mul_self_lt_mul_self (abs_nonneg (μ j0)) hi
      rw [abs_mul_abs_self] at h1
      nlinarith [mul_pos (sub_pos.mpr h1) hyy]
  have hsum : 0 < ∑ i, (t ^ 2 * (y i * y i) - (μ i * z i) * (μ i * z i)) :=
    Finset.sum_pos' (fun i _ => hterm i) ⟨j0, Finset.mem_univ _, hpos⟩
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum] at hsum
  rw [hvec, hB, hC] at hv
  linarith

end Spectral

section Schur

variable {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq ι] [DecidableEq κ]

/-- The core of Lemma 2.6: with `N = N_A(t)`, `s_{N-k}(S) ≥ t` in the approximation-number form. -/
theorem schur_sqapprox (B : Matrix ι ι ℝ) (C : Matrix ι κ ℝ) (D : Matrix κ κ ℝ) (hB : IsUnit B.det)
    (hA : (fromBlocks B C Cᵀ D).IsHermitian) (t : ℝ) (ht : 0 < t) :
    SqApprox (Fintype.card {j // t ≤ |hA.eigenvalues j|} - Fintype.card ι) t (D - Cᵀ * B⁻¹ * C) := by
  obtain ⟨N, hN⟩ : ∃ N, Fintype.card {j // t ≤ |hA.eigenvalues j|} = N := ⟨_, rfl⟩
  rw [hN]
  obtain ⟨Φ, lam, hΦ, hAΦ, hlam⟩ := eigenframe (fromBlocks B C Cᵀ D) hA N t hN.symm.le
  intro R hR
  set X : Matrix ι (Fin N) ℝ := Φ.submatrix Sum.inl id with hX
  set Y : Matrix κ (Fin N) ℝ := Φ.submatrix Sum.inr id with hY
  have hrank : (incl1 ι κ * (B * X + C * Y) + incl2 ι κ * (R * Y)).rank < Fintype.card (Fin N) := by
    have h1 : (incl1 ι κ * (B * X + C * Y)).rank ≤ Fintype.card ι :=
      (Matrix.rank_mul_le_right _ _).trans (Matrix.rank_le_card_height _)
    have h2 : (incl2 ι κ * (R * Y)).rank ≤ R.rank :=
      (Matrix.rank_mul_le_right _ _).trans (Matrix.rank_mul_le_left _ _)
    have h3 := rank_add_le' (incl1 ι κ * (B * X + C * Y)) (incl2 ι κ * (R * Y))
    rw [Fintype.card_fin]
    omega
  obtain ⟨a, ha0, hTa⟩ := exists_ker _ hrank
  have hTa' : incl1 ι κ *ᵥ ((B * X + C * Y) *ᵥ a) + incl2 ι κ *ᵥ ((R * Y) *ᵥ a) = 0 := by
    rw [mulVec_mulVec, mulVec_mulVec, ← add_mulVec]; exact hTa
  obtain ⟨htop, hbot⟩ := incl_split _ _ hTa'
  obtain ⟨x, hxdef⟩ : ∃ x : ι → ℝ, x = X *ᵥ a := ⟨_, rfl⟩
  obtain ⟨y, hydef⟩ : ∃ y : κ → ℝ, y = Y *ᵥ a := ⟨_, rfl⟩
  have htop' : B *ᵥ x + C *ᵥ y = 0 := by
    rw [hxdef, hydef, mulVec_mulVec, mulVec_mulVec, ← add_mulVec]; exact htop
  have hbot' : R *ᵥ y = 0 := by
    rw [hydef, mulVec_mulVec]; exact hbot
  -- x = -B⁻¹ C y
  have hxeq : x = -((B⁻¹ * C) *ᵥ y) := by
    have h1 : B *ᵥ x = -(C *ᵥ y) := eq_neg_of_add_eq_zero_left htop'
    calc x = (B⁻¹ * B) *ᵥ x := by rw [Matrix.nonsing_inv_mul B hB, one_mulVec]
      _ = B⁻¹ *ᵥ (B *ᵥ x) := by rw [mulVec_mulVec]
      _ = -((B⁻¹ * C) *ᵥ y) := by rw [h1, Matrix.mulVec_neg, mulVec_mulVec]
  have hbotS : Cᵀ *ᵥ x + D *ᵥ y = (D - Cᵀ * B⁻¹ * C) *ᵥ y := by
    rw [hxeq, Matrix.mulVec_neg, mulVec_mulVec, sub_mulVec, Matrix.mul_assoc]
    abel
  have hphi : Φ *ᵥ a = Sum.elim x y := by
    funext r
    rcases r with i | j
    · rw [hxdef]; rfl
    · rw [hydef]; rfl
  have hAv : fromBlocks B C Cᵀ D *ᵥ (Φ *ᵥ a) = Sum.elim (0 : ι → ℝ) ((D - Cᵀ * B⁻¹ * C) *ᵥ y) := by
    rw [hphi, fromBlocks_mulVec]
    simp only [Sum.elim_comp_inl, Sum.elim_comp_inr]
    rw [htop', hbotS]
  -- ‖A Φ a‖² ≥ t² ‖a‖²
  have hstretch : t ^ 2 * nsq a ≤ nsq (fromBlocks B C Cᵀ D *ᵥ (Φ *ᵥ a)) := by
    rw [mulVec_mulVec, hAΦ, ← mulVec_mulVec, nsq_mulVec_orth Φ hΦ]
    simp only [nsq, dotProduct, mulVec_diagonal]
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro c _
    have h1 := mul_self_le_mul_self ht.le (hlam c)
    rw [abs_mul_abs_self] at h1
    nlinarith [mul_self_nonneg (a c)]
  have hnorm : nsq y ≤ nsq a := by
    have h1 : nsq (Φ *ᵥ a) = nsq a := nsq_mulVec_orth Φ hΦ a
    rw [hphi, nsq_elim] at h1
    linarith [nsq_nonneg x]
  have hSy : t ^ 2 * nsq y ≤ nsq ((D - Cᵀ * B⁻¹ * C - R) *ᵥ y) := by
    have e : (D - Cᵀ * B⁻¹ * C - R) *ᵥ y = (D - Cᵀ * B⁻¹ * C) *ᵥ y := by
      rw [sub_mulVec, hbot', sub_zero]
    rw [e]
    have h2 := hstretch
    rw [hAv, nsq_elim, nsq_zero, zero_add] at h2
    have h3 : t ^ 2 * nsq y ≤ t ^ 2 * nsq a := mul_le_mul_of_nonneg_left hnorm (by positivity)
    linarith
  have hy0 : y ≠ 0 := by
    intro hy
    have hx0 : x = 0 := by rw [hxeq, hy, mulVec_zero, neg_zero]
    have hphi0 : Φ *ᵥ a = 0 := by
      rw [hphi, hx0, hy]; funext r; rcases r with i | j <;> rfl
    have h1 : nsq a = 0 := by rw [← nsq_mulVec_orth Φ hΦ a, hphi0, nsq_zero]
    exact ha0 (dotProduct_self_eq_zero.mp h1)
  exact ⟨y, hy0, hSy⟩

/-- **Lemma 2.6.** For a real symmetric `A = [[B, C], [Cᵀ, D]]` with `B` invertible and `S = D - Cᵀ B⁻¹ C`,
`N_A(t) ≤ N_S(t) + k` for every `t > 0`, `k` the size of `B`. -/
theorem schur_count (B : Matrix ι ι ℝ) (C : Matrix ι κ ℝ) (D : Matrix κ κ ℝ) (hB : IsUnit B.det)
    (hA : (fromBlocks B C Cᵀ D).IsHermitian) (hS : (D - Cᵀ * B⁻¹ * C).IsHermitian) (t : ℝ) (ht : 0 < t) :
    Fintype.card {j // t ≤ |hA.eigenvalues j|}
      ≤ Fintype.card {j // t ≤ |hS.eigenvalues j|} + Fintype.card ι := by
  have h := card_abs_eig_of_sqapprox (D - Cᵀ * B⁻¹ * C) hS _ t ht (schur_sqapprox B C D hB hA t ht)
  omega

/-- The Schur complement of a real symmetric block matrix is symmetric, so `hS` in `schur_count` always holds. -/
theorem schur_isHermitian (B : Matrix ι ι ℝ) (C : Matrix ι κ ℝ) (D : Matrix κ κ ℝ)
    (hA : (fromBlocks B C Cᵀ D).IsHermitian) : (D - Cᵀ * B⁻¹ * C).IsHermitian := by
  have hBt : Bᵀ = B := by
    have := congrArg (fun M => M.toBlocks₁₁) hA
    simpa [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial, Matrix.fromBlocks_transpose] using this
  have hDt : Dᵀ = D := by
    have := congrArg (fun M => M.toBlocks₂₂) hA
    simpa [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial, Matrix.fromBlocks_transpose] using this
  unfold Matrix.IsHermitian
  rw [Matrix.conjTranspose_eq_transpose_of_trivial, Matrix.transpose_sub, Matrix.transpose_mul,
    Matrix.transpose_mul, Matrix.transpose_transpose, Matrix.transpose_nonsing_inv, hBt, hDt, Matrix.mul_assoc]

/-- **Lemma 2.6**, with the symmetry of the Schur complement derived. -/
theorem schur_count' (B : Matrix ι ι ℝ) (C : Matrix ι κ ℝ) (D : Matrix κ κ ℝ) (hB : IsUnit B.det)
    (hA : (fromBlocks B C Cᵀ D).IsHermitian) (t : ℝ) (ht : 0 < t) :
    Fintype.card {j // t ≤ |hA.eigenvalues j|}
      ≤ Fintype.card {j // t ≤ |(schur_isHermitian B C D hA).eigenvalues j|} + Fintype.card ι :=
  schur_count B C D hB hA (schur_isHermitian B C D hA) t ht

end Schur

end QformFiveB
