from pathlib import Path
from fractions import Fraction as F
import json,time
started=time.perf_counter(); ROOT=Path(__file__).resolve().parents[1]
ns={'__file__':str(Path(__file__).with_name('finite_hod.py'))}
exec(Path(__file__).with_name('finite_hod.py').read_text(encoding='utf-8').split('cur=(iv')[0],ns)
iv=ns['iv']; add=ns['add']; neg=ns['neg']; mul=ns['mul']; lg=ns['lg']; step=ns['step']
def metrics(t):
    N=len(t); n=N.bit_length()-1
    a=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(N)]
    assert sum(v*v for v in a)==N*N
    p=[F(v*v,N*N) for v in a]
    I=sum(s.bit_count()*w for s,w in enumerate(p))
    edgeI=F(sum(t[x]!=t[x^(1<<j)] for x in range(N) for j in range(n)),N)
    assert I==edgeI
    H=iv(0)
    for w in p:
        if w: H=add(H,neg(mul(iv(w),lg(w))))
    return iv(F(sum(v==-1 for v in t),N)),iv(I),H
tables=[[1 if m&(1<<x) else -1 for x in range(4)] for m in range(16)]
cases=0
for a in tables:
    for b in tables:
        # Constant children are checked directly; finite_hod's interior assertion excludes them.
        A,B=metrics(a),metrics(b)
        t=[(1+u+v-u*v)//2 for v in b for u in a]
        C=metrics(t); dual=metrics([-t[15^x] for x in range(16)])
        assert dual[0]==(1-C[0][1],1-C[0][0]) and dual[1]==C[1]
        assert max(dual[2][0],C[2][0])<=min(dual[2][1],C[2][1])
        if 0<A[0][0]<1 and 0<B[0][0]<1:
            predicted=step(A,B)
            assert predicted[0]==dual[0] and predicted[1]==dual[1]
            assert max(predicted[2][0],dual[2][0])<=min(predicted[2][1],dual[2][1])
        cases+=1
        assert time.perf_counter()-started<60
out={'status':'PASS','cases':cases,'nonconstant_sector_formula_cases':ns['checks'],'method':'direct character sums, physical pivotal edges, dual truth tables, rational log intervals','runtime_seconds':time.perf_counter()-started}
(ROOT/'out/GATE_RECONSTRUCTION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
