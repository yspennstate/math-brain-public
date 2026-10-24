import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas

/-!
account02/B11 WIP toward repaired Lemma 2.6 (Schur complement singular-value count).

Exact manuscript target:
  yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa
  repaired-2026-09-25/paper.tex
  blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a

This file isolates the finite-rank perturbation step in the approximation-number
language already used by lean/QformFive3.lean.

IMPORTANT: this runtime has no lean/lake executable, so this file is UNCOMPILED WIP
and must not be counted in LEAN_COVERAGE until compiled against Lean 4.29.1 /
Mathlib 5e932f97 with no sorry/admit/new axiom and #print axioms checked.
-/

open Matrix

namespace QformFiveB11

variable {κ μ : Type*} [Fintype κ] [Fintype μ]

/-- Squared Euclidean norm, matching QformFive3.lean. -/
def nsq (v : κ → ℝ) : ℝ := v ⬝ᵥ v

/-- Euclidean norm, matching QformFive3.lean. -/
noncomputable def nrm (v : κ → ℝ) : ℝ := Real.sqrt (nsq v)

/-- Rank subadditivity, copied from the compiled QformFive3 pattern. -/
theorem rank_add_le' (A B : Matrix μ κ ℝ) : (A + B).rank ≤ A.rank + B.rank := by
  unfold Matrix.rank
  rw [Matrix.mulVecLin_add]
  exact (Submodule.finrank_mono (LinearMap.range_add_le _ _)).trans
    (Submodule.finrank_add_le_finrank_add_finrank _ _)

/-- Approximation-number lower bound used throughout the existing QFORM Lean files.
This is the formal proxy for s_k(T) ≥ σ. -/
def ApproxGE (k : ℕ) (σ : ℝ) (T : Matrix μ κ ℝ) : Prop :=
  ∀ R : Matrix μ κ ℝ, R.rank < k →
    ∃ v : κ → ℝ, v ≠ 0 ∧ σ * nrm v ≤ nrm ((T - R) *ᵥ v)

/-- Lemma 2.5 finite-rank perturbation in ApproxGE form.

If the (j+q)-th approximation number of T is at least σ and rank R ≤ q,
then the j-th approximation number of T-R is at least σ.

This is the exact rank-loss step needed by the direct Schur factorization
A = U B Uᵀ + diag(0,S). -/
theorem approx_rank_sub {j q : ℕ} {σ : ℝ} {T R : Matrix μ κ ℝ}
    (hT : ApproxGE (j + q) σ T) (hR : R.rank ≤ q) :
    ApproxGE j σ (T - R) := by
  intro B hB
  have hsum : B.rank + R.rank < j + q := by omega
  have hBR : (B + R).rank < j + q :=
    lt_of_le_of_lt (rank_add_le' B R) hsum
  obtain ⟨v, hv0, hv⟩ := hT (B + R) hBR
  refine ⟨v, hv0, ?_⟩
  have heq : T - (B + R) = (T - R) - B := by
    ext i k
    simp [Matrix.sub_apply, Matrix.add_apply]
    ring
  rw [← heq]
  exact hv

#print axioms QformFiveB11.approx_rank_sub

end QformFiveB11
