from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import itertools,json,sys,time,importlib.util
R=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0
# Read-only reuse of A083's certified scalar log implementation; no peer checker.
old=R.parents[0]/'20261014T023633Z-fleet05-A083-formal-core/code/occupancy_check.py'
spec=importlib.util.spec_from_file_location('a083_scalar',old);E=importlib.util.module_from_spec(spec);spec.loader.exec_module(E)
def ck(b):
    global CHECKS
    CHECKS+=1
    if not b:raise AssertionError(CHECKS)
    if time.perf_counter()-START>60:raise TimeoutError('frozen runtime')
def save(name,v):(R/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def serial(v):return {str(k):str(x) for k,x in v.items()}
@lru_cache(None)
def spectral(t):
    a=list(t);N=len(a);step=1
    while step<N:
        for start in range(0,N,step*2):
            for j in range(start,start+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
        step*=2
    return tuple(F(x*x,N*N) for x in a)
def child(t,i,b):return tuple(v for x,v in enumerate(t) if (x>>i)&1==b)
def erase(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def marg(law,key):
    out=defaultdict(F)
    for z,p in enumerate(law):out[key(z)]+=p
    return out
def vec_log(x):
    v=defaultdict(F)
    for p,e in E.factors(x.numerator).items():v[p]+=e
    for p,e in E.factors(x.denominator).items():v[p]-=e
    return {p:c for p,c in v.items() if c}
def kl(p,q):
    v={}
    for a,b in zip(p,q):
        if a:ck(b>0);v=E.add(v,E.mul(vec_log(a/b),a))
    return v
def conditional(p,q,Z):
    pt=marg(p,lambda z:z&~Z);qt=marg(q,lambda z:z&~Z);v={}
    for z,a in enumerate(p):
        if a:
            T=z&~Z;ck(q[z]>0 and qt[T]>0)
            v=E.add(v,E.mul(vec_log((a/pt[T])/(q[z]/qt[T])),a))
    return v
def query(t,i,Z,q,mode):
    n=len(t).bit_length()-1;p=spectral(t);N=len(t)//2
    pc=[spectral(child(t,i,b)) for b in (0,1)]
    pe=[F(0)]*N;qe=[F(0)]*N
    for s,(a,b) in enumerate(zip(p,q)):pe[erase(s,i)]+=a;qe[erase(s,i)]+=b
    ck(sum(q)==1 and all(q[s]>0 for s,a in enumerate(p) if a))
    ck(all(pe[z]==(pc[0][z]+pc[1][z])/2 for z in range(N)))
    K=[[pc[b][z]/(2*pe[z]) if pe[z] else F(1,2) if mode=='fair' else F(b==int(mode)) for z in range(N)] for b in (0,1)]
    ck(all(K[0][z]+K[1][z]==1 for z in range(N)))
    Qj=[[qe[z]*K[b][z] for z in range(N)] for b in (0,1)]
    qb=[sum(v) for v in Qj];ck(sum(qb)==1 and min(qb)>0)
    Qb=[[a/qb[b] for a in Qj[b]] for b in (0,1)]
    # Literal conditional-law matching, including reference-only atoms.
    matching=True
    for b in (0,1):
        pt=marg(pc[b],lambda z:z&~Z);qt=marg(Qj[b],lambda z:z&~Z)
        for z in range(N):
            T=z&~Z
            if pt[T] and pc[b][z]*qt[T]!=Qj[b][z]*pt[T]:matching=False
    # Independent graph-clique criterion on FULL reference support (L=0 allowed).
    criterion=True
    for T in set(z&~Z for z in range(N)):
        for b in (0,1):
            vals={pe[z]/qe[z] for z in range(N) if z&~Z==T and qe[z] and K[b][z]}
            if len(vals)>1:criterion=False
    ck(matching==criterion)
    Ce=conditional(pe,qe,Z)
    Cchild=E.mul(E.add(*(conditional(pc[b],Qb[b],Z) for b in (0,1))),F(1,2))
    pt=marg(pe,lambda z:z&~Z);qt=marg(qe,lambda z:z&~Z);Oc={}
    for T in pt:
        if not pt[T]:continue
        ps=[sum(pe[z]*K[b][z] for z in range(N) if z&~Z==T)/pt[T] for b in (0,1)]
        qs=[sum(Qj[b][z] for z in range(N) if z&~Z==T)/qt[T] for b in (0,1)]
        Oc=E.add(Oc,E.mul(kl(ps,qs),pt[T]))
    ck(Ce==E.add(Oc,Cchild));ck((not Cchild)==matching)
    erasure={}
    for z in range(N):
        if pe[z]:
            a=[p[s]/pe[z] for s in range(len(p)) if erase(s,i)==z]
            b=[q[s]/qe[z] for s in range(len(p)) if erase(s,i)==z]
            erasure=E.add(erasure,E.mul(kl(a,b),pe[z]))
    O=kl([F(1,2)]*2,qb);Dchild=E.mul(E.add(*(kl(pc[b],Qb[b]) for b in (0,1))),F(1,2))
    ck(kl(p,q)==E.add(erasure,O,Dchild))
    ghosts=sum(qe[z] for z in range(N) if not pe[z])
    ck(sum(Qj[b][z] for b in (0,1) for z in range(N) if not pe[z])==ghosts)
    return {'matching':matching,'reference_only_erased_mass':str(ghosts),'conditional_source_KL':serial(Ce),'conditional_child_KL':serial(Cchild),'conditional_outcome_KL':serial(Oc),'outcome_KL':serial(O),'child_KL':serial(Dchild)},(p,pe,qe,pc,K,Qj)
def canonical():
    # Original reached priority gate, query private b (index2), Z={y}.
    t=tuple((-1)**(x>>1&1) if not (x&1) else (2*(x>>3&1)-1) if x>>2&1 else 1 for x in range(16))
    p=spectral(t);n=4;r=[F(8,15),F(8,15),F(4,15),F(4,15)]
    direct=tuple(F(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(t)),16)**2 for s in range(16))
    ck(p==direct and E.entropy_vector(p)=={2:F(3)})
    inf=[F(sum(t[x]!=t[x^(1<<i)] for x in range(16)),16) for i in range(4)]
    ck(inf==[F(1,2),F(1,2),F(1,4),F(1,4)])
    pcs=[spectral(child(t,2,b)) for b in (0,1)]
    childI=[F(sum(child(t,2,b)[x]!=child(t,2,b)[x^(1<<i)] for x in range(8) for i in range(3)),8) for b in (0,1)]
    ck(childI==[F(1),F(3,2)] and all(E.entropy_vector(a)=={2:F(2)} for a in pcs))
    def product(c):
        a=F(1)
        for v in r:a*=1-c*v
        return a
    lo,hi=F(3,4),F(7,8)
    ck(1-lo-product(lo)>0 and 1-hi-product(hi)<0)
    ck(1-F(13,16)-product(F(13,16))<0)
    for _ in range(48):
        mid=(lo+hi)/2
        if 1-mid-product(mid)>0:lo=mid
        else:hi=mid
    Qiv=[]
    Zlo,Zhi=1-product(lo),1-product(hi)
    for s in range(16):
        if not s:Qiv.append((F(1,16),F(1,16)));continue
        a=b=F(1)
        for j,v in enumerate(r):
            l,h=lo*v,hi*v
            a*=l if s>>j&1 else 1-h;b*=h if s>>j&1 else 1-l
        Qiv.append((F(15,16)*a/Zhi,F(15,16)*b/Zlo))
    def ref(c):
        out=[F(1,16)]
        for s in range(1,16):
            a=F(1)
            for j,v in enumerate(r):a*=c*v if s>>j&1 else 1-c*v
            out.append(F(15,16)*a/(1-product(c)))
        return out
    targeted=[]
    for c in [F(3,4),F(7,8)]:
        for mode in ['fair','0','1']:
            row,data=query(t,2,4,ref(c),mode);ck(not row['matching']);targeted.append(row)
            if mode=='fair':
                _,pe,qe,pc,K,Qj=data
                for b in (0,1):
                    for T in (2,3): # erased {x,a} with a present
                        q0=Qj[b][T];q1=Qj[b][T|4]
                        ck(pc[b][T|4]==0 and q1/(q0+q1)==4*c/15)
                ck(row['conditional_child_KL']==serial(E.mul(vec_log(1/(1-4*c/15)),F(1,2))))
    # Conditional inherited bill: branch prediction factors cancel within each T.
    pe=[(pcs[0][z]+pcs[1][z])/2 for z in range(8)]
    qeiv=[(F(0),F(0)) for _ in range(8)]
    for s,(a,b) in enumerate(Qiv):
        z=erase(s,2);qeiv[z]=(qeiv[z][0]+a,qeiv[z][1]+b)
    K=[[pcs[b][z]/(2*pe[z]) if pe[z] else F(1,2) for z in range(8)] for b in (0,1)]
    def conditional_interval(source,qiv):
        pt=marg(source,lambda z:z&~4);qt={T:(sum(qiv[z][0] for z in range(8) if z&~4==T),sum(qiv[z][1] for z in range(8) if z&~4==T)) for T in pt}
        lower=upper=F(0)
        for z,a in enumerate(source):
            if not a:continue
            T=z&~4;L,U=qiv[z];tl,tu=qt[T]
            ll=E.log2_interval((a/pt[T])*tl/U)[0]
            uu=E.log2_interval((a/pt[T])*tu/L)[1]
            lower+=a*ll;upper+=a*uu
        return lower,upper
    Ce=conditional_interval(pe,qeiv)
    rows=[]
    for b in (0,1):rows.append(conditional_interval([a/2 for a in pcs[b]],[(a*K[b][z],c*K[b][z]) for z,(a,c) in enumerate(qeiv)]))
    Cchild=tuple(rows[0][j]+rows[1][j] for j in (0,1))
    ghost_lower=E.scale(E.log2_interval(F(5,4)),F(1,2))
    ck(ghost_lower[0]>F(1,8))
    ck(Cchild[0]>F(1,8) and Cchild[1]<F(3,8))
    ck(Cchild[1]<F(3,16) and 60**8<8*47**8)
    ck(Ce[1]<F(3,8))
    ck(5**4>2*4**4)
    result={'status':'PASS','truth_table':t,'query':'b','spectator':'y','canonical_c_bracket':list(map(str,[lo,hi])),'canonical_conditional_source_KL_interval':E.outward(Ce),'canonical_conditional_child_KL_interval':E.outward(Cchild),'ghost_contribution_strict_lower_bound_bits':'1/8','conditional_child_strict_upper_bound_bits':'3/16','mean_actual_child_S4_bits':'3','dedicated_fraction_bound':'1/16 of mean S4 (conditional bill only; quotient still unpaid)','exact_conditional_child_formula':'-(1/2)log2(1-4c/15)','terminal_H_bits':['2','2'],'terminal_I':list(map(str,childI)),'rational_support_fixture_cases':targeted}
    save('CANONICAL_FIXTURE.json',result)
    return 6
def main():
    pilot='--pilot' in sys.argv;cases=0;matches=0;ghostcases=0
    for n in ([2] if pilot else [2,3]):
        N=1<<n
        for bits in range(1<<N):
            t=tuple(1-2*((bits>>x)&1) for x in range(N))
            for i in range(n):
                for Z in range(1,1<<(n-1)):
                    for mode in ['fair','0','1']:
                        row,_=query(t,i,Z,[F(1,N)]*N,mode)
                        cases+=1;matches+=row['matching'];ghostcases+=F(row['reference_only_erased_mass'])>0
        save('CENSUS_'+str(n)+('.pilot.json' if pilot else '.json'),{'n':n,'cases':cases,'matches':matches,'reference_only_cases':ghostcases,'assertions':CHECKS})
    targets=0
    if not pilot:
        tt=tuple((1-2*((x&3)==3))*(-1)**(x>>2&1) for x in range(8))
        toy=[]
        for mode in ['fair','0','1']:
            row,data=query(tt,0,3,[F(1,8)]*8,mode);ck(not row['matching']);toy.append(row);targets+=1
        ck(toy[0]['conditional_child_KL']=={'2':'1'} and not toy[0]['outcome_KL'])
        ck(toy[1]['conditional_child_KL']=={'3':'1/2'})
        save('AND_PARITY.json',{'truth_table':tt,'cases':toy,'H_bits':2,'I':2,'query_I':'1/2','mean_terminal_H_bits':0,'mean_terminal_I':'3/2'})
        targets+=canonical()
    ck(cases==(96 if pilot else 7008));ck(targets==(0 if pilot else 9))
    result={'status':'PASS','pilot':pilot,'census_cases':cases,'targeted_rational_cases':targets,'canonical_interval_cases':0 if pilot else 1,'assertions':CHECKS,'seconds':time.perf_counter()-START,'float_used':False,'prior_helper_read_only':str(old)}
    save('PILOT.json' if pilot else 'RESULT.json',result);print(json.dumps(result))
if __name__=='__main__':main()
