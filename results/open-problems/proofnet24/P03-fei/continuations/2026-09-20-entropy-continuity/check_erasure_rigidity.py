#!/usr/bin/env python3
"""Exact checks for spectral-bit independence and a rare controlled bent family.
Uses the companion verify_continuity.py, which uses only the standard library.
The analytical proof is in ERASURE_RIGIDITY.md. No claim of full FEI.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import argparse,json
from verify_continuity import walsh,log_int,SCALE,LN2,interval_json,require


def binary_erasure(a,i):
    L=len(a); lo=hi=F(0)
    def xlog(k):
        if not k:return F(0),F(0)
        l,h=log_int(k);return F(k*l,SCALE),F(k*h,SCALE)
    for s in range(L):
        if s>>i&1:continue
        r,t=a[s]**2,a[s|(1<<i)]**2
        r0,r1=xlog(r);t0,t1=xlog(t);v0,v1=xlog(r+t)
        lo+=(v0-r1-t1)/(L*L);hi+=(v1-r0-t0)/(L*L)
    return lo,hi


def run():
    counts=Counter(); per_dimension=[]
    for n in range(1,5):
        L=1<<n;full=indep=0
        for mask in range(1<<L):
            f=tuple(1-2*((mask>>x)&1) for x in range(L));a=walsh(f);p=tuple(v*v for v in a)
            statuses=[];fair=0
            for i in range(n):
                beta=sum(p[s] for s in range(L) if s>>i&1)
                independent=all(p[s|(1<<i)]*L*L==beta*(p[s]+p[s|(1<<i)])
                                for s in range(L) if not(s>>i&1))
                statuses.append(independent)
                if independent and beta not in (0,L*L):
                    require(2*beta==L*L,'nondegenerate independent bit is not fair')
                    fair+=1;indep+=1
                counts['coordinate_independence_tests']+=1
            if all(statuses):
                full+=1
                require(fair%2==0,'odd-dimensional independent fair support')
                masses={x for x in p if x}
                require(masses=={L*L//(1<<fair)},'independent spectrum not flat')
                require(sum(x>0 for x in p)==1<<fair,'independent support cardinality')
            counts['exhaustive_boolean_tables']+=1
        per_dimension.append({'n':n,'fully_independent_spectra':full,'nondegenerate_independent_coordinate_occurrences':indep})
    examples=[]
    for m in (2,4,6,8,10):
        N=1<<m;L=2*N;delta=F(1,N)
        def g(y):return 1-2*(sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2))%2)
        f=tuple(g(y)*(-1 if t and y==0 else 1) for t in (0,1) for y in range(N))
        a=walsh(f)
        require(sum(a[s]*a[s] for s in range(N,L))==L*L//N,'control influence')
        require(all(a[s]==2 for s in range(N,L)),'control Fourier coefficients')
        B=binary_erasure(a,m)
        ln1=log_int(N-1);h=(F(m)-F(N-1,N)*F(ln1[1],SCALE),F(m)-F(N-1,N)*F(ln1[0],SCALE))
        MI=h[0]-B[1],h[1]-B[0]
        chi=delta/(1-delta)*(sum((F(L*L,N*N*(a[s]*a[s]+a[s+N]*a[s+N])) for s in range(N)),F(0))-1)
        require(chi==4*delta*delta/(1+4*delta*delta),'exact chi-square formula')
        require(MI[0]>0 and MI[1]<=chi/LN2[0],'mutual information bounds')
        for i in range(m):
            alpha=F(sum(a[s]*a[s] for s in range(L) if s>>i&1),L*L)
            require(alpha==F(1,2)+delta,'background coordinate influence')
        examples.append({'background_dimension':m,'dimension':m+1,'control_influence':str(delta),
                         'B_control_over_influence':interval_json((B[0]/delta,B[1]/delta)),
                         'mutual_information':interval_json(MI),'chi_square_mutual_information':str(chi),
                         'total_influence':str(m*(F(1,2)+delta)+delta)})
        counts['controlled_bent_examples']+=1
    # An exact three-variable certificate against the proposed sum-JS <= 2J shortcut.
    f=(-1,1,1,1,1,1,1,1);a=walsh(f)
    from verify_continuity import entropy
    H=entropy(a);b=binary_erasure(a,0)
    Z=(3*(H[0]-1-b[1]),3*(H[1]-1-b[0]));J=F(3,4)
    require(Z[0]>2*J,'JS counterexample certificate')
    return {'status':'PASS','counts':dict(counts),'independence_by_dimension':per_dimension,
            'controlled_bent_examples':examples,'three_variable_JS_counterexample':{'J':str(J),'sum_JS':interval_json(Z),'sum_JS_over_J':interval_json((Z[0]/J,Z[1]/J))},
            'arithmetic':'Integer Walsh transforms, rational chi-square identities, rigorous logarithm enclosures from verify_continuity.py.',
            'scope':'Exact spectral independence is rigid, but almost-independence does not yield a uniform one-coordinate erasure payment. These are not a full FEI proof or a claim of first discovery.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path('erasure_rigidity_checks.json'));args=p.parse_args()
    obj=run();args.output.write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'status':obj['status'],'counts':obj['counts']},indent=2))
