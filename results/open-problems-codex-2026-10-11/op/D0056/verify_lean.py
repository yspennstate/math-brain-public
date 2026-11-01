import subprocess,pathlib,time
cmd=['lake','env','lean','~/brain_workers/TRIO_1011/op/D0056/Barrier.lean']
t=time.monotonic()
r=subprocess.run(cmd,cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
text=f'Command: {cmd}\nExit: {r.returncode}\nSeconds: {time.monotonic()-t:.2f}\n{r.stdout}\n{r.stderr}'
pathlib.Path('lean_check.txt').write_text(text,encoding='utf8');print(text)
