import Init

-- Integer-scaled local source accounts. This lemma is the finite budget
-- induction step only; it does not formalize Fourier/KL transport.
theorem combine_original_book (b d l r p q : Nat)
    (local : d + l + r <= b)
    (left : p <= l) (right : q <= r) : d + p + q <= b := by
  exact Nat.le_trans (Nat.add_le_add (Nat.add_le_add_left left d) right) local

theorem successive_original_book (b spent remaining final : Nat)
    (old : spent + remaining <= b)
    (continuation : final <= remaining) : spent + final <= b := by
  exact Nat.le_trans (Nat.add_le_add_left continuation spent) old
