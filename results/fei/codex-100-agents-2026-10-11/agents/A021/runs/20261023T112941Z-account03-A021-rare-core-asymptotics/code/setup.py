from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1];(r/'out').mkdir(exist_ok=True)
old=r.parent/'20261023T045725Z-account03-A021-rare-core-asymptotics/code/arithmetic.py';(r/'code/arithmetic.py').write_bytes(old.read_bytes())
spec={'helper_version':{'arithmetic':hashlib.sha256(old.read_bytes()).hexdigest(),'checker':hashlib.sha256((r/'code/check.py').read_bytes()).hexdigest()},'family':'t=2 tensor g3 and every single vertex sign flip; fixed block-first low-bit-first order; ALL deterministic data stopping cuts through depth5 via Bellman certificate','domain':'base function plus all64 edited vertices; all63 prefix nodes for each','case_count':65,'node_count':4095,'pilot_functions':[None,0,1,63],'symmetry':'none','arithmetic':'exact Fraction spectra/influences and prime-log expressions;40-term rational atanh sign certificates','memory_estimate_mb':80,'pilot_max_seconds':60,'main_max_seconds':60,'controller_extension':'analytic conditioning on full controller assignment, not enumeration or dimension extrapolation'}
(r/'SEARCH_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('RUN_CREATED; SPEC_FROZEN')
