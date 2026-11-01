from pathlib import Path
import subprocess,time
s='''import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-- Least squared distance of two intensities' square roots to a common value. -/
theorem symmetric_hellinger_lower (p q s : Real) :
    (p-q)^2 <= 2*((p-s)^2+(q-s)^2) := by
  nlinarith [sq_nonneg (p+q-2*s)]

theorem symmetric_hellinger_identity (p q s : Real) :
    2*((p-s)^2+(q-s)^2)-(p-q)^2 = (p+q-2*s)^2 := by
  ring

theorem symmetric_hellinger_optimum (p q : Real) :
    2*((p-(p+q)/2)^2+(q-(p+q)/2)^2) = (p-q)^2 := by
  ring

#print axioms symmetric_hellinger_lower
#print axioms symmetric_hellinger_identity
#print axioms symmetric_hellinger_optimum
'''
p=Path('HellingerObstruction.lean');p.write_text(s,encoding='utf8')
t=time.time();r=subprocess.run(['lake','env','lean',str(p.resolve())],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('lean_hellinger_check.txt').write_text(r.stdout+'\n'+r.stderr+f'\nexit={r.returncode}; seconds={time.time()-t:.2f}\n',encoding='utf8')
print(r.stdout,r.stderr,'exit',r.returncode)
