import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

/-!
# The reduction to `L^2`: a square-integrable density has finite entropy

For a probability density `f` (so `f >= 0` and `int f = 1`),

  `int f log f <= log (int f^2)`.

The proof used here is not Jensen but the pointwise inequality `log x <= x - 1`: with
`A = int f^2 > 0`,

  `f log f <= f^2 / A - f + f log A`   pointwise (both sides vanish where `f = 0`),

and integrating the right-hand side gives `A/A - 1 + log A = log A`.

For the Bernoulli convolution at `lambda = 2/3` this is the whole content of "L^2 implies finite
entropy": if `mu` has a density in `L^2` then `int f log f <= log ||f||_2^2`, and by Plancherel
`||f||_2^2 = 1 + 2 S` with `S = sum_{k >= 1} |hat mu (k)|^2`.  Nothing in this file says anything
about whether `mu` has a density; it is the (elementary) implication only.
-/

open MeasureTheory

namespace BC23

/-- The pointwise inequality behind the reduction.  For `A > 0` and `t >= 0`,
`t log t <= t^2/A - t + t log A`.  At `t = 0` both sides are `0` (Lean's `log 0 = 0`). -/
theorem mul_log_le_pointwise {A t : ℝ} (hA : 0 < A) (ht : 0 ≤ t) :
    t * Real.log t ≤ t ^ 2 / A - t + t * Real.log A := by
  rcases ht.eq_or_lt with h | h
  · simp [← h]
  · have h1 : Real.log (t / A) ≤ t / A - 1 := Real.log_le_sub_one_of_pos (by positivity)
    have h2 : Real.log (t / A) = Real.log t - Real.log A := Real.log_div (ne_of_gt h) (ne_of_gt hA)
    have h3 : t * (Real.log t - Real.log A) ≤ t * (t / A - 1) := by
      rw [← h2]; exact mul_le_mul_of_nonneg_left h1 ht
    have h4 : t * (t / A - 1) = t ^ 2 / A - t := by field_simp
    rw [h4] at h3
    linarith [h3]

/-- **The reduction to `L^2`.**  If `f` is a probability density (nonnegative, integral `1`) with
`f^2` and `f log f` integrable, then `int f log f <= log (int f^2)`. -/
theorem integral_mul_log_le_log_integral_sq
    {α : Type*} [MeasurableSpace α] {μ : Measure α} {f : α → ℝ}
    (h0 : 0 ≤ᵐ[μ] f)
    (hf : Integrable f μ) (hf2 : Integrable (fun x => f x ^ 2) μ)
    (hflog : Integrable (fun x => f x * Real.log (f x)) μ)
    (hone : ∫ x, f x ∂μ = 1) :
    ∫ x, f x * Real.log (f x) ∂μ ≤ Real.log (∫ x, f x ^ 2 ∂μ) := by
  set A := ∫ x, f x ^ 2 ∂μ with hAdef
  have hA0 : 0 ≤ A := integral_nonneg (fun x => sq_nonneg (f x))
  have hApos : 0 < A := by
    rcases hA0.eq_or_lt with h | h
    · exfalso
      have hz : (fun x => f x ^ 2) =ᵐ[μ] 0 :=
        (integral_eq_zero_iff_of_nonneg (fun x => sq_nonneg (f x)) hf2).1 h.symm
      have hf0 : f =ᵐ[μ] 0 := by
        filter_upwards [hz] with x hx
        have hx2 : f x ^ 2 = 0 := hx
        have := pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hx2
        simpa using this
      have hzero : ∫ x, f x ∂μ = 0 := by
        rw [integral_congr_ae hf0]; simp
      rw [hone] at hzero
      norm_num at hzero
    · exact h
  -- the majorant
  have h1 : Integrable (fun x => f x ^ 2 / A) μ := hf2.div_const A
  have h2 : Integrable (fun x => f x ^ 2 / A - f x) μ := h1.sub hf
  have h3 : Integrable (fun x => f x * Real.log A) μ := hf.mul_const (Real.log A)
  have hg : Integrable (fun x => f x ^ 2 / A - f x + f x * Real.log A) μ := h2.add h3
  have e1 : ∫ x, (f x ^ 2 / A - f x + f x * Real.log A) ∂μ
      = (∫ x, (f x ^ 2 / A - f x) ∂μ) + ∫ x, f x * Real.log A ∂μ := integral_add h2 h3
  have e2 : ∫ x, (f x ^ 2 / A - f x) ∂μ = A / A - 1 := by
    rw [integral_sub h1 hf, integral_div, hone, ← hAdef]
  have e3 : ∫ x, f x * Real.log A ∂μ = Real.log A := by
    rw [integral_mul_const, hone, one_mul]
  have hint_g : ∫ x, (f x ^ 2 / A - f x + f x * Real.log A) ∂μ = Real.log A := by
    rw [e1, e2, e3, div_self (ne_of_gt hApos)]
    ring
  have hae : (fun x => f x * Real.log (f x))
      ≤ᵐ[μ] fun x => f x ^ 2 / A - f x + f x * Real.log A := by
    filter_upwards [h0] with x hx
    exact mul_log_le_pointwise hApos hx
  calc ∫ x, f x * Real.log (f x) ∂μ
      ≤ ∫ x, (f x ^ 2 / A - f x + f x * Real.log A) ∂μ := integral_mono_ae hflog hg hae
    _ = Real.log A := hint_g

/-- The form the Bernoulli-convolution program uses.  If Plancherel gives
`int f^2 = 1 + 2 S` with `S = sum_{k >= 1} |hat mu (k)|^2` (the hypothesis `hpar`), then the
entropy of the density is at most `2 S`.  Combined with the measured `S = 0.103155` this is
`int f log f <= 0.20631`. -/
theorem entropy_le_two_S
    {α : Type*} [MeasurableSpace α] {μ : Measure α} {f : α → ℝ} {S : ℝ}
    (h0 : 0 ≤ᵐ[μ] f)
    (hf : Integrable f μ) (hf2 : Integrable (fun x => f x ^ 2) μ)
    (hflog : Integrable (fun x => f x * Real.log (f x)) μ)
    (hone : ∫ x, f x ∂μ = 1)
    (hpar : ∫ x, f x ^ 2 ∂μ = 1 + 2 * S) (hS : 0 ≤ S) :
    ∫ x, f x * Real.log (f x) ∂μ ≤ 2 * S := by
  have h := integral_mul_log_le_log_integral_sq h0 hf hf2 hflog hone
  rw [hpar] at h
  have hlog : Real.log (1 + 2 * S) ≤ (1 + 2 * S) - 1 :=
    Real.log_le_sub_one_of_pos (by linarith)
  linarith

/-- The same reduction for a finite probability vector: `sum p log p <= log (sum p^2)`.
This is the discrete companion used on the fibre laws. -/
theorem sum_mul_log_le_log_sum_sq {ι : Type*} (s : Finset ι) (p : ι → ℝ)
    (hp : ∀ i ∈ s, 0 ≤ p i) (hone : ∑ i ∈ s, p i = 1) :
    ∑ i ∈ s, p i * Real.log (p i) ≤ Real.log (∑ i ∈ s, p i ^ 2) := by
  set A := ∑ i ∈ s, p i ^ 2 with hAdef
  have hA0 : 0 ≤ A := Finset.sum_nonneg (fun i _ => sq_nonneg (p i))
  have hApos : 0 < A := by
    rcases hA0.eq_or_lt with h | h
    · exfalso
      have hz : ∀ i ∈ s, p i ^ 2 = 0 :=
        (Finset.sum_eq_zero_iff_of_nonneg (fun i _ => sq_nonneg (p i))).1 h.symm
      have hz' : ∀ i ∈ s, p i = 0 := by
        intro i hi
        have := hz i hi
        exact pow_eq_zero_iff (n := 2) (by norm_num) |>.1 this
      rw [Finset.sum_congr rfl hz'] at hone
      simp at hone
    · exact h
  have hstep : ∑ i ∈ s, p i * Real.log (p i)
      ≤ ∑ i ∈ s, (p i ^ 2 / A - p i + p i * Real.log A) :=
    Finset.sum_le_sum (fun i hi => mul_log_le_pointwise hApos (hp i hi))
  have hsplit : ∑ i ∈ s, (p i ^ 2 / A - p i + p i * Real.log A) = Real.log A := by
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.sum_div, ← Finset.sum_mul,
      hone, ← hAdef, div_self (ne_of_gt hApos), one_mul]
    ring
  rw [hsplit] at hstep
  exact hstep

end BC23

#print axioms BC23.mul_log_le_pointwise
#print axioms BC23.integral_mul_log_le_log_integral_sq
#print axioms BC23.entropy_le_two_S
#print axioms BC23.sum_mul_log_le_log_sum_sq
