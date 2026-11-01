"""Exact rational self-check of X029; no random search."""
from pathlib import Path
import json
import sympy as s

OUT = Path(__file__).with_name("results.json")
I = s.I
R = s.Rational
t = s.symbols("t", real=True)


def atoms(K):
    n = K.rows
    return [s.expand((-1) ** (n-m.bit_count()) *
                     (K-s.diag(*[int(not(m >> j & 1)) for j in range(n)])).det())
            for m in range(1 << n)]


def prime_log(x):
    x = s.Rational(x)
    out = {}
    for q, e in s.factorint(x.p).items():
        out[int(q)] = int(e)
    for q, e in s.factorint(x.q).items():
        out[int(q)] = out.get(int(q), 0)-int(e)
    return {q:e for q,e in out.items() if e}


def add_log(out, coeff, x):
    for q,e in prime_log(x).items():
        out[q] = s.cancel(out.get(q, 0)+coeff*e)
    return {q:e for q,e in out.items() if e}


def check(K, A):
    pol = atoms(K+t*A)
    p = [z.subs(t, 0) for z in pol]
    v = [s.diff(z,t).subs(t,0) for z in pol]
    a = [s.diff(z,t,2).subs(t,0) for z in pol]
    assert sum(p)==1 and all(z>0 for z in p)
    assert sum(v)==sum(a)==0
    B=A.adjugate()
    r={(i,j): -A.extract([i,j],[i,j]).det() for i in range(3) for j in range(i+1,3)}
    total=sum(r.values())
    q=s.expand(-s.trace(K*B))
    assert total>0 and 0<=q<=total and all(z>=0 for z in r.values())
    rho=q/total
    mu=[x*y for x in p for y in p]
    drift=[s.S.Zero]*64
    fac=[s.S.Zero]*8
    diss_log={}
    face_log={}
    rates=[]
    for (i,j), rij in r.items():
        k=3-i-j
        for bit in (0,1):
            z=bit<<k
            aa,bb,cc,dd=z,z|(1<<i),z|(1<<j),z|(1<<i)|(1<<j)
            weight=rij*(rho if bit else 1-rho)
            u=p[aa]*p[dd]
            w=p[bb]*p[cc]
            assert w>u
            rate=s.cancel(2*weight/(w-u))
            assert rate>=0
            rates.append(rate)
            for x,y,sign in [(aa,aa,-1),(bb,bb,1),(cc,cc,1),(dd,dd,-1)]:
                fac[x]+=2*weight*sign
            for left,right in ((8*aa+dd,8*bb+cc),(8*dd+aa,8*cc+bb)):
                flux=s.cancel(rate*(mu[right]-mu[left]))
                drift[left]+=flux
                drift[right]-=flux
                diss_log=add_log(diss_log,flux,mu[right]/mu[left])
            face_log=add_log(face_log,2*weight,w/u)
    assert all(s.cancel(x-y)==0 for x,y in zip(a,fac))
    marginal=[sum(drift[8*x:8*x+8]) for x in range(8)]
    assert all(s.cancel(x+y)==0 for x,y in zip(a,marginal))
    curvature_log={}
    for ax,px in zip(a,p):
        curvature_log=add_log(curvature_log,ax,px)
    assert curvature_log==face_log
    assert curvature_log=={q:s.cancel(e/2) for q,e in diss_log.items() if e}
    fisher=s.cancel(sum(vx**2/px for vx,px in zip(v,p)))
    numeric=s.N(fisher+sum(ax*s.log(px) for ax,px in zip(a,p)),40)
    return {"p":[str(z) for z in p],"v":[str(z) for z in v],"a":[str(z) for z in a],
            "R":str(total),"q":str(q),"rho":str(rho),"det_A":str(A.det()),
            "fisher":str(fisher),"acceleration_log_coefficients":{str(q):str(e) for q,e in curvature_log.items()},
            "negative_entropy_hessian":str(numeric),"all_six_rates_positive":all(z>0 for z in rates)}


K=s.Matrix([[R(2,5),R(1,10),I/12],[R(1,10),R(1,2),(1+I)/20],[-I/12,(1-I)/20,R(3,5)]])
A=s.Matrix([[0,1,1+I],[1,0,2-I],[1-I,2+I,0]])
example=check(K,A)
# A simple exact row-sum bound places every eigenvalue in [1/5,4/5].
# Replace |(1+i)/20|=sqrt(2)/20 by 3/40.
radii=[R(1,10)+R(1,12),R(1,10)+R(3,40),R(1,12)+R(3,40)]
assert all(K[i,i]-radii[i]>=R(1,5) and K[i,i]+radii[i]<=R(4,5) for i in range(3))
assert K*A!=A*K

triangle=R(1,2)*s.eye(3)+R(1,10)*(s.ones(3)-s.eye(3))
angular=s.Matrix([[0,I,0],[-I,0,0],[0,0,0]])
obstruction=check(triangle,angular)
assert all(z=="0" for z in obstruction["v"])
assert obstruction["acceleration_log_coefficients"]=={"2":"3","3":"-2","7":"-1","11":"1"}
# Marginal and pair acceleration formulas for an arbitrary symmetric product generator.
b,d,P0,P1,z=s.symbols("b d P0 P1 z", positive=True)
c=s.sqrt(b*d)
S=s.Matrix([[-b,c],[c,-d]])
X=s.diag(0,1)
C=S*(S*X-X*S)-(S*X-X*S)*S
assert s.simplify(C[0,0]*P0+C[1,1]*P1+2*C[0,1]*z-
                 (2*b*d*(P1-P0)+2*c*(d-b)*z))==0
F=s.Matrix([[0,1],[1,0]])
Z=s.diag(-1,1)
F0=s.kronecker_product(F,s.eye(2));F1=s.kronecker_product(s.eye(2),F)
ZZ=s.kronecker_product(Z,Z)
t0,t1=s.symbols("t0 t1", real=True)
T=t0*F0+t1*F1
CC=T*(T*ZZ-ZZ*T)-(T*ZZ-ZZ*T)*T
assert CC==4*(t0*t0+t1*t1)*ZZ+8*t0*t1*F0*F1*ZZ

# The 3/10 threshold is sharp for the acceleration cone.
Astar=s.ones(3)-s.eye(3)
Kstar=R(1,5)*s.eye(3)+R(1,5)*s.ones(3)
assert -s.trace(Kstar*Astar.adjugate())==0
assert set(Kstar.eigenvals())=={R(1,5),R(4,5)}
results={"status":"PASS","dense_complex_example":example,
         "product_bridge_obstruction_example":obstruction,
         "exact_checks":["all atom jets","negative face redistribution","64-state reversible generator marginal drift",
                         "entropy dissipation as exact prime-log coefficients","product bridge marginal and pair commutators",
                         "sharp acceleration-cone spectral threshold"]}
OUT.write_text(json.dumps(results,indent=2)+"\n")
print(json.dumps(results,indent=2))
