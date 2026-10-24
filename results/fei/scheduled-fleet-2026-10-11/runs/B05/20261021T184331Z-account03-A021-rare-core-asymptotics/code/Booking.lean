theorem three_bookings (r u v a b c : Nat)
    (hr : r <= a) (hu : u <= b) (hv : v <= c) :
    r + u + v <= a + b + c :=
  Nat.add_le_add (Nat.add_le_add hr hu) hv
