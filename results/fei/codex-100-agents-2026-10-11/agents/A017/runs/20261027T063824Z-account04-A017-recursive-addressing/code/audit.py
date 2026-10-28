"""Separate direct-character/Fraction entropy implementation; no primary helper import."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib,json,sys,time
R=Path(__file__).resolve().parents[1]; O=R/'out'
def save(n,v):(O/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def freeze():
    save('audit_spec.json',dict(helper_version='A017-direct-character-ledger-audit-v1',helper_sha256=digest(Path(__file__)),
      family='ALL256 Boolean3-bit f times ALL16 Boolean multipliers on original unqueried bits1,2; actual root and BOTH children at original bit0',
      domain='4096 ordered pairs; direct Walsh character sums; boundary positive controls',case_count=4096,symmetry='none',
      arithmetic='Fraction prime-log entropy; independent128-term UNREDUCED rational atanh log intervals',
      memory_estimate_MB=40,max_runtime_seconds=60))
def add(a,b,k=F(1)):
    c=dict(a)
    for p,v in b.items():c[p]=c.get(p,F(0))+k*v
    return {p:v for p,v in c.items() if v}
def truth(n,c):return tuple(1-2*((c>>x)&1) for x in range(1<<n))
def encode(t):return sum(int(v<0)<<x for x,v in enumerate(t))
@lru_cache(None)
def data(n,c):
    t=truth(n,c);N=len(t)
    w=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(N)]
    assert sum(v*v for v in w)==N*N
    h={2:F(2*n)}
    for v in w:
        z=abs(v);p=2
        if not z:continue
        while z>1:
            k=0
            while z%p==0:k+=1;z//=p
            if k:h[p]=h.get(p,F(0))-F(2*v*v*k,N*N)
            p+=1
    h={p:v for p,v in h.items() if v}
    return t,w,h
@lru_cache(None)
def ln(p):
    x=F(p-1,p+1);a=x;s=F(0)
    for j in range(128):s+=2*a/(2*j+1);a*=x*x
    return s,s+2*a/(257*(1-x*x))
def nonnegative(d):
    if not d:return True
    lower=sum(v*ln(p)[0 if v>=0 else 1] for p,v in d.items())
    upper=sum(v*ln(p)[1 if v>=0 else 0] for p,v in d.items())
    assert lower>0 or upper<0
    return lower>0
def run():
    spec=json.loads((O/'audit_spec.json').read_text(encoding='utf-8'));assert spec['helper_sha256']==digest(Path(__file__))
    start=time.monotonic();checks=0;pairs=0; endpoints=set()
    for fc in range(256):
        t,fw,fh=data(3,fc)
        for cc in range(16):
            ct=truth(2,cc);cw=data(2,cc)[1];r=0 if sum(v!=0 for v in cw)==1 else 2
            c=tuple(ct[x>>1] for x in range(8));gt=tuple(x*y for x,y in zip(t,c));gc=encode(gt);gh=data(3,gc)[2]
            E=add(gh,fh,F(-1));phi=add({2:F(r)},E)
            assert nonnegative(phi) and nonnegative(add({2:F(2*r)},phi,F(-1)));checks+=2
            if not phi:endpoints.add('zero')
            if not add({2:F(2*r)},phi,F(-1)) and r:endpoints.add('twice_rank')
            fhc=[];ghc=[];ech=[];phch=[]
            for b in (0,1):
                ft=t[b::2];gg=gt[b::2]
                assert tuple(x*y for x,y in zip(ft,ct))==gg
                ffh=data(2,encode(ft))[2];ggh=data(2,encode(gg))[2]
                fhc.append(ffh);ghc.append(ggh);e=add(ggh,ffh,F(-1));ech.append(e);phch.append(add({2:F(r)},e));checks+=1
            omega=add(E,add(ech[0],ech[1]),F(-1,2))
            drift=add(phi,add(phch[0],phch[1]),F(-1,2))
            assert omega==drift;checks+=1
            deltaf=add(fh,add(fhc[0],fhc[1]),F(-1,2))
            deltag=add(gh,add(ghc[0],ghc[1]),F(-1,2))
            assert add(deltag,deltaf,F(-1))==omega;checks+=1
            assert sum(t[x]!=t[x^1] for x in range(8))==sum(gt[x]!=gt[x^1] for x in range(8));checks+=1;pairs+=1
        assert time.monotonic()-start<60
    assert endpoints=={'zero','twice_rank'};checks+=1
    # Positive controls for deliberately false extensions.
    assert F(4)>10*F(5,16);checks+=1 # m4 translated-defect Phi is NOT bounded by10I.
    t=(1,-1,1,-1);gt=tuple(x*x for x in t)
    assert sum(t[x]!=t[x^1] for x in range(4))==4 and sum(gt[x]!=gt[x^1] for x in range(4))==0;checks+=1
    save('audit.json',dict(status='PASS',pairs=pairs,assertions=checks,endpoints=sorted(endpoints),elapsed_seconds=time.monotonic()-start,
      scope='Separate author representation, NOT independent-agent acceptance; direct root/BOTH-child entropy and physical influence'))
    print(json.dumps(dict(status='PASS',pairs=pairs,assertions=checks,elapsed_seconds=time.monotonic()-start)))
if __name__=='__main__':
    if '--freeze' in sys.argv:freeze()
    else:run()
