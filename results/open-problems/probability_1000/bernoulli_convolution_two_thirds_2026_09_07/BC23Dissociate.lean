import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Data.Int.GCD
import Mathlib.Algebra.Prime.Defs
import Mathlib.RingTheory.Int.Basic
import Mathlib.Tactic.NormNum.Prime
import Mathlib.Tactic.Common
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The frequencies `2^i * 3^(K-i)` carry no small relation

If `eps i ∈ {0, ±1, ±2}` and `∑_{i ≤ K} eps i * 2^i * 3^(K-i) = 0`, then every `eps i = 0`.

The proof is an induction on `K`: modulo 3 only the top term survives, which forces `eps (K+1) = 0`,
and the rest of the sum is `3 *` the same statement one step down.

This dissociateness is what makes the full-period average of
`∏_{i ≤ K} cos²(π k 2^i / 3^(i+1))` equal to `2^(-K-1)` exactly.
-/

open Finset

namespace BC23

/-- The coefficients we allow: `{0, ±1, ±2}`. -/
def Small (e : ℤ) : Prop := e = 0 ∨ e = 1 ∨ e = -1 ∨ e = 2 ∨ e = -2

lemma Small.eq_zero_of_three_dvd {e : ℤ} (h : Small e) (h3 : (3 : ℤ) ∣ e) : e = 0 := by
  rcases h with h | h | h | h | h <;> subst h
  · rfl
  all_goals (exfalso; omega)

/-- The weighted sum whose vanishing we study. -/
def S (eps : ℕ → ℤ) (K : ℕ) : ℤ := ∑ i ∈ range (K + 1), eps i * 2 ^ i * 3 ^ (K - i)

lemma S_zero (eps : ℕ → ℤ) : S eps 0 = eps 0 := by
  simp [S]

lemma S_succ (eps : ℕ → ℤ) (K : ℕ) :
    S eps (K + 1) = 3 * S eps K + eps (K + 1) * 2 ^ (K + 1) := by
  have hterm : ∀ i ∈ range (K + 1),
      eps i * 2 ^ i * 3 ^ (K + 1 - i) = 3 * (eps i * 2 ^ i * 3 ^ (K - i)) := by
    intro i hi
    have hiK : i ≤ K := Nat.lt_succ_iff.mp (mem_range.mp hi)
    have hsub : K + 1 - i = (K - i) + 1 := by omega
    rw [hsub]
    ring
  calc S eps (K + 1)
      = (∑ i ∈ range (K + 1), eps i * 2 ^ i * 3 ^ (K + 1 - i))
          + eps (K + 1) * 2 ^ (K + 1) * 3 ^ (K + 1 - (K + 1)) := by
        rw [S, Finset.sum_range_succ]
    _ = (∑ i ∈ range (K + 1), 3 * (eps i * 2 ^ i * 3 ^ (K - i)))
          + eps (K + 1) * 2 ^ (K + 1) := by
        rw [Finset.sum_congr rfl hterm]; simp
    _ = 3 * S eps K + eps (K + 1) * 2 ^ (K + 1) := by
        rw [S, Finset.mul_sum]

theorem eq_zero_of_S_eq_zero (eps : ℕ → ℤ) (hs : ∀ i, Small (eps i)) :
    ∀ K, S eps K = 0 → ∀ i, i ≤ K → eps i = 0 := by
  intro K
  induction K with
  | zero =>
    intro h i hi
    have : i = 0 := Nat.le_zero.mp hi
    subst this
    rwa [S_zero] at h
  | succ K ih =>
    intro h i hi
    have hsplit : (0 : ℤ) = 3 * S eps K + eps (K + 1) * 2 ^ (K + 1) := by
      rw [← h, S_succ]
    have h3 : (3 : ℤ) ∣ eps (K + 1) * 2 ^ (K + 1) := ⟨-S eps K, by linarith⟩
    have hp : Prime (3 : ℤ) := Int.prime_iff_natAbs_prime.mpr (by norm_num)
    have hnot : ¬ ((3 : ℤ) ∣ (2 : ℤ) ^ (K + 1)) := by
      intro hd
      have h23 : (3 : ℤ) ∣ (2 : ℤ) := hp.dvd_of_dvd_pow hd
      norm_num at h23
    have hdvd : (3 : ℤ) ∣ eps (K + 1) := by
      rcases hp.dvd_mul.mp h3 with hgood | hbad
      · exact hgood
      · exact absurd hbad hnot
    have htop : eps (K + 1) = 0 := (hs (K + 1)).eq_zero_of_three_dvd hdvd
    have hrest : S eps K = 0 := by
      rw [htop] at hsplit
      simp at hsplit
      linarith
    rcases Nat.lt_or_ge i (K + 1) with hlt | hge
    · exact ih hrest i (Nat.lt_succ_iff.mp hlt)
    · have : i = K + 1 := le_antisymm hi hge
      rw [this]
      exact htop

end BC23

#print axioms BC23.eq_zero_of_S_eq_zero
#print axioms BC23.S_succ
