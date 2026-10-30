from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'code/check.py';ns={'__file__':str(p)}
exec(p.read_text(encoding='utf-8').split('PD=(1,1,1,-1)')[0],ns)
add,phi,const,ZERO=[ns[k] for k in ('add','phi','const','ZERO')]
entropy,child,mix,qs,cuts,mean=[ns[k] for k in ('entropy','child','mix','qs','cuts','mean')]
reserve,positive=[ns[k] for k in ('reserve','positive')]
start=time.perf_counter();checks=nodes=0
def ck(v):
    global checks
    checks+=1;assert v,checks;assert time.perf_counter()-start<55
v=json.loads((ROOT/'out/VALIDATION.json').read_text(encoding='utf-8'))
w=v['positive_slack_witness'] or v['maximum'];labels=tuple(w['labels']);first=w['query']
order=(first,)+tuple(i for i in range(3) if i!=first)
PD=(1,1,1,-1);di=(1,-1,1,-1)
u=tuple(PD[x>>1] if not x&1 else di[x>>1] for x in range(8))
cores=(u,PD,PD)
def direct(t):
    # Direct character sums, independent of the FWHT algorithm.
    den=len(t)**2
    nums=[sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)) for s in range(len(t))]
    return add(*((count,phi(F(a*a,den))) for a,count in Counter(abs(a) for a in nums if a).items()))
equalcores=(PD,)*3;f=mix(labels,equalcores)
ck(direct(f)==entropy(f))
for sign in (0,1):ck(direct(child(f,first,sign))==entropy(child(f,first,sign)))
for t in cuts(labels):ck(direct(t)==entropy(t))
def weights(m):return tuple((1+m[(j+1)%3]*m[(j+2)%3]-m[j]*(m[(j+1)%3]+m[(j+2)%3]))/4 for j in range(3))
def account(lab,cs,ctrlorder):
    m=tuple(mean(t) for t in cs);q=qs(lab);w=weights(m)
    rr=[reserve(t,ctrlorder,1) if ctrlorder else ZERO for t in cuts(lab)]
    P=add(*((w[j],rr[j]) for j in range(3)))
    R=add(*((1-m[j]**2,phi(q[j])) for j in range(3)))
    A=add(*((q[j],reserve(t,tuple(range(len(t).bit_length()-1)),1)) for j,t in enumerate(cs)))
    return add((1,P),(1,R),(1,A)),P,R,A
root,rootP,rootR,rootA=account(labels,cores,order)
pre=[]
for sign in (0,1):
    cc=(child(u,0,sign),PD,PD);a,pp,rr,aa=account(labels,cc,order)
    pre.append(dict(mean=str(mean(cc[0])),H=ns['encode'](entropy(mix(labels,cc))) if 'encode' in ns else [[p,str(c)] for p,c in entropy(mix(labels,cc))],P=pp,R=rr,A=aa,total=a))
ck(rootP==add((F(1,2),pre[0]['P']),(F(1,2),pre[1]['P'])))
def walk(lab,cs,ctrlorder,steps):
    global nodes
    f=mix(lab,cs);A,P,R,B=account(lab,cs,ctrlorder)
    if not steps:
        ck(len(f)==1);ck(A==ZERO);ck(entropy(f)==ZERO);return
    kind,j=steps[0]
    before=sum(len(t).bit_length()-1 for t in cs[:j])
    i=ctrlorder[0] if kind=='c' else len(lab).bit_length()-1+before
    ck(0<=i<len(f).bit_length()-1)
    inf=F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
    children=[];Hs=[];Ps=[]
    for s in (0,1):
        if kind=='c':
            ll=child(lab,i,s);cc=cs;oo=tuple(k-(k>i) for k in ctrlorder[1:])
        else:
            ll=lab;cc=list(cs);cc[j]=child(cc[j],0,s);cc=tuple(cc);oo=ctrlorder
        Ac,Pc,Rc,Bc=account(ll,cc,oo);children.append(Ac);Ps.append(Pc);Hs.append(entropy(mix(ll,cc)))
        walk(ll,cc,oo,steps[1:])
    D=add((1,entropy(f)),(-F(1,2),Hs[0]),(-F(1,2),Hs[1]))
    residual=add((1,D),(-1,const(15*inf)),(-1,A),(F(1,2),children[0]),(F(1,2),children[1]))
    ck(positive(residual)==ZERO)
    if kind=='d':ck(P==add((F(1,2),Ps[0]),(F(1,2),Ps[1])))
    nodes+=1
steps=(('d',0),)+tuple(('c',0) for _ in range(3))+tuple(('d',j) for j in range(3) for _ in range(2))
walk(labels,cores,order,steps)
# The equal-mean entropy identity really needs independent physical cores.
ck(entropy(PD)!=ns['rhs'](labels,(PD,PD,PD)))
# The actual unused cut slack is positive but insufficient at this non-flat
# surjective node. Do not replace a terminal account by spendable slack.
parse=lambda x:tuple((p,F(c)) for p,c in x)
E=parse(w['E']);s=parse(w['unused_same_cut_slack'])
net=add((1,E),(-1,s))
ck(s==const(F(3,16)))
ck(net==add((F(27,64),ns['expr']({3:1})),(-1,const(F(9,16)))))
ck(positive(add((1,net),(-1,const(F(1,10)))))!=ZERO)
ck(positive(add((1,net),(-1,const(F(7,64)))))==ZERO)
enc=lambda x:[[p,str(c)] for p,c in x]
for row in pre:
    for k in ['P','R','A','total']:row[k]=enc(row[k])
out=dict(status='PASS',checks=checks,internal_tree_nodes=nodes,price=15,labels=labels,controller_order=order,root_account=enc(root),root_cut_account=enc(rootP),root_rarity=enc(rootR),root_core_account=enc(rootA),predecessor_core_means=['1/4','1/2','1/2'],both_data_children=pre,independent_direct_character_sums=True,shared_core_countercontrol=True,remaining_local_debt_after_actual_unused_slack=enc(net),remaining_debt_bounds=['1/10','7/64'],elapsed_seconds=time.perf_counter()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'out/CONTINUATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['both_data_children']},indent=2))
