import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
import Mathlib.Tactic

/-!
Finite Lean sublemmas for the repaired Lemma 3.2 projection proof in
"Quadratic forms with five large singular values have bounded densities".

Exact manuscript source:
  yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa
  repaired-2026-09-25/paper.tex
  blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a

This is fleet03/B05 WIP. It has NOT been compiled in this runtime because Lean/lake
are not installed here. It must not be counted as verified until it compiles against
the pinned project Mathlib revision with no sorry/admit/new axiom and the axiom check
is recorded.
-/

open Finset Real

namespace QformFiveB

/-- Repair item 7, finite core: if beta = ||w||^2 vanishes then the fiber row w vanishes.
Thus the corresponding factor is independent of the fiber variable. -/
theorem zero_beta_norm {E : Type*} [NormedAddCommGroup E] (w : E)
    (h : ‖w‖ ^ 2 = 0) : w = 0 := by
  have hn : ‖w‖ = 0 := by
    nlinarith [norm_nonneg w]
  exact norm_eq_zero.mp hn

/-- The scalar entropy inequality used on repaired source line 224.
Mathlib's log is zero at zero, so the beta=0 branch realizes the manuscript's
"read the zero term as 0" convention.  The inequality in fact needs only beta >= 0. -/
theorem beta_log_inv_le_one_sub (beta : ℝ) (hbeta : 0 ≤ beta) :
    beta * Real.log (1 / beta) ≤ 1 - beta := by
  by_cases hz : beta = 0
  · simp [hz]
  have hbase := Real.self_sub_one_le_mul_log hbeta
  have hlog : Real.log (1 / beta) = -Real.log beta := by
    rw [one_div, Real.log_inv]
  rw [hlog]
  linarith

/-- Sum form of the entropy inequality in Lemma 3.2. -/
theorem beta_entropy_sum_le_complement {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (beta : ι → ℝ)
    (hbeta : ∀ i ∈ s, 0 ≤ beta i) :
    (∑ i ∈ s, beta i * Real.log (1 / beta i))
      ≤ ∑ i ∈ s, (1 - beta i) := by
  exact Finset.sum_le_sum fun i hi =>
    beta_log_inv_le_one_sub (beta i) (hbeta i hi)

/-- The exact finite entropy conclusion needed in repaired source lines 222--226:
if sum beta_i = |s| - d, then one half of the beta-entropy sum is at most d/2. -/
theorem beta_entropy_half_le {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (beta : ι → ℝ) (d : ℝ)
    (hbeta : ∀ i ∈ s, 0 ≤ beta i)
    (hsum : (∑ i ∈ s, beta i) = (s.card : ℝ) - d) :
    (1 / 2 : ℝ) * (∑ i ∈ s, beta i * Real.log (1 / beta i)) ≤ d / 2 := by
  have h := beta_entropy_sum_le_complement s beta hbeta
  have hcomp : (∑ i ∈ s, (1 - beta i)) = d := by
    rw [Finset.sum_sub_distrib, hsum]
    simp
  rw [hcomp] at h
  nlinarith

end QformFiveB
