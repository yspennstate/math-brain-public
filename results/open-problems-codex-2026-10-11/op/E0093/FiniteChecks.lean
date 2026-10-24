import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fintype.BigOperators

namespace E0093
abbrev V := Fin 2 → ZMod 2

def spans (k : ℕ) (g : Fin k → V) : Prop :=
  ∀ v : V, ∃ c : Fin k → ZMod 2,
    ∀ j : Fin 2, (∑ i : Fin k, c i * g i j) = v j

def oddFunctional (k : ℕ) (g : Fin k → V) : Prop :=
  ∃ f : V, ∀ i : Fin k, (∑ j : Fin 2, f j * g i j) = 1

instance (k : ℕ) (g : Fin k → V) : Decidable (spans k g) :=
  inferInstanceAs (Decidable (∀ v : V, ∃ c : Fin k → ZMod 2,
    ∀ j : Fin 2, (∑ i : Fin k, c i * g i j) = v j))

instance (k : ℕ) (g : Fin k → V) : Decidable (oddFunctional k g) :=
  inferInstanceAs (Decidable (∃ f : V, ∀ i : Fin k,
    (∑ j : Fin 2, f j * g i j) = 1))

def generatingCount (k : ℕ) : ℕ :=
  (Finset.univ.filter (fun g : Fin k → V => spans k g)).card

def periodicGeneratingCount (k : ℕ) : ℕ :=
  (Finset.univ.filter (fun g : Fin k → V => spans k g ∧ oddFunctional k g)).card

set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem generatingCount_two : generatingCount 2 = 6 := by decide +kernel
theorem periodicCount_two : periodicGeneratingCount 2 = 6 := by decide +kernel
theorem generatingCount_three : generatingCount 3 = 42 := by decide +kernel
theorem periodicCount_three : periodicGeneratingCount 3 = 18 := by decide +kernel

end E0093
