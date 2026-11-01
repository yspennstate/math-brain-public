import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
B17 WIP for the repaired five-singular-value paper, source blob 98e45d53.

This isolates finite/logical pieces of the Section 7 assembly which are not separate
compiled theorems in FiveS7.lean: exact pivot boundary routing, the sign split of
a pair pivot, the definite/indefinite determinant algebra, exact one-/two-coordinate
Schur-count losses, scalar completion of the square with affine terms retained,
and the logical final branch assembly.

STATUS: UNCOMPILED in the fleet01/B17 runtime (Lean/lake unavailable there).
Do not count this file as verification until a matching Lean build succeeds with
no sorry/admit/new axiom and #print axioms is checked.
-/

open Matrix

namespace QformFiveB
namespace B17Pivot

noncomputable section

universe u v

def eta : ℝ := 1 / 12
def zeta : ℝ := 1 / 256

theorem eta_pos : 0 < eta := by
  norm_num [eta]

theorem zeta_pos : 0 < zeta := by
  norm_num [zeta]

variable {ι : Type u} [Fintype ι] [DecidableEq ι]

def pairDet (A : Matrix ι ι ℝ) (i j : ι) : ℝ :=
  A i i * A j j - A i j ^ 2

def HasDiagPivot (A : Matrix ι ι ℝ) : Prop :=
  ∃ i, eta ≤ |A i i|

def HasPairPivot (A : Matrix ι ι ℝ) : Prop :=
  ∃ i j, i ≠ j ∧ zeta ≤ |pairDet A i j|

def NoPivot (A : Matrix ι ι ℝ) : Prop :=
  (∀ i, |A i i| < eta) ∧
    ∀ i j, i ≠ j → |pairDet A i j| < zeta

def HasDefinitePair (A : Matrix ι ι ℝ) : Prop :=
  ∃ i j, i ≠ j ∧ zeta ≤ pairDet A i j

def HasIndefinitePair (A : Matrix ι ι ℝ) : Prop :=
  ∃ i j, i ≠ j ∧ pairDet A i j ≤ -zeta

theorem diag_boundary_is_pivot (A : Matrix ι ι ℝ) (i : ι)
    (h : |A i i| = eta) : HasDiagPivot A := by
  exact ⟨i, h.ge⟩

theorem pair_boundary_is_pivot (A : Matrix ι ι ℝ) (i j : ι) (hij : i ≠ j)
    (h : |pairDet A i j| = zeta) : HasPairPivot A := by
  exact ⟨i, j, hij, h.ge⟩

theorem noPivot_diag_strict (A : Matrix ι ι ℝ) (h : NoPivot A) (i : ι) :
    |A i i| < eta := h.1 i

theorem noPivot_pair_strict (A : Matrix ι ι ℝ) (h : NoPivot A) (i j : ι)
    (hij : i ≠ j) : |pairDet A i j| < zeta := h.2 i j hij

/-- A pair pivot lands in exactly one of the determinant-sign branches used in
the proof.  Equality |det| = zeta stays in a pivot branch. -/
theorem pair_pivot_sign (A : Matrix ι ι ℝ) :
    HasPairPivot A → HasDefinitePair A ∨ HasIndefinitePair A := by
  rintro ⟨i, j, hij, hp⟩
  by_cases hd : 0 ≤ pairDet A i j
  · left
    refine ⟨i, j, hij, ?_⟩
    simpa [abs_of_nonneg hd] using hp
  · right
    have hdlt : pairDet A i j < 0 := lt_of_not_ge hd
    have hz : zeta ≤ -(pairDet A i j) := by
      simpa [abs_of_neg hdlt] using hp
    exact ⟨i, j, hij, by linarith⟩

/-- Exact exhaustive routing of the normalized proof. -/
theorem pivot_exhaustive (A : Matrix ι ι ℝ) :
    NoPivot A ∨ HasDiagPivot A ∨ HasDefinitePair A ∨ HasIndefinitePair A := by
  by_cases hd : HasDiagPivot A
  · exact Or.inr (Or.inl hd)
  by_cases hp : HasPairPivot A
  · rcases pair_pivot_sign A hp with hdef | hind
    · exact Or.inr (Or.inr (Or.inl hdef))
    · exact Or.inr (Or.inr (Or.inr hind))
  · left
    constructor
    · intro i
      have hnot : ¬ eta ≤ |A i i| := by
        intro hi
        exact hd ⟨i, hi⟩
      exact lt_of_not_ge hnot
    · intro i j hij
      have hnot : ¬ zeta ≤ |pairDet A i j| := by
        intro hpij
        exact hp ⟨i, j, hij, hpij⟩
      exact lt_of_not_ge hnot

/-- Positive determinant at a pair pivot forces the two diagonal entries to
have the same nonzero sign.  For a symmetric 2x2 block this is the algebraic
certificate that the block is definite. -/
theorem definite_pair_same_sign (A : Matrix ι ι ℝ) (i j : ι)
    (h : zeta ≤ pairDet A i j) :
    (0 < A i i ∧ 0 < A j j) ∨ (A i i < 0 ∧ A j j < 0) := by
  have hd : 0 < pairDet A i j := lt_of_lt_of_le zeta_pos h
  have hs : 0 ≤ A i j ^ 2 := sq_nonneg (A i j)
  have hp : 0 < A i i * A j j := by
    dsimp [pairDet] at hd
    nlinarith
  exact (mul_pos_iff.mp hp)

/-- In the indefinite branch, D = a_ij^2 - a_ii a_jj is at least zeta. -/
theorem indefinite_pair_D (A : Matrix ι ι ℝ) (i j : ι)
    (h : pairDet A i j ≤ -zeta) :
    zeta ≤ A i j ^ 2 - A i i * A j j := by
  dsimp [pairDet] at h
  linarith

/-- Five large directions lose at most one under a scalar Schur complement. -/
theorem schur_loss_one_from_five {Nfull Nschur : ℕ}
    (hfull : 5 ≤ Nfull) (hcount : Nfull ≤ Nschur + 1) : 4 ≤ Nschur := by
  omega

/-- The s3 half-potential scalar branch retains two large directions. -/
theorem schur_loss_one_from_three {Nfull Nschur : ℕ}
    (hfull : 3 ≤ Nfull) (hcount : Nfull ≤ Nschur + 1) : 2 ≤ Nschur := by
  omega

/-- Five large directions lose at most two under a pair Schur complement. -/
theorem schur_loss_two_from_five {Nfull Nschur : ℕ}
    (hfull : 5 ≤ Nfull) (hcount : Nfull ≤ Nschur + 2) : 3 ≤ Nschur := by
  omega

theorem four_implies_three {N : ℕ} (h : 4 ≤ N) : 3 ≤ N := by
  omega

/-- Scalar completion of the square with the residual affine/quadratic term
retained exactly. -/
theorem complete_square (a ell r x : ℝ) (ha : a ≠ 0) :
    a * x ^ 2 + ell * x + r =
      a * (x - (-ell / (2 * a))) ^ 2 + (r - ell ^ 2 / (4 * a)) := by
  field_simp [ha]
  ring

/-- Pointwise family form used when ell and r depend on untouched coordinates. -/
theorem complete_square_family {α : Type v} (a : ℝ) (ha : a ≠ 0)
    (ell r : α → ℝ) (x : ℝ) (y : α) :
    a * x ^ 2 + ell y * x + r y =
      a * (x - (-ell y / (2 * a))) ^ 2 +
        (r y - (ell y) ^ 2 / (4 * a)) := by
  exact complete_square a (ell y) (r y) x ha

/-- Logical endgame once the four analytic branch bounds are supplied. -/
theorem final_bound_from_branches (A : Matrix ι ι ℝ) (M : ℝ)
    (hNo : NoPivot A → M < 167)
    (hDiag : HasDiagPivot A → M < 267)
    (hDef : HasDefinitePair A → M < 51)
    (hIndef : HasIndefinitePair A → M < 269) :
    M < 270 := by
  rcases pivot_exhaustive A with hnp | hrest
  · linarith [hNo hnp]
  · rcases hrest with hd | hrest
    · linarith [hDiag hd]
    · rcases hrest with hdef | hind
      · linarith [hDef hdef]
      · linarith [hIndef hind]

end
end B17Pivot
end QformFiveB
