import subprocess,pathlib,time
root=pathlib.Path(__file__).resolve().parent
if (root/'lean_check.txt').exists() and not (root/'lean_check_initial.txt').exists():
 (root/'lean_check_initial.txt').write_bytes((root/'lean_check.txt').read_bytes())
t=time.monotonic()
try:
 p=subprocess.run(['lake','env','lean',str(root/'GridBridge.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf-8',timeout=3600)
 result=f'Exit code: {p.returncode}\nElapsed seconds: {time.monotonic()-t:.2f}\n'+p.stdout+p.stderr
except Exception as e:result=repr(e)
(root/'lean_check.txt').write_text(result,encoding='utf-8')
print(result)
