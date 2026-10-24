import subprocess,pathlib,time
p=pathlib.Path('~/brain_workers/TRIO_1011/op/P0030')
t=time.time()
try:
 r=subprocess.run(['lake','env','lean',str(p/'WindowSeparation.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 out=r.stdout+r.stderr
 (p/'lean_check.txt').write_text(f'exit_code={r.returncode}\nelapsed_seconds={time.time()-t:.3f}\n'+out,encoding='utf8')
 print('exit',r.returncode,out)
except subprocess.TimeoutExpired as e:
 (p/'lean_check.txt').write_text('One-hour timeout reached. Not checked.',encoding='utf8');print('timeout')
