#!/usr/bin/env python3
"""Exact/numerical falsification checks for B16 local triple-curvature flag theorem.
Standard library only. No external data or network.
"""
from __future__ import annotations
import itertools, math, random
from fractions import Fraction

TOL=2e-10

def bits(x,n):
    return tuple((x>>i)&1 for i in range(n))

def dot2(a,b):
    return sum(x*y for x,y in zip(a,b))&1

def all_bool_functions(n):
    N=1<<n
    for mask in range(1<<N):
        yield [1 if ((mask>>x)&1)==0 else -1 for x in range(N)]

def influence(f,n,i):
    N=1<<n
    return Fraction(sum(1 for x in range(N) if f[x]!=f[x^(1<<i)]),N)

def character_gauge(f,n):
    inf=[influence(f,n,i) for i in range(n)]
    K=[i for i,p in enumerate(inf) if p>Fraction(1,2)]
    g=[]
    for x,val in enumerate(f):
        phase=-1 if sum((x>>i)&1 for i in K)&1 else 1
        g.append(val*phase)
    beta=[min(p,1-p) for p in inf]
    return g,beta

def parent_cells(n,order):
    rank={v:j for j,v in enumerate(order)}
    out=[]
    for i in order:
        later=[j for j in order if rank[j]>rank[i]]
        m=len(later)
        for patt in range(1<<m):
            fixed={i:0}
            for t,j in enumerate(later):
                fixed[j]=(patt>>t)&1
            cell=[]
            for x in range(1<<n):
                if all(((x>>j)&1)==v for j,v in fixed.items()):
                    cell.append(x)
            out.append((i,m,tuple(cell)))
    return out

def conditional_influence(f,n,cell,free_i):
    S=set(cell)
    if not cell: return Fraction(0)
    return Fraction(sum(1 for x in cell if (x^(1<<free_i)) in S and f[x]!=f[x^(1<<free_i)]), len(cell))

def affine_basis_words(n):
    N=1<<n
    basis=[tuple(1 for _ in range(N))]
    for i in range(n):
        basis.append(tuple((x>>i)&1 for x in range(N)))
    return basis

def relation_code_C0(n):
    N=1<<n
    aff=affine_basis_words(n)
    out=[]
    for m in range(1<<N):
        w=tuple((m>>x)&1 for x in range(N))
        if all(dot2(w,a)==0 for a in aff):
            out.append(w)
    return out

def dual_of(code,n):
    N=1<<n
    out=[]
    for m in range(1<<N):
        r=tuple((m>>x)&1 for x in range(N))
        if all(dot2(r,w)==0 for w in code):
            out.append(r)
    return out

def phase_from_word(r):
    return [(-1 if z else 1) for z in r]

def mean_phase_product(h,rphase):
    return sum(a*b for a,b in zip(h,rphase))/len(h)

def phi_E(h,s,P):
    N=len(h)
    return 2*N/len(P)*sum(math.cos(s*mean_phase_product(h,phase_from_word(r))) for r in P)

def mul(a,b): return [x*y for x,y in zip(a,b)]

def retained_psi(h,s,P0,P1): return phi_E(h,s,P0)-phi_E(h,s,P1)

def diff3_psi(h,g0,g1,f,s,P0,P1):
    ans=0.0
    for a,b,c in itertools.product([0,1], repeat=3):
        hh=h[:]
        if a: hh=mul(hh,g0)
        if b: hh=mul(hh,g1)
        if c: hh=mul(hh,f)
        ans += (-1)**(a+b+c)*retained_psi(hh,s,P0,P1)
    return ans

def cell_stats(f_old,n_old,cell):
    N=1<<n_old
    uplus=Fraction(sum(1 for x in cell if f_old[x]==1),N)
    uminus=Fraction(sum(1 for x in cell if f_old[x]==-1),N)
    pplus=Fraction(sum(1 for x in range(N) if f_old[x]==1),N)
    pminus=1-pplus
    return uplus,uminus,pplus-uplus,pminus-uminus,pplus,pminus

def triple_bound(gamma,s,uplus,uminus,aplus,aminus):
    up,um,ap,am=map(float,[uplus,uminus,aplus,aminus])
    delta=up+um
    B=(ap*ap+am*am)/2+(up*up+um*um)/6
    return 16*gamma*s**4*(2*math.sqrt(up*um)*B+ap*am*delta)

def extend_dummy(f_old,n_old):
    N=1<<n_old
    return [f_old[x%N] for x in range(2*N)]

def clone_generators(n_old,cell):
    N=1<<n_old
    S=set(cell)
    g0=[];g1=[]
    for z in range(2*N):
        x=z%N; y=z//N
        g0.append(-1 if x in S and y==0 else 1)
        g1.append(-1 if x in S and y==1 else 1)
    return g0,g1

def test_scalar_factorization():
    rng=random.Random(1604)
    count=0
    for _ in range(10000):
        A1,A0,B1,B0,C1,C0=[rng.uniform(-1,1) for _ in range(6)]
        ss=rng.uniform(0,4)
        def q(A,B,C): return math.cos(ss*A)*math.sin(ss*B)*math.sin(ss*C)
        lhs=q(A1+A0,B1+B0,C1+C0)-q(A1-A0,B1-B0,C1-C0)
        rhs=2*(
            math.cos(ss*A1)*math.cos(ss*A0)*math.sin(ss*B1)*math.cos(ss*B0)*math.cos(ss*C1)*math.sin(ss*C0)
            +math.cos(ss*A1)*math.cos(ss*A0)*math.cos(ss*B1)*math.sin(ss*B0)*math.sin(ss*C1)*math.cos(ss*C0)
            -math.sin(ss*A1)*math.sin(ss*A0)*math.sin(ss*B1)*math.cos(ss*B0)*math.sin(ss*C1)*math.cos(ss*C0)
            -math.sin(ss*A1)*math.sin(ss*A0)*math.cos(ss*B1)*math.sin(ss*B0)*math.cos(ss*C1)*math.sin(ss*C0))
        assert abs(lhs-rhs)<3e-12
        count+=1
    return count

def test_parent_aggregate_exact():
    count=0
    max_ratio=Fraction(0)
    for n in range(1,4):
        for f in all_bool_functions(n):
            g,beta=character_gauge(f,n)
            J=sum(beta,Fraction(0))
            pplus=Fraction(sum(v==1 for v in g),1<<n); pminus=1-pplus
            P=pplus*pminus
            assert P<=J/Fraction(4) if J else P==0
            for order in itertools.permutations(range(n)):
                cells=parent_cells(n,order)
                suv=Fraction(0); sd2=Fraction(0)
                rank={v:j for j,v in enumerate(order)}
                for i,m,cell in cells:
                    up,um,ap,am,pp,pm=cell_stats(g,n,cell)
                    delta=up+um
                    assert delta==Fraction(1,2**(m+1))
                    suv+=up*um
                    sd2+=delta*delta
                    free=[j for j in order if rank[j]<rank[i]]
                    Ic=sum((conditional_influence(g,n,cell,j) for j in free),Fraction(0))
                    if delta:
                        theta=up/delta
                        assert 4*theta*(1-theta)<=Ic
                    count+=1
                assert suv<=J/4
                assert sd2<Fraction(1,2)
                if J:
                    ratio=suv/J
                    max_ratio=max(max_ratio,ratio)
                    assert P*P*sd2<=J/Fraction(32)
                else:
                    assert suv==0 and P==0
    return count,max_ratio

def test_dual_local_bound():
    n_old=2; n_ext=3; Next=1<<n_ext
    C0=relation_code_C0(n_ext)
    zero=[tuple(0 for _ in range(Next))]
    P0=dual_of(C0,n_ext)
    P1=dual_of(zero,n_ext)
    assert len(P0)==2*Next and len(P1)==1<<Next
    rho=2*Next/len(P1); gamma=1-rho
    rng=random.Random(1616)
    checks=0; worst=0.0
    parent_list=parent_cells(n_old,(0,1))
    for f0 in all_bool_functions(n_old):
        f,beta=character_gauge(f0,n_old)
        fup=extend_dummy(f,n_old)
        for i,m,cell in parent_list:
            g0,g1=clone_generators(n_old,cell)
            up,um,ap,am,pp,pm=cell_stats(f,n_old,cell)
            for hcase in range(12):
                h=[1 if rng.getrandbits(1)==0 else -1 for _ in range(Next)]
                for ss in [0.07,0.2,0.5,1.0,1.8]:
                    val=abs(diff3_psi(h,g0,g1,fup,ss,P0,P1))
                    bd=triple_bound(gamma,ss,up,um,ap,am)
                    if bd<1e-15:
                        assert val<2e-10
                    else:
                        worst=max(worst,val/bd)
                        assert val<=bd+3e-9
                    checks+=1
    return checks,worst,rho

def test_multiplier_and_final_constant():
    count=0; maxratio=Fraction(0); arg=None
    for q in range(3,200,2):
        for k in range(1,q,2):
            if (q-k)%2: continue
            r=(q-k)//2
            eps=2*Fraction(1,2**q*q)*(Fraction(1,2**k*k)-Fraction(1,2**q*q))
            ratio=eps/Fraction(16*r)
            if ratio>maxratio: maxratio,arg=ratio,(q,k,r)
            assert ratio<=Fraction(11,4608)
            count+=1
    c_D=64*(2/3+1/(4*math.sqrt(2)))**2
    c_E=(11/4608)*c_D
    return count,maxratio,arg,c_D,c_E

def main():
    sc=test_scalar_factorization()
    pc,mr=test_parent_aggregate_exact()
    dc,worst,rho=test_dual_local_bound()
    mc,mult,arg,cD,cE=test_multiplier_and_final_constant()
    print('PASS')
    print(f'scalar_trig_factorizations={sc}')
    print(f'parent_cell_exact_cases={pc}')
    print(f'max_sum_parent_signmix_over_J={mr} <= 1/4')
    print(f'retained_dual_local_bound_checks={dc}')
    print(f'worst_direct_local_bound_ratio={worst:.12f}')
    print(f'test_retained_rho={rho:.12f}')
    print(f'multiplier_cases={mc}')
    print(f'max_epsilon_over_16r={mult} at {arg} = 11/4608')
    print(f'parent_D_square_constant={cD:.12f}')
    print(f'derived_central_current_constant={cE:.12f}')

if __name__=='__main__': main()
