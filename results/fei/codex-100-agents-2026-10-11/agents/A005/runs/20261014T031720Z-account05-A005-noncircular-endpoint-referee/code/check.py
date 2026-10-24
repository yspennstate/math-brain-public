from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent/'20261014T001325Z-account05-A005-noncircular-endpoint-referee/code/check.py'
A={'__name__':'arithmetic_only','__file__':str(BASE)}
exec(compile(BASE.read_text(),str(BASE),'exec'),A)
add,scale,phi,fwht,entropy,influence,total,seed,evaluate,sign,const,physical_i=(A[k] for k in ['add','scale','phi','fwht','entropy','influence','total','seed','evaluate','sign','const','physical_i'])
def labels(D):
    r=2
    while (1<<r)-r-1<D:r+=1
    return r,[x for x in range(1,1<<r) if x.bit_count()>=2][:D]
def tensor(f,t):
    n=(len(f)-1).bit_length();v=[]
    for x in range(1<<(n*t)):
        y=1
        for j in range(t):y*=f[(x>>(n*j))&((1<<n)-1)]
        v.append(y)
    return v
def coded(f,t):
    g=tensor(f,t);D=(len(g)-1).bit_length();r,ls=labels(D);N=D+r
    v=[]
    for x in range(1<<N):
        z=x>>D;y=x&((1<<D)-1)
        for j,l in enumerate(ls):y^=((l&z).bit_count()&1)<<j
        v.append(g[y])
    return v,D,r,ls
def restrict(v,N,coords,b):
    rest=[i for i in range(N) if i not in coords];out=[]
    for y in range(1<<len(rest)):
        x=sum(((y>>j)&1)<<i for j,i in enumerate(rest))+sum(((b>>j)&1)<<i for j,i in enumerate(coords))
        out.append(v[x])
    return out
def quotient(x,y):return x/y if y else Q(0)
def pair(a,i,j):
    C=Mi=Mj=ci=cj=Q(0);B={}
    for s,al in enumerate(a):
        if (s>>i)&1 or (s>>j)&1:continue
        be=a[s|(1<<i)];ga=a[s|(1<<j)];de=a[s|(1<<i)|(1<<j)]
        q=al*al+be*be+ga*ga+de*de
        if not q:continue
        ri=4*quotient(al*al*be*be,al*al+be*be)+4*quotient(ga*ga*de*de,ga*ga+de*de)
        rj=4*quotient(al*al*ga*ga,al*al+ga*ga)+4*quotient(be*be*de*de,be*be+de*de)
        Ai=4*(al*be+ga*de)**2/q;Aj=4*(al*ga+be*de)**2/q
        P=4*(al*de+be*ga)**2/q
        C+=Ai+Aj+P;Mi+=ri-Ai;Mj+=rj-Aj;ci+=ri;cj+=rj
        B=add(B,*(phi(x*x) for x in [al,be,ga,de]),scale(phi(q),-1))
    return C,Mi,Mj,ci,cj,B
def collision_i(a,i):
    return sum((4*quotient(u*u*a[s|(1<<i)]**2,u*u+a[s|(1<<i)]**2) for s,u in enumerate(a) if not s>>i&1),Q(0))
def physical_pair_collision(a,i,j):
    val=Q(0)
    for s,u in enumerate(a):
        if s>>i&1 or s>>j&1:continue
        b=a[s|(1<<i)];c=a[s|(1<<j)];d=a[s|(1<<i)|(1<<j)];q=u*u+b*b+c*c+d*d
        if q:val+=sum(((u+(-1)**x*b+(-1)**y*c+(-1)**(x+y)*d)**4 for x in [0,1] for y in [0,1]),Q(0))/(4*q)-q
    return val
def run(mode):
    start=time.perf_counter();checks=0;cases=0;pairs=0
    def eq(x,y):
        nonlocal checks
        checks+=1;assert x==y,(x,y)
    if mode=='control':
        f=seed(3,254);a=fwht(f);t=64;D=192;r,ls=labels(D);N=D+r;K=Q(8,3);p=Q(1,1<<N)
        eq(r,8);eq(N,200);eq(len(set(ls)),D);eq(all(l.bit_count()>=2 for l in ls),True)
        tag=[];masks=[]
        for z in range(r):
            masks_z=[sum(((ls[3*b+j]>>z)&1)<<j for j in range(3)) for b in range(t)]
            corr=Q(1)
            for mask in masks_z:
                aut=sum((u*u*((-1)**((s&mask).bit_count())) for s,u in enumerate(a)),Q(0))
                eq(aut,1 if not mask else Q(1,2));corr*=aut
            tag.append((1-corr)/2);masks.append(sum(bool(m) for m in masks_z))
        IF=t*total(a,3)+sum(tag,Q(0));eq(IF<=52,True)
        # TV <= v=2sqrt(p)=2^-99; h2(v)<=v*(99+3/2).
        v=Q(1,1<<99);E_H=Q(601,2)*v;E_I=2*N*p
        lower=add(scale(entropy(a),t),const(-K*IF-E_H-K*E_I))
        eq(sign(lower),1);lo,hi=evaluate(lower)
        eq(lo>3,True)
        pair_upper=(3*N+29)*p;singleton_upper=(2*N+13)*p
        eq(pair_upper<lo,True);eq(singleton_upper<lo,True)
        # Any one/two-bit exceptional child: probability <=4p,
        # TV<=2^-98; ambient dimension <=199. Use the larger
        # common bound (199+98+3/2)*2^-98 for BOTH block sizes.
        child_EH=Q(597,2)*Q(1,1<<98);child_EI=2*(N-2)*4*p
        child_lower=add(scale(entropy(a),t),const(-K*IF-child_EH-K*child_EI))
        eq(sign(child_lower),1)
        eq(evaluate(child_lower)[0]>3,True)
        result={'mode':mode,'cases':1,'assertions':checks,'failures':0,'N':N,'D':D,'r':r,'K':'8/3','t':64,'labels':ls,
          'tag_nonzero_copy_masks':masks,'tag_influences':[str(x) for x in tag],'I_F':str(IF),'p':str(p),
          'entropy_surgery_error_upper':str(E_H),'influence_surgery_error_upper':str(E_I),
          'root_deficit_lower_bound_interval':[str(x) for x in [lo,hi]],'uniform_pair_S_upper':str(pair_upper-lo),
          'uniform_singleton_sigma_upper':str(singleton_upper-lo),'all_pair_count':N*(N-1)//2,
          'every_individual_singleton_and_pair_child_deficit_lower_interval':[str(x) for x in evaluate(child_lower)],
          'total_pair_collision_and_refund_upper':str(16*Q(N*(N-1),2)*p),
          'certificate_scope':'Analytic compressed actual Boolean N200 family; no truth-table enumeration is claimed'}
    else:
        domains=[(2,2)] if mode.startswith('chunk') else [(1,1),(1,2),(2,1)]+([] if mode=='pilot' else [(2,2)])
        for n,t in domains:
            bs=range(4*int(mode[-1]),4*int(mode[-1])+4) if mode.startswith('chunk') else range(1<<(1<<n))
            for b in bs:
                assert time.perf_counter()-start<50,'Frozen in-loop guard'
                f=seed(n,b);v,D,r,ls=coded(f,t);N=D+r;cases+=1;a=fwht(v);aa=fwht(tensor(f,t));p=Q(1,1<<N)
                mapped={s|(sum(((sum(((ls[k]>>z)&1) for k in range(D) if s>>k&1)&1)<<z) for z in range(r))<<D):u for s,u in enumerate(aa) if u}
                for s,u in enumerate(a):eq(u,mapped.get(s,Q(0)))
                supp=[s for s,u in enumerate(a) if u]
                eq(all((x^y).bit_count()>=3 for x,y in combinations(supp,2)),True)
                eq(entropy(a),scale(entropy(fwht(f)),t))
                eq(total(a,N),t*total(fwht(f),n)+sum((influence(a,i) for i in range(D,N)),Q(0)))
                w=v[:];w[0]*=-1;c=fwht(w)
                eq(sum(x<0 for x in v)%2,0);eq(sum(x<0 for x in w)%2,1);eq(all(c),True)
                for s,u in enumerate(c):eq(u,a[s]-v[0]*2*p)
                collisions=[collision_i(c,i) for i in range(N)]
                for i in range(N):
                    eq(influence(c,i),physical_i(w,N,i));eq(abs(influence(c,i)-influence(a,i))<=2*p,True)
                    eq(collision_i(a,i),0);eq(collisions[i]<=8*p,True)
                    # Independent source review: signed tensor corrected-price maximum identity.
                for i,j in combinations(range(N),2):
                    pairs+=1;C,Mi,Mj,ci,cj,B=pair(c,i,j)
                    eq(pair(a,i,j)[:5],(0,0,0,0,0));eq(C,physical_pair_collision(c,i,j))
                    eq(C<=16*p,True);eq(Mi>=0 and Mj>=0 and Mi+Mj<=16*p,True)
                    eq(ci,collisions[i]);eq(cj,collisions[j])
                    children=[fwht(restrict(w,N,[i,j],z)) for z in range(4)]
                    HC=scale(add(*(entropy(ch) for ch in children)),Q(1,4));IC=sum((total(ch,N-2) for ch in children),Q(0))/4
                    L=add(entropy(c),scale(HC,-1));I=total(c,N);IA=influence(c,i)+influence(c,j)
                    eq(I-IC,IA);eq(sign(add(const((3*N+29)*p),scale(L,-1)))>0,True)
                    for K in [Q(0),Q(1),Q(8,3),Q(4)]:
                        delta=add(entropy(c),const(-K*I));S=add(const(K*IC),scale(HC,-1))
                        eq(add(delta,S,const(K*IA)),L)
        result={'mode':mode,'cases':cases,'pair_cuts':pairs,'assertions':checks,'failures':0,'max_dimension':7 if mode!='pilot' else 5}
    result['elapsed_seconds']=time.perf_counter()-start;assert result['elapsed_seconds']<55
    (ROOT/'out'/f'{mode.upper()}_VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['labels','tag_influences']}))
if __name__=='__main__':run(sys.argv[1])
