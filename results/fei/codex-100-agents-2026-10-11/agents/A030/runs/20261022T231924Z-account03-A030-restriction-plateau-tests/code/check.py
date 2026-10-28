from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
import json,time,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[1]/'runs/20261013T212321Z-account05-A030-restriction-plateau-tests/code/check.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('for n in (1,2,3):')[0],ns)
expr,add,const,positive,child,walsh=[ns[k] for k in ['expr','add','const','positive','child','walsh']]
ZERO=();start=time.perf_counter();pilot='--pilot' in sys.argv;limit=55 if pilot else 180
checks=0
def ck(v):
    global checks
    checks+=1;assert v,checks;assert time.perf_counter()-start<limit,'frozen runtime guard'
@lru_cache(None)
def phi(s):
    if not s:return ZERO
    d={}
    for p,e in ns['factors'](s.denominator).items():d[p]=s*e
    for p,e in ns['factors'](s.numerator).items():d[p]=d.get(p,F(0))-s*e
    return expr(d)
def phisq(x):return phi(x*x)
def psi(a,d):return add((1,phisq(a+d)),(1,phisq(d)),(-F(1,2),phisq(a)),(-F(1,2),phisq(a+2*d)))
def Hseq(seq,scale=1):
    den=F((len(seq)*scale)**2)
    return add(*((count,phi(F(a*a,den))) for a,count in Counter(abs(x) for x in walsh(seq) if x).items()))
def enc(x):return [[p,str(c)] for p,c in x]
def smallbounds(x):
    a,b=ns['bounds'](x);D=10**9
    return [str(F((a*D).__floor__(),D)),str(F((b*D).__ceil__(),D))]
def js(q):
    q0,q1,q2=q
    return add((1,phi((q0+q2)/4)),(3,phi(q0/4)),(4,phi(q1/4)),(3,phi(q2/4)),(-1,const(2)))
def closed(r):
    eps=F(1,2**r);t=F(1,2**(r//2));N=2**r
    np=(N+2**(r//2))//2;nm=N-np;p=(1+t)/2;v=F(3,4)
    dh0=add((1,psi(F(1),-eps)),(N-1,const(4*eps*eps)))
    dh1=add((np,psi(-t,eps)),(nm,psi(t,eps)))
    dc0=const(eps)
    dc1=add((1,psi(p,-eps/2)),(np-1,psi(t/2,-eps/2)),(nm,psi(-t/2,-eps/2)))
    da=add((1,psi((t-1)/4,eps/4)),(np-1,psi(t/4,eps/4)),(nm,psi(-t/4,eps/4)))
    df=add((1,da),(v,dc0),(1,dc1))
    rarity=add((1,const(3*eps/8)),(1,phi(p-eps/2)),(-F(1,2),phi(p)),(-F(1,2),phi(p-eps)))
    seed=add((F(5,16),dh0),(F(3,16),dh1))
    E=add((1,df),(-1,seed),(-1,rarity));d=eps/2
    q0=(F(0),p,1-p);q1=(eps,p-eps,1-p);q=(eps/2,p-eps/2,1-p)
    J=add((1,js(q)),(-F(1,2),js(q0)),(-F(1,2),js(q1)))
    ck(positive(add((-1,J)))==ZERO);ck(positive(add((-1,rarity)))==ZERO)
    ck(positive(dh0)!=ZERO);ck(positive(dh1)!=ZERO)
    # At C=1 positive raw cut debit forces the least Bellman reserve to
    # have zero unused slack regardless of its actual child continuations.
    raw0=add((1,dh0),(-1,const(eps)));raw1=add((1,dh1),(-1,const(eps)))
    if r>=4:ck(positive(raw0)!=ZERO);ck(positive(raw1)!=ZERO)
    return dict(r=r,eps=eps,t=t,np=np,nm=nm,df=df,dh=[dh0,dh1,ZERO],rarity=rarity,seed=seed,E=E,d=d,J=J,q=q,child_q=[q0,q1])
def controller(r):
    g=tuple(-1 if sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(r//2))%2 else 1 for z in range(2**r))
    a=tuple(1 if v==1 else 2 for v in g);b=(0,)+a[1:]
    # s is coordinate0: preserve the exact old/new child tables.
    root=tuple(a[x>>1] if not x&1 else b[x>>1] for x in range(2**(r+1)))
    return g,a,b,root
def Hout(lab):
    # Independent direct row-sector expansion, with no sign multiplicity use.
    means2=(1,0,-1);V=(F(3,4),F(1),F(3,4))
    hs=Hseq(tuple(means2[j] for j in lab),scale=2)
    q=[F(lab.count(j),len(lab)) for j in range(3)]
    for j in range(3):
        c=tuple(int(x==j) for x in lab)
        hs=add((1,hs),(V[j],Hseq(c)),(q[j],add((1,const(2)),(-1,phi(F(means2[j]**2,4))))))
    return hs
def rawF(lab):
    cores=((1,1,1,-1),tuple(1 if x.bit_count()<=1 else -1 for x in range(8)),(-1,-1,-1,1))
    n=len(lab).bit_length()-1;offs=(n,n+2,n+5)
    return tuple(cores[lab[x&(len(lab)-1)]][(x>>offs[lab[x&(len(lab)-1)]])&(len(cores[lab[x&(len(lab)-1)]])-1)] for x in range(2**(n+7)))
direct=[]
for r in ([2,4] if pilot else [4,6,8]):
    c=closed(r);g,a,b,root=controller(r)
    ck(set(walsh(g))=={-2**(r//2),2**(r//2)})
    ck(sum(g)==2**(r//2));ck(g[0]==1);ck(len(set(root))==3)
    df=add((1,Hout(root)),(-F(1,2),Hout(a)),(-F(1,2),Hout(b)))
    ck(df==c['df'])
    for j in range(3):
        hh=tuple(-1 if label==j else 1 for label in root)
        dh=add((1,Hseq(hh)),(-F(1,2),Hseq(child(hh,0,0))),(-F(1,2),Hseq(child(hh,0,1))))
        ck(dh==c['dh'][j])
    if r in ([2,4] if pilot else [4]):
        f=rawF(root);ck(Hseq(f)==Hout(root));ck(Hseq(child(f,0,0))==Hout(a));ck(Hseq(child(f,0,1))==Hout(b))
        ck(F(sum(f[x]!=f[x^1] for x in range(len(f))),len(f))==c['d'])
        # Every z influence is bounded below by 1/4-eps. This check is
        # independent direct physical edges on the actual full truth table.
        for i in range(1,r+1):ck(F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))>=F(1,4)-c['eps'])
    direct.append(r)
rows=[]
for r in ([2,4,6,8] if pilot else [4,8,12,16,20,24]):
    c=closed(r);ratio=add((1/c['d'],c['E']));jr=add((1/c['d'],c['J']));remaining=add((1,ratio),(-1,jr))
    # Exact residual after removing the proposed r/4 leading term; its
    # convergence is diagnostic only. The analytic Taylor bound proves it.
    centered=add((1,ratio),(-1,const(F(r,4))))
    rows.append(dict(r=r,influence=str(c['d']),E=enc(c['E']),E_over_d=enc(ratio),E_over_d_bounds=smallbounds(ratio),JS_release=enc(c['J']),JS_release_over_d_bounds=smallbounds(jr),after_JS_over_d_bounds=smallbounds(remaining),centered_bounds=smallbounds(centered),raw_seed_debits_positive_at_C1=r>=4,original_cut_slack_at_C1='0 for r>=4 by strictly positive root debit and same h2 continuation',both_child_label_probabilities=[[str(x) for x in q] for q in c['child_q']],both_child_entropies_retained=True))
out=dict(status='PASS',pilot=pilot,helper_version='A030-unequal-mean-bent-new-label-v1',checks=checks,compact_rows=rows,direct_controller_r=direct,raw_full_F_r=[2,4] if pilot else [4],elapsed_seconds=time.perf_counter()-start,certified_signs=ns['signs'],exact_zero_signs=ns['zeros'],code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest())
(ROOT/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='compact_rows'},indent=2));print(json.dumps([{'r':x['r'],'E/d':x['E_over_d_bounds'],'JSrelease/d':x['JS_release_over_d_bounds'],'after_JS/d':x['after_JS_over_d_bounds']} for x in rows],indent=2))
