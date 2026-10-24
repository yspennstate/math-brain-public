from itertools import combinations
import sympy as sp

def partitions_response(n, edges, terminals=(0,1,2)):
    m=len(edges)
    d=a=b=c=t=0
    for mask in range(1<<m):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(x,y):
            x,y=find(x),find(y)
            if x==y:
                return False
            parent[y]=x
            return True
        ok=True
        for j,(u,v) in enumerate(edges):
            if (mask>>j)&1:
                if not union(u,v):
                    ok=False
                    break
        if not ok:
            continue
        r=[find(x) for x in terminals]
        eq01=r[0]==r[1]
        eq02=r[0]==r[2]
        eq12=r[1]==r[2]
        if not (eq01 or eq02 or eq12):
            d+=1
        elif eq01 and not eq02:
            a+=1
        elif eq02 and not eq01:
            b+=1
        elif eq12 and not eq01:
            c+=1
        elif eq01 and eq02:
            t+=1
        else:
            raise RuntimeError("bad partition")
    return d,a,b,c,t

# Symbolic K4 = terminal triangle u,v,w plus Steiner star p,q,r.
u,v,w,p,q,r=sp.symbols("u v w p q r", positive=True)
weighted_edges=[
    (0,1,u),(0,2,v),(1,2,w),
    (0,3,p),(1,3,q),(2,3,r)
]
vals=[sp.Integer(0)]*5
for mask in range(1<<6):
    parent=list(range(4))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(x,y):
        x,y=find(x),find(y)
        if x==y: return False
        parent[y]=x
        return True
    mon=sp.Integer(1); ok=True
    for j,(x,y,z) in enumerate(weighted_edges):
        if (mask>>j)&1:
            if not union(x,y):
                ok=False; break
            mon*=z
    if not ok: continue
    rr=[find(i) for i in (0,1,2)]
    e01=rr[0]==rr[1]; e02=rr[0]==rr[2]; e12=rr[1]==rr[2]
    if not(e01 or e02 or e12): idx=0
    elif e01 and not e02: idx=1
    elif e02 and not e01: idx=2
    elif e12 and not e01: idx=3
    elif e01 and e02: idx=4
    else: raise RuntimeError
    vals[idx]+=mon
d,a,b,c,t=map(sp.factor, vals)
D=1+p+q+r
assert sp.expand(d-D)==0
assert sp.expand(a-(u*D+p*q))==0
assert sp.expand(b-(v*D+p*r))==0
assert sp.expand(c-(w*D+q*r))==0
tau=sp.factor(d*t-a*b-a*c-b*c)
assert sp.expand(tau-p*q*r)==0

print("K4_RESPONSE_FORMULAS_PASS")
print("d =", sp.factor(d))
print("a =", sp.factor(a))
print("b =", sp.factor(b))
print("c =", sp.factor(c))
print("tau =", tau)

# Synthesis algebra audit.
lam,x,y,z,rho=sp.symbols("lam x y z rho", positive=True)
A=lam*x; B=lam*y; C=lam*z
pp=A*B/rho; qq=A*C/rho; rr=B*C/rho
DD=1+pp+qq+rr
rel=lam**3*x*y*z-rho*lam**2*(x*y+x*z+y*z)-rho**2
# DD = ABC/rho^2 modulo rel
assert sp.factor((DD-A*B*C/rho**2)*rho**2 + rel)==0
# Pair responses modulo relation via substitution DD -> ABC/rho^2:
DDtarget=A*B*C/rho**2
assert sp.factor(pp*qq/DDtarget-A)==0
assert sp.factor(pp*rr/DDtarget-B)==0
assert sp.factor(qq*rr/DDtarget-C)==0
assert sp.factor(pp*qq*rr/DDtarget**2-rho)==0
print("K4_SYNTHESIS_ALGEBRA_PASS")
print("lambda_equation = lam^3*x*y*z - rho*lam^2*(x*y+x*z+y*z) - rho^2 = 0")

# Deterministic exhaustive unit-weight scan all labelled simple graphs n<=5.
print("EXHAUSTIVE_RESPONSE_SCAN_BEGIN")
for n in (3,4,5):
    all_edges=list(combinations(range(n),2))
    neg_tau=neg_slack=0
    min_tau=None; min_slack=None
    graphs=0
    for mask in range(1<<len(all_edges)):
        edges=[e for j,e in enumerate(all_edges) if (mask>>j)&1]
        d0,a0,b0,c0,t0=partitions_response(n,edges)
        tau0=d0*t0-a0*b0-a0*c0-b0*c0
        slack=a0*b0*c0-tau0*t0
        graphs+=1
        min_tau=tau0 if min_tau is None else min(min_tau,tau0)
        min_slack=slack if min_slack is None else min(min_slack,slack)
        neg_tau += tau0<0
        neg_slack += slack<0
    print(f"n={n} graphs={graphs} min_tau={min_tau} min_abc_minus_tau_t={min_slack} neg_tau={neg_tau} neg_slack={neg_slack}")
    assert neg_tau==0 and neg_slack==0
print("EXHAUSTIVE_RESPONSE_SCAN_PASS")

# Named regression examples.
star=[(0,3),(1,3),(2,3)]
K4=list(combinations(range(4),2))
for name,edges in [("THREE_SPOKE_STAR",star),("K4_UNIT",K4)]:
    d0,a0,b0,c0,t0=partitions_response(4,edges)
    tau0=d0*t0-a0*b0-a0*c0-b0*c0
    slack=a0*b0*c0-tau0*t0
    print(name, "response=", (d0,a0,b0,c0,t0), "tau=",tau0,"abc_minus_tau_t=",slack)
