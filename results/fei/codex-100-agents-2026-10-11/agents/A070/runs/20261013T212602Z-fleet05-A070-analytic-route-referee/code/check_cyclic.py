from pathlib import Path
from fractions import Fraction as Q
from math import comb
from collections import defaultdict
from functools import lru_cache
import json,time
run=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(v):
    global checks
    assert v
    checks+=1
    if time.monotonic()-start>55:raise RuntimeError('frozen 55s guard')
def chars(v):return [sum(t*(-1 if (s&x).bit_count()%2 else 1) for x,t in enumerate(v)) for s in range(len(v))]
def contract(v):
    if len(v)==1:return v[:]
    even=contract(v[::2]);odd=contract(v[1::2]);a=[]
    for x,y in zip(even,odd):a.extend([x+y,x-y])
    return a
def edges(v,N):return [Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(N)]
def ln_series(y):
    t=(y-1)/(y+1);t2=t*t;power=t;lo=Q(0)
    for j in range(18):lo+=2*power/Q(2*j+1);power*=t2
    hi=lo+2*power/(37*(1-t2))
    return lo,hi
ln2lo,ln2hi=ln_series(Q(2))
@lru_cache(None)
def log2_interval(x):
    ck(x>0)
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(Q(2)**k)
    if y<1:k-=1;y*=2
    if y>=2:k+=1;y/=2
    ck(1<=y<2)
    lo,hi=ln_series(y)
    lower=Q(k)+lo/ln2hi;upper=Q(k)+hi/ln2lo
    scale=1<<80
    floored=(lower*scale).numerator//(lower*scale).denominator
    ceiled=-((-upper*scale).numerator//(-upper*scale).denominator)
    outlo=Q(floored,scale);outhi=Q(ceiled,scale)
    ck(outlo<=lower<=upper<=outhi)
    return outlo,outhi
def cost_interval(groups):
    lo=Q(0);hi=Q(0)
    for probability,mass in groups.items():
        l,h=log2_interval(probability);lo-=mass*h;hi-=mass*l
    return lo,hi
fixtures=[];bases=[]
for q in [5,7]:
    D=1<<q;M0=D*D;mask=D-1
    majority=[1 if x.bit_count()<=q//2 else -1 for x in range(D)]
    b=chars(majority)
    ck(contract(majority)==b)
    control_orient=[sum((((z>>i)&1)*((z>>((i+1)%q))&1))<<i for i in range(q)) for z in range(D)]
    phi={}
    for s in range(D):
        v=[-1 if (s&orientation).bit_count()%2 else 1 for orientation in control_orient]
        c=chars(v);ck(c==contract(v));phi[s]=c
        support=[t for t in range(D) if c[t]];ck(len(support)&(len(support)-1)==0)
        ck(all(c[t]*c[t]*len(support)==D*D for t in support))
        origin=support[0];directions={t^origin for t in support}
        ck(all(u^v in directions for u in directions for v in directions))
    truth=[1 if ((v&mask)^control_orient[v>>q]).bit_count()<=q//2 else -1 for v in range(M0)]
    a=contract(truth)
    ck(all(a[s|(t<<q)]==b[s]*phi[s][t] for s in range(D) for t in range(D)))
    ck(contract(a)==[M0*x for x in truth])
    Ibase=edges(truth,2*q);c_q=Q(comb(q-1,(q-1)//2),1<<(q-1));J=q*c_q
    ck(all(t==c_q for t in Ibase[:q]));ck(all(t==3*c_q/4 for t in Ibase[q:]));ck(J>=Q(15,8))
    w=defaultdict(Q);rankweight={};Z=defaultdict(Q)
    for s in range(D):
        w[s.bit_count()]+=Q(b[s]*b[s],D*D)
        weight=Q(1)
        for i in range(q):
            if s>>i&1:weight/=Q((i+1)**2)
        rankweight[s]=weight;Z[s.bit_count()]+=weight
    R0={}
    for s in range(D):
        if not w[s.bit_count()]:continue
        support=[t for t in range(D) if phi[s][t]]
        p=w[s.bit_count()]*rankweight[s]/Z[s.bit_count()]/len(support)
        for t in support:R0[s|(t<<q)]=p
    ck(sum(R0.values())==1);ck(set(R0)=={i for i,t in enumerate(a) if t})
    basegroups=defaultdict(Q)
    for i,p in R0.items():basegroups[p]+=Q(a[i]*a[i],M0*M0)
    basecost=cost_interval(basegroups)
    bases.append({'q':q,'I_x':str(J),'I_z':str(sum(Ibase[q:])),'reference_mass':'1','support':len(R0),'Gamma0_interval':[str(x) for x in basecost]})
    for N in [2*q,2*q+2]:
        M=1<<N;delta=Q(1,M);scale=1<<(N-2*q)
        Lfallback=Q(2*N)
        for x0 in [0,1,1<<q,M0-1]:
            sign=truth[x0];v=[truth[x& (M0-1)] for x in range(M)];v[x0]*=-1
            fresh=contract(v);ii=edges(v,N)
            ck(all(fresh[s]==(a[s]*scale if s<M0 else 0)-2*sign*(-1 if (s&x0).bit_count()%2 else 1) for s in range(M)))
            for i in range(N):ck(abs(ii[i]-(Ibase[i] if i<2*q else 0))<=2*delta)
            ck(sum(Q(t*t,M*M) for t in fresh)==1)
            for i in range(N):ck(sum(Q(fresh[s]*fresh[s],M*M) for s in range(M) if s>>i&1)==ii[i])
            refs=defaultdict(Q);oldmass=Q(0)
            for s,p0 in R0.items():
                p=(1-delta)*p0+delta*delta
                mass=Q(fresh[s]*fresh[s],M*M);refs[p]+=mass;oldmass+=mass
            # Every formerly unsupported atom has amplitude exactly +/-2/M.
            fallbackmass=Q(4*(M-len(R0)),M*M)
            ck(oldmass+fallbackmass==1)
            refs[delta*delta]+=fallbackmass
            ck((1-delta)*sum(R0.values())+M*delta*delta==1)
            cost=cost_interval(refs)
            target=8*sum(ii[:q])+2*sum(ii[q:])
            ck(cost[1]<target)
            ck(target-cost[1]>Q(287,1920)*J)
            # Exact upper cap on all reference lengths; it includes new padding/empty atoms.
            ck(all(p>=delta*delta for p in refs))
            hist=defaultdict(Q)
            for t in fresh:
                if t:hist[Q(t*t,M*M)]+=Q(t*t,M*M)
            H=cost_interval(hist)
            ck(H[1]<target)
            fixtures.append({'q':q,'N':N,'edit_vertex':x0,'I_x':str(sum(ii[:q])),'I_z_with_padding':str(sum(ii[q:])),'H_interval':[str(x) for x in H],'Gamma_interval':[str(x) for x in cost],'rational_8Ix_2Iz':str(target),'margin_lower':str(target-cost[1]),'fallback_mass':str(fallbackmass)})
ck(len(fixtures)==16)
ck(4*Q(1,24)*(9+Q(1,640))<Q(25,16))
ck(Q(3,2)-Q(1,640)-Q(1,24)-Q(5,4)-Q(11,192)==Q(287,1920))
out={'status':'PASS','helper_version':'A070-stage2-independent-v1.1','cases':len(fixtures),'exact_assertions':checks,'seconds':time.monotonic()-start,'method':'direct q-block character sums plus independently recursive even/odd full transform; literal truth-table edge counts; complete mixture costs with outward Fraction log intervals','log_certificate':'18 atanh terms; tail 2*t^37/[37*(1-t^2)]; denominator ln2 interval positive; correct signed quotient endpoints; final log intervals rounded outward to denominator 2^80','bases':bases,'fixtures':fixtures}
(run/'out/CYCLIC_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['bases','fixtures']}))
