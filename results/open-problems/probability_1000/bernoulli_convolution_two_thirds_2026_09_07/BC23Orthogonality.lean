import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.GeomSum
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Character orthogonality over a period

`∑_{k < N} exp(2πi k m / N) = N` when `N ∣ m`, and `0` otherwise.

This is the second ingredient of the exact full-period average of
`∏_{i ≤ K} cos²(π k 2^i / 3^(i+1))`; the first is the dissociateness lemma of `BC23Dissociate`.
-/

open Finset Complex

namespace BC23

noncomputable def e (t : ℝ) : ℂ := Complex.exp (2 * Real.pi * Complex.I * t)

lemma e_add (s t : ℝ) : e (s + t) = e s * e t := by
  unfold e
  rw [← Complex.exp_add]
  push_cast
  ring_nf

lemma e_int (n : ℤ) : e (n : ℝ) = 1 := by
  unfold e
  have : (2 * Real.pi * Complex.I * (n : ℝ)) = (n : ℂ) * (2 * Real.pi * Complex.I) := by
    push_cast; ring
  rw [this, Complex.exp_int_mul_two_pi_mul_I]

/-- `e (k * m / N)` as a power of the primitive root `e (m / N)`. -/
lemma e_pow (m : ℝ) (k : ℕ) : e (k * m) = (e m) ^ k := by
  induction k with
  | zero => simp [e]
  | succ k ih =>
    have hstep : ((k : ℝ) + 1) * m = (k : ℝ) * m + m := by ring
    push_cast
    rw [hstep, e_add, ih, pow_succ]

/-- Orthogonality: the sum of `e (k m / N)` over a full period is `N` or `0`. -/
theorem sum_e_period (N : ℕ) (hN : 0 < N) (m : ℤ) :
    (∑ k ∈ range N, e ((k : ℝ) * (m : ℝ) / (N : ℝ)))
      = if (N : ℤ) ∣ m then (N : ℂ) else 0 := by
  have hNne : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hN.ne'
  set z : ℂ := e ((m : ℝ) / (N : ℝ)) with hz
  have hterm : ∀ k ∈ range N, e ((k : ℝ) * (m : ℝ) / (N : ℝ)) = z ^ k := by
    intro k _
    have : (k : ℝ) * (m : ℝ) / (N : ℝ) = (k : ℝ) * ((m : ℝ) / (N : ℝ)) := by
      field_simp
    rw [this, hz, e_pow]
  rw [Finset.sum_congr rfl hterm]
  by_cases hdvd : (N : ℤ) ∣ m
  · have hz1 : z = 1 := by
      obtain ⟨c, hc⟩ := hdvd
      have : (m : ℝ) / (N : ℝ) = (c : ℝ) := by
        rw [hc]; push_cast; field_simp
      rw [hz, this, e_int]
    simp [hz1, hdvd]
  · have hzN : z ^ N = 1 := by
      rw [hz, ← e_pow]
      have : (N : ℝ) * ((m : ℝ) / (N : ℝ)) = (m : ℝ) := by field_simp
      rw [this, e_int]
    have hzne : z ≠ 1 := by
      intro h1
      apply hdvd
      rw [hz] at h1
      unfold e at h1
      obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp h1
      have hpi : (2 : ℂ) * (Real.pi : ℂ) * Complex.I ≠ 0 := by
        have h1' : (Real.pi : ℂ) ≠ 0 := by
          exact_mod_cast Real.pi_ne_zero
        simp [h1', Complex.I_ne_zero]
      have hreal : (m : ℝ) / (N : ℝ) = (n : ℝ) := by
        field_simp at hn
        exact_mod_cast hn
      have hm : (m : ℝ) = (N : ℝ) * (n : ℝ) := by
        field_simp at hreal
        linarith
      exact ⟨n, by exact_mod_cast hm⟩
    have := geom_sum_eq hzne N
    rw [this, hzN]
    simp [hdvd]

end BC23

#print axioms BC23.sum_e_period
