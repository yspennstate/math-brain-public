import Mathlib.Tactic.Ring
import Lean.Elab.Tactic.Omega

-- s is an oriented crossing sign; n is its dimer occupation.
def walkHeight : List (Int × Int) → Int
  | [] => 0
  | (s,n) :: xs => s * (1 - 4*n) + walkHeight xs

def baseHeight : List (Int × Int) → Int
  | [] => 0
  | (s,_) :: xs => s + baseHeight xs

theorem height_minus_base_divisible_four (xs : List (Int × Int)) :
    ∃ k : Int, walkHeight xs - baseHeight xs = 4*k := by
  induction xs with
  | nil => exact ⟨0, rfl⟩
  | cons x xs ih =>
    obtain ⟨k, hk⟩ := ih
    obtain ⟨s,n⟩ := x
    refine ⟨k - s*n, ?_⟩
    simp only [walkHeight, baseHeight]
    calc
      s * (1 - 4*n) + walkHeight xs - (s + baseHeight xs)
          = (walkHeight xs - baseHeight xs) - 4*s*n := by ring
      _ = 4*(k - s*n) := by rw [hk]; ring

theorem two_heights_same_residue (xs ys : List (Int × Int))
    (hbase : baseHeight xs = baseHeight ys) :
    walkHeight xs % 4 = walkHeight ys % 4 := by
  obtain ⟨k, hk⟩ := height_minus_base_divisible_four xs
  obtain ⟨l, hl⟩ := height_minus_base_divisible_four ys
  omega

#print axioms height_minus_base_divisible_four
#print axioms two_heights_same_residue
