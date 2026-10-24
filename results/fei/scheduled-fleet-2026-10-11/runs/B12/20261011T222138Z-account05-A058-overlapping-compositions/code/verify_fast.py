from pathlib import Path
import json,time,itertools,sys
from verify import walsh,table,mass_entropy,plus,Q

R=Path(__file__).resolve().parents[1]
resume=len(sys.argv)>1 and sys.argv[1]=='--resume'
spec=json.loads((R/'out/FROZEN_SPEC_V3.json' if resume else R/'out/FROZEN_SPEC_V2.json').read_text())
first=spec.get('start_outer_table',0)
tables=[table(t,2) for t in range(16)]; spectra=[walsh(t) for t in tables]
H=[sum(a*a*(4-2*(abs(a).bit_length()-1)) for a in w if a)//16 for w in spectra]
Iv=[sum(a*a*s.bit_count() for s,a in enumerate(w)) for w in spectra]
checks=0; count=0; start=time.perf_counter()
def ck(c):
    global checks
    checks+=1
    if not c:raise AssertionError((count,checks))

for ft in range(first,16):
    F=tables[ft]
    fw=spectra[ft]
    for rows in itertools.product(range(4),repeat=2):
        u=[((T&rows[0]).bit_count()%2)+2*((T&rows[1]).bit_count()%2) for T in range(4)]
        ds=[sum(fw[T]**2 for T in range(4) if u[T]&(1<<j)) for j in range(2)]
        q=[sum(fw[T]**2 for T in range(4) if u[T]==v) for v in range(4)]
        hq=mass_entropy(q,16); B={}
        for v,c in enumerate(q):
            if c:B=plus(B,mass_entropy([fw[T]**2 for T in range(4) if u[T]==v],c),Q(c,16))
        ck(plus(hq,B)==mass_entropy([a*a for a in fw],16))
        for j,row in enumerate(rows):ck(ds[j]==4*sum(F[y]!=F[y^row] for y in range(4)))
        for bt in range(16):
            for ct in range(16):
                bs=[tables[bt],tables[ct]]; bw=[spectra[bt],spectra[ct]]
                truth=[]
                for x in range(64):
                    y=x&3
                    if bs[0][(x>>2)&3]==-1:y^=rows[0]
                    if bs[1][(x>>4)&3]==-1:y^=rows[1]
                    truth.append(F[y])
                w=walsh(truth)
                for x,a in enumerate(w):
                    T=x&3; U=u[T]; s=(x>>2)&3; t=(x>>4)&3
                    e=fw[T]*(bw[0][s] if U&1 else (4 if s==0 else 0))*(bw[1][t] if U&2 else (4 if t==0 else 0))
                    ck(a==e)
                inf=[sum(a*a for s,a in enumerate(w) if s&(1<<i)) for i in range(6)]
                for i in range(6):
                    ck(inf[i]==64*sum(truth[x]!=truth[x^(1<<i)] for x in range(64)))
                    if i<2:ck(inf[i]==256*sum(a*a for T,a in enumerate(fw) if T&(1<<i)))
                    else:
                        j,k=divmod(i-2,2)
                        ck(inf[i]==16*ds[j]*sum(a*a for S,a in enumerate(bw[j]) if S&(1<<k)))
                hn=0
                for a in w:
                    if a:
                        aa=abs(a); ck(aa&(aa-1)==0)
                        hn+=a*a*(12-2*(aa.bit_length()-1))
                ck(hn==4096*H[ft]+256*(ds[0]*H[bt]+ds[1]*H[ct]))
                ck(sum(inf)==256*Iv[ft]+16*(ds[0]*Iv[bt]+ds[1]*Iv[ct]))
                ck(hn<=2*sum(inf)); count+=1
    result={'mode':'main','helper':'v2','case_count':count,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh, integer dyadic entropy, exact rational prime-log posterior','result':'IN_PROGRESS'}
    (R/'out'/('remaining_checkpoint.json' if resume else 'main_checkpoint.json')).write_text(json.dumps(result,indent=2))
    if result['elapsed_seconds']>180:raise RuntimeError('Frozen v2 runtime exceeded')
ck(count==spec['case_count'])
result.update(result='PASS',case_count=count,exact_assertions=checks,elapsed_seconds=time.perf_counter()-start)
(R/'out'/('remaining_results.json' if resume else 'main_results.json')).write_text(json.dumps(result,indent=2))
print(json.dumps(result))
