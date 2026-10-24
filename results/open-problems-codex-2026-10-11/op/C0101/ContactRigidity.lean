import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- Finite arithmetic at two neighboring contact points. No periodicity assumed.
theorem mixed_contact_bounds (a b c delta d : ℚ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c)
    (hs : a + b ≤ delta) (hd : 1 ≤ d)
    (hca : c ≤ 2*d*a + delta) (hcb : c ≤ 2*d*b + delta) :
    -delta ≤ c-a-b ∧ c-a-b ≤ d*delta := by
  constructor
  · linarith
  · have hp : 0 ≤ (d-1)*(delta-a-b) :=
      mul_nonneg (by linarith) (by linarith)
    nlinarith

theorem contact_integer_trace (m K : ℤ) (delta : ℚ)
    (hdelta : delta < 1)
    (hlo : (K : ℚ)-delta ≤ (m : ℚ)) (hhi : m ≤ K) : m = K := by
  have h : (K : ℚ) < (m : ℚ) + 1 := by linarith
  have hi : K < m + 1 := by exact_mod_cast h
  omega
