from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,sys,time
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
START=time.perf_counter(); CHECKS=0
def ck(b):
    global CHECKS
    CHECKS+=1
    if not b: raise AssertionError(CHECKS)
    if time.perf_counter()-START>60: raise TimeoutError('frozen runtime')
def save(name,v): (R/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def ln_interval(x):
    # Scale into [1,2). z in [0,1/3]; omitted positive tail bounded geometrically.
    def unit(y):
        z=(y-1)/(y+1);power=z;lo=F(0)
        for j in range(64):
            lo+=2*power/(2*j+1); power*=z*z
        return lo,lo+2*power/(129*(1-z*z))
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    a,b=unit(x);c,d=unit(F(2))
    return (a+k*c,b+k*d) if k>=0 else (a+k*d,b+k*c)
def log2_interval(x):
    a,b=ln_interval(x);c,d=ln_interval(F(2))
    vals=[a/c,a/d,b/c,b/d]
    return min(vals),max(vals)
def scale(interval,c):
    a,b=interval
    return (a*c,b*c) if c>=0 else (b*c,a*c)
def kl(p,q):
    pieces=[scale(log2_interval(p/q),p),scale(log2_interval((1-p)/(1-q)),1-p)]
    return sum(x[0] for x in pieces),sum(x[1] for x in pieces)
def outward(iv,bits=80):
    d=1<<bits
    return [str(F(iv[0].numerator*d//iv[0].denominator,d)),str(F(-((-iv[1].numerator*d)//iv[1].denominator),d))]
def spectrum(t,labels):
    vals=list(t);N=len(vals);step=1
    while step<N:
        for start in range(0,N,2*step):
            for i in range(start,start+step):
                a,b=vals[i],vals[i+step]; vals[i],vals[i+step]=a+b,a-b
        step*=2
    out={sum(1<<label for j,label in enumerate(labels) if s>>j&1):F(v*v,N*N) for s,v in enumerate(vals) if v}
    ck(sum(out.values())==1)
    return out
def restriction(t,i,b):
    return tuple(v for x,v in enumerate(t) if (x>>i)&1==b)
@lru_cache(None)
def factors(n):
    ans={};d=2
    while d*d<=n:
        while n%d==0:ans[d]=ans.get(d,0)+1;n//=d
        d+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def add(*vectors):
    v=defaultdict(F)
    for a in vectors:
        for p,c in a.items():v[p]+=c
    return {p:c for p,c in v.items() if c}
def mul(v,c):return {p:a*c for p,a in v.items() if a*c}
def entropy_vector(law):
    v=defaultdict(F)
    for p in law:
        if p:
            for q,e in factors(p.numerator).items():v[q]-=p*e
            for q,e in factors(p.denominator).items():v[q]+=p*e
    return {p:c for p,c in v.items() if c}
def serial(v):return {str(p):str(c) for p,c in v.items()}
def audit(m,datafirst):
    n=m+4;labels=tuple(range(n));t=[]
    for x in range(1<<n):
        z=x&((1<<m)-1);a=x>>m&1;b=x>>(m+1)&1;u=x>>(m+2)&1;v=x>>(m+3)&1
        t.append((-1)**(u+v) if z==(1<<m)-1 and a else 1-2*u*v if z==(1<<m)-1 and b else 1)
    root=spectrum(t,labels)
    I=F(sum(t[x]!=t[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)
    tau=F(1,1<<m);ck(I==tau*(F(5*m,8)+2))
    leaves=[];nodes={};terminalI=F(0);M={};J={};L={}
    def walk(tt,ll,path,reach):
        nonlocal terminalI,M,J,L
        d=dict(path);i=None
        if datafirst and m+2 not in d:i=m+2
        else:
            for z in range(m):
                if z not in d:i=z;break
                if not d[z]:break
            else:
                if m not in d:i=m
                elif not d[m] and m+1 not in d and not (datafirst and d[m+2]==0):i=m+1
        if i is None:
            law=spectrum(tt,ll);leaves.append((path,reach,law))
            L=add(L,mul(entropy_vector(law.values()),reach))
            terminalI+=reach*F(sum(tt[x]!=tt[x^(1<<j)] for x in range(len(tt)) for j in range(len(ll))),len(tt))
            return
        ck(i in ll)
        nodes[path]=(reach,i)
        j=ll.index(i);rest=ll[:j]+ll[j+1:]
        ck(any(tt[x]!=tt[x^(1<<j)] for x in range(len(tt))))
        law=spectrum(tt,ll);erased=defaultdict(F)
        for s,p in law.items():erased[s&~(1<<i)]+=p
        ts=[restriction(tt,j,b) for b in (0,1)]
        childlaws=[spectrum(c,rest) for c in ts]
        avg=mul(add(*(entropy_vector(c.values()) for c in childlaws)),F(1,2))
        M=add(M,mul(add(entropy_vector(law.values()),mul(entropy_vector(erased.values()),-1)),reach))
        J=add(J,mul(add(entropy_vector(erased.values()),mul(avg,-1)),reach))
        for b in (0,1):walk(ts[b],rest,path+((i,b),),reach/2)
    walk(tuple(t),labels,(),F(1))
    ck(sum(w for h,w,q in leaves)==1)
    data_mask=(1<<(m+3)) if datafirst else ((1<<(m+2))|(1<<(m+3)))
    marginal=defaultdict(F)
    for s,p in root.items():marginal[s&data_mask]+=p
    joint=defaultdict(F)
    for h,reach,law in leaves:
        ck(all(s&~data_mask==0 for s in law))
        for w,p in law.items():joint[h,w]=reach*p
    for w in set(marginal)|{w for h,w in joint}:
        ck(marginal[w]==sum(p for (h,s),p in joint.items() if s==w))
    # Posterior factors through every prefix; absent rows are never divided.
    for (h,w),atom in joint.items():
        total=marginal[w]; ck(total>0)
        for depth in range(len(h)+1):
            prefix=h[:depth]
            group=sum(p for (hh,ww),p in joint.items() if hh[:depth]==prefix and ww==w)
            ck(group>0 and (group/total)*(atom/group)==atom/total)
    for w,total in marginal.items():
        ck(sum(p/total for (h,s),p in joint.items() if s==w)==1)
    H=entropy_vector(root.values());Hp=entropy_vector(reach for h,reach,law in leaves)
    Hw=entropy_vector(marginal.values());Hjoint=entropy_vector(joint.values())
    B=add(Hjoint,mul(Hw,-1));jW=add(Hw,mul(L,-1))
    Sigma=add(mul(Hp,F(1,2)),M,mul(J,-1))
    ck(H==add(M,J,L));ck(Hjoint==add(Hp,L))
    ck(H==add(L,mul(M,2),mul(B,F(1,2)),mul(jW,F(1,2)),mul(Sigma,-1)))
    if datafirst:
        ck(terminalI==5*tau/8)
        ck(all(len(q)==1 for h,reach,q in leaves)) # characters or constants; retain both
        ck(marginal[1<<(m+3)]==5*tau/8)
        for b,k in ((0,1),(1,2)):
            ls=[(h,w,q) for h,w,q in leaves if h[0]==(m+2,b)]
            ck(len(ls)==m+2+b and sum(w for h,w,q in ls)==F(1,2))
            p=sum(2*reach*q.get(1<<(m+3),F(0)) for h,reach,q in ls)
            q=sum(law.get(1<<(m+3),F(0)) for h,reach,law in ls)/len(ls)
            ck(p==(tau/2 if b==0 else 3*tau/4) and q==F(k,m+2+b))
            correct_reverse=sum(2*reach*law.get(1<<(m+3),F(0))/p for h,reach,law in ls)
            ck(correct_reverse==1)
            # Using the wrong column with true physical atom weights fails normalization.
            ck(p/q!=1)
        ck(Hp=={2:3-3*tau/4})
    else:
        ck(terminalI==5*tau/4)
        ck(marginal[0]==1-11*tau/16 and marginal[1<<(m+2)]==tau/16 and marginal[1<<(m+3)]==tau/16 and marginal[data_mask]==9*tau/16)
    save(('DATA_' if datafirst else 'BASE_')+str(m)+'.json',{'m':m,'data_first':datafirst,'n':n,'I':str(I),'terminal_I':str(terminalI),'removed_I':str(I-terminalI),'terminal_H_bits':str(F(0) if datafirst else tau/2),'W_marginal':{str(k):str(v) for k,v in marginal.items()},'leaves':[{'path':h,'physical_reach':str(reach),'spectrum':{str(k):str(v) for k,v in law.items()}} for h,reach,law in leaves],'posterior_factorization':'PASS','zero_rows_divided':False,'signed_ledger':{k:serial(v) for k,v in [('H_root',H),('H_transcript',Hp),('M',M),('J',J),('L',L),('B',B),('jW',jW),('Sigma',Sigma)]}})
def main():
    pilot='--pilot' in sys.argv
    for m in ([1] if pilot else range(1,7)):
        for d in (False,True):audit(m,d)
    scalars=[]
    for m in ([] if pilot else [10,16,24,40,80]):
        tau=F(1,1<<m);I=tau*(F(5*m,8)+2)
        ivs=[kl(tau/2,F(1,m+2)),kl(3*tau/4,F(2,m+3))]
        iv=tuple((ivs[0][j]+ivs[1][j])/2 for j in (0,1))
        bound=F(1,2*(m+3))
        ck(iv[0]>bound and F(3,4)*(m+3)**2*tau<=F(1,2))
        result={'m':m,'physical_I':str(I),'conditional_KL_bits_interval':outward(iv),'KL_over_I_interval':outward((iv[0]/I,iv[1]/I)),'analytic_lower_bound_bits':str(bound),'truth_table_constructed':False}
        scalars.append(result);save('KL_'+str(m)+'.json',result)
    result={'status':'PASS','pilot':pilot,'actual_tree_cases':2 if pilot else 12,'formula_cases':len(scalars),'assertions':CHECKS,'seconds':time.perf_counter()-START,'arithmetic':'exact Fraction and rational logarithm enclosures','floating_signs':False}
    save('PILOT.json' if pilot else 'RESULT.json',result);print(json.dumps(result))
if __name__=='__main__':main()
