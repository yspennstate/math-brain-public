import math, random, json, time
from functools import lru_cache

C = 2.0/math.log(2.0)


def fwht(a):
    a = [float(x) for x in a]
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    inv=1.0/n
    return [x*inv for x in a]


def entropy_probs(p):
    s=0.0
    for x in p:
        if x>0:
            s -= x*math.log2(x)
    return s


def entropy_vals(vals):
    a=fwht(vals)
    return entropy_probs([x*x for x in a])


def vals_from_mask(mask,n):
    N=1<<n
    return [(-1.0 if (mask>>x)&1 else 1.0) for x in range(N)]


def influence_vals(vals,n,i):
    bit=1<<i; N=1<<n; d=0
    for x in range(N):
        if not (x&bit) and vals[x]!=vals[x|bit]: d+=1
    return d/(N/2)


def influences_vals(vals,n):
    return [influence_vals(vals,n,i) for i in range(n)]


def spectral_probs(vals):
    a=fwht(vals)
    return [x*x for x in a]


def marginal_entropy(p,n,coord_mask):
    # entropy of spectral bits on coord_mask
    coords=[i for i in range(n) if (coord_mask>>i)&1]
    m=len(coords); q=[0.0]*(1<<m)
    for S,prob in enumerate(p):
        t=0
        for k,i in enumerate(coords):
            if (S>>i)&1: t |= 1<<k
        q[t]+=prob
    return entropy_probs(q)


def block_cond_entropy(vals,n,A_mask):
    p=spectral_probs(vals)
    H=entropy_probs(p)
    Y=((1<<n)-1)^A_mask
    return H-marginal_entropy(p,n,Y)


def restrict_vals(vals,n,fixed_mask,fixed_bits):
    rem=[i for i in range(n) if not ((fixed_mask>>i)&1)]
    fixed=[i for i in range(n) if ((fixed_mask>>i)&1)]
    out=[]
    for z in range(1<<len(rem)):
        x=0
        for k,i in enumerate(rem):
            if (z>>k)&1: x |= 1<<i
        for k,i in enumerate(fixed):
            if (fixed_bits>>k)&1: x |= 1<<i
        out.append(vals[x])
    return out, rem


def average_section_entropy(vals,n,A_mask):
    Y_mask=((1<<n)-1)^A_mask
    Ycoords=[i for i in range(n) if (Y_mask>>i)&1]
    Acoords=[i for i in range(n) if (A_mask>>i)&1]
    total=0.0
    for y in range(1<<len(Ycoords)):
        sec=[]
        for a in range(1<<len(Acoords)):
            x=0
            for k,i in enumerate(Acoords):
                if (a>>k)&1: x|=1<<i
            for k,i in enumerate(Ycoords):
                if (y>>k)&1: x|=1<<i
            sec.append(vals[x])
        total += entropy_vals(sec)
    return total/(1<<len(Ycoords))


def child_vals(vals,n,i,bit):
    rem=[j for j in range(n) if j!=i]
    out=[]
    for z in range(1<<(n-1)):
        x=(bit<<i)
        for k,j in enumerate(rem):
            if (z>>k)&1: x|=1<<j
        out.append(vals[x])
    return out, rem


def js_div(p,q):
    m=[0.5*(a+b) for a,b in zip(p,q)]
    return entropy_probs(m)-0.5*entropy_probs(p)-0.5*entropy_probs(q)


def remap_mask(mask, rem):
    out=0
    for k,j in enumerate(rem):
        if (mask>>j)&1: out|=1<<k
    return out


def exhaustive_block(max_n=4):
    max_violation=-1e99
    max_gap_ratio=0.0
    cases=0
    worst=None
    start=time.time()
    for n in range(1,max_n+1):
        N=1<<n
        for mask in range(1<<N):
            vals=vals_from_mask(mask,n)
            p=spectral_probs(vals)
            H=entropy_probs(p)
            inf=influences_vals(vals,n)
            for A in range(1,(1<<n)-1):
                Y=((1<<n)-1)^A
                HA=marginal_entropy(p,n,A)
                avg=average_section_entropy(vals,n,A)
                Iy=sum(inf[i] for i in range(n) if (Y>>i)&1)
                rhs=avg+C*Iy
                vio=HA-rhs
                cases+=1
                if vio>max_violation:
                    max_violation=vio; worst=(n,mask,A,HA,avg,Iy,rhs)
                if Iy>1e-15:
                    r=max(0.0,HA-avg)/Iy
                    if r>max_gap_ratio: max_gap_ratio=r
        print('done n',n,'cases',cases,'elapsed',time.time()-start,flush=True)
    return dict(cases=cases,max_violation=max_violation,max_gap_ratio=max_gap_ratio,worst=worst,seconds=time.time()-start)


def random_local(trials=20000,seed=20260920):
    rng=random.Random(seed)
    max_js_vio=-1e99; max_c_vio=-1e99; max_step_vio=-1e99
    max_step_ratio=0.0; worst=None
    for _ in range(trials):
        n=rng.randint(2,8); N=1<<n
        vals=[1.0 if rng.getrandbits(1)==0 else -1.0 for _ in range(N)]
        i=rng.randrange(n)
        others=[j for j in range(n) if j!=i]
        A=0
        for j in others:
            if rng.random()<0.5: A|=1<<j
        if A==0: A=1<<rng.choice(others)
        root=marginal_entropy(spectral_probs(vals),n,A)
        g,rem=child_vals(vals,n,i,0); h,_=child_vals(vals,n,i,1)
        Achild=remap_mask(A,rem)
        avg=0.5*(marginal_entropy(spectral_probs(g),n-1,Achild)+marginal_entropy(spectral_probs(h),n-1,Achild))
        pg=spectral_probs(g); ph=spectral_probs(h)
        js=js_div(pg,ph)
        inf=influence_vals(vals,n,i); j=min(inf,1-inf)
        gap=root-avg
        max_js_vio=max(max_js_vio,gap-js)
        max_c_vio=max(max_c_vio,js-C*j)
        max_step_vio=max(max_step_vio,gap-C*j)
        if j>1e-15 and gap/j>max_step_ratio:
            max_step_ratio=gap/j; worst=(n,i,A,gap,js,j)
    return dict(trials=trials,max_gap_minus_js=max_js_vio,max_js_minus_cj=max_c_vio,max_gap_minus_cj=max_step_vio,max_gap_ratio=max_step_ratio,worst=worst)


def bent_q_vals(d):
    # q = x0*x1 + x2*x3 + ... in 0/1 variables; sign (-1)^q, g(0)=1
    vals=[]
    for x in range(1<<d):
        q=0
        for k in range(0,d,2):
            q ^= ((x>>k)&1) & ((x>>(k+1))&1)
        vals.append(-1.0 if q else 1.0)
    return vals


def sharpness(ds=(2,4,6,8,10,12,14)):
    out=[]
    for d in ds:
        g=bent_q_vals(d); h=g.copy(); h[0]*=-1
        # parent coords A=0..d-1, selector i=d, selector 0->g,1->h
        vals=[]
        for x in range(1<<(d+1)):
            y=(x>>d)&1; a=x&((1<<d)-1)
            vals.append((h if y else g)[a])
        A=(1<<d)-1
        HA=marginal_entropy(spectral_probs(vals),d+1,A)
        avg=0.5*(entropy_vals(g)+entropy_vals(h))
        delta=influence_vals(vals,d+1,d)
        pg=spectral_probs(g); ph=spectral_probs(h)
        js=js_div(pg,ph)
        out.append(dict(d=d,N=1<<d,delta=delta,gap=HA-avg,ratio=(HA-avg)/delta,js=js,js_ratio=js/delta,gap_minus_js=(HA-avg)-js))
    return out

if __name__=='__main__':
    result={}
    result['constant_2_over_ln2']=C
    result['exhaustive_block']=exhaustive_block(4)
    result['random_local']=random_local()
    result['sharpness']=sharpness()
    result['status']='PASS' if result['exhaustive_block']['max_violation']<1e-10 and result['random_local']['max_gap_minus_js']<1e-10 and result['random_local']['max_js_minus_cj']<1e-10 else 'FAIL'
    print(json.dumps(result,indent=2))
    with open('/mnt/data/verify_p03_section_block_output.json','w') as f: json.dump(result,f,indent=2)
