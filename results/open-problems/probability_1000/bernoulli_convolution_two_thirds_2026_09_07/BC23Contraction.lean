import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import BC23Analytic

/-!
# From a uniform L² contraction to geometric decay of the fibre deficits

Let `j n = E psi(u_n)` be the fibre deficit and `e n = E[u_n^2]` the second moment of the
bias.  The two pointwise inequalities `t^2 ≤ 2 psi t` and `psi t ≤ t^2 psi 1` (|t| ≤ 1)
integrate to `e n ≤ 2 j n` and `j n ≤ psi 1 * e n`.  If the signed three-preimage average
contracts uniformly, `e (n+1) ≤ (1 - κ) e n`, then `j (n+1) ≤ ρ j n` with
`ρ = 2 psi 1 (1 - κ)`, and `ρ < 1` gives summability with the explicit bound
`∑ j n ≤ j 0 / (1 - ρ)`.  Since `psi 1 = ∑ 1/(2k(2k-1)) = log 2`, the threshold is
`κ > 1 - 1/(2 log 2) ≈ 0.279`; the measured values of κ are 0.71 to 0.98.
The contraction hypothesis itself is the open statement; nothing here proves it.
-/

open Real

namespace BC23

/-- `psi t ≤ t^2 psi 1` for |t| ≤ 1: the series is termwise dominated. -/
theorem psi_le_sq_mul {t : ℝ} (ht : |t| ≤ 1) : psi t ≤ t ^ 2 * psi 1 := by
  have h := psi_mul_le (u := 1) (v := t) (by simp) ht
  simpa using h

/-- Geometric decay of the deficits from a uniform L² contraction of the bias. -/
theorem summable_of_L2_contraction (j e : ℕ → ℝ) (κ : ℝ)
    (hκ1 : 1 - κ ≥ 0)
    (hρ : 2 * psi 1 * (1 - κ) < 1)
    (hnn : ∀ n, 0 ≤ j n)
    (hje : ∀ n, j n ≤ psi 1 * e n)
    (hej : ∀ n, e n ≤ 2 * j n)
    (hcon : ∀ n, e (n + 1) ≤ (1 - κ) * e n) :
    Summable j ∧ ∑' n, j n ≤ j 0 / (1 - 2 * psi 1 * (1 - κ)) := by
  set ρ := 2 * psi 1 * (1 - κ) with hρdef
  have hpsi1 : 0 ≤ psi 1 := by
    unfold psi
    exact tsum_nonneg (fun k => psiTerm_nonneg 1 k)
  have hρ0 : 0 ≤ ρ := by rw [hρdef]; positivity
  -- one step: j (n+1) ≤ ρ j n
  have hstep : ∀ n, j (n + 1) ≤ ρ * j n := by
    intro n
    have h1 := hje (n + 1)
    have h2 := hcon n
    have h3 := hej n
    have h4 : psi 1 * e (n + 1) ≤ psi 1 * ((1 - κ) * e n) := by gcongr
    have h5 : (1 - κ) * e n ≤ (1 - κ) * (2 * j n) := by gcongr
    have h6 : psi 1 * ((1 - κ) * e n) ≤ psi 1 * ((1 - κ) * (2 * j n)) := by gcongr
    calc j (n + 1) ≤ psi 1 * e (n + 1) := h1
      _ ≤ psi 1 * ((1 - κ) * e n) := h4
      _ ≤ psi 1 * ((1 - κ) * (2 * j n)) := h6
      _ = ρ * j n := by rw [hρdef]; ring
  -- iterate: j n ≤ ρ^n j 0
  have hgeom : ∀ n, j n ≤ ρ ^ n * j 0 := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      calc j (n + 1) ≤ ρ * j n := hstep n
        _ ≤ ρ * (ρ ^ n * j 0) := by gcongr
        _ = ρ ^ (n + 1) * j 0 := by ring
  have hρ1 : ρ < 1 := hρ
  have hsg : Summable (fun n : ℕ => ρ ^ n * j 0) :=
    (summable_geometric_of_lt_one hρ0 hρ1).mul_right (j 0)
  have hsum : Summable j :=
    Summable.of_nonneg_of_le hnn hgeom hsg
  refine ⟨hsum, ?_⟩
  have htsum : ∑' n, ρ ^ n * j 0 = j 0 / (1 - ρ) := by
    rw [tsum_mul_right, tsum_geometric_of_lt_one hρ0 hρ1]
    field_simp
  calc ∑' n, j n ≤ ∑' n, ρ ^ n * j 0 := hsum.tsum_le_tsum hgeom hsg
    _ = j 0 / (1 - ρ) := htsum

end BC23
