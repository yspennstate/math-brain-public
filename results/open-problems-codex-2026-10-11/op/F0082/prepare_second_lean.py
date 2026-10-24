from pathlib import Path
p=Path('UncrossingCostChecks.lean')
p.write_text(r'''import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

-- The geometric limit giving h is proved in SECOND_ATTEMPT.md.
-- This theorem kernel-checks the functional-inequality to midpoint-identity step.
theorem four_arm_forces_midpoint (f : ℝ → ℝ)
    (h : ∀ a b c d : ℝ, 0 < a → 0 < b → 0 < c → 0 < d →
      f (a + d) + f (c + b) ≤ f (a + b) + f (c + d))
    (x y : ℝ) (hx : 0 < x) (hy : 0 < y) :
    f ((x+y)/2) = (f x + f y)/2 := by
  have hx2 : 0 < x/2 := by linarith
  have hy2 : 0 < y/2 := by linarith
  have hxx : x/2+x/2=x := by ring
  have hyy : y/2+y/2=y := by ring
  have hxy : x/2+y/2=(x+y)/2 := by ring
  have hyx : y/2+x/2=(x+y)/2 := by ring
  have h1 := h (x/2) (x/2) (y/2) (y/2) hx2 hx2 hy2 hy2
  have h2 := h (x/2) (y/2) (y/2) (x/2) hx2 hy2 hy2 hx2
  simp only [hxx, hyy, hxy, hyx] at h1 h2
  linarith

def sqdist2 (x y u v : ℚ) : ℚ := (x-u)^2+(y-v)^2

-- A proper crossing whose squared-length objective INCREASES on uncrossing.
example : sqdist2 (-1/2) 0 (9/2) 0 = 25 := by norm_num [sqdist2]
example : sqdist2 (-27/10) (-18/5) (3/10) (2/5) = 25 := by
  norm_num [sqdist2]
example : sqdist2 (-1/2) 0 (3/10) (2/5) = 4/5 := by
  norm_num [sqdist2]
example : sqdist2 (-27/10) (-18/5) (9/2) 0 = 324/5 := by
  norm_num [sqdist2]
example : (4/5 : ℚ) + 324/5 > 25+25 := by norm_num
''',encoding='utf8')
p=Path('run_second_lean.py');p.write_text('''import subprocess,pathlib,time
p=pathlib.Path('~/brain_workers/TRIO_1011/op/F0082')
s=time.time()
r=subprocess.run(['lake','env','lean',str(p/'UncrossingCostChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,timeout=3600)
(p/'second_lean_check.log').write_text(f'exit={r.returncode}; seconds={time.time()-s}\\n'+r.stdout+r.stderr,encoding='utf8')
print(r.returncode,r.stdout,r.stderr)
''',encoding='utf8')
