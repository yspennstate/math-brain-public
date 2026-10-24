import subprocess, pathlib, time
p=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
try:
 r=subprocess.run(['lake','env','lean',str(p/'RunRecurrence.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf-8',timeout=3600)
 log=f'Command: lake env lean {p / "RunRecurrence.lean"}\nCWD: ~/lean_verify\nExit code: {r.returncode}\nElapsed seconds: {time.monotonic()-start:.2f}\n'+r.stdout+r.stderr
except Exception as e:
 log=f'Lean invocation failed: {e}\nElapsed seconds: {time.monotonic()-start:.2f}\n'
(p/'lean_check.txt').write_text(log,encoding='utf-8')
print(log)
