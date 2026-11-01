from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib, json, sys, time

R = Path(__file__).resolve().parents[1]
checks = 0
def ck(ok):
    global checks
    checks += 1
    if not ok: raise AssertionError(checks)
def add(*forms):
    out = {}
    for form in forms:
        for p, c in form.items(): out[p] = out.get(p, Q(0)) + c
    return {p:c for p,c in out.items() if c}
def mul(form, v): return {p:c*v for p,c in form.items() if c*v}
def sub(a,b): return add(a,mul(b,-1))
def constant(v): return {2:Q(v)} if v else {}
def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def logform(x):
    x=Q(x)
    return sub(factors(x.numerator),factors(x.denominator))
def entropy(masses): return add(*(mul(logform(x),-x) for x in masses if x))
def L(x,y):
    return sub(entropy([x*x,y*y]),mul(entropy([(x+y)**2,(x-y)**2]),Q(1,2)))
def ln_interval(z):
    # Positive atanh series, 48 terms; exact tail upper bound.
    n=48
    low=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))
    return low,low+2*z**(2*n+1)/(Q(2*n+1)*(1-z*z))
LN2=ln_interval(Q(1,3))
@lru_cache(None)
def log_interval(p):
    if p==2:return Q(1),Q(1)
    k=p.bit_length()-1; y=Q(p,2**k)
    a,b=ln_interval((y-1)/(y+1)); c,d=LN2
    return Q(k)+a/d,Q(k)+b/c
def interval(f):
    lo=hi=Q(0)
    for p,c in f.items():
        a,b=log_interval(p)
        if c<0:a,b=b,a
        lo+=c*a; hi+=c*b
    return lo,hi
def nonnegative(f):
    if not f:return True
    lo,hi=interval(f)
    if lo>=0:return True
    if hi<0:return False
    raise ArithmeticError('Unresolved interval; no branch chosen')
def restrict(t,i,b):
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
@lru_cache(None)
def coefficients(t):
    # DIFFERENT REPRESENTATION: multilinear polynomial in bits b=(1-z)/2.
    # Finite differences give c_T; a_S=(-1)^|S| sum_{T>=S} c_T/2^|T|.
    c=list(t); n=len(t).bit_length()-1
    for i in range(n):
        for s in range(len(t)):
            if s>>i&1:c[s]-=c[s^(1<<i)]
    a=[]
    for s in range(len(t)):
        v=sum((Q(c[u],2**u.bit_count()) for u in range(len(t)) if u&s==s),Q(0))
        a.append(-v if s.bit_count()%2 else v)
    # Independent inverse evaluation checks polynomial conversion.
    for x,v in enumerate(t):
        ck(sum((a[s]*(-1 if (s&x).bit_count()%2 else 1) for s in range(len(t))),Q(0))==v)
    ck(sum(v*v for v in a)==sum(Q(v*v,len(t)) for v in t))
    return tuple(a)
@lru_cache(None)
def data(t):
    a=coefficients(t);n=len(t).bit_length()-1
    ds=tuple(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
    for i,d in enumerate(ds):ck(d==sum(v*v for s,v in enumerate(a) if s>>i&1))
    return entropy(v*v for v in a),sum(ds,Q(0)),ds,a
def compose(h,gs):
    ns=[len(g).bit_length()-1 for g in gs]; out=[]
    for x in range(1<<sum(ns)):
        z=offset=0
        for j,(g,n) in enumerate(zip(gs,ns)):
            if g[(x>>offset)&((1<<n)-1)]<0:z|=1<<j
            offset+=n
        out.append(h[z])
    return tuple(out)
def pivots(h,gs):
    ps=[Q(g.count(-1),len(g)) for g in gs]; out=[]
    for j in range(len(gs)):
        q=Q(0)
        for z in range(1<<len(gs)):
            if z>>j&1:continue
            p=Q(1)
            for k in range(len(gs)):
                if k!=j:p*=ps[k] if z>>k&1 else 1-ps[k]
            if h[z]!=h[z|1<<j]:q+=p
        out.append(q)
    return tuple(out)
def account(h,gs):
    t=compose(h,gs);qs=pivots(h,gs)
    H,I,_,_=data(t)
    ck(I==sum(q*data(g)[1] for g,q in zip(gs,qs)))
    return t,qs,sub(H,add(*(mul(data(g)[0],q) for g,q in zip(gs,qs))))
@lru_cache(None)
def hull(t,K):
    H,I,ds,_=data(t); base=sub(H,constant(K*I))
    best=base if nonnegative(base) else {}
    for i in range(len(ds)):
        candidate=mul(add(*(hull(restrict(t,i,b),K) for b in (0,1))),Q(1,2))
        if nonnegative(sub(candidate,best)):best=candidate
    return best
def outside(h,gs,j):
    others=list(gs);others[j]=(1,)
    plus=compose(h,others);others[j]=(-1,);minus=compose(h,others)
    return tuple(Q(a+b,2) for a,b in zip(plus,minus)),tuple(Q(a-b,2) for a,b in zip(plus,minus))
def bank(h,gs,K):
    t,qs,C=account(h,gs)
    return add(C,constant(3*data(t)[1]),*(mul(hull(g,K),q) for g,q in zip(gs,qs)))
def row(h,gs,j,i):
    t,qs,C=account(h,gs);pi=sum(len(g).bit_length()-1 for g in gs[:j])+i
    kids=[]
    for b in (0,1):
        gg=list(gs);gg[j]=restrict(gs[j],i,b);gg=tuple(gg)
        tt,qq,cc=account(h,gg);ck(tt==restrict(t,pi,b));kids.append((gg,tt,qq,cc))
    for k,q in enumerate(qs):ck(sum(kid[2][k] for kid in kids)/2==q)
    H,I,ds,a=data(gs[j]);mu=a[0];tau=a[1<<i];d=ds[i];df=data(t)[2][pi]
    ck(abs(mu)+abs(tau)<=1);ck(abs(tau)<=d);ck(df==qs[j]*d)
    A,D=outside(h,gs,j);aa,dd=coefficients(A),coefficients(D)
    ck(sum(v*v for v in dd)==qs[j])
    primitive=L(mu,tau)
    special=add(*(L(x+mu*y,tau*y) for x,y in zip(aa,dd)))
    drift=sub(mul(add(*(kid[3] for kid in kids)),Q(1,2)),C)
    ck(drift==sub(mul(primitive,qs[j]),special))
    ck(nonnegative(special));ck(nonnegative(primitive))
    # Independent actual entropy decrement checks the whole row sum.
    total=add(*(L(a[s],a[s|1<<i]) for s in range(len(a)) if not s>>i&1))
    ck(total==sub(H,mul(add(*(data(restrict(gs[j],i,b))[0] for b in (0,1))),Q(1,2))))
    # Certified 2/ln2 bound using upper enclosure of L and lower ln2.
    lo,hi=interval(primitive);ck(hi*LN2[1]<=2*d or primitive=={})
    ck(nonnegative(sub(constant(3*df),drift)))
    ck(data(t)[1]-sum(data(k[1])[1] for k in kids)/2==df)
    for K in (Q(0),Q(5,2),Q(4)):
        U=bank(h,gs,K); child=[bank(h,k[0],K) for k in kids]
        slack=sub(U,mul(add(*child),Q(1,2)));ck(nonnegative(slack));ck(nonnegative(U))
        for V,k in zip(child,kids):
            ck(nonnegative(V));ck(nonnegative(sub(V,sub(data(k[1])[0],constant(K*data(k[1])[1])))))
        outgoing=[add(V,slack) for V in child]
        ck(mul(add(*outgoing),Q(1,2))==U)
    return {'j':j,'i':i,'influence':str(df),'drift':{str(p):str(c) for p,c in drift.items()},'primitive':{str(p):str(c) for p,c in primitive.items()}}
def table(n,mask):return tuple(-1 if mask>>x&1 else 1 for x in range(1<<n))
def save(name,obj):
    path=R/'out'/name;tmp=path.with_suffix('.tmp')
    tmp.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');tmp.replace(path)
def main():
    mode=sys.argv[1];start=time.monotonic()
    if mode=='freeze':
        save('FROZEN_SPEC.json',{'helper_version':'A074-mobius-whole-row-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'Every two-input Boolean gate, every two-bit first core and one-bit second core; separately declared 4-bit primitive and 7-bit positive-drift witness','domain':{'outer_masks':[0,15],'first_core_masks':[0,15],'second_core_masks':[0,3]},'case_count':1024,'query_rows':3072,'symmetry':'none','arithmetic':'Fraction and exact prime-log identities; positive atanh 48-term rational interval with proved tail','memory_estimate_mb':100,'max_runtime_seconds':{'pilot':55,'main':240,'witness':55},'automatic_dimension_escalation':False,'pilot_domain':'outer masks0..3,first masks0..3,second masks0..3:64 circuits/192 rows'})
        print('frozen');return
    spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
    ck(spec['helper_sha256']==hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    rows=[];circuits=0;cap=240 if mode=='main' else 55
    if mode in ('pilot','main'):
        count=4 if mode=='pilot' else 16
        for hm in range(count):
            chunk=[]
            for gm in range(count):
                for km in range(4):
                    if time.monotonic()-start>cap:raise TimeoutError('frozen cap')
                    h=table(2,hm);gs=(table(2,gm),table(1,km));circuits+=1
                    for j,i in ((0,0),(0,1),(1,0)):
                        item=row(h,gs,j,i);item['circuit']=[hm,gm,km];chunk.append(item)
            save(mode+'_chunk_'+str(hm)+'.json',chunk);rows.extend(chunk)
        ck(len(rows)==(192 if mode=='pilot' else 3072))
    elif mode=='witness':
        g=tuple(-1 if x>=8 and x-8<3 else 1 for x in range(16))
        _,_,ds,a=data(g);ck(a[0]==Q(5,8));ck(a[8]==Q(3,8));ck(ds[3]==Q(3,8))
        delta=sub(L(a[0],a[8]),constant(2*ds[3]))
        ck(delta=={2:Q(37,16),3:Q(-9,32),5:Q(-25,32)});ck(2**74>3**9*5**25);ck(nonnegative(delta))
        save('PRIMITIVE.json',{'truth_table':list(g),'query':3,'mu':'5/8','tau':'3/8','influence':'3/8','positive_gap':{str(p):str(c) for p,c in delta.items()},'integer_sign':'2^74>3^9*5^25'})
        h=tuple(1 if z==0 else -1 for z in range(8));gs=tuple(tuple(-1 if x==0 else 1 for x in range(1<<n)) for n in (3,2,2))
        for j,n in enumerate((3,2,2)):
            for i in range(n):rows.append(row(h,gs,j,i))
        ck(nonnegative({int(p):Q(c) for p,c in rows[0]['drift'].items()}))
        save('WITNESS_ROWS.json',rows)
    else:raise ValueError(mode)
    result={'status':'PASS','mode':mode,'circuits':circuits,'query_rows':len(rows),'bank_rows':3*len(rows),'predicates':checks,'elapsed_seconds':time.monotonic()-start,'implementation':'finite-difference multilinear polynomial then centered expansion; no producer import or execution','sign_policy':'exact symbolic equality; directed rational strict signs; unresolved interval aborts'}
    save(mode.upper()+'.json',result);print(json.dumps(result))
if __name__=='__main__':main()
