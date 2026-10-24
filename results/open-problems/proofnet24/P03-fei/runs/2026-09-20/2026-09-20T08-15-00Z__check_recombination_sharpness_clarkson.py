#!/usr/bin/env python3
import math, json

SVALS = [1.0, 1.25, 1.5, 1.75]
TOL = 2e-12

def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    inv = 1.0/n
    return [x*inv for x in a]

def entropy(a):
    ans = 0.0
    for x in a:
        p = x*x
        if p:
            ans -= p*math.log2(p)
    return ans

def m_s(a,s):
    return sum(abs(x)**s for x in a)

def m2_derivative(a):
    ans=0.0
    for x in a:
        y=abs(x)
        if y:
            ans += y*y*math.log(y)
    return ans

def pairs(a,n,i):
    A=[]; B=[]
    for S in range(1<<n):
        if ((S>>i)&1)==0:
            A.append(a[S])
            B.append(a[S|(1<<i)])
    return A,B

def children_from_pairs(A,B):
    return ([x+y for x,y in zip(A,B)],
            [x-y for x,y in zip(A,B)])

def js(p,q):
    ans=0.0
    for x,y in zip(p,q):
        m=(x+y)/2
        if x:
            ans += 0.5*x*math.log2(x/m)
        if y:
            ans += 0.5*y*math.log2(y/m)
    return ans

def bent_value(x,n):
    e=0
    for j in range(0,n,2):
        e ^= ((x>>j)&1) & ((x>>(j+1))&1)
    return -1 if e else 1

def psi(r):
    if r == 0.0:
        return 0.5
    return 0.5*math.log2(2/(1+r)) + 0.5*r*math.log2(2*r/(1+r))

# 1. Exhaustive Clarkson deficit and endpoint identity through dimension 4.
min_deficit={str(s): float("inf") for s in SVALS}
max_endpoint_error=0.0
function_count=0
coordinate_count=0
for n in range(1,5):
    N=1<<n
    for mask in range(1<<N):
        vals=[-1 if ((mask>>x)&1) else 1 for x in range(N)]
        a=fwht(vals)
        H=entropy(a)
        function_count += 1
        for i in range(n):
            A,B=pairs(a,n,i)
            ap,am=children_from_pairs(A,B)
            Hp,Hm=entropy(ap),entropy(am)
            entropy_dec=H-(Hp+Hm)/2
            dprime=m2_derivative(a)-(m2_derivative(ap)+m2_derivative(am))/2
            endpoint_dec=-(2/math.log(2))*dprime
            max_endpoint_error=max(max_endpoint_error,abs(entropy_dec-endpoint_dec))
            for s in SVALS:
                D=m_s(a,s)-(m_s(ap,s)+m_s(am,s))/2
                min_deficit[str(s)]=min(min_deficit[str(s)],D)
                if D < -TOL:
                    raise AssertionError(("Clarkson deficit",n,mask,i,s,D))
            coordinate_count += 1

# 2. Bent-background one-point pair: direct Walsh JS vs exact two-mass formula.
sharp_rows=[]
max_js_formula_error=0.0
sharp_upper=2/math.log(2)
for n in range(2,13,2):
    N=1<<n
    g=[bent_value(x,n) for x in range(N)]
    h=g[:]
    h[0]*=-1
    ag,ah=fwht(g),fwht(h)
    pg=[x*x for x in ag]
    ph=[x*x for x in ah]
    J=js(pg,ph)
    delta=1.0/N
    t=1/math.sqrt(N)
    rm=(1-2*t)**2
    rp=(1+2*t)**2
    J_formula=((1+t)/2)*psi(rm)+((1-t)/2)*psi(rp)
    max_js_formula_error=max(max_js_formula_error,abs(J-J_formula))
    ratio=J/delta
    if ratio > sharp_upper + TOL:
        raise AssertionError(("JS upper",n,ratio,sharp_upper))
    bent_mag_err=max(abs(abs(x)-1/math.sqrt(N)) for x in ag)
    mismatches=sum(1 for x,y in zip(g,h) if x!=y)
    if mismatches != 1 or bent_mag_err > TOL:
        raise AssertionError(("bent/mismatch",n,mismatches,bent_mag_err))
    sharp_rows.append({
        "n":n, "delta":delta, "js":J, "js_over_j":ratio,
        "gap_to_2_over_ln2":sharp_upper-ratio,
        "formula_error":abs(J-J_formula)
    })

# Formula-only approach to the sharp constant farther out.
sharp_formula_rows=[]
for n in range(4,21,2):
    N=2.0**n
    t=1/math.sqrt(N)
    J=((1+t)/2)*psi((1-2*t)**2)+((1-t)/2)*psi((1+2*t)**2)
    ratio=J*N
    sharp_formula_rows.append({
        "n":n,
        "js_over_j":ratio,
        "gap_to_2_over_ln2":sharp_upper-ratio
    })

# 3. One-point obstruction for every fixed s<2.
def onepoint_M(n,s):
    N=2.0**n
    return (1-2/N)**s + (N-1)*(2/N)**s

def onepoint_D(n,s):
    return onepoint_M(n,s)-0.5*(1+onepoint_M(n-1,s))

onepoint_rows=[]
for s in SVALS:
    for n in [8,16,32,40]:
        N=2.0**n
        D=onepoint_D(n,s)
        inf_i=2/N
        local_ratio=D/inf_i
        predicted_scale=(2**(s-1)-2**(2*s-3))
        scaled=local_ratio/(N**(2-s))
        global_ratio=(onepoint_M(n,s)-1)/(2*n/N)
        if D < -TOL:
            raise AssertionError(("onepoint deficit",s,n,D))
        onepoint_rows.append({
            "s":s, "n":n,
            "local_deficit_over_influence":local_ratio,
            "scaled_local_ratio":scaled,
            "predicted_scaled_limit":predicted_scale,
            "global_excess_over_total_influence":global_ratio
        })

out={
    "status":"PASS",
    "exhaustive_boolean_functions_dim_1_to_4":function_count,
    "exhaustive_coordinate_cases_dim_1_to_4":coordinate_count,
    "s_values":SVALS,
    "min_clarkson_deficit":min_deficit,
    "max_endpoint_entropy_identity_error":max_endpoint_error,
    "sharp_recombination_limit_2_over_ln2":sharp_upper,
    "max_direct_walsh_vs_exact_js_formula_error":max_js_formula_error,
    "bent_one_point_direct_rows":sharp_rows,
    "bent_one_point_formula_rows":sharp_formula_rows,
    "onepoint_fixed_s_rows":onepoint_rows
}
print(json.dumps(out,indent=2,sort_keys=True))
