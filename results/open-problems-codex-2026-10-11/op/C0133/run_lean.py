from pathlib import Path
import subprocess,time,json
start=time.monotonic()
cmd=['lake','env','lean','~/brain_workers/TRIO_1011/op/C0133/FiniteChecks.lean']
r=subprocess.run(cmd,cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('lean_check.log').write_text(r.stdout+r.stderr,encoding='utf8')
Path('lean_result.json').write_text(json.dumps({'command':cmd,'cwd':'~/lean_verify','timeout_seconds':3600,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-start,'scope':'Finite harmonic uniqueness and returning-excursion algebra only; not full probability argument.'},indent=2))
print(r.returncode,r.stdout,r.stderr)
