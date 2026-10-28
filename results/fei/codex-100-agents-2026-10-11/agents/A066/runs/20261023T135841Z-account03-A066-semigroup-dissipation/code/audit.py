"""Independent author-side direct-character and edge enumeration."""
from fractions import Fraction as R
from pathlib import Path
import json,time
base=Path(__file__).resolve().parents[1]
t0=time.perf_counter();count=0
def check(b):
    global count
    count+=1
    assert b,count
    assert time.perf_counter()-t0<45
def spectrum(table):
    N=len(table)
    return [R(sum(value*((-1)**((s&mask).bit_count()%2)) for s,value in enumerate(table)),N) for mask in range(N)]
rows=[]
for n in [8,10]:
    N=2**n
    values=[(-1 if s==0 else (-1 if s%2 else 1)) for s in range(N)]
    w=spectrum(values);p=[a*a for a in w];delta=R(2,N)
    check(w[1]==1-delta)
    check(all(w[i]==-delta for i in range(N) if i!=1))
    check(all(p));check(sum(p)==1)
    edges=[]
    for j in range(n):
        v=R(sum(values[s]!=values[s^(2**j)] for s in range(N)),N)
        edges.append(v);check(v>0)
    check(sum(edges)==1+(n-2)*delta)
    check(p[0]==delta*delta)
    # Actual sign outcomes, without importing or calling the primary checker.
    for t in [-1,1]:
        for x in [-1,1]:
            check([q*q for q in spectrum([t*x*v for v in values])]==p)
    q0=p[0];qother=(1-q0)/(N-1)
    check(q0+(N-1)*qother==1)
    check(qother>0);check(qother!=p[1])
    check(R(63,64)*(n-1)>R(17,16) if n==10 else True)
    if n==8:
        # New balanced zero-energy sector: explicit physical z and x coordinates.
        zh=[(-1 if s&1 else 1)*values[s>>1] for s in range(2*N)]
        wz=spectrum(zh);pz=[a*a for a in wz]
        check(sum(zh)==0)
        check(pz==[p[s>>1] if s&1 else 0 for s in range(2*N)])
        xzh=[(-1 if s&1 else 1)*zh[s>>1] for s in range(4*N)]
        wx=spectrum(xzh)
        check(sum(xzh)==0);check(wx[1]==0)
        check(all(wx[2*j]*wx[2*j+1]==0 for j in range(2*N)))
        check(all(wx[2*j]==0 for j in range(2*N)))
        for t in [-1,1]:
            for x in [0,1]:
                terminal=[t*xzh[x+2*s] for s in range(2*N)]
                check(sum(terminal)==0)
                check(terminal==[t*((-1)**x)*a for a in zh])
    rows.append({'n':n,'I':str(sum(edges)),'direct_coefficients':N,'terminal_signs':4})
out={'status':'PASS','assertions':count,'seconds':time.perf_counter()-t0,'rows':rows,'balanced_physical_h_n':8,'independence':'direct character sums and physical edge enumeration, explicit balanced x/z parent and four terminals, no primary imports; same author, not independent-agent review'}
(base/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(out))
