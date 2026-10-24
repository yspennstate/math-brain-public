import Lean.Elab.Tactic.Omega

/- If x never toppled, its terminal height is its initial height plus all
   incoming grains. A threshold-reaching activated neighbour set therefore
   forces x to have toppled in any stable terminal configuration. -/
theorem activation_forces_toppling (h u incoming activated : Int)
    (nonnegative : 0 ≤ u) (incoming_lb : activated ≤ incoming)
    (threshold : 4 ≤ h + activated)
    (stable : h - 4*u + incoming ≤ 3) : 1 ≤ u := by
  omega

/- After a whole ladder column has toppled, the next column's height-three
   site is legal; its toppling supplies the second grain needed at height two. -/
theorem ladder_column_transfer (high low : Int)
    (high_height : 3 ≤ high) (low_height : 2 ≤ low) :
    4 ≤ high + 1 ∧ 4 ≤ low + 1 + 1 := by
  omega

/- Exact integer-scaled star Green function arithmetic. -/
theorem star_barrier_equations :
    (4: Int)*4 - (1+1+1) = 13 ∧ (4: Int)*1 - 4 = 0 := by
  decide +kernel

theorem star_outside_bound (incoming : Int) (mass_bound : incoming ≤ 7) :
    -13 ≤ -incoming := by
  omega

theorem ceiling_fails : (3: Int) < 2 + 1 + 1 := by
  decide +kernel
