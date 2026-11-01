/-
Machine-checked components of Section 7 of

  "Phi-mixing implies interlaced rho-mixing for Markov chains" (Bradley's Question 5):

the reset chain on {0, 1, 2, ...} with P(i, 0) = 1 - q and P(i, i+1) = q.

Contents: the closed form (7.2) of the n-step kernel is characterised by its recursion
(P^{n+1} = P^n P written out for this sparse kernel: the 0-column equals 1 - q, the (j+1)-column
equals q times the j-column of P^n), starting from the identity, with rows summing to one on the
finite support {0, ..., i + n}; and the invariant law pi_i = (1 - q) q^i sums to one and satisfies
the balance equations sum_i pi_i P(i, j) = pi_j (as absolutely convergent series).
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open Finset

namespace BradleyQ5.Reset

/-- One-step kernel of the reset chain. -/
noncomputable def P (q : ℝ) (i j : ℕ) : ℝ := if j = 0 then 1 - q else if j = i + 1 then q else 0

/-- The closed form (7.2) of the `n`-step kernel. -/
noncomputable def Pn (q : ℝ) (n i j : ℕ) : ℝ :=
  if j < n then (1 - q) * q ^ j else if j = i + n then q ^ n else 0

/-- The invariant law `pi_i = (1 - q) q^i`. -/
noncomputable def piw (q : ℝ) (i : ℕ) : ℝ := (1 - q) * q ^ i

theorem Pn_zero (q : ℝ) (i j : ℕ) : Pn q 0 i j = if j = i then 1 else 0 := by
  unfold Pn
  simp

/-- The `0`-column of `P^{n+1}` is `1 - q` (a reset in the last step). -/
theorem Pn_succ_zero (q : ℝ) (n i : ℕ) : Pn q (n + 1) i 0 = 1 - q := by
  unfold Pn
  simp

/-- The `(j+1)`-column of `P^{n+1}` is `q` times the `j`-column of `P^n` (no reset in the last
step).  Together with `Pn_succ_zero` this is the identity `P^{n+1} = P^n P` for the sparse kernel
`P`, once the rows of `P^n` sum to one. -/
theorem Pn_succ_succ (q : ℝ) (n i j : ℕ) : Pn q (n + 1) i (j + 1) = q * Pn q n i j := by
  unfold Pn
  by_cases h1 : j < n
  · have h1' : j + 1 < n + 1 := by omega
    rw [if_pos h1', if_pos h1]
    ring
  · have h1' : ¬ (j + 1 < n + 1) := by omega
    rw [if_neg h1', if_neg h1]
    by_cases h2 : j = i + n
    · have h2' : j + 1 = i + (n + 1) := by omega
      rw [if_pos h2', if_pos h2]
      ring
    · have h2' : ¬ (j + 1 = i + (n + 1)) := by omega
      rw [if_neg h2', if_neg h2]
      ring

/-- Rows of `P^n` vanish beyond `i + n`. -/
theorem Pn_support (q : ℝ) (n i j : ℕ) (h : i + n < j) : Pn q n i j = 0 := by
  unfold Pn
  have h1 : ¬ (j < n) := by omega
  have h2 : ¬ (j = i + n) := by omega
  simp [h1, h2]

/-- Rows of `P^n` sum to one over their support `{0, ..., i + n}`. -/
theorem Pn_row_sum (q : ℝ) (n i : ℕ) : ∑ j ∈ range (i + n + 1), Pn q n i j = 1 := by
  induction n with
  | zero =>
    simp only [Nat.add_zero, Pn_zero]
    rw [Finset.sum_ite_eq']
    simp
  | succ n ih =>
    rw [show i + (n + 1) + 1 = (i + n + 1) + 1 by ring, Finset.sum_range_succ']
    simp only [Pn_succ_succ, Pn_succ_zero]
    rw [← Finset.mul_sum, ih]
    ring

/-- `sum_i pi_i = 1` for `0 <= q < 1`. -/
theorem piw_tsum (q : ℝ) (h0 : 0 ≤ q) (h1 : q < 1) : ∑' i, piw q i = 1 := by
  unfold piw
  rw [tsum_mul_left, tsum_geometric_of_lt_one h0 h1]
  have : (1 - q) ≠ 0 := by linarith
  field_simp

theorem piw_summable (q : ℝ) (h0 : 0 ≤ q) (h1 : q < 1) : Summable (piw q) := by
  unfold piw
  exact (summable_geometric_of_lt_one h0 h1).mul_left (1 - q)

/-- `P(i, j+1) = q` if `i = j` and `0` otherwise. -/
theorem P_succ (q : ℝ) (i j : ℕ) : P q i (j + 1) = if i = j then q else 0 := by
  unfold P
  by_cases h : i = j
  · subst h; simp
  · have hne : ¬ (j + 1 = i + 1) := by omega
    rw [if_neg (Nat.succ_ne_zero j), if_neg hne, if_neg h]

/-- Balance at state `0`: `sum_i pi_i P(i, 0) = pi_0`. -/
theorem balance_zero (q : ℝ) (h0 : 0 ≤ q) (h1 : q < 1) : ∑' i, piw q i * P q i 0 = piw q 0 := by
  have hP : ∀ i, P q i 0 = 1 - q := by intro i; unfold P; simp
  simp_rw [hP]
  rw [tsum_mul_right, piw_tsum q h0 h1]
  unfold piw
  simp

/-- Balance at state `j + 1`: `sum_i pi_i P(i, j+1) = pi_{j+1}`. -/
theorem balance_succ (q : ℝ) (j : ℕ) : ∑' i, piw q i * P q i (j + 1) = piw q (j + 1) := by
  have h : ∀ i, piw q i * P q i (j + 1) = if i = j then piw q j * q else 0 := by
    intro i
    rw [P_succ]
    by_cases hij : i = j
    · subst hij; simp
    · simp [hij]
  simp_rw [h]
  rw [tsum_ite_eq]
  unfold piw
  ring

end BradleyQ5.Reset

#print axioms BradleyQ5.Reset.Pn_zero
#print axioms BradleyQ5.Reset.Pn_succ_zero
#print axioms BradleyQ5.Reset.Pn_succ_succ
#print axioms BradleyQ5.Reset.Pn_support
#print axioms BradleyQ5.Reset.Pn_row_sum
#print axioms BradleyQ5.Reset.piw_tsum
#print axioms BradleyQ5.Reset.piw_summable
#print axioms BradleyQ5.Reset.balance_zero
#print axioms BradleyQ5.Reset.balance_succ
