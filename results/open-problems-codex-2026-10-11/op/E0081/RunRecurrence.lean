import Mathlib.Tactic.Ring

def runValue (k i : Nat) : Rat := (2 : Rat) ^ (k + 1) - 2 ^ (i + 1)

theorem run_boundary (k : Nat) : runValue k k = 0 := by
  simp [runValue]

theorem run_initial (k : Nat) : runValue k 0 = (2 : Rat) ^ (k + 1) - 2 := by
  simp [runValue]

-- The equation is algebraic and holds even beyond the states i < k.
-- Only states i < k are used in the probabilistic first-step equations.
theorem run_bellman (k i : Nat) :
    runValue k i = 1 + (runValue k (i + 1) + runValue k 0) / 2 := by
  simp only [runValue, pow_succ]
  ring
