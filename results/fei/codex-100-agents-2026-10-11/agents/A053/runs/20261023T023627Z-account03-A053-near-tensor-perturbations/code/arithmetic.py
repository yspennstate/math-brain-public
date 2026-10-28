from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product,combinations
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();assertions=0
def check(ok):
    global assertions
    assertions+=1
    assert ok,assertions
    if time.perf_counter()-START>55:raise RuntimeError('55-second frozen guard')
def save(name,obj):(RUN/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def fwht(table):
    v=list(table);step=1
    while step<len(v):
        for j in range(0,len(v),2*step):
            for k in range(j,j+step):u,w=v[k],v[k+step];v[k]=u+w;v[k+step]=u-w
        step*=2
    return v
def frac(a,b):return F(a,b) if b else F(0)
def quartet(a,b,c,d):
    A=a*a+b*b;B=c*c+d*d;J=a*a+c*c;L=b*b+d*d;q=A+B
    ci=frac(4*a*a*b*b,A)+frac(4*c*c*d*d,B)
    cj=frac(4*a*a*c*c,J)+frac(4*b*b*d*d,L)
    p=frac(4*(a*d+b*c)**2,q)
    Q=frac(4*((a*b+c*d)**2+(a*c+b*d)**2+(a*d+b*c)**2),q)
    mi=ci-frac(4*(a*b+c*d)**2,q);mj=cj-frac(4*(a*c+b*d)**2,q)
    check(mi>=0 and mj>=0);check(Q==ci+cj+p-mi-mj)
    check(mi==frac(4*(a*d-b*c)**2*(a*c-b*d)**2,q*A*B))
    check(mj==frac(4*(a*d-b*c)**2*(a*b-c*d)**2,q*J*L))
    Delta=a*d-b*c;E=(a*c==b*d and a*b==c*d)
    check((mi==mj==0)==(Delta==0 or E))
    if Delta and E:
        diag=(b==c==0);anti=(a==d==0)
        balanced=all((a,b,c,d)) and any(d==s*a and c==s*b for s in (-1,1)) and a*a!=b*b
        check(diag or anti or balanced)
        if balanced:
            vals=[a+b*x+c*y+d*x*y for x,y in product((-1,1),repeat=2)]
            check(sum(v!=0 for v in vals)==2);check(Q>=q)
    return ci,cj,Q,p,mi,mj
@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1);zz=z*z;power=z;value=F(0)
    for j in range(24):value+=2*power/(2*j+1);power*=zz
    tail=2*abs(power)/(49*(1-zz))
    return value-tail,value+tail
LN2=ln_unit(F(2))
@lru_cache(None)
def log2(x):
    k=x.numerator.bit_length()-x.denominator.bit_length();r=x/(F(2)**k)
    if r<1:k-=1;r*=2
    if r>=2:k+=1;r/=2
    lo,hi=ln_unit(r);return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def entropy(ps):
    lo=hi=F(0)
    for p in ps:
        if p:
            a,b=log2(p);lo-=p*b;hi-=p*a
    return lo,hi
def h2(x):return entropy([x,1-x])
def coded_truth(h):
    k=(len(h)-1).bit_length();n=3*k
    return [h[sum(((x>>(3*j))&7).bit_count()%2<<j for j in range(k))] for x in range(1<<n)]
def infs(table):
    N=len(table);n=(N-1).bit_length()
    return [F(sum(table[x]!=table[x^(1<<i)] for x in range(N)),N) for i in range(n)]
def seed_check(h):
    f=coded_truth(h);N=len(f);n=(N-1).bit_length();ints=fwht(f)
    check(sum(a*a for a in ints)==N*N)
    support=[s for s,a in enumerate(ints) if a]
    for s,t in combinations(support,2):check((s^t).bit_count()>=3)
    hi=infs(h);fi=infs(f)
    check(fi==[hi[i//3] for i in range(n)])
    logical=fwht(h);check(sorted(F(a*a,N*N) for a in ints if a)==sorted(F(a*a,len(h)**2) for a in logical if a))
    g=f.copy();g[0]*=-1;new=fwht(g);shift=-2*f[0]
    check(all(b==a+shift for a,b in zip(ints,new)))
    gi=infs(g);p=F(1,N)
    for i in range(n):check(abs(gi[i]-fi[i])<=2*p)
    Ci=[];singles=[]
    for i in range(n):
        collision=F(0);B=F(0);G=F(0);off=F(0)
        for t in range(N):
            if t>>i&1:continue
            a,b=new[t],new[t|1<<i];q=a*a+b*b
            check(not(ints[t] and ints[t|1<<i]))
            collision+=frac(4*a*a*b*b,q)/(N*N)
            anchor=0 if ints[t] or not ints[t|1<<i] else 1
            off+=F((b if anchor==0 else a)**2,N*N)
            ps=[F(a*a,q),F(b*b,q)];B+=F(q,N*N)*entropy(ps)[1]
            c=frac(4*a*a*b*b,q*q);G+=F(q,N*N)*log2(1+c)[1]
        check(off==2*p);check(collision<=8*p);check(B<=h2(2*p)[1])
        check(B+G<(2*n+13)*p)
        Ci.append(collision);singles.append({'i':i,'C':str(collision),'V_upper':str(B+G),'Influence':str(gi[i])})
    pairs=[]
    for i,j in combinations(range(n),2):
        total=[F(0)]*6;B=F(0);G=F(0);off=F(0)
        for t in range(N):
            if t&(1<<i|1<<j):continue
            idx=[t,t|1<<i,t|1<<j,t|1<<i|1<<j]
            old=[ints[s] for s in idx];check(sum(a!=0 for a in old)<=1)
            vals=[new[s] for s in idx];q=sum(a*a for a in vals)
            quantities=quartet(*vals)
            for k,v in enumerate(quantities):total[k]+=v/(N*N)
            w=[sum(a*(x if k&1 else 1)*(y if k&2 else 1) for k,a in enumerate(vals)) for x,y in product((-1,1),repeat=2)]
            direct=(F(sum(v**4 for v in w),4*q)-q)/(N*N)
            check(direct==quantities[2]/(N*N))
            anchor=next((k for k,v in enumerate(old) if v),0)
            off+=F(sum(v*v for k,v in enumerate(vals) if k!=anchor),N*N)
            B+=F(q,N*N)*entropy([F(a*a,q) for a in vals])[1]
            G+=F(q,N*N)*log2(1+quantities[2]/q)[1]
        check(total[0]==Ci[i] and total[1]==Ci[j]);check(total[2]<=16*p)
        check(total[4]+total[5]<=16*p);check(off==3*p)
        check(B<=h2(3*p)[1]+3*p*log2(F(3))[1]);check(B+G<(3*n+29)*p)
        pairs.append({'i':i,'j':j,'C_pair':str(total[2]),'refund_sum':str(total[4]+total[5]),'P':str(total[3]),'V_upper':str(B+G),'Influence':str(gi[i]+gi[j])})
    return {'n':n,'seed_truth_sha256':hashlib.sha256(bytes(1 if v==1 else 0 for v in f)).hexdigest(),'singletons':singles,'pairs':pairs,'minimum_support_distance':min(((s^t).bit_count() for s,t in combinations(support,2)),default=None)}
def main():
    rows=0
    for row in product(range(-2,3),repeat=4):quartet(*row);rows+=1
    save('ROW_CLASSIFICATION.json',{'status':'PASS','rational_real_quartets':rows,'Boolean_realizability_not_assumed':True})
    cases=[]
    for code in range(16):
        h=[-1 if code>>x&1 else 1 for x in range(4)]
        record=seed_check(h);record['logical_code']=code;cases.append(record)
        save('CODE_CASES.json',{'status':'IN_PROGRESS','completed':len(cases),'cases':cases})
    h=[-1]+[1]*7;record=seed_check(h);record['logical_name']='three-bit point defect';cases.append(record)
    save('CODE_CASES.json',{'status':'PASS','completed':len(cases),'cases':cases})
    save('EXACT_CHECK.json',{'status':'PASS','assertions':assertions,'real_quartets':rows,'Boolean_roots':17,'n6_roots':16,'n9_roots':1,'singleton_cuts':105,'pair_cuts':276,'total_cuts':381,'runtime_seconds':time.perf_counter()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'Integer FWHT and physical edges; Fraction; rational atanh24-term logarithm intervals; exact signs only'})
    print((RUN/'out/EXACT_CHECK.json').read_text())
if __name__=='__main__':main()
