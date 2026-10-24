import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/- Numerator of the target-versus-planted degree-pair discrepancy.
   Division by positive 2*mu*(mu-2), and the probabilistic limits,
   are supplied by the written proof. -/
theorem degree_pair_rank_one (mu j k : ℝ) :
    mu * ((j - 2) * (k - 2)) + 2 * mu * (mu - 2) -
      (mu - 2) * j * k = 2 * (j - mu) * (k - mu) := by
  ring

theorem degree_three_discrepancy (mu : ℝ) :
    2 * mu * (mu - 2) + mu - 9 * (mu - 2) =
      2 * (mu - 3) ^ 2 := by
  ring
