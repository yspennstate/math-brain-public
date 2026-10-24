import subprocess,pathlib,time
p=subprocess.run(['lake','env','lean',str(pathlib.Path('PeelingAlgebra.lean').resolve())],cwd='~/lean_verify',capture_output=True,text=True,timeout=3600)
pathlib.Path('lean_check.txt').write_text('exit_code='+str(p.returncode)+'\n'+p.stdout+p.stderr,encoding='utf8');print(p.returncode,p.stdout,p.stderr)
