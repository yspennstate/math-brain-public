import Mathlib.LinearAlgebra.Matrix.SchurComplement

namespace P0220
open scoped Matrix
variable {m n R : Type*} [Fintype m] [Fintype n]
  [DecidableEq m] [DecidableEq n] [CommRing R]

theorem finite_joint_block_schur
    (A : Matrix m m R) (F : Matrix m n R)
    (G : Matrix n m R) (Q : Matrix n n R) [Invertible A] :
    (Matrix.fromBlocks A F (-G) (-Q)).det =
      A.det * (G * ⅟A * F - Q).det := by
  simpa only [Matrix.neg_mul, sub_neg_eq_add, sub_eq_add_neg, neg_neg, add_comm]
    using Matrix.det_fromBlocks₁₁ A F (-G) (-Q)

end P0220

#print axioms P0220.finite_joint_block_schur
