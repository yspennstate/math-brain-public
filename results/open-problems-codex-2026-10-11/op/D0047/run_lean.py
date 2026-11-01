import subprocess,pathlib,time
f=pathlib.Path('BoundaryAlgebra.lean').resolve();t=time.time()
r=subprocess.run(['lake','env','lean',str(f)],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',errors='replace',timeout=3600)
pathlib.Path('lean_check.txt').write_text(f'Command: lake env lean {f}\nWorking directory: ~/lean_verify\nTimeout: 3600 seconds\nExit code: {r.returncode}\nElapsed: {time.time()-t:.2f} seconds\n'+r.stdout+r.stderr,encoding='utf8');print(r.returncode,r.stdout,r.stderr)
