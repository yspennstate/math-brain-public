from pathlib import Path
from itertools import product
from fractions import Fraction as F
import importlib.util,time,json
R=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('new_cell_checker',R/'code/check.py'); mod=importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
h=mod.h; start=time.perf_counter(); raw=valid=owned_fail=q_fail=flat_checks=0; first=None
g=[F(1),F(-1,3),F(5,3),F(1,3)]
for p,q in [((0,0,-1),(0,-1,0)),((0,0,-1),(1,-1,0))]:
    cs,bad=mod.cells(p,q); _,_,pv=mod.controller(p); _,_,qv=mod.controller(q); nz=8
    for A,B in product(product((0,1),repeat=4),repeat=2):
        for mode in ('xor','or'):
            raw+=1
            e=[(A[x]*pv[z]^B[x]*qv[z]) if mode=='xor' else int(bool(A[x]*pv[z] or B[x]*qv[z])) for x in range(4) for z in range(nz)]
            if any(sum(e[x*nz:(x+1)*nz])*4>nz for x in range(4)): continue
            valid+=1
            v=[g[x]*(1-2*e[x*nz+z]) for x in range(4) for z in range(nz)]
            spec=h.spectrum(v); inf=h.influences(v); iz=sum(inf[:3]); ix=sum(inf[3:])
            mi=h.influences([1-2*a for a in e]); mx=sum(mi[3:])
            owned_fail+=ix<mx
            if ix<mx and first is None: first={'p':p,'q':q,'A':A,'B':B,'mode':mode,'final_core_energy':str(ix),'mask_core_influence':str(mx)}
            for t in range(4):
                for c in cs:
                    assert len({spec[t*nz+s] for s in c})==1; flat_checks+=1
            children=[h.spectrum([v[x*nz+z] for x in range(4)]) for z in range(nz)]
            assert sum(spec)==1 and all(sum(c)==1 for c in children)
            HC={}
            for c in children: HC=h.add(HC,h.entropy(c),F(1,nz))
            Q=h.add(h.entropy(spec),HC,-1)
            bound=(4+h.log2(5 if bad else 4)[0]+2/h.U2)*iz+2*ix
            q_fail+=h.interval(Q)[1]>bound
# Actual rational normalized-real degree-one terminal, empty final edit.
a,b=F(4095,4097),F(128,4097); mass=b*b
assert a*a+mass==1 and mass<F(1,1024)
assert F(842,1215)>F(2,3)
assert 5**2<2**5 # log2(5)<5/2, so K<19/2<10.
out={'raw_real_inputs':raw,'valid_real_cases':valid,'real_ownership_failures':owned_fail,'first_ownership_witness':first,'real_access_interval_failures':q_fail,'flat_cell_checks':flat_checks,'real_degree_one_terminal':{'fourier':[str(a),str(b)],'I':str(mass),'U':'0','H_over_I_strict_lower_bound':10,'source_K_strict_upper_bound':'19/2','final_edit':'empty','actual_children_norm':'1'},'runtime_seconds':time.perf_counter()-start,'failures':0,'scope':'Ownership and U/degree-two terminal extensions false on normalized real seeds; bare access general-real extension remains undecided'}
(R/'out/REAL_SCOPE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
