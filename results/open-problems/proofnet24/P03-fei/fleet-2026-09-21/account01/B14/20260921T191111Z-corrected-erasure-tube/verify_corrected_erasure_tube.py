from __future__ import annotations
import itertools, json, math

TOL=2e-10
TS=(0.25,0.5,0.75)

def fwht(a):
    a=[float(x) for x in a]
    h=1
    while h<len(a):
        for s in range(0,len(a),2*h):
            for j in range(h):
                x,y=a[s+j],a[s+j+h]
                a[s+j],a[s+j+h]=x+y,x-y
        h*=2
    return a

def spectrum(vals):
    N=len(vals)
    return [(x/N)**2 for x in fwht(vals)]

def H(p):
    return -sum(x*math.log2(x) for x in p if x>0)

def h2(x):
    if x<=0.0 or x>=1.0: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def eta(p):
    s=min(p,1-p)
    return 1-h2(0.5+math.sqrt(max(0.0,s*(1-s))))

def infs(p):
    n=(len(p)).bit_length()-1
    return [sum(x for S,x in enumerate(p) if (S>>i)&1) for i in range(n)]

def stats(vals):
    p=spectrum(vals); aa=infs(p)
    return H(p),sum(aa),sum(eta(x) for x in aa),aa,p

def restrict(vals,A,z):
    n=(len(vals)).bit_length()-1
    A=tuple(A); rem=[i for i in range(n) if i not in A]
    out=[]
    for y in range(1<<len(rem)):
        x=0
        for j,i in enumerate(rem):
            x |= ((y>>j)&1)<<i
        for j,i in enumerate(A):
            x |= ((z>>j)&1)<<i
        out.append(vals[x])
    return out

def block(vals,A):
    n=(len(vals)).bit_length()-1
    A=tuple(sorted(A)); rem=[i for i in range(n) if i not in A]
    HH,II,Phi,aa,p=stats(vals)
    marg=[0.0]*(1<<len(rem))
    for S,m in enumerate(p):
        r=0
        for j,i in enumerate(rem):
            r |= ((S>>i)&1)<<j
        marg[r]+=m
    B=HH-H(marg)
    hch=[]; pch=[]
    for z in range(1<<len(A)):
        v=restrict(vals,A,z)
        hz,iz,phiz,az,_=stats(v)
        hch.append(hz); pch.append(phiz)
    avH=sum(hch)/len(hch); avPhi=sum(pch)/len(pch)
    dH=HH-avH; dPhi=Phi-avPhi; JS=dH-B
    return {"B":B,"JS":JS,"dH":dH,"dPhi":dPhi,
            "sum_eta_A":sum(eta(aa[i]) for i in A),
            "I_A":sum(aa[i] for i in A), "H":HH,"I":II,"Phi":Phi}

def avg_curve(vals,t):
    n=(len(vals)).bit_length()-1
    HH,II,Phi,aa,p=stats(vals)
    F=J=barDP=barDE=0.0
    for r in range(n+1):
        w=(t**r)*((1-t)**(n-r))
        for A in itertools.combinations(range(n),r):
            b=block(vals,A)
            F+=w*b["B"]; J+=w*b["JS"]; barDP+=w*b["dPhi"]
            barDE+=w*(b["dH"]-b["dPhi"])
    C=barDP-t*Phi; D=t*HH-F
    identity=(t*(HH-Phi)-barDE)-(D+C-J)
    return D,C,J,identity

def variance_lower(vals,t):
    n=(len(vals)).bit_length()-1
    HH,II,Phi,aa,p=stats(vals)
    total_var=0.0
    for k in range(n):
        others=[i for i in range(n) if i!=k]
        e1=e2=0.0
        for r in range(len(others)+1):
            w=(t**r)*((1-t)**(len(others)-r))
            for A in itertools.combinations(others,r):
                rem=[i for i in range(n) if i not in A]
                kk=rem.index(k)
                for z in range(1<<r):
                    v=restrict(vals,A,z)
                    _,_,_,az,_=stats(v)
                    q=az[kk]
                    wz=w/(1<<r)
                    e1+=wz*q; e2+=wz*q*q
        total_var+=e2-e1*e1
    return 2*(1-t)/(3*math.log(2))*total_var

def descendants(vals):
    n=(len(vals)).bit_length()-1
    for r in range(n+1):
        for A in itertools.combinations(range(n),r):
            for z in range(1<<r):
                v=restrict(vals,A,z)
                HH,II,Phi,aa,p=stats(v)
                if II>TOL:
                    yield (HH-Phi)/II,v

out={"functions":{},"global":{"min_block_absorption":1e9,
                              "max_identity_error":0.0,
                              "min_corrected_critical_margin":1e9,
                              "min_C_minus_variance_lower":1e9}}
for n in range(1,4):
    count=0; block_cases=0; critical_cases=0
    minabs=1e9; maxid=0.0; mincrit=1e9; minvar=1e9
    for mask in range(1<<((1<<n)-1)):
        vals=[1]
        for j in range(1,(1<<n)):
            vals.append(-1 if (mask>>(j-1))&1 else 1)
        count+=1
        for r in range(1,n+1):
            for A in itertools.combinations(range(n),r):
                b=block(vals,A); block_cases+=1
                gap=b["dPhi"]-b["JS"]
                minabs=min(minabs,gap)
                assert gap>=-TOL
                assert b["JS"]<=b["sum_eta_A"]+TOL
        ds=list(descendants(vals))
        if ds:
            rho,g=max(ds,key=lambda z:z[0])
            for t in TS:
                D,C,J,ident=avg_curve(g,t)
                maxid=max(maxid,abs(ident)); critical_cases+=1
                mincrit=min(mincrit,J-D-C)
                assert abs(ident)<=TOL
                assert J-D-C>=-TOL
                vlb=variance_lower(g,t)
                minvar=min(minvar,C-vlb)
                assert C-vlb>=-TOL
    out["functions"][str(n)]={"global_sign_classes":count,
                              "block_cases":block_cases,
                              "critical_curve_cases":critical_cases,
                              "min_DeltaPhi_minus_JS":minabs,
                              "max_corrected_curve_identity_error":maxid,
                              "min_J_minus_D_minus_C_on_corrected_critical":mincrit,
                              "min_C_minus_strong_concavity_variance_lower":minvar}
    out["global"]["min_block_absorption"]=min(out["global"]["min_block_absorption"],minabs)
    out["global"]["max_identity_error"]=max(out["global"]["max_identity_error"],maxid)
    out["global"]["min_corrected_critical_margin"]=min(out["global"]["min_corrected_critical_margin"],mincrit)
    out["global"]["min_C_minus_variance_lower"]=min(out["global"]["min_C_minus_variance_lower"],minvar)
print(json.dumps(out,indent=2,sort_keys=True))
