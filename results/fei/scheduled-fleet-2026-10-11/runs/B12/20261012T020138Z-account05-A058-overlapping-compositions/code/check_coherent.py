from pathlib import Path
from collections import Counter
from functools import lru_cache
from fractions import Fraction as Qrat
import argparse,itertools,json,time

RUN=Path(__file__).resolve().parents[1]
checks=0
def ck(c):
    global checks
    checks+=1
    if not c:raise AssertionError(checks)
def walsh(a):
    a=list(a); h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return a
def table(t,n):return [1-2*((t>>x)&1) for x in range(1<<n)]
@lru_cache(None)
def factors(n):
    out=[];p=2
    while p*p<=n:
        v=0
        while n%p==0:v+=1;n//=p
        if v:out.append((p,v))
        p+=1
    if n>1:out.append((n,1))
    return tuple(out)
def add(a,b,scale=1):
    out=dict(a)
    for p,v in b.items():out[p]=out.get(p,0)+scale*v
    return {p:v for p,v in out.items() if v}
@lru_cache(maxsize=4096)
def ent_cached(masses,D):
    out={p:D*v for p,v in factors(D)}
    for c in masses:
        if c:
            for p,v in factors(c):out[p]=out.get(p,0)-c*v
    return {p:v for p,v in out.items() if v}
def ent(masses,D):
    ck(sum(masses)==D)
    return ent_cached(tuple(sorted(c for c in masses if c)),D)
def logweights(values,weights):
    out={}
    for c,w in zip(values,weights):
        if c:
            for p,v in factors(c):out[p]=out.get(p,0)+w*v
        else:ck(w==0)
    return {p:v for p,v in out.items() if v}

def one(F,fw,b,bw,row,sign,m):
    N0=(1<<m)*4;D=N0*N0;N=N0//2;private=m-1
    C=[]
    for T in range(1<<m):
        a=fw[T]*(-1 if sign==-1 and T&2 else 1)
        active=(T&row).bit_count()%2
        C.extend(a*c for c in (bw if active else [4,0,0,0]))
    q=[0]*N;p=[0]*N;collision=[0]*N
    for T in range(1<<m):
        if T&2:continue
        T1=T^3;U=(T&1)^((T>>1)&1)|((T>>2)<<1)
        for S in range(4):
            v,w=C[4*T+S],C[4*T1+S];y=U+(S<<private)
            q[y]=v*v+w*w;p[y]=(v+w)**2;collision[y]=2*v*w
    truth=[]
    for x in range(N):
        y=3*(x&1)+4*((x>>1)&((1<<(m-2))-1))
        if sign==-1:y^=2
        if b[(x>>private)&3]==-1:y^=row
        truth.append(F[y])
    w=walsh(truth)
    for T in range(1<<m):
        if T&2:continue
        U=(T&1)^((T>>1)&1)|((T>>2)<<1)
        for S in range(4):
            y=U+(S<<private)
            ck(2*w[y]==C[4*T+S]+C[4*(T^3)+S])
    ck(sum(q)==D);ck(sum(p)==D);ck(sum(collision)==0)
    for pi,qi,di in zip(p,q,collision):ck(pi==qi+di and 0<=pi<=2*qi)
    hl=ent([c*c for c in C],D);hq=ent(q,D);hp=ent(p,D)
    posterior=add(hl,hq,-1)
    kl=add(logweights(p,p),logweights(q,p),-1)
    R=logweights(q,[-d for d in collision])
    ck(hp==add(add(add(hl,posterior,-1),kl,-1),R))
    # Coordinate membership is actual physical influence, independently from edges.
    for i in range(private+2):
        si=sum(pi for y,pi in enumerate(p) if y&(1<<i))
        ei=sum(truth[x]!=truth[x^(1<<i)] for x in range(N))
        ck(si*N==ei*D)
    return hl,hp,posterior,kl,R,Qrat(sum(p[y] for y in range(N) if y&1),D)

def controls():
    records=[]
    # F is -1 only at binary address 2, namely (+1,-1).
    F=table(1<<2,2)
    ck(walsh(F)==[2,-2,2,2])
    for k in range(1,5):
        n=2*k;Ns=1<<n
        b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k)) for x in range(Ns)]
        bw=walsh(b);ck(all(a*a==Ns for a in bw))
        ck(sum(a*a*S.bit_count() for S,a in enumerate(bw))==k*Ns*Ns)
        truth=[-((-1)**(x&1))*b[x>>1] for x in range(2*Ns)]
        W=walsh(truth);D=(2*Ns)**2
        ck(ent([a*a for a in W],D)=={2:2*k*D})
        ck(sum(a*a for S,a in enumerate(W) if S&1)==D)
        ck(sum(a*a*S.bit_count() for S,a in enumerate(W))==(k+1)*D)
        # In common denominator 2*Ns, Q=(1/2 delta_empty,1/2 spectral_b).
        Dq=2*Ns;q=[0]*(2*Ns);p=[0]*(2*Ns);q[0]=Ns
        for S in range(Ns):q[1+2*S]=1;p[1+2*S]=2
        delta=[pi-qi for pi,qi in zip(p,q)]
        ck(ent(q,Dq)=={2:(k+1)*Dq})
        ck(add(logweights(p,p),logweights(q,p),-1)=={2:Dq})
        ck(logweights(q,[-d for d in delta])=={2:k*Dq})
        records.append({'k':k,'H_old':k+2,'H_new':2*k,'entropy_increment':k-2,'posterior_bits':1,'KL_bits':1,'cross_surprisal_bits':k,'anchor_influence':1,'data_influence_old':str(Qrat(k,2)),'data_influence_new':k,'exact_deficit_reserve':'Delta H=2 Delta I_data-2'})
    zero=one(F,walsh(F),[1]*4,[4,0,0,0],0,1,2)
    ck(zero[1]=={} and zero[2]=={2:256} and zero[-1]==0)
    # X004 physical xy: no use of an incoherent leaf mixture.
    xy=[(-1)**((x&1)^((x>>1)&1)) for x in range(4)]
    W=walsh(xy);ck(W==[0,0,0,4]);ck(ent([a*a for a in W],16)=={})
    ck(sum(a*a*S.bit_count() for S,a in enumerate(W))==32)
    splices=[]
    for n in [2,4,6]:
        N=1<<n;b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(n//2)) for x in range(N)]
        h=b[:];h[0]*=-1
        truth=[]
        for x in range(2*N):truth.append((b if not x&1 else h)[x>>1])
        W=walsh(truth);D=(2*N)**2;bw=walsh(b)
        for S in range(N):ck(W[2*S]==2*bw[S]-2 and W[2*S+1]==2)
        ck(sum(a*a for S,a in enumerate(W) if S&1)*(N)==D)
        masses=[a*a for a in W];q=[masses[2*S]+masses[2*S+1] for S in range(N)]
        B=add(ent(masses,D),ent(q,D),-1)
        splices.append({'core_dimension':n,'selector_influence':str(Qrat(1,N)),'erasure_prime_log_numerator':B,'denominator':D})
    return {'bent_counterfamily':records,'zero_anchor_posterior':'1 bit with I_x=0','X004':{'H':0,'I':2},'X009_splices':splices}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['pilot','main'],required=True);ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    spec=json.loads((RUN/'out/FROZEN_SPEC.json').read_text());s=json.loads((RUN/'out/FROZEN_SPEC_RESUME.json').read_text()) if args.resume else spec[args.mode];m=s['outer_arity'];start=time.perf_counter();count=0
    bs=[table(t,2) for t in range(16)];bws=[walsh(b) for b in bs]
    for ft in range(s.get('start_outer_table',0),1<<(1<<m)):
        F=table(ft,m);fw=walsh(F)
        for b,bw in zip(bs,bws):
            for row in range(1<<m):
                for sign in [1,-1]:one(F,fw,b,bw,row,sign,m);count+=1
        result={'mode':args.mode,'case_count':count,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'status':'CHECKED_PREFIX','next_outer_table':ft+1}
        if not args.resume or (ft+1)%16==0 or ft==255:
            (RUN/'out'/f'{args.mode}{"_remaining" if args.resume else ""}_checkpoint.json').write_text(json.dumps(result,indent=2))
        if result['elapsed_seconds']>s['max_runtime_seconds']:raise RuntimeError('Frozen wall-clock guard after complete outer table')
    ck(count==s['case_count']); extra=controls()
    result.update(status='PASS',exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,controls=extra)
    (RUN/'out'/f'{args.mode}{"_remaining" if args.resume else ""}_results.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='controls'}))
if __name__=='__main__':main()
