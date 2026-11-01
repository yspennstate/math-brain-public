import subprocess,pathlib,time
r=pathlib.Path(__file__).resolve().parent
t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(r/'TailAlgebra.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 result=f'exit_code={p.returncode}\nelapsed_seconds={time.time()-t}\n'+p.stdout+p.stderr
except Exception as e:result=f'LEAN NOT CHECKED: {e}'
(r/'lean_check.txt').write_text(result,encoding='utf8')
print(result,flush=True)
