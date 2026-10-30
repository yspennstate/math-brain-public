theorem two_allocations (u v a b : Nat) (hu : u <= a) (hv : v <= b) :
    u + v <= a + b := Nat.add_le_add hu hv
