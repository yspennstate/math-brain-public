from pathlib import Path
import json,hashlib,subprocess,sys
r=Path(__file__).resolve().parents[1]
spec={'helpers':{n:hashlib.sha256((r/'code'/n).read_bytes()).hexdigest() for n in ['independent.py','mixed.py']},'independent':{'family':'all65 Bellman functions and4095 prefix nodes, direct character replay','case_count':65,'arithmetic':'Fraction direct-character sums, independent48-term intervals','symmetry':'none','memory_estimate_mb':80,'max_seconds':60},'physical':{'family':'t2 actual point surgery; all16 two-bit controllers; vertices0,1,63; depths1,2,4; CONTROL then DATA only on outcome0 then CONTROL on newly active leaf','case_count':144,'frontier_count':432,'arithmetic':'exact spectra, physical edges, full references, both KLs, original source spend','symmetry':'none','memory_estimate_mb':100,'max_seconds':120}}
(r/'REPLAY_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
for name in ['check.py','independent.py','mixed.py']:
 result=subprocess.run([sys.executable,'-X','utf8',str(r/'code'/name)],capture_output=True,text=True,encoding='utf-8',timeout=130)
 (r/'out'/(name+'.log')).write_text(result.stdout+result.stderr,encoding='utf-8');print(name,result.returncode,result.stdout[-700:],result.stderr[-1000:],flush=True)
 if result.returncode:raise SystemExit(result.returncode)
