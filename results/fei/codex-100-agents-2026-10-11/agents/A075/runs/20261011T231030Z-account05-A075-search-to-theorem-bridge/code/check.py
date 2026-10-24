from fractions import Fraction as Q
from pathlib import Path
import json, time, hashlib
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
assertions=0
def check(x):
    global assertions
    assert x
    assertions+=1
def factors(n):
    ans={}; d=2
    while d*d<=n:
        while n%d==0: ans[d]=ans.get(d,0)+1; n//=d
        d+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans
def add(a,b,c=Q(1)):
    r=a.copy()
    for p,v in b.items():
        r[p]=r.get(p,Q(0))+c*v
        if not r[p]: del r[p]
    return r
def scale(a,c): return {p:v*c for p,v in a.items() if v*c}
def logform(x):
    r={p:Q(v) for p,v in factors(x.numerator).items()}
    return add(r,{p:Q(v) for p,v in factors(x.denominator).items()},-1)
def entropy(ps):
    r={}
    for x in ps:
        if x: r=add(r,logform(x),-x)
    return r
def phi(a,b): return add(entropy([a,b]),entropy([a+b]),-1)
def walsh(t):
    a=list(t); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h): a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return [Q(x,len(a)) for x in a]
def metrics(t):
    a=walsh(t); p=[x*x for x in a]; n=(len(t)-1).bit_length()
    infl=[sum((p[s] for s in range(len(p)) if s>>i&1),Q(0)) for i in range(n)]
    B=[]
    for i in range(n):
        v={}
        for s in range(len(p)):
            if not(s>>i&1): v=add(v,phi(p[s],p[s|(1<<i)]))
        B.append(v)
    return a,p,entropy(p),sum(infl,Q(0)),infl,B
def table(n,mask): return [1 if mask>>s&1 else -1 for s in range(1<<n)]
def compose(f,g):
    m=(len(f)-1).bit_length(); n=(len(g)-1).bit_length()
    out=[]
    for x in range(1<<(m*n)):
        y=sum((g[(x>>(j*n))&((1<<n)-1)]==1)<<j for j in range(m))
        out.append(f[y])
    return out
cases=0; positive_corrections=0
for m in [1,2]:
    for fm in range(1<<(1<<m)):
        f=table(m,fm); af,pf,Hf,If,ii,Bf=metrics(f)
        for n in [1,2,3]:
            for gm in range(1<<(1<<n)):
                g=table(n,gm)
                if sum(g): continue
                ag,pg,Hg,Ig,ig,Bg=metrics(g)
                F=compose(f,g); a,p,H,I,inf,B=metrics(F)
                check(H==add(Hf,Hg,If)); check(I==If*Ig)
                for j in range(m):
                    for i in range(n):
                        corr={}
                        for s in range(1<<m):
                            if not(s>>j&1): corr=add(corr,phi(pf[s],pf[s|(1<<j)]*pg[1<<i]))
                        check(B[j*n+i]==add(scale(Bg[i],ii[j]),corr))
                        check(inf[j*n+i]==ii[j]*ig[i])
                        if corr: positive_corrections+=1
                        check(bool(corr)==bool(pg[1<<i] and Bf[j]))
                cases+=1
check(cases==1560)
def maj(t): return 1 if sum(t)>0 else -1
def recur(t):
    if len(t)==1: return t[0]
    k=len(t)//3
    return maj([recur(t[j*k:(j+1)*k]) for j in range(3)])
records=[]
for d in [1,2]:
    n=3**d
    t=[recur([1 if x>>j&1 else -1 for j in range(n)]) for x in range(1<<n)]
    a,p,H,I,ii,B=metrics(t)
    check(I==Q(3,2)**d); check(H=={2:4*(Q(3,2)**d-1)}); check(all(not b for b in B))
    records.append({'depth':d,'dimension':n,'I':str(I),'H_bits':str(H.get(2,0)),'B':0})
    if d==2:
        fixed={2:-1,4:1,5:-1,6:-1,7:-1,8:-1}; free=[0,1,3]
        rt=[]
        for y in range(8):
            vals=[fixed.get(j,0) for j in range(9)]
            for k,j in enumerate(free): vals[j]=1 if y>>k&1 else -1
            rt.append(recur(vals))
        check(rt==[-1]*7+[1]); ar,pr,Hr,Ir,ir,Br=metrics(rt)
        Kstar={2:Q(4),5:Q(5,2),3:Q(-9,2)}
        check(all(scale(b,1/i)==Kstar for b,i in zip(Br,ir)))
        check(pr==[Q(9,16)]+[Q(1,16)]*7)
def ln_interval(x,N=48):
    z=(x-1)/(x+1); check(0<=z<=Q(1,3))
    lo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(N)),Q(0))
    tail=2*z**(2*N+1)/(Q(2*N+1)*(1-z*z))
    return lo,lo+tail
ln2=ln_interval(Q(2))
def log_interval(p):
    k=p.bit_length()-1; a,b=ln_interval(Q(p,1<<k))
    return Q(k)+a/ln2[1],Q(k)+b/ln2[0]
def enclose(expr):
    lo=hi=Q(0)
    for p,c in expr.items():
        a,b=log_interval(p)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
kl,ku=enclose(Kstar)
check(Q(267,100)<kl<ku<Q(107,40))
# c=2/ln2 is enclosed outward; recursion at d=10 has ratio >1+c.
c_lo,c_hi=2/ln2[1],2/ln2[0]
check(4*(1-Q(2,3)**10)>1+c_hi)
out={'helper_version':'A075-composition-v1','composition_cases':cases,'exact_assertions':assertions,'positive_singleton_collision_rows':positive_corrections,'recursive_checks':records,'restriction':{'fixed_coordinates_zero_based':{str(k):v for k,v in fixed.items()},'free_coordinates_zero_based':free,'truth_table':rt,'spectral_probabilities':[str(x) for x in pr],'I':str(Ir),'B_i_over_Inf_i':'4+(5/2)log2(5)-(9/2)log2(3)'},'Kstar_interval':[str(kl),str(ku)],'Kstar_rational_bracket':['267/100','107/40'],'analytic_depth10_potential_K1_positive':True,'runtime_seconds':time.perf_counter()-start,'entropy_verdicts':'Exact prime-log identities and rational outward intervals; no floating sign verdicts','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['Kstar_interval','restriction']},indent=2))
