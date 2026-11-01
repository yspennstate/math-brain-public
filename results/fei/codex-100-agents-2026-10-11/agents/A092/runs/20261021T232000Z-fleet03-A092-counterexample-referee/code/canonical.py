"""Audit the all-r substatement of A047; no canonical bisection needed."""
from review import F,ROOT,spectrum,edges,ent,add,mul,sub,pretty
from pathlib import Path
import json,time,hashlib

checks=0
def ck(b):
    global checks
    checks+=1
    assert b,checks

def point(r):return [-1 if z==2**r-1 else 1 for z in range(2**r)]
def audit(m,r):
    size=2**(m*r)
    def core(z):return -1 if sum(((z>>(i*r))&((1<<r)-1))==(1<<r)-1 for i in range(m))%2 else 1
    h=[core(z) for z in range(size)]
    vals=[(-1 if (u>>1)&1 else 1) if (u&1)==0 else (core(u>>3) if (u>>2)&1 else 1) for u in range(8*size)]
    w=spectrum(vals);p=[z*z for z in w]
    wh=spectrum(h);ph=[z*z for z in wh]
    delta=F(1,2**r);mu=(1-2*delta)**m;t=(1-mu)/2;p0=(1-t)**2/4
    expected=[F(0)]*len(p)
    expected[0]=expected[1]=p0
    expected[2]=expected[3]=F(1,4)
    expected[4]=expected[5]=t*t/4
    for s in range(1,size):
        for ctl in (0,1,4,5):expected[(s<<3)|ctl]=ph[s]/16
    ck(p==expected);ck(sum(p)==1)
    inf=edges(vals);ck(inf[:3]==[F(1,2),F(1,2),t/2]);ck(all(d==delta/2 for d in inf[3:]))
    ck(sum(inf)==1+t/2+m*r*delta/2)
    ppoint=[v*v for v in spectrum(point(r))]
    ck(ppoint==[(1-2*delta)**2]+[4*delta*delta]*(2**r-1))
    # Independent terminal spectra from actual restrictions, not copied formulas.
    terminal=[]
    for b,zval in [(0,None),(1,0),(1,1)]:
        restricted=[vals[u] for u in range(len(vals)) if ((u>>2)&1)==b and (zval is None or ((u>>3)&1)==zval)]
        q=[v*v for v in spectrum(restricted)]
        terminal.append((ent(q),sum(edges(restricted))))
    Hterm=add(mul(F(1,2),terminal[0][0]),mul(F(1,4),add(terminal[1][0],terminal[2][0])))
    Iterm=terminal[0][1]/2+(terminal[1][1]+terminal[2][1])/4
    ck(Iterm==1+(m*r-1)*delta/2)
    hp=ent(ppoint);hpnext=ent([v*v for v in spectrum(point(r-1))])
    hformula=add((F(2),F(2)),add(mul(F(m-1,4),hp),mul(F(1,8),hpnext)))
    diff=sub(Hterm,hformula);ck(diff[0]<=0<=diff[1])
    ck(ent(p)[1]<4*sum(inf));ck(len(set(h[0::2]))==2 and len(set(h[1::2]))==2)
    return dict(m=m,r=r,dimension=3+m*r,I=str(sum(inf)),H=pretty(ent(p)),terminal_I=str(Iterm))

tic=time.perf_counter()
small=[audit(m,r) for m,r in [(2,2),(2,3),(3,2)]]
finite=[]
for r in (2,3,4,5):
    m=2**(r+2);delta=F(1,2**r);mu=(1-2*delta)**m;t=(1-mu)/2;v=1-(1-t)**2/4
    d=[F(1,2),F(1,2),t/2]+[delta/2]*(m*r)
    prod=F(1)
    for x in d:prod*=1-x/(2*v)
    ck(F(3,4)<v<F(15,16));ck(all(0<x/v<1 for x in d));ck(sum(d)>v)
    ck(prod<F(1,2));ck(m*r*delta/2==2*r)
    ck((2*r*r-1)/(2*r+F(5,4))>r-1)
    finite.append(dict(r=r,m=m,dimension=3+m*r,c_lower='1/2',CE_lower=str(2*r*r-1),I_upper=str(2*r+F(5,4))))
for r in range(2,129):
    ck(2*r*r-1-(r-1)*(2*r+F(5,4))==F(3*r+1,4))
    ck(F(1,1+r)<F(1,2));ck(2*r*r-1>0)
result=dict(status='PASS',small_truth_table_cases=small,finite_normalizer_cases=finite,
            scalar_boundary_cases=127,assertions=checks,runtime_seconds=time.perf_counter()-tic,
            scope='A047 all-r no-finite-K substatement, not its finite numerical excesses or scoped A050 review',
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'out/CANONICAL_REVIEW.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['small_truth_table_cases','finite_normalizer_cases']}))
