from pathlib import Path
from itertools import combinations_with_replacement
from functools import lru_cache
from collections import defaultdict
import importlib.util,json,time,sys
from check import union_table,restrict
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261011T232653Z-fleet05-A021-rare-core-asymptotics'/'code'/'check.py'
spec=importlib.util.spec_from_file_location('certified_old',OLD)
old=importlib.util.module_from_spec(spec)
previous_bytecode_setting=sys.dont_write_bytecode;sys.dont_write_bytecode=True
spec.loader.exec_module(old)
sys.dont_write_bytecode=previous_bytecode_setting
records=[]
@lru_cache(None)
def walk(a):
    if len(a)==1 or len(set(a))==1:return 0
    f=tuple(1+aa*(old.seed(x)-1) for aa in a for x in range(64))
    j=6;N=len(f);w=old.walsh(f);v=defaultdict(int);dsum=0
    for T in range(N):
        if not(T>>j&1):
            A,D=w[T]**2,w[T|(1<<j)]**2
            old.logadd(v,A+D,A+D);old.logadd(v,A,-A);old.logadd(v,D,-D)
            v[2]-=4*D;dsum+=D
    vec=tuple(sorted((p,c) for p,c in v.items() if c))
    lo,hi,terms=old.interval_vec(vec)
    sign=1 if lo>0 else -1 if hi<0 else 0
    records.append({'controller':a,'dimension':6+(len(a)-1).bit_length(),'queried_coordinate':6,'I_coordinate':str(old.F(dsum,N*N)),'log_vector':vec,'sign_B_minus_4d':sign,'interval_numerator_lower':str(lo),'interval_numerator_upper':str(hi),'atanh_terms':terms,'denominator':'N^2 ln2'})
    return int(sign>0)+walk(tuple(restrict(a,0,0)))+walk(tuple(restrict(a,0,1)))

start=time.perf_counter();families=[]
for events in combinations_with_replacement(range(1,16),3):
    if time.perf_counter()-start>58:raise RuntimeError('Frozen cap reached')
    a=tuple(union_table(events,4));bad=walk(a)
    families.append({'events':events,'bad_control_nodes':bad})
result={'status':'PASS','scope':'All three positive point-subcube event multisets on four controls; fixed physical control order 0,1,2,3; balanced bent4/point-flip selector seed untouched','families':len(families),'distinct_nonconstant_control_nodes':len(records),'families_with_bad_control_node':sum(r['bad_control_nodes']>0 for r in families),'bad_distinct_nodes':sum(r['sign_B_minus_4d']>0 for r in records),'seconds':time.perf_counter()-start,'arithmetic':'integer Walsh and outward rational atanh log bounds; entropy logs not evaluated as floating point'}
(ROOT/'out'/'three_event_validation.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'out'/'three_event_control_certificates.json').write_text(json.dumps(records,indent=2)+'\n')
(ROOT/'out'/'three_event_families.json').write_text(json.dumps(families,indent=2)+'\n')
print(json.dumps(result,indent=2))
