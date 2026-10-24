import pathlib,subprocess,time
root=pathlib.Path(__file__).resolve().parent
t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(root/'FiniteMultiplicity.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 output=p.stdout+p.stderr+'\nEXIT_CODE: '+str(p.returncode)+'\nSECONDS: '+str(time.time()-t)+'\n'
except Exception as e:output=repr(e)+'\nSECONDS: '+str(time.time()-t)+'\n'
(root/'second_lean_check.txt').write_text(output,encoding='utf8')
print(output,flush=True)
