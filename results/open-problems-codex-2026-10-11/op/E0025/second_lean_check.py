import subprocess,pathlib,time
p=pathlib.Path(__file__).resolve().parent
t=time.monotonic()
r=subprocess.run(['lake','env','lean',str(p/'SecondMargins.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
(p/'second_lean_check.txt').write_text(f'exit_code={r.returncode}\nelapsed_seconds={time.monotonic()-t:.2f}\n'+r.stdout+r.stderr,encoding='utf8')
print(r.returncode,r.stdout,r.stderr,flush=True)
