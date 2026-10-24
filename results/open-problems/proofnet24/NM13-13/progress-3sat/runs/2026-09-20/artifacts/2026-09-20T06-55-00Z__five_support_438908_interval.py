#!/usr/bin/env python3
"""Rigorous outward-interval certificate for NM13-13 / T04 five-support
hard-field one-step interpolation trial at alpha=4.38908.

Exact symmetric survey law:
  alpha = 109727/25000 = 4.38908
  R in {7/1000, 159/2000, 1/2, 1841/2000, 993/1000}
  weights {33/625, 9/50, 334/625, 9/50, 33/625}.

For mu_k=E[Q^k] with 0<=Q<=1, log-convexity gives
  r_K=mu_K/mu_{K-1},  mu_{K+t} >= mu_K r_K^t.
Thus for finite T,
  A <= A_K - mu_K^2 sum_{t=1}^T r_K^(2t)/(K+t).
All arithmetic below is outward mpmath interval arithmetic.
"""
import mpmath as mp

DPS = 1450
KMAX = 2400
TTAIL = 25000
mp.iv.dps = DPS
Z0 = mp.iv.mpf([0,0])
O1 = mp.iv.mpf([1,1])

def q(n,d):
    return mp.iv.mpf([n,n])/d

alpha = q(109727,25000)
vals = [q(7,1000), q(159,2000), O1/2, q(1841,2000), q(993,1000)]
probs = [q(33,625), q(9,50), q(334,625), q(9,50), q(33,625)]
lam = 3*alpha/2
pair = [(probs[a]*probs[b], O1-vals[a]*vals[b])
        for a in range(5) for b in range(5)]

EZ=[O1]
pows=[O1 for _ in pair]
for j in range(1,KMAX+1):
    moment=Z0
    for idx,(wt,base) in enumerate(pair):
        pows[idx]=pows[idx]*base
        moment=moment+wt*pows[idx]
    EZ.append(mp.iv.exp(lam*(moment-O1)))

arr=EZ
series=Z0
mu_prev=None
mu_K=None
all_mu_positive=True
for k in range(1,KMAX+1):
    arr=[arr[j+1]-arr[j] for j in range(len(arr)-1)]
    mu=arr[0] if k%2==0 else -arr[0]
    all_mu_positive = all_mu_positive and bool(mu.a > 0)
    series=series+mu*mu/k
    if k==KMAX-1:
        mu_prev=mu
    if k==KMAX:
        mu_K=mu

L=Z0
for a in range(5):
    for b in range(5):
        for c in range(5):
            L=L+probs[a]*probs[b]*probs[c]*mp.iv.log(O1-vals[a]*vals[b]*vals[c])
A_K=-series-2*alpha*L

r=mu_K/mu_prev
r2=r*r
rp=r2
geo=Z0
for t in range(1,TTAIL+1):
    geo=geo+rp/(KMAX+t)
    rp=rp*r2
Tail_LB=mu_K*mu_K*geo
A_upper=A_K-Tail_LB

mp.iv.dps=80
print('NM13-13 T04 FIVE-SUPPORT LOG-CONVEX CERTIFICATE')
print('alpha = 109727/25000 = 4.38908')
print('survey support = {7/1000, 159/2000, 1/2, 1841/2000, 993/1000}')
print('survey weights = {33/625, 9/50, 334/625, 9/50, 33/625}')
print('KMAX =',KMAX)
print('TTAIL =',TTAIL)
print('interval computation dps =',DPS)
print('all mu_1..mu_K intervals strictly positive =',all_mu_positive)
print('mu_2399 =',mu_prev)
print('mu_2400 =',mu_K)
print('r_2400 =',r)
print('A_2400 =',A_K)
print('finite log-convex tail lower bound =',Tail_LB)
print('A upper bound =',A_upper)
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(A_upper.b < 0))
print('CERTIFIED_A_NEGATIVE =',bool(A_upper.b < 0),'because A <= A_2400 - tail_LB')
