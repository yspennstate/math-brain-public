import subprocess,pathlib,time
start=time.time()
r=subprocess.run(['lake','env','lean',str(pathlib.Path('Reservoir.lean').resolve())],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
pathlib.Path('lean_check.txt').write_text(r.stdout+r.stderr+f'\nexit_code={r.returncode}; elapsed={time.time()-start:.2f}s\n',encoding='utf8');print(r.stdout+r.stderr);print('exit',r.returncode)
