/-
Tensor-product reversal index arithmetic for multilevel Hankel matrices.

This file formalizes the elementary indexing step behind Lemma `lem:tensorrev`
in `paper12/matrix_spencer_lifts.tex`.

For a one-dimensional index set `{0, ..., d-1}`, reversal sends `j` to
`d - 1 - j`. Thus a Hankel block depending on the sum `i + j` becomes, after
right multiplication by reversal, a block depending on

  `i + (d - 1 - j) = (d - 1) + (i - j)`,

which is a Toeplitz difference index up to the fixed offset `d - 1`. The
multilevel statement is just this identity coordinate by coordinate.

The file intentionally proves only the finite-index arithmetic, not matrix
operator-norm facts about permutation matrices.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

namespace TensorReversal

/-- Reversal of the finite interval `{0, ..., d - 1}`. -/
def rev {d : Nat} (_hd : 0 < d) (i : Fin d) : Fin d :=
  { val := d - 1 - i.val
    isLt := by
      have hi : i.val < d := i.isLt
      omega }

@[simp] theorem rev_val {d : Nat} (hd : 0 < d) (i : Fin d) :
    (rev hd i).val = d - 1 - i.val := rfl

/-- Reversal is an involution. -/
theorem rev_involutive {d : Nat} (hd : 0 < d) (i : Fin d) :
    rev hd (rev hd i) = i := by
  ext
  have hi : i.val < d := i.isLt
  simp [rev]
  omega

/-- The index identity turning a Hankel sum index into a Toeplitz difference
index after right multiplication by the reversal. -/
theorem hankel_to_toeplitz_index {d : Nat} (hd : 0 < d) (i j : Fin d) :
    ((i.val : Int) + ((rev hd j).val : Int)) =
      ((d : Int) - 1) + ((i.val : Int) - (j.val : Int)) := by
  have hj : j.val < d := j.isLt
  simp [rev]
  omega

/-- The centered anti-diagonal for a one-dimensional Hankel matrix. -/
def center (d : Nat) : Int := (d : Int) - 1

/-- Integer Toeplitz lag. -/
def lag (i j : Nat) : Int := (i : Int) - (j : Int)

/-- A Toeplitz lag lies in half-bandwidth `w`. -/
def lagInBand (w : Nat) (k : Int) : Prop :=
  And (-(w : Int) <= k) (k <= (w : Int))

/-- A Hankel coefficient index lies in the centered anti-diagonal band with
half-bandwidth `w`. -/
def centeredHankelBand (d w : Nat) (k : Int) : Prop :=
  And (center d - (w : Int) <= center d + k)
    (center d + k <= center d + (w : Int))

/-- Centered Hankel bandedness is exactly Toeplitz lag bandedness after
subtracting the anti-diagonal center. -/
theorem centeredHankelBand_iff_lagInBand {d w : Nat} {k : Int} :
    centeredHankelBand d w k <-> lagInBand w k := by
  unfold centeredHankelBand lagInBand center
  constructor
  next =>
    intro h
    constructor <;> omega
  next =>
    intro h
    constructor <;> omega

/-- Coordinatewise tensor-product reversal on a finite box. -/
def revIndex {alpha : Type*} {d : alpha -> Nat} (hd : forall a, 0 < d a)
    (m : forall a, Fin (d a)) : forall a, Fin (d a) :=
  fun a => rev (hd a) (m a)

/-- Tensor-product reversal is an involution. -/
theorem revIndex_involutive {alpha : Type*} {d : alpha -> Nat}
    (hd : forall a, 0 < d a) (m : forall a, Fin (d a)) :
    revIndex hd (revIndex hd m) = m := by
  funext a
  exact rev_involutive (hd a) (m a)

/-- The multilevel Hankel-to-Toeplitz index identity, coordinate by
coordinate. -/
theorem tensor_hankel_to_toeplitz_index {alpha : Type*} {d : alpha -> Nat}
    (hd : forall a, 0 < d a) (m m' : forall a, Fin (d a)) (a : alpha) :
    (((m a).val : Int) + (((revIndex hd m') a).val : Int)) =
      ((d a : Int) - 1) + (((m a).val : Int) - ((m' a).val : Int)) := by
  exact hankel_to_toeplitz_index (hd a) (m a) (m' a)

end TensorReversal
