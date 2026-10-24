import subprocess,pathlib,time
p=pathlib.Path(__file__).resolve().parent;t=time.time()
r=subprocess.run(['lake','env','lean',str(p/'P0336SecondChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
s='Exit code: '+str(r.returncode)+'\nElapsed: '+str(time.time()-t)+'\n'+r.stdout+r.stderr
(p/'lean_second_check.txt').write_text(s,encoding='utf8');print(s)
