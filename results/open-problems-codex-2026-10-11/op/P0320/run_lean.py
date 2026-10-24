import pathlib, subprocess, time
root=pathlib.Path(__file__).resolve().parent
t=time.monotonic()
try:
 p=subprocess.run(['lake','env','lean',str(root/'TransportAlgebra.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 result=f'exit={p.returncode}\nelapsed={time.monotonic()-t:.2f}\n'+p.stdout+p.stderr
except Exception as e:
 result=f'FAILED {type(e).__name__}: {e}'
(root/'lean_check.txt').write_text(result,encoding='utf8')
print(result)
