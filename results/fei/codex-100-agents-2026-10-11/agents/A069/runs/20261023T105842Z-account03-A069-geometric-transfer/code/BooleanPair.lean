import Std

theorem boolean_pair_identity (a b : Int)
    (ha : a = 1 ∨ a = -1) (hb : b = 1 ∨ b = -1) :
    (a+b)*(a-b)=0 ∧ (a+b)^2+(a-b)^2=4 := by
  cases ha with
  | inl h =>
    subst a
    cases hb with
    | inl h => subst b; decide
    | inr h => subst b; decide
  | inr h =>
    subst a
    cases hb with
    | inl h => subst b; decide
    | inr h => subst b; decide
