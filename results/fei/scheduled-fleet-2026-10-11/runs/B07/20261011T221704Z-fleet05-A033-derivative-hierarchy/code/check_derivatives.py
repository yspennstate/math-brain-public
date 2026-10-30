from pathlib import Path
from fractions import Fraction as F
import json,time,math
R=Path(__file__).resolve().parents[1]
t0=time.perf_counter(); checks=0; cases=0; blocks=0
def ck(b):
    global checks
    checks+=1
    assert b
def fwht(v):
    a=v[:]; h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    return a
def anf(v,n):
    a=v[:]
    for i in range(n):
        for m in range(1<<n):
            if m>>i&1:a[m]^=a[m^(1<<i)]
    return a
def degree(a):return max((s.bit_count() for s,v in enumerate(a) if v),default=-1)
def powprod(ws):
    z=1
    for w in ws:
        if w:z*=w**w
    return z
records=[]
for n in range(4):
    N=1<<n; D=N*N
    for mask in range(1<<N):
        f=[1-2*((mask>>x)&1) for x in range(N)]
        a=fwht(f); w=[x*x for x in a]; ck(sum(w)==D)
        p=anf([(mask>>x)&1 for x in range(N)],n)
        q=[]; deg=[]
        for i in range(n):
            h=[int(f[x]!=f[x^(1<<i)]) for x in range(N)]
            dp=anf(h,n); di=degree(dp); deg.append(di)
            wi=sum(w[s] for s in range(N) if s>>i&1);q.append(wi)
            ck(wi*N==sum(h)*D)
            for x in range(N):
                di_f=F(f[x]-f[x^(1<<i)],2)
                av=F(f[x]+f[x^(1<<i)],2)
                ck(di_f**3==di_f and di_f*av==0 and di_f**2+av**2==1)
            if di>=1:
                ck(min(wi,D-wi)*(1<<di)>=D)
            else:ck(wi in (0,D))
        # Independent physical representation of A031's full signed isometry:
        # v arbitrary rational Fourier weight, multiplication by f preserves its norm.
        v=[F(a[s]*(s.bit_count()+1),N) for s in range(N)]
        spatial=fwht(v)
        cv=fwht([F(f[x])*spatial[x] for x in range(N)])
        cv=[x/N for x in cv]
        direct=[sum(F(a[s],N)*v[s^u] for s in range(N)) for u in range(N)]
        ck(cv==direct);ck(sum(x*x for x in cv)==sum(x*x for x in v))
        back=fwht([f[x]*z for x,z in enumerate(fwht(cv))]);back=[x/N for x in back]
        ck(back==v)
        for X in range(N):
            Y=(N-1)^X
            marg=[0]*N
            for s in range(N):marg[s&Y]+=w[s]
            M=sum(min(q[i],D-q[i]) for i in range(n) if X>>i&1)
            ds=[deg[i] for i in range(n) if X>>i&1 and deg[i]>=1]
            if not ds:
                ck(powprod(marg)==powprod(w))
            else:
                d=max(ds); b=1<<d
                # D*H(S_X|S_Y)=log(prod marg^marg/prod w^w).
                # D*kappa(d)*sum_i J_i=log(2^(d*b*M)/(b-1)^((b-1)*M)).
                ck(powprod(marg)*(b-1)**((b-1)*M)<=powprod(w)*(1<<(d*b*M)))
            blocks+=1
        cases+=1
    records.append({'n':n,'truth_tables':1<<N})
point=[]
for n in range(3,13):
    N=1<<n;D=N*N;w0=(N-2)**2;w=4
    q=F(2,N);I=n*q
    ck(w0+(N-1)*w==D)
    ck(q==F(1,1<<(n-1)))
    H=float(F(w0,D))*math.log2(D/w0)+float(F((N-1)*w,D))*math.log2(D/w)
    bill=n*(-float(q)*math.log2(float(q))-(1-float(q))*math.log2(1-float(q)))
    point.append({'n':n,'I_exact':str(I),'H_over_I_display':H/float(I),'marginal_bill_over_I_display':bill/float(I),'TC_over_I_display':(bill-H)/float(I),'derivative_degree':n-1})
out={'helper_version':'derivative-check-v1','truth_tables':cases,'blocks':blocks,'assertions':checks,'seconds':time.perf_counter()-t0,'arithmetic':'exact integer/Fraction; point-defect entropy display only','domains':records,'point_defects':point,'result':'PASS'}
(R/'out/validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='point_defects'},indent=2))
