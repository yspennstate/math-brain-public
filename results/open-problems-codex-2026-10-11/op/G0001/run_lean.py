import pathlib,subprocess,time
root=pathlib.Path(r'~/brain_workers/TRIO_1011/op/G0001')
t=time.time()
try:
 r=subprocess.run(['lake','env','lean',str(root/'FiniteAlgebra.lean')],cwd=r'~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 s=f'Command: lake env lean {root / "FiniteAlgebra.lean"}\nExit: {r.returncode}\nElapsed seconds: {time.time()-t:.3f}\n'+r.stdout+r.stderr
except Exception as e:s=f'Lean failed: {e}'
(root/'lean_check.log').write_text(s,encoding='utf8');print(s)
