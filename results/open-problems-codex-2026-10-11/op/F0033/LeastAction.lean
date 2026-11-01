import Lean.Elab.Tactic.Omega
import Mathlib.Tactic.Ring

/- The integer inequality at the first attempted excess toppling.
   c and b are total incoming counts for the legal prefix and barrier.
   u=v at that vertex before the excess; c≤b follows from neighbour counts.
   A stable upper barrier forces its current height below the legal threshold. -/
theorem first_excess_impossible (h u v c b : Int)
    (same : u = v) (incoming : c ≤ b)
    (barrier : h - 4 * v + b ≤ 3)
    (legal : 4 ≤ h - 4 * u + c) : False := by
  omega

/- An origin at height four starts a wave; after one origin toppling,
   its final height is the number of its four neighbours that toppled. -/
theorem wave_continues_iff (a : Int) (lo : 0 ≤ a) (hi : a ≤ 4) :
    (4 ≤ 4 - 4 + a ↔ a = 4) := by
  omega

theorem quadratic_laplacian (a x : Int) :
    4 * (a - x*x) - ((a-(x-1)*(x-1)) + (a-(x+1)*(x+1))
      + (a-x*x) + (a-x*x)) = 2 := by
  ring
