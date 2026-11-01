import Std.Tactic.Omega

theorem a087_envelope_step (k k0 k1 o e m m0 m1 : Int)
    (chain : 2*k = 2*e + 2*o + k0 + k1)
    (erasure : 0 <= e) (marginal : m0+m1 <= 2*m) :
    (k0+m0)+(k1+m1)+2*o <= 2*(k+m) := by
  omega
