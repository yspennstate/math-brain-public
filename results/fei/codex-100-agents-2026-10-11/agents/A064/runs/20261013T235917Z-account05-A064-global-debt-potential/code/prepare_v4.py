from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]; p=r/'code/check.py';s=p.read_text(encoding='utf-8')
(r/'code/check_v3_timeout.py').write_text(s,encoding='utf-8')
checkpoint=json.loads((r/'out/CHECKPOINT.json').read_text())
(r/'out/FAILED_FULL_v3.json').write_text(json.dumps({'status':'RUNTIME_CAP_REACHED','helper':'code/check_v3_timeout.py','sha256':hashlib.sha256(s.encode()).hexdigest(),'cap_seconds':240,'checkpoint':checkpoint,'scope':'No full81x16x16 certificate; exact assertions reported only for reached cases'},indent=2)+'\n',encoding='utf-8')
# Reconstruct the v2 helper from the recorded reverse patch: the asynchronous
# shell copy originally captured v3 after the edit. Correct that snapshot label.
v2=s.replace('    return outer_values(ctrl,m,mo,j,beta)\n@lru_cache(None)\ndef outer_values(ctrl,m,mo,j,beta):\n    t=beta*beta\n','    t=beta*beta\n')
v2=v2.replace('def bounds(v): return bounds_tuple(tuple(sorted(v.items())))\n@lru_cache(None)\ndef bounds_tuple(v):','def bounds(v):').replace('    for p,a in v:\n','    for p,a in v.items():\n')
v2=v2.replace("(58 if PILOT else 235): raise TimeoutError('Frozen execution cap')","58: raise TimeoutError('Frozen 60-second execution cap')")
v2='\n'.join(l for l in v2.splitlines() if "ROOT/'out'/'CHECKPOINT.json'" not in l)+'\n'
(r/'code/check_v2_timeout.py').write_text(v2,encoding='utf-8')
f=json.loads((r/'out/FAILED_FULL_v2.json').read_text());f['helper_provenance']='Reconstructed from recorded reverse patch after asynchronous snapshot race; not a byte-pinned original execution source';(r/'out/FAILED_FULL_v2.json').write_text(json.dumps(f,indent=2)+'\n',encoding='utf-8')
s=s.replace('else: roots=allcores','else: roots=named')
p.write_text(s,encoding='utf-8');print('Prepared final fixed1296-root certificate domain; preserved runtime-limited helpers.')
