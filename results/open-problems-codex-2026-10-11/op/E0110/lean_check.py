import subprocess,pathlib,time
root=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
p=subprocess.run(['lake','env','lean',str(root/'SpecialCase.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
(root/'lean_check.txt').write_text(p.stdout+p.stderr+'\nexit='+str(p.returncode)+'\nseconds='+str(time.monotonic()-start),encoding='utf8')
print(p.stdout,p.stderr,'exit',p.returncode,flush=True)
