from pathlib import Path
from fractions import Fraction as R
from math import comb
from functools import lru_cache
import json, time, sys

ROOT=Path(__file__).resolve().parents[1]
NEG={0,1,2,4,8,16,32,6,17,40}
TABLE=[-1 if x in NEG else 1 for x in range(64)]
COUNT=0
def check(cond):
    global COUNT
    assert cond
    COUNT+=1
def save(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2),encoding='utf-8')
def fwht(a):
    a=list(a);w=1
    while w<len(a):
        for k in range(0,len(a),2*w):
            for j in range(k,k+w):
                x,y=a[j],a[j+w];a[j],a[j+w]=x+y,x-y
        w*=2
    return a
WH=[R(x,64) for x in fwht(TABLE)]

def trim(a):
    a=list(map(R,a))
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):
    c=[R(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)
def mul(a,b):
    c=[R(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def compose(a,b):
    c=[R(0)]
    for x in reversed(a):c=add(mul(c,b),[x])
    return c
def evaluate(a,x):
    c=R(0)
    for z in reversed(a):c=c*x+z
    return c
TAU=list(map(R,[0,0,12,-28,27,-12,2]))
B=list(map(R,[0,0,0,0,3,0,-2]))
Q=list(map(R,[0,24,-84,108,-60,12]))
QC=compose(Q,[1,-1])
def bernstein(a,lo,hi):
    power=compose(a,[lo,hi-lo]);n=len(a)-1
    power+= [R(0)]*(n+1-len(power))
    return [sum(power[j]*R(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
def certify(name,poly,lo,hi,strict):
    leaves=[]
    for k in range(32):
        a=lo+(hi-lo)*R(k,32);b=lo+(hi-lo)*R(k+1,32)
        coeff=bernstein(poly,a,b)
        check(min(coeff)>0 if strict else min(coeff)>=0)
        leaves.append({'box':[str(a),str(b)],'Bernstein_coefficients':[str(x) for x in coeff]})
    check(R(leaves[0]['box'][0])==lo and R(leaves[-1]['box'][1])==hi)
    for a,b in zip(leaves,leaves[1:]):check(a['box'][1]==b['box'][0])
    save(name+'.json',{'polynomial_power_coefficients':[str(x) for x in poly],'domain':[str(lo),str(hi)],'strict':strict,'leaves':leaves})

N=24;BITS=64;ARG_BITS=80;SCALE=1<<BITS
def floor(x,bits=BITS):return R((x.numerator<<bits)//x.denominator,1<<bits)
def ceil(x,bits=BITS):return -floor(-x,bits)
def ln_series(x):
    z=(x-1)/(x+1);t=z;s=R(0)
    for j in range(N):s+=t/(2*j+1);t*=z*z
    tail=2*t/((2*N+1)*(1-z*z))
    return 2*s,2*s+tail
L2=ln_series(R(2))
@lru_cache(maxsize=2000)
def log2(x):
    check(x>0);k=0
    # Integer bit lengths reduce an arbitrarily small rational in one step.
    k=x.numerator.bit_length()-x.denominator.bit_length()
    x=x/R(2)**k
    if x<1:x*=2;k-=1
    if x>2:x/=2;k+=1
    a=floor(x,ARG_BITS);b=ceil(x,ARG_BITS)
    lo=ln_series(a)[0];hi=ln_series(b)[1]
    corners=[u/v+k for u in (lo,hi) for v in L2]
    return floor(min(corners)),ceil(max(corners))
def ent(masses):
    lo=hi=R(0)
    for p in masses:
        if p:
            a,b=log2(p);lo+=floor(-p*b);hi+=ceil(-p*a)
    return floor(lo),ceil(hi)
def add_iv(a,b):return a[0]+b[0],a[1]+b[1]
def sub_iv(a,b):return a[0]-b[1],a[1]-b[0]
def scale_iv(a,x):
    assert x>=0
    return floor(a[0]*x),ceil(a[1]*x)
def raw_coeff(m,T):
    k=T.bit_count()
    return sum(WH[W]*m**(W.bit_count()-k) for W in range(64) if W&T==T)
def outer(p):
    m=1-2*p;v=1-m*m
    masses=[v**T.bit_count()*raw_coeff(m,T)**2 for T in range(64)]
    check(sum(masses)==1)
    q=evaluate(Q,p)/6
    check(sum(T.bit_count()*masses[T] for T in range(64))==6*v*q)
    for j in range(6):
        pivotal=sum(p**x.bit_count()*(1-p)**(5-x.bit_count()) for x in range(32)
            if TABLE[(x&((1<<j)-1))|((x>>j)<<(j+1))]!=TABLE[((x&((1<<j)-1))|((x>>j)<<(j+1)))|(1<<j)])
        check(pivotal==q)
        check(sum(masses[T] for T in range(64) if T&(1<<j))==v*q)
    C=sub_iv(ent(masses),scale_iv(ent([v,1-v]),6*q))
    return masses,C,q
def influence(table):
    n=(len(table)-1).bit_length()
    ds=[R(sum(table[x]!=table[x|(1<<j)] for x in range(len(table)) if not x&(1<<j)),len(table)//2) for j in range(n)]
    return ds

def algebra():
    check(fwht(fwht(TABLE))==[64*x for x in TABLE])
    check(sum(x*x for x in WH)==1)
    check(trim([i*x for i,x in enumerate(TAU)][1:])==Q)
    check(trim([i*x for i,x in enumerate(B)][1:])==QC)
    check(sum(T.bit_count()*WH[T]**2 for T in range(64))==evaluate(Q,R(1,2)))
    certify('LOW_Q_CERTIFICATE',add(Q,[-R(19,16)]),R(1,16),R(7,32),True)
    certify('COMPLEMENT_Q_CERTIFICATE',add(QC,[-R(1,9)]),R(7,32),R(1,2),True)
    certify('RARE_Q_LOWER',add([x/6 for x in Q],[0,-3]),R(0),R(1,16),False)
    certify('RARE_Q_UPPER',add([0,4],[-x/6 for x in Q]),R(0),R(1,16),False)
    certify('RARE_BIAS_CONTRACTION',add([0,0,12],[-x for x in TAU]),R(0),R(1,16),False)
    endpoints={
        'tau_7_over_32':evaluate(TAU,R(7,32)),
        'b_3_over_8':evaluate(B,R(3,8)),
        'b_1_over_2':evaluate(B,R(1,2)),
        'Q_1_over_16':evaluate(Q,R(1,16)),
        'Q_complement_7_over_32':evaluate(QC,R(7,32))}
    check(endpoints['tau_7_over_32']<R(3,8))
    check(endpoints['b_3_over_8']<R(1,16))
    check(endpoints['b_1_over_2']==R(5,32))
    check(sum(R(comb(6,k))*R(1,4)**(k-2) for k in range(2,7))==R(5385,256))
    check(72+96+R(48465,256)<360)
    check(R(288,19)<16 and 162<256)
    check(R(38,3)+R(16,7)==R(314,21))
    check(R(152,3)+16==R(200,3))
    check(R(314,21)+R(24,5)==R(2074,105)<20)
    check(R(200,3)+16==R(248,3)<83)
    save('ALGEBRA.json',{'endpoints':{k:str(v) for k,v in endpoints.items()},'moderate_interval':['-314/21','200/3'],'complete_interval':['-2074/105','248/3'],'all_checks_passed':True})

def physical(mask):
    table=[-1 if mask&(1<<x) else 1 for x in range(4)]
    p=R(sum(x<0 for x in table),4)
    check(p<=R(1,2))
    selected=[-x for x in table] if p>R(7,32) else table
    chosen=1-p if p>R(7,32) else p
    f=[]
    for x in range(4096):
        y=sum((selected[(x>>(2*j))&3]<0)<<j for j in range(6))
        f.append(TABLE[y])
    corewh=[R(x,4) for x in fwht(selected)]
    m=corewh[0];full=fwht(f)
    check(fwht(full)==[4096*x for x in f]);check(sum(x*x for x in full)==4096**2)
    raw=[raw_coeff(m,T) for T in range(64)]
    for x in range(4096):
        T=0;amplitude=R(1)
        for j in range(6):
            block=(x>>(2*j))&3
            if block:T|=1<<j;amplitude*=corewh[block]
        check(R(full[x],4096)==raw[T]*amplitude)
    ds=influence(table);fd=influence(f);_,C,q=outer(chosen)
    for j in range(6):
        for i in range(2):check(fd[2*j+i]==q*ds[i])
    check(R(sum(x<0 for x in f),4096)==(1-evaluate(TAU,chosen)))
    H=ent([R(x*x,4096**2) for x in full]);HG=ent([x*x for x in corewh])
    difference=sub_iv(sub_iv(H,scale_iv(HG,6*q)),C)
    check(difference[0]<=0<=difference[1]);check(difference[1]-difference[0]<R(1,10**12))
    check(C[0]/(6*q*sum(ds))>=-R(8,7))
    check(C[1]/(6*q*sum(ds))<8)
    save('PHYSICAL_'+str(mask)+'.json',{'core_mask':mask,'physical_bits':12,'signed_Fourier_coefficient_checks':4096,'chosen_p':str(chosen),'I_core':str(sum(ds)),'I_parent':str(sum(fd)),'q':str(q),'C_interval':[str(x) for x in C],'entropy_identity_residual_interval':[str(x) for x in difference],'scope':'Exact coefficient and influence identity; analytic proof establishes exact entropy identity, narrow intervals are implementation checks.'})

def trajectories():
    records=[]
    for n,M in [(4,1),(5,7),(1,1)]:
        table=[-1 if x<M else 1 for x in range(1<<n)]
        p=R(M,1<<n);I=sum(influence(table));cum=(R(0),R(0));steps=[]
        for k in range(3):
            chosen=1-p if p>R(7,32) else p
            _,C,q=outer(chosen);cum=add_iv(cum,scale_iv(C,1/(6*q*I)))
            check(cum[0]>=-R(2074,105));check(cum[1]<=R(248,3))
            nxt=evaluate(B,p) if p>R(7,32) else evaluate(TAU,p)
            steps.append({'depth':k,'minority':str(p),'I':str(I),'C_interval':[str(x) for x in C],'cumulative_interval':[str(x) for x in cum]})
            I*=6*q;p=nxt
        records.append({'initial_core':[n,M],'steps':steps})
    save('TRAJECTORY_FIXTURES.json',records)
    thin=[]
    for v,q in [(R(1,4),R(1,5)),(R(15,64),R(1,5)),(R(3,4),R(1,54)),(R(1),R(1,2))]:
        L=sub_iv(add_iv(scale_iv(ent([v,1-v]),q),scale_iv(ent([q,1-q]),v)),ent([v*q,1-v*q]))
        check(L[0]>0 if v<1 else L[0]<=0<=L[1])
        thin.append({'v':str(v),'q':str(q),'thinning_remainder':[str(x) for x in L]})
    save('THINNING_FIXTURES.json',thin)

if __name__=='__main__':
    start=time.perf_counter();algebra()
    pilot='--pilot' in sys.argv
    if not pilot:
        physical(1);physical(6);trajectories()
    elapsed=time.perf_counter()-start
    check(elapsed<(55 if pilot else 120))
    result={'mode':'pilot' if pilot else 'full','exact_assertions':COUNT,'polynomial_boxes':160,'physical_coefficient_checks':0 if pilot else 8192,'all_checks_passed':True,'runtime_seconds':elapsed,'memory_estimate_MB':100,'full_FEI':'OPEN','independent_review':'pending'}
    save('PILOT_RESULT.json' if pilot else 'VALIDATION.json',result)
    print(json.dumps(result),flush=True)
