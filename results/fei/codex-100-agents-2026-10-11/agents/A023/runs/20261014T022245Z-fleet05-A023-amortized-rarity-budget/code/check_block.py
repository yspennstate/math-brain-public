"""Frozen 1039-case direct shared-data point-block validation, no source imports."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,time,sys
sys.set_int_max_str_digits(0)
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0;SIGNS={}
def ck(v):
    global CHECKS
    assert v
    CHECKS+=1
    if time.perf_counter()-START>60: raise RuntimeError('Frozen pilot cap reached')
def save(name,obj):
    (RUN/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def fac(n):
    out=[];p=2
    while p*p<=n:
        k=0
        while n%p==0:n//=p;k+=1
        if k:out.append((p,k))
        p+=1
    if n>1:out.append((n,1))
    return out
def lg(v,x,c):
    if not x or not c:return
    x=Q(x)
    for n,sg in [(x.numerator,1),(x.denominator,-1)]:
        for p,k in fac(n):
            v[p]=v.get(p,Q(0))+sg*k*c
            if not v[p]:del v[p]
def add(*parts):
    out={}
    for rate,v in parts:
        for p,c in v.items():
            out[p]=out.get(p,Q(0))+rate*c
            if not out[p]:del out[p]
    return out
def rational(q):return {2:Q(q)} if q else {}
def logs(x,c=1):
    out={};lg(out,x,Q(c));return out
@lru_cache(None)
def fw(v):
    a=list(v);span=1
    while span<len(a):
        for start in range(0,len(a),span*2):
            lower=a[start:start+span];upper=a[start+span:start+2*span]
            a[start:start+span]=[x+y for x,y in zip(lower,upper)]
            a[start+span:start+2*span]=[x-y for x,y in zip(lower,upper)]
        span*=2
    return a
@lru_cache(None)
def inf(v):
    N=len(v);n=N.bit_length()-1
    return Q(2*sum(v[x]!=v[x|(1<<i)] for i in range(n) for x in range(N) if not x&(1<<i)),N)
@lru_cache(None)
def ent(v):
    N=len(v);o={}
    for a in fw(v):
        if a:lg(o,Q(a*a,N*N),-Q(a*a,N*N))
    return o
def ln_interval(x,T):
    z=(x-1)/(x+1);power=z;total=Q(0)
    for j in range(T):total+=power/(2*j+1);power*=z*z
    return 2*total,2*total+2*power/(2*T+1)/(1-z*z)
@lru_cache(None)
def log_interval(p,T):
    k=p.bit_length()-1;l,h=ln_interval(Q(p,1<<k),T);a,b=ln_interval(Q(2),T)
    return k+l/b,k+h/a
def sign(v):
    key=tuple(sorted(v.items()))
    if key in SIGNS:return SIGNS[key]['sign']
    if not v:SIGNS[key]={'vector':{},'sign':0,'exact_zero':True};return 0
    for T in [24,48]:
        lo=hi=Q(0)
        for p,c in v.items():
            a,b=log_interval(p,T);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
        # Round outward to dyadic endpoints; the rational series before rounding is exact.
        scale=1<<100;lo=Q((lo*scale).__floor__(),scale);hi=Q((hi*scale).__ceil__(),scale)
        if lo>0 or hi<0:
            result=1 if lo>0 else -1
            SIGNS[key]={'vector':{str(p):str(c) for p,c in v.items()},'sign':result,'lower':str(lo),'upper':str(hi),'terms':T,'outward_dyadic_bits':100}
            return result
    raise AssertionError('Exact sign unresolved')
def le(v):ck(sign(v)<=0)
@lru_cache(None)
def node(v):
    N=len(v);w=fw(v);ck(sum(a*a for a in w)==N*N)
    B={};J={};mu=Q(0)
    for i in range(0,N,2):
        a,b=Q(w[i]**2,N*N),Q(w[i+1]**2,N*N)
        lg(B,a+b,a+b);lg(B,a,-a);lg(B,b,-b)
        mm=min(a,b);mu+=mm;lg(J,a+b,mm);lg(J,mm,-mm)
    d=Q(sum(a*a for a in w[1::2]),N*N)
    g,h=v[::2],v[1::2]
    face=inf(tuple(a*b for a,b in zip(g,h)))/2
    ck(inf(v)==d+(inf(g)+inf(h))/2);ck(mu<=d)
    return d,B,J,mu,face
def point(G,H,s):
    # Fresh low control bits; active all-one point; high data bits shared.
    N=1<<s
    return tuple(H[y] if x==N-1 else G[y] for y in range(len(G)) for x in range(N))
def bent(m):
    b=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2)) for x in range(1<<m))
    h=tuple(-v if x==0 else v for x,v in enumerate(b))
    return b+tuple(-v for v in b),h+tuple(-v for v in h)
def vector(v):return {str(p):str(c) for p,c in v.items()}
def run_case(G,H,s,label):
    alpha=Q(1,1<<s);gamma=Q(sum(g!=h for g,h in zip(G,H)),len(G));eta=Q(sum(g==-1 for g in G),len(G))
    ig,ih=inf(G),inf(H);prod=tuple(g*h for g,h in zip(G,H));ip=inf(prod)
    IS=2*s*alpha*gamma;IT=(1-alpha)*ig+alpha*ih;reserve=2*alpha*(1-alpha)*ip
    f=point(G,H,s);ck(inf(f)==IS+IT);ck(reserve<=2*IT)
    # Check reserve ownership at each actual physical data coordinate.
    nd=len(G).bit_length()-1
    for i in range(nd):
        gi=Q(sum(G[x]!=G[x^(1<<i)] for x in range(len(G))),len(G))
        hi=Q(sum(H[x]!=H[x^(1<<i)] for x in range(len(H))),len(H))
        ki=Q(sum(prod[x]!=prod[x^(1<<i)] for x in range(len(prod))),len(prod))
        ck(ki<=gi+hi)
    EB={};JT={};mudebit=Q(0);dfull=Q(0);fullface=Q(0);badface=Q(0);v=f
    for j in range(s,0,-1):
        l=j-1;rho=Q(1,1<<l);reach=Q(1,1<<(s-j));d,B,J,mu,face=node(v)
        ck(d==rho*gamma);ck(reach*d==2*alpha*gamma)
        ck(face==rho*ip/2+(j-1)*rho*gamma)
        ck(v[::2]==point(G,G,j-1))
        # Independent source A021 upper-price review at actual nodes.
        if gamma:
            C=Q(81,56)
            L=add((1,rational(C)),(1,logs(8*eta/gamma+4)))
            chosen=L if sign(add((1,L),(-1,rational(4))))>=0 else rational(4)
            le(add((1,B),(-d,chosen),(-d,rational(Q(16,9)))))
            # The simpler unseparated packet inequality drives the new proof.
            upper=add((1,rational(2*(1-rho)*d+rho*rho*gamma*C)),(rho*rho*gamma,logs(1/(rho*rho*gamma))))
            le(add((1,B),(-1,upper)))
        else:ck(not B and not J and d==0)
        le(add((1,J),(-1,B)))
        EB=add((1,EB),(reach,B));JT=add((1,JT),(reach,J));mudebit+=reach*mu;dfull+=reach*d;fullface+=reach*face
        if sign(add((1,B),(-4,rational(d))))>0:badface+=reach*face
        v=v[1::2]
    ck(v==H);ck(dfull==IS);ck(mudebit<=IS)
    ck(fullface==alpha*(s*ip+gamma*s*(s-1)))
    HT=add((1-alpha,ent(G)),(alpha,ent(H)));over=add((1,ent(f)),(-1,HT))
    le(add((1,over),(-1,EB),(-2*Q(81,56),rational(IS))))
    le(add((1,over),(-1,rational(Q(11,2)*IS+reserve))))
    le(add((1,JT),(-1,rational(Q(5,2)*IS+reserve))))
    # Exact closed form of cumulative elementary bound, c replaced outward.
    if gamma:
        budget=add((1,rational(2*(1-2*alpha)*IS+4*Q(81,56)*alpha*gamma*(1-alpha))),
            (4*alpha*gamma*(1-alpha),logs(1/gamma)))
        le(add((1,EB),(-1,budget)))
        ck(gamma<=1)
    if label.startswith('bent'):
        ck(ig>=1+nd//2-Q(0)) # nd=m+1; floor matches m/2
        ck(ih>=1+Q(nd-1,2)-2*(nd-1)*gamma)
        le(add((1,ent(G)),(-2,rational(ig))));le(add((1,ent(H)),(-2,rational(ih))))
        le(add((1,ent(f)),(-Q(11,2),rational(inf(f)))))
    return {'label':label,'s':s,'gamma':str(gamma),'inactive_minority':str(eta),
        'selector_I':str(IS),'terminal_I':str(IT),'boundary_reserve':str(reserve),
        'terminal_H':vector(HT),'prefix_B':vector(EB),'prefix_entropy_increment':vector(over),
        'J_tree':vector(JT),'minority_mass_sum':str(mudebit),
        'unfiltered_face':str(fullface),'bad_face_4':str(badface)}
def main():
    rows=[];tables=list(itertools.product([-1,1],repeat=4))
    instant=(RUN/'out/rows.jsonl').open('w',encoding='utf-8')
    def record(row):
        rows.append(row);instant.write(json.dumps(row)+'\n');instant.flush()
    for a,G in enumerate(tables):
        for b,H in enumerate(tables):
            for s in range(1,5):record(run_case(G,H,s,f'pair-{a}-{b}'))
        save('results.json',rows)
    for m in [4,6,8]:
        G,H=bent(m)
        for s in range(1,6):record(run_case(G,H,s,f'bent-{m}'))
        save('results.json',rows)
    const=[];C=Q(81,56)
    for s in range(1,6):
        a=Q(1,1<<s);b=2*(1-2*a)+2*C*(1-a)/s;A=b+2*C
        ck(b<Q(5,2));ck(A<Q(11,2));const.append({'s':s,'B_rate_upper':str(b),'entropy_rate_upper':str(A)})
    ck(2+Q(12,5)*C<Q(11,2));ck(2+C/3<Q(5,2));ck(Q(5,2)+3*C<7)
    save('constant_certificates.json',{'finite':const,'entropy_s_ge_5_upper':str(2+Q(12,5)*C),
        'B_s_ge_6_upper':str(2+C/3),'full_KL_rate_upper':str(Q(5,2)+3*C),
        'c_upper':'81/56','proof':'ln2>56/81 by two positive atanh terms'})
    save('sign_certificates.json',list(SIGNS.values()))
    out={'status':'PASS','cases':len(rows),'checks':CHECKS,'sign_certificates':len(SIGNS),
        'elapsed_seconds':time.perf_counter()-START,'max_dimension':14,
        'A021_review_scope':'Upper point-switch price only; no blanket claim acceptance',
        'new_scope':'Whole point block actual entropy and retained KL with once-owned terminal reserve; not localized odd-face payment'}
    save('validation.json',out);print(json.dumps(out))
    instant.close()
if __name__=='__main__':main()
