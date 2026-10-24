import subprocess, pathlib, time
root=pathlib.Path(__file__).parent
start=time.time()
r=subprocess.run(['lake','env','lean',str(root/'obstruction.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
(root/'lean_check.txt').write_text(r.stdout+r.stderr+'\nEXIT_CODE='+str(r.returncode)+'\nELAPSED_SECONDS='+str(time.time()-start),encoding='utf8')
print(r.stdout,r.stderr,'EXIT_CODE',r.returncode)
