import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Invertible

/-!
B07 Lean WIP for the repaired five-singular-value paper, source
4e530247ec0ef4101a6e5ecf621bd35a969c42aa / blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

Target: the algebraic core of Lemma 2.7(b), source lines 163--174:
the Gram determinant factorization after orthogonal projection.

This file is intentionally self-contained over Mathlib.  The core determinant proof below is
the same algebra already kernel-checked in the repository theorem QformNine.gram_factor.
The additional wrappers connect positivity/nonzero determinant to the Invertible hypothesis
and record the row-projection identities needed to match the repaired paper.

IMPORTANT: this new file was not kernel-built in fleet01/B07's current runtime because no
lean/lake executable is exposed there.  It contains no sorry, admit, axiom, or unsafe command;
its status is UNBUILT until an existing authorized Lean environment compiles it.
-/

open Matrix

namespace QformFiveB07

/-- Matrix formula for the orthogonal row-space projector used in Lemma 2.7(b). -/
noncomputable def rowProj {k d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ)
    [Invertible (N * N.transpose)] : Matrix (Fin d) (Fin d) ℝ :=
  N.transpose * ⅟(N * N.transpose) * N

/-- The Gram matrix N N^T is symmetric. -/
theorem gram_symm {k d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ) :
    (N * N.transpose).transpose = N * N.transpose := by
  rw [Matrix.transpose_mul, Matrix.transpose_transpose]

/-- The inverse-of a symmetric invertible Gram matrix is symmetric. -/
theorem gram_inv_symm {k d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ)
    [Invertible (N * N.transpose)] :
    (⅟(N * N.transpose)).transpose = ⅟(N * N.transpose) := by
  have hGsymm : (N * N.transpose).transpose = N * N.transpose := gram_symm N
  have h1 : (N * N.transpose) * (⅟(N * N.transpose)).transpose = 1 := by
    have h0 := congrArg Matrix.transpose (invOf_mul_self (N * N.transpose))
    rw [Matrix.transpose_mul, Matrix.transpose_one, hGsymm] at h0
    exact h0
  calc
    (⅟(N * N.transpose)).transpose
        = ⅟(N * N.transpose) *
            ((N * N.transpose) * (⅟(N * N.transpose)).transpose) := by
          rw [← Matrix.mul_assoc, invOf_mul_self, Matrix.one_mul]
    _ = ⅟(N * N.transpose) := by rw [h1, Matrix.mul_one]

/-- The matrix formula for the row-space projector is symmetric. -/
theorem rowProj_symm {k d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ)
    [Invertible (N * N.transpose)] :
    (rowProj N).transpose = rowProj N := by
  unfold rowProj
  rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose,
    gram_inv_symm N, Matrix.mul_assoc]

/-- The row-space projector is idempotent. -/
theorem rowProj_idem {k d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ)
    [Invertible (N * N.transpose)] :
    rowProj N * rowProj N = rowProj N := by
  unfold rowProj
  calc
    (N.transpose * ⅟(N * N.transpose) * N) *
        (N.transpose * ⅟(N * N.transpose) * N)
        = N.transpose * ⅟(N * N.transpose) * (N * N.transpose) *
            ⅟(N * N.transpose) * N := by
              simp only [Matrix.mul_assoc]
    _ = N.transpose * ⅟(N * N.transpose) * N := by
          rw [Matrix.mul_assoc N.transpose (⅟(N * N.transpose)) (N * N.transpose),
            invOf_mul_self, Matrix.mul_one]

/-- The projector fixes every row of N. -/
theorem rowProj_fixes_rows {k d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ)
    [Invertible (N * N.transpose)] :
    N * rowProj N = N := by
  unfold rowProj
  calc
    N * (N.transpose * ⅟(N * N.transpose) * N)
        = (N * N.transpose) * ⅟(N * N.transpose) * N := by
            simp only [Matrix.mul_assoc]
    _ = N := by rw [mul_invOf_self, Matrix.one_mul]

/-- The residual operator kills the rows of N, i.e. its image is orthogonal to their span. -/
theorem row_residual_zero {k d : ℕ} (N : Matrix (Fin k) (Fin d) ℝ)
    [Invertible (N * N.transpose)] :
    N * ((1 : Matrix (Fin d) (Fin d) ℝ) - rowProj N) = 0 := by
  rw [Matrix.mul_sub, Matrix.mul_one, rowProj_fixes_rows N, sub_self]

/-- Lemma 2.7(b), determinant core in finite matrix coordinates.

The block Gram determinant factors by the Gram determinant of the selected H-rows and
the Gram determinant of the residual rows T (I-Pi).
-/
theorem gram_factor_repaired {k l d : ℕ}
    (N : Matrix (Fin k) (Fin d) ℝ) (T : Matrix (Fin l) (Fin d) ℝ)
    [Invertible (N * N.transpose)] :
    (Matrix.fromBlocks (N * N.transpose) (N * T.transpose)
      (T * N.transpose) (T * T.transpose)).det
      = (N * N.transpose).det *
        ((T * ((1 : Matrix (Fin d) (Fin d) ℝ) - rowProj N)) *
          (T * ((1 : Matrix (Fin d) (Fin d) ℝ) - rowProj N)).transpose).det := by
  rw [Matrix.det_fromBlocks₁₁]
  congr 2
  have hPiT : (rowProj N).transpose = rowProj N := rowProj_symm N
  have hPi2 : rowProj N * rowProj N = rowProj N := rowProj_idem N
  rw [Matrix.transpose_mul, Matrix.transpose_sub, Matrix.transpose_one, hPiT]
  have hidem :
      ((1 : Matrix (Fin d) (Fin d) ℝ) - rowProj N) *
          ((1 : Matrix (Fin d) (Fin d) ℝ) - rowProj N)
        = 1 - rowProj N := by
    rw [Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub, Matrix.one_mul,
      Matrix.mul_one, Matrix.one_mul, hPi2]
    abel
  unfold rowProj
  calc
    T * T.transpose -
        T * N.transpose * ⅟(N * N.transpose) * (N * T.transpose)
        = T * (1 - N.transpose * ⅟(N * N.transpose) * N) * T.transpose := by
            rw [Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one]
            simp only [Matrix.mul_assoc]
    _ = T *
          ((1 - N.transpose * ⅟(N * N.transpose) * N) *
            (1 - N.transpose * ⅟(N * N.transpose) * N)) *
          T.transpose := by
            rw [show
              (1 - N.transpose * ⅟(N * N.transpose) * N) *
                (1 - N.transpose * ⅟(N * N.transpose) * N)
                = 1 - N.transpose * ⅟(N * N.transpose) * N by
                  simpa [rowProj] using hidem]
    _ = T * (1 - N.transpose * ⅟(N * N.transpose) * N) *
          ((1 - N.transpose * ⅟(N * N.transpose) * N) * T.transpose) := by
            simp only [Matrix.mul_assoc]

/-- A directly paper-shaped wrapper: positivity of the selected Gram determinant gives
the invertibility needed by the Schur-complement formula. -/
theorem gram_factor_of_pos {k l d : ℕ}
    (N : Matrix (Fin k) (Fin d) ℝ) (T : Matrix (Fin l) (Fin d) ℝ)
    (hTheta : 0 < (N * N.transpose).det) :
    (Matrix.fromBlocks (N * N.transpose) (N * T.transpose)
      (T * N.transpose) (T * T.transpose)).det
      = (N * N.transpose).det *
        ((T * ((1 : Matrix (Fin d) (Fin d) ℝ) -
          N.transpose * ⅟(N * N.transpose) * N)) *
          (T * ((1 : Matrix (Fin d) (Fin d) ℝ) -
            N.transpose * ⅟(N * N.transpose) * N)).transpose).det := by
  letI : Invertible (N * N.transpose) :=
    invertibleOfIsUnitDet _ (Ne.isUnit (ne_of_gt hTheta))
  simpa [rowProj] using gram_factor_repaired N T

end QformFiveB07
