"""Independent literal-cube verifier. Frozen domain in ../out/FROZEN_SPEC.json."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
import json, sys, time

RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNT=0; ROOTS=0; HIST=0
POSITIVE=0; NEGATIVE=0; RESET_WITNESS=None
def ck(x):
    global COUNT
    COUNT+=1
    assert x, COUNT
    if time.perf_counter()-START>55: raise TimeoutError('frozen runtime guard')
def dump(n,x): (RUN/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def ln(q):
    z=(q-1)/(q+1); term=z; val=F(0)
    for k in range(24): val+=2*term/(2*k+1);term*=z*z
    return val,val+2*term/(49*(1-z*z))
LN2=ln(F(2))
@lru_cache(None)
def lg(q):
    q=F(q); assert q>0
    k=q.numerator.bit_length()-q.denominator.bit_length()
    z=q/(F(2)**k)
    if z<1:k-=1;z*=2
    assert 1<=z<2
    lo,hi=ln(z);lo=lo/LN2[1]+k;hi=hi/LN2[0]+k
    scale=1<<72
    return F((lo*scale).__floor__(),scale),F((hi*scale).__ceil__(),scale)
def add(*xs):return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def mul(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub(x,y):return add(x,mul(-1,y))
def ce(P,Q):
    terms=[]
    for p,q in zip(P,Q):
        if p:ck(q>0);terms.append(mul(-p,lg(q)))
    return add(*terms)
def wht(vals):
    z=list(vals);h=1
    while h<len(z):
        for a in range(0,len(z),2*h):
            for j in range(a,a+h): x,y=z[j],z[j+h];z[j],z[j+h]=x+y,x-y
        h*=2
    return [F(x,len(z)) for x in z]
def spec(vals):return [x*x for x in wht(vals)]
def influ(vals):
    n=(len(vals)-1).bit_length()
    return [F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals)) for j in range(n)]
def marginal(P,j):
    out=[F(0)]*(len(P)//2)
    for x,v in enumerate(P):out[(x&((1<<j)-1))|((x>>(j+1))<<j)]+=v
    return out
def child(vals,j,bit):
    return [vals[(x&((1<<j)-1))|((x>>j)<<(j+1))|(bit<<j)] for x in range(len(vals)//2)]
def calib(R,P):
    if P[0]==1:return [F(1)]+[F(0)]*(len(P)-1)
    assert R[0]<1
    return [P[0]]+[(1-P[0])*x/(1-R[0]) for x in R[1:]]
def function(a,b,r):
    amask=(1<<a)-1;N=1<<(a+b+r)
    return [1-2*int((x&amask)==0)+2*int(x==0) for x in range(N)]
def source(a,b):
    return [1-2*int((x&((1<<a)-1))==0) for x in range(1<<(a+b))]
def floor(a,b,r,R):
    s,t,p=F(1,1<<a),F(1,1<<(a+b)),F(1,1<<r);e=2*p*t;mu=1-2*s
    vals=function(a,b,r);P=spec(vals);M=[sum(P[T+(U<<(a+b))] for U in range(1<<r)) for T in range(1<<(a+b))]
    Rp=[(1-e/s)*v+(e/s)*mu*int(T==0)+2*e*t for T,v in enumerate(R)]
    Q=[Rp[x%len(R)]*v/M[x%len(R)] for x,v in enumerate(P)]
    ck(sum(Q)==sum(P)==1);ck(all(q>=0 for q in Q));ck(Rp[0]==M[0])
    return vals,P,Q
def erasure(P,j):return sub(ce(P,P),ce(marginal(P,j),marginal(P,j)))
def one(a,b,r,R,j):
    global POSITIVE,NEGATIVE,RESET_WITNESS
    vals,P,Q=floor(a,b,r,R);g=source(a,b);Pg=spec(g)
    bg,bf=erasure(Pg,j),erasure(P,j)
    ck(bg[0]>=bf[1])
    s,t,p=F(1,1<<a),F(1,1<<(a+b)),F(1,1<<r);e=2*p*t;mu=1-2*s
    qj=4*s*s-4*s*e+2*e*t;k=(2*s-e)**2/qj
    ck(qj>=2*s*s);ck(1-k<=e/s)
    V=marginal(R,j);Qold=marginal(Q,j)
    qstar=(mu+e)**2+k*((1-e/s)*R[1<<j]+2*e*t)
    ck(Qold[0]==qstar);ck(V[0]==mu*mu+R[1<<j]);ck(V[0]-qstar<=8*e)
    loss=sub(mul(-1,lg(qstar)),mul(-1,lg(V[0])))
    vmax=1-mu*mu
    qmax=(mu+e)**2+k*((1-e/s)*vmax+2*e*t)
    ck(qstar*1>=V[0]*qmax);ck(qmax>=F(27,52));ck(1-qmax<=6*e)
    ck(loss[1]<=18*e)
    cp=child(vals,j,0);const=child(vals,j,1);ck(all(x==1 for x in const))
    gp=child(g,j,0);ck(gp==source(a-1,b));Rp=calib(V,spec(gp))
    vv,PP,QQ=floor(a-1,b,r,Rp);ck(vv==cp)
    c,cc=ce(Pg,R),ce(spec(gp),Rp)
    W=add(c,(10*e*(a+b+r),)*2)
    Wp=add(cc,(20*e*(a-1+b+r),)*2)
    local=add(bf,mul(F(1,2),Wp),mul(F(-1,2),lg(qstar)))
    ck(local[1]<=W[0]-e)
    # Signed reset is compared against actual inherited Q, not a TV surrogate.
    oldterm=ce(spec(cp),Qold);newterm=ce(PP,QQ)
    reset=mul(F(1,2),sub(newterm,oldterm))
    if reset[0]>0:
        POSITIVE+=1
        if RESET_WITNESS is None:RESET_WITNESS={'a':a,'b':b,'r':r,'j':j,'R':[str(x) for x in R],'expected_reset_interval':[str(x) for x in reset]}
    if reset[1]<0:NEGATIVE+=1
    ck(sum(Qold)==1);ck(sum(QQ)==1)
    return Rp,Qold[0],bf,reset
def history(a,b,r,R,order):
    global HIST
    rootg=source(a,b);rootc=ce(spec(rootg),R);s=F(1,1<<a);e=F(2,1<<(a+b+r))
    vals,P,Q=floor(a,b,r,R);I=sum(influ(vals));Ig=2*a*s
    C0=rootc[1]/Ig;K=2*C0+10;quota=K*I
    debit=(F(0),F(0));constant=(F(0),F(0));reach=F(1);labels=list(range(a));aa=a;final_terminal=None
    for label in order:
        j=labels.index(label)
        if aa==1:
            vv,PP,QQ=floor(aa,b,r,R);old=marginal(QQ,j)
            cp=child(vv,j,0);ck(child(vv,j,1)==[1]*len(cp))
            m=b+r;u=F(1,1<<m)
            match=[(1-2*u)**2]+[4*u*u]*((1<<m)-1)
            ck(match==spec(cp));ck(sum(match)==1)
            bf=erasure(PP,j);terminal=ce(match,match)
            local=add(bf,mul(F(1,2),terminal),mul(F(-1,2),lg(old[0])))
            parentcost=ce(PP,QQ)
            if local[1]>parentcost[0]:ck(sub(parentcost,local)[1]>=0)
            else:ck(True)
            debit=add(debit,mul(reach,bf));constant=add(constant,mul(-reach/2,lg(old[0])))
            reach/=2;final_terminal=terminal;aa=0;break
        Rn,qstar,bf,reset=one(aa,b,r,R,j)
        # qstar is the untouched complementary full terminal; never replaced by 1.
        debit=add(debit,mul(reach,bf));constant=add(constant,mul(-reach/2,lg(qstar)))
        reach/=2;R=Rn;aa-=1;labels.pop(j)
    if final_terminal is None:
        vv,PP,QQ=floor(aa,b,r,R);final_terminal=ce(PP,QQ)
    total=add(debit,constant,mul(reach,final_terminal))
    Wroot=add(rootc,(10*e*(a+b+r),)*2)
    ck(total[1]<=Wroot[0]);ck(total[1]<=quota)
    # Original source-erasure-plus-terminal envelope, with no restarted child quota.
    ck(quota>=Wroot[1]);HIST+=1
    if R==spec(source(a,b)):ck(total[1]<=18*I)
    return {'order':list(order),'debit':[str(x) for x in debit],'constant_full_CE':[str(x) for x in constant],'total_upper':str(total[1]),'quota':str(quota)}
def main():
    global ROOTS
    pilot='--pilot' in sys.argv;out=[]
    for a in ([2] if pilot else [2,3,4]):
      for b in ([0] if pilot else [0,1]):
       for r in ([1] if pilot else [1,2,3]):
        g=source(a,b);Pg=spec(g);N=len(Pg)
        for name,raw in [('matching',Pg),('uniform',[F(1,N)]*N),('increasing_rational',[F(2*(j+1),N*(N+1)) for j in range(N)])]:
          R=calib(raw,Pg);ROOTS+=1
          vals,P,Q=floor(a,b,r,R);wf=wht(vals)
          ck(sum(P)==1);ck(sum(influ(vals))==sum(i.bit_count()*v for i,v in enumerate(P)))
          # Direct character sums independently reproduce every root Walsh coefficient.
          for z,v in enumerate(wf):ck(v==F(sum(y*(-1 if (x&z).bit_count()%2 else 1) for x,y in enumerate(vals)),len(vals)))
          localrows=[]
          for length in range(a+1):
            for order in permutations(range(a),length):localrows.append(history(a,b,r,R,order))
          out.append({'a':a,'b':b,'r':r,'reference':name,'histories':len(localrows),'last':localrows[-1]})
    # Unused a>=2 hypothesis must fail outside its domain.
    p1=spec(source(1,0));pf=spec(function(1,0,1));b1=erasure(p1,0);be=erasure(pf,0)
    ck(b1==(0,0));ck(be[0]>0)
    result={'status':'PASS','pilot':pilot,'roots':ROOTS,'histories':HIST,'assertions':COUNT,'positive_reset_calls':POSITIVE,'negative_reset_calls':NEGATIVE,'positive_reset_witness':RESET_WITNESS,'runtime_seconds':time.perf_counter()-START,'a1_boundary':'strict erasure comparison fails, as required','rows':out}
    dump('PILOT.json' if pilot else 'VALIDATION.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__': main()
