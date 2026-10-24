import Lean

def ternary (i : Fin 3) : Int := if i.val = 0 then 0 else if i.val = 1 then 1 else -1
def sign (i : Fin 2) : Int := if i.val = 0 then 1 else -1

theorem complementary_phase_is_boolean :
    ∀ (a b : Fin 3) (z h : Fin 2),
      ternary a * ternary b = 0 →
      ternary a * ternary a + ternary b * ternary b = 1 →
      (ternary a + sign z * ternary b * sign h = 1 ∨
       ternary a + sign z * ternary b * sign h = -1) := by
  decide
