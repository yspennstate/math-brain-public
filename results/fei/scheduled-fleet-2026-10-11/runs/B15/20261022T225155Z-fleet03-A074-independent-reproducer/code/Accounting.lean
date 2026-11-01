import Lean

theorem A074_shortfall (s e v w d : Int) (h : v + w = s + e) :
    d + e - v = w - (s - d) := by omega

theorem A074_saturated_children (s0 s1 d0 d1 : Int)
    (h0 : d0 <= s0) (h1 : d1 <= s1) (h : d0 + d1 = s0 + s1) :
    d0 = s0 ? d1 = s1 := by omega
