from pathlib import Path
import json
j=json.loads(Path('second_exact_counterexample.json').read_text())
s='''import Mathlib.Analysis.Real.Sqrt
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- The exact perspective-action splitting identity.
theorem perspective_split (d1 d2 h1 h2 : ℝ)
    (h1d : 0 < d1) (h2d : 0 < d2) :
    h1 ^ 2 / (2 * d1) + h2 ^ 2 / (2 * d2) -
      (h1 + h2) ^ 2 / (2 * (d1 + d2)) =
    (d2 * h1 - d1 * h2) ^ 2 / (2 * d1 * d2 * (d1 + d2)) := by
  have hn1 : d1 ≠ 0 := ne_of_gt h1d
  have hn2 : d2 ≠ 0 := ne_of_gt h2d
  have hn3 : d1 + d2 ≠ 0 := ne_of_gt (add_pos h1d h2d)
  field_simp
  <;> ring

-- Algebraic cubic consequence of the occupancy lower bound.
theorem swept_cubic (w D M : ℝ) (hw : 0 ≤ w) (hD : 0 ≤ D)
    (hlarge : 8 * D ≤ w)
    (hbound : (w ^ 2 / 16) * (w / 2 - 2 * D) ≤ M) :
    w ^ 3 ≤ 64 * M := by
  have hfactor : 0 ≤ w / 4 - 2 * D := by linarith
  have hp : 0 ≤ w ^ 2 * (w / 4 - 2 * D) :=
    mul_nonneg (sq_nonneg w) hfactor
  nlinarith

'''
# Prove sqrt inequalities from exact squared inequalities using nonnegativity.
for i,(frac,bounds) in enumerate(zip(j['squared_distances_diag_then_off'],j['sqrt_bounds_numerators'])):
 num,den=frac.split('/');klo,khi=bounds
 kind='upper' if i<2 else 'lower';k=khi if i<2 else klo
 prop=f'Real.sqrt ({num} / {den} : ℝ) < {k} / 1000000000' if i<2 else f'{k} / 1000000000 < Real.sqrt ({num} / {den} : ℝ)'
 s+=f'''theorem root_{kind}_{i} : {prop} := by
  have hs := Real.sq_sqrt (show (0 : ℝ) ≤ {num} / {den} by norm_num)
  have hn := Real.sqrt_nonneg ({num} / {den} : ℝ)
  nlinarith

'''
f=j['squared_distances_diag_then_off'];ks=j['sqrt_bounds_numerators']
s+=f'''theorem different_euclidean_choice :
    Real.sqrt ({f[0]} : ℝ) + Real.sqrt ({f[1]} : ℝ) <
    Real.sqrt ({f[2]} : ℝ) + Real.sqrt ({f[3]} : ℝ) := by
  have h0 := root_upper_0
  have h1 := root_upper_1
  have h2 := root_lower_2
  have h3 := root_lower_3
  linarith

'''
a=j['source'];b=j['target']
q=[]
for i,k in [(0,0),(1,1),(0,1),(1,0)]:
 q.append(f'(({b[k][1]} : ℝ) - ({a[i][1]})) ^ 2 / (2 * (({b[k][0]}) - ({a[i][0]})))')
s+=f'''theorem different_quadratic_choice :
    {q[2]} + {q[3]} < {q[0]} + {q[1]} := by
  norm_num

#print axioms perspective_split
#print axioms swept_cubic
#print axioms different_euclidean_choice
#print axioms different_quadratic_choice
'''
Path('P0336SecondChecks.lean').write_text(s,encoding='utf8')
