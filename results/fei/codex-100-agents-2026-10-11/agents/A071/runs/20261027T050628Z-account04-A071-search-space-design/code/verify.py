"""A071 independent exact truth-matrix audit; Python standard library only."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, itertools, json, time
ROOT=Path(__file__).resolve().parents[1]
def dump(name,obj):
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def fwht(v):
    v=list(v); h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):
                a,b=v[j],v[j+h]; v[j],v[j+h]=a+b,a-b
        h*=2
    return v
def embed(v,positions):
    return sum(((v>>j)&1)<<p for j,p in enumerate(positions))
def rows(f,N,A):
    B=[i for i in range(N) if i not in A]
    return {tuple(f[embed(a,A)|embed(b,B)] for b in range(1<<len(B))) for a in range(1<<len(A))}
def influence(f,N):
    return [Q(sum(f[t]!=f[t^(1<<i)] for t in range(1<<N)),1<<N) for i in range(N)]
def run(pilot):
    start=time.monotonic(); counts=dict(functions=0,blocks=0,assertions=0,walsh_atoms=0)
    def check(x):
        counts['assertions']+=1
        assert x
    for n in range(1,3 if pilot else 4):
        for mask in range(1<<(1<<n)):
            g=[1-2*((mask>>x)&1) for x in range(1<<n)]
            for k in ([2] if pilot else [2,3]):
                N=n+k
                f=[g[t% (1<<n)]*(-1 if t.bit_count()<=1 else 1) for t in range(1<<N)]
                counts['functions']+=1
                # Entire labelled domain, no quotient, all proper nonsingleton blocks.
                for a in range(1, (1<<N)-1):
                    A=[i for i in range(N) if a>>i&1]
                    if len(A)<2: continue
                    check(len(rows(f,N,A))>=3); counts['blocks']+=1
                check(len(rows(f,N,list(range(n,N))))==3)
                U=[int(z==0) for z in range(1<<k)]
                V=[int(z.bit_count()==1) for z in range(1<<k)]
                check(set(zip(U,V))=={(0,0),(1,0),(0,1)})
                # Exact factorization on all physical inputs, no independence assumption.
                for t in range(1<<N):
                    x,z=t% (1<<n),t>>n
                    check(f[t]==g[x]*(1-2*(int(x.bit_count()<=1)*U[z]+int(x==0)*V[z])))
                I=influence(f,N); w=fwht(f)
                for i in range(N):
                    check(I[i]==Q(sum(w[s]**2 for s in range(1<<N) if s>>i&1),1<<(2*N)))
                check(sum(v*v for v in w)==1<<(2*N))
                # Independent direct character sum at every Fourier atom.
                for s in range(1<<N):
                    check(w[s]==sum(f[t]*(-1 if (s&t).bit_count()%2 else 1) for t in range(1<<N)))
                    counts['walsh_atoms']+=1
                check(sum(I[n:])==Q(k*(N-1),1<<(N-1)))
                iu=sum(influence([1-2*u for u in U],k))
                iv=sum(influence([1-2*v for v in V],k))
                check(iu==Q(k,1<<(k-1))); check(iv==Q(k*k,1<<(k-1)))
                weighted=Q(n+1,1<<n)*iu+Q(1,1<<n)*iv
                check(weighted-sum(I[n:])==Q(2*k,1<<(N-1)))
                check(Q(1,1<<k)+Q(k,1<<k)+Q((1<<k)-k-1,1<<k)==1)
                # Exact edit and physical influence continuity; constants included.
                seed=[g[t% (1<<n)] for t in range(1<<N)]
                eps=Q(N+1,1<<N)
                check(Q(sum(a!=b for a,b in zip(f,seed)),1<<N)==eps)
                check(abs(sum(I)-sum(influence(g,n)))<=2*N*eps)
                if time.monotonic()-start>55: raise TimeoutError('frozen 55s budget')
    # Missing-fresh-bit controls retained as exact witnesses, not false refutations.
    controls=[]
    for n,k,mask,A in [(2,1,1,[0,1]),(3,0,2,[1,2])]:
        N=n+k; f=[(1-2*((mask>>(t%(1<<n)))&1))*(-1 if t.bit_count()<=1 else 1) for t in range(1<<N)]
        r=len(rows(f,N,A)); check(r==2)
        controls.append(dict(n=n,k=k,seed_mask=mask,block=A,row_count=r))
    for s in range(2,129): check(s+2<=1<<s)
    dump('PILOT.json' if pilot else 'RESULT.json',dict(counts=counts,seconds=time.monotonic()-start,controls=controls,status='PASS',arithmetic='integers and fractions; no floating sign decisions',helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
    print(json.dumps(dict(counts=counts,seconds=time.monotonic()-start,status='PASS')))
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--pilot',action='store_true');run(p.parse_args().pilot)
