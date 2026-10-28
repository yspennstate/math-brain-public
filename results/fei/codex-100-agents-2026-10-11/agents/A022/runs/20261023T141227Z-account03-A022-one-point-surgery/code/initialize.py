from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261023T120109Z-account03-A022-one-point-surgery'
(R/'out').mkdir(parents=True,exist_ok=True)
for name in ('exact.py','gu.py','v.py'):
    (R/'code'/name).write_bytes((OLD/'code'/name).read_bytes())
spec={'helper_version':'A022-stage11-selector-v1; exact.py/gu.py/v.py byte copies of stage10','family':'actual Boolean mux h(y,z)=a(z) if y=0 else c(z); epsilon absorbed into c; and g tensor2 with two adjacent controlled edits','domain':'ALL 16 by16 ordered Boolean controller pairs on two physical bits; pilot pairs (1,6),(3,5),(7,1),(0,15); adjacent seeds at (0,1) and (1,3), four pairs each','case_count':{'pilot':4,'main':256,'adjacent':8},'symmetry':'NONE: all ordered pairs retained; epsilon absorbed exactly by complementing c','arithmetic':'integer FWHT, exact Fraction, prime-log vectors and 40-term outward atanh bounds; no floating point signs','memory_estimate_MB':100,'maximum_runtime_seconds':{'pilot':60,'main':60,'adjacent':60,'independent':60},'frozen_hypotheses':['R=Delta_y V(h)-J_y(h) is nonnegative','G_z R is nonpositive'],'purpose':'resolve signs exactly and derive actual CONTROL signed-drift identity; not a universal GU proof','source_hashes':{n:hashlib.sha256((R/'code'/n).read_bytes()).hexdigest() for n in ('exact.py','gu.py','v.py')}}
(R/'SEARCH_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print('FROZEN: 4 pilot,256 pairs,8 adjacent,100MB,60s per job')
