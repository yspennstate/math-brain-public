from pathlib import Path
import sys,json,hashlib,subprocess,os,time
RUN=Path(__file__).resolve().parents[1]
spec={'family':'Hamming kernel pullback of bent selector; flip the selector-one zero-fibre and physical0; edit count2^k+1; root FEI3, odd negative count and full Fourier support','domain':'odd k=3,5,7,9 compressed profiles; k3 physical n8 full truth table','case_count':'four compressed profiles, one complete physical table with every coefficient and directional edge','symmetry':'none','arithmetic':'integer Gaussian nullspace basis/Walsh/physical edges; Fraction; rational atanh24 for n8 entropy; all-dimensional lower family analytic','helper_sha256':hashlib.sha256((RUN/'code/arithmetic.py').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256((RUN/'code/check_sharpness.py').read_bytes()).hexdigest(),'memory_estimate_MB':80,'maximum_runtime_seconds':55,'maximum_physical_n':8,'automatic_dimension_escalation':False}
(RUN/'out/FROZEN_SHARPNESS.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
cmd=[sys.executable,'-B','-X','utf8',str(RUN/'code/check_sharpness.py')]
start=time.perf_counter()
r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding='utf-8',timeout=60,creationflags=0x08000000 if os.name=='nt' else 0)
(RUN/'out/sharpness.log').write_text(r.stdout,encoding='utf-8')
(RUN/'out/SHARPNESS_JOB.json').write_text(json.dumps({'command':cmd,'exit_code':r.returncode,'controller_wall_seconds':time.perf_counter()-start},indent=2)+'\n',encoding='utf-8')
print(r.stdout)
raise SystemExit(r.returncode)
