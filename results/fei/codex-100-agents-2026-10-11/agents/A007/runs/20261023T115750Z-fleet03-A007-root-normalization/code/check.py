from fractions import Fraction as R
from itertools import product
from pathlib import Path
import argparse, json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); count=0
def ck(x):
    global count
    count+=1
    assert x, count
    if count%1000==0: assert time.perf_counter()-START<55
def walsh(t):
    a=list(map(R,t)); h=1
    while h<len(a):
        for s in range(0,len(a),2*h):
            for j in range(s,s+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return [x/len(a) for x in a]
def facts(n):
    d={}; p=2
    while p*p<=n:
        while n%p==0: d[p]=d.get(p,0)+1; n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def add(v,w,c=R(1)):
    for p,e in w.items():
        v[p]=v.get(p,0)+c*e
        if not v[p]: del v[p]
    return v
def lg(q):
    return add({p:R(e) for p,e in facts(q.numerator).items()},facts(q.denominator),R(-1))
def ent(q):
    v={}
    for p in q:
        if p:add(v,lg(p),-p)
    return v
def kl(a,b):
    v={}
    for p,q in zip([a,1-a],[b,1-b]):add(v,lg(p/q),p)
    return v
def phi(a): return {p:4*a*e for p,e in ent([a,1-a]).items()}
def ce(p,q):
    v={}
    for s in range(1,len(p)):
        if p[s]:add(v,lg(q[s]),-p[s])
    return v
def indicator(n,mask):return [R((mask>>j)&1) for j in range(1<<n)]
def data(t,style):
    n=(len(t)-1).bit_length(); a=sum(t)/len(t); g=[2*x-1 for x in t]
    p=[x*x for x in walsh(g)]
    weights=[0]+[1 if style==0 else j+1 for j in range(1,len(t))]
    q=[R(x,sum(weights)) for x in weights]
    influence=sum(R(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g)) for i in range(n))
    ck(influence==sum(s.bit_count()*p[s] for s in range(len(p))))
    return {'t':t,'n':n,'a':a,'p':p,'q':q,'C':ce(p,q),'I':influence}
def combine(ds):
    ns=[d['n'] for d in ds]; n=sum(ns); aa=R(1)
    for d in ds:aa*=d['a']
    table=[]; Q=[R(0)]*(1<<n)
    for x in range(1<<n):
        shift=0; value=R(1); prob=R(1)
        for d in ds:
            s=(x>>shift)&((1<<d['n'])-1); shift+=d['n']
            value*=d['t'][s]
            prob*=d['a'] if not s else (1-d['a'])*d['q'][s]
        table.append(value)
        if x:Q[x]=prob/(1-aa)
    ck(sum(Q)==1)
    g=[2*x-1 for x in table]; p=[x*x for x in walsh(g)]; C=ce(p,Q)
    I=sum(R(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g)) for i in range(n))
    ck(I==sum(aa/d['a']*d['I'] for d in ds))
    expected={}
    for d in ds:add(expected,d['C'],aa/d['a'])
    activation={}
    for d in ds:add(activation,ent([d['a'],1-d['a']]),4*aa)
    add(activation,ent([aa,1-aa]),-4*aa)
    add(expected,activation)
    ck(C==expected)
    aug=add(dict(C),phi(aa)); rhs={}
    for d in ds:add(rhs,add(dict(d['C']),phi(d['a'])),aa/d['a'])
    ck(aug==rhs)
    # Independent complete reconstruction of the uniform three-sector code.
    if len(ds)==2:
        q3=[]
        for x in range(len(Q)):
            s=x&((1<<ns[0])-1); t=x>>ns[0]
            q3.append(R(0) if not x else (ds[0]['q'][s] if s else 1)*(ds[1]['q'][t] if t else 1)/3)
        ck(sum(q3)==1)
        rhs3=add({},lg(R(3)),4*aa*(1-aa))
        add(rhs3,ds[0]['C'],ds[1]['a']);add(rhs3,ds[1]['C'],ds[0]['a'])
        ck(ce(p,q3)==rhs3)
        theta=[R(1,3),R(2,5)]; B=theta[0]*theta[1]; qt=[]
        for x in range(len(Q)):
            s=x&((1<<ns[0])-1);t=x>>ns[0]
            qt.append(R(0) if not x else ((1-theta[0])*ds[0]['q'][s] if s else theta[0])*((1-theta[1])*ds[1]['q'][t] if t else theta[1])/(1-B))
        ck(sum(qt)==1)
        residual={}
        for d,th in zip(ds,theta):add(residual,kl(d['a'],th),4*aa)
        add(residual,kl(aa,B),-4*aa)
        ck(ce(p,qt)==add(dict(C),residual))
    return {'t':table,'n':n,'a':aa,'p':p,'q':Q,'C':C,'I':I}
def source_checks():
    pins=[]
    for agent,run,cid,expected in [
      ('A008','20261023T062437Z-fleet03-A008-gate-label-compression','A008-RARE-CHILD-MOMENT-AND-FIXED-POLARITY-MIXTURE-OBSTRUCTION','8665cf2638011cb0dffa64b7c0cad0b347746eeb92dc2541e4bbc262ce55e6e5'),
      ('A015','20261023T110145Z-fleet03-A015-minterm-barrier-analysis','A015-ONCE-TAGGED-JOINT-DICTIONARY-REFERENCE','2ab314e33940b8c5c4555a26811c7fa8f3413f0359afa3382937915c0b502bd1')]:
        path=ROOT.parents[2]/agent/'runs'/run/'CLAIMS.json'
        claims=json.loads(path.read_text(encoding='utf-8-sig')); c=next(x for x in claims if x['claim_id']==cid)
        payload={'statement':c['exact_statement'],'hypotheses':c['hypotheses']}
        raw=c['exact_statement'].encode() if agent=='A015' else json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
        digest=hashlib.sha256(raw).hexdigest()
        ck(digest==expected==c['statement_sha256']);pins.append({'path':str(path),'statement_sha256':digest})
    return pins
def moments():
    t=R(17,20)
    cert=sum(t**c/R((c+1)*(c+2)) for c in range(17))+t**17/18
    ck(cert<R(4,5))
    fixtures=0
    for z in [R(1),R(2),R(4)]:
        lam=[R(1,8),R(1,64)];xs=[x/16 for x in lam];a0=sum(xs);mark=lam[1]
        ck(z*mark<=R(1,16) and z*a0<=R(1,16))
        D=(1+xs[0])*(1+xs[1])-1; H=R(0)
        for height in range(4):
            child=(lam[0]+z*lam[1])*H
            # Truncation gives a finite-height, finite-offspring subcollection.
            H=sum(child**c/R((c+1)*(c+2)) for c in range(7))
            ck(H<=R(4,5))
            root=((1+z*xs[0]*H)*(1+z*xs[1]*H)-1)/(z*D)
            ck(root<=R(16,19));fixtures+=1
    return {'offspring_certificate_numerator':str(cert.numerator),'offspring_certificate_denominator':str(cert.denominator),'finite_root_fixtures':fixtures}
def overlap():
    u=[R(0),R(1),R(1),R(1)]
    physical=walsh([2*x-1 for x in u]); virtual=walsh([2*u[x&3]*u[x>>2]-1 for x in range(16)])
    pushed=[R(0)]*4; signed=[R(0)]*4
    for s,c in enumerate(virtual):pushed[(s&3)^(s>>2)]+=c*c;signed[(s&3)^(s>>2)]+=c
    ck(pushed==[R(1,16)]+[R(5,16)]*3)
    ck([c*c for c in physical]==[R(1,4)]*4);ck(signed==physical);ck(pushed!=[c*c for c in physical])
    return {'pushforward_squared':list(map(str,pushed)),'actual_squared':list(map(str,[c*c for c in physical]))}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
    inds=[indicator(2,m) for m in range(1,15)]; one=[indicator(1,m) for m in [1,2]]
    if args.pilot:inds=inds[:2]
    cases=0
    for style in [0,1]:
        dd=[data(t,style) for t in inds];oo=[data(t,style) for t in one]
        for a,b in product(dd,repeat=2):combine([a,b]);cases+=1
        for a,b,c in product(dd,dd,oo):
            flat=combine([a,b,c]);nested=combine([combine([a,b]),c]);ck(flat['q']==nested['q']);ck(flat['C']==nested['C']);cases+=1
        for a,b,c,d in product(oo,repeat=4):
            flat=combine([a,b,c,d]);nested=combine([combine([a,b]),combine([c,d])]);ck(flat['q']==nested['q']);ck(flat['C']==nested['C']);cases+=1
    expected=56 if args.pilot else 1208
    # Pilot 2 styles*(2^2 + 2^2*2 + 2^4) = 56; frozen display 64 corrected in SPEC_NOTES.
    ck(cases==expected)
    result={'version':'A007-normalizer-telescope-v1','pilot':args.pilot,'cases':cases,'assertions':count,'moments':moments(),'overlap':overlap(),'source_pins':source_checks()}
    result['assertions']=count;result['elapsed_seconds']=time.perf_counter()-START
    ck(result['elapsed_seconds']<55)
    result['assertions']=count
    (ROOT/'out').mkdir(exist_ok=True)
    out=ROOT/'out'/('pilot.json' if args.pilot else 'full.json');out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'PASS':True,'pilot':args.pilot,'cases':cases,'assertions':count,'elapsed_seconds':result['elapsed_seconds']}))
if __name__=='__main__':main()
