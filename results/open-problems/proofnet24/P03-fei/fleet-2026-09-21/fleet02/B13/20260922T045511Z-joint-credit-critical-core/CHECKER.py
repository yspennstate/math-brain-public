#!/usr/bin/env python3
import math

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def walsh(vals):
    a=[float(v) for v in vals]
    n=len(a)
    step=1
    while step<n:
        for i in range(0,n,2*step):
            for j in range(i,i+step):
                x,y=a[j],a[j+step]
                a[j],a[j+step]=x+y,x-y
        step*=2
    return [x/n for x in a]

def credit(a,b):
    hb=hj=delta=0.0
    for x,y in zip(a,b):
        T=(x*x+y*y)/2.0
        if T==0.0:
            continue
        post=y*y/(x*x+y*y)
        theta=(x-y)*(x-y)/(2.0*(x*x+y*y))
        hb += T*h2(post)
        hj += T*h2(theta)
        delta += T*theta
    C=hb+h2(delta)-hj
    z=(1.0-2.0*math.sqrt(max(0.0,delta*(1.0-delta))))/2.0
    return delta,C,h2(z)

checks=0
min_slack=1e100
balanced_checks=0
balanced_local_min=1e100
Ccap=6.5
for m in range(4):
    N=1<<m
    funcs=[]
    for mask in range(1<<N):
        vals=[-1 if ((mask>>i)&1) else 1 for i in range(N)]
        funcs.append((vals,walsh(vals)))
    for vals0,a in funcs:
        r0=sum(v==-1 for v in vals0)/N
        for vals1,b in funcs:
            r1=sum(v==-1 for v in vals1)/N
            delta,C,bound=credit(a,b)
            min_slack=min(min_slack,C-bound)
            checks+=1
            if abs(r0-.5)<1e-15 and abs(r1-.5)<1e-15 and delta>=.25-1e-15:
                local=Ccap*delta-1.0-h2(delta)+C
                balanced_local_min=min(balanced_local_min,local)
                balanced_checks+=1

assert min_slack >= -1e-12
assert balanced_local_min > 0.0
print("PASS")
print("child_pair_checks", checks)
print("joint_credit_min_slack", format(min_slack, ".17g"))
print("balanced_delta_ge_quarter_checks", balanced_checks)
print("balanced_exact_local_min_at_C_6p5", format(balanced_local_min, ".17g"))
print("analytic_quarter_crude_margin_lower_than", "0.005")
