set_option maxRecDepth 100000
set_option maxHeartbeats 1000000
theorem A017_integer_signs : (17 : Nat)^170 * 5^80 < 2^896 ? 2^832 < (17 : Nat)^136 * 5^120 := by decide
