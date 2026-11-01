from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parent
RUN=ROOT/'runs/20261026T195737Z-fleet04-A068-antichain-beyond-one-order'
for p in (RUN/'code', RUN/'out'): p.mkdir(parents=True,exist_ok=True)
spec=dict(helper_version='subspace-stabilizer-v1',family='all 16 Boolean cores on two latent bits, embedded by three rank-two linear maps in four physical bits; all 16 one-point edits',domain=dict(N=4,core_bits=2,embeddings=[[1,2],[3,6],[5,10]],restrictions='all 3^4 physical partial assignments'),case_count=16*3*16*81,symmetry='none',arithmetic='integer Walsh, Fraction, exact integer AM-GM; no numerical logarithm signs',memory_estimate_MB=35,max_runtime_seconds=55,pilot_max_seconds=60,automatic_escalation=False)
(RUN/'SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print(str(RUN))
