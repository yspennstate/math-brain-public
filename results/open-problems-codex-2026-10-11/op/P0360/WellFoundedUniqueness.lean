import Mathlib.Logic.Basic
import Mathlib.Order.Basic

/- Abstract kernel of Proposition A. The two hypotheses must still be
   verified for frozen percolation, as done in ATTEMPT.md. -/
theorem uniqueness_of_wellFounded_dependencies
    {Time Vertex : Type} (r : Time → Time → Prop)
    (wf : WellFounded r)
    (A B P Q : Time → Vertex → Prop)
    (earlier : ∀ t, (∀ s, r s t → ∀ v, P s v ↔ Q s v) →
      ∀ v, A t v ↔ B t v)
    (extensional : ∀ t, (∀ v, A t v ↔ B t v) →
      ∀ v, P t v ↔ Q t v) :
    ∀ t v, P t v ↔ Q t v := by
  intro t
  exact wf.induction t (fun t ih => extensional t (earlier t ih))

/- The strict decrease used at a switching vertex of Proposition B. -/
theorem next_time_is_earlier {Time : Type} [Preorder Time]
    {next activation current : Time}
    (h₁ : next ≤ activation) (h₂ : activation < current) :
    next < current := lt_of_le_of_lt h₁ h₂
