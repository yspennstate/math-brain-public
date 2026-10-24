"""Exact-rational algebra checks, not iid-stable simulations or proof by testing."""
from fractions import Fraction as Q
from random import Random
import json

rng = Random(20261024)
X = ((Q(1), Q(0)), (Q(3, 5), Q(4, 5)))
G = ((Q(1), Q(3, 5)), (Q(3, 5), Q(1)))
a, L, gamma = Q(5), Q(2), Q(1, 2)
h = gamma / L

def dot(x, y):
    return sum((p*q for p,q in zip(x,y)), Q(0))

def positive(u):
    return tuple(max(Q(0), dot(x,u)) for x in X)

def output(w, hidden):
    return tuple(sum((wi*vi[j] for wi,vi in zip(w,hidden)), Q(0))/(a*L) for j in range(2))

steps = reactivations = deactivations = 0
for trial in range(100):
    w = [Q(rng.randint(-4,4)) for _ in range(3)]
    u = [tuple(Q(rng.randint(-3,3)) for _ in range(2)) for _ in range(3)]
    y = tuple(Q(rng.randint(-3,3)) for _ in range(2))
    w0 = w[:]
    hh = [positive(v) for v in u]
    hh0 = hh[:]
    f0 = output(w,hh)
    hist = []
    for n in range(4):
        f = output(w,hh)
        r = tuple(yj-fj for yj,fj in zip(y,f))
        hist.append((r,hh[:]))
        mask = [tuple(int(dot(x,v)>0) for x in X) for v in u]
        unew = [tuple(ui[t]+gamma/a*wi*sum((X[j][t]*di[j]*r[j] for j in range(2)),Q(0)) for t in range(2)) for wi,ui,di in zip(w,u,mask)]
        wnew = [wi+gamma/a*dot(r,vi) for wi,vi in zip(w,hh)]
        hhnew = [positive(v) for v in unew]
        fnew = output(wnew,hhnew)
        for j in range(2):
            first = sum((wi/a*(hn[j]-ho[j]) for wi,hn,ho in zip(w,hhnew,hh)),Q(0))
            second = gamma/a**2*sum((dot(r,ho)*hn[j] for ho,hn in zip(hh,hhnew)),Q(0))
            assert L*(fnew[j]-f[j]) == first+second
            endpoint = sum((wi/a*(hn[j]-ho[j]) for wi,hn,ho in zip(w0,hhnew,hh0)),Q(0))/L
            cross = h/a**2*sum((sum((hn[j]*dot(rpast,hpast_i) for hn,hpast_i in zip(hhnew,hpast)),Q(0)) for rpast,hpast in hist),Q(0))
            assert fnew[j]-f0[j] == endpoint+cross
        for old,new in zip(u,unew):
            for x in X:
                reactivations += int(dot(x,old)<=0<dot(x,new))
                deactivations += int(dot(x,old)>0>=dot(x,new))
        w,u,hh = wnew,unew,hhnew
        steps += 1
assert reactivations > 0 and deactivations > 0
print(json.dumps({'seed':20261024,'trials':100,'steps':steps,'vector_step_identities':steps,'cross_time_identities':steps,'reactivations':reactivations,'deactivations':deactivations,'arithmetic':'exact Fraction','all_assertions_passed':True,'scope':'algebra only; arbitrary finite arrays, not stable-law draws'},indent=2))
