import json,time,itertools
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def combine(a,b,q=Q(1)):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,Q(0))+q*v
    return {k:v for k,v in c.items() if v}
def scaled(a,q):return {k:v*q for k,v in a.items() if v*q}
def factors(n):
    d=2;out={}
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def profile(a):
    N=len(a);n=N.bit_length()-1
    w=[sum(v*(-1 if (j & x).bit_count()%2 else 1) for j,v in enumerate(a)) for x in range(N)]
    assert sum(t*t for t in w)==N*N
    H={2:Q(2*n)}
    for t in w:
        if t:H=combine(H,factors(abs(t)),Q(-2*t*t,N*N))
    I=sum(Q(a[j]!=a[j^(1<<i)],2*N) for j in range(N) for i in range(n))*2
    If=sum(Q(t*t,N*N)*x.bit_count() for x,t in enumerate(w))
    assert I==If
    return H,I
def mux(A,B,s,outer=True):
    N=len(A);ns=len(s)
    if outer:return [A[x%N] if (x//N)%2 and s[x//(2*N)]==-1 else B[x%N] for x in range(2*N*ns)]
    return [A[x%N] if s[x//N]==-1 else B[x%N] for x in range(N*ns)]
start=time.monotonic();cases=nonzeroK=assertions=0
for idx in itertools.combinations(range(8),4):
    ss=[-1 if j in idx else 1 for j in range(8)];Hs,Is=profile(ss)
    for cores in ([list(v) for v in itertools.product([-1,1],repeat=2)], [[-1,1,1,1],[-1,-1,-1,1],[1,-1,-1,1],[1,1,1,1]]):
        for A in cores:
            for B in cores:
                HA,IA=profile(A);HB,IB=profile(B);K=combine(scaled(HA,Q(1,4)),HB,Q(3,4));nonzeroK+=bool(K)
                delta=Q(sum(a!=b for a,b in zip(A,B)),len(A));E=profile([a*b for a,b in zip(A,B)])[1]
                HP,IP=profile(mux(A,B,ss));D=combine(HP,K,-1)
                Hflat=profile(mux(A,B,[-1,1]))[0];Df=combine(Hflat,K,-1)
                assert combine(D,Df,-1)==scaled(Hs,delta/2);assertions+=1
                G=mux(A,B,ss,False);N=len(A)
                It=Q(sum(a!=b for a,b in zip(G,B*8)),len(G))
                J=profile([a*b for a,b in zip(G,B*8)])[1]
                assert 4*It+J==E/2+delta*(2+Is);assertions+=1
                Kc=combine(scaled(HA,Q(1,2)),HB,Q(1,2));Dc=combine(profile(G)[0],Kc,-1)
                Dcf=combine(profile(mux(A,B,[-1,1],False))[0],Kc,-1)
                assert combine(D,Dc,Q(-1,2))==combine(Df,Dcf,Q(-1,2));assertions+=1
                cases+=1
assert cases==2240 and nonzeroK>0
cert=json.loads((root/'out'/'CERTIFICATE.json').read_text(encoding='utf-8'))
S=1<<100;ex=cert['levels'][-1]['excess_interval'];lo,hi=map(Q,ex)
assert 11*lo/4-Q(19,5)>Q(9,400)
assert 10*hi/4-Q(7,2)<0
out={'status':'PASS','cases':cases,'assertions':assertions+2,'nonzero_inherited_K_cases':nonzeroK,'method':'direct character sums and physical edges, formal prime-log equality','first_actual_tensor_failure':11,'counterexample_gap_lower_bound':'9/400','elapsed_s':time.monotonic()-start}
(root/'out'/'SMALL_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
