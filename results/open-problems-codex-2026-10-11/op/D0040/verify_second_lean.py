import subprocess,shutil,pathlib,json,time
P=pathlib.Path(__file__).resolve().parent
lake=shutil.which('lake')
if not lake: raise RuntimeError('lake not on PATH')
args=[lake,'env','lean',str(P/'JacobiCheck.lean')]
if lake.lower().endswith(('.cmd','.bat')):
 args=['cmd.exe','/d','/c',subprocess.list2cmdline(args)]
t=time.monotonic()
with (P/'second_lean.log').open('w',encoding='utf-8') as out:
 try:
  r=subprocess.run(args,cwd='~/lean_verify',stdout=out,stderr=subprocess.STDOUT,timeout=3600)
  status={'exit_code':r.returncode,'elapsed_seconds':time.monotonic()-t,'timeout_seconds':3600,'checked':r.returncode==0}
 except subprocess.TimeoutExpired:
  status={'exit_code':None,'elapsed_seconds':time.monotonic()-t,'timeout_seconds':3600,'checked':False,'error':'one-hour timeout'}
(P/'second_lean_result.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
print(json.dumps(status),flush=True)
print((P/'second_lean.log').read_text(encoding='utf-8',errors='replace')[-6000:],flush=True)
