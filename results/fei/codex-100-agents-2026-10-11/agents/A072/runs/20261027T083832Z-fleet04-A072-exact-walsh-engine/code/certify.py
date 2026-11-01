from search import *
from functools import lru_cache

# Natural log interval by positive atanh series, after exact power-of-two reduction.
@lru_cache(None)
def ln(x):
    x=F(x); assert x>0
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def series(y):
        z=(y-1)/(y+1); zz=z*z; term=z; v=F(0)
        for j in range(48):v+=term/F(2*j+1);term*=zz
        return 2*v,2*v+2*term/(97*(1-zz))
    lo,hi=series(x); l2,u2=series(F(2))
    return (lo+k*l2,hi+k*u2) if k>=0 else (lo+k*u2,hi+k*l2)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def nat_e(x):return scale(ln(x),x) if x else (F(0),F(0))
@lru_cache(None)
def natL(a,b):
    return add(add(scale(nat_e((a+b)**2),F(1,2)),scale(nat_e((a-b)**2),F(1,2))),add(scale(nat_e(a*a),-1),scale(nat_e(b*b),-1)))
def ell(b):return natL(1-b,b)
def rootN(b):
    v=add(add(scale(ln(1-b),1-b),scale(ln(b),-b)),scale(ln(1-2*b),-(1-2*b)))
    return add(scale(v,4*b),scale(ell(b),-1))
def rounded(a,bits=100):
    den=1<<bits
    return [str(F(a[0].numerator*den//a[0].denominator,den)),str(F(-((-a[1].numerator*den)//a[1].denominator),den))]
def root_check():
    a,c=F(3,10),F(49,100)
    assert rootN(a)[0]>0 and rootN(c)[1]<0
    for _ in range(32):
        b=(a+c)/2; s=rootN(b)
        if s[0]>0:a=b
        elif s[1]<0:c=b
        else:raise AssertionError('precision insufficient')
    l2,u2=ln(F(2)); low=ell(a)[0]/(c*u2); high=ell(c)[1]/(a*l2)
    assert low>2 and high<F(9,4)
    # Four-bit actual Boolean primitive, negative at three vertices on one i-slice.
    g=[1]*16
    for x in (1,3,5):g[x]=-1
    mask=sum(1<<x for x,v in enumerate(g) if v==-1)
    _,w,inf=verify(4,mask);mu=F(w[0],16);t=F(w[1],16)
    primitive=natL(mu,t); assert primitive[0]>2*inf[0]*u2
    result=dict(verdict='PASS',beta=[str(a),str(c)],N_left=rounded(rootN(a)),N_right=rounded(rootN(c)),lambda_interval=rounded((low,high)),primitive=dict(n=4,negative_vertices=[1,3,5],mu=str(mu),t=str(t),influence=str(inf[0]),strictly_above_rate2=True),log_method='48-term exact positive atanh plus geometric tail; power-of-two reduction')
    save('ROOT_CERTIFICATE.json',result);return result
def padd(a,b,c=F(1)):
    a=dict(a)
    for p,v in b.items():
        a[p]=a.get(p,F(0))+c*v
        if not a[p]:del a[p]
    return a
@lru_cache(None)
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
@lru_cache(None)
def eprofile(x):
    if not x:return {}
    d={p:x*v for p,v in factors(x.numerator).items()}
    return padd(d,{p:x*v for p,v in factors(x.denominator).items()},-1)
@lru_cache(None)
def lp(a,b):
    return padd(padd(eprofile((a+b)**2),eprofile((a-b)**2)),padd(eprofile(a*a),eprofile(b*b)),-2)
def pliv(p):
    v=(F(0),F(0))
    for prime,c in p.items():v=add(v,scale(ln(F(prime)),c))
    return v
def full_check():
    start=time.perf_counter(); sig={};checks=0
    for m in range(256):
        _,w,ds=verify(3,m)
        for i,d in enumerate(ds):
            if d:sig.setdefault((abs(F(w[0],8)),abs(F(w[1<<i],8)),d),(m,i))
    rows=0;equal=0;direct_checks=0;signcache={}
    for hm in range(256):
        _,hw,ds=verify(3,hm)
        for j,q in enumerate(ds):
            if not q:continue
            ab=[(F(hw[s],8),F(hw[s|(1<<j)],8)) for s in range(8) if not s>>j&1]
            for (mu,t,d),witness in sig.items():
                for mu in sorted({mu,-mu}):
                    prof={p:c*q/2 for p,c in lp(mu,t).items()}
                    for a,b in ab:
                        prof=padd(prof,lp(a+mu*b,t*b),F(-1,2))
                    # Exact prime-log comparison with the attained finite maximum.
                    normalized={p:c/(q*d) for p,c in prof.items()}
                    diff=padd(normalized,{3:F(3),2:F(-4)},-1)
                    if not diff:equal+=1
                    else:
                        key=tuple(sorted(diff.items()))
                        if key not in signcache:signcache[key]=pliv(diff)[1]<0
                        assert signcache[key],(hm,j,mu,t,d,diff)
                    gm,gi=witness;ga=table(3,gm)
                    if F(sum(ga),8)!=mu:ga=[-x for x in ga]
                    other=[k for k in range(3) if k!=j]
                    ha=table(3,hm);truth=[]
                    for x in range(32):
                        y=((ga[x&7]<0)<<j)
                        for k,axis in enumerate(other):y|=((x>>(3+k))&1)<<axis
                        truth.append(ha[y])
                    fm=sum(1<<x for x,a in enumerate(truth) if a<0)
                    _,fwht,fds=verify(5,fm);assert fds[gi]==q*d
                    # One complete parent/child profile reconstruction per outer query.
                    if mu==F(1,2) and t==F(1,2) and d==F(1,2):
                        def hp(a):
                            N=len(a);res={}
                            for w in fw(a):res=padd(res,eprofile(F(w*w,N*N)),-1)
                            return res
                        def rr(a,i,b):return [v for x,v in enumerate(a) if (x>>i)&1==b]
                        cp=padd(hp(truth),hp(ga),-q);kids=[]
                        for bit in (0,1):kids.append(padd(hp(rr(truth,gi,bit)),hp(rr(ga,gi,bit)),-q))
                        dp=padd(padd({p:v/2 for p,v in padd(kids[0],kids[1]).items()},cp,-1),prof,-1)
                        assert not dp;direct_checks+=1
                    rows+=1
        if time.perf_counter()-start>50:raise RuntimeError('frozen time limit')
    l2,u2=ln(F(2));l3,u3=ln(F(3));maxiv=(3*l3/u2-4,3*u3/l2-4)
    result=dict(verdict='PASS',rows=rows,signatures=len(sig),finite_bound='maximum full drift / physical query influence = 3 log2(3)-4',equality_rows=equal,distinct_strict_sign_profiles=len(signcache),direct_full_entropy_identity_checks=direct_checks,all_full_integer_Walsh_edge_checks=rows,maximum_interval=rounded(maxiv),runtime_seconds=time.perf_counter()-start,scope='all 3-bit outer gates, 3-bit queried core, other outer cores fresh dictators; both mean signs; no arbitrary-dimension conclusion')
    save('FULL_CERTIFICATE.json',result);return result
def witness():
    h=table(3,7);g=table(3,3)
    truth=[h[(((x>>3)&1)|(((x>>4)&1)<<1)|((g[x&7]<0)<<2))] for x in range(32)]
    def checked(a):
        N=len(a);n=N.bit_length()-1;mask=sum(1<<x for x,v in enumerate(a) if v<0)
        _,w,ds=verify(n,mask)
        direct=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(a)) for s in range(N)]
        assert w==direct
        H=(F(0),F(0))
        for v in w:H=add(H,scale(nat_e(F(v*v,N*N)),-1))
        return H,ds,mask,w
    def restrict(a,i,b):return [v for x,v in enumerate(a) if (x>>i)&1==b]
    HP,ds,mask,w=checked(truth);HG,_,_,_=checked(g);q=F(3,4)
    C=add(HP,scale(HG,-q));kids=[]
    for b in (0,1):
        HF,_,_,_=checked(restrict(truth,1,b));Hgc,_,_,_=checked(restrict(g,1,b));kids.append(add(HF,scale(Hgc,-q)))
    drift=add(scale(add(*kids),F(1,2)),scale(C,-1));l2,u2=ln(F(2));ratio=(drift[0]/(ds[1]*u2),drift[1]/(ds[1]*l2))
    assert ratio[0]>F(1,2) and ratio[1]<F(9,4)
    res=dict(verdict='PASS',n=5,truth_mask=mask,Walsh=w,influence=[str(v) for v in ds],outer=dict(n=3,mask=7,queried_input=2),inner=dict(n=3,mask=3,queried_coordinate=1),ratio_interval=rounded(ratio),refuted_statement='Every disjoint-core composition has full correction drift <= (1/2) physical query influence',checks='direct characters = FWHT; Parseval; sign inverse; independent all-edge counts; direct full parent and both child entropy intervals')
    save('HALF_RATE_COUNTEREXAMPLE.json',res);return res
if __name__=='__main__':
    if sys.argv[-1]=='freeze':
        save('CERTIFICATE_SPEC_V4.json',dict(helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),family='same frozen finite family; exact scalar root on continuum via analytic uniqueness proof',case_count='at most 16896 distinct signed rows/full integer spectra plus 32 bisections and one direct Boolean witness',arithmetic='exact prime-log cancellation; strict signs memoized by EXACT normalized coefficient tuple; Fraction log intervals with48 positive atanh terms and explicit geometric tail',symmetry='same absolute signatures; both mean signs',memory_estimate_mb=80,max_runtime_seconds=55,pilot_max_seconds=55));print('CERTIFICATE FROZEN V4')
    elif sys.argv[-1]=='root':print(json.dumps(root_check()))
    elif sys.argv[-1]=='witness':print(json.dumps(witness()))
    else:print(json.dumps(full_check()))
