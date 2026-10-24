import subprocess,pathlib,time
root=pathlib.Path('~/brain_workers/TRIO_1011/op/G0006')
t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(root/'CertificateChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 result=f'Command: lake env lean {root / "CertificateChecks.lean"}\nWorking directory: ~/lean_verify\nTimeout: 3600 seconds\nExit: {p.returncode}\nElapsed: {time.time()-t:.3f} seconds\n'+p.stdout+p.stderr
except Exception as e:result=f'Lean check exception: {e}\nElapsed: {time.time()-t:.3f}\n'
(root/'lean_check.txt').write_text(result,encoding='utf8');print(result)
