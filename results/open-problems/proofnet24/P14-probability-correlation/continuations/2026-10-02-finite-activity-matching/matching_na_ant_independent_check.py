"""Independent exact NA audit using covering block partitions.

Matching masses are computed in a raw nilpotent polynomial basis, not via
the forced-Y representation. Every monotone event on each side of every
covering bipartition is checked by exact integer contingency arithmetic.
Covering partitions suffice because ignored coordinates can be added to
one block without changing either event. No author helper imports.
"""
from fractions import Fraction as Q
from functools import reduce
from itertools import product
from math import lcm
from operator import mul
from pathlib import Path
import json
import numpy as np


def prod(items):
    return reduce(mul,items,1)


def integerize(weights):
    denominator=lcm(*(x.denominator for x in weights))
    return [int(x*denominator) for x in weights]


def core_data(columns,core):
    b,c,d=columns
    p,q,r=core
    B,J=b+c+d,b*c*d
    S=1+p+q+r+p*q+p*r+q*r
    L=b*c+b*d+c*d+p*d*(b+c)+q*c*(b+d)+r*b*(c+d)
    return B,J,S,L


def raw_matching_law(rows,columns,core,activities):
    B,J,S,L=core_data(columns,core)
    def multiply(v,w):
        a,b,c=v
        d,e,f=w
        return (a*d,a*e+b*d,a*f+c*d+2*B*b*e)
    def terminal(x):
        return (1+B*x,x*x,x**3)
    n=len(activities)
    weights=[]
    for mask in range(1<<n):
        v=(Q(1),Q(0),Q(0))
        factor=Q(1)
        for i,w in enumerate(activities):
            a,b=rows[2*i:2*i+2]
            if mask>>i&1:
                group=terminal(a+b)
                factor*=w
            else:
                group=multiply(terminal(a),terminal(b))
            v=multiply(v,group)
        for a in rows[2*n:]:
            v=multiply(v,terminal(a))
        c0,cP,cQ=v
        weights.append(factor*(S*c0+L*cP+J*cQ))
    return weights


def literal_or_law(rows,columns,core,activities):
    B,J,S,L=core_data(columns,core)
    d=lambda x:1+B*x
    alpha=lambda x:x*x/d(x)
    gamma=lambda x:x**3/d(x)**2
    U,G=sum(map(alpha,rows)),sum(map(gamma,rows))
    A=S+L*U+J*G+B*J*U*U
    M,K=L+2*B*J*U,2*B*J
    n=len(activities)
    theta,t,h=[],[],[]
    for i,w in enumerate(activities):
        a,b=rows[2*i:2*i+2]
        de=alpha(a+b)-alpha(a)-alpha(b)
        ep=gamma(a+b)-gamma(a)-gamma(b)
        c=d(a+b)/(d(a)*d(b))
        th=c*w/(1+c*w)
        assert 0<de<1/(B*B) and 0<ep/de<2/B
        theta.append(th)
        t.append(de*th)
        h.append(M+J*ep/de+B*J*de)
    assert min(h)**2>K*A and max(h)<2*min(h)
    y={0:A}
    for i in range(n):
        y[1<<i]=h[i]*t[i]
        for j in range(i):
            y[(1<<i)|(1<<j)]=K*t[i]*t[j]
    YZ=sum(y.values())
    bernoulli=[prod(theta[i] if mask>>i&1 else 1-theta[i] for i in range(n)) for mask in range(1<<n)]
    result=[Q(0)]*(1<<n)
    for forced,weight in y.items():
        for random_mask,mass in enumerate(bernoulli):
            result[forced|random_mask]+=weight*mass/YZ
    return result,[y.get(i,Q(0)) for i in range(1<<n)]


EVENTS={0:np.array([[False],[True]],dtype=object)}
MASKS={0:[0,1]}


def monotone_events(n):
    if n not in EVENTS:
        previous=monotone_events(n-1)
        half=1<<(n-1)
        masks=[]
        for low in MASKS[n-1]:
            for high in MASKS[n-1]:
                if low&~high==0:
                    masks.append(low|(high<<half))
        MASKS[n]=masks
        # Remove the two constant events; their covariance is identically zero.
        full=(1<<(1<<n))-1
        EVENTS[n]=np.array([[int(mask>>i&1) for i in range(1<<n)]
                            for mask in masks if mask not in (0,full)],dtype=object)
    return EVENTS[n]


def all_event_na(weights):
    n=(len(weights)-1).bit_length()
    Z=sum(weights)
    comparisons=0
    if n<2:
        return 0
    for left in range(1,(1<<n)-1):
        if not left&1:
            continue # Covariance is symmetric; include each partition once.
        li=[i for i in range(n) if left>>i&1]
        ri=[i for i in range(n) if not left>>i&1]
        table=np.zeros((1<<len(li),1<<len(ri)),dtype=object)
        for outcome,weight in enumerate(weights):
            a=sum(((outcome>>i)&1)<<j for j,i in enumerate(li))
            b=sum(((outcome>>i)&1)<<j for j,i in enumerate(ri))
            table[a,b]+=weight
        E,F=monotone_events(len(li)),monotone_events(len(ri))
        marginal_e=E@table.sum(axis=1)
        marginal_f=F@table.sum(axis=0)
        joint=(E@table)@F.T
        for i in range(len(E)):
            for j in range(len(F)):
                assert marginal_e[i]*marginal_f[j]>=Z*joint[i,j],(n,left,i,j)
                comparisons+=1
    return comparisons


def all_conditionings(weights):
    n=(len(weights)-1).bit_length()
    laws=checks=0
    for assignment in product((-1,0,1),repeat=n):
        free=[i for i,v in enumerate(assignment) if v==-1]
        conditional=[0]*(1<<len(free))
        for outcome,weight in enumerate(weights):
            if all(v==-1 or (outcome>>i&1)==v for i,v in enumerate(assignment)):
                local=sum(((outcome>>i)&1)<<j for j,i in enumerate(free))
                conditional[local]+=weight
        if sum(conditional)>0:
            checks+=all_event_na(conditional)
            laws+=1
    return laws,checks


def main():
    rows=[Q(j+1,j+2) for j in range(12)]+[Q(0),Q(7,3)]
    columns=list(map(Q,[1,2,4]))
    core=list(map(Q,[1,3,2]))
    activities=[Q(1,100),Q(100),Q(2,3),Q(7,5),Q(11),Q(13,17)]
    graph=raw_matching_law(rows,columns,core,activities)
    represented,y=literal_or_law(rows,columns,core,activities)
    assert represented==[w/sum(graph) for w in graph]
    conditional_laws,event_checks=all_conditionings(integerize(graph))
    y_checks=all_event_na(integerize(y))
    report=dict(status="PASS",arithmetic="Exact rational laws and integer contingency comparisons",
                matching_edges=6,matching_patterns=64,OR_identity_exact=True,
                conditional_laws=conditional_laws,all_monotone_event_comparisons=event_checks,
                forced_law_monotone_event_comparisons=y_checks,
                monotone_event_counts={str(n):len(MASKS[n]) for n in sorted(MASKS)},
                abstract_lemma_cases=[])
    for t in ([Q(1),Q(2),Q(3),Q(4),Q(5),Q(6)],
              [Q(1),Q(0),Q(1),Q(0),Q(2),Q(3)]):
        h=list(map(Q,[2,2,4,3,2,4]))
        A,K=Q(4),Q(1)
        assert min(h)**2==K*A and max(h)==2*min(h)
        weights=[Q(0)]*64
        weights[0]=A
        for i in range(6):
            weights[1<<i]=h[i]*t[i]
            for j in range(i):
                weights[(1<<i)|(1<<j)]=K*t[i]*t[j]
        checks=all_event_na(integerize(weights))
        report["abstract_lemma_cases"].append(dict(t=list(map(str,t)),h=list(map(str,h)),
                                                 both_hypotheses_at_equality=True,event_comparisons=checks))
    # Independently factor the actual diagonal generating polynomial, using
    # raw forest coefficients rather than the claimed theta discriminant.
    tiny=[Q(1,100)]*10
    diagonal_law=raw_matching_law(tiny,[Q(1)]*3,[Q(0)]*3,[Q(1)]*5)
    coefficients=[sum(w for mask,w in enumerate(diagonal_law) if mask.bit_count()==k) for k in range(6)]
    a=Q(1,100)
    c=(1+6*a)/(1+3*a)**2
    divisor=[Q(1),3*c,3*c*c,c**3]
    quotient=[coefficients[0]]
    quotient.append(coefficients[1]-divisor[1]*quotient[0])
    quotient.append(coefficients[2]-divisor[1]*quotient[1]-divisor[2]*quotient[0])
    convolution=[sum(quotient[i]*divisor[k-i] for i in range(3) if 0<=k-i<4) for k in range(6)]
    assert convolution==coefficients
    discriminant=quotient[1]**2-4*quotient[0]*quotient[2]
    D0=(1+3*a)**10
    scaled_discriminant=discriminant/(D0*D0*c*c)
    assert scaled_discriminant==Q(-553191,1580777123645)<0
    report["non_real_stability_witness"]=dict(
        raw_diagonal_coefficients=list(map(str,coefficients)),
        factorization="(1+c*w)^3 times an exactly extracted quadratic",
        quadratic_coefficients=list(map(str,quotient)),
        actual_quadratic_discriminant=str(discriminant),
        theta_quadratic_discriminant=str(scaled_discriminant),
        independently_factored_from_raw_forest_law=True)
    Path(__file__).with_name("matching_na_ant_independent_checks.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
