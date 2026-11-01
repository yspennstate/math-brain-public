#!/usr/bin/env python3
"""Independent exact checks of the retained local obstruction and trace routes.

No author modules imported; no huge tiny-coordinate truth table claimed.
"""
from fractions import Fraction as F
from math import comb, gcd
from itertools import combinations_with_replacement, combinations
from pathlib import Path
from collections import defaultdict
import json

HERE=Path(__file__).resolve().parent

def retained(N):
    w=N+1;K=2*N**6;den=N**6;a=F(3*w,K);cuts=(-w,2,w)
    assert N%2 and w>1>a>0 and 2*a<1
    samples={}
    for z in (-1,1):
        old=w*z-N
        def numerator(r):return old*den+3*w*(r-den)
        assert numerator(0)<-w*den and numerator(K)>w*den
        rs=[0]
        for lo,hi in zip(cuts,cuts[1:]):
            r=((lo-old)*den+3*w*den)//(3*w)+1
            assert 0<=r<=K and lo*den<numerator(r)<hi*den
            rs.append(r)
        rs.append(K)
        assert all(numerator(r)%2 for r in rs)
        samples[str(z)]=[{'positive_y_bits':r,'score':str(F(numerator(r),den))}for r in rs]
    # Exact zero noise is attained; the original pivotal configuration survives.
    assert K//2==den
    for z,expected in [(-1,-1),(1,1)]:
        score=w*z-N
        label=-1 if score<-w else 1 if score<2 else -1 if score<w else 1
        assert label==expected
    bound=F(1,2**((N-1)//2)*N*((N+1)//2))
    central=F(comb(N-1,(N-1)//2),2**(N-1))
    minimum=min(abs(central*F(comb((N-1)//2,l),comb(N-1,2*l))) for l in range((N+1)//2))
    assert minimum>=bound
    out={'N':N,'fine_coordinates':K,'branch_region_samples':samples,
         'majority_coefficient_bound_exact':True}
    if N>=15:
        eps=F(1,2**N);B=N**4//72;D=N**4//36;M=N+K+1
        assert minimum>=2*eps and D>=2*B and B>=3*N*N and D>=6*N*N
        assert M+B<=3*N**6<=2**(2+6*N)
        assert 3*N*N>=8*N+5 and 6*N*N>=2*N+2
        # The exponent-only comparisons prove both errors <= epsilon^2.
        assert 7*N+5-3*N*N<=-N
        assert N+2-6*N*N<=-N
        out['explicit_dyadic_continuity_bounds_exact']=True
    return out

def generic_trace(k,N):
    # Compress fine-bit permutations, retaining their exact binomial masses.
    # Pivotal counts are obtained from the actual defining score on each orbit.
    A=2*N+1;mass=1<<(k+N);Knum=Mnum=Inum=0
    for bits in range(1<<k):
        Y=sum((1<<j)*(1 if bits>>j&1 else -1)for j in range(k))
        for r in range(N+1):
            T=2*r-N;score=A*Y+T;H=1 if score>A else -1
            g=-1 if Y==1 else 1
            assert g==(-1 if 0<score<2*A else 1)
            assert score not in (0,A,2*A)
            weight=comb(N,r);gamma=0;gf=0
            for j in range(k):
                old=1 if bits>>j&1 else -1
                newY=Y-2*old*(1<<j)
                gamma+=H!=(1 if A*newY+T>A else -1)
                gf+=g!=(-1 if newY==1 else 1)
            gamma+=r*(H!=(1 if score-2>A else -1))
            gamma+=(N-r)*(H!=(1 if score+2>A else -1))
            Knum+=weight*gamma;Mnum+=weight*gamma*g;Inum+=weight*gf
    K,M,I=F(Knum,mass),F(Mnum,mass),F(Inum,mass)
    p=F(1,1<<k);MN=F(N*comb(N-1,(N-1)//2),1<<(N-1))
    assert K==1+(k-2)*p+p*MN and M==1-2*p-p*MN and I==2*k*p
    return {'k':k,'fine_bits':N,'K':str(K),'K_times_nu_mean':str(M),
            'I_f':str(I),'trace_value':str(K-M*M/K),'trace_ratio':str((K-M*M/K)/I)}

def fluxes(weights,cuts):
    n=len(weights);size=1<<n
    scores=[sum(w*(1 if x>>j&1 else -1)for j,w in enumerate(weights))for x in range(size)]
    attained=sorted(set(scores));rank={s:i for i,s in enumerate(attained)}
    region=[sum(rank[s]>=cut for cut in cuts)for s in scores]
    counts=defaultdict(int);gamma=[0]*size;I=0;mean=0
    for lower in range(size):
        for j in range(n):
            if lower>>j&1:continue
            upper=lower|(1<<j);aa,bb=region[lower],region[upper]
            if aa!=bb:counts[aa,bb]+=1
            I+=(aa-bb)%2!=0
            if (aa>=2)!=(bb>=2):
                gamma[lower]+=1;gamma[upper]+=1
    pivot_endpoints=sum(gamma)
    mean=sum(g*(-1)**r for g,r in zip(gamma,region))
    x,y=counts[0,2],counts[1,3];o=counts[0,3]+counts[1,2];t=counts[0,1]+counts[2,3]
    K=x+y+o
    assert pivot_endpoints==2*K and mean==2*(x-y) and I==o+t
    trace=F(K*K-(x-y)**2,K*I)
    component=F(I+2*min(x,y),I)
    assert (trace<=2)==(4*x*y<=o*o+2*t*K)
    return trace,component,counts,attained

def all_flux_cases(weights):
    n=len(weights);size=1<<n
    scores=[sum(w*(1 if x>>j&1 else -1)for j,w in enumerate(weights))for x in range(size)]
    attained=sorted(set(scores));rank={s:i for i,s in enumerate(attained)}
    edges=[(rank[scores[x]],rank[scores[x|(1<<j)]])for x in range(size)for j in range(n)if not x>>j&1]
    count=0;maxtrace=F(0);maxcomp=F(0)
    for a,b,c in combinations(range(1,len(attained)),3):
        e=defaultdict(int)
        for lo,hi in edges:
            aa=(lo>=a)+(lo>=b)+(lo>=c);bb=(hi>=a)+(hi>=b)+(hi>=c)
            if aa!=bb:e[aa,bb]+=1
        x,y=e[0,2],e[1,3];o=e[0,3]+e[1,2];t=e[0,1]+e[2,3]
        K,I=x+y+o,o+t
        assert K and I
        trace=F(K*K-(x-y)**2,K*I);component=F(I+2*min(x,y),I)
        assert trace<=2 and component<=3
        assert (trace<=2)==(4*x*y<=o*o+2*t*K)
        count+=1;maxtrace=max(trace,maxtrace);maxcomp=max(component,maxcomp)
    return count,maxtrace,maxcomp

def coverage():
    result=[]
    for n in range(1,9):
        families=patterns=0
        for ws in combinations_with_replacement(range(1,9),n):
            if gcd(*ws)!=1:continue
            attainable_subsets=1
            for w in ws:attainable_subsets|=attainable_subsets<<w
            u=attainable_subsets.bit_count()
            if u>=4:families+=1;patterns+=comb(u-1,3)
        result.append({'dimension':n,'families':families,'triple_cuts':patterns})
    return result

def main():
    author=json.loads((HERE/'three_crossing_trace_k_route_obstructions.json').read_text())
    generic=[generic_trace(row['k'],row['fine_bits'])for row in author['truth_checks']]
    assert generic==author['truth_checks']
    rows=coverage();exhaustive=json.loads((HERE/'exhaustive_small_weights_three_crossing_results.json').read_text())
    assert rows==exhaustive['dimensions']
    assert sum(r['families']for r in rows)==exhaustive['families']==12321
    assert sum(r['triple_cuts']for r in rows)==exhaustive['triple_cuts']==47693379
    checked=maxtrace=maxcomp=0
    for n in range(2,5):
        for ws in combinations_with_replacement(range(1,9),n):
            if gcd(*ws)!=1:continue
            cases,tr,cr=all_flux_cases(ws);checked+=cases;maxtrace=max(maxtrace,tr);maxcomp=max(maxcomp,cr)
    for ws in ((2,2,2,2,3),(1,1,2,3,5,8),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7,8),(1,1,1,1,1,1,1,8)):
        cases,tr,cr=all_flux_cases(ws);checked+=cases;maxtrace=max(maxtrace,tr);maxcomp=max(maxcomp,cr)
    witnesses={}
    for label,row in (('trace',exhaustive['max_trace_ratio']),('component',exhaustive['max_component_ratio'])):
        tr,cr,e,attained=fluxes(row['weights'],row['cut_indices'])
        assert str(tr if label=='trace'else cr)==row['ratio']
        witnesses[label]={'trace_ratio':str(tr),'component_ratio':str(cr),
                          'unnormalized_undirected_flux':{str(k):v for k,v in e.items()}}
    p,q=F(3,4),F(1,4)
    minor=p*q*q*q-p*q*p*p
    assert str(minor)==author['score_semigroup_TP2_minor']=='-3/32'
    # Asymptotic generic counterexample's exact coefficient formulas and dyadic bounds.
    asymptotic=[]
    for k in range(2,7):
        N=4**k+1;prob=F(1,2**k);MN=F(N*comb(N-1,(N-1)//2),2**(N-1))
        K=1+(k-2)*prob+prob*MN;M=1-2*prob-prob*MN;I=2*k*prob
        trace=K-M*M/K
        assert trace>=F(2,3) and trace/I>=F(1,3*k*prob)
        asymptotic.append({'k':k,'N':N,'ratio_at_least':str(F(1,3*k*prob))})
    report={'status':'PASS: exact method obstructions and finite coverage; retained middle trace unproved',
      'full_retention_exact_grid_and_coefficient_checks':[retained(N)for N in range(3,82,2)],
      'common_score_non_crossing_trace_truth_checks':generic,'asymptotic_fraction_checks':asymptotic,
      'score_ordered_noise_negative_TP2_minor':str(minor),
      'all_47M_family_and_pattern_counts_independently_reconstructed':rows,
      'independent_direct_edge_subset_patterns_checked':checked,
      'subset_max_trace_ratio':str(maxtrace),'subset_max_component_ratio':str(maxcomp),
      'exact_reported_witness_checks':witnesses}
    (HERE/'three_crossing_routes_ant_independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k]for k in ('status','independent_direct_edge_subset_patterns_checked',
        'subset_max_trace_ratio','subset_max_component_ratio')},indent=2))

if __name__=='__main__':main()
