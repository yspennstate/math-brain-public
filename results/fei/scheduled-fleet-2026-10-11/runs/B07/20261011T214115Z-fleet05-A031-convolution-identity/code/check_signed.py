"""Frozen v2: all Boolean tables n=0..3; n=4 characters and point defects."""
import json, math, time, hashlib
from pathlib import Path
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parents[1]
def fwht(v):
    v=list(v); h=1
    while h<len(v):
        for j in range(0,len(v),2*h):
            for k in range(j,j+h):
                u,z=v[k],v[k+h]; v[k],v[k+h]=u+z,u-z
        h*=2
    return v

def log_interval(x,terms=36):
    # ln x via range reduction and atanh, with a rational positive tail.
    x=F(x); k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def core(y):
        z=(y-1)/(y+1)
        lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return lo,lo+tail
    a,b=core(x); c,d=core(F(2))
    # Divide all corners; no incorrect signed denominator ordering.
    corners=[a/c,a/d,b/c,b/d]
    return k+min(corners),k+max(corners)

def main():
    start=time.monotonic(); counts={}; assertions=0
    for n in range(5):
        N=1<<n; weights=[s.bit_count() for s in range(N)]
        L=math.lcm(*range(1,n+1)) if n else 1
        if n<4:
            tables=range(1<<N)
        else:
            tables=set()
            for s in range(N):
                table=sum(1<<x for x in range(N) if (s&x).bit_count()%2==0)
                tables.update([table,table^((1<<N)-1)])
            for x in range(N):
                tables.update([1<<x,((1<<N)-1)^(1<<x)])
        for table in tables:
            if time.monotonic()-start>58:
                raise RuntimeError('Frozen 60-second pilot cap approached; no dimension escalation')
            f=[1 if (table>>x)&1 else -1 for x in range(N)]
            W=fwht(f)
            assert sum(v*v for v in W)==N*N; assertions+=1
            for u in range(1,N):
                assert sum(W[s]*W[s^u] for s in range(N))==0; assertions+=1
            # Integer information proxy; logs are exact if magnitudes are powers of 2.
            w=[2*(n-(abs(v).bit_length()-1)) if v else 0 for v in W]
            C=[sum(W[s]*W[s^u]*w[s] for s in range(N)) for u in range(N)]
            assert sum(v*v for v in C)==N*N*sum(W[s]**2*w[s]**2 for s in range(N)); assertions+=1
            energy=sum(weights[u]*C[u]**2 for u in range(1,N))
            for r in range(N):
                assert sum(W[r^u]*C[u] for u in range(N))==N*N*W[r]*w[r]; assertions+=1
                if W[r]:
                    inv=sum(W[r^u]**2*(L//weights[u]) for u in range(1,N))
                    assert L*W[r]**2*(C[0]-N*N*w[r])**2<=inv*energy; assertions+=1
            counts[n]=counts.get(n,0)+1
    result={'helper_version':'check_signed-v2','domain':'all Boolean tables n=0..3; n=4 signed characters and point defects',
            'counts':counts,'total_cases':sum(counts.values()),'exact_assertions':assertions,
            'arithmetic':'integer Walsh, exact rational logarithm intervals for separate defects',
            'runtime_seconds':time.monotonic()-start,'symmetry':'none','entropy_log_checks':[]}
    for n in range(3,13):
        N=1<<n; p0=F((N-2)**2,N*N); q=F(4,N*N); I=F(2*n,N)
        lo,hi=log_interval(p0/q)
        A=sum((F(math.comb(n,k),k) for k in range(1,n+1)),F(0))
        J=q*A
        # Rigorous log upper bound proves squared signed cost < 36 I^2.
        assert J*I*hi*hi < 36*I*I
        elo,ehi=log_interval(1/p0)
        assert ehi<2*I
        # H = ell0 + (1-p0) Delta, exact symbolic entropy identity.
        Hlo=elo+(1-p0)*lo; Hhi=ehi+(1-p0)*hi
        assert Hhi<8*I
        result['entropy_log_checks'].append({'n':n,'H_over_I_lower':float(Hlo/I),
            'H_over_I_upper':float(Hhi/I),'cost_squared_over_I_squared_upper':float(J*hi*hi/I),
            'certificate':'exact Fraction inequalities; rational atanh tail; no floating sign decisions'})
    result['runtime_seconds']=time.monotonic()-start
    (ROOT/'out'/'validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
