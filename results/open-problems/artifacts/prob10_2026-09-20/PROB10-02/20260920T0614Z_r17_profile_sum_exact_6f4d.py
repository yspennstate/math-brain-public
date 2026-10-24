from fractions import Fraction

UV=((0,0),(0,1),(1,0),(1,1))

def bits(mask,m):
    return tuple((mask>>(m-1-i))&1 for i in range(m))

def mask_from_bits(xs):
    z=0
    for b in xs: z=(z<<1)|b
    return z

def compress_zero_bit(gmask,j,m):
    z=0
    for i in range(m):
        if i!=j:
            z=(z<<1)|((gmask>>(m-1-i))&1)
    return z

def expand_zero_bit(c,j,m):
    out=0; src=m-2
    for i in range(m):
        out <<= 1
        if i==j:
            b=0
        else:
            b=(c>>src)&1; src-=1
        out |= b
    return out

def encode(xmask,gmask,j,m):
    B=1<<(m-1)
    return ((xmask*m+j)*B)+compress_zero_bit(gmask,j,m)

def decode(idx,m):
    B=1<<(m-1); c=idx%B; q=idx//B; j=q%m; xmask=q//m
    return xmask,expand_zero_bit(c,j,m),j

def carrier_update(xmask,gmask,m,u,v):
    x=bits(xmask,m); g=bits(gmask,m); d=[0]*(m+1)
    for i in range(1,m+1):
        d[i]=(1-g[i-1])*int(d[i-1] or (x[i-1]==v))
    gp=[0]*m
    for i in range(1,m):
        gp[i-1]=g[i]+d[i+1]-d[i]
        assert gp[i-1] in (0,1)
    gp[m-1]=(1-d[m])*int(u==v)
    xp=x[1:]+(u,)
    return mask_from_bits(xp),mask_from_bits(gp)

def edge_transition(idx,m,u,v):
    x,g,j=decode(idx,m)
    h=g|(1<<(m-1-j))
    xp,gp=carrier_update(x,g,m,u,v)
    xp2,hp=carrier_update(x,h,m,u,v)
    assert xp==xp2
    diff=gp^hp
    if diff==0: return -1
    assert diff&(diff-1)==0
    j2=m-1-(diff.bit_length()-1)
    assert ((gp>>(m-1-j2))&1)==0 and ((hp>>(m-1-j2))&1)==1
    return encode(xp,gp,j2,m)

def build_trans(m):
    n=m*(1<<m)*(1<<(m-1))
    return [[edge_transition(i,m,u,v) for (u,v) in UV] for i in range(n)]

def profile_certificate(m,T):
    tr=build_trans(m); n=len(tr)
    N=[1]*n
    prefix=Fraction(0,1)
    alpha_list=[]
    for t in range(T+1):
        alpha=Fraction(max(N),4**t)
        alpha_list.append(alpha)
        if t==T: break
        prefix += min(Fraction(1,1), m*alpha)
        N=[sum(N[q] for q in row if q>=0) for row in tr]
    NN=[sum(N[q] for q in row if q>=0) for row in tr]
    lam=max(Fraction(a,4*b) for a,b in zip(NN,N) if b)
    alpha=alpha_list[T]
    assert lam<1 and m*alpha<1
    C=Fraction(m,1)+prefix+m*alpha/(1-lam)
    return tr,alpha_list,lam,C,prefix

def guaranteed_survival(tr,depthmax):
    good=[True]*len(tr); counts=[]
    for r in range(1,depthmax+1):
        good=[all(q>=0 and good[q] for q in row) for row in tr]
        counts.append(sum(good))
        if counts[-1]==0: break
    return counts

def moore_classes(tr):
    n=len(tr); cls=[0]*n; hist=[]
    while True:
        d={}; new=[0]*n
        for i,row in enumerate(tr):
            sig=tuple(-1 if q<0 else cls[q] for q in row)
            c=d.get(sig)
            if c is None:
                c=len(d); d[sig]=c
            new[i]=c
        hist.append(len(d))
        if new==cls: return len(d),hist
        cls=new

print('R17 PROB10-02 exact profile-sum / obstruction checker')
print('guaranteed-survival depths and Moore survival-language quotient')
for m in range(2,7):
    tr=build_trans(m)
    gs=guaranteed_survival(tr,2*m)
    last=max((i+1 for i,c in enumerate(gs) if c>0),default=0)
    classes,hist=moore_classes(tr)
    print(f'm={m} edge_states={len(tr)} guaranteed_counts={gs} max_guaranteed_depth={last} moore_non_sink_classes={classes} moore_with_sink={classes+1} refinement={hist}')

for m in (7,8):
    tr=build_trans(m)
    gs=guaranteed_survival(tr,2*m)
    last=max((i+1 for i,c in enumerate(gs) if c>0),default=0)
    print(f'm={m} edge_states={len(tr)} guaranteed_counts={gs} max_guaranteed_depth={last}')

m=8; T=32
tr,alphas,lam,C,prefix=profile_certificate(m,T)
print(f'PROFILE m={m} T={T}')
print(f'alpha_T={alphas[T].numerator}/{alphas[T].denominator}={float(alphas[T]):.18f}')
print(f'lambda_T={lam.numerator}/{lam.denominator}={float(lam):.18f}')
print(f'prefix_sum={prefix.numerator}/{prefix.denominator}={float(prefix):.18f}')
print(f'C_profile={C.numerator}/{C.denominator}={float(C):.18f}')
assert C < 39
assert alphas[T] == Fraction(666247718450140937,18446744073709551616)
assert lam == Fraction(994266288913277,1142366470455998)
print('m=8 exact profile-summed finite-horizon/stationary certificate: C_8^profile < 39; PASS')
print('inherited T=32 alpha/lambda exact cross-check: PASS')
print('guaranteed-survival and Moore quotient exact finite checks: PASS')
print('ALL_EXACT_CHECKS_PASS')
