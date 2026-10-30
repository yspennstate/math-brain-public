from __future__ import annotations
from fractions import Fraction
from itertools import product
import json, math

def fwht_int(v):
    a=list(map(int,v)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spec_entropy(v):
    N=len(v); norm2=sum(x*x for x in v)
    if norm2==0: return 0.0
    W=fwht_int(v); den=N*norm2; ans=0.0
    for w in W:
        if w:
            q=Fraction(w*w,den); qf=float(q); ans-=qf*math.log2(qf)
    return ans

def fourier_dirichlet(v):
    N=len(v); W=fwht_int(v)
    return sum(Fraction(s.bit_count()*W[s]*W[s],N*N) for s in range(N))

def boundary(A,n):
    S=set(A); N=1<<n; num=0
    for i in range(n):
        for x in range(N):
            if ((x in S) != ((x^(1<<i)) in S)): num+=1
    return Fraction(num,N)

def components(A,n):
    unseen=set(A); out=[]
    while unseen:
        root=min(unseen); unseen.remove(root); stack=[root]; comp=[root]
        while stack:
            x=stack.pop()
            for i in range(n):
                y=x^(1<<i)
                if y in unseen:
                    unseen.remove(y); stack.append(y); comp.append(y)
        out.append(tuple(sorted(comp)))
    return tuple(out)

def frustration(v):
    N=len(v); n=N.bit_length()-1; total=0
    for i in range(n):
        for x in range(N):
            y=x^(1<<i)
            if v[x] and v[y] and v[x]!=v[y]: total+=1
    return Fraction(total,N)

def component_phase_min(A,n):
    comps=components(A,n)
    if not comps: return 0.0,0.0
    N=1<<n; mix=[0.0]*N
    for comp in comps:
        w=Fraction(len(comp),len(A)); vec=[1 if x in comp else 0 for x in range(N)]
        W=fwht_int(vec); den=N*len(comp)
        for s,z in enumerate(W): mix[s]+=float(w*Fraction(z*z,den))
    Hmix=-sum(q*math.log2(q) for q in mix if q>0)
    best=1e100; k=len(comps)
    for mask in range(1<<max(0,k-1)):
        signs={}
        for j,comp in enumerate(comps):
            sg=1 if j==0 else (1 if (mask>>(j-1))&1 else -1)
            for x in comp: signs[x]=sg
        best=min(best,spec_entropy([signs.get(x,0) for x in range(N)]))
    return best,Hmix

def verify_rows(n=3):
    N=1<<n; row_count=0; support_seen=set(); max_phase_excess=-1e100; max_iso_slack=-1.0
    for vals in product((-1,0,1), repeat=N):
        if not any(vals): continue
        row_count+=1; A=tuple(i for i,x in enumerate(vals) if x)
        ind=[1 if x else 0 for x in vals]
        assert fourier_dirichlet(vals)-fourier_dirichlet(ind)==frustration(vals)
        if A not in support_seen:
            support_seen.add(A); B=boundary(A,n); p=Fraction(len(A),N); comps=components(A,n)
            weights=[Fraction(len(c),len(A)) for c in comps]
            Hw=-sum(float(w)*math.log2(float(w)) for w in weights if w)
            lower=2*float(p)*(math.log2(1/float(p))+Hw)
            assert float(B)+1e-12>=lower
            best,Hmix=component_phase_min(A,n)
            assert best<=Hmix+1e-12
            max_phase_excess=max(max_phase_excess,best-Hmix)
            max_iso_slack=max(max_iso_slack,float(B)-lower)
    return {"ternary_rows_checked":row_count,"distinct_nonempty_supports_checked":len(support_seen),"max_component_phase_min_minus_mixture_entropy":max_phase_excess,"max_isoperimetric_slack":max_iso_slack}

def bool_value(mask,x): return 1 if ((mask>>x)&1) else -1

def verify_square_curl_all_4bit():
    n=4; N=1<<n; checks=0
    for mask in range(1<<N):
        vals=[bool_value(mask,x) for x in range(N)]
        for y in range(n):
            for i in range(n):
                if i==y: continue
                for x in range(N):
                    if (x>>y)&1: continue
                    xy=x^(1<<y); xi=x^(1<<i); xiy=xi^(1<<y)
                    ey0=(vals[x]!=vals[xy]); ey1=(vals[xi]!=vals[xiy])
                    ei0=(vals[x]!=vals[xi]); ei1=(vals[xy]!=vals[xiy])
                    assert (ey0!=ey1)==(ei0!=ei1); checks+=1
    return checks

def parity_gadget():
    high=[]; low=[]
    for y in (0,1):
        for x in range(8):
            b=[(x>>i)&1 for i in range(3)]
            if sum(b)%2:
                high.append(1); low.append(1)
            else:
                low.append(1 if y==0 else -1)
                phase=b[0]*b[1]
                high.append(1 if ((y+phase)&1)==0 else -1)
    Wh=fwht_int(high); Wl=fwht_int(low); ch={}; cl={}
    for W,C in ((Wh,ch),(Wl,cl)):
        for z in W: C[z*z]=C.get(z*z,0)+1
    Hh,Hl=spec_entropy(high),spec_entropy(low); Ih,Il=fourier_dirichlet(high),fourier_dirichlet(low)
    assert ch=={64:2,16:8,0:6}; assert cl=={64:4,0:12}
    assert abs(Hh-3.0)<1e-12 and abs(Hl-2.0)<1e-12
    assert Ih==Fraction(2,1) and Il==Fraction(2,1)
    return {"high_entropy_truth_table":high,"low_entropy_truth_table":low,"high_walsh_square_multiplicities":ch,"low_walsh_square_multiplicities":cl,"high_entropy":Hh,"low_entropy":Hl,"high_influence":str(Ih),"low_influence":str(Il),"entropy_gap_bits":Hh-Hl,"influence_gap":str(Ih-Il)}

def parity_fragmentation_sharpness(m=3):
    N=1<<m; A=[x for x in range(N) if x.bit_count()%2==0]; B=boundary(A,m); p=Fraction(len(A),N)
    comps=components(A,m); w=[Fraction(len(c),len(A)) for c in comps]
    Hw=-sum(float(z)*math.log2(float(z)) for z in w); rhs=2*float(p)*(math.log2(1/float(p))+Hw)
    assert abs(float(B)-rhs)<1e-12
    return {"base_dimension":m,"density":float(p),"component_count":len(comps),"component_label_entropy":Hw,"transverse_boundary":float(B),"isoperimetric_rhs":rhs,"equality":True}

if __name__=="__main__":
    out={"schema_version":1,"row_checks":verify_rows(3),"square_curl_checks":verify_square_curl_all_4bit(),"parity_gadget":parity_gadget(),"parity_fragmentation_sharpness":parity_fragmentation_sharpness(3),"status":"PASS"}
    print(json.dumps(out,sort_keys=True,indent=2))
