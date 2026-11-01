from pathlib import Path
from fractions import Fraction as Q
from math import comb, gcd
import json,time,sys
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]
from arithmetic import *
import arithmetic as arithmetic_state
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
def logq(x):
    x=Q(x); assert x>0
    return add(logform(x.numerator),logform(x.denominator),Q(-1))
def hmass(x):
    return scale(logq(x),-x) if x else {}
def phi(a,b):
    return add(add(hmass(a),hmass(b)),hmass(a+b),Q(-1))
def hout(masses):
    r={}
    for x in masses:r=add(r,hmass(x))
    return r
def tau(p):return 12*p*p-28*p**3+27*p**4-12*p**5+2*p**6
def pivot(p):return 2*p*(1-p)**3*(2-p)
NEG={0,1,2,4,8,16,32,6,17,40}
def packets(p):
    # Independent truth-table moments; centered 0/1 bits, not the grouped formula.
    vs=p*(1-p); m=1-2*p; out=[]
    for T in range(32):
        c=d=Q(0)
        for x in range(32):
            index=x<<1
            z0=-1 if index in NEG else 1
            z1=-1 if index+1 in NEG else 1
            A=Q(z0+z1,2); D=Q(z0-z1,2)
            weight=p**x.bit_count()*(1-p)**(5-x.bit_count())
            centered=Q(1)
            for i in range(5):
                if T>>i&1:centered*=Q(x>>i&1)-p
            c+=weight*(A+m*D)*centered; d+=weight*D*centered
        out.append((c*c/vs**T.bit_count(),d*d/vs**T.bit_count()))
    q=sum(d for u,d in out)
    ck(q==pivot(p));ck(sum(u+(1-m*m)*d for u,d in out)==1)
    return out
def reserve(p,t,pk):
    r={}
    for u,d in pk:r=add(r,phi(u,t*d))
    return add(r,phi((1-2*p)**2,t),-pivot(p))
def correction(p,pk):
    v=4*p*(1-p)
    return add(hout([z for u,d in pk for z in (u,v*d)]),phi(v,1-v),-6*pivot(p))
def erasure(W,i):
    N=len(W); r={}
    for x in range(N):
        if not(x>>i&1):r=add(r,G(W[x]**2,W[x|(1<<i)]**2),Q(1,N*N))
    return r
def bounds(expr):
    lo,hi=enclose(expr)
    return {'lower':str(lo),'upper':str(hi),'display':[float(lo),float(hi)]}
def dump(name,x):
    (ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n')

profiles=[]
for r in range(4,9):
    p=Q(1,1<<r); pk=packets(p); q=pivot(p)
    ck(3*p<=q<=4*p);ck(0<tau(p)<=12*p*p)
    ck(all(not d or u>=49*p*p*d for u,d in pk))
    C=correction(p,pk);lo,hi=enclose(C)
    ck(lo>=-144*p*p);ck(hi<=360*p*p)
    fixtures=[]
    for beta in [Q(0),2*p,p/2,p/8]:
        R=reserve(p,beta*beta,pk)
        bound=add(R,logq(1/(49*p*p)),q*beta*beta)
        ck(enclose(bound)[0]>=0)
        fixtures.append({'beta':str(beta),'reserve':bounds(R),'certified_loss_bound':True})
    profiles.append({'p':str(p),'q':str(q),'tau':str(tau(p)), 'correction':bounds(C),'fixtures':fixtures})
    dump('RARE_PROFILES.json',profiles)

P=[Q(1,16)]
for _ in range(5):P.append(tau(P[-1]))
ck(P[1]<Q(3,64));ck(P[5]<Q(1,1<<21))
loss={}
for p in P[1:5]:loss=add(loss,logq(1/(49*p*p)),2*p)
tail=Q(260,9*(1<<19))
lo,hi=enclose(loss);totalhi=Q(9,28)+hi+tail
ck(totalhi<1)
dump('INFINITE_LOSS_CERTIFICATE.json',{'precision_bits':192,'atanh_terms':TERMS,'iterates':[str(p) for p in P], 'four_middle_losses':bounds(loss),'initial_loss_upper':'9/28','tail_upper':str(tail),'total_upper':str(totalhi),'total_upper_display':float(totalhi),'gap_to_one':str(1-totalhi)})

direct=[]
for table in range(1,15):
    core=[-1 if table>>x&1 else 1 for x in range(4)]
    p=Q(table.bit_count(),4);pk=packets(p);q=pivot(p)
    W=fwht(core)
    parent=[]
    for x in range(4096):
        outer=sum((core[x>>(2*j)&3]<0)<<j for j in range(6))
        parent.append(-1 if outer in NEG else 1)
    V=fwht(parent);N=len(V)
    outer_w=fwht([-1 if z in NEG else 1 for z in range(64)])
    raw=[];m=1-2*p
    for T in range(64):
        raw.append(sum((Q(w,64)*m**(Z.bit_count()-T.bit_count()) for Z,w in enumerate(outer_w) if Z&T==T),Q(0)))
    for S,value in enumerate(V):
        occupied=0;product=Q(1)
        for j in range(6):
            subset=S>>(2*j)&3
            if subset:occupied|=1<<j;product*=Q(W[subset],4)
        ck(Q(value,N)==raw[occupied]*product)
    # Coefficient-level checks are exact. Entropy/erasure log expressions are
    # independently enclosed, with an interval around zero recorded rather than
    # mistaking a small float for a proof.
    Cp=correction(p,pk)
    hdiff=add(add(entropy(V),entropy(W),-6*q),Cp,Q(-1))
    he=enclose(hdiff);ck(he[0]<=0<=he[1]);ck(he[1]-he[0]<Q(1,1<<140))
    erasures=[]
    for i in range(2):
        d=Q(sum(w*w for s,w in enumerate(W) if s>>i&1),16)
        dp=Q(sum(w*w for s,w in enumerate(V) if s>>i&1),N*N);ck(dp==q*d)
        bdiff=add(add(erasure(V,i),erasure(W,i),-q),reserve(p,Q(W[1<<i]**2,16),pk),Q(-1))
        be=enclose(bdiff);ck(be[0]<=0<=be[1]);ck(be[1]-be[0]<Q(1,1<<140))
        erasures.append({'coordinate':i,'interval':bounds(bdiff),'log_expression_exact_zero':not bdiff})
    # Exact validation of every full biased outer coefficient and physical
    # spectrum, separate from the logarithm comparison above.
    masses=[Q(w*w,N*N) for w in V]
    ck(sum(masses)==1)
    direct.append({'core_negative_table':table,'p':str(p),'influence_exact':True,'H_identity_interval':bounds(hdiff),'B_identity_intervals':erasures,'log_expression_H_exact_zero':not hdiff})
    dump('DIRECT_PHYSICAL_FIXTURES.json',direct)

points=[]
for n in range(4,9):
    N=1<<n;p=Q(1,N);truth=[-1]+[1]*(N-1);W=fwht(truth)
    beta=Q(W[1],N);d=Q(sum(W[x]**2 for x in range(N) if x&1),N*N)
    ck(beta==-2*p and d==2*p);pk=packets(p)
    B=erasure(W,0);R=reserve(p,beta*beta,pk);q=pivot(p)
    ck(enclose(add(R,logq(1/(49*p*p)),q*beta*beta))[0]>=0)
    points.append({'n':n,'p':str(p),'beta':str(beta),'influence':str(d),'core_erasure':bounds(B),'composed_ratio_change':bounds(scale(R,1/(q*d))),'composed_influence':str(6*q*n*d),'compressed_parent_only':True})
dump('POINT_DEFECT_FIXTURES.json',points)
def bmap(p):return p**4*(3-2*p*p)
a=Q(1,16);b=Q(7,32)
ck(tau(a)<a);ck(b<tau(b)<Q(3,8));ck(bmap(Q(3,8))<a);ck(bmap(Q(1,2))==Q(5,32)<b)
ck(2-10*b+5*b*b==Q(53,1024))
dump('BIAS_DYNAMICS_CERTIFICATE.json',{'tau_1_16':str(tau(a)),'tau_7_32':str(tau(b)),'b_3_8':str(bmap(Q(3,8))),'b_1_2':str(bmap(Q(1,2))),'convexity_factor_at_7_32':'53/1024','fixed_point_polynomial_ascending':[-1,12,-28,27,-12,2],'rational_root_candidates':[1,-1,'1/2','-1/2'],'actual_core_biases':'dyadic; none equals the unique irrational fixed point in (1/16,7/32)'})
dump('VALIDATION.json',{'helper':'A075-rare-tail-v1','checks':arithmetic_state.checks,'runtime_seconds':time.perf_counter()-start,'direct_cores':len(direct),'profiles':len(profiles),'point_defects':len(points),'max_physical_dimension':12,'full_fei':'OPEN'})
print(json.dumps({'checks':arithmetic_state.checks,'runtime_seconds':time.perf_counter()-start,'total_loss_upper':float(totalhi),'direct_cores':len(direct)}))
