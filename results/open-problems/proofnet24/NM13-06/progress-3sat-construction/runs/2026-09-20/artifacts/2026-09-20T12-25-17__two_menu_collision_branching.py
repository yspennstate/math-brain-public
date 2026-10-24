#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps = 50
K = 50

def poisson_probs(mu):
    p=[mp.e**(-mu)]
    for k in range(K):
        p.append(p[-1]*mu/(k+1))
    return p

def stats(alpha):
    a=mp.mpf(alpha); mu=mp.mpf('1.5')*a
    x=2*mu
    q=mp.mpf('0.5')*(1-mp.e**(-x)*(mp.besseli(0,x)+mp.besseli(1,x)))
    EZ=2*mu*q
    p=poisson_probs(mu)
    q2=q*q
    bprob=[mp.mpf('0')]*(K+1)
    palm=mp.mpf('0')
    for P in range(K+1):
        for N in range(K+1):
            z=min(P,N)
            if not z: continue
            m=max(P,N)
            w=mp.mpf(z)*p[P]*p[N]/EZ
            palm += w
            pb=(1-q2)**m
            bprob[0]+=w*pb
            if m:
                ratio=q2/(1-q2)
                for b in range(1,m+1):
                    pb = pb*(m-b+1)/b*ratio
                    bprob[b]+=w*pb
    tail=[mp.mpf('0')]*(K+2)
    for t in range(K,-1,-1):
        tail[t]=tail[t+1]+bprob[t]
    r2=mp.fsum(tail[t]**2 for t in range(1,K+1))
    r3=mp.fsum(tail[t]**3 for t in range(1,K+1))
    s=1+r3/(1-r2)
    u=a*q**3
    C2=2*u*s*s
    return q,r2,r3,s,u,C2,1-mp.fsum(p),1-palm

def f(x,d=18): return mp.nstr(x,d)

print('T04 fresh-copy two-menu collision branching diagnostic')
print('mp.dps=50 K=50')
for a in ('3.52','3.55','3.58','3.58068','3.58069','3.60','4.00'):
    q,r2,r3,s,u,C2,pt,pm=stats(a)
    print(f'alpha={a} q={f(q)} r2={f(r2)} r3={f(r3)} s={f(s)} u={f(u)} C2={f(C2)} pois_tail={f(pt,8)} palm_missing={f(pm,8)}')
lo=mp.mpf('3.58068'); hi=mp.mpf('3.58069')
Clo=stats(lo)[5]; Chi=stats(hi)[5]
root_est = lo + (1-Clo)*(hi-lo)/(Chi-Clo)
print('sign bracket: C2(3.58068) < 1 < C2(3.58069)')
print('linear root estimate =', mp.nstr(root_est,20))
print('NOTE: high-precision finite-sum diagnostic; not a directed-rounding interval proof.')
