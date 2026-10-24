from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time

ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic()
def guard():
    if time.monotonic()-START>120: raise RuntimeError('frozen runtime exceeded')

def walsh(table):
    a=list(table); k=1
    while k<len(a):
        for i in range(0,len(a),2*k):
            for j in range(k):
                u,v=a[i+j],a[i+j+k]; a[i+j],a[i+j+k]=u+v,u-v
        k*=2
    return a

def direct(table):
    return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)) for s in range(len(table))]

@lru_cache(None)
def ln_unit(x):
    # x in [1,2]. Positive terms and a geometric majorant for the tail.
    z=(x-1)/(x+1); zz=z*z; term=z; total=F(0); N=40
    for k in range(N): total+=2*term/(2*k+1); term*=zz
    return total,total+2*term/((2*N+1)*(1-zz))

@lru_cache(None)
def log2i(x):
    assert x>0
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    lo,hi=ln_unit(x); dl,dh=ln_unit(F(2))
    return F(k)+lo/dh,F(k)+hi/dl

def entropy(ps):
    assert sum(ps)==1 and all(t>=0 for t in ps)
    lo=hi=F(0)
    for t in ps:
        if t:
            a,b=log2i(t); lo-=t*b; hi-=t*a
    return lo,hi

def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def scale(a,b):
    return (a[0]*b,a[1]*b) if b>=0 else (a[1]*b,a[0]*b)
def interval_record(a):
    return {'lower':str(a[0]),'upper':str(a[1]),'approx':[float(a[0]),float(a[1])]}

def finite(g,h,p):
    N=len(g); G=[F(x,N) for x in walsh(g)]; H=[F(x,N) for x in walsh(h)]
    joint=[]; q=[]
    for u,v in zip(G,H):
        a=((1-p)*u+p*v)**2; b=p*(1-p)*(v-u)**2
        assert a+b==(1-p)*u*u+p*v*v
        joint.extend([a,b]); q.append(a+b)
    mismatch=F(sum(u!=v for u,v in zip(g,h)),N)
    assert sum(joint[1::2])==4*p*(1-p)*mismatch
    ej=add(scale(entropy([x*x for x in G]),1-p),scale(entropy([x*x for x in H]),p))
    M=sub(entropy(joint),entropy(q)); J=sub(entropy(q),ej); D=sub(J,M)
    return {'p':str(p),'joint':[str(x) for x in joint], 'M':interval_record(M),'J':interval_record(J),'debt':interval_record(D)}

def main():
    out={'version':1,'exact_counts':{},'finite':[],'self_checks':{}}
    for n in range(4):
        N=1<<n
        tables=[[1 if (mask>>x)&1 else -1 for x in range(N)] for mask in range(1<<N)]
        W=[walsh(t) for t in tables]
        assert all(w==direct(t) for w,t in zip(W,tables))
        assert all(sum(x*x for x in w)==N*N for w in W)
        assert all(walsh(w)==[N*x for x in t] for w,t in zip(W,tables))
        for w,t in zip(W,tables):
            for bit in range(n):
                spectral=sum(x*x for s,x in enumerate(w) if (s>>bit)&1)
                physical=N*sum(t[x]!=t[x^(1<<bit)] for x in range(N))
                assert spectral==physical
        maximum=-10*N*N; maximizers=positive=zero=balanced_max_count=0; sample=None
        balanced_max=-10*N*N
        for i,G in enumerate(W):
            for j,H in enumerate(W):
                guard()
                corr=sum(a*b for a,b in zip(G,H))
                assert corr==N*sum(a*b for a,b in zip(tables[i],tables[j]))
                Z=sum(b*b for a,b in zip(G,H) if a==0)
                D=sum((b-a)**2 for a,b in zip(G,H) if a!=0)
                coeff=Z-D
                assert coeff==2*Z+2*corr-2*N*N
                assert Z*N*N<=N**4-corr*corr
                assert 2*coeff<=N*N
                positive+=coeff>0; zero+=coeff==0
                if coeff>maximum: maximum=coeff; maximizers=1; sample=[i,j]
                elif coeff==maximum: maximizers+=1
                if G[0]==H[0]==0:
                    if coeff>balanced_max: balanced_max=coeff; balanced_max_count=1
                    elif coeff==balanced_max: balanced_max_count+=1
        out['exact_counts'][str(n)]={'pairs':len(W)**2,'positive':positive,'zero':zero,'maximum':str(F(maximum,N*N)), 'maximizers':maximizers,'sample_truth_masks':sample,'balanced_maximum':str(F(balanced_max,N*N)) if balanced_max_count else None}
        (ROOT/'out'/'endpoint_counts.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    # g=1, h=1-2 1_{y=00}; c=1/2. Character multiplication gives balanced children.
    choices=[('constant_to_quarter_defect',[1]*4,[-1,1,1,1]),
             ('constant_to_balanced',[1]*4,[-1,-1,1,1]),
             ('dictator_to_balanced_quarter_surgery',[1,-1,1,-1,1,-1,1,-1],[-1,1,1,-1,1,-1,1,-1]),
             ('equal_children',[1,-1],[1,-1]),('opposite_children',[1,-1],[-1,1])]
    for label,g,h in choices:
        for p in (F(1,8),F(1,64),F(1,1024)):
            guard(); row=finite(g,h,p); row['label']=label
            if label in ('constant_to_quarter_defect','dictator_to_balanced_quarter_surgery'): assert F(row['debt']['lower'])>0
            if label=='opposite_children': assert F(row['debt']['upper'])<0
            out['finite'].append(row)
            (ROOT/'out'/'results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    for k in range(-12,13): assert log2i(F(2)**k)==(F(k),F(k))
    assert entropy([F(0),F(1)])==(0,0)
    out['self_checks']={'direct_Walsh_all_tables':'PASS','inverse_Walsh_all_tables':'PASS','edge_influences_all_tables':'PASS','selector_influence_all_finite_cases':'PASS','Parseval_all_tables':'PASS','physical_corr_all_pairs':'PASS','Cauchy_bound_all_pairs':'PASS','log_powers_two':25,'zero_entropy':'PASS'}
    out['runtime_seconds']=time.monotonic()-START
    (ROOT/'out'/'results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in out.items() if k!='finite'},indent=2))
    print('PASS; finite rational certificates:',len(out['finite']))
if __name__=='__main__': main()
