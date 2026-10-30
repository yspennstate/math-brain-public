import Std.Tactic.Omega

theorem a087_owned_step (k k0 k1 o r r0 r1 : Int)
    (h : 2*r >= max 0 (2*o+k0+k1-2*k)+r0+r1) :
    2*o+(k0+r0)+(k1+r1) <= 2*(k+r) := by
  have hd : 2*o+k0+k1-2*k <= max 0 (2*o+k0+k1-2*k) := le_max_right _ _
  omega
