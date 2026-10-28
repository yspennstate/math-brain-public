theorem jumpParityImpossible (a b c d : Bool)
    (h1 : Bool.xor a b = false)
    (h2 : Bool.xor c d = false)
    (h3 : Bool.xor (Bool.xor (Bool.xor a b) c) d = true) : False := by
  cases a <;> cases b <;> cases c <;> cases d <;> simp_all

#print axioms jumpParityImpossible
