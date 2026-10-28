-- Exact arithmetic only, no Mathlib or external axioms.
theorem refresh_log_sign : (7:Nat)^112 < 2^25 * 6^112 := by decide
theorem tensor_refresh_log_sign : (7:Nat)^300 < 2^67 * 6^300 := by decide
theorem initial_supplier_log_sign : (8:Nat)^5 < 2 * 7^5 := by decide
theorem point3_factor_sign : (2:Nat)^57 < 3^36 := by decide
#print axioms refresh_log_sign
#print axioms tensor_refresh_log_sign
#print axioms initial_supplier_log_sign
#print axioms point3_factor_sign
