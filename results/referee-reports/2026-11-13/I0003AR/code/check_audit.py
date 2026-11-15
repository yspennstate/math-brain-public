"""Small independent checks; none is used as an infinite-volume proof."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random
import resource
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RNG = random.Random(13032026)
result = {"seed": 13032026, "nice": os.getpriority(os.PRIO_PROCESS, 0), "threads": 1}

def primitive(sign, k):
    if k >= 0: return sum(sign(j) for j in range(1, k+1))
    return -sum(sign(j) for j in range(k+1, 1))

def generator(e, f):
    n = len(e)
    L = np.zeros((n*n, n*n))
    for x in range(n):
        for y in range(n):
            i = n*x+y
            L[i, n*((x+e[y]) % n)+y] += 1
            L[i, n*x+(y+f[x]) % n] += 1
            L[i, i] -= 2
    return L

def quadratic(A, H):
    return H - np.einsum('ij,jk->ik', A, np.linalg.solve(H, A), optimize=False)

worst_identity = worst_variational = 0.0
comparisons = []
for rep in range(8):
    e = [RNG.choice((-1,1)) for _ in range(6)]
    f = [RNG.choice((-1,1)) for _ in range(6)]
    et, ft = e[::-1], f[2:]+f[:2]
    L, Lt = generator(e,f), generator(et,ft)
    S, A, At = (L+L.T)/2, (L-L.T)/2, (Lt-Lt.T)/2
    assert np.array_equal(S, (Lt+Lt.T)/2)
    assert np.array_equal(A.T, -A)
    assert np.all(L.sum(axis=0)==0) and np.all(L.sum(axis=1)==0)
    es = lambda k: et[k%6]-e[k%6]
    fs = lambda k: ft[k%6]-f[k%6]
    hd = max(abs((primitive(es,y)-primitive(fs,x))/2) for x in range(6) for y in range(6))
    C = 2 + 128*hd*hd
    for lam in (1.0, 0.125, 0.015625):
        H = lam*np.eye(36)-S
        Q, Qt = quadratic(A,H), quadratic(At,H)
        R = np.linalg.inv(H-A)
        Rq = np.linalg.inv(Q)
        err = np.max(np.abs((R+R.T)/2-Rq))
        worst_identity=max(worst_identity,float(err))
        assert err < 2e-10
        v = np.zeros(36); v[0]=1
        u = np.linalg.solve(Q,v)
        var = 2*u[0]-np.einsum('i,ij,j->', u, Q, u, optimize=False)
        worst_variational=max(worst_variational,abs(float(var-R[0,0])))
        assert abs(var-R[0,0]) < 2e-10
        low1 = np.linalg.eigvalsh(C*Q-Qt).min()
        low2 = np.linalg.eigvalsh(C*Qt-Q).min()
        assert min(low1,low2) >= -2e-10
        ratio = np.linalg.inv(H-At)[0,0]/R[0,0]
        assert 1/C-1e-10 <= ratio <= C+1e-10
        comparisons.append({"lambda":lam,"C":C,"diagonal_ratio":float(ratio)})
result["torus"]={"fields":8,"lambda_values":[1,0.125,0.015625],
                 "max_identity_error":worst_identity,"max_variational_error":worst_variational,
                 "comparisons":comparisons}

for rep in range(30):
    ed={k:RNG.choice((-1,1)) for k in range(-9,10)}
    fd={k:RNG.choice((-1,1)) for k in range(-9,10)}
    e, f = ed.__getitem__, fd.__getitem__
    U={ (x,y):F(RNG.randrange(-9,10),3) for x in range(-3,4) for y in range(-3,4)}
    V={ (x,y):F(RNG.randrange(-9,10),5) for x in range(-3,4) for y in range(-3,4)}
    u=lambda z: U.get(z,F(0))
    v=lambda z: V.get(z,F(0))
    lhs=F(0)
    for (x,y),ux in U.items():
        lhs+=ux*(e(y)*(v((x+1,y))-v((x-1,y)))+f(x)*(v((x,y+1))-v((x,y-1))))/2
    rhs=F(0); W=F(0); Ev=F(0)
    for x in range(-5,6):
        for y in range(-5,6):
            q=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
            us,vs=[u(z) for z in q],[v(z) for z in q]
            curl=sum(us[i]*vs[(i+1)%4]-us[(i+1)%4]*vs[i] for i in range(4))
            diag=(us[0]-us[2])*(vs[1]-vs[3])-(us[1]-us[3])*(vs[0]-vs[2])
            assert curl==diag
            h=F(primitive(e,y)-primitive(f,x),2)
            rhs+=h*curl
            W+=h*h*sum((us[(i+1)%4]-us[i])**2 for i in range(4))
            Ev+=sum((v((x+dx,y+dy))-v((x,y)))**2 for dx,dy in ((1,0),(0,1)))/2
    assert lhs==rhs
    assert lhs*lhs <= 16*W*Ev
result["face_identity"]={"exact_rational_trials":30,"passed":True}

def g(k): return 1 if k>=0 else -1
def rad(x,y): return (abs(2*x+1)+abs(2*y+1))//2
for rep in range(24):
    N=RNG.randrange(2,13)
    phi={r:F(RNG.randrange(-8,9),RNG.randrange(1,9)) for r in range(1,N+1)}
    p=lambda r:phi.get(r,F(0))
    a={r:p(r+1)-p(r) for r in range(1,N+1)}
    expected=defaultdict(F)
    for r in range(2,N+2):
        pairs=[((r-1,0),(r-1,-1)),((-r,-1),(-r,0)),
               ((-1,r-1),(0,r-1)),((0,-r),(-1,-r))]
        for z,w in pairs:
            expected[z]+=a[r-1]/2; expected[w]-=a[r-1]/2
    E=F(0)
    for x in range(-N-3,N+3):
        for y in range(-N-3,N+3):
            u=lambda xx,yy:p(rad(xx,yy))
            Au=(g(y)*(u(x+1,y)-u(x-1,y))-g(x)*(u(x,y+1)-u(x,y-1)))/2
            assert Au==expected[(x,y)]
            E+=((u(x+1,y)-u(x,y))**2+(u(x,y+1)-u(x,y))**2)/2
    assert E==4*sum(r*a[r]**2 for r in a)
result["circulating"]={"exact_rational_profiles":24,"passed":True}
result["square_annuli"]=[]
for m in range(8):
    count=sum(8*k+4 for k in range(2**m,2**(m+1)))
    assert count==12*4**m
    result["square_annuli"].append({"m":m,"gradient_edges":count})
for k in range(-200,201):
    sg=primitive(g,k)
    assert sg==(k if k>=0 else -k-2)
for r in range(1,201):
    assert max(abs(primitive(g,k)) for k in range(-r,r+1))==r
result["circulating_envelope"]="M(r)^2 = 2*r^2 for integer r>=1; dyadic series < 1/6"

def counts(e,f,steps=64):
    paths={(0,0):1}; out=[]
    for n in range(steps+1):
        assert sum(paths.values())==2**n
        out.append(paths.get((0,0),0))
        nxt=defaultdict(int)
        for (x,y),c in paths.items():
            nxt[(x+e(y),y)]+=c
            nxt[(x,y+f(x))]+=c
        paths=nxt
    return out

Crec=counts(g,lambda x:-g(x))
Csad=counts(g,g)
Csad_flip=counts(g,lambda x: -g(x) if x in (-1,0) else g(x))
assert all(c==0 for c in Csad[1:])
assert Csad_flip[4]>0
result["finite_path_counts"]={"horizon":64,
    "circulating":Crec,"saddle":Csad,"saddle_two_line_flips":Csad_flip,
    "note":"Counts divided by 2**n are exact; finite horizons do not prove recurrence."}

source_rows=[json.loads(s) for s in (ROOT/'sources/MANIFEST.txt').read_text().splitlines()]
for row in source_rows:
    if row['status']=='ok':
        p=ROOT/'sources'/(row['name']+'.txt')
        assert hashlib.sha256(p.read_bytes()).hexdigest()==row['text_sha256']
result['sources_verified']=sum(r['status']=='ok' for r in source_rows)
result['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
(ROOT/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('torus','finite_path_counts')},indent=2))
print('max resolvent identity error:',worst_identity)
print('max variational error:',worst_variational)
print('All independent checks passed.')
