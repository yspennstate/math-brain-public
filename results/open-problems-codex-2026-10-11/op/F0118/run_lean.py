import subprocess,pathlib,time
root=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
try:
    p=subprocess.run(['lake','env','lean',str(root/'FiniteAlgebra.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600,shell=True)
    result=f'exit_code: {p.returncode}\nseconds: {time.monotonic()-start:.3f}\n'+p.stdout+p.stderr
except subprocess.TimeoutExpired as e:
    result='TIMEOUT at 3600 seconds\n'+str(e)
(root/'lean_check.log').write_text(result,encoding='utf8')
print(result,flush=True)
