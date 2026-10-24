import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

-- The completion-fiber cardinality is the finite input to heat-bath cancellation.
def ders4 : Finset (Equiv.Perm (Fin 4)) :=
  Finset.univ.filter (fun p => ∀ i, p i ≠ i)

example : ders4.card = 9 := by decide +kernel
example : (ders4.filter (fun p => p 0 = 1)).card = 3 := by decide +kernel
example : (ders4.filter (fun p => p 0 = 2)).card = 3 := by decide +kernel
example : (ders4.filter (fun p => p 0 = 3)).card = 3 := by decide +kernel

-- Analytic double count, stated without division to isolate all sign obligations.
theorem heat_bath_double_count (s t k a b ell : ℝ)
    (hcount : s * k * a / 16 ≤ t * (ell + 1) * b) :
    s * k * a ≤ 16 * t * (ell + 1) * b := by
  linarith

-- The constants used in the window restriction: 49*16 = 784.
theorem window_constant (n r k ell : ℝ)
    (hk : 0 < k) (hr : 0 < r)
    (hsize : 784 * n * r^2 ≤ k^2)
    (hwindow : ell * k ≤ 49 * n * r) :
    16 * r * ell ≤ k := by
  nlinarith [mul_nonneg (le_of_lt hr) (sub_nonneg.mpr hwindow)]

-- Final substitution produces 800 rather than a degree-dependent factorial.
theorem final_constant (p n r k ell : ℝ)
    (hk : 0 < k) (hr : 0 ≤ r)
    (hcount : p * k ≤ 16 * r * (ell + 1))
    (hwindow : (ell + 1) * k ≤ 50 * n * r) :
    p * k^2 ≤ 800 * n * r^2 := by
  nlinarith [mul_nonneg (le_of_lt hk) (sub_nonneg.mpr hcount),
    mul_nonneg hr (sub_nonneg.mpr hwindow)]
