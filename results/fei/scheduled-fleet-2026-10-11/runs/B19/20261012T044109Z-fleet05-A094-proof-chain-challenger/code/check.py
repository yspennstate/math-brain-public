from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,product
from math import factorial
from collections import defaultdict
import json,time,sys
RUN=Path(__file__).resolve().parents[1]
SPEC={'helper_version':'B19-RANKCODE-GLOBAL-ORDER-NOGO@1 / A086-ACTIVATION-REFERENCE-DEBT-PROJECTION@1 independent challenge v2','family':'XORs of equal-width point defects, all balanced <=3-bit cores under point activation, and balanced point-defect tensor cores under dictionary/compatible references','domain':{'rank_L_m':[[2,1],[2,2],[2,3],[3,1],[3,2]],'balanced_dimensions':[1,2,3],'r':[1,2,3],'reference_types':['uniform-nonempty','nonuniform product conditional nonempty scaled by 1/2','compatible transfer of uniform-nonempty data reference','compatible transfer of half-mass uniform-nonempty data reference'],'tensor_seed_L':[2,3],'tensor_t':[1,2,3],'quantitative_row':{'L':8,'n':1000000000}},'case_count':{'coordinate_orders':1472,'projection_cases':936,'activated_tensors':18,'large_dimension_analytic_rows':1},'symmetry':'no reduction in coordinate-order enumeration; balanced labelled cores exhaust all tables; large dimension evaluated only through exact moment formulas, never enumerated','arithmetic':'integer FWHT; Fraction probabilities/counts; exact rational coefficients of logarithms of primes; rational atanh-series intervals with proved remainder','memory_estimate_MB':50,'max_runtime_seconds':60,'dimension_escalation':False}
def write(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
if '--freeze' in sys.argv:write(RUN/'FROZEN_SPEC.json',SPEC);print('FROZEN');sys.exit()
assert json.loads((RUN/'FROZEN_SPEC.json').read_text())==SPEC
start=time.perf_counter();checks=0
def ck(b):
    global checks
    checks+=1
    assert b
def fwht(f):
    a=list(f);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
        h*=2
    return a
def probs(f):return [Q(x*x,len(f)**2) for x in fwht(f)]
def inf(f):
    return sum((Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(len(f).bit_length()-1)),Q(0))
def fac(n):
    result={};d=2
    while d*d<=n:
        while n%d==0:result[d]=result.get(d,0)+1;n//=d
        d+=1
    if n>1:result[n]=result.get(n,0)+1
    return result
def logform(q):
    q=Q(q);assert q>0
    r=defaultdict(Q)
    for d,e in fac(q.numerator).items():r[d]+=e
    for d,e in fac(q.denominator).items():r[d]-=e
    return {d:Q(e) for d,e in r.items() if e}
def add(a,b,c=Q(1)):
    a=dict(a)
    for k,v in b.items():a[k]=a.get(k,Q(0))+c*v
    return {k:v for k,v in a.items() if v}
def KL(P,R):
    out={}
    for k,p in P.items():
        if p:out=add(out,logform(p/R[k]),p)
    return out
def ent(P):
    out={}
    for p in P.values():
        if p:out=add(out,logform(1/p),p)
    return out
def CE(P,R):
    out={}
    for k,p in P.items():
        if p:out=add(out,logform(1/R[k]),p)
    return out
def lni(x,N=50):
    x=Q(x);assert x>0
    exponent=0
    while x>=2:x/=2;exponent+=1
    while x<1:x*=2;exponent-=1
    def base(y):
        z=(y-1)/(y+1);term=z;s=Q(0)
        for j in range(N):s+=term/Q(2*j+1);term*=z*z
        err=2*abs(z)**(2*N+1)/(Q(2*N+1)*(1-z*z))
        s*=2
        return s-err,s+err
    lo,hi=base(x);l2,h2=base(Q(2))
    if exponent>=0:return lo+exponent*l2,hi+exponent*h2
    return lo+exponent*h2,hi+exponent*l2
def interval(form):
    lo=Q(0);hi=Q(0)
    for k,c in form.items():
        l,h=lni(Q(k))
        if c>=0:lo+=c*l;hi+=c*h
        else:lo+=c*h;hi+=c*l
    l2,h2=lni(Q(2))
    vals=[lo/l2,lo/h2,hi/l2,hi/h2]
    return min(vals),max(vals)
rank_rows=[];orders=0
for L,m in SPEC['domain']['rank_L_m']:
    n=L*m;d=Q(1,2**(L-1))
    f=[]
    for x in range(2**n):
        value=1
        for b in range(m):value*= -1 if ((x>>(b*L))&((1<<L)-1))==0 else 1
        f.append(value)
    wa=fwht(f);wi=[x*x for x in wa];den=len(f)**2
    ck(sum(wi)==den);ck(inf(f)==n*d)
    target=[0]+[int(d*den)]*n
    for S,w in enumerate(wi):
        for k in range(1,S.bit_count()+1):target[k]-=w
    I=n*d;E2=sum(Q(w,den)*S.bit_count()**2 for S,w in enumerate(wi));ck(E2/I==I+Q(L+1,2)-L*d)
    order_count=0
    for order in permutations(range(n)):
        vec=[0]*(n+1);prefix=0
        for pos,c in enumerate(order,1):
            prefix|=1<<c;mean_numer=0;event_weight=0
            for S,w in enumerate(wi):
                if S>>c&1:
                    selected=(S&prefix).bit_count();vec[pos]+=w;vec[selected]-=w
                    mean_numer+=w*selected;event_weight+=w
            a=sum(j//L==c//L for j in order[:pos-1])
            exact=1+Q(a,2)+(pos-1-a)*d
            ck(Q(mean_numer,event_weight)==exact)
            ck(exact<=Q(L+1,2)+(pos-1)*d)
            ck(event_weight==d*den)
        ck(vec==target);orders+=1;order_count+=1
    rank_rows.append({'L':L,'m':m,'orders':order_count,'I':str(I),'R_log_integer_coefficients':[str(Q(x,den)) for x in target]})
ck(orders==1472)
projection_cases=0;balanced_cores=0
for n in [1,2,3]:
    for bits in range(2**(2**n)):
        if bits.bit_count()!=2**(n-1):continue
        g=[1 if bits>>x&1 else -1 for x in range(2**n)];pg=probs(g);balanced_cores+=1
        ck(pg[0]==0)
        for r in [1,2,3]:
            p=Q(1,2**r);v=p*(2-p);beta=1/(2-p)
            f=[g[T] if U==0 else 1 for U in range(2**r) for T in range(2**n)]
            P0=probs(f);P={ (S//2**n,S%2**n):w/v for S,w in enumerate(P0) if S}
            ck(1-P0[0]==v);ck(inf(f)==p*(inf(g)+r))
            for (U,T),w in P.items():ck(v*w==(p*p*pg[T] if T else p*p))
            refs=[];states=list(P)
            refs.append({x:Q(1,len(states)) for x in states})
            raw={}
            for U,T in states:
                S=U*2**n+T;q=Q(1)
                for i in range(n+r):
                    b=Q(1 if i%2==0 else 2,3);q*=b if S>>i&1 else 1-b
                raw[U,T]=q
            total=sum(raw.values());refs.append({x:w/total/2 for x,w in raw.items()})
            for z in [Q(1),Q(1,2)]:
                refs.append({(U,T):p*p*(z/Q(2**n-1) if T else 1)/v for U,T in states})
            for index,R in enumerate(refs):
                M=sum(R.values());q={x:w/M for x,w in R.items()};gamma=sum(w for (U,T),w in q.items() if T)
                qg={T:sum(q[U,T] for U in range(2**r))/gamma for T in range(1,2**n)}
                lhs=add({},KL(P,R),v)
                chain=add({},logform(1/M),v)
                chain=add(chain,KL({0:1-beta,1:beta},{0:1-gamma,1:gamma}),v)
                core=add({},KL({T:w for T,w in enumerate(pg) if T},qg),p)
                chain=add(chain,core)
                ctrl0={U:q[U,0]/(1-gamma) for U in range(1,2**r)}
                chain=add(chain,KL({U:Q(1,2**r-1) for U in ctrl0},ctrl0),v*(1-beta))
                for T in range(1,2**n):
                    marginal=sum(q[U,T] for U in range(2**r))
                    ctrl={U:q[U,T]/marginal for U in range(2**r)}
                    chain=add(chain,KL({U:p for U in ctrl},ctrl),p*pg[T])
                ck(lhs==chain);ck(Q(0)<gamma<1);ck(M<=1)
                if index>=2:
                    z=Q(1) if index==2 else Q(1,2)
                    expected=add({},KL({T:w for T,w in enumerate(pg) if T},{T:z/Q(2**n-1) for T in range(1,2**n)}),p)
                    ck(lhs==expected)
                    ck(M==(1-p+z)/(2-p));ck(gamma==z/(1-p+z))
                projection_cases+=1
ck(balanced_cores==78);ck(projection_cases==936)
tensor_rows=[]
for L in [2,3]:
    ih=Q(L,2**(L-1))
    h=[-1]+[1]*(2**L-1);ph=probs(h);Hh=ent(dict(enumerate(ph)))
    for t in [1,2,3]:
        N=t*L+1;g=[]
        for x in range(2**N):
            sign=1 if not(x&1) else -1
            for b in range(t):sign*=-1 if ((x>>(1+b*L))&((1<<L)-1))==0 else 1
            g.append(sign)
        Pg=probs(g);ck(Pg[0]==0);ck(inf(g)==1+t*ih);ck(ent(dict(enumerate(Pg)))==add({},Hh,t))
        dictionary={T:Q(1,2**N-1) for T in range(1,2**N)}
        cg=logform(2**N-1);Dg=add(cg,Hh,-t)
        ck(CE({T:w for T,w in enumerate(Pg) if T},dictionary)==cg)
        for r in [1,2,3]:
            p=Q(1,2**r);v=p*(2-p)
            F=[g[T] if U==0 else 1 for U in range(2**r) for T in range(2**N)]
            PF=probs(F);ck(inf(F)==p*(1+t*ih+r))
            A=add(logform(1/(1-p)**2),(logform(1/p**2)),p*(2-p))
            # Vacuum contributes its actual probability, not a probability-one logarithm.
            A=add(add({},logform(1/(1-p)**2),(1-p)**2),logform(1/p**2),p*(2-p))
            hf=add(add({},Hh,p*t),A)
            ck(ent(dict(enumerate(PF)))==hf)
            transfer={(U,T):(p*p*dictionary[T] if T else p*p) for U in range(2**r) for T in range(2**N) if U or T}
            full_transfer={U*2**N+T:w for (U,T),w in transfer.items()};full_transfer[0]=(1-p)**2
            ck(sum(full_transfer.values())==1)
            cost=CE(dict(enumerate(PF)),full_transfer);ck(cost==add(add({},cg,p),A))
            ck(add(cost,hf,-1)==add({},Dg,p))
            # Direct one-gate uniform dictionary output (A008 generic generator) on full activated support.
            onecost=add({},logform(2**(N+r)-1),v)
            Pplus={S:w/v for S,w in enumerate(PF) if S}
            directq={S:Q(1,2**(N+r)-1) for S in range(1,2**(N+r))}
            debt=add({},KL(Pplus,directq),v)
            sector_gamma=Q(2**r*(2**N-1),2**(N+r)-1);sector_beta=1/(2-p)
            expected=add(add({},Dg,p),KL({1:sector_beta,0:1-sector_beta},{1:sector_gamma,0:1-sector_gamma}),v)
            ck(debt==expected)
            tensor_rows.append({'L':L,'t':t,'r':r,'data_dimension':N,'seed_influence':str(ih),'activated_influence':str(inf(F)),'transfer_debt_log_prime_form':{str(k):str(vv) for k,vv in add({},Dg,p).items()},'onegate_dictionary_cost_log_prime_form':{str(k):str(vv) for k,vv in onecost.items()}})
L=8;n=1000000000;d=Q(1,128);I=n*d;a=Q(L+1,2)-L*d
ln2lo,ln2hi=lni(Q(2));elllo,ellhi=lni(1+a/I);il,ih=lni(I+1)
lower=2*(L-1)-2/ln2lo*(ellhi+(1+ih)/I)
target=Q(1399999,100000);ck(lower>target)
ph=probs([-1]+[1]*255);hr=ent(dict(enumerate(ph)));hl,hh=interval(hr)
ck(hh/(L*d)<Q(3843,1000))
row={'L':8,'n':n,'I':str(I),'rank_term_over_I_lower':str(lower),'certified_rank_term_over_I_gt':'13.99999','entropy_over_I_interval':[str(hl/(L*d)),str(hh/(L*d))],'certified_entropy_over_I_lt':'3.843','logarithm_terms':50,'numeric_floats_used':False}
write(RUN/'out/QUANTITATIVE_CERTIFICATE.json',row)
elapsed=time.perf_counter()-start;ck(elapsed<60)
write(RUN/'out/EXACT_RESULTS.json',{'status':'PASS','assertions':checks,'coordinate_orders':orders,'rank_rows':rank_rows,'balanced_cores':balanced_cores,'projection_cases':projection_cases,'activated_tensor_cases':len(tensor_rows),'tensor_rows':tensor_rows,'seconds':elapsed,'arithmetic':'integer FWHT and Fraction; exact log-prime identities; rational logarithm intervals with proved remainder','large_dimension_truth_tables_computed':False})
print(json.dumps({'status':'PASS','assertions':checks,'coordinate_orders':orders,'projection_cases':projection_cases,'tensor_cases':len(tensor_rows),'seconds':elapsed}))
