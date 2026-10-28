def signValue (b : Bool) : Int := if b then 1 else -1

theorem source_scalar_checks :
    (forall a b : Bool, (signValue a - signValue b)^2 =
      if a = b then (0 : Int) else 4) /\
    ((3 : Nat)*128 - 28*4 - 1 - 2*128 = 15) := by
  constructor
  · intro a b
    cases a <;> cases b <;> decide
  · decide
