import Init.Data.Fin.Lemmas

-- Ranked states: 0 = type 2, 1 = vacant, 2 = type 1.
def birthOne (s t : Fin 3) : Fin 3 :=
  if s = 2 ∧ t = 1 then 2 else t

def birthTwo (s t : Fin 3) : Fin 3 :=
  if s = 0 ∧ t = 1 then 0 else t

def toxin (s t : Fin 3) : Fin 3 :=
  if s = 2 ∧ t = 0 then 1 else t

def baselineDeath (_s _t : Fin 3) : Fin 3 := 1

theorem all_local_maps_monotone :
    ∀ s t S T : Fin 3, s ≤ S → t ≤ T →
      birthOne s t ≤ birthOne S T ∧
      birthTwo s t ≤ birthTwo S T ∧
      toxin s t ≤ toxin S T ∧
      baselineDeath s t ≤ baselineDeath S T := by
  decide +kernel
