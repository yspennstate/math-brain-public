import Init.Data.Rat.Lemmas

namespace FEICoherent

theorem mul_left_comm (a b c : Rat) : a*(b*c)=b*(a*c) := by
  rw [← Rat.mul_assoc, Rat.mul_comm a b, Rat.mul_assoc]

-- Retain the old sector label; the branch kernel only uses its erased row.
theorem row_transport {p0 p1 a b : Rat}
    (hrow : p0+p1 = (a+b)/2) (hab : a+b ≠ 0) :
    (p0+p1) * (a/(a+b)) = a/2 := by
  rw [hrow]
  simp only [Rat.div_def]
  calc
    ((a+b) * (2 : Rat)⁻¹) * (a * (a+b)⁻¹) =
        (a * (2 : Rat)⁻¹) * ((a+b) * (a+b)⁻¹) := by
      simp only [Rat.mul_assoc, Rat.mul_comm, mul_left_comm]
    _ = a * (2 : Rat)⁻¹ := by
      rw [Rat.mul_inv_cancel _ hab, Rat.mul_one]

-- For squared child amplitudes a,b, a zero row has no true mass.
theorem zero_row_transport {p0 p1 a b k : Rat}
    (hrow : p0+p1 = (a+b)/2) (hsum : a+b=0) (ha : a=0) :
    (p0+p1)*k = a/2 := by
  rw [hrow, hsum, ha]
  simp only [Rat.div_def, Rat.zero_mul]

theorem fair_branch_from_normalized_child {mass : Rat}
    (hchild : mass=1) : mass/2 = (1 : Rat)/2 := by rw [hchild]

-- Positive and zero rows are both covered; no division by an unreachable row.
def kernel (a b : Rat) : Rat := if a+b=0 then 1/2 else a/(a+b)

theorem kernel_normalized (a b : Rat) : kernel a b + kernel b a = 1 := by
  by_cases h : a+b=0
  · simp only [kernel, Rat.add_comm b a, h, if_true]
    decide +kernel
  · simp only [kernel, Rat.add_comm b a, h, if_false, Rat.div_def]
    rw [← Rat.add_mul, Rat.mul_inv_cancel _ h]

theorem transport_with_fallback {p0 p1 a b : Rat}
    (hrow : p0+p1 = (a+b)/2)
    (hzero : a+b=0 → a=0) :
    (p0+p1)*kernel a b = a/2 := by
  unfold kernel
  split
  · rename_i h
    exact zero_row_transport hrow h (hzero h)
  · rename_i h
    exact row_transport hrow h

#print axioms row_transport
#print axioms transport_with_fallback

theorem nonnegative_zero_sum {a b : Rat} (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hsum : a+b=0) : a=0 := by
  have h : a+0 ≤ a+b := Rat.add_le_add_left.mpr hb
  have ha0 : a ≤ 0 := by simpa only [Rat.add_zero, hsum] using h
  exact Rat.le_antisymm ha0 ha

theorem transport_nonnegative {p0 p1 a b : Rat}
    (hrow : p0+p1=(a+b)/2) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (p0+p1)*kernel a b = a/2 :=
  transport_with_fallback hrow (nonnegative_zero_sum ha hb)

#print axioms transport_nonnegative
#print axioms kernel_normalized
end FEICoherent
