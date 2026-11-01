import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

open scoped BigOperators

-- Dropping an arbitrary prefix likelihood in [0,1] gives an upper bound.
theorem discard_prefix_likelihood {A : Type*} (s : Finset A)
    (p w f : A -> Real)
    (hp : forall i, i ∈ s -> 0 <= p i)
    (hw : forall i, i ∈ s -> w i <= 1)
    (hf : forall i, i ∈ s -> 0 <= f i) :
    s.sum (fun i => p i * w i * f i) <= s.sum (fun i => p i * f i) := by
  apply Finset.sum_le_sum
  intro i hi
  calc
    p i * w i * f i = w i * (p i * f i) := by ring
    _ <= 1 * (p i * f i) :=
      mul_le_mul_of_nonneg_right (hw i hi) (mul_nonneg (hp i hi) (hf i hi))
    _ = p i * f i := by ring

-- Strictly positive replay weights preserve a zero continuation probability.
-- This is the finite-space version of the positive-likelihood argument.
theorem positive_replay_detects_zero {A : Type*} (s : Finset A)
    (p w f : A -> Real)
    (hp : forall i, i ∈ s -> 0 < p i)
    (hw : forall i, i ∈ s -> 0 < w i)
    (hf : forall i, i ∈ s -> 0 <= f i)
    (hz : s.sum (fun i => p i * w i * f i) = 0) :
    forall i, i ∈ s -> f i = 0 := by
  have hn : forall i, i ∈ s -> 0 <= p i * w i * f i := by
    intro i hi
    exact mul_nonneg (le_of_lt (mul_pos (hp i hi) (hw i hi))) (hf i hi)
  have he : forall i, i ∈ s -> p i * w i * f i = 0 :=
    (Finset.sum_eq_zero_iff_of_nonneg hn).mp hz
  intro i hi
  have hpos : 0 < p i * w i := mul_pos (hp i hi) (hw i hi)
  exact (mul_eq_zero.mp (he i hi)).resolve_left (ne_of_gt hpos)

#print axioms discard_prefix_likelihood
#print axioms positive_replay_detects_zero
