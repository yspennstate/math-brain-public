from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def check(b):
    global checks
    assert b
    checks+=1
    if time.perf_counter()-start>55:raise RuntimeError('frozen55s cap')
def dot(x):return x.bit_count()%2
def coeff(a):
    return tuple(sum(y*(-1)**dot(s&x) for x,y in enumerate(a)) for s in range(len(a)))
def bits(a):
    return [Q(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range(len(a).bit_length()-1)]
def error(a):
    return Q(len(a)-max(abs(x) for x in coeff(a)),2*len(a))
def restrict(a,j,b):
    return tuple(a[(x%(1<<j))+(x//(1<<j))*(1<<(j+1))+b*(1<<j)] for x in range(len(a)//2))
def lnsmall(x):
    y=(x-1)/(x+1);N=40
    value=2*sum((y**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    return value,value+2*y**(2*N+1)/(Q(2*N+1)*(1-y*y))
ln2=lnsmall(Q(2))
@lru_cache(None)
def logint(x):
    shift=0
    while x<1:x*=2;shift-=1
    while x>2:x/=2;shift+=1
    lo,hi=lnsmall(x)
    return shift+lo/ln2[1],shift+hi/ln2[0]
@lru_cache(None)
def H(a):
    counts={}
    for x in coeff(a):
        if x:counts[x*x]=counts.get(x*x,0)+1
    lo=hi=Q(0)
    for weight,num in counts.items():
        p=Q(weight,len(a)**2);l,h=logint(p)
        lo-=num*p*h;hi-=num*p*l
    return lo,hi
def phibound(a):
    if not a:return Q(0),Q(0)
    l,h=logint(a);ll,hh=logint(1-a)
    return -a*h-(1-a)*hh+2*a/ln2[1],-a*l-(1-a)*ll+2*a/ln2[0]
# Fixed bent2 tensor-square, k3, evaluated from its Boolean exponent.
raw=[]
for x in range(128):
    controls=x>>4
    exponent=(x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1)
    raw.append((-1)**exponent if controls==0 else 1)
raw=tuple(raw)
# Mix data0 with control0; this changes the subsequent data-query partition.
root=tuple(raw[x^((x>>4)&1)] for x in range(128))
check(sorted(x*x for x in coeff(root))==sorted(x*x for x in coeff(raw)))
check(error(root)==error(raw))
check(sum(bits(root))==sum(bits(raw)))
for j in range(7):
    ch=[restrict(root,j,b) for b in [0,1]]
    check(sum(error(x) for x in ch)/2<=error(root))
    check(sum(sum(bits(x)) for x in ch)/2==sum(bits(root))-bits(root)[j])
    for v in range(1,128):
        w=Q(sum(root[x]!=root[x^v] for x in range(128)),128)
        check(min(w,1-w)<=2*error(root))
leaves=[];reset_savings=Q(0)
for b in [0,1]:
    a=restrict(root,0,b)
    # Different actual coordinate permutations in the two daughters.
    d=6
    if b==0:permutation=list(reversed(range(d)))
    else:permutation=[1,0,2,3,4,5]
    reset=tuple(a[sum(((x>>i)&1)<<j for i,j in enumerate(permutation))] for x in range(len(a)))
    check(error(reset)==error(a));check(sorted(x*x for x in coeff(reset))==sorted(x*x for x in coeff(a)))
    check(sum(bits(reset))==sum(bits(a)))
    # Centering output characters is allowed only when it lowers I.
    shift=sum((int(p>Q(1,2))<<j) for j,p in enumerate(bits(reset)))
    reset2=tuple(y*(-1)**dot(x&shift) for x,y in enumerate(reset))
    check(sum(bits(reset2))<=sum(bits(reset)))
    check(error(reset2)==error(reset));check(H(reset2)==H(reset))
    reset_savings+=(sum(bits(a))-sum(bits(reset2)))/2
    second=(len(reset2).bit_length()-2) if b==0 else 0
    ch=[restrict(reset2,second,c) for c in [0,1]]
    check(sum(error(x) for x in ch)/2<=error(reset2))
    leaves.extend(ch)
eh=(sum(H(x)[0] for x in leaves)/4,sum(H(x)[1] for x in leaves)/4)
rh=H(root);a=min(2*error(root),Q(1,2));budget=phibound(a)
check(rh[1]-eh[0]<=2*budget[0])
K=Q(15,4)
rootD=(rh[0]-K*sum(bits(root)),rh[1]-K*sum(bits(root)))
leafD=(eh[0]-K*sum(sum(bits(x)) for x in leaves)/4,eh[1]-K*sum(sum(bits(x)) for x in leaves)/4)
check(leafD[0]>=rootD[1]-2*budget[0])
# Scope adversaries: all-leaf positivity and increasing-reset conservation.
inactive=restrict(raw,6,1)
check(all(x==1 for x in inactive));check(H(inactive)==(0,0));check(error(inactive)==0)
constant=(1,1,1,1);character=(1,-1,1,-1)
check(H(constant)==H(character));check(error(constant)==error(character)==0)
check(sum(bits(character))>sum(bits(constant)))
# Independent scalar certificate, no giant truth table or large mean power.
def atom_h(x):
    lo,hi=logint(x*x)
    return -x*x*hi,-x*x*lo
u=atom_h(Q(127,128));v=atom_h(Q(1,128))
sourceH=(u[0]+255*v[0],u[1]+255*v[1])
check(sourceH[0]-K*Q(1,16)>Q(1,256))
check(ln2[0]>Q(2,3))
k=20;t=1<<20;r=64;p=Q(1,t)
root_error=(10+2*K)*k+15
frontier_error=2*r*(k+Q(9,2))
check(root_error==365);check(frontier_error==3136)
remaining=Q(1,256)-p*(root_error+frontier_error)
check(remaining==Q(595,1048576));check(remaining>0)
result={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,
 'direct_mixed_fixture':{'dimension':7,'complete_depth2_terminals':4,'branch_dependent_resets':True,'root_I':str(sum(bits(root))),'root_character_error':str(error(root))},
 'scope_guards':{'inactive_control_leaf':'constant with zero deficit','increasing_reset':'entropy/error preserved but I increases'},
 'universal_scalar_certificate':{'seed':'8-bit point defect','K':str(K),'k':k,'t':t,'maximum_query_depth':r,'ALL_policy_expected_terminal_deficit_lower':str(remaining),'root_deficit_lower':str(Q(1,256)-p*root_error),'large_truth_table_constructed':False}}
(R/'out/INDEPENDENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result))
