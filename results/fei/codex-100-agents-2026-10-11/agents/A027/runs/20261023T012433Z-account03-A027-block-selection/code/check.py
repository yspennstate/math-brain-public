import exact as x
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import itertools,json,sys,time,hashlib
RUN=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
START=time.monotonic();COUNTS={}
CCTL=Q(21,4)
def ck(ok,label):
    assert ok,label
    COUNTS[label]=COUNTS.get(label,0)+1
    if time.monotonic()-START>(60 if PILOT else 300):raise RuntimeError('frozen runtime cap')
def log(q):
    assert q>0
    return x.add((1,x.factor(q.numerator)),(-1,x.factor(q.denominator)))
@lru_cache(None)
def point(r):return (-1,)+(1,)*((1<<r)-1)
@lru_cache(None)
def G(r,d):return {} if r==0 else x.add((d,x.Hplus(point(r))),(1,x.R(Q(1,1<<r),d)))
@lru_cache(None)
def Gp(r,d):
    if r==0:return {}
    p=Q(1,1<<r);V=4*p*(1-p)
    return x.add((1,x.Hplus(point(r))),(4*(1-2*d),x.eta(p*p)),(2*(1-2*d)*V,{2:Q(1)}),(-4*V*d,log(d) if d else {}),(8*p*(1-2*p*d),log(1-2*p*d)),(-8*p*(1-2*d),log(1-2*d)))
def tangent(r,t,d):return x.add((1,G(r,t)),(d-t,Gp(r,t)))
def gap(r,t,d):return x.add((1,G(r,d)),(-1,tangent(r,t,d)))
def enc(e):
    lo,hi=x.bounds(e)
    return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(lo),str(hi)]}
def eligible(d):return d<Q(1,2) and 1-4*d+2*d*d>=0
def shuffles(r):
    for k in range(r+1):
        for ds in itertools.combinations(range(3+k),3):
            ds=set(ds);i=j=0;order=[]
            for z in range(3+k):
                if z in ds:order.append(i);i+=1
                else:order.append(7+j);j+=1
            yield tuple(order)
def adaptive(fixed,r,mode,u):
    qdata=sum(j in fixed for j in range(3));qc=sum(7+j in fixed for j in range(r))
    sel=fixed.get(2,None)
    if mode==0:
        if qdata<3:return qdata
        return 7+qc if sel==0 and qc<r else None
    if mode==1:
        if qdata==0:return 0
        if qc==0:return 7
        if qdata<3:return qdata
        return 7+qc if sel==1 and qc<min(2,r) else None
    if mode==2:
        if qdata<2:return qdata
        if qdata==2:
            d=x.neg(x.restrict(u,tuple(sorted((j,b) for j,b in fixed.items() if j<7))))
            if qc==0 and d>Q(1,8):return 7
            return 2
        return None
    if qdata==0:return 0
    if qc==0:return 7
    if qdata==1:return 1
    if qdata==2:
        if qc<min(2,r):return 7+qc
        return 2
    return 7+qc if sel==0 and qc<r else None

CASES=POSITIVE=0;WITNESS=None
def case(u,r,order=None,mode=None):
    global CASES,POSITIVE,WITNESS
    t=x.neg(u);p0=Q(1,1<<r);F=x.activate(u,point(r));rootH=x.H(F);rootI=x.I(F)
    leaves=[];nodes=[]
    def state(fixed):
        failed=any(fixed.get(7+j,0)==1 for j in range(r))
        s=r-sum(7+j in fixed for j in range(r))
        v=x.restrict(u,tuple(sorted((j,b) for j,b in fixed.items() if j<7)))
        f=x.restrict(F,tuple(sorted(fixed.items())))
        if failed:ck(all(z==1 for z in f),'actual failed-control leaf constant')
        else:ck(f==x.activate(v,point(s)),'actual active physical restriction')
        return failed,s,v,f
    def walk(fixed,w,depth):
        failed,s,v,f=state(fixed);d=x.neg(v)
        if failed or all(z==f[0] for z in f):j=None
        elif order is not None:j=order[depth] if depth<len(order) else None
        else:j=adaptive(fixed,r,mode,u)
        if j is None:
            leaves.append((w,failed,s,v,f));return
        ck(j not in fixed,'no physical query reused')
        children=[]
        for bit in (0,1):
            child=dict(fixed);child[j]=bit;children.append(state(child))
        dh=x.add((1,x.H(f)),(Q(-1,2),x.H(children[0][3])),(Q(-1,2),x.H(children[1][3])))
        idx=j-sum(k<j for k in fixed);q=x.inf(f,idx)
        U=gap(s,t,d);ck(x.bounds(U)[0]>=0,'same root tangent bank nonnegative')
        if j<7:
            cdh=x.add((1,x.H(v)),(Q(-1,2),x.H(children[0][2])),(Q(-1,2),x.H(children[1][2])))
            coreidx=j-sum(k<j for k in fixed if k<7)
            ck(q==Q(1,1<<s)*x.inf(v,coreidx),'exact physical core influence scaling')
            e=x.add((1,dh),(-Q(1,1<<s),cdh))
            expected=x.add((1,G(s,d)),(Q(-1,2),G(s,x.neg(children[0][2]))),(Q(-1,2),G(s,x.neg(children[1][2]))))
            ck(e==expected,'FULL data correction includes structural cost')
            bankafter=x.add((Q(1,2),gap(s,t,x.neg(children[0][2]))),(Q(1,2),gap(s,t,x.neg(children[1][2]))))
            ck(x.add((1,U),(-1,bankafter))==e,'same bank pays signed DATA debit')
            aa={};release={}
        else:
            ck(s>=1,'live control exists')
            ck(q==2*Q(1,1<<s)*d,'actual own queried control influence')
            expected=x.add((1,G(s,d)),(Q(-1,2),G(s-1,d)))
            ck(dh==expected,'exact actual control entropy decrement')
            ck(expected==G(1,2*Q(1,1<<s)*d),'independent one-bit rescaling h_s(d)=A(2p_s*d)')
            aa=x.add((1,tangent(s,t,d)),(Q(-1,2),tangent(s-1,t,d)))
            release=x.add((1,U),(Q(-1,2),gap(s-1,t,d)))
            ck(release==x.add((1,dh),(-1,aa)),'control price releases SAME original account')
            ck(x.bounds(release)[0]>=0,'control never renews supporting-line bank')
            ck(x.bounds(x.add((1,aa),(-CCTL*q,{2:Q(1)})))[1]<=0,'signed control tangent paid by OWN influence')
            ck(x.bounds(x.add((1,dh),(-CCTL*q,{2:Q(1)})))[1]<=0,'certified actual one-bit price21/4')
            e=dh;bankafter=x.add((Q(1,2),gap(s-1,t,d)))
        nodes.append({'w':w,'fixed':tuple(sorted(fixed.items())),'j':j,'s':s,'d':d,'q':q,'e':e,'aa':aa,'release':release,'before':U,'after':bankafter})
        for bit in (0,1):
            child=dict(fixed);child[j]=bit;walk(child,w/2,depth+1)
    walk({},Q(1),0)
    lh=ph={};li=pi=Q(0);mass=Q(0);B={};Qcore=Qcontrol=Q(0);bill={};corrections={}
    for w,failed,s,v,f in leaves:
        lh=x.add((1,lh),(w,x.H(f)));li+=w*x.I(f)
        if not failed:
            d=x.neg(v);ck(eligible(d),'complete projected endpoint band')
            mass+=w*Q(1,1<<s)/p0;ph=x.add((1,ph),(w*Q(1,1<<s)/p0,x.H(v)));pi+=w*Q(1,1<<s)/p0*x.I(v)
            B=x.add((1,B),(w,gap(s,t,d)))
    for n in nodes:
        w=n['w'];corrections=x.add((1,corrections),(w,n['e']))
        if n['j']<7:
            Qcore+=w*n['q']
            if x.bounds(n['e'])[0]>0:POSITIVE+=1
        else:Qcontrol+=w*n['q'];bill=x.add((1,bill),(w,n['aa']))
    ck(mass==1,'ORIGINAL-input projected leaf weights normalize')
    ck(Qcore==p0*(x.I(u)-pi),'actual original-input projected core budget')
    ck(rootI==Qcore+Qcontrol+li,'complete physical influence incl BOTH terminals')
    E=x.add((1,rootH),(-1,lh),(-p0,x.H(u)),(p0,ph))
    ck(E==corrections,'all signed local corrections telescope')
    ck(E==x.add((1,bill),(-1,B)),'EXACT mixed-history SAME-root bank identity')
    ck(x.bounds(B)[0]>=0,'full terminal bank nonnegative')
    ck(x.bounds(x.add((1,E),(-CCTL*Qcontrol,{2:Q(1)})))[1]<=0,'full mixed zero-core-surcharge price21/4')
    # Every recursion prefix in DFS is a genuine physical frontier, including its opposite siblings.
    balance={}
    for n in nodes:
        balance=x.add((1,balance),(-n['w'],n['before']),(n['w'],n['after']))
        ck(x.bounds(balance)[0]>=0,'nonnegative SAME bank at EVERY DFS frontier')
    ck(balance==B,'no bank issuance at descendants')
    if r==2 and order==(0,7,1,2) and t==Q(7,128) and WITNESS is None:
        exitnodes=[n for n in nodes if n['j']==2 and x.bounds(n['e'])[0]>0]
        if exitnodes:
            WITNESS={'r':r,'root_bias':str(t),'order':list(order),'root_I':str(rootI),'queried_core_I':str(Qcore),'queried_control_I':str(Qcontrol),'full_terminal_I':str(li),'full_signed_error':enc(E),'control_tangent_bill':enc(bill),'frontier_bank':enc(B),'positive_exit':enc(exitnodes[0]['e']),'control_releases':[enc(n['release']) for n in nodes if n['j']>=7],'full_terminal_entropy':enc(lh)}
    CASES+=1

sets=[set(),{0},{0,1,2},{0,1,2,3},{0,1,2,4}]
pairs=list(itertools.product(range(5),repeat=2))
if PILOT:pairs=[(2,3)]
for gi,hi in pairs:
    g=tuple(-1 if j in sets[gi] else 1 for j in range(16));h=tuple(-1 if j in sets[hi] else 1 for j in range(16))
    u=tuple((g[j>>3] if not(j&4) else h[j>>3]) if not(j&3) else 1 for j in range(128))
    for r in ([2] if PILOT else [1,2,3]):
        for order in shuffles(r):case(u,r,order=order)
        for mode in range(4):case(u,r,mode=mode)
        for fn in [x.spectrum,x.H,x.inf,x.I,x.restrict,x.activate,x.identity,G,Gp]:fn.cache_clear()

guards=[]
pricecert=x.add((1,Gp(1,Q(1,8))),(Q(1,6),log(Q(9,7))))
ck(x.bounds(pricecert)[1]<CCTL,'analytic global derivative bound C<21/4 certified')
if not PILOT:
    s=Q(1,16);b=Q(3,10)
    tangentcert=x.add((1,G(1,b)),(-1,G(1,s)),(-(b-s),Gp(1,s)))
    ck(x.bounds(tangentcert)[0]>Q(17,1000),'root supporting-line scalar certificate reproduced')
    u=(-1,)+(1,)*15;F=x.activate(u,point(1));e=x.add((1,x.H(F)),(Q(-1,2),x.H(u)))
    ck(e==G(1,Q(1,16)) and x.bounds(e)[0]>0,'actual endpoint-band omission refuted')
    guards.append({'name':'endpoint-band omitted','root_bias':'1/16','complete_core_leaf_biases':['0','1'],'control_query_budget':'0','positive_full_error':enc(e)})
    g=tuple(-1 if j<3 else 1 for j in range(16));h=tuple(-1 if j<4 else 1 for j in range(16));u=tuple(g[j//2] if not(j&1) else h[j//2] for j in range(32))
    e=x.add((1,G(1,x.neg(u))),(Q(-1,2),G(1,x.neg(g))),(Q(-1,2),G(1,x.neg(h))))
    ck(x.bounds(e)[0]>0,'actual root-condition omission refuted')
    guards.append({'name':'root-condition omitted','root_bias':'7/32','complete_core_leaf_biases':['3/16','1/4'],'control_query_budget':'0','positive_full_error':enc(e)})
else:tangentcert={}
ck(WITNESS is not None,'mixed positive-exit witness after actual control exposure')
result={'status':'PASS','cases':CASES,'positive_DATA_nodes':POSITIVE,'assertions':sum(COUNTS.values()),'counts':COUNTS,'elapsed_seconds':time.monotonic()-START,'witness':WITNESS,'guards':guards,'tangent_certificate':enc(tangentcert),'control_price_certificate':enc(pricecert),'control_price':'21/4','helper_sha256':hashlib.sha256((RUN/'code/exact.py').read_bytes()).hexdigest()}
(RUN/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['counts','witness','guards','tangent_certificate','control_price_certificate']}))
