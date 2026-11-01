import Std
namespace A084
theorem account_conservation (s0 s1 d0 d1 s d e : Int)
    (hs : s0 + s1 = 2 * (s + e)) (hd : d0 + d1 = 2 * (d + e)) :
    (s0 - d0) + (s1 - d1) = 2 * (s - d) := by omega
theorem saturated_children (r0 r1 : Int) (h0 : 0 ≤ r0) (h1 : 0 ≤ r1)
    (h : r0 + r1 = 0) : r0 = 0 ∧ r1 = 0 := by omega
end A084
#print axioms A084.account_conservation
#print axioms A084.saturated_children
