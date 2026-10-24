import subprocess,time,pathlib
p=pathlib.Path('~/brain_workers/TRIO_1011/op/C0100')
t=time.monotonic()
r=subprocess.run(['lake','env','lean',str(p/'DirichletChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
s=f'Command: lake env lean {p / "DirichletChecks.lean"}\nCWD: ~/lean_verify\nTimeout: 3600 seconds\nExit: {r.returncode}\nSeconds: {time.monotonic()-t}\n'+r.stdout+r.stderr
(p/'dirichlet_lean_check.log').write_text(s,encoding='utf8');print(s)
