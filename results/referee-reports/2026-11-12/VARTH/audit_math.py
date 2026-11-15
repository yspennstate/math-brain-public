"""Independent referee checks. No imports from the supplied authors' code.

Run one mode per invocation: gamma, paths, random, discrete, controls.
All outputs go to this directory. CPU deadline: 280 wall seconds per invocation.
"""
import os
os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
import csv
import random
import resource
import signal
import sys
import time
from fractions import Fraction as F
import mpmath as mp

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("280 second limit")))
signal.alarm(280)
mp.mp.dps = 70
START = time.monotonic()
TARGET = mp.exp(-1)


def fmt(x, digits=38):
    return mp.nstr(x, digits)


def bisect(fun, lo, hi, iterations=145):
    lo, hi = mp.mpf(lo), mp.mpf(hi)
    assert fun(lo) > TARGET and fun(hi) < TARGET
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if fun(mid) > TARGET:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2, hi - lo


def tail(k, t):
    # Poisson lower tail, built recursively without factorial calls.
    term = total = mp.mpf(1)
    for j in range(1, k):
        term *= t / j
        total += term
    return mp.exp(-t) * total


def gamma():
    rows = []
    for k in range(1, 61):
        root, width = bisect(lambda t: tail(k, t), 0, 3*k+10, 190)
        slope = -mp.exp(-root)*root**(k-1)/mp.factorial(k-1)
        rows.append((k, root, root/k, slope, width))
        print(k, fmt(root, 48), fmt(root/k, 48), "slope", fmt(slope, 16))
    with open("gamma_results.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(["k", "t_k", "t_k/k", "survival derivative", "bracket width"])
        w.writerows([[r[0]]+[fmt(x, 60) for x in r[1:]] for r in rows])
    best = max(rows, key=lambda r:r[2])
    print("MAX", best[0], fmt(best[2], 55), "largest bracket width", fmt(max(r[4] for r in rows)))


def bd(k, eps):
    n = k+1
    q = mp.zeros(n)
    for i in range(n):
        if i: q[i, i-1] = 1
        if i<k: q[i, i+1] = eps
        q[i, i] = -sum(q[i,j] for j in range(n) if j!=i)
    weights = [eps**i for i in range(n)]
    pi = [v/sum(weights) for v in weights]
    return q, pi


class Path:
    def __init__(self, k, eps):
        self.k, self.eps = k, eps
        self.q, self.pi = bd(k, eps)
        n = k+1
        # Analytic eigenvalues checked separately against characteristic identities.
        self.rates = [mp.mpf(0)]+[1+eps-2*mp.sqrt(eps)*mp.cos(mp.pi*j/n) for j in range(1,n)]
        self.proj = []
        for j, r in enumerate(self.rates):
            a = mp.eye(n)
            for l, s in enumerate(self.rates):
                if l!=j: a = a*(self.q+s*mp.eye(n))/(s-r)
            self.proj.append(a)

    def matrix(self, t):
        p = mp.zeros(self.k+1)
        for r,a in zip(self.rates,self.proj): p += mp.exp(-r*t)*a
        return p

    def distance(self, t):
        return db(self.matrix(t))[0]

    def threshold(self):
        return bisect(self.distance, 0, 3*self.k+10)[0]


def db(p):
    vals = [(sum(abs(p[i,l]-p[j,l]) for l in range(p.cols))/2, (i,j))
            for i in range(p.rows) for j in range(i+1,p.rows)]
    return max(vals)


def hitting(q):
    n = q.rows
    h = mp.zeros(n)
    for j in range(n):
        ids = [i for i in range(n) if i!=j]
        a = mp.matrix([[-q[i,l] for l in ids] for i in ids])
        v = mp.lu_solve(a, mp.ones(n-1,1))
        for i,x in zip(ids,v): h[i,j] = x
    return h


def paths():
    worst_expm = worst_t0 = mp.mpf(0)
    grid = []
    for z in range(1,101):
        eps = mp.mpf(z)/10000
        p = Path(2,eps)
        t0 = 2*(1+eps)/(1+eps+eps**2)
        t1 = p.threshold()
        d2,pair = db(p.matrix(2))
        assert t1>2>t0 and pair==(0,2)
        grid.append([fmt(eps),fmt(t0),fmt(d2),fmt(t1),fmt(t1/t0)])
        if z in (10,100):
            h = hitting(p.q)
            errors = [abs(sum(p.pi[j]*h[i,j] for j in range(3))-t0) for i in range(3)]
            worst_t0 = max(worst_t0, max(errors), abs(sum(1/r for r in p.rates[1:])-t0))
            print("THREE", *grid[-1], "tau0 second-way error", fmt(max(errors),5))
            with open("dbar_eps_%s.csv"%z,"w") as f:
                w=csv.writer(f); w.writerow(["t","dbar","max pair","direct expm error"])
                for j in range(17):
                    t=mp.mpf(j)/4
                    direct=mp.expm(t*p.q); spectral=p.matrix(t)
                    err=max(abs(direct[a,b]-spectral[a,b]) for a in range(3) for b in range(3))
                    worst_expm=max(worst_expm,err)
                    value,pair=db(direct)
                    w.writerow([fmt(t),fmt(value),str(pair),fmt(err,5)])
    with open("eps_grid.csv","w") as f:
        w=csv.writer(f);w.writerow(["eps","tau0","dbar(2)","tau1","ratio"]);w.writerows(grid)
    print("EPS GRID 100 points: all tau1 > 2 > tau0; smallest dbar(2)", min(mp.mpf(r[2]) for r in grid))
    print("MAX direct expm discrepancy",fmt(worst_expm,5),"MAX tau0 discrepancy",fmt(worst_t0,5))
    for k in (3,4,5):
        limit=bisect(lambda t:tail(k,t),0,3*k+10)[0]
        for es in ("0.001","0.00001","0.0000001"):
            p=Path(k,mp.mpf(es));h=hitting(p.q)
            t0=sum(p.pi[j]*h[k,j] for j in range(k+1));t1=p.threshold()
            d,pair=db(p.matrix(t1));direct=mp.expm(p.q*t1)
            err=max(abs(direct[a,b]-p.matrix(t1)[a,b]) for a in range(k+1) for b in range(k+1))
            assert abs(t0-sum(1/r for r in p.rates[1:]))<mp.mpf("1e-40")
            assert err<mp.mpf("1e-40")
            print("LIMIT",k,es,"tau0",fmt(t0),"tau1",fmt(t1),"ratio",fmt(t1/t0),"t1-tk",fmt(t1-limit,10),"expm error",fmt(err,4),"pair",pair)
    # Exact uniform-in-epsilon analytic lower margin at the endpoint.
    e=mp.mpf("0.01");margin=3-mp.e-(4+2*mp.e**2)*e-4*e**2
    print("ANALYTIC WHOLE-RANGE MARGIN",fmt(margin),"distance excess bound",fmt(mp.exp(-2)*margin))


def solve(a,b):
    """Exact Gauss-Jordan; a and b are rational lists."""
    n=len(b);m=[list(a[i])+[b[i]] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if m[i][j])
        m[j],m[pivot]=m[pivot],m[j]
        s=m[j][j];m[j]=[v/s for v in m[j]]
        for i in range(n):
            if i!=j:
                s=m[i][j];m[i]=[x-s*y for x,y in zip(m[i],m[j])]
    return [r[-1] for r in m]


def mm(x):
    return mp.mpf(x.numerator)/x.denominator


def random_checks():
    rng=random.Random(129845)
    stats={}
    rows=[]
    for n in range(2,7):
        ratios=[];state_slack=[];construct_errors=[]
        for sample in range(15):
            weights=[rng.randint(1,13) for _ in range(n)]
            pi=[F(w,sum(weights)) for w in weights]
            cond=[[F(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i):cond[i][j]=cond[j][i]=F(rng.randint(1,20),20)
            q=[[cond[i][j]/pi[i] if i!=j else F(0) for j in range(n)] for i in range(n)]
            for i in range(n):q[i][i]=-sum(q[i])
            # Invert Pi-Q exactly; Z=(Pi-Q)^(-1)-Pi. No author's implementation.
            a=[[pi[j]-q[i][j] for j in range(n)] for i in range(n)]
            columns=[solve(a,[F(i==j) for i in range(n)]) for j in range(n)]
            z=[[columns[j][i]-pi[j] for j in range(n)] for i in range(n)]
            m=[max(-z[i][j]/pi[j] for j in range(n)) for i in range(n)]
            # Exhaust the LP vertices: xQ=pi-delta_i has a one-dimensional affine solution;
            # setting each coordinate to zero enumerates all possible finite vertices.
            for i in range(n):
                candidates=[]
                for zero in range(n):
                    eq=[[q[l][j] for l in range(n)] for j in range(n-1)]
                    rhs=[pi[j]-F(j==i) for j in range(n-1)]
                    eq.append([F(l==zero) for l in range(n)]);rhs.append(F(0))
                    x=solve(eq,rhs)
                    if all(v>=0 for v in x):candidates.append(sum(x))
                assert min(candidates)==m[i]
                x=[z[i][j]+m[i]*pi[j] for j in range(n)]
                assert all(v>=0 for v in x) and sum(x)==m[i]
                assert all(sum(x[l]*q[l][j] for l in range(n))==pi[j]-F(i==j) for j in range(n))
            sq=[mp.sqrt(mm(v)) for v in pi]
            sym=mp.matrix([[-sq[i]*mm(q[i][j])/sq[j] for j in range(n)] for i in range(n)])
            ev,vec=mp.eigsy(sym);gap=ev[1];tau2=1/gap
            u=[vec[i,1]/sq[i] for i in range(n)];norm=max(abs(v) for v in u);u=[v/norm for v in u]
            tau=max(m);ratio=mm(tau)/tau2
            assert ratio>1-mp.mpf("1e-60")
            slack=min(mm(m[i])-tau2*abs(u[i]) for i in range(n))
            assert slack>-mp.mpf("1e-60")
            ratios.append(ratio);state_slack.append(slack)
            # Discrete P=I+cQ with some eigenvalues allowed negative. Exact value scales.
            c=F(1)/max(-q[i][i] for i in range(n))
            p=[[F(i==j)+c*q[i][j] for j in range(n)] for i in range(n)]
            for i in range(n):
                xd=[(z[i][j]+m[i]*pi[j])/c for j in range(n)]
                y=[xd[j]+pi[j] for j in range(n)]
                stop=[pi[j]/y[j] for j in range(n)]
                assert all(F(0)<v<=1 for v in stop)
                assert all(y[j]==F(i==j)+sum(xd[l]*p[l][j] for l in range(n)) for j in range(n))
                # Independently solve actual stopping rule, not merely its balance constraints.
                a2=[[F(j==l)-(1-stop[j])*p[j][l] for l in range(n)] for j in range(n)]
                means=solve(a2,[1-stop[j] for j in range(n)])
                assert means[i]==m[i]/c
                for target in range(n):
                    end=solve(a2,[stop[j]*F(j==target) for j in range(n)])
                    assert end[i]==pi[target]
            rows.append([n,sample,str(tau),fmt(tau2,50),fmt(ratio,40),str(c)])
        print("RANDOM n",n,"chains",len(ratios),"CT and DT ratio range",fmt(min(ratios),18),fmt(max(ratios),18),"min state slack",fmt(min(state_slack),8))
    with open("random_results.csv","w") as f:
        w=csv.writer(f);w.writerow(["n","sample","exact tau_stop CT","tau2 CT","ratio CT and DT","c for DT"]);w.writerows(rows)
    print("75 rational chains, 300 initial states: exact LP vertices and constructed stopping rules all agree, CT and DT.")
    # The most oscillatory irreducible two-state example, including periodicity.
    for delta in (F(0),F(1,100),F(1,4)):
        print("TWO STATE delta",delta,"tau_stop=tau2",F(1)/(2*(1-delta)),"absolute relaxation", "infinite" if not delta else F(1)/(2*delta))


def discrete():
    for es in ("0.01","0.001"):
        eps=mp.mpf(es);path=Path(2,eps);t0=2*(1+eps)/(1+eps+eps**2);t1=path.threshold()
        for c in (1/(1+eps),mp.mpf("0.1"),mp.mpf("0.01"),mp.mpf("0.001")):
            p=mp.eye(3)+c*path.q
            def d(m):return db(p**m)[0]
            lo,hi=0,1
            while d(hi)>TARGET:hi*=2
            while hi-lo>1:
                mid=(lo+hi)//2
                if d(mid)>TARGET:lo=mid
                else:hi=mid
            h=hitting(p-mp.eye(3));t0_disc=sum(path.pi[j]*h[2,j] for j in range(3))
            assert abs(t0_disc-t0/c)<mp.mpf("1e-60")
            assert d(hi)<=TARGET<d(hi-1)
            err=mp.mpf(0)
            for m in (1,2,int(mp.floor(2/c))):
                err=max(err,max(sum(abs((p**m)[i,j]-mp.expm(m*c*path.q)[i,j]) for j in range(3)) for i in range(3)))
            bound=c*(2*(1+eps))**2*mp.exp(c*2*(1+eps))
            print("DISCRETE eps",es,"c",fmt(c,15),"tau0",fmt(t0_disc,24),"own threshold",hi,"c*threshold",fmt(c*hi,20),"own>tau0",hi>t0_disc,"continuized tau1",fmt(t1/c,24),"ratio",fmt(t1/t0,24),"Euler error",fmt(err,8),"paper bound",fmt(bound,8))
    print("Uniform sufficient c=0.002: bound",fmt(mp.mpf("0.002")*mp.mpf("2.02")**2*mp.exp(mp.mpf("0.00404"))))


def controls():
    p=Path(2,mp.mpf("0.05"))
    t0=2*(1+p.eps)/(1+p.eps+p.eps**2)
    t1=p.threshold()
    f=3-mp.e-(4+2*mp.e**2)*p.eps-4*p.eps**2
    print("CONTROL eps=0.05 f",fmt(f),"tau0",fmt(t0),"tau1",fmt(t1),"ratio",fmt(t1/t0))
    assert f<0 and t1>t0
    for es in ("0.01","0.001"):
        p=Path(2,mp.mpf(es));qa=p.q.copy()
        for j in range(3):qa[0,j]=0
        smallest=mp.mpf(1)
        for j in range(2001):
            t=mp.mpf(j)/1000
            mat=p.matrix(t);d,pair=db(mat)
            g=mp.exp(-(1+p.eps)*t)*(1+(1+p.eps)*t)
            bound=mp.exp(-p.eps*t)-1+g
            smallest=min(smallest,bound)
            assert mat[0,0]+mp.mpf("1e-65")>=mp.exp(-p.eps*t)
            assert d+mp.mpf("1e-65")>=mat[0,0]-mat[2,0]>=bound-mp.mpf("1e-65")
            assert bound>TARGET
            if j%50==0:
                hit=mp.expm(t*qa)[2,0]
                assert mat[2,0]<=hit+mp.mpf("1e-65")<=1-g+mp.mpf("2e-65")
        print("BOUND GRID eps",es,"2001 times, absorbed-chain check at 41 times, smallest scalar lower bound",fmt(smallest))
    worst=mp.mpf(0)
    with open("gamma_results.csv") as f:
        for row in csv.DictReader(f):
            k=int(row["k"]);t=mp.mpf(row["t_k"])
            # Cross-check the recursively summed Poisson tail against the special-function API.
            residual=abs(mp.gammainc(k,t,mp.inf)/mp.gamma(k)-TARGET)
            worst=max(worst,residual)
    print("GAMMA incomplete-gamma API max residual over all 60 roots",fmt(worst,8))
    assert worst<mp.mpf("1e-54")


if __name__=="__main__":
    print("INDEPENDENT AUDIT mode",sys.argv[1],"mpmath",mp.__version__,"precision",mp.mp.dps,flush=True)
    {"gamma":gamma,"paths":paths,"random":random_checks,"discrete":discrete,"controls":controls}[sys.argv[1]]()
    print("ALL ASSERTIONS PASSED; elapsed seconds",round(time.monotonic()-START,3))
    print("Peak resident bytes (macOS ru_maxrss)",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
