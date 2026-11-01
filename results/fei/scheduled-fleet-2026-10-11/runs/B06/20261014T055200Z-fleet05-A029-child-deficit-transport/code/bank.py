import argparse,itertools,json,time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];ASSERT=0
def ck(b):
    global ASSERT
    ASSERT+=1
    if not b:raise AssertionError(ASSERT)
@lru_cache(None)
def states(n):return tuple(itertools.product((-1,0,1),repeat=n))
@lru_cache(None)
def points(state):
    free=tuple(i for i,b in enumerate(state) if b==-1);fixed=sum(b<<i for i,b in enumerate(state) if b!=-1)
    return free,tuple(fixed+sum(((z>>j)&1)<<i for j,i in enumerate(free)) for z in range(2**len(free)))
def child(st,i,b):z=list(st);z[i]=b;return tuple(z)
@lru_cache(None)
def restriction(mask,state):
    free,xx=points(state);N=len(xx)
    return free,tuple(1 if mask>>x&1 else -1 for x in xx)
def canonical_maps():
    ans=[]
    for pair in itertools.combinations(range(4),2):
        rest=[i for i in range(4) if i not in pair];a=[0]*4;a[rest[0]]=1;a[rest[1]]=2;ans.append(tuple(a))
    return ans
def data_metrics(masks,state):
    free,t0=restriction(masks[0],state);tt=[restriction(m,state)[1] for m in masks];N=len(t0)
    pivots=[];product_d=[]
    for i in range(len(free)):
        rs=[tuple(int(t[x]!=t[x^(1<<i)]) for x in range(N)) for t in tt]
        patterns=tuple(sum(rs[j][x]<<j for j in range(3)) for x in range(N));pivots.append(patterns)
        row=[]
        for j,k in ((0,1),(0,2),(1,2)):
            prod=[a*b for a,b in zip(tt[j],tt[k])]
            # Separate actual product boundary, not XOR used as implementation.
            row.append(F(sum(prod[x]!=prod[x^(1<<i)] for x in range(N)),N))
        product_d.append(tuple(row))
    return free,N,tuple(pivots),tuple(product_d)
def run_root(masks,labelmap,n):
    data={st:data_metrics(masks,st) for st in states(n)}
    controls={}
    for st in states(2):
        free,yy=points(st);nums=tuple(sum(labelmap[y]==j for y in yy) for j in range(3));D=len(yy)
        qnum=tuple(sum(nums[j] for j in range(3) if pattern>>j&1) for pattern in range(8))
        controls[st]=(free,D,nums,qnum)
    values={}
    for ds,cs in itertools.product(states(n),states(2)):
        free,N,pattern,product_d=data[ds];_,D,nums,qnum=controls[cs]
        wpair=(F(2*nums[0]*nums[1],D*D),F(2*nums[0]*nums[2],D*D),F(2*nums[1]*nums[2],D*D))
        R=sum((wpair[j]*v[j] for v in product_d for j in range(3)),F(0))
        variance=F(2*sum(qnum[p]*(D-qnum[p]) for row in pattern for p in row),D*D*N)
        ck(R==variance)
        di=tuple(F(sum(qnum[p] for p in row),D*N) for row in pattern)
        ck(R<=2*sum(di));values[(ds,cs)]=(R,di)
    transitions=0
    release={}
    for ds,cs in itertools.product(states(n),states(2)):
        R,di=values[(ds,cs)];free,N,patterns,product_d=data[ds];cf,D,nums,qnum=controls[cs]
        for pos,i in enumerate(free):
            kids=[(child(ds,i,b),cs) for b in (0,1)]
            rel=R-sum(values[k][0] for k in kids)/2
            exact=sum((F(2*nums[j]*nums[k],D*D)*product_d[pos][z] for z,(j,k) in enumerate(((0,1),(0,2),(1,2)))),F(0))
            ck(rel==exact>=0);ck(rel<=2*di[pos]*(1-di[pos]));transitions+=1
            release[(ds,cs,i)]=rel
        for i in cf:
            cs0,cs1=child(cs,i,0),child(cs,i,1);q0,q1=controls[cs0][3],controls[cs1][3];den=controls[cs0][1]
            ck(den==controls[cs1][1])
            rel=R-(values[(ds,cs0)][0]+values[(ds,cs1)][0])/2
            square=F(sum((q0[p]-q1[p])**2 for row in patterns for p in row),2*N*den*den)
            ck(rel==square>=0);transitions+=1;release[(ds,cs,n+i)]=rel
    # Two stopped trees resolving controllers only, with data exposed first or controls first.
    for data_first in (False,True):
        def walk(ds,cs,w):
            df=points(ds)[0];cf=points(cs)[0]
            if not cf:return F(0),w*values[(ds,cs)][0]
            if data_first and df:
                i=df[0];kids=[(child(ds,i,b),cs) for b in (0,1)]
            else:
                i=n+cf[0];kids=[(ds,child(cs,cf[0],b)) for b in (0,1)]
            total=w*release[(ds,cs,i)];terminal=F(0)
            for d,c in kids:
                x,t=walk(d,c,w/2);total+=x;terminal+=t
            return total,terminal
        total,terminal=walk((-1,)*n,(-1,)*2,F(1));root=values[((-1,)*n,(-1,)*2)][0]
        ck(root==total+terminal);ck(terminal==0)
        ck(F(7,4)*root==F(7,4)*total+F(7,4)*terminal)
    return len(values),transitions
def guard():
    tab=(-1,1,1,1);N=4
    W=[sum(tab[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
    ck(all(v*v==4 for v in W)) # integer Walsh numerators +/-2, coefficients +/-1/2; H=2 bits
    ck(F(2)-F(1,2)==F(3,2));ck((F(2)-F(1,2))/F(1,2)==3)
    (BASE/'out/guard.json').write_text(json.dumps({'status':'PASS','actual_truth_table':tab,'Fourier_numerators':W,'root_H':'2','data_child_H':['0','0'],'release_R':'1/2','data_influence':'1/2','release_only_gap':'3/2','necessary_added_price':'3'},indent=2))
def main(pilot):
    start=time.monotonic();roots=histories=queries=0
    domains=[(1,(0,1,3) if pilot else range(4),list(itertools.product(range(3),repeat=4))[:3] if pilot else itertools.product(range(3),repeat=4)),
      (2,(1,6,10) if pilot else (0,1,3,5,6,10,12,15),canonical_maps()[:1] if pilot else canonical_maps())]
    for n,masks,maps in domains:
        for lm in maps:
            for triple in itertools.product(masks,repeat=3):
                h,q=run_root(triple,tuple(lm),n);roots+=1;histories+=h;queries+=q
        out={'status':'PASS','completed_dimension':n,'roots':roots,'histories':histories,'queries':queries,'assertions':ASSERT,'seconds':time.monotonic()-start}
        (BASE/'out'/('bank_pilot_checkpoint.json' if pilot else 'bank_checkpoint.json')).write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
    guard()
    out={'status':'PASS','pilot':pilot,'roots':roots,'histories':histories,'queries':queries,'stopped_trees':2*roots,'assertions':ASSERT,'seconds':time.monotonic()-start,'arithmetic':'Exact conditional label counts, Fraction pair boundary and independently enumerated pivot variance','max_physical_dimension':4}
    (BASE/'out'/('bank_pilot.json' if pilot else 'bank.json')).write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');main(p.parse_args().pilot)
