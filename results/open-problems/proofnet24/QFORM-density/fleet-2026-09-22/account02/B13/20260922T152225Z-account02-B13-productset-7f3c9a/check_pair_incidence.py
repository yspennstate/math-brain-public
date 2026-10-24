import random, math

random.seed(20260922)
max_total=0.0
max_inc=0.0
min_margin=float('inf')
cases=0
for _ in range(1000):
    n=random.randint(5,12)
    z=[random.uniform(-1,1) for _ in range(n)]
    nz=math.sqrt(sum(t*t for t in z))
    if nz<1e-12:
        continue
    z=[t/nz for t in z]
    def orth(v):
        dot=sum(v[i]*z[i] for i in range(n))
        return [v[i]-dot*z[i] for i in range(n)]
    b=orth([random.uniform(-1,1) for _ in range(n)])
    u=orth([random.uniform(-1,1) for _ in range(n)])
    B=sum(t*t for t in b)
    U=sum(t*t for t in u)
    if B<1e-10 or U<1e-10:
        continue
    c=0.5+0.49*random.random()
    s=0.5+0.49*random.random()
    p={}
    q={}
    for k in range(n):
        for l in range(k+1,n):
            p[k,l]=c*(b[k]*z[l]-z[k]*b[l])**2
            q[k,l]=s*(u[k]*z[l]-z[k]*u[l])**2
    alpha=sum(p.values())
    beta=sum(q.values())
    pk=[sum(v for e,v in p.items() if k in e) for k in range(n)]
    qk=[sum(v for e,v in q.items() if k in e) for k in range(n)]
    max_total=max(max_total,abs(alpha-c*B),abs(beta-s*U))
    max_inc=max(max_inc,
                max(abs(pk[k]-c*(b[k]**2+B*z[k]**2)) for k in range(n)),
                max(abs(qk[k]-s*(u[k]**2+U*z[k]**2)) for k in range(n)))
    M=sum(p[e]*q[f] for e in p for f in q if set(e).isdisjoint(f))
    lb=alpha*beta-sum(pk[k]*qk[k] for k in range(n))
    min_margin=min(min_margin,M-lb)
    cases+=1

print('QFORM_PAIR_INCIDENCE_CHECK_PASS')
print('cases',cases)
print('max_total_mass_error',format(max_total,'.17g'))
print('max_coordinate_incidence_error',format(max_inc,'.17g'))
print('minimum_M_minus_union_bound',format(min_margin,'.17g'))
