from pathlib import Path
import subprocess,time
root=Path.cwd();p=root/'PrefixDomination.lean';p.write_text(p.read_text(encoding='utf-8-sig'),encoding='utf8')
t=time.time()
try:
 r=subprocess.run(['lake','env','lean',str(p)],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 out=f'exit_code={r.returncode}\nelapsed_seconds={time.time()-t:.3f}\n'+r.stdout+r.stderr
except Exception as e:out=repr(e)
(root/'prefix_lean_check.txt').write_text(out,encoding='utf8');print(out)
