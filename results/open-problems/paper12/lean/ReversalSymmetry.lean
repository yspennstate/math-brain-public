/-
The reversal permutation of a finite index set is a symmetric orthogonal
involution.

This file completes the permutation-matrix half of Lemma `lem:tensorrev` in
`paper12/matrix_spencer_lifts.tex`, which `TensorReversal.lean` deliberately
left out (it proved only the finite-index arithmetic, not the matrix-level
statements about `J_Λ`).

For the one-dimensional index set `{0, ..., d - 1}` the reversal
`i ↦ d - 1 - i` is the involution already studied in `TensorReversal.lean`.
Packaged as a permutation `J = revPerm`, it is the exchange/reversal matrix,
and the proof of `lem:tensorrev` uses three of its properties:

* it is its own inverse, `J⁻¹ = J` (an involution as a group element);
* its permutation matrix is **symmetric**, `Jᵀ = J`;
* hence that matrix is **orthogonal**, `Jᵀ = J⁻¹`, i.e. `Jᵀ J = 1`.

The combinatorial heart of the symmetry is the index equivalence

  `i = revIdx j  ↔  j = revIdx i`,   where `revIdx i = d - 1 - i`,

which says exactly that the `(i, j)` entry of the reversal matrix equals its
`(j, i)` entry. We prove that first, lift it to `J⁻¹ = J`, and then read off
`Jᵀ = J` and `Jᵀ = J⁻¹` from mathlib's `Matrix.transpose_permMatrix`.

The reversal involution itself (`J ∘ J = id`) is `TensorReversal.rev_involutive`,
which this file reuses verbatim.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.LinearAlgebra.Matrix.Permutation
import Mathlib.Tactic
import TensorReversal

open Equiv

namespace ReversalSymmetry

variable {d : ℕ}

/-! ### The index-level symmetry -/

/-- The reversal index map on `{0, ..., d - 1}`, i.e. `i ↦ d - 1 - i`, as used in
`TensorReversal.rev`. -/
abbrev revIdx (hd : 0 < d) (i : Fin d) : Fin d := TensorReversal.rev hd i

/-- **Index symmetry of the reversal matrix.** The `(i, j)` entry of the reversal
permutation matrix — the indicator of `i = revIdx j` — equals its `(j, i)` entry,
because `i = d - 1 - j` and `j = d - 1 - i` are the same constraint. This is the
elementary fact that makes the reversal matrix symmetric. -/
theorem revIdx_symm (hd : 0 < d) (i j : Fin d) :
    (i = revIdx hd j) ↔ (j = revIdx hd i) := by
  -- both sides say `i.val + j.val = d - 1`
  have hi : i.val < d := i.isLt
  have hj : j.val < d := j.isLt
  constructor
  · intro h
    apply Fin.ext
    have := congrArg Fin.val h
    simp only [revIdx, TensorReversal.rev_val] at this ⊢
    omega
  · intro h
    apply Fin.ext
    have := congrArg Fin.val h
    simp only [revIdx, TensorReversal.rev_val] at this ⊢
    omega

/-! ### The reversal as a permutation -/

/-- The **reversal permutation** `J` of `Fin d`, built from the involutive
reversal map `TensorReversal.rev`. As an `Equiv.Perm (Fin d)` it has
`toFun = invFun = (i ↦ d - 1 - i)`, the exchange matrix's permutation. -/
def revPerm (hd : 0 < d) : Equiv.Perm (Fin d) :=
  Function.Involutive.toPerm (TensorReversal.rev hd) (TensorReversal.rev_involutive hd)

@[simp] theorem revPerm_apply (hd : 0 < d) (i : Fin d) :
    revPerm hd i = TensorReversal.rev hd i := rfl

@[simp] theorem revPerm_apply_val (hd : 0 < d) (i : Fin d) :
    (revPerm hd i).val = d - 1 - i.val := rfl

/-- `J` is an involution as a permutation: applying it twice is the identity. -/
theorem revPerm_involutive (hd : 0 < d) :
    Function.Involutive (revPerm hd) :=
  fun i => TensorReversal.rev_involutive hd i

/-- The symmetry of `revPerm` stated directly on the permutation: `i = J j ↔ j = J i`. -/
theorem revPerm_symm_apply (hd : 0 < d) (i j : Fin d) :
    (i = revPerm hd j) ↔ (j = revPerm hd i) := by
  simpa using revIdx_symm hd i j

/-! ### Self-inverse / symmetric / orthogonal -/

/-- `J.symm = J`: the reversal equals its own inverse equivalence. -/
@[simp] theorem revPerm_symm (hd : 0 < d) : (revPerm hd).symm = revPerm hd :=
  Function.Involutive.toPerm_symm (TensorReversal.rev_involutive hd)

/-- **`J⁻¹ = J`.** The reversal is its own group inverse in `Equiv.Perm (Fin d)`
(the permutation-group statement that `J` is an involution). -/
@[simp] theorem revPerm_inv (hd : 0 < d) : (revPerm hd)⁻¹ = revPerm hd :=
  revPerm_symm hd

/-- `J * J = 1`: the same involution written multiplicatively in the symmetric
group. -/
theorem revPerm_mul_self (hd : 0 < d) : revPerm hd * revPerm hd = 1 := by
  rw [← revPerm_inv hd]; exact inv_mul_cancel (revPerm hd)

/-- **Symmetry of the reversal matrix.** Over any type `R` with `0` and `1`, the
permutation matrix of `J` is symmetric, `Jᵀ = J`. This is the matrix-level
assertion (left unproved in `TensorReversal.lean`) that the reversal `J_Λ` of
`lem:tensorrev` is a symmetric operator. -/
theorem transpose_permMatrix_revPerm (R : Type*) [Zero R] [One R] (hd : 0 < d) :
    ((revPerm hd).permMatrix R).transpose = (revPerm hd).permMatrix R := by
  rw [Matrix.transpose_permMatrix, revPerm_inv]

/-- **Orthogonality of the reversal matrix.** Its transpose equals its inverse
matrix, `Jᵀ = J⁻¹` (because `J⁻¹ = J` and the matrix is symmetric). Combined
with `Matrix.permMatrix` being a group homomorphism this gives `Jᵀ J = 1`. -/
theorem transpose_permMatrix_revPerm_eq_inv (R : Type*) [Zero R] [One R] (hd : 0 < d) :
    ((revPerm hd).permMatrix R).transpose = ((revPerm hd)⁻¹).permMatrix R := by
  rw [Matrix.transpose_permMatrix]

/-! ### Multilevel (tensor-product) reversal -/

variable {α : Type*} {dd : α → ℕ}

/-- The coordinatewise reversal of a finite box `∏_a {0, ..., dd a - 1}`, as a
permutation of the dependent product `∀ a, Fin (dd a)`. This is the tensor
product `⨂_a J` of the per-axis reversals, the permutation behind the multilevel
reversal `J_Λ`. -/
def revIndexPerm (hd : ∀ a, 0 < dd a) : Equiv.Perm (∀ a, Fin (dd a)) :=
  Function.Involutive.toPerm (TensorReversal.revIndex hd)
    (fun m => TensorReversal.revIndex_involutive hd m)

@[simp] theorem revIndexPerm_apply (hd : ∀ a, 0 < dd a) (m : ∀ a, Fin (dd a)) :
    revIndexPerm hd m = TensorReversal.revIndex hd m := rfl

/-- The multilevel reversal is its own inverse: `(⨂ J)⁻¹ = ⨂ J`. -/
@[simp] theorem revIndexPerm_inv (hd : ∀ a, 0 < dd a) :
    (revIndexPerm hd)⁻¹ = revIndexPerm hd :=
  Function.Involutive.toPerm_symm (fun m => TensorReversal.revIndex_involutive hd m)

/-- For a finite axis set, the multilevel reversal matrix is symmetric, `(⨂ J)ᵀ = ⨂ J`. -/
theorem transpose_permMatrix_revIndexPerm (R : Type*) [Zero R] [One R]
    [Fintype α] [DecidableEq α] (hd : ∀ a, 0 < dd a) :
    ((revIndexPerm hd).permMatrix R).transpose = (revIndexPerm hd).permMatrix R := by
  rw [Matrix.transpose_permMatrix, revIndexPerm_inv]

end ReversalSymmetry
