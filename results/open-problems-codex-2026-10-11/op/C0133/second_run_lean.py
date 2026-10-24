from pathlib import Path
import subprocess,time,json
start=time.monotonic();cmd=['lake','env','lean','~/brain_workers/TRIO_1011/op/C0133/SecondChecks.lean']
r=subprocess.run(cmd,cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('second_lean_check.log').write_text(r.stdout+r.stderr,encoding='utf8')
Path('second_lean_result.json').write_text(json.dumps({'command':cmd,'cwd':'~/lean_verify','timeout_seconds':3600,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-start,'scope':'Finite cylinder-probability formulas and mixture covariance, not the infinite probabilistic reduction.'},indent=2))
print(r.returncode,r.stdout,r.stderr)
