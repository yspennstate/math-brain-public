import argparse,json,math,time
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out';OUT.mkdir(exist_ok=True)

def walsh(z):
    z=list(z);h=1
    while h<len(z):
        for a in range(0,len(z),2*h):
            for j in range(a,a+h):
                s,t=z[j],z[j+h];z[j],z[j+h]=s+t,s-t
        h*=2
    return z

@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1); L=Q(0);term=z
    for j in range(40):
        L+=2*term/Q(2*j+1);term*=z*z
    return L,L+2*term/(Q(81)*(1-z*z))

@lru_cache(None)
def lg(x):
    x=Q(x);k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    a,b=ln_unit(x);c,d=ln_unit(Q(2))
    return k+a/d,k+b/c

def isum(parts):
    a=b=Q(0)
    for w,x in parts:
        if not w:continue
        lo,hi=lg(x)
        if w>=0:a+=w*lo;b+=w*hi
        else:a+=w*hi;b+=w*lo
    return a,b

def clean(v):return {k:w for k,w in v.items() if k!=1 and w}
def add(v,k,w):
    if w and k>0:v[k]+=w

def verify_phase(A,V,certify_logs=False):
    N=len(A);m=N.bit_length()-1
    assert all(a*a+v*v==1 and a*v==0 for a,v in zip(A,V))
    U=walsh(A);Z=walsh(V);G=[a*a-v*v for a,v in zip(A,V)];GW=walsh(G)
    k=sum(v*v for v in V);assert sum(v*v for v in Z)==N*k
    s=[];checks=2
    for t in range(N):
        rr=sum(U[j]*U[j^t]+Z[j]*Z[j^t] for j in range(N))
        ri=sum(U[j]*Z[j^t] for j in range(N))
        ss=sum(Z[j]*Z[j^t] for j in range(N))
        assert rr==(N*N if t==0 else 0) and ri==0
        assert GW[t]*N==(N*N if t==0 else 0)-2*ss
        s.append(ss);checks+=2
    en=sum(t.bit_count()*GW[t]**2 for t in range(N))
    assert en*N*N==4*sum(t.bit_count()*s[t]**2 for t in range(N));checks+=1
    boundary=sum(1 for x in range(N) for j in range(m) if not(x>>j&1) and (V[x]**2!=V[x^(1<<j)]**2))
    assert en==2*N*boundary;checks+=1
    if k:
        assert Q(boundary)>=k*lg(Q(N,k))[1];checks+=1
    # Independent exact formal-log encoding of spectral entropy and mutual information.
    B=defaultdict(int);M=defaultdict(int);H=defaultdict(int)
    add(H,N,N*N);add(H,k,-N*k);add(H,N-k,-N*(N-k))
    for u,v in zip(U,Z):
        a=u*u;b=v*v;q=a+b
        add(B,q,q);add(B,a,-a);add(B,b,-b)
        for mass,den in [(a,N-k),(b,k)]:
            if mass:
                add(M,mass,mass);add(M,N,mass);add(M,q,-mass);add(M,den,-mass)
    BM=defaultdict(int,B)
    for q,v in M.items():BM[q]+=v
    assert clean(BM)==clean(H);checks+=1
    # Fully exact scalar if every formal log is a power of 2 (e.g. flat bent).
    def dyadic_scalar(vec):
        if all(t&(t-1)==0 for t in clean(vec)):
            return Q(sum(w*(t.bit_length()-1) for t,w in clean(vec).items()),N*N)
        return None
    result={'m':m,'d':str(Q(k,N)),'W':str(Q(boundary,N)),
            'B_exact_if_dyadic':str(dyadic_scalar(B)),
            'M_exact_if_dyadic':str(dyadic_scalar(M)),'integer_assertions':checks}
    if certify_logs:
        blo,bhi=isum([(Q(w,N*N),Q(t)) for t,w in clean(B).items()])
        mlo,mhi=isum([(Q(w,N*N),Q(t)) for t,w in clean(M).items()])
        hparts=[]
        for num in [k,N-k]:
            if num:hparts.append((Q(num,N),Q(N,num)))
        hlo,hhi=isum(hparts)
        # B+M=h(d) already exact formally; their independent intervals intersect.
        assert blo+mlo<=hhi and bhi+mhi>=hlo;checks+=1
        result.update(B_interval=[str(blo),str(bhi)],M_interval=[str(mlo),str(mhi)],
                      B_display=float((blo+bhi)/2),M_display=float((mlo+mhi)/2))
        result['integer_assertions']=checks
    return result

def enumerate_all(max_m,max_seconds):
    start=time.monotonic();counts={};checks=0
    for m in range(max_m+1):
        N=1<<m
        for table in range(4**N):
            if time.monotonic()-start>max_seconds-2:
                raise RuntimeError('Frozen runtime cap approached')
            A=[];V=[]
            for x in range(N):
                phase=(table>>(2*x))&3
                A.append([1,-1,0,0][phase]);V.append([0,0,1,-1][phase])
            result=verify_phase(A,V)
            checks+=result['integer_assertions']
            counts[m]=counts.get(m,0)+1
        (OUT/'checkpoint.json').write_text(json.dumps({'counts':counts,'assertions':checks},indent=2))
    return {'counts':counts,'cases':sum(counts.values()),'integer_assertions':checks,
            'runtime_seconds':time.monotonic()-start,'arithmetic':'integer signed Walsh; exact formal-log coefficients; rational isoperimetric intervals'}

def dense_bent(r):
    n=2*r;N=1<<n;mask=(1<<r)-1
    def b(z):
        x=z&mask;y=z>>r
        # (I+J)y = y xor all-ones if y has odd parity.
        My=y^(mask if y.bit_count()%2 else 0)
        return -1 if (x&My).bit_count()%2 else 1
    f=[b(z) for z in range(N)];W=walsh(f)
    assert all(v*v==N for v in W)
    influence=Q(sum(s.bit_count()*v*v for s,v in enumerate(W)),N*N)
    assert influence==r
    phase=[]
    for i in range(n):
        A=[];V=[]
        for z in range(1<<(n-1)):
            lo=z&((1<<i)-1);hi=z>>i
            x=lo|(hi<<(i+1));g=f[x];h=f[x|(1<<i)]
            A.append((g+h)//2);V.append((g-h)//2)
        rec=verify_phase(A,V)
        assert Q(rec['W'])==Q(r-1,2)
        assert Q(rec['B_exact_if_dyadic'])==1 and Q(rec['M_exact_if_dyadic'])==0
        phase.append(rec)
    return {'r':r,'I':str(influence),'Q':str(r*(r-1)),'Q_over_I':r-1,'spectral_credit':0,'coordinates':phase}

def bent_surgery(m):
    N=1<<m;g=[-1 if sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(m//2))%2 else 1 for z in range(N)]
    V=[1]+[0]*(N-1);A=[g[z]-V[z] for z in range(N)]
    rec=verify_phase(A,V,True);d=Q(1,N)
    assert Q(rec['W'])==m*d
    lo,hi=lg(1+4*d*d/(1+4*d*d))
    # M <= log(1+chi2); check this with rigorous outward intervals on the certificate.
    assert Q(rec['M_interval'][1])<lo
    rec.update(sharpness_W=str(m*d),B_over_W_display=rec['B_display']/float(m*d),
               chi_squared_exact=str(4*d*d/(1+4*d*d)))
    return rec

def diagnostic():
    d=Q(9,25);lo,hi=isum([(d,1/d),(1-d,1/(1-d))])
    lnlo,lnhi=ln_unit(Q(2));costhi=d/lnlo
    assert lo>costhi
    return {'coefficients':['4/5','3/5'],'norm_squared':'1','d':str(d),'W':'0',
            'B_lower':str(lo),'B_upper':str(hi),'claimed_cost_upper':str(costhi),
            'violation_lower':str(lo-costhi),'B_display':float(lo),'cost_display':float(costhi),
            'certificate':'exact rational atanh intervals; this vector is explicitly non-Boolean'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--full',action='store_true');args=ap.parse_args()
    assert args.pilot^args.full
    result=enumerate_all(2 if args.pilot else 3,60 if args.pilot else 300)
    name='pilot.json' if args.pilot else 'validation.json'
    (OUT/name).write_text(json.dumps(result,indent=2))
    if args.full:
        cert={'dense_bent':[dense_bent(r) for r in [2,4]],
              'bent_surgery':[bent_surgery(m) for m in [2,4,6]],
              'non_boolean':diagnostic(),'log_terms':40,'log_tail':'2 z^81/[81(1-z^2)] after 40 terms'}
        (OUT/'certificates.json').write_text(json.dumps(cert,indent=2))
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
