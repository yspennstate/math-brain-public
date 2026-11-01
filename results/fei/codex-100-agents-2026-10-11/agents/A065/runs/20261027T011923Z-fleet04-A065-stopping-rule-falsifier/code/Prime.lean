theorem activation_prime_fiber (a b c : Bool)
    (hb : Bool.xor a b = false) (hc : Bool.xor a c = false) : b = c := by
  cases a
  · cases b
    · cases c
      · rfl
      · cases hc
    · cases hb
  · cases b
    · cases hb
    · cases c
      · cases hc
      · rfl

theorem constant_branch_forces_constant {X Y : Type} (A : X → Bool)
    (B : Y → Bool) (x : X)
    (h : ∀ y, Bool.xor (A x) (B y) = false) : ∀ y z, B y = B z := by
  intro y z
  exact activation_prime_fiber (A x) (B y) (B z) (h y) (h z)
