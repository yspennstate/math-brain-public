#!/usr/bin/env python3
import itertools, math

C_LIVE = 6.521851214
CS = (5.1, C_LIVE)

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1.0-x)*math.log2(1.0-x)

def T(d):
    if d == 0.0:
        return 4.0
    return (2*h2(d) - 0.5*h2(4*d*(1-d)))/d

def Q_peer(d):
    b = 1-2*d
    m = (1+b*b)/2
    return (2-m-m*h2(b*b/(1+b*b))+m*h2(d*d/m))/d

def fwht(vals):
    a = [float(x) for x in vals]
    h = 1
    N = len(a)
    while h < N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return [x/N for x in a]

def HI(vals):
    c = fwht(vals)
    H = I = 0.0
    for s,x in enumerate(c):
        p = x*x
        if p:
            H -= p*math.log2(p)
        I += s.bit_count()*p
    return H,I

def balanced_tables(n):
    N = 1 << n
    out=[]
    for neg in itertools.combinations(range(N),N//2):
        ss=set(neg)
        out.append([-1 if i in ss else 1 for i in range(N)])
    return out

def selector_tables(n):
    N=1<<n
    out=[]
    for mask in range(1<<N):
        vals=[-1 if (mask>>i)&1 else 1 for i in range(N)]
        d=sum(v==-1 for v in vals)/N
        if 0<d<1:
            out.append(vals)
    return out

def pm_and(a,f):
    return -1 if a == -1 and f == -1 else 1

def selector_suspend(a,f):
    m=(len(a)).bit_length()-1
    n=(len(f)).bit_length()-1
    vals=[]
    for idx in range(1<<(m+n+1)):
        ia=idx & ((1<<m)-1)
        jf=(idx>>m) & ((1<<n)-1)
        z=-1 if ((idx>>(m+n))&1) else 1
        vals.append(z*pm_and(a[ia],f[jf]))
    return vals

def tensor(f,g):
    nf=(len(f)).bit_length()-1
    ng=(len(g)).bit_length()-1
    vals=[]
    for idx in range(1<<(nf+ng)):
        i=idx & ((1<<nf)-1)
        j=(idx>>nf) & ((1<<ng)-1)
        vals.append(f[i]*g[j])
    return vals

# Exact-formula numerical regression over all nonconstant selectors up to 3 bits
# and every balanced core up to 3 bits.
formula_cases=0
max_formula_error=0.0
min_direct_slack=1e99
cores={n:balanced_tables(n) for n in range(1,4)}
for m in range(1,4):
    for a in selector_tables(m):
        Ha,Ia=HI(a)
        d=sum(v==-1 for v in a)/len(a)
        for n in range(1,4):
            for f in cores[n]:
                Hf,If=HI(f)
                Hg,Ig=HI(selector_suspend(a,f))
                for C in CS:
                    direct=C*(Ig-1)-Hg
                    rhs=0.5*(C*Ia-Ha)+d*(C*(If-1)-Hf)+d*(C-T(d))
                    max_formula_error=max(max_formula_error,abs(direct-rhs))
                    if C*Ia-Ha >= -1e-12 and C*(If-1)-Hf >= -1e-12:
                        min_direct_slack=min(min_direct_slack,direct)
                    formula_cases += 1

# Tensor identity on all balanced pairs up to 3 bits.
tensor_cases=0
max_tensor_error=0.0
for n1 in range(1,4):
    for n2 in range(1,4):
        for f in cores[n1]:
            Hf,If=HI(f)
            for g in cores[n2]:
                Hg,Ig=HI(g)
                Hp,Ip=HI(tensor(f,g))
                lhs=C_LIVE*(Ip-1)-Hp
                rhs=(C_LIVE*(If-1)-Hf)+(C_LIVE*(Ig-1)-Hg)+C_LIVE
                max_tensor_error=max(max_tensor_error,abs(lhs-rhs))
                tensor_cases += 1

# Check algebraic scalar identification numerically on dyadic points.
q_cases=0
max_q_error=0.0
for k in range(2,11):
    N=1<<k
    for j in range(1,N//2+1):
        d=j/N
        max_q_error=max(max_q_error,abs(T(d)-Q_peer(d)))
        q_cases += 1

# Floating diagnostic only; the rigorous <5.1 theorem is imported from account04/B17.
best=(-1.0,None)
for j in range(1,1000001):
    d=0.5*j/1000000
    v=T(d)
    if v>best[0]:
        best=(v,d)

assert max_formula_error < 1e-11
assert max_tensor_error < 1e-11
assert max_q_error < 1e-11
assert best[0] < 5.1
print(f"formula_cases={formula_cases}")
print(f"max_formula_error={max_formula_error:.17g}")
print(f"min_direct_slack_when_components_safe={min_direct_slack:.17g}")
print(f"tensor_cases={tensor_cases}")
print(f"max_tensor_error={max_tensor_error:.17g}")
print(f"scalar_identity_dyadic_cases={q_cases}")
print(f"max_abs_T_minus_Q={max_q_error:.17g}")
print(f"diagnostic_grid_max_T={best[0]:.15f}")
print(f"diagnostic_grid_argmax_d={best[1]:.9f}")
print("status=PASS")
