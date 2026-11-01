from pathlib import Path
import subprocess,time,json
start=time.monotonic();cmd=['lake','env','lean','~/brain_workers/TRIO_1011/op/C0133/FreshHistoryChecks.lean']
r=subprocess.run(cmd,cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('fresh_history_lean.log').write_text(r.stdout+r.stderr,encoding='utf8')
Path('fresh_history_lean_result.json').write_text(json.dumps({'command':cmd,'cwd':'~/lean_verify','timeout_seconds':3600,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-start,'scope':'Finite prefix-likelihood domination and zero-probability preservation; not the infinite probability proof.'},indent=2))
print(r.returncode,r.stdout,r.stderr)
