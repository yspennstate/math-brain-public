import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Fintype.Pi

#synth Fintype (Fin 2)
#synth DecidableEq ℤ
#synth Decidable (∀ i : Fin 2, i = i)
#synth Decidable (∀ i j : Fin 2, (0 : ℤ) = 1)
