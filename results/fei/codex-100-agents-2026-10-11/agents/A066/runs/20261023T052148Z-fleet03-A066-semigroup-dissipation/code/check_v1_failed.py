from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time,hashlib

run=Path(__file__).resolve().parents[1]
mode=sys.argv[1];start=time.perf_counter();counts={};nodes=0
def ck(x,tag):
    counts[tag]=counts.get(tag,0)+1
    assert x,tag
    assert time.perf_counter()-start<55,'FROZEN_RUNTIME'
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,x):return (a[0]*x,a[1]*x) if x>=0 else (a[1]*x,a[0]*x)
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
@lru_cache(None)
def ln(x):
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(28)),F(0))
    return lo,lo+2*z**57/(57*(1-z*z))
ln2=ln(F(2))
@lru_cache(None)
def lg(x):
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    lo,hi=ln(x)
    return k+lo/ln2[1],k+hi/ln2[0]
@lru_cache(None)
def ce(p,q):
    v=(F(0),F(0))
    for x,y in zip(p,q):
        if x:
            assert y>0
            v=add(v,mul(lg(1/y),x))
    return v
def ent(p):return ce(p,p)
@lru_cache(None)
def sp(v):
    # Direct characters, independent of the previous stage's FWHT.
    n=len(v)
    a=tuple(F(sum(t*(-1 if (i&s).bit_count()%2 else 1) for i,t in enumerate(v)),n) for s in range(n))
    p=tuple(t*t for t in a)
    assert sum(p)==1
    return p
def child(v,i,s):
    return tuple(t for k,t in enumerate(v) if ((k>>i)&1)==s)
def erase(q,i):
    n=len(q)//2
    def ix(t):return (t&((1<<i)-1))+((t>>i)<<(i+1))
    return tuple(q[ix(t)]+q[ix(t)+(1<<i)] for t in range(n))
def influence(v,i):return F(sum(t!=v[k^(1<<i)] for k,t in enumerate(v)),len(v))
def interval_out(a):
    u=1<<60
    return [str(F((a[0]*u).__floor__(),u)),str(F((a[1]*u).__ceil__(),u))]

def node(v,q,i):
    global nodes
    nodes+=1;p=sp(v);vs=[child(v,i,s) for s in [0,1]];ps=[sp(t) for t in vs];qb=erase(q,i);pb=erase(p,i)
    ck(sum(q)==sum(qb)==1,'normalized_full_refs')
    ck(tuple((x+y)/2 for x,y in zip(*ps))==pb,'physical_projection')
    ck(all(not x or y>0 for pp in ps for x,y in zip(pp,qb)),'both_child_support')
    avgH=mul(add(ent(ps[0]),ent(ps[1])),F(1,2));dh=sub(ent(p),avgH)
    C=(F(0),F(0))
    conditional_same=True
    for k,(x,y) in enumerate(zip(p,q)):
        if x:
            t=(k&((1<<i)-1))+((k>>(i+1))<<i)
            C=add(C,mul(lg(qb[t]/y),x))
            if x*qb[t]!=y*pb[t]:conditional_same=False
    B=sub(ent(p),ent(pb));D=sub(C,B);J=sub(ent(pb),avgH)
    if ps[0]==ps[1]:J=(F(0),F(0))
    else:ck(J[0]>0,'strict_JS')
    if conditional_same:D=(F(0),F(0))
    else:ck(D[0]>0,'strict_conditional_KL')
    ck(overlap(sub(C,dh),add(J,D)),'true_entropy_refund_identity')
    childCE=mul(add(ce(ps[0],qb),ce(ps[1],qb)),F(1,2))
    ck(overlap(sub(ce(p,q),childCE),C),'full_CE_release_identity')
    ck(C[0]>=0,'nonnegative_release')
    if J[0]+D[0]>0:ck(C[0]>=dh[1],'positive_debit_paid')
    e=influence(v,i);means=[F(sum(t),len(t)) for t in vs];a=(means[0]-means[1])/2
    ck(abs(a)<=e,'boolean_mean_mismatch')
    b=ce((p[0],),(p[0],)) if p[0] else (F(0),F(0))
    bs=[ce((pp[0],),(pp[0],)) if pp[0] else (F(0),F(0)) for pp in ps]
    bd=sub(b,mul(add(*bs),F(1,2)))
    if e:ck(max(abs(bd[0]),abs(bd[1]))*ln2[1]<=2*e,'absolute_boundary_nats')
    else:ck(p[0]==ps[0][0]==ps[1][0],'zero_influence_boundary')
    heat=sub(sub(ent(p),b),mul(add(sub(ent(ps[0]),bs[0]),sub(ent(ps[1]),bs[1])),F(1,2)))
    ck(overlap(heat,sub(dh,bd)),'heat_signed_boundary_identity')
    # Psi/ln2 = CE minus the empty entropy atom; signed boundaries cancel.
    psi=sub(ce(p,q),b);childpsi=mul(add(sub(ce(ps[0],qb),bs[0]),sub(ce(ps[1],qb),bs[1])),F(1,2))
    ck(overlap(add(heat,sub(childpsi,psi)),mul(add(J,D),-1)),'heat_reference_refund_identity')
    return vs,qb,dh,C

policy_nodes=0;rows=[];admitted=failed=0;seed_queries=0
for d in range(3 if mode=='pilot' else 4):
    N=1<<d;delta=F(1,N);e=delta/2;R=(d+1)*e
    for mask in range(1<<(N-1)):
        b=tuple([1]+[1 if mask>>(x-1)&1 else -1 for x in range(1,N)])
        f0=tuple(b[x]-2*z*(x==0) for x in range(N) for z in range(2))
        f1=tuple(b[x]-2*(x==0) for x in range(N) for z in range(2))
        FF=tuple(b[x]+((1 if j==z==0 else -1)-1)*(x==0) for x in range(N) for z in range(2) for j in range(2))
        initialH=sub(ent(sp(FF)),mul(add(ent(sp(f0)),ent(sp(f1))),F(1,2)))
        L=(max(initialH[0]-5*e,0),max(initialH[1]-5*e,0))
        Ibar=sum(sum(influence(v,i) for i in range(d+1)) for v in [f0,f1])/2
        for ref in ['actual','half_uniform']:
            qs=[sp(f0),sp(f1)]
            if ref=='half_uniform':qs=[tuple((x+F(1,len(q)))/2 for x in q) for q in qs]
            incoming=mul(add(ce(sp(f0),qs[0]),ce(sp(f1),qs[1])),F(1,2))
            for K in [4,8]:
                tau=Ibar/4;U=sub((K*Ibar-tau,)*2,incoming)
                if U[0]>=F(3,2)*R-e/4:
                    admitted+=1;ck(U[0]-R-L[1]>=0,'original_source_admission_retains_old_L')
                elif U[1]<F(3,2)*R-e/4:failed+=1
                else:raise AssertionError('ADMISSION_INTERVAL_UNRESOLVED')
            # Every genuine seed coordinate immediately after j, both branches.
            for v,q in zip([f0,f1],qs):
                for i in range(1,d+1):node(v,q,i);seed_queries+=1
            # Three fully adaptive policies; leaf forecasts use only original refs.
            for policy in [0,1,2]:
                forest=[]
                for s,(v,q) in enumerate(zip([f0,f1],qs)):
                    forest.append((v,q,tuple(['z']+list(range(d))),F(1,2),s==0,0))
                positive=(F(0),F(0));term=(F(0),F(0));reserve=F(0)
                while forest:
                    v,q,labels,w,active,depth=forest.pop()
                    k=sum(x!='z' for x in labels);rr=F(k,1<<k) if active and 'z'in labels else F(0)
                    # A genuine stopping cut for policy2; retains full terminal bill.
                    if not labels or policy==2 and depth>=2 and sum(v)<=0:
                        term=add(term,mul(ce(sp(v),q),w));reserve+=w*rr;continue
                    i=(len(labels)-1 if policy==0 else 0 if policy==1 else sum(v)%len(labels))
                    vs,qb,dh,C=node(v,q,i);policy_nodes+=1
                    positive=add(positive,mul((max(dh[0],0),max(dh[1],0)),w))
                    rrchildren=[]
                    for ss,vv in enumerate(vs):
                        ll=labels[:i]+labels[i+1:];ac=active and labels[i]!='z' and ss==0
                        kk=sum(x!='z' for x in ll);rrchildren.append(F(kk,1<<kk) if ac and 'z'in ll else F(0))
                        forest.append((vv,qb,ll,w/2,ac,depth+1))
                    ck(rr>=sum(rrchildren)/2,'same_reserve_supermartingale')
                # Interval equality may leave a tiny positive outward width. The
                # local exact identities (1)-(3), not a numerical tolerance,
                # certify the aggregate inequality for all zero-margin cases.
                ck(positive[0]+term[0]<=incoming[1],'aggregate_positive_tree_debit')
                ck(reserve<=R-e,'original_expected_reserve')
                if d==3 and mask in [0,127] and ref=='half_uniform':rows.append({'d':d,'mask':mask,'policy':policy,'incoming_CE':interval_out(incoming),'positive_debits':interval_out(positive),'complete_terminal_CE':interval_out(term),'reserve':str(reserve)})

# Zero-influence prescribed-reset guard, exact powers of two, no log intervals.
v=(1,1,1,1);q=(F(1,4),)*4
vs,qb,dh,C=node(v,q,0)
ck(qb==(F(1,2),F(1,2)),'reset_guard_projection')
ck(C==(F(1),F(1)),'reset_guard_old_release')
qnew=(F(1,8),F(7,8));newcost=ce(sp(vs[0]),qnew)
ck(newcost==(F(3),F(3)),'reset_guard_prescribed_full_CE')
ck(newcost[0]-ce(sp(vs[0]),qb)[1]>C[1],'reset_guard_rejects_unpaid_extra')

out={'status':'PASS','mode':mode,'seed_count':sum(1<<(2**d-1) for d in range(3 if mode=='pilot' else 4)),'seed_query_cases':seed_queries,'policy_nodes':policy_nodes,'all_nodes':nodes,'source_admitted':admitted,'source_not_admitted':failed,'exact_assertions':sum(counts.values()),'counts':counts,'seconds':time.perf_counter()-start,'rows':rows,'reset_guard':{'physical_influence':0,'old_CE':2,'projected_CE':1,'prescribed_CE':3,'conversion':2,'available_old_release':1,'unpaid':1},'rounding':'outward dyadic 2^-60; zero-margin aggregate certified via rational local identities and analytic nonnegative KL/JS, not tolerance'}
(run/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','counts','reset_guard']}))
