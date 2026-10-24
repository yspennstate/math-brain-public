from fractions import Fraction as F
from math import comb,log2
import json

def entropy(values):
    coeff=values.copy();N=len(values);step=1
    while step<N:
        for start in range(0,N,2*step):
            for j in range(start,start+step):
                x,y=coeff[j],coeff[j+step]
                coeff[j],coeff[j+step]=x+y,x-y
        step*=2
    H=sum((x*x/(N*N))*log2((N*N)/(x*x))for x in coeff if x)
    energy=sum(j.bit_count()*x*x for j,x in enumerate(coeff))
    return H,F(energy,N*N)

def influence(values,n):
    N=1<<n
    return F(sum((values[x]-values[x|(1<<j)])**2 for x in range(N)for j in range(n)if not(x>>j)&1),2*N)

def monotone_masks(n):
    out=[0,1];size=1
    for dim in range(1,n+1):
        out=[low|(high<<size)for low in out for high in out if low&~high==0]
        size*=2
    return out

def check_dimension(n):
    N=1<<n;levels=[x.bit_count()for x in range(N)]
    edges=[(x,x|(1<<j))for x in range(N)for j in range(n)if not(x>>j)&1]
    thresholds=[[1 if r>t else -1 for r in levels]for t in range(-1,n+1)]
    symH=[entropy(g)[0]for g in thresholds]
    symI=[influence(g,n)for g in thresholds]
    checked=0;max_ratio=0.;max_scaled=F(0);large_cases=0
    for mask in monotone_masks(n):
        f=[1 if(mask>>x)&1 else -1 for x in range(N)]
        plus=[sum(f[x]>0 for x in range(N)if levels[x]==r)for r in range(n+1)]
        q=[F(plus[r],comb(n,r))for r in range(n+1)]
        ext=[F(0)]+q+[F(1)];mu=[ext[j+1]-ext[j]for j in range(n+2)]
        assert min(mu)>=0 and sum(mu)==1
        I=influence(f,n);H,FI=entropy(f);assert FI==I
        expectedI=sum(mu[j]*symI[j]for j in range(n+2));assert expectedI==I
        q0plus=next((r for r in range(n+1)if plus[r]),n)
        qlastminus=max((r for r in range(n+1)if plus[r]<comb(n,r)),default=0)
        a,b=q0plus,qlastminus
        if a>b:a=b=q0plus
        k=b-a+1;assert k>=1
        delta=F(0);Id=F(0);variance=F(0)
        for j,w in enumerate(mu):
            if not w:continue
            g=thresholds[j];d=[x-y for x,y in zip(f,g)]
            assert all(not dx or a<=r<=b for dx,r in zip(d,levels))
            dt=F(sum(x!=y for x,y in zip(f,g)),N)
            idt=F(sum((d[x]-d[y])**2 for x,y in edges),2*N)
            md=F(sum(d),N)
            vt=4*dt-md*md
            assert idt>=vt
            assert H<=2*symH[j]+32*n*float(dt)+1e-11
            if n>=(k+1)**2:
                assert idt>=F(n,2*(k+1)**2)*4*dt
                large_cases+=1
            delta+=w*dt;Id+=w*idt;variance+=w*vt
        assert delta==sum(F(comb(n,r),N)*2*q[r]*(1-q[r])for r in range(n+1))
        assert Id<=4*I and variance>=2*delta
        assert n*delta<=2*(k+1)**2*I
        assert H<=(25+64*(k+1)**2)*float(I)+1e-11
        if k==1:assert H<=62*float(I)+1e-11
        if I:
            max_ratio=max(max_ratio,H/float(I))
            max_scaled=max(max_scaled,F(n)*delta/((k+1)**2*I))
        checked+=1
    return {'n':n,'monotone_functions':checked,'exact_identities_passed':True,'entropy_checks':'floating displays/checks only; inequalities proved analytically','largest_H_over_I_display':max_ratio,'largest_n_Edelta_over_band_squared_I_exact':str(max_scaled),'large_dimension_threshold_instances':large_cases}

if __name__=='__main__':
    report=[]
    for n in range(1,6):
        row=check_dimension(n);report.append(row);print(json.dumps(row),flush=True)
    with open('/workspace/scratch/61b7096f9f41/fei_research/independent_hamming_band_checks.json','w')as f:json.dump(report,f,indent=2)
