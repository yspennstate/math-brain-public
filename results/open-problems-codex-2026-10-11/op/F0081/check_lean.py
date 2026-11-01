import subprocess,pathlib,time
start=time.time()
r=subprocess.run(['lake','env','lean',str(pathlib.Path('ResidualChecks.lean').resolve())],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
pathlib.Path('lean_check.log').write_text(r.stdout+r.stderr+f'\nexit_code={r.returncode}\nelapsed_seconds={time.time()-start:.3f}\n',encoding='utf8')
print(r.stdout+r.stderr,'exit_code',r.returncode)
