from fractions import Fraction as F
from itertools import permutations, combinations
from math import factorial
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
base = runpy.run_path(str(ROOT / 'artifacts/hard7_2026-09-18/HARD7-03/theta_reoptimization_20260919T1824Z.py'), run_name='hard703_base')

# Exact later correction formulas, self-contained.
Uvec=(F(1),F(0),F(0)); Vvec=(F(0),F(1),F(0)); Wvec=(F(0),F(0),F(1))
ORDER=(Uvec,tuple(Uvec[i]+Vvec[i] for i in range(3)),tuple(Uvec[i]+Vvec[i]+Wvec[i] for i in range(3)))
def vadd(*vs): return tuple(sum(v[i] for v in vs) for i in range(3))
def vscale(c,v): return tuple(c*x for x in v)
def gap_cone_integral(g):
    rates=(F(3)-g[0],F(2)-g[1],F(1)-g[2]); assert all(r>0 for r in rates); return F(1)/(rates[0]*rates[1]*rates[2])
def max_shift(avec,rank,labels): return avec[max(labels,key=lambda x:rank[x])]
def high_minus_rank_gap_integral(g,rank):
    rates=(F(3)-g[0],F(2)-g[1],F(1)-g[2]); base=F(1)/(rates[0]*rates[1]*rates[2])
    return F(0) if rank==2 else base*sum(F(1,rates[j]) for j in range(rank+1,3))
def edge_boundary_transforms(t):
    a=F(1)-t;b=F(2)-t;c=F(3)-t;T0=Ta=Tb=F(0)
    for perm in permutations((-1,0,1)):
        rank={lab:i for i,lab in enumerate(perm)};avec={perm[r]:ORDER[r] for r in range(3)};s0=ORDER[2];s1=avec[0] if rank[0]>rank[1] else avec[1];s2=avec[1];r1=max(rank[0],rank[1]);e1=vadd(s2,vscale(-a,s1));e0=vadd(s2,vscale(-a,s0));ec=vadd(s2,s1,vscale(-b,s0))
        T0+=(gap_cone_integral(e1)-gap_cone_integral(e0))/(a*b)+gap_cone_integral(ec)/(b*c)
        Ta+=high_minus_rank_gap_integral(e0,r1)/b-a*gap_cone_integral(e0)/(b*b)+gap_cone_integral(ec)/c
        Tb+=gap_cone_integral(e0)/b-(F(1)+F(1,c))*gap_cone_integral(ec)/c-high_minus_rank_gap_integral(ec,r1)/c
    return T0,Ta,Tb
def near_boundary_T0(t):
    b=F(2)-t;c=F(3)-t;d=F(4)-t;total=F(0)
    for perm in permutations((-1,0,1)):
        rank={lab:i for i,lab in enumerate(perm)};avec={perm[r]:ORDER[r] for r in range(3)};sU=max_shift(avec,rank,(-1,0));s0=ORDER[2];s1=max_shift(avec,rank,(0,1));s2=avec[1];g1=vadd(sU,s1,vscale(-b,s0));g2=vadd(sU,s2,vscale(-b,s0));g3=vadd(sU,s1,s2,vscale(-c,s0));total+=(gap_cone_integral(g1)+gap_cone_integral(g2))/(b*c)-F(2)*gap_cone_integral(g3)/(c*d)
    return total
def center_boundary_T0(t):
    total=F(0);zero=(F(0),F(0),F(0))
    for perm in permutations((-1,0,1)):
        rank={lab:i for i,lab in enumerate(perm)};avec={perm[r]:ORDER[r] for r in range(3)};sU=avec[-1];s0=ORDER[2];s1=max_shift(avec,rank,(0,1));ell1=max_shift(avec,rank,(-1,0));ell2=avec[1];dens=((F(1),s0,1),(F(1),s1,1),(F(-2),vadd(s0,s1),2));lower=((F(1),zero,0),(F(-1),ell1,1),(F(-1),ell2,1),(F(1),vadd(ell1,ell2),2));val=F(0)
        for cd,sd,n in dens:
            for cl,sl,k in lower:
                lam=F(n+k+1)-t;val+=cd*cl*gap_cone_integral(vadd(sU,sd,sl,vscale(-lam,s0)))/lam
        assert val>0;total+=val
    return total
def double_outrunner_T(t):
    b=F(2)-t;total=F(0)
    for perm in permutations((-1,0,1)):
        rank={lab:i for i,lab in enumerate(perm)};avec={perm[r]:ORDER[r] for r in range(3)};sm=max_shift(avec,rank,(-1,0));s0=ORDER[2];sp=max_shift(avec,rank,(0,1));shifts=(sm,s0,sp);outer=vadd(avec[-1],avec[1]);val=F(0)
        for r in range(1,4):
            for inds in combinations(range(3),r):
                coeff=F(((-1)**(r+1))*r,b+r);sexp=vadd(*(shifts[i] for i in inds));val+=coeff*gap_cone_integral(vadd(outer,sexp,vscale(-(b+r),s0)))
        assert val>0;total+=val
    return total
def full_U4(t):
    q=F(1)-t;a=q;b=F(2)-t;c=F(3)-t;kap=t/(b*c);u=base['U4_allpairs'](t)
    T0e,Tae,Tbe=edge_boundary_transforms(t);ce=t/(a*b)*(T0e-Tae)-kap*(T0e-Tbe)
    tn=near_boundary_T0(t);tc=center_boundary_T0(t);cn=t*tn*(F(1,b*b)-F(1,c*c));cc=t*tc*(F(1,b*b)-F(1,c*c))
    D=F(2)*t*((F(1,b*b)-F(1,c*c))+(F(1,b*b*b)-F(1,c*c*c)));cb=D*double_outrunner_T(t)
    return u-(F(2)*ce+F(2)*(cn+cc)+cb)/q,(ce,cn,cc,cb)

# Counterexample-first exact 5! atlas.
YLABS=(-2,-1,0,1,2)
def Srank(rank,e): return max(rank[z] for z in YLABS if abs(z-e)<=1)
def sgn(a,b): return '+' if a>b else ('0' if a==b else '-')
def patt(rank,d): return sgn(Srank(rank,d-1),Srank(rank,d)),sgn(Srank(rank,d+1),Srank(rank,d))
counts={d:{} for d in (0,1,2)}
for perm in permutations(YLABS):
    rank={lab:i for i,lab in enumerate(perm)}
    for d in (0,1,2): counts[d][patt(rank,d)]=counts[d].get(patt(rank,d),0)+1
    p2=patt(rank,2)
    assert (p2==('+','-')) == (rank[0]>rank[1]>rank[2])
    assert (p2==('+','0')) == (rank[0]>rank[2]>rank[1])
    p1=patt(rank,1); M=max(rank[1],rank[2])
    assert (p1==('+','-')) == (rank[-1]>rank[0]>M)
    assert (p1==('+','0')) == (rank[-1]>M>rank[0])
    p0=patt(rank,0); R=max(rank[0],rank[1],rank[2]); L=max(rank[-2],rank[-1],rank[0])
    assert (p0==('+','-')) == (rank[-2]>rank[-1]>R)
    assert (p0==('-','+')) == (rank[2]>rank[1]>L)
    M0=max(rank[0],rank[1]); L0=max(rank[-1],rank[2])
    assert (p0==('+','0')) == (rank[-2]>M0>L0)
    Mr=max(rank[-1],rank[0]); Lr=max(rank[-2],rank[1])
    assert (p0==('0','+')) == (rank[2]>Mr>Lr)
    T=max(rank[-1],rank[0],rank[1])
    assert (p0==('+','+')) == (rank[-2]>T and rank[2]>T)
expected={
0:{('+','+'):12,('+','-'):6,('+','0'):12,('-','+'):6,('-','0'):24,('0','+'):12,('0','-'):24,('0','0'):24},
1:{('+','-'):10,('+','0'):20,('-','0'):30,('0','-'):30,('0','0'):30},
2:{('+','-'):20,('+','0'):20,('0','-'):40,('0','0'):40}}
assert counts==expected
assert sum(sum(counts[d].values()) for d in (0,1,2))==360
# Remaining nonpositive boundary sectors are exact baseline sectors.
for ttest in (F(1,5),F(1,2),F(4,5)):
    b=F(2)-ttest;c=F(3)-ttest
    assert ttest*(F(1,b)-F(1,c)) == ttest/(b*c)

# Reconstruct latest point exactly then reoptimize theta.
told=F(57343,100000); uold,_=full_U4(told)
latest=F(44104948057835881726074263653049462747385972189701092886716639414717371037400000000000000000000,54442695413156570473578553858609910677406260157304013873650482583987300880543061947950013587)
assert uold==latest

th=F(286501,500000); unew,parts=full_U4(th)
Aold=F(291978907,100000000); Lold=F(25000000,291978907)
Anew=F(2919788131,1000000000); assert Anew<Aold
x=F(4)*th*Anew; S32=sum(x**k/F(factorial(k)) for k in range(33)); margin=S32-unew; assert margin>0
Lnew=F(1)/(F(4)*Anew); assert Lnew==F(250000000,2919788131) and Lnew>Lold

print('HARD7-03 exact four-step sign-atlas closure and theta reoptimization')
print('counts_d0 =',counts[0]);print('counts_d1 =',counts[1]);print('counts_d2 =',counts[2])
print('old_theta =',told);print('old_U4_exact =',uold);print('old_U4_matches_2123Z =',uold==latest)
print('new_theta =',th);print('new_U4_exact =',unew)
print('later_corrections_new =',parts)
print('A_old =',Aold);print('A_new =',Anew);print('S32_minus_U_new =',margin)
print('L_old =',Lold);print('L_new =',Lnew);print('metric_gain =',Lnew-Lold)
print('new_U4_float = %.15f'%float(unew));print('A_new_float = %.15f'%float(Anew));print('margin_float = %.15e'%float(margin));print('L_new_float = %.15f'%float(Lnew));print('metric_gain_float = %.15e'%float(Lnew-Lold))
print('ALL_EXACT_CHECKS_PASS = True')
