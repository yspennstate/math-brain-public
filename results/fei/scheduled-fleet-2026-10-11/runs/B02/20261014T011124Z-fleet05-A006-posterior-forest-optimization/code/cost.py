from pathlib import Path
from fractions import Fraction as Q
from time import perf_counter
import json,sys
BASE=Path(__file__).resolve().parents[1]
def ln_interval(y):
    z=(y-1)/(y+1); power=z; value=Q(0)
    for k in range(20): value+=2*power/(2*k+1); power*=z*z
    return value,value+2*power/(41*(1-z*z))
L2,U2=ln_interval(Q(2))
def log2_interval(x):
    assert x>=1
    k=x.numerator.bit_length()-x.denominator.bit_length()
    if x<2**k: k-=1
    y=x/Q(2**k); assert 1<=y<2
    lo,hi=ln_interval(y)
    return Q(k)+lo/U2,Q(k)+hi/L2
start=perf_counter(); n=3 if '--pilot' in sys.argv else 4
data=json.loads((BASE/'out'/('CHECK_'+str(n)+'.json')).read_text(encoding='utf-8'))
rows=[]; assertions=0
for table in data['tables']:
    for kind in ['uniform','endpoint_degree']:
        C=[Q(0),Q(0)]; I=Q(0); CL=[Q(0),Q(0)]
        for r in table['rows']:
            if r['weight_kind']!=kind: continue
            p=Q(r['P'])
            if not p: continue
            q=Q(r['complete_mass']); lower=Q(r['lower_mass'])
            assert 0<lower<=q<=1; assertions+=1
            lo,hi=log2_interval(1/q); llo,lhi=log2_interval(1/lower)
            C[0]+=p*lo; C[1]+=p*hi; CL[0]+=p*llo; CL[1]+=p*lhi
            I+=p*r['A'].bit_count()
        assert I>0; assertions+=1
        row={'edges':table['edges'],'weights':kind,'I':str(I),'C_over_I_interval':[str(x/I) for x in C],
             'lower_mass_cost_over_I_interval':[str(x/I) for x in CL]}
        rows.append(row)
        (BASE/'out'/('COST_PARTIAL_'+str(n)+'.json')).write_text(json.dumps({'cases':len(rows),'last':row},indent=2)+'\n',encoding='utf-8')
        if perf_counter()-start>55: raise RuntimeError('55-second guard')
worst=max(rows,key=lambda r:Q(r['C_over_I_interval'][1])); upper=Q(worst['C_over_I_interval'][1])
bound=(upper.numerator+upper.denominator-1)//upper.denominator
assert all(Q(r['C_over_I_interval'][1])<bound for r in rows); assertions+=len(rows)
assert perf_counter()-start<60
out={'status':'PASS','n':n,'cases':len(rows),'assertions':assertions,'seconds':perf_counter()-start,
     'certified_C_MS_over_I_strict_bound':bound,'worst_upper_case':worst,
     'maximum_upper_display':float(upper),'rows':rows}
(BASE/'out'/('COST_3.json' if n==3 else 'COST_4.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
