import pathlib, subprocess, time
root=pathlib.Path(__file__).parent.resolve()
start=time.monotonic()
try:
 p=subprocess.run(['lake','env','lean',str(root/'FiniteChecks.lean')],
     cwd='~/lean_verify',capture_output=True,text=True,
     encoding='utf-8',timeout=3600)
 result=f'exit_code={p.returncode}\nelapsed_seconds={time.monotonic()-start:.2f}\n'+p.stdout+p.stderr
except Exception as e:
 result=f'ERROR: {e}\nelapsed_seconds={time.monotonic()-start:.2f}\n'
(root/'lean_check.txt').write_text(result,encoding='utf-8')
print(result,flush=True)
