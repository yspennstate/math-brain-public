#!/usr/bin/env python3
import json, math

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1.0-x)*math.log2(1.0-x)

def fwht(a):
    a = list(a)
    h = 1
    n = len(a)
    while h < n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return a

def direct_composition(n):
    # inner h(x1,x2)=+1 except h(1,1)=-1; outer is +1 iff every inner output is +1.
    N = 1 << (2*n)
    vals = []
    for x in range(N):
        good = True
        for b in range(n):
            if ((x >> (2*b)) & 3) == 3:
                good = False
                break
        vals.append(1 if good else -1)
    W = fwht(vals)
    den = float(N*N)
    H = 0.0
    I = 0.0
    total = 0.0
    for s,w in enumerate(W):
        if not w:
            continue
        p = (w*w)/den
        total += p
        H += p*math.log2(1.0/p)
        I += p*s.bit_count()
    return H,I,total

def formulas(n):
    delta = (3.0/4.0)**n
    eps = 4.0*delta*(1.0-delta)
    Hmu = h2(eps)+4.0*delta*(n*h2(0.25)-h2(delta))
    I = 4.0*n*delta/3.0
    L = Hmu-I*h2(0.75)
    Hfull = Hmu+n*delta*math.log2(3.0)

    delta0 = 2.0**(-n)
    eps0 = 4.0*delta0*(1.0-delta0)
    Hunif_outer = h2(eps0)+eps0*math.log2((1 << n)-1)
    Hsource = Hunif_outer+2.0*n*delta0*h2(0.75)
    return dict(delta=delta,Hmu=Hmu,I=I,L=L,Hfull=Hfull,Hsource=Hsource)

rows=[]
max_H_err=max_I_err=max_mass_err=0.0
for n in range(1,8):
    f=formulas(n)
    Hd,Id,mass=direct_composition(n)
    herr=abs(Hd-f["Hfull"])
    ierr=abs(Id-f["I"])
    max_H_err=max(max_H_err,herr)
    max_I_err=max(max_I_err,ierr)
    max_mass_err=max(max_mass_err,abs(mass-1.0))
    assert herr < 2e-12, (n,Hd,f["Hfull"],herr)
    assert ierr < 2e-12, (n,Id,f["I"],ierr)
    rows.append({
        "n":n,
        "H_direct":Hd,
        "I_direct":Id,
        "H_over_I":Hd/Id,
        "Hmu_over_Hsource":f["Hmu"]/f["Hsource"],
        "L_over_I":f["L"]/f["I"],
    })

lim_L=10.0-4.5*math.log2(3.0)
lim_H=12.0-4.5*math.log2(3.0)
assert abs((lim_H-lim_L)-2.0) < 1e-15
out={
    "status":"PASS",
    "family":"outer one-point gate composed with n identical 2-bit 3/4-biased gates",
    "checked_direct_dimensions":[2*n for n in range(1,8)],
    "max_entropy_formula_error":max_H_err,
    "max_influence_formula_error":max_I_err,
    "max_parseval_error":max_mass_err,
    "asymptotic_L_over_I":lim_L,
    "asymptotic_H_over_I":lim_H,
    "rows":rows,
}
print(json.dumps(out,indent=2,sort_keys=True))
