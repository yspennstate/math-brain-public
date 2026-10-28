from pathlib import Path
import subprocess,sys,json,hashlib
r=Path(__file__).resolve().parents[1]
p=r.parent/'20261023T112941Z-account03-A021-rare-core-asymptotics/code/independent.py';text=p.read_text(encoding='utf-8').split('def q(d,h):')[0];(r/'code/direct_math.py').write_text(text,encoding='utf-8',newline='')
obj={'helper_version':{n:hashlib.sha256((r/'code'/n).read_bytes()).hexdigest() for n in ['check.py','independent.py','direct_math.py']},'main_domain':[3,5,7],'independent_actual_domain':[3],'scalar_domain':'m1..256 exact central-binomial coefficients; analytic induction supplies ALL m','symmetry':'none','arithmetic':'integer FWHT versus independent direct characters; exact rational-log identities with40/48-term intervals','memory_estimate_mb':180,'max_seconds':120,'revision':'Records pre-pilot correction to singleton coefficient MAGNITUDE (Walsh sign convention); removes one vacuous assertion; no family/domain change. Main/replay hashes frozen before execution.'}
(r/'REPLAY_SPEC.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
for name in ['check.py','independent.py']:
 out=subprocess.run([sys.executable,'-X','utf8',str(r/'code'/name)],capture_output=True,text=True,encoding='utf-8',timeout=130)
 (r/'out'/(name+'.log')).write_text(out.stdout+out.stderr,encoding='utf-8',newline='');print(name,out.returncode,out.stdout[-1200:],out.stderr[-1600:],flush=True)
 if out.returncode:raise SystemExit(out.returncode)
