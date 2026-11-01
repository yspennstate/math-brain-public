import Init.Data.Rat.Lemmas

namespace FEIReferenceOnly

-- A normalized fallback cannot discard reference-only mass.
theorem fallback_mass (g k0 k1 : Rat) (hk : k0+k1=1) :
    g*k0+g*k1=g := by rw [← Rat.mul_add, hk, Rat.mul_one]

theorem no_free_disappearance (g k0 k1 : Rat) (hk : k0+k1=1)
    (h0 : g*k0=0) (h1 : g*k1=0) : g=0 := by
  have h := fallback_mass g k0 k1 hk
  rw [h0, h1, Rat.zero_add] at h
  exact h.symm

-- A true point-mass posterior matches a reference only if its extra mass vanishes.
theorem posterior_one_iff (u g : Rat) (hden : u+g ≠ 0) :
    u/(u+g)=1 ↔ g=0 := by
  constructor
  · intro h
    have hh := congrArg (fun x : Rat => x*(u+g)) h
    rw [Rat.div_mul_cancel hden, Rat.one_mul] at hh
    have hc : u+0=u+g := by rw [Rat.add_zero]; exact hh
    exact (Rat.add_left_cancel u hc).symm
  · intro h
    rw [h, Rat.add_zero]
    have hu : u ≠ 0 := by simpa only [h, Rat.add_zero] using hden
    simp only [Rat.div_def, Rat.mul_inv_cancel _ hu]

#print axioms fallback_mass
#print axioms no_free_disappearance
#print axioms posterior_one_iff
end FEIReferenceOnly
