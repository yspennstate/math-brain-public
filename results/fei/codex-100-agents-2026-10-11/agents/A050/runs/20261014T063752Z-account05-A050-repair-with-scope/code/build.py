from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
old=root.parent/'20261014T004109Z-account05-A050-repair-with-scope'/'code/check.py'
prefix=old.read_text(encoding='utf-8').split('@lru_cache(None)\ndef stats')[0]
old4=root.parent/'20261014T033613Z-account05-A050-repair-with-scope'/'code/check.py'
primitives=old4.read_text(encoding='utf-8').split('def logvec(x):')[1].split('def productref')[0]
suffix=(root/'code/body.py').read_text(encoding='utf-8')
(root/'code/check.py').write_text(prefix+'\nLIMIT=60 if PILOT else 120\n\ndef logvec(x):'+primitives+'\n'+suffix,encoding='utf-8')
spec={'helper_version':'A050-envelope-v1','helper_sha256':hashlib.sha256((root/'code/check.py').read_bytes()).hexdigest(),'family':'Every Boolean sign n=2,3; each physical query, spectator all remaining coordinates; uniform or independent Bernoulli(1/4) full reference; source-zero fallback fair, all0, all1. Regular and extreme parity-one-flip selector r=2..8. Canonical priority fixture at rational c=3/4,25/32,13/16; these sample references are normalized explicitly, not falsely canonical; true c bracket separately certified.','domain':'fixed n=2,3 and declared families only','case_count':4800+14+3,'pilot':'first 24 census cases plus all 17 targets','symmetry':'none','arithmetic':'Integer Walsh and direct physical edges; Fraction normalized full-support same-channel likelihood; log vectors and rational 32-term atanh bounds; exact polynomial and integer signs','memory_estimate_MB':100,'max_runtime_seconds':120,'pilot_max_runtime_seconds':60}
(root/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print(json.dumps(spec))
