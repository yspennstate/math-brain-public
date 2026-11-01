import Init.Data.Rat.Lemmas

namespace FEIBayes

theorem mul_left_comm (a b c : Rat) : a*(b*c)=b*(a*c) := by
  rw [← Rat.mul_assoc, Rat.mul_comm a b, Rat.mul_assoc]

-- Normalization includes the physical reach weights, not leaf counts.
theorem weighted_binary_normalized (w0 w1 a0 a1 b0 b1 : Rat)
    (hw : w0+w1=1) (ha : a0+a1=1) (hb : b0+b1=1) :
    (w0*a0+w1*b0)+(w0*a1+w1*b1)=1 := by
  calc
    (w0*a0+w1*b0)+(w0*a1+w1*b1) =
        w0*(a0+a1)+w1*(b0+b1) := by
      simp only [Rat.mul_add, Rat.add_assoc, Rat.add_comm, Rat.add_left_comm]
    _ = 1 := by rw [ha, hb, Rat.mul_one, Rat.mul_one, hw]

-- Bayes posterior on a terminal factors through any occupied prefix.
theorem posterior_factorization (total group atom : Rat)
    (hg : group ≠ 0) :
    (group/total)*(atom/group)=atom/total := by
  simp only [Rat.div_def]
  calc
    (group*total⁻¹)*(atom*group⁻¹) =
        (atom*total⁻¹)*(group*group⁻¹) := by
      simp only [Rat.mul_assoc, Rat.mul_comm, mul_left_comm]
    _ = atom*total⁻¹ := by rw [Rat.mul_inv_cancel _ hg, Rat.mul_one]

-- No posterior division is needed on an unoccupied prefix.
theorem empty_prefix_atom (group atom rest : Rat)
    (ha : 0 ≤ atom) (hr : 0 ≤ rest)
    (hm : group=atom+rest) (hz : group=0) : atom=0 := by
  have hs : atom+rest=0 := hm.symm.trans hz
  have h : atom+0 ≤ atom+rest := Rat.add_le_add_left.mpr hr
  have h0 : atom ≤ 0 := by simpa only [Rat.add_zero, hs] using h
  exact Rat.le_antisymm h0 ha

#print axioms weighted_binary_normalized
#print axioms posterior_factorization
#print axioms empty_prefix_atom
end FEIBayes
