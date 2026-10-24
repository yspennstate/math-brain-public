import pathlib, subprocess, time
root=pathlib.Path(__file__).resolve().parent
t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(root/'BoundaryChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 text=p.stdout+p.stderr+'\nEXIT_CODE: '+str(p.returncode)+'\nSECONDS: '+str(time.time()-t)+'\n'
except Exception as e:
 text=repr(e)+'\nSECONDS: '+str(time.time()-t)+'\n'
(root/'lean_check.txt').write_text(text,encoding='utf8')
print(text,flush=True)
