"""Bounded exact random testing, spectral tests and a separate numerical LP."""
import json
import random
import time
from fractions import Fraction as F
from itertools import combinations
import numpy as np
import scipy
from scipy.optimize import linprog
from referee_core import exact_chain, exact_hit, lump, inverse

start = time.monotonic()
rng = random.Random(9812026)
out = dict(seed=9812026,numpy=np.__version__,scipy=scipy.__version__,
           chains=0,eigenfunction_checks=0,lp_checks=0,hitting_checks=0,
           green_identity_checks=0,failures=[])
worst_hit = 0.
for n in range(2,7):
    for case in range(45):
        assert time.monotonic()-start < 200
        w = [[F(0)]*n for _ in range(n)]
        for i in range(n-1):
            w[i][i+1] = w[i+1][i] = F(rng.randint(1,9),rng.randint(1,4))
        for i in range(n):
            for j in range(i,n):
                if rng.random()<.5:
                    w[i][j] += F(rng.randint(1,30),rng.randint(1,6))
                    w[j][i] = w[i][j]
        a = exact_chain(w)
        out['chains'] += 1
        wf = np.array(w,dtype=float)
        d = wf.sum(axis=1)
        pi = d/d.sum()
        p = wf/d[:,None]
        s = wf/np.sqrt(d[:,None]*d[None,:])
        vals,vecs = np.linalg.eigh(s)
        relax = 1/(1-vals[-2])
        assert relax <= float(a['tmix'])+1e-8
        assert float(a['tau0']) <= (n-1)*relax+1e-8
        assert abs(sum(1/(1-v) for v in vals[:-1])-float(a['tau0']))<1e-7
        # Each real nonconstant eigenfunction, not only lambda_2.
        for k in range(n-1):
            g = vecs[:,k]/np.sqrt(pi)
            i = np.argmax(np.abs(g))
            assert float(a['starts'][i])+1e-8 >= 1/(1-vals[k])
            out['eigenfunction_checks'] += 1
        # Minimize sum(v), subject to occupation conservation.
        for i in range(n):
            rhs = -pi.copy()
            rhs[i] += 1
            lp = linprog(np.ones(n),A_eq=(np.eye(n)-p).T,b_eq=rhs,
                         bounds=(0,None),method='highs')
            assert lp.success and abs(lp.fun-float(a['starts'][i]))<1e-7
            out['lp_checks'] += 1
        # Surjective random partition, also identity and one-state edge cases.
        m = rng.randint(1,n)
        labels = list(range(m))+[rng.randrange(m) for _ in range(n-m)]
        rng.shuffle(labels)
        v = lump(w,labels)
        if m==1:
            assert sum(map(sum,v))==sum(map(sum,w))
            continue
        b = exact_chain(v)
        assert b['tmix'] <= b['tau0'] <= a['tau0']
        assert b['tmix'] <= (n-1)*a['tmix']
        dh=np.array(v,dtype=float).sum(axis=1)
        sh=np.array(v,dtype=float)/np.sqrt(dh[:,None]*dh[None,:])
        valh=np.linalg.eigvalsh(sh)
        relaxh=1/(1-valh[-2])
        assert relaxh <= relax+1e-8
        assert float(b['tau0']) <= (m-1)*relaxh+1e-8
        assert b['tmix'] <= (m-1)*a['tmix']
        if m<n:
            assert b['tmix'] <= (n-2)*a['tmix']
        for block in range(m):
            assert b['pi'][block] == sum(a['pi'][i] for i in range(n) if labels[i]==block)
        for bits in range(1,2**m-1):
            targeth = {j for j in range(m) if (bits>>j)&1}
            target = {i for i in range(n) if labels[i] in targeth}
            outside,e,g,k = exact_hit(w,target)
            oh,eh,gh,kh = exact_hit(v,targeth)
            trace = sum(g[j][j] for j in range(len(outside)))
            # G(x,y)=Pr_x(T_y<T_A) G(y,y), check probability independently
            # from the harmonic Dirichlet system with y wired to voltage one.
            for jy,y in enumerate(outside):
                others = [x for x in outside if x!=y]
                if others:
                    mat = [[(sum(w[x]) if x==z else F(0))-w[x][z]
                            for z in others] for x in others]
                    ki = inverse(mat)
                    prob = [sum(row[t]*w[z][y] for t,z in enumerate(others)) for row in ki]
                    for x,px in zip(others,prob):
                        assert g[outside.index(x)][jy] == px*g[jy][jy]
                        out['green_identity_checks'] += 1
                assert g[jy][jy] == sum(w[y])*k[jy][jy]
                block=labels[y]
                ib=oh.index(block)
                assert kh[ib][ib] <= k[jy][jy]
            assert max(eh) <= trace <= sum(e) <= (n-len(target))*max(e)
            for block in oh:
                worst_hit=max(worst_hit,float(eh[block]/max(e)))
                out['hitting_checks'] += 1
out['largest_hit_ratio'] = worst_hit
out['seconds'] = time.monotonic()-start
out['all_passed'] = True
with open('referee_random.json','w') as f:
    json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
