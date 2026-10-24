from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import itertools,json,time,sys,math
import exact as e
R=Path(__file__).resolve().parents[1]; start=time.perf_counter()
@lru_cache(2048)
def coeff(t):
    a=list(t); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
        step*=2
    return tuple(Q(x,len(t)) for x in a)
def squares(t):return tuple(x*x for x in coeff(t))
def phi(a,b):return e.add((1,e.entropy((a,b))),(-1,e.entropy((a+b,))))
def eta(x):return e.entropy((x,))
def pos(d):e.nonnegative(d)
def const(x):return {2:Q(x)} if x else {}
# Keep the original enclosure function; caching it changes no arithmetic.
original_interval=e.interval
def interval_cached(d):return iv2(tuple(sorted(d.items())))
@lru_cache(4096)
def iv2(items):return original_interval(dict(items))
e.interval=interval_cached
def cut(t,i,b):return tuple(t[(x&((1<<i)-1))+((x>>i)<<(i+1))+(b<<i)] for x in range(len(t)//2))
def local(t,i):
    P=squares(t); paired=tuple(P[s]+P[s|(1<<i)] for s in range(len(P)) if not s>>i&1)
    B=e.add((1,e.entropy(P)),(-1,e.entropy(paired)))
    D=e.add((1,e.entropy(P)),(-Q(1,2),e.entropy(squares(cut(t,i,0)))),(-Q(1,2),e.entropy(squares(cut(t,i,1)))))
    I=Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
    J=e.add((1,D),(-1,B)); pos(e.add((1,const(3*I)),(-1,J))) # 2/ln2 < 3
    e.check(I,sum(v for s,v in enumerate(P) if s>>i&1));return B,D,I
def compose(labels,cores):
    widths=[(len(u)-1).bit_length() for u in cores]; nc=(len(labels)-1).bit_length();out=[]
    for x in range(1<<(nc+sum(widths))):
        c=labels[x&((1<<nc)-1)]; off=nc; values=[]
        for u,w in zip(cores,widths):values.append(u[(x>>off)&((1<<w)-1)]);off+=w
        out.append(values[c])
    return tuple(out)
def reserve(labels,cores):
    return e.add(*[(1-(sum(u,Q(0))/len(u))**2,eta(Q(labels.count(j),len(labels)))) for j,u in enumerate(cores)])
def activation(labels,us,glabels,gs):
    # Prefix labels 0=fallback, 1=u1, 2=u2. All G labels share actual physical blocks.
    nz=(len(labels)-1).bit_length(); ng=(len(glabels)-1).bit_length();fine=[]
    for x in range(1<<(1+nz+ng)):
        y=x&1; j=labels[(x>>1)&((1<<nz)-1)]; l=glabels[(x>>(1+nz))&((1<<ng)-1)]
        fine.append(j-1 if y and j else len(us)+l)
    cores=us+gs; F=compose(tuple(fine),cores); G=compose(glabels,gs)
    means=[sum(u,Q(0))/len(u) for u in us]; n=sum(G,Q(0))/len(G); V=1-n*n
    ps=[Q(labels.count(j+1),len(labels)) for j in range(len(us))];t=sum(ps)
    h=tuple(Q(0) if j==0 else means[j-1]-n for j in labels);h0=sum(h,Q(0))/len(h)
    vh=sum(v*v for v in h)/len(h)-h0*h0
    Z=sum(Q(glabels.count(l),len(glabels))*(1-(sum(u,Q(0))/len(u))**2) for l,u in enumerate(gs))
    k=e.add((1,eta(1-t/2)),(-Q(1,2),eta(1-t)))
    kap=e.add((1,const(sum(p*(1-m*m)/2 for p,m in zip(ps,means)))),(Z,k))
    actual=e.add((1,reserve(tuple(fine),cores)),(-Q(1,2),reserve(tuple(fine[::2]),cores)),(-Q(1,2),reserve(tuple(fine[1::2]),cores)))
    e.check(actual,kap);pos(kap)
    B,D,I=local(F,0);e.check(I,sum(p*(1-m*n)/2 for p,m in zip(ps,means)))
    formula=e.add((1,const(vh/2+V*t*(1-t)/2)),(1,phi((n+h0/2)**2,(h0/2)**2)),(V,phi((1-t/2)**2,(t/2)**2)),(-Z,k))
    e.check(e.add((1,B),(-1,kap)),formula)
    pos(e.add((1,const(8*I)),(-1,B),(1,kap)))
    pos(e.add((1,const(11*I)),(-1,D),(1,kap))) # stated real price <11, checked weaker finite rational bound
def source(us,widths):
    nc=sum(widths); labels=[]
    for z in range(1<<nc):
        off=0;selected=len(us)
        for j,w in enumerate(widths):
            if (z>>off)&((1<<w)-1)==(1<<w)-1:selected=j;break
            off+=w
        labels.append(selected)
    cores=us+((1,),);F=compose(tuple(labels),cores)
    for j in range(len(us)):
        i=sum(widths[:j]);q=Q(1,1<<widths[j]); np=sum(widths[:j]);ear=[]
        for z in range(1<<np):
            off=0;v=0
            for h,w in enumerate(widths[:j]):
                if (z>>off)&((1<<w)-1)==(1<<w)-1:v=h+1;break
                off+=w
            ear.append(v)
        m=sum(us[j],Q(0))/len(us[j]); means=[sum(u,Q(0))/len(u) for u in us[:j]]
        Et=tuple(1 if v==0 else 0 for v in ear); Kt=tuple(Q(0) if v==0 else means[v-1] for v in ear);guard=sum(Et,Q(0))/len(Et)
        # Build actual suffix once, including its fine selector law.
        sw=widths[j+1:]; sl=[]
        for z in range(1<<sum(sw)):
            off=0;v=len(sw)
            for h,w in enumerate(sw):
                if (z>>off)&((1<<w)-1)==(1<<w)-1:v=h;break
                off+=w
            sl.append(v)
        sc=us[j+1:]+((1,),);G=compose(tuple(sl),sc);n=sum(G,Q(0))/len(G);V=1-n*n
        Z=sum(Q(sl.count(h),len(sl))*(1-(sum(u,Q(0))/len(u))**2) for h,u in enumerate(sc))
        k=e.add((1,eta(1-q)),(-Q(1,2),eta(1-2*q)))
        kap=e.add((1,const(guard*q*(1-m*m))),(guard*Z,k))
        children=[tuple(labels[(x&((1<<i)-1))+((x>>i)<<(i+1))+(b<<i)] for x in range(len(labels)//2)) for b in [0,1]]
        actual=e.add((1,reserve(tuple(labels),cores)),*[(-Q(1,2),reserve(c,cores)) for c in children]);e.check(actual,kap)
        B,D,I=local(F,i);e.check(I,guard*q*(1-m*n))
        delta=m-n; M=n+q*delta;EC=coeff(Et);KC=coeff(Kt)
        S=e.add(*[(1,phi((a+M*b)**2,q*q*delta*delta*b*b)) for a,b in zip(KC,EC)])
        rhs=e.add((1,const(guard*(q-2*q*q)*(V+delta*delta))),(guard*V,phi((1-q)**2,q*q)),(-guard*Z,k),(1,S))
        e.check(e.add((1,B),(-1,kap)),rhs);pos(e.add((1,const(17*I)),(-1,D),(1,kap)))
        if guard:
            e.check(sum(b*b for b in EC),guard)
            ps=[Q(1,1<<w) for w in widths[:j]];t=[e.prod(1-p for p in ps)]+[e.prod(1-p for p in ps[h+1:]) for h in range(j)]
            for mask,(a,b) in enumerate(zip(KC,EC)):
                if not b:continue
                J=0;off=0
                for h,w in enumerate(widths[:j]):
                    if mask>>off&((1<<w)-1):J=h+1
                    off+=w
                if J:e.check(a/b,-means[J-1]/t[J]+sum(means[h]*ps[h]/t[h] for h in range(J,j)))
                else:e.check(a/b,sum(Kt,Q(0))/len(Kt)/guard)
    return len(us)
def main():
    kind=sys.argv[1];pilot='--pilot' in sys.argv;lo=int(sys.argv[2]);hi=int(sys.argv[3]);cases=0;queries=0
    maps=list(itertools.product(range(3),repeat=4));pool=tuple(e.tab(mask,1) for mask in range(4))
    if kind=='source':
        for idx,us in enumerate(itertools.product(pool,repeat=3)):
            if lo<=idx<hi:
                for widths in [(1,1,1),(2,1,1),(1,2,1)]:queries+=source(us,widths);cases+=1
        # Genuine biased/partially exposed cores, no artificial mean surrogate.
        if not pilot:
            and2=(-1,-1,-1,1)
            for j in range(3):
                for b in [0,1]:
                    us=list((and2,tuple(-x for x in and2),and2));us[j]=cut(us[j],0,b)
                    queries+=source(tuple(us),(1,1,1));cases+=1
    else:
        for labels in maps[lo:hi]:
            if kind in ['direct','fallback']:
                for us in itertools.product(pool,repeat=3):
                    activation(labels,us[:2],(0,) if kind=='direct' else (0,1),(us[2],) if kind=='direct' else ((1,),us[2]));cases+=1
            elif kind=='biased':
                and2=(-1,-1,-1,1); bases=[(and2,and2,and2),(and2,tuple(-v for v in and2),and2)]
                for base in bases:
                    activation(labels,base[:2],(0,1),((1,),base[2]));cases+=1
                    for j in range(3):
                        for b in [0,1]:
                            us=list(base);us[j]=cut(us[j],0,b);activation(labels,tuple(us[:2]),(0,1),((1,),us[2]));cases+=1
            if time.perf_counter()-start>(55 if pilot else 180):raise RuntimeError('frozen watchdog')
    # Exact rational certificate for source constant <17.
    e.check(sum(Q(7,3)**j/math.factorial(j) for j in range(9))>10,True)
    out={'status':'PASS','kind':kind,'range':[lo,hi],'cases':cases,'source_queries':queries,'exact_assertions':e.COUNT,'seconds':time.perf_counter()-start,'arithmetic':'integer FWHT, Fraction spectra, prime-log equalities, 40-term rational atanh enclosures with proved tail and outward mesh','pilot':pilot}
    path=R/'out'/f'{kind}_{lo}_{hi}{"_PILOT" if pilot else ""}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
