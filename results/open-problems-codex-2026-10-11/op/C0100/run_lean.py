import subprocess,time,pathlib
folder=pathlib.Path('~/brain_workers/TRIO_1011/op/C0100')
s=time.time()
try:
 r=subprocess.run(['lake','env','lean',str(folder/'MomentChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 log=f'Command: lake env lean {folder / "MomentChecks.lean"}\nCWD: ~/lean_verify\nTimeout: 3600 seconds\nExit: {r.returncode}\nSeconds: {time.time()-s:.3f}\n'+r.stdout+r.stderr
except Exception as e:log=str(e)
(folder/'lean_check.log').write_text(log,encoding='utf8');print(log)
