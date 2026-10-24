from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json, time, hashlib
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
START=time.perf_counter()
A=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
B=[1-v*v for v in A]
checks=0
def ck(v):
    global checks
    checks+=1
    assert v, checks
    assert time.perf_counter()-START<60, 'frozen compute timeout'
def walsh(f):
    # Deliberately direct character sums, independent of author's fast transform.
    return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(len(f))]
def law(f):
    return [Q(w*w,len(f)**2) for w in walsh(f)]
def factors(v):
    d=2
    while d*d<=v:
        e=0
        while v%d==0: v//=d; e+=1
        if e: yield d,e
        d+=1
    if v>1: yield v,1
def add(*terms):
    r={}
    for scale,d in terms:
        for k,v in d.items(): r[k]=r.get(k,Q(0))+scale*v
    return {k:v for k,v in r.items() if v}
def ent(ps):
    d={}
    for p in ps:
        if not p: continue
        for a,sgn in [(p.numerator,-1),(p.denominator,1)]:
            for prime,e in factors(a): d[prime]=d.get(prime,Q(0))+sgn*p*e
    return {k:v for k,v in d.items() if v}
def ilaw(p): return sum((v*s.bit_count() for s,v in enumerate(p)),Q(0))
def lograt(v):
    r={}
    for a,sgn in [(v.numerator,1),(v.denominator,-1)]:
        for prime,e in factors(a):r[prime]=r.get(prime,Q(0))+sgn*e
    return {p:c for p,c in r.items() if c}
def renyi(row):
    w=walsh(row)
    return lograt(Q(sum(abs(v) for v in w)**2,sum(v*v for v in w)))
def edges(f):
    n=(len(f)-1).bit_length()
    return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f)) for i in range(n)),len(f))
def lnat(v):
    # log(v)=2 sum t^(2j+1)/(2j+1); v in [1,2], t<=1/3.
    t=(v-1)/(v+1); s=Q(0); power=t
    for j in range(48): s+=2*power/(2*j+1); power*=t*t
    return s,s+2*power/((2*48+1)*(1-t*t))
L2=lnat(Q(2))
@lru_cache(None)
def log2(p):
    k=p.bit_length()-1; lo,hi=lnat(Q(p,1<<k))
    return Q(k)+lo/L2[1],Q(k)+hi/L2[0]
def bounds(d):
    lo=hi=Q(0)
    for p,c in d.items():
        x,y=log2(p)
        lo+=c*(x if c>=0 else y); hi+=c*(y if c>=0 else x)
    return lo,hi
def enc(v):
    if isinstance(v,Q): return str(v)
    if isinstance(v,dict): return {str(k):enc(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [enc(x) for x in v]
    return v
def save(name,v): (OUT/name).write_text(json.dumps(enc(v),indent=2)+'\n',encoding='utf-8')
def restricted(row,state):
    free=[i for i in range(4) if state[i]<0]
    inds=[sum((state[i] if state[i]>=0 else ((x>>free.index(i))&1))<<i for i in range(4)) for x in range(1<<len(free))]
    return [row[i] for i in inds]
def completion(a,b,h):
    # u low bits, seed next, z highest.
    return [av+z*bv*hv for z in [1,-1] for hv in h for av,bv in zip(a,b)]
def productlaw(p):
    mass=sum(p); n=(len(p)-1).bit_length()
    if not mass:return True
    marg=[sum(v for s,v in enumerate(p) if s>>i&1)/mass for i in range(n)]
    for s,v in enumerate(p):
        v0=mass
        for i in range(n):v0*=marg[i] if s>>i&1 else 1-marg[i]
        if v!=v0:return False
    return True

ck(walsh(A)==[2]*8+[4,-4,-4,-4,-4,4,4,4])
ck(walsh(B)==[6,-2,-2,-2,6,-2,-2,-2]+[0]*8)
ck(productlaw(law(A)));ck(not productlaw(law(B)))
ck(renyi(A)==lograt(Q(72,5)));ck(renyi(B)==lograt(Q(6)))
HROOT={2:Q(5),3:-Q(9,16)}
HCHILD={2:Q(6),3:-Q(27,16)}
DELTA={2:-Q(1),3:Q(9,8)}
ck(3**5<2**8)
ck(bounds(add((Q(1),{2:Q(1)}),(-1,DELTA)))[0]>Q(1,5))
states=list(product([-1,0,1],repeat=4)); data={}; fixtures=[]
for state in states:
    a,b=restricted(A,state),restricted(B,state)
    f=completion(a,b,[1]); p=law(f)
    h=ent(p); beta=Q(sum(b),len(b)); n=(len(a)-1).bit_length()
    iu=sum((v*(s&((1<<n)-1)).bit_count() for s,v in enumerate(p)),Q(0))
    ck(ilaw(p)==edges(f)); ck(ilaw(p)==iu+beta)
    data[state]={'a':a,'b':b,'H':h,'beta':beta,'Iu':iu,'I':ilaw(p),'S4':add((4,{2:ilaw(p)}),(-1,h))}
    fixtures.append({'state':state,'truth_table':f,'spectrum':p,'H':h,'I':ilaw(p),'beta':beta,'S4':data[state]['S4']})
seedcount=0
for n in range(3):
    for h in product([-1,1],repeat=1<<n):
        seedcount+=1; ph=law(h); hh=ent(ph); ih=edges(h)
        gap=add((1,ent([Q(5,8),Q(3,8)])),(-Q(5,8),renyi(A)),(-Q(3,8),renyi(B)),(-Q(3,8),renyi(h)))
        ck(gap==add((1,{2:Q(3,4),3:-Q(2)}),(-Q(3,8),renyi(h))))
        # Address/seed spectral joint and marginal laws. For a balanced seed,
        # address=1 iff the sampled seed frequency is nonempty.
        joint=[Q(5,8)]+[Q(3,8)*v for v in ph]
        marginal=[Q(3,8)*v+(Q(5,8) if s==0 else 0) for s,v in enumerate(ph)]
        mi=add((1,ent([Q(5,8),Q(3,8)])),(1,ent(marginal)),(-1,ent(joint)))
        if sum(h)==0:ck(mi==ent([Q(5,8),Q(3,8)]))
        for state in states:
            d=data[state]; f=completion(d['a'],d['b'],h); p=law(f)
            ck(all(v in [-1,1] for v in f));ck(sum(p)==1)
            ck(ent(p)==add((1,d['H']),(d['beta'],hh)))
            ck(ilaw(p)==d['I']+d['beta']*ih);ck(edges(f)==ilaw(p))
        ck(data[(-1,)*4]['H']==HROOT)
        for bit in [0,1]:
            ck(data[(-1,-1,-1,bit)]['H']==HCHILD)
            ck(data[(-1,-1,-1,bit)]['I']==(Q(7,4) if bit==0 else Q(3,2)))
        if n<=1:fixtures.append({'seed':h,'truth_table':completion(A,B,h),'spectrum':law(completion(A,B,h))})

# All 108 physical query transitions, with exact seed coefficient conservation.
transitions=[]; failures2=[];failures4=[]
for state,d in data.items():
    for i in range(4):
        if state[i]>=0:continue
        kids=[]
        for bit in [0,1]:
            st=list(state);st[i]=bit;kids.append(data[tuple(st)])
        delta=add((1,d['H']),(-Q(1,2),kids[0]['H']),(-Q(1,2),kids[1]['H']))
        inf=d['I']-(kids[0]['I']+kids[1]['I'])/2
        ck(d['beta']==(kids[0]['beta']+kids[1]['beta'])/2)
        ck(inf>=0)
        c2=add((1,delta),(-2,{2:inf})); c4=add((1,delta),(-4,{2:inf}))
        if bounds(c2)[0]>0: failures2.append((state,i,c2))
        if bounds(c4)[0]>0: failures4.append((state,i,c4))
        transitions.append({'state':state,'query':i,'Delta':delta,'influence':inf,'cost4':c4})
ck(len(transitions)==108)

# Backward induction maximizes total paid cost Delta-4Inf over ALL adaptive
# controller-query trees and stopping cuts. Every comparison has exact log intervals.
dp={}; policy={}
for state in sorted(states,key=lambda s:s.count(-1)):
    d=data[state]; best={}; choice='STOP'
    for tr in transitions:
        if tuple(tr['state'])!=state:continue
        vals=[]
        for bit in [0,1]:
            child=list(state); child[tr['query']]=bit; vals.append(dp[tuple(child)])
        cand=add((1,tr['cost4']),(Q(1,2),vals[0]),(Q(1,2),vals[1]))
        diff=add((1,cand),(-1,best))
        if not diff:continue
        lo,hi=bounds(diff)
        ck(lo>0 or hi<0)
        if lo>0:best=cand;choice=tr['query']
    dp[state]=best;policy[state]=choice
root=(-1,)*4
save('controller_fixtures.json',fixtures)
save('controller_transitions.json',transitions)
save('controller_stopping.json',{'maximum_cost4':dp[root],'bounds':bounds(dp[root]),'policy':[{'state':s,'action':policy[s],'cost':dp[s]} for s in states]})
result={'PASS':True,'checks':checks,'seconds':time.perf_counter()-START,'states':len(states),'edges':len(transitions),'seeds':seedcount,'state_seed_pairs':len(states)*seedcount,'local_rate2_failures':failures2,'local_rate4_failures':failures4,'root_maximum_stopping_cost4':dp[root],'root_bank4':data[root]['S4'],'first_query_Delta':DELTA,'first_query_rate2_release':add((1,{2:Q(1)}),(-1,DELTA))}
save('validation.json',result)
print(json.dumps(enc({k:v for k,v in result.items() if not k.endswith('failures')}),indent=2))
print('local failures rate2/rate4:',len(failures2),len(failures4))
