import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

def occupancy (b : Bool) : Int := if b then 1 else 0

def clockUpdate (l r : Bool) : Bool × Bool :=
  if l && !r then (false, true) else (l, r)

-- A common bond clock preserves the sitewise order of the two processes.
theorem common_clock_preserves_order (a b x y : Bool) :
    (occupancy a ≤ occupancy x ∧ occupancy b ≤ occupancy y) →
    (occupancy (clockUpdate a b).1 ≤ occupancy (clockUpdate x y).1 ∧
     occupancy (clockUpdate a b).2 ≤ occupancy (clockUpdate x y).2) := by
  cases a <;> cases b <;> cases x <;> cases y <;> decide +kernel

theorem common_clock_preserves_total_discrepancy (a b x y : Bool) :
    (occupancy (clockUpdate x y).1 - occupancy (clockUpdate a b).1) +
      (occupancy (clockUpdate x y).2 - occupancy (clockUpdate a b).2) =
    (occupancy x - occupancy a) + (occupancy y - occupancy b) := by
  cases a <;> cases b <;> cases x <;> cases y <;> decide +kernel

def jumpCount (l r : Bool) : Int := if l && !r then 1 else 0

theorem left_cut_discrepancy_balance (a b x y : Bool) :
    (occupancy (clockUpdate x y).1 - occupancy (clockUpdate a b).1) -
      (occupancy x - occupancy a) = jumpCount a b - jumpCount x y := by
  cases a <;> cases b <;> cases x <;> cases y <;> decide +kernel

theorem transmitted_current_lower_bound (r k incoming outgoing p q : ℝ)
    (hk : 0 ≤ k) (hinput : r*(1-r) ≤ incoming)
    (hbalance : incoming = outgoing + k*p)
    (hp : p = outgoing + q) (hq : q ≤ r^2) :
    (r*(1-r)-k*r^2)/(1+k) ≤ outgoing := by
  have hd : 0 < 1+k := by linarith
  apply (div_le_iff₀ hd).2
  have hm := mul_le_mul_of_nonneg_left hq hk
  rw [hp] at hbalance
  nlinarith

theorem transmitted_current_upper_bound (r k incoming outgoing p q : ℝ)
    (hk : 0 ≤ k) (hinput : incoming ≤ r)
    (hbalance : incoming = outgoing + k*p)
    (hp : p = outgoing + q) (hq : 0 ≤ q) :
    outgoing ≤ r/(1+k) := by
  have hd : 0 < 1+k := by linarith
  apply (le_div_iff₀ hd).2
  have hm := mul_nonneg hk hq
  rw [hp] at hbalance
  nlinarith

theorem occupied_run_current_bound (k n incoming outgoing p epsilon lower : ℝ)
    (hk : 0 ≤ k) (hn : 0 ≤ n)
    (hinput : lower ≤ incoming)
    (hbalance : incoming = outgoing + k*p)
    (hrun : p ≤ n*outgoing+epsilon) :
    (lower-k*epsilon)/(1+k*n) ≤ outgoing := by
  have hd : 0 < 1+k*n := by positivity
  apply (div_le_iff₀ hd).2
  have hm := mul_le_mul_of_nonneg_left hrun hk
  nlinarith
