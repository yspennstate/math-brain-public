from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'code/check.py';ns={'__file__':str(p)}
exec(p.read_text(encoding='utf-8').split('direct=[]')[0],ns)
add,phi,const,positive,ZERO=[ns[k] for k in ['add','phi','const','positive','ZERO']]
reserve=ns['ns']['reserve'];child=ns['child'];enc=ns['enc']
checks=0;start=time.perf_counter()
def ck(v):
    global checks
    checks+=1;assert v,checks;assert time.perf_counter()-start<55
def rw(t):
    # Recursive even/odd character transform, independent of the main FWHT.
    if len(t)==1:return tuple(t)
    e,o=rw(t[::2]),rw(t[1::2]);a=[]
    for x,y in zip(e,o):a.extend((x+y,x-y))
    return tuple(a)
def entropy(t):return add(*((1,phi(F(v*v,len(t)**2))) for v in rw(t) if v))
def mean(t):return F(sum(t),len(t))
def weights(m):return tuple((1+m[(j+1)%3]*m[(j+2)%3]-m[j]*(m[(j+1)%3]+m[(j+2)%3]))/4 for j in range(3))
g,a,b,labels=ns['controller'](4);nc=5
cuts=[tuple(-1 if j==l else 1 for l in labels) for j in range(3)]
cutres=[reserve(h,tuple(range(nc)),1) for h in cuts]
q=[F(labels.count(j),len(labels)) for j in range(3)]
PD=(1,1,1,-1);Maj=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
Tag=tuple(PD[x>>1]*(1 if not x&1 else -1) for x in range(8))
def mix(lab,cs):
    n=len(lab).bit_length()-1;dims=[len(t).bit_length()-1 for t in cs];offs=[n,n+dims[0],n+dims[0]+dims[1]]
    return tuple(cs[lab[x&(len(lab)-1)]][(x>>offs[lab[x&(len(lab)-1)]])&(len(cs[lab[x&(len(lab)-1)]])-1)] for x in range(2**(n+sum(dims))))
def stat(cs):
    t=mix(labels,cs);w=rw(t);den=len(t)**2
    joint={i:F(v*v,den) for i,v in enumerate(w) if v}
    marginal={}
    for mask,p in joint.items():marginal[mask>>nc]=marginal.get(mask>>nc,F(0))+p
    candidate={};offset=0
    for j,core in enumerate(cs):
        for mask,v in enumerate(rw(core)):
            if v:candidate[mask<<offset]=candidate.get(mask<<offset,F(0))+q[j]*F(v*v,len(core)**2)
        offset+=len(core).bit_length()-1
    ck(marginal==candidate);ck(sum(marginal.values())==1)
    H=add(*((1,phi(p)) for p in joint.values()));Hm=add(*((1,phi(p)) for p in marginal.values()))
    T=add(*((q[j],entropy(core)) for j,core in enumerate(cs)))
    J=add((1,Hm),(-1,T))
    L=add(*((marginal[mask>>nc],phi(p/marginal[mask>>nc])) for mask,p in joint.items()))
    ck(H==add((1,T),(1,J),(1,L)))
    m=[mean(core) for core in cs];ww=weights(m);P=add(*((ww[j],cutres[j]) for j in range(3)))
    R=add(*((1-m[j]**2,phi(q[j])) for j in range(3)))
    for core in cs:ck(entropy(core)==const(2))
    return dict(H=H,T=T,J=J,L=L,P=P,R=R,means=[str(x) for x in m],source_entropy=[entropy(core) for core in cs])
root=stat((Tag,Maj,Tag));mid=[];leaves=[]
for sa in (0,1):
    c0=child(Tag,0,sa);mid.append(stat((c0,Maj,Tag)))
    row=[]
    for sb in (0,1):row.append(stat((c0,Maj,child(Tag,0,sb))))
    leaves.append(row)
def avg(xs,key):return add(*((F(1,len(xs)),x[key]) for x in xs))
ck(root['H']==avg(mid,'H')) # genuine first-query entropy plateau
ck(root['P']==avg(mid,'P'))
for i in (0,1):ck(mid[i]['P']==avg(leaves[i],'P'))
flat=leaves[0]+leaves[1];ck(root['P']==avg(flat,'P'))
dataJ=add((1,root['J']),(-1,avg(mid,'J')))
dataL=add((1,root['L']),(-1,avg(mid,'L')))
for i in (0,1):
    dataJ=add((1,dataJ),(F(1,2),mid[i]['J']),(-F(1,2),avg(leaves[i],'J')))
    dataL=add((1,dataL),(F(1,2),mid[i]['L']),(-F(1,2),avg(leaves[i],'L')))
ck(dataJ==add((1,root['J']),(-1,avg(flat,'J'))))
ck(dataL==add((1,root['L']),(-1,avg(flat,'L'))))
ck(add((1,root['H']),(-1,avg(flat,'H')))==add((1,dataJ),(1,dataL)))
target=leaves[0][1];ck(target['means']==['1/2','0','-1/2'])
c=ns['closed'](4);cs=(PD,Maj,tuple(-x for x in PD));f=mix(labels,cs)
df=add((1,entropy(f)),(-F(1,2),entropy(child(f,0,0))),(-F(1,2),entropy(child(f,0,1))))
ck(df==c['df'])
slacks=[]
for h,res in zip(cuts,cutres):
    kids=[child(h,0,s) for s in (0,1)]
    dh=add((1,entropy(h)),(-F(1,2),entropy(kids[0])),(-F(1,2),entropy(kids[1])))
    inf=F(sum(h[x]!=h[x^1] for x in range(len(h))),len(h))
    slack=add((1,const(inf)),(1,res),(-F(1,2),reserve(kids[0],tuple(range(nc-1)),1)),(-F(1,2),reserve(kids[1],tuple(range(nc-1)),1)),(-1,dh))
    ck(slack==ZERO);slacks.append(slack)
def encode_row(row):return {k:[enc(vv) for vv in v] if k=='source_entropy' else enc(v) if k!='means' else v for k,v in row.items()}
out=dict(status='PASS',checks=checks,full_history_nodes=7,frontier_leaves=4,physical_target_reach='1/4',root=encode_row(root),middle=[encode_row(x) for x in mid],frontier=[encode_row(x) for x in flat],total_signed_DATA_JS_bill=enc(dataJ),total_signed_DATA_structural_bill=enc(dataL),cut_reserves= [enc(x) for x in cutres],actual_unused_target_cut_slacks=[enc(x) for x in slacks],first_tag_entropy_plateau=True,same_original_cut_payload_harmonic=True,both_siblings_retained=True,elapsed_seconds=time.perf_counter()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'out/HISTORY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['root','middle','frontier','cut_reserves']},indent=2))
