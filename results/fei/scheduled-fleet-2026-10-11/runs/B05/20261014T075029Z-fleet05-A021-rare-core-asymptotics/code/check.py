from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import runpy, json, time, sys
RUN=Path(__file__).resolve().parents[1]
OLD=RUN.parent/'20261014T035704Z-fleet05-A021-rare-core-asymptotics/code/check.py'
# Pinned own earlier helper; run_path does not execute its __main__ or write pyc.
H=runpy.run_path(str(OLD))
ln,ent,add,sub,mul,total,walsh,influence,LN2=[H[x] for x in ('ln','ent','add','sub','mul','total','walsh','influence','LN2')]
def ep(q): return (F(0),F(0)) if q==0 else mul(ln(q),-q)
def one(m,mask,u,v,r,s,direct=False):
    n=1<<m; d=F(1,n); a=F(1,1<<r); t=F(1,1<<s); pi=(1-a,a*(1-t),a*t)
    seed=[1 if mask>>x&1 else -1 for x in range(n)]
    cores=[seed,[(-y if x==u else y) for x,y in enumerate(seed)],[(-y if x==v else y) for x,y in enumerate(seed)]]
    xj=[[F(y,n) for y in walsh(g)] for g in cores]
    ht=total((total((ent(x),1) for x in g),p) for p,g in zip(pi,xj))
    it=sum((p*(1+influence(walsh(g))) for p,g in zip(pi,cores)),F(0))
    expected=Counter(); constant=[]; qvals=[]; vv=[]; nonempty=[]
    for k in range(n):
        xx=[xj[j][k] for j in range(3)]; mean=sum((p*x for p,x in zip(pi,xx)),F(0))
        q=sum((p*x*x for p,x in zip(pi,xx)),F(0)); var=q-mean*mean
        aa=a*((1-t)*xx[1]+t*xx[2]-xx[0]); bb=a*t*(xx[2]-xx[1])
        expected[abs(mean)]+=1; expected[abs(aa)]+=int(1/a-1); expected[abs(bb)]+=int((1/a)*(1/t-1))
        constant.append((ent(mean),1)); nonempty.extend([(ent(aa),1/a-1),(ent(bb),(1/a)*(1/t-1))])
        qvals.append(q); vv.append(var)
    expected[F(0)]+=n*int(1/(a*t)) # missing z-free half of full spectrum
    va=2*a*(1-a)*d*(1+(1-2*t)**2); vb=8*a*t*(1-t)*d; mass=va+vb
    assert sum(vv)==mass and sum(qvals)==1
    assert all(0<v<=2*d*mass and q>=v for q,v in zip(qvals,vv))
    assert sum((v*q for v,q in zip(vv,qvals)),F(0))<=2*d*mass
    ic=2*r*a*d+4*s*a*t*d
    assert mass<=ic
    adj=int((u^v).bit_count()==1)
    rs=2*(pi[0]*pi[1]*2*m*d+pi[0]*pi[2]*2*m*d+pi[1]*pi[2]*4*(m-adj)*d)
    assert rs==m*mass-8*adj*d*pi[1]*pi[2]
    hf=add(total(constant),total(nonempty)); diff=sub(hf,ht)
    hq=total((ep(q),1) for q in qvals); js=sub(hq,ht)
    assert js[1]<=2*ic,(m,mask,u,v,r,s,'JS')
    empty_loss=sub(total(constant),hq)
    tangent=add(total((ln(q),v) for q,v in zip(qvals,vv)),(mass,mass))
    assert empty_loss[1]<=tangent[0],(m,mask,u,v,r,s,'tangent')
    refund=add(mul(LN2,(1-m)*mass),(mass,mass))
    assert empty_loss[1]<=refund[0],(m,mask,u,v,r,s,'refund')
    margin=sub(mul(LN2,rs+10*ic),diff)
    assert margin[0]>0,(m,mask,u,v,r,s,'payment')
    if direct:
        values=[]
        for x in range(1<<(m+1+r+s)):
            data=x&(n-1); z=-1 if (x>>m)&1 else 1
            aa=((x>>(m+1))&((1<<r)-1))==0
            bb=((x>>(m+1+r))&((1<<s)-1))==0
            values.append(z*cores[0 if not aa else 2 if bb else 1][data])
        fw=walsh(values)
        assert Counter(F(abs(y),len(fw)) for y in fw)==expected
        assert influence(fw)==ic+it
        for j,k,pred in [(0,1,2*m*d),(0,2,2*m*d),(1,2,4*(m-adj)*d)]:
            assert influence(walsh([x*y for x,y in zip(cores[j],cores[k])]))==pred
    return dict(m=m,mask=mask,u=u,v=v,r=r,s=s,zero_seed_coefficients=sum(x==0 for x in xj[0]),unequal_nonzero_seed_magnitudes=len(set(abs(x) for x in xj[0] if x))>1,IC=str(ic),Rstar=str(rs),V=str(mass),D_nat_interval=[str(x) for x in diff],margin_nat_interval=[str(x) for x in margin],direct=direct)
def main():
    pilot='--pilot' in sys.argv; limit=96 if pilot else 2432
    start=time.monotonic(); count=direct=zero=unequal=0
    target=RUN/'out'/('pilot_rows.jsonl' if pilot else 'rows.jsonl')
    with target.open('w',encoding='utf-8') as out:
        for m in (2,3):
            pairs=[(u,v) for u in range(1<<m) for v in range(u+1,1<<m)] if m==2 else [(0,1),(0,3)]
            for mask in range(1<<(1<<m)):
                for u,v in pairs:
                    for r in (1,2):
                        for s in (1,2):
                            row=one(m,mask,u,v,r,s,m==2); out.write(json.dumps(row)+'\n'); out.flush()
                            count+=1; direct+=row['direct']; zero+=row['zero_seed_coefficients']>0; unequal+=row['unequal_nonzero_seed_magnitudes']
                            assert time.monotonic()-start<(60 if pilot else 180),'frozen runtime cap'
                            if count==limit: break
                        if count==limit: break
                    if count==limit: break
                if count==limit: break
            if count==limit: break
    result=dict(helper_version='A021-nonflat-two-edit-v1',mode='pilot' if pilot else 'full',cases=count,direct_fixtures=direct,cases_with_zero_seed_rows=zero,cases_with_unequal_nonzero_seed_magnitudes=unequal,elapsed_seconds=time.monotonic()-start,result='PASS')
    (RUN/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
