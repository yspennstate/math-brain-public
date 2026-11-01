#!/usr/bin/env python3
"""Floating diagnostic only for a candidate global scalar inequality.
No output from this script is a certificate.
"""
import random, math
rng=random.Random(202609161958)
N=300000
min_sec=float('inf'); min_harm=float('inf'); arg_sec=None; arg_harm=None
accepted=0
for _ in range(N):
    y=rng.uniform(0.002,0.998)
    x1,x0=sorted((rng.uniform(0.002,0.998),rng.uniform(0.002,0.998)))
    rho=x0-x1
    maxs=min(x1*y,(1-x0)*(1-y))
    if maxs<=1e-15 or rho<=1e-15: continue
    u=rng.random()
    if u<0.5:
        frac=10**rng.uniform(-10,-0.000001)
    else:
        frac=rng.uniform(1e-8,0.999999)
    s=maxs*frac
    c=rng.uniform(0.002,0.998); a=1-c
    def vals(x):
        p00=(1-x)*(1-y)-s; p10=x*(1-y)+s
        p01=(1-x)*y+s; p11=x*y-s
        if min(p00,p10,p01,p11)<=0: return None
        L=math.log(p10*p01/(p00*p11))
        Hy=(1-x)*math.log(p00/p01)+x*math.log(p10/p11)
        return L,Hy
    z1=vals(x1); z0=vals(x0)
    if z1 is None or z0 is None: continue
    L1,H1=z1; L0,H0=z0
    if L0<=0 or L1<=0: continue
    G=H0-H1
    sec=min(L0,L1)-G/rho
    harm=rho/(c/L0+a/L1)-G
    accepted+=1
    if sec<min_sec:
        min_sec=sec; arg_sec=(x1,x0,y,s,c,L1,L0,G)
    if harm<min_harm:
        min_harm=harm; arg_harm=(x1,x0,y,s,c,L1,L0,G)
print('diagnostic_only=True')
print('trials=',N)
print('accepted=',accepted)
print('negative_secant_found=',min_sec<0)
print('min_secant_margin=',repr(min_sec))
print('argmin_secant=',repr(arg_sec))
print('negative_harmonic_found=',min_harm<0)
print('min_harmonic_margin=',repr(min_harm))
print('argmin_harmonic=',repr(arg_harm))
