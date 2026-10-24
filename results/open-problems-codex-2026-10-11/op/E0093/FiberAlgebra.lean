import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Fintype.Pi
import Mathlib.Tactic.FinCases

namespace E0093Second

abbrev M := Matrix (Fin 2) (Fin 2) ℤ

-- Standard S3 representation in an integral (not orthonormal) basis.
def T : M := fun i j => if i = j then 0 else 1
def U : M := fun i j =>
  if i = 0 then (if j = 0 then 1 else 0) else -1
def R : M := T * U
def I2 : M := fun i j => if i = j then 1 else 0
def Z2 : M := fun _ _ => 0

set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem T_square : T * T = I2 := by
  apply Matrix.ext
  intro i j
  fin_cases i <;> fin_cases j <;> decide +kernel
theorem U_square : U * U = I2 := by
  apply Matrix.ext
  intro i j
  fin_cases i <;> fin_cases j <;> decide +kernel
theorem reflection_anticommutator : T * U + U * T = -I2 := by
  apply Matrix.ext
  intro i j
  fin_cases i <;> fin_cases j <;> decide +kernel
theorem rotation_relation : R * R + R + I2 = Z2 := by
  apply Matrix.ext
  intro i j
  fin_cases i <;> fin_cases j <;> decide +kernel
theorem rotation_cube : R * R * R = I2 := by
  apply Matrix.ext
  intro i j
  fin_cases i <;> fin_cases j <;> decide +kernel
theorem conjugation_relation : T * R * T = R * R := by
  apply Matrix.ext
  intro i j
  fin_cases i <;> fin_cases j <;> decide +kernel

end E0093Second
