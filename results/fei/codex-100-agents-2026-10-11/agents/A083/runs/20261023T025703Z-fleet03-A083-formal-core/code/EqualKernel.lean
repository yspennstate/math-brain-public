import Init.Data.Rat.Lemmas
namespace A083Stage18
-- Equality is required on ALL reference-positive rows, including the fallback rows.
theorem equal_normalized_kernel (k0 k1 : Rat) (heq : k0=k1)
    (hnorm : k0+k1=1) : k0=(1/2 : Rat) := by
  have h : k0+k0=1 := by simpa only [← heq] using hnorm
  have htwo : (2 : Rat)*k0=1 := by
    rw [show (2 : Rat)=1+1 from by decide]
    simpa only [Rat.add_mul, Rat.one_mul] using h
  have hh := congrArg (fun x : Rat => (1/2)*x) htwo
  rw [← Rat.mul_assoc, show (1/2 : Rat)*2=1 from by decide,
      Rat.one_mul, Rat.mul_one] at hh
  exact hh
end A083Stage18
