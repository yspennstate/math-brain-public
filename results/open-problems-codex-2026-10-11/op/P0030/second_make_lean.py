from pathlib import Path
Path('HellingerFilling.lean').write_text('''import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Key finite induction step in the one-way Kakutani proof.
theorem product_deficiency_step (a b : ℝ) (ha : a ≤ 1) (hb : b ≤ 1) :
    1 - a * b ≤ (1 - a) + (1 - b) := by
  nlinarith [mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hb)]

-- Finite source-mass conservation, used orbitwise in the filling proof.
theorem filling_source_step (source accepted : ℝ)
    (hacc : 0 ≤ accepted) (hbound : accepted ≤ source) :
    0 ≤ source - accepted ∧ source - accepted ≤ source := by
  constructor <;> linarith

-- If two residual masses start equal and consume equal accepted mass,
-- their masses remain equal. This is the finite conservation induction.
theorem filling_equal_mass (source target accepted : ℝ)
    (heq : source = target) :
    source - accepted = target - accepted := by
  linarith
''',encoding='utf8')
# Use a distinct log for this attempt; the original Lean check remains untouched.
s=Path('run_lean.py').read_text(encoding='utf-8-sig').replace('WindowSeparation.lean','HellingerFilling.lean').replace('lean_check.txt','second_lean_check.txt')
Path('second_run_lean.py').write_text(s,encoding='utf8')
