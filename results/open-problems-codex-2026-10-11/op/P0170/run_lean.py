import subprocess,time
from pathlib import Path
root=Path(__file__).parent
out=root/'lean_check.log'
if out.exists(): (root/'lean_check_first_attempt.log').write_bytes(out.read_bytes())
t=time.time()
out.write_text('Running finite parity checks with explicit reducible predicates.\n',encoding='utf-8')
try:
 with out.open('a',encoding='utf-8') as f:
  r=subprocess.run(['lake','env','lean',str(root/'ParityCheck.lean')],cwd='~/lean_verify',stdout=f,stderr=subprocess.STDOUT,timeout=3600)
  f.write(f'\nelapsed={time.time()-t:.3f}\nexit_code={r.returncode}\n')
except subprocess.TimeoutExpired:
 with out.open('a',encoding='utf-8') as f:f.write('\nTimeout after 3600 seconds; not checked.\n')
print(out.read_text(encoding='utf-8'),flush=True)
