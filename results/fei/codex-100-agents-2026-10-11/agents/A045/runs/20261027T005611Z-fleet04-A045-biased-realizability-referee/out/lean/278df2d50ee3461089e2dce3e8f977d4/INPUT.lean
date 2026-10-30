theorem three_rows_no_boolean_code
    (h : Bool → Bool × Bool) (a b c : Bool) :
    ¬ (h a = (false, false) ∧ h b = (false, true) ∧
       h c = (true, true)) := by
  cases a <;> cases b <;> cases c <;> simp_all
