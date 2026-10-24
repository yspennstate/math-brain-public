#!/usr/bin/env python3
import math

def F_T(x,T):
    if x == 0.0:
        return 0.0
    return x*math.log1p(T/x)

def K_T(u,v,T):
    return F_T((u+v)**2,T)-F_T((u-v)**2,T)

def Fprime_T(x,T):
    return math.log1p(T/x)-T/(x+T)

def amp_density(r,T):
    if r == 0.0:
        return 0.0
    return 2.0*r*Fprime_T(r*r,T)

derivative_checks = 0
max_ratio = 0.0
max_at = None
for T in (2.0**-8, 0.125, 0.5, 2.0, 8.0, 2.0**8):
    for k in range(-180,181):
        if k == 0:
            continue
        r = 10.0**(k/30.0)
        for rr in (r,-r):
            ratio = abs(amp_density(rr,T))/(2.0*math.sqrt(T))
            if ratio > max_ratio:
                max_ratio,max_at = ratio,(rr,T)
            assert ratio <= 1.0 + 2e-14
            derivative_checks += 1

window_checks = 0
for A,B in ((0.0,0.125),(0.125,2.0),(0.5,8.0),(2.0,9.0)):
    cap = 2.0*(math.sqrt(B)-math.sqrt(A))
    for r in (1e-5,0.003,0.07,0.4,1.0,3.0,20.0):
        d = amp_density(r,B) - (amp_density(r,A) if A>0 else 0.0)
        assert abs(d) <= cap + 1e-12
        window_checks += 1

N=16
Q={0,3,4,7,9,10,12,15}
FSET={0,1,3,5,10,12,14,15}

def affine_masks_4():
    out=[]
    for a in range(16):
        for c in (0,1):
            out.append([(((a & x).bit_count() & 1)^c) for x in range(16)])
    return out
MASKS=affine_masks_4()

def uv(zset,m):
    u=v=0
    for x in range(N):
        s=-1 if ((x in zset) ^ bool(m[x])) else 1
        if x in Q:
            v += s
        else:
            u += s
    return u/N,v/N

witness_rows=[]
pointwise_gate_checks=0
for T in (0.125,0.25,0.5,2.0):
    vals=[]
    inc2=[]
    for m in MASKS:
        uf,vf=uv(FSET,m)
        u0,v0=uv(set(),m)
        d=K_T(uf,vf,T)-K_T(u0,v0,T)
        du,dv=uf-u0,vf-v0
        vals.append(d)
        q=du*du+dv*dv
        inc2.append(q)
        assert d*d <= 16.0*T*q + 1e-12
        pointwise_gate_checks += 1
    avg=sum(vals)/len(vals)
    P=math.log(4*T+1)-0.5*math.log(16*T*T+17*T+1)
    assert abs(avg-2*P/N) < 2e-13
    assert avg < 0.0
    ratio=max((d*d)/(16*T*q) if q else 0.0 for d,q in zip(vals,inc2))
    witness_rows.append((T,avg,ratio))

avg_inc=sum(
    (uv(FSET,m)[0]-uv(set(),m)[0])**2+
    (uv(FSET,m)[1]-uv(set(),m)[1])**2
    for m in MASKS
)/len(MASKS)
expected_inc=4.0*len(FSET)/(N*N)
assert abs(avg_inc-expected_inc)<1e-15

print("PASS")
print(f"derivative_checks={derivative_checks}")
print(f"window_checks={window_checks}")
print(f"pointwise_gate_checks={pointwise_gate_checks}")
print(f"max_derivative_ratio_to_2sqrtT={max_ratio:.15g}")
print(f"max_derivative_ratio_location={max_at}")
print(f"rm14_avg_increment_square={avg_inc:.15g}")
print(f"rm14_exact_orthogonality_target={expected_inc:.15g}")
for T,avg,ratio in witness_rows:
    print(f"b17_witness T={T:g} avg_gate={avg:.15g} max_pointwise_square_ratio={ratio:.15g}")
