import Mathlib.Tactic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.Order.Chebyshev
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.DotProduct
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
Lemma 2.5 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), for singular values in approximation-number form: `ApproxGE j σ T` says that every matrix of rank less
than `j` is at operator distance at least `σ` from `T`, which is `s_j(T) ≥ σ` by the characterization
`s_j(T) = min {‖T - B‖ : rank B < j}` with which the paper's proof begins. No symmetry is assumed.

* `approx_perturb`: `s_j(U) ≥ s_j(T) - ‖T - U‖`; applied both ways, `|s_j(T) - s_j(U)| ≤ ‖T - U‖`.
* `approx_rank_perturb`: `s_{j+q}(T + R) ≤ s_j(T)` whenever `rank R ≤ q`.
* `approx_of_compress`: `s_j(Uᵀ T V) ≤ s_j(T)` when `U` and `V` have orthonormal columns.

The norms, the rank inequality and the kernel lemma are taken over, with their proofs, from `lean/QformFive3.lean`
(Section 6), in the namespace `QformFiveB.Weyl` so that this file compiles on its own.
-/

open Matrix

namespace QformFiveB

namespace Weyl

section Norms

variable {ι κ μ : Type*} [Fintype ι] [Fintype κ] [Fintype μ]

/-- The squared Euclidean norm. -/
def nsq (v : ι → ℝ) : ℝ := v ⬝ᵥ v

/-- The Euclidean norm. -/
noncomputable def nrm (v : ι → ℝ) : ℝ := Real.sqrt (nsq v)

theorem nsq_nonneg (v : ι → ℝ) : 0 ≤ nsq v :=
  Finset.sum_nonneg (fun i _ => mul_self_nonneg (v i))

theorem nrm_nonneg (v : ι → ℝ) : 0 ≤ nrm v := Real.sqrt_nonneg _

theorem nsq_zero : nsq (0 : ι → ℝ) = 0 := by simp [nsq]

theorem nrm_sq (v : ι → ℝ) : nrm v ^ 2 = nsq v := Real.sq_sqrt (nsq_nonneg v)

theorem nrm_pos {v : ι → ℝ} (hv : v ≠ 0) : 0 < nrm v := by
  apply Real.sqrt_pos.mpr
  rcases (nsq_nonneg v).lt_or_eq with h | h
  · exact h
  · exact absurd (dotProduct_self_eq_zero.mp h.symm) hv

/-- Cauchy-Schwarz. -/
theorem dot_le_nrm (u v : ι → ℝ) : u ⬝ᵥ v ≤ nrm u * nrm v := by
  have hcs : (u ⬝ᵥ v) ^ 2 ≤ nsq u * nsq v := by
    have h := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ u v
    simpa [nsq, dotProduct, sq] using h
  have h2 : (u ⬝ᵥ v) ^ 2 ≤ (nrm u * nrm v) ^ 2 := by
    rw [mul_pow, nrm_sq, nrm_sq]; exact hcs
  have h0 : 0 ≤ nrm u * nrm v := mul_nonneg (nrm_nonneg u) (nrm_nonneg v)
  nlinarith [h2, h0]

theorem nsq_add (u v : ι → ℝ) : nsq (u + v) = nsq u + 2 * (u ⬝ᵥ v) + nsq v := by
  simp only [nsq, add_dotProduct, dotProduct_add, dotProduct_comm v u]; ring

/-- The triangle inequality. -/
theorem nrm_add_le (u v : ι → ℝ) : nrm (u + v) ≤ nrm u + nrm v := by
  have key : nsq (u + v) ≤ (nrm u + nrm v) ^ 2 := by
    rw [nsq_add, add_sq, nrm_sq, nrm_sq]
    nlinarith [dot_le_nrm u v]
  calc nrm (u + v) = Real.sqrt (nsq (u + v)) := rfl
    _ ≤ Real.sqrt ((nrm u + nrm v) ^ 2) := Real.sqrt_le_sqrt key
    _ = nrm u + nrm v := Real.sqrt_sq (add_nonneg (nrm_nonneg u) (nrm_nonneg v))

/-- The reverse triangle inequality for a difference of three vectors. -/
theorem nrm_sub_sub_ge (a b c : ι → ℝ) : nrm a - nrm b - nrm c ≤ nrm (a - b - c) := by
  have h1 := nrm_add_le (a - b - c) b
  have h2 := nrm_add_le (a - b - c + b) c
  have e : a - b - c + b + c = a := by abel
  rw [e] at h2
  linarith

theorem nsq_smul (c : ℝ) (v : ι → ℝ) : nsq (c • v) = c ^ 2 * nsq v := by
  simp only [nsq, smul_dotProduct, dotProduct_smul, smul_eq_mul]; ring

theorem nrm_smul (c : ℝ) (v : ι → ℝ) : nrm (c • v) = |c| * nrm v := by
  rw [nrm, nsq_smul, Real.sqrt_mul (sq_nonneg c), Real.sqrt_sq_eq_abs]; rfl

/-- From a bound on squared norms to a bound on norms. -/
theorem nrm_le_of_nsq_le {u : ι → ℝ} {v : κ → ℝ} {c : ℝ} (hc : 0 ≤ c) (h : nsq u ≤ c ^ 2 * nsq v) :
    nrm u ≤ c * nrm v := by
  calc nrm u = Real.sqrt (nsq u) := rfl
    _ ≤ Real.sqrt (c ^ 2 * nsq v) := Real.sqrt_le_sqrt h
    _ = c * nrm v := by rw [Real.sqrt_mul (sq_nonneg c), Real.sqrt_sq hc]; rfl

theorem nrm_ge_of_nsq_ge {u : ι → ℝ} {v : κ → ℝ} {c : ℝ} (hc : 0 ≤ c) (h : c ^ 2 * nsq u ≤ nsq v) :
    c * nrm u ≤ nrm v := by
  calc c * nrm u = Real.sqrt (c ^ 2 * nsq u) := by
        rw [Real.sqrt_mul (sq_nonneg c), Real.sqrt_sq hc]; rfl
    _ ≤ Real.sqrt (nsq v) := Real.sqrt_le_sqrt h
    _ = nrm v := rfl

/-! ## Operator bounds -/

/-- The squared Frobenius norm. -/
def frob (Q : Matrix κ μ ℝ) : ℝ := ∑ c, ∑ d, Q c d ^ 2

/-- The operator norm is at most the Frobenius norm. -/
theorem nsq_mulVec_le (Q : Matrix κ μ ℝ) (v : μ → ℝ) : nsq (Q *ᵥ v) ≤ frob Q * nsq v := by
  have h : ∀ c, (Q *ᵥ v) c * (Q *ᵥ v) c ≤ (∑ d, Q c d ^ 2) * nsq v := by
    intro c
    have hc := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ (fun d => Q c d) v
    have e1 : (Q *ᵥ v) c = ∑ d, Q c d * v d := rfl
    have e2 : nsq v = ∑ d, v d ^ 2 := by simp [nsq, dotProduct, sq]
    rw [e1, e2, ← sq]; exact hc
  calc nsq (Q *ᵥ v) = ∑ c, (Q *ᵥ v) c * (Q *ᵥ v) c := rfl
    _ ≤ ∑ c, (∑ d, Q c d ^ 2) * nsq v := Finset.sum_le_sum (fun c _ => h c)
    _ = frob Q * nsq v := by rw [frob, Finset.sum_mul]

/-- A diagonal matrix with entries of modulus at most δ has operator norm at most δ. -/
theorem nrm_diagonal_mulVec_le [DecidableEq ι] (d : ι → ℝ) (δ : ℝ) (hδ : 0 ≤ δ) (hd : ∀ i, |d i| ≤ δ)
    (w : ι → ℝ) : nrm (diagonal d *ᵥ w) ≤ δ * nrm w := by
  apply nrm_le_of_nsq_le hδ
  have h : ∀ i, (diagonal d *ᵥ w) i * (diagonal d *ᵥ w) i ≤ δ ^ 2 * (w i * w i) := by
    intro i
    rw [mulVec_diagonal]
    have h1 : d i ^ 2 ≤ δ ^ 2 := by
      rw [← sq_abs]; exact pow_le_pow_left₀ (abs_nonneg _) (hd i) 2
    nlinarith [mul_self_nonneg (w i)]
  calc nsq (diagonal d *ᵥ w) = ∑ i, (diagonal d *ᵥ w) i * (diagonal d *ᵥ w) i := rfl
    _ ≤ ∑ i, δ ^ 2 * (w i * w i) := Finset.sum_le_sum (fun i _ => h i)
    _ = δ ^ 2 * nsq w := by rw [← Finset.mul_sum]; rfl

/-- A matrix with orthonormal columns preserves norms. -/
theorem nsq_mulVec_orth [DecidableEq κ] (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (v : κ → ℝ) :
    nsq (Φ *ᵥ v) = nsq v := by
  unfold nsq
  rw [dotProduct_mulVec, ← mulVec_transpose, mulVec_mulVec, hΦ, one_mulVec]

theorem nrm_mulVec_orth [DecidableEq κ] (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (v : κ → ℝ) :
    nrm (Φ *ᵥ v) = nrm v := by
  rw [nrm, nsq_mulVec_orth Φ hΦ v]; rfl

/-- Bessel's inequality: the transpose of a matrix with orthonormal columns does not increase norms. -/
theorem nrm_transpose_mulVec_le [DecidableEq κ] (Φ : Matrix ι κ ℝ) (hΦ : Φᵀ * Φ = 1) (u : ι → ℝ) :
    nrm (Φᵀ *ᵥ u) ≤ nrm u := by
  have h1 : nsq (Φ *ᵥ (Φᵀ *ᵥ u)) = nsq (Φᵀ *ᵥ u) := nsq_mulVec_orth Φ hΦ _
  have h2 : u ⬝ᵥ (Φ *ᵥ (Φᵀ *ᵥ u)) = nsq (Φᵀ *ᵥ u) := by
    rw [dotProduct_mulVec, ← mulVec_transpose, nsq]
  have h3 : 0 ≤ nsq (u - Φ *ᵥ (Φᵀ *ᵥ u)) := nsq_nonneg _
  have h4 : nsq (u - Φ *ᵥ (Φᵀ *ᵥ u))
      = nsq u - 2 * (u ⬝ᵥ (Φ *ᵥ (Φᵀ *ᵥ u))) + nsq (Φ *ᵥ (Φᵀ *ᵥ u)) := by
    simp only [nsq, sub_dotProduct, dotProduct_sub, dotProduct_comm (Φ *ᵥ (Φᵀ *ᵥ u)) u]; ring
  have h5 : nsq (Φᵀ *ᵥ u) ≤ nsq u := by linarith
  exact Real.sqrt_le_sqrt h5

end Norms

/-! ## Rank -/

section Rank

variable {κ μ : Type*} [Fintype κ] [Fintype μ]

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

end Rank

section Approx

variable {ι κ μ : Type*} [Fintype ι] [Fintype κ] [Fintype μ]

def ApproxGE (k : ℕ) (σ : ℝ) (T : Matrix μ κ ℝ) : Prop :=
  ∀ R : Matrix μ κ ℝ, R.rank < k → ∃ v : κ → ℝ, v ≠ 0 ∧ σ * nrm v ≤ nrm ((T - R) *ᵥ v)

theorem ApproxGE.mono {k : ℕ} {σ σ' : ℝ} {T : Matrix μ κ ℝ} (h : ApproxGE k σ T) (hσ : σ' ≤ σ) :
    ApproxGE k σ' T := by
  intro R hR
  obtain ⟨v, hv0, hv⟩ := h R hR
  exact ⟨v, hv0, le_trans (mul_le_mul_of_nonneg_right hσ (nrm_nonneg v)) hv⟩

/-- **Lemma 2.5, first assertion.** If `‖(T - U) v‖ ≤ ε ‖v‖` for every `v`, then `s_j(T) ≥ σ` gives `s_j(U) ≥ σ - ε`. -/
theorem approx_perturb {j : ℕ} {σ ε : ℝ} (T U : Matrix μ κ ℝ) (hT : ApproxGE j σ T)
    (hε : ∀ v, nrm ((T - U) *ᵥ v) ≤ ε * nrm v) : ApproxGE j (σ - ε) U := by
  intro R hR
  obtain ⟨v, hv0, hv⟩ := hT R hR
  refine ⟨v, hv0, ?_⟩
  have htri : nrm ((T - R) *ᵥ v) ≤ nrm ((U - R) *ᵥ v) + nrm ((T - U) *ᵥ v) := by
    have h := nrm_add_le ((U - R) *ᵥ v) ((T - U) *ᵥ v)
    rwa [← add_mulVec, show U - R + (T - U) = T - R by abel] at h
  have h2 := hε v
  nlinarith [hv, htri, h2]

/-- **Lemma 2.5, first assertion, both ways.** If `‖(T - U) v‖ ≤ ε ‖v‖` for every `v`, then `s_j(T) ≥ σ` and `s_j(U) ≥ σ`
are each moved by at most `ε` in passing to the other matrix. -/
theorem approx_perturb_symm {j : ℕ} {σ ε : ℝ} (T U : Matrix μ κ ℝ)
    (hε : ∀ v, nrm ((T - U) *ᵥ v) ≤ ε * nrm v) :
    (ApproxGE j σ T → ApproxGE j (σ - ε) U) ∧ (ApproxGE j σ U → ApproxGE j (σ - ε) T) := by
  refine ⟨fun h => approx_perturb T U h hε, fun h => approx_perturb U T h (fun v => ?_)⟩
  have e : (U - T) *ᵥ v = -((T - U) *ᵥ v) := by rw [← neg_mulVec, neg_sub]
  rw [e]
  have hn : nrm (-((T - U) *ᵥ v)) = nrm ((T - U) *ᵥ v) := by
    unfold nrm nsq
    rw [neg_dotProduct, dotProduct_neg, neg_neg]
  rw [hn]
  exact hε v

/-- **Lemma 2.5, second assertion.** `s_{j+q}(T + R') ≤ s_j(T)` whenever `rank R' ≤ q`. -/
theorem approx_rank_perturb {j q : ℕ} {σ : ℝ} (T R' : Matrix μ κ ℝ) (hR' : R'.rank ≤ q)
    (h : ApproxGE (j + q) σ (T + R')) : ApproxGE j σ T := by
  intro R hR
  have hrank : (R + R').rank < j + q := lt_of_le_of_lt (rank_add_le' R R') (by omega)
  obtain ⟨v, hv0, hv⟩ := h (R + R') hrank
  refine ⟨v, hv0, ?_⟩
  rwa [show T + R' - (R + R') = T - R by abel] at hv

/-- **Lemma 2.5, third assertion.** If `U` and `V` have orthonormal columns, `s_j(Uᵀ T V) ≤ s_j(T)`. -/
theorem approx_of_compress {μ' κ' : Type*} [Fintype μ'] [Fintype κ'] [DecidableEq μ'] [DecidableEq κ']
    {j : ℕ} {σ : ℝ} (T : Matrix μ κ ℝ) (U : Matrix μ μ' ℝ) (V : Matrix κ κ' ℝ) (hU : Uᵀ * U = 1)
    (hV : Vᵀ * V = 1) (h : ApproxGE j σ (Uᵀ * T * V)) : ApproxGE j σ T := by
  intro R hR
  have hr : (Uᵀ * R * V).rank < j :=
    lt_of_le_of_lt ((rank_mul_le_left _ _).trans (rank_mul_le_right _ _)) hR
  obtain ⟨v, hv0, hv⟩ := h (Uᵀ * R * V) hr
  refine ⟨V *ᵥ v, ?_, ?_⟩
  · intro h0
    have h1 : nrm v = 0 := by rw [← nrm_mulVec_orth V hV v, h0]; simp [nrm, nsq]
    exact (ne_of_gt (nrm_pos hv0)) h1
  · rw [nrm_mulVec_orth V hV v]
    have e : (Uᵀ * T * V - Uᵀ * R * V) *ᵥ v = Uᵀ *ᵥ ((T - R) *ᵥ (V *ᵥ v)) := by
      rw [Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, Matrix.mul_sub, Matrix.sub_mul]
    calc σ * nrm v ≤ nrm ((Uᵀ * T * V - Uᵀ * R * V) *ᵥ v) := hv
      _ = nrm (Uᵀ *ᵥ ((T - R) *ᵥ (V *ᵥ v))) := by rw [e]
      _ ≤ nrm ((T - R) *ᵥ (V *ᵥ v)) := nrm_transpose_mulVec_le U hU _

end Approx

end Weyl

end QformFiveB
