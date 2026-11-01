import math, random, itertools, hashlib, json, time

TOL=2e-12

def h2(p):
    if p<=0.0 or p>=1.0: return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def influence_bool(y,n,i):
    N=1<<n
    return sum(1 for x in range(N) if y[x] != y[x^(1<<i)])/N

def cond_stats_event(y,n,A):
    # Y Boolean 0/1, A bitmask. Uniform cube.
    N=1<<n
    coords=[i for i in range(n) if (A>>i)&1]
    groups={}
    for x in range(N):
        key=tuple((x>>i)&1 for i in coords)
        s,c=groups.get(key,(0,0))
        groups[key]=(s+y[x],c+1)
    cval=0.0; H=0.0
    for s,c in groups.values():
        u=s/c
        w=c/N
        cval += w*max(2*u-1,0.0)
        H += w*h2(u)
    return cval,H

def event_checker(max_n=4):
    total=0; max_cross_violation=-1e9; max_entropy_violation=-1e9; max_identity_err=0.0
    equality_one_resid_err=0.0
    for n in range(1,max_n+1):
        N=1<<n
        # complement symmetry: enumerate only density <=1/2 automatically.
        for mask in range(1<<N):
            pop=mask.bit_count()
            if pop*2>N: continue
            y=[(mask>>x)&1 for x in range(N)]
            p=pop/N
            inf=[influence_bool(y,n,i) for i in range(n)]
            for A in range(1<<n):
                c,H=cond_stats_event(y,n,A)
                residual=sum(inf[i] for i in range(n) if not ((A>>i)&1))
                # direct E min posterior
                coords=[i for i in range(n) if (A>>i)&1]
                groups={}
                for x in range(N):
                    key=tuple((x>>i)&1 for i in coords)
                    s,ct=groups.get(key,(0,0)); groups[key]=(s+y[x],ct+1)
                emin=0.0
                for s,ct in groups.values():
                    u=s/ct; emin+=(ct/N)*min(u,1-u)
                max_identity_err=max(max_identity_err,abs((p-c)-emin))
                max_entropy_violation=max(max_entropy_violation,H-residual)
                max_cross_violation=max(max_cross_violation,(p-0.5*residual)-c)
                residual_coords=[i for i in range(n) if not ((A>>i)&1)]
                if len(residual_coords)==1:
                    equality_one_resid_err=max(equality_one_resid_err,abs(c-(p-0.5*residual)))
                total+=1
    return dict(total_event_block_cases=total,max_cross_lower_bound_violation=max_cross_violation,
                max_cond_entropy_boundary_violation=max_entropy_violation,
                max_p_minus_c_identity_error=max_identity_err,
                max_one_residual_equality_error=equality_one_resid_err)

def fwht(vals):
    a=[float(v) for v in vals]
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return [v/n for v in a]

def char_gauge(f,n,T):
    return [f[x]*(-1 if ((x&T).bit_count()&1) else 1) for x in range(1<<n)]

def center_f(f,n):
    T=0
    ps=[]
    for i in range(n): ps.append(influence_bool(f,n,i))
    for i,p in enumerate(ps):
        if p>0.5: T|=1<<i
    g=char_gauge(f,n,T)
    return g,T

def eta(f,n,j):
    # Represent on full cube; independent of bit j. This keeps uniform averaging simple.
    return [1 if f[x]!=f[x^(1<<j)] else 0 for x in range(1<<n)]

def beta_matrix(f,n):
    et=[eta(f,n,j) for j in range(n)]
    b=[[0.0]*n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if i!=j: b[i][j]=influence_bool(et[j],n,i)
    return et,b

def spectral_cond_entropy(pdist,n,A):
    # H(X_A | X_Ac)
    Hfull=sum(-p*math.log2(p) for p in pdist if p>0)
    Ac=((1<<n)-1)^A
    mass={}
    for S,p in enumerate(pdist):
        key=S&Ac
        mass[key]=mass.get(key,0.0)+p
    Hac=sum(-p*math.log2(p) for p in mass.values() if p>0)
    return Hfull-Hac

def phi(z,k):
    if k<=0:return 0.0
    if abs(z-1.0)<1e-15:return float(k)
    return (1-z**k)/(1-z)

def folded_minimizer(pdist,n,z):
    best=None; bestT=0
    for T in range(1<<n):
        val=0.0
        for S,p in enumerate(pdist):
            val+=p*phi(z,(S^T).bit_count())
        if best is None or val<best-1e-15:
            best=val; bestT=T
    return bestT,best

def Lambda(pdist,n,z,T,A):
    out=0.0
    full=(1<<n)-1
    for S,p in enumerate(pdist):
        R=S^T
        kin=(R&A).bit_count(); kout=(R&(full^A)).bit_count()
        out += p*(z**kout)*phi(z,kin)
    return out

def crossing_full_eta(etaj,n,j,A):
    # A excludes j; condition full-cube eta on A, j is irrelevant automatically.
    return cond_stats_event(etaj,n,A)[0]

def boolean_policy_checker():
    total_f=0; symmetry_err=0.0; act_violation=-1e9; cert_cross_violation=-1e9; cert_refund_violation=-1e9; cert_cases=0
    rng=random.Random(20260921)
    cases=[]
    for n in [1,2,3]:
        N=1<<n
        for mask in range(1<<(N-1)): # fix f(0)=+1; other signs arbitrary
            f=[1]+[-1 if ((mask>>(x-1))&1) else 1 for x in range(1,N)]
            cases.append((n,f))
    n=4; N=1<<n
    for _ in range(2000):
        f=[1]+[rng.choice([-1,1]) for _ in range(1,N)]
        cases.append((n,f))
    for n,f0 in cases:
        f,Tmed=center_f(f0,n)
        p=[influence_bool(f,n,i) for i in range(n)]
        coeff=fwht(f); pd=[c*c for c in coeff]
        # spectral/influence consistency
        for i in range(n):
            pm=sum(pd[S] for S in range(1<<n) if (S>>i)&1)
            if abs(pm-p[i])>2e-11: raise AssertionError(('spectral mismatch',n,i,pm,p[i]))
        et,b=beta_matrix(f,n)
        for i in range(n):
            for j in range(n):
                symmetry_err=max(symmetry_err,abs(b[i][j]-b[j][i]))
        d=n; z=0.0 if d==1 else 1-1/d
        Tstar,_=folded_minimizer(pd,n,z)
        # every physical block activation lower bound
        for A in range(1<<n):
            lam=Lambda(pd,n,z,Tstar,A)
            IA=sum(p[i] for i in range(n) if (A>>i)&1)
            act_violation=max(act_violation, math.exp(-1)*IA-lam)
        for L in [3.0,4.0,6.0,8.0]:
            for j in range(n):
                if p[j]<=1e-15 or p[j]>0.5+TOL: continue
                A=0
                for i in range(n):
                    if i==j: continue
                    if h2(p[i]) <= L*p[i] + 1e-14:
                        A|=1<<i
                R=sum(b[i][j] for i in range(n) if i!=j and not ((A>>i)&1))
                if R <= p[j]+1e-13: # gamma=1/2 condition
                    c=crossing_full_eta(et[j],n,j,A)
                    cert_cross_violation=max(cert_cross_violation,0.5*p[j]-c)
                    BA=spectral_cond_entropy(pd,n,A)
                    lam=Lambda(pd,n,z,Tstar,A)
                    cert_refund_violation=max(cert_refund_violation,BA-math.e*L*lam)
                    cert_cases+=1
        total_f+=1
    return dict(boolean_functions_or_samples=total_f,beta_symmetry_max_error=symmetry_err,
                activation_lower_bound_max_violation=act_violation,
                policy_certificate_cases=cert_cases,
                policy_crossing_max_violation=cert_cross_violation,
                policy_B_minus_eL_Lambda_max_violation=cert_refund_violation)

def combinatorial_activation_check(max_d=500):
    max_violation=-1e9; cases=0
    for d in range(1,max_d+1):
        z=0.0 if d==1 else 1-1/d
        for kin in range(d+1):
            for kout in range(d-kin+1):
                if kin==0: lhs=0.0
                else: lhs=(z**kout)*phi(z,kin) if d>1 else 1.0
                rhs=math.exp(-1)*kin
                max_violation=max(max_violation,rhs-lhs); cases+=1
    return dict(d_split_cases=cases,max_einv_termwise_violation=max_violation)

start=time.time()
res={
  'event':event_checker(4),
  'activation':combinatorial_activation_check(500),
  'boolean_policy':boolean_policy_checker(),
}
res['elapsed_seconds']=round(time.time()-start,3)
print(json.dumps(res,indent=2,sort_keys=True))
