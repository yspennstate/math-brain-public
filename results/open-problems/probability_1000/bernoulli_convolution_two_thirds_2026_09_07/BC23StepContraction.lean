import Mathlib.Topology.Algebra.InfiniteSum.NatInt
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Contraction over blocks of `L` levels implies summability

`BC23TwoLevel` proves the one-level (`e (n+1) <= (1-k) e n`) and two-level (`e (n+2) <= (1-k) e n`)
statements.  This file proves the general block form, with any step `L >= 1`, an explicit tail
bound, and an "eventually" version in which the contraction is only assumed from some level on.

The core is entirely elementary: if `j >= 0` and `j (n + L) <= rho * j n` with `0 <= rho < 1`, then
the partial sums over blocks satisfy `B (m+1) <= C + rho * B m` with `C = sum_{r < L} j r`, so
every partial sum is at most `C / (1 - rho)`.

Nothing here proves a contraction; the contraction hypothesis is the open part of the program.  At
`lambda = 2/3` the one-level contraction of the fibre bias is measured to FAIL (ratio `0.966` at
level 4, five independent methods agreeing), which is why the block form with `L >= 2` is the one
of interest; the two-level form fails as an operator statement as well.  This file says only what
a block contraction would buy, not that one holds.
-/

open Finset

namespace BC23

/-- Block partial sums are bounded: `sum_{i < L m} j i <= C / (1 - rho)`. -/
theorem block_sum_le (L : ℕ) (j : ℕ → ℝ) (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (hnn : ∀ n, 0 ≤ j n) (hstep : ∀ n, j (n + L) ≤ ρ * j n) (m : ℕ) :
    ∑ i ∈ range (L * m), j i ≤ (∑ r ∈ range L, j r) / (1 - ρ) := by
  set C := ∑ r ∈ range L, j r with hC
  have hC0 : 0 ≤ C := Finset.sum_nonneg (fun r _ => hnn r)
  have hden : 0 < 1 - ρ := by linarith
  induction m with
  | zero => simpa using div_nonneg hC0 (le_of_lt hden)
  | succ m ih =>
    have hsplit : ∑ i ∈ range (L * (m + 1)), j i
        = (∑ i ∈ range L, j i) + ∑ i ∈ range (L * m), j (L + i) := by
      have : L * (m + 1) = L + L * m := by ring
      rw [this, Finset.sum_range_add]
    have hterm : ∀ i ∈ range (L * m), j (L + i) ≤ ρ * j i := by
      intro i _
      have := hstep i
      rwa [add_comm L i]
    have hle : ∑ i ∈ range (L * m), j (L + i) ≤ ρ * ∑ i ∈ range (L * m), j i := by
      rw [Finset.mul_sum]
      exact Finset.sum_le_sum hterm
    have hmul : ρ * ∑ i ∈ range (L * m), j i ≤ ρ * (C / (1 - ρ)) := by
      exact mul_le_mul_of_nonneg_left ih hρ0
    have hfin : C + ρ * (C / (1 - ρ)) = C / (1 - ρ) := by
      field_simp
      ring
    calc ∑ i ∈ range (L * (m + 1)), j i
        = (∑ i ∈ range L, j i) + ∑ i ∈ range (L * m), j (L + i) := hsplit
      _ ≤ C + ρ * (C / (1 - ρ)) := by rw [← hC]; linarith
      _ = C / (1 - ρ) := hfin

/-- **Block contraction implies summability.**  With `L >= 1`, `j >= 0` and
`j (n + L) <= rho j n` for `0 <= rho < 1`, the series converges and
`sum j <= (sum_{r < L} j r) / (1 - rho)`. -/
theorem summable_of_step_contraction (L : ℕ) (hL : 0 < L) (j : ℕ → ℝ) (ρ : ℝ)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (hnn : ∀ n, 0 ≤ j n) (hstep : ∀ n, j (n + L) ≤ ρ * j n) :
    Summable j ∧ ∑' n, j n ≤ (∑ r ∈ range L, j r) / (1 - ρ) := by
  have hpart : ∀ n : ℕ, ∑ i ∈ range n, j i ≤ (∑ r ∈ range L, j r) / (1 - ρ) := by
    intro n
    have hsub : range n ⊆ range (L * n) := by
      intro x hx
      simp only [mem_range] at hx ⊢
      have : n ≤ L * n := Nat.le_mul_of_pos_left n hL
      omega
    have h1 : ∑ i ∈ range n, j i ≤ ∑ i ∈ range (L * n), j i :=
      Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => hnn i)
    exact h1.trans (block_sum_le L j ρ hρ0 hρ1 hnn hstep n)
  exact ⟨summable_of_sum_range_le hnn hpart, Real.tsum_le_of_sum_range_le hnn hpart⟩

/-- The entropy-chain form with an abstract constant `c` (in the application `c = psi 1 = log 2`):
`j n <= c e n`, `e n <= 2 j n`, and a block contraction of the bias `e (n + L) <= (1-k) e n` give
summability of the deficits `j`, provided `2 c (1-k) < 1`. -/
theorem summable_of_step_contraction_chain (L : ℕ) (hL : 0 < L) (j e : ℕ → ℝ) (c κ : ℝ)
    (hc : 0 ≤ c) (hκ : 0 ≤ 1 - κ) (hρ : 2 * c * (1 - κ) < 1)
    (hnn : ∀ n, 0 ≤ j n)
    (hje : ∀ n, j n ≤ c * e n) (hej : ∀ n, e n ≤ 2 * j n)
    (hcon : ∀ n, e (n + L) ≤ (1 - κ) * e n) :
    Summable j ∧ ∑' n, j n ≤ (∑ r ∈ range L, j r) / (1 - 2 * c * (1 - κ)) := by
  set ρ := 2 * c * (1 - κ) with hρdef
  have hρ0 : 0 ≤ ρ := by rw [hρdef]; positivity
  have hstep : ∀ n, j (n + L) ≤ ρ * j n := by
    intro n
    have h1 := hje (n + L)
    have h2 : c * e (n + L) ≤ c * ((1 - κ) * e n) := by
      exact mul_le_mul_of_nonneg_left (hcon n) hc
    have h3 : c * ((1 - κ) * e n) ≤ c * ((1 - κ) * (2 * j n)) := by
      have : (1 - κ) * e n ≤ (1 - κ) * (2 * j n) := mul_le_mul_of_nonneg_left (hej n) hκ
      exact mul_le_mul_of_nonneg_left this hc
    have h4 : c * ((1 - κ) * (2 * j n)) = ρ * j n := by rw [hρdef]; ring
    linarith
  exact summable_of_step_contraction L hL j ρ hρ0 hρ hnn hstep

/-- Two levels: the statement of `BC23TwoLevel.summable_of_two_level_contraction`, obtained here as
the case `L = 2` and with a tail bound attached. -/
theorem summable_of_two_level_contraction_bound (j e : ℕ → ℝ) (c κ : ℝ)
    (hc : 0 ≤ c) (hκ : 0 ≤ 1 - κ) (hρ : 2 * c * (1 - κ) < 1)
    (hnn : ∀ n, 0 ≤ j n)
    (hje : ∀ n, j n ≤ c * e n) (hej : ∀ n, e n ≤ 2 * j n)
    (hcon : ∀ n, e (n + 2) ≤ (1 - κ) * e n) :
    Summable j ∧ ∑' n, j n ≤ (j 0 + j 1) / (1 - 2 * c * (1 - κ)) := by
  have h := summable_of_step_contraction_chain 2 (by norm_num) j e c κ hc hκ hρ hnn hje hej hcon
  have hsum : ∑ r ∈ range 2, j r = j 0 + j 1 := by
    simp [Finset.sum_range_succ]
  rw [hsum] at h
  exact h

/-- **Eventual form.**  The contraction only has to hold from some level `n0` on. -/
theorem summable_of_eventual_step_contraction (L : ℕ) (hL : 0 < L) (n0 : ℕ) (j : ℕ → ℝ) (ρ : ℝ)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (hnn : ∀ n, 0 ≤ j n) (hstep : ∀ n, n0 ≤ n → j (n + L) ≤ ρ * j n) :
    Summable j := by
  have hshift : Summable (fun n => j (n + n0)) := by
    refine (summable_of_step_contraction L hL (fun n => j (n + n0)) ρ hρ0 hρ1
      (fun n => hnn _) ?_).1
    intro n
    have h := hstep (n + n0) (Nat.le_add_left n0 n)
    have hrw : n + n0 + L = n + L + n0 := by omega
    rw [hrw] at h
    exact h
  exact (summable_nat_add_iff n0).1 hshift

end BC23

#print axioms BC23.block_sum_le
#print axioms BC23.summable_of_step_contraction
#print axioms BC23.summable_of_step_contraction_chain
#print axioms BC23.summable_of_two_level_contraction_bound
#print axioms BC23.summable_of_eventual_step_contraction
