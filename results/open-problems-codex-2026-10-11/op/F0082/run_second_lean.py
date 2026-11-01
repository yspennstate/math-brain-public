import subprocess,pathlib,time
p=pathlib.Path('~/brain_workers/TRIO_1011/op/F0082')
s=time.time()
r=subprocess.run(['lake','env','lean',str(p/'UncrossingCostChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,timeout=3600)
(p/'second_lean_check.log').write_text(f'exit={r.returncode}; seconds={time.time()-s}\n'+r.stdout+r.stderr,encoding='utf8')
print(r.returncode,r.stdout,r.stderr)
