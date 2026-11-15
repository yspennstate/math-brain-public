"""Independent exact-size recursive sampler for a genuine two-component kernel.

No imports from claim_files. Finite-progeny probabilities are calculated by a
coefficient recurrence, then used to draw each conditional subtree. The sampler
is exact apart from floating-point quadrature and arithmetic; no MCMC, size
window, rejection cutoff, or discretisation of the continuous type space.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
import argparse
import csv
import ctypes
import datetime
import itertools
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
from numpy.polynomial.legendre import leggauss

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "independent_data"


def govern():
    state = json.loads((Path.home() / ".claude/compute/compute_state.json").read_text())
    if state.get("status") == "distress":
        raise RuntimeError("Governor distress: stopping numerical work")
    return {k: state.get(k) for k in ("ts", "status", "mode", "mem_free_pct")}


def priority():
    lib = ctypes.CDLL(None, use_errno=True)
    ctypes.set_errno(0)
    p = lib.getpriority(0, 0)
    if ctypes.get_errno():
        raise OSError(ctypes.get_errno(), "getpriority")
    if p < 10 and lib.setpriority(0, 0, 10):
        raise OSError(ctypes.get_errno(), "setpriority")
    assert lib.getpriority(0, 0) >= 10
    return lib.getpriority(0, 0)


def parameters(points=480, cutoff=12.0):
    # Gauss-Legendre on a finite interval, independent of submitted GH/adaptive code.
    nodes, weights = leggauss(points)
    x, weights = cutoff * nodes, cutoff * weights
    q = np.exp(-0.5 * (x[None, :] - np.array([[-0.8], [0.8]]))**2) / math.sqrt(2*math.pi)
    base_p = 0.55 + 0.15 * np.tanh(x)
    w = np.array([0.5 + 0.2 * np.tanh(x), 0.5 - 0.2 * np.tanh(x)])
    base_c = q @ (weights * base_p)
    mu_weights = q * (weights * base_p)[None, :] / base_c[:, None]
    base_r = w * base_c[:, None]
    A = mu_weights @ base_r.T
    rho = (np.trace(A) + math.sqrt((A[0, 0]-A[1, 1])**2 + 4*A[0, 1]*A[1, 0]))/2
    nu_poisson = 1/rho
    tau = nu_poisson/2
    r = tau * base_r
    M = 2 * mu_weights @ r.T
    a = np.array([M[1, 0], 1-M[0, 0]])
    a /= a.sum()
    b = np.array([M[0, 1], 1-M[0, 0]])
    b /= a @ b
    h = 2 * b @ r
    ell_weights = a @ mu_weights
    h2 = ell_weights @ h**2
    reject = 1-r.sum(axis=0)
    p0 = mu_weights @ reject**2
    p1 = np.array([[mu_weights[i] @ (2*reject*r[j]) for j in range(2)] for i in range(2)])
    p2 = np.array([[[mu_weights[i] @ (r[j]*r[k]) for k in range(2)] for j in range(2)] for i in range(2)])
    Q = 2*p2
    sigma2 = float(np.einsum("i,j,k,ijk", a, b, b, Q))
    assert np.max(abs(M@b-b)) < 1e-12
    assert np.max(abs(a@M-a)) < 1e-12
    assert abs(ell_weights@h-1) < 1e-12
    assert abs(sigma2 - h2/2) < 1e-12
    assert np.max(abs(p0+p1.sum(axis=1)+p2.sum(axis=(1,2))-1)) < 1e-12
    ordinary_mean = 2*r.sum(axis=0)
    # For the submitted Poisson model, m(x)=2 sum r_j(x) as well.
    spine_mean = ell_weights @ (h*ordinary_mean)
    raw_poisson_var = ell_weights @ (h*(ordinary_mean+ordinary_mean**2))-spine_mean**2
    info = {"integration": {"method": "Gauss-Legendre", "points": points, "cutoff": cutoff},
            "potential_children": 2, "Gamma": "w1(x)N(-0.8,1)+(1-w1(x))N(0.8,1); w1=.5+.2tanh(x)",
            "p": "tau*(.55+.15tanh(y))", "tau": tau,
            "M": M.tolist(), "a": a.tolist(), "b": b.tolist(),
            "sigma2": sigma2, "scale": math.sqrt(sigma2)/2,
            "poisson_claim_check": {"nu": nu_poisson, "sigma2": float(h2),
                                    "scale": math.sqrt(h2)/2,
                                    "spine_mean_count": float(spine_mean),
                                    "spine_raw_count_variance": float(raw_poisson_var)},
            "p0": p0.tolist(), "p1": p1.tolist(), "p2": p2.tolist(),
            "checks": {"left_residual": float(np.max(abs(a@M-a))),
                       "right_residual": float(np.max(abs(M@b-b))),
                       "continuous_vs_factorial": abs(sigma2-float(h2)/2)}}
    return p0, p1, p2, info


def progeny_probabilities(nmax, p0, p1, p2):
    # F_i(z) = z[p0_i + sum p1_ij F_j + sum p2_ijk F_j F_k].
    prob = np.zeros((2, nmax+1))
    prob[:, 1] = p0
    for n in range(2, nmax+1):
        govern() if n % 5000 == 0 else None
        if n == 2:
            conv = np.zeros(3)
        else:
            conv = np.array([np.dot(prob[j, 1:n-1], prob[k, n-2:0:-1])
                             for j,k in ((0,0),(0,1),(1,1))])
        prob[:, n] = p1 @ prob[:, n-1] + p2[:,0,0]*conv[0] + 2*p2[:,0,1]*conv[1] + p2[:,1,1]*conv[2]
    assert np.all(prob[:,1:] > 0)
    return prob


def all_choices(t, n, prob, p1, p2):
    if n == 1:
        return [((), ())], np.array([1.0])
    options = [((j,), (n-1,)) for j in range(2)]
    values = list(p1[t] * prob[:,n-1])
    for j,k in itertools.product(range(2), repeat=2):
        options.extend([((j,k),(s,n-1-s)) for s in range(1,n-1)])
        values.extend(p2[t,j,k]*prob[j,1:n-1]*prob[k,n-2:0:-1])
    return options, np.array(values)


def exhaustive_checks(p0,p1,p2,prob):
    # Enumerate every typed plane unary/binary tree through size 6, then compare
    # both the coefficient recurrence and the telescope of conditional choices.
    cache = {}
    def enum(t,n):
        if (t,n) in cache:
            return cache[t,n]
        if n == 1:
            result = [(float(p0[t]), float(p0[t]/prob[t,n]))]
        else:
            result = []
            for j in range(2):
                for mass,cond in enum(j,n-1):
                    result.append((p1[t,j]*mass, (p1[t,j]*prob[j,n-1]/prob[t,n])*cond))
            for j,k in itertools.product(range(2),repeat=2):
                for s in range(1,n-1):
                    factor = p2[t,j,k]*prob[j,s]*prob[k,n-1-s]/prob[t,n]
                    for l,lc in enum(j,s):
                        for r,rc in enum(k,n-1-s):
                            result.append((p2[t,j,k]*l*r, factor*lc*rc))
        cache[t,n] = result
        return result
    out=[]
    for n in range(1,7):
        for t in range(2):
            pairs=enum(t,n)
            err=max(abs(c-m/prob[t,n]) for m,c in pairs)
            assert err < 1e-13
            assert abs(math.fsum(m for m,c in pairs)-prob[t,n]) < 1e-13
            assert abs(math.fsum(c for m,c in pairs)-1) < 1e-12
            out.append({"n":n,"root_type":t,"typed_trees":len(pairs),"max_probability_error":err})
    return out


def sample(n, rng, prob, p0,p1,p2,small):
    pending=[(0,n,-1,0)]
    parents=np.empty(n,dtype=np.int32)
    depths=np.empty(n,dtype=np.int32)
    types=np.empty(n,dtype=np.int8)
    degrees=np.empty(n,dtype=np.int8)
    index=0
    while pending:
        t,size,par,depth=pending.pop()
        parents[index],depths[index],types[index]=par,depth,t
        if size==1:
            child_types,child_sizes=(),()
        elif size<=64:
            choices,cum=small[t,size]
            chosen=min(int(np.searchsorted(cum,rng.random()*cum[-1])),len(cum)-1)
            child_types,child_sizes=choices[chosen]
        else:
            unary=p1[t]*prob[:,size-1]
            binary=np.array([p2[t,j,k]*np.dot(prob[j,1:size-1],prob[k,size-2:0:-1])
                             for j,k in itertools.product(range(2),repeat=2)])
            categories=np.cumsum(np.r_[unary,binary])
            assert abs(categories[-1]/prob[t,size]-1)<1e-11
            choice=min(int(np.searchsorted(categories,rng.random()*categories[-1])),5)
            if choice<2:
                child_types,child_sizes=(choice,),(size-1,)
            else:
                j,k=divmod(choice-2,2)
                cumulative=np.cumsum(prob[j,1:size-1]*prob[k,size-2:0:-1])
                s=1+min(int(np.searchsorted(cumulative,rng.random()*cumulative[-1])),size-3)
                child_types,child_sizes=(j,k),(s,size-1-s)
        degrees[index]=len(child_types)
        for ct,cs in reversed(list(zip(child_types,child_sizes))):
            pending.append((ct,cs,index,depth+1))
        index+=1
    assert index==n and degrees.sum()==n-1
    assert np.all(depths[1:]==depths[parents[1:]]+1)
    assert np.array_equal(np.bincount(parents[1:],minlength=n),degrees)
    return int(depths.max()),float(depths.mean()),parents,depths,types,degrees


def max_excursion_cdf(value):
    if value<=0:
        return 0.0
    if value<1:
        return math.sqrt(2*math.pi)*math.pi**2/value**3*sum(k*k*math.exp(-math.pi**2*k*k/(2*value**2)) for k in range(1,30))
    return 1-2*sum((4*k*k*value*value-1)*math.exp(-2*k*k*value*value) for k in range(1,30))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--sizes",default="500,2000,10000")
    parser.add_argument("--replicates",type=int,default=600)
    args=parser.parse_args()
    started=time.monotonic()
    nice=priority()
    gov=govern()
    OUT.mkdir(exist_ok=True)
    p0,p1,p2,info=parameters()
    _,_,_,second=parameters(320,11.0)
    info["second_quadrature_scale_difference"]=abs(info["scale"]-second["scale"])
    sizes=[int(n) for n in args.sizes.split(",")]
    prob=progeny_probabilities(max(sizes),p0,p1,p2)
    enumeration=exhaustive_checks(p0,p1,p2,prob)
    small={}
    for t in range(2):
        for n in range(2,65):
            choices,values=all_choices(t,n,prob,p1,p2)
            assert abs(values.sum()/prob[t,n]-1)<1e-12
            small[t,n]=choices,np.cumsum(values)
    seed=1515202611130917
    rng=np.random.Generator(np.random.PCG64(seed))
    summaries=[]
    with (OUT/"trees.csv").open("w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["n","replicate","height","mean_depth","scaled_height","scaled_mean_depth"])
        for n in sizes:
            heights=[]
            means=[]
            for rep in range(args.replicates):
                if rep%50==0:
                    govern()
                ht,md,parents,depths,types,degrees=sample(n,rng,prob,p0,p1,p2,small)
                sh,sm=info["scale"]*np.array([ht,md])/math.sqrt(n)
                writer.writerow([n,rep,ht,md,sh,sm])
                heights.append(sh)
                means.append(sm)
                if n==max(sizes) and rep==0:
                    with (OUT/"example_tree.csv").open("w",newline="") as e:
                        ew=csv.writer(e)
                        ew.writerow(["vertex","parent","depth","latent_type","offspring"])
                        ew.writerows(zip(range(n),parents,depths,types,degrees))
            heights=np.array(heights)
            means=np.array(means)
            ordered=np.sort(heights)
            cdf=np.array([max_excursion_cdf(v) for v in ordered])
            ks=float(max(np.max(np.arange(1,len(ordered)+1)/len(ordered)-cdf),
                         np.max(cdf-np.arange(len(ordered))/len(ordered))))
            item={"n":n,"replicates":args.replicates,
                  "height_mean":float(heights.mean()),"height_se":float(heights.std(ddof=1)/math.sqrt(len(heights))),
                  "mean_depth_mean":float(means.mean()),"mean_depth_se":float(means.std(ddof=1)/math.sqrt(len(means))),
                  "height_KS_to_CRT":ks,"size_probability_root0":float(prob[0,n]),
                  "size_probability_asymptotic_ratio":float(prob[0,n]*n**1.5*math.sqrt(2*math.pi*info["sigma2"])/info["b"][0])}
            summaries.append(item)
            print(json.dumps(item),flush=True)
            f.flush()
    result={"parameters":info,"seed":seed,"root_law":"mu_1, integrated exactly into latent root class 0",
            "predictions":{"max_excursion_mean":math.sqrt(math.pi/2),"mean_excursion_area":math.sqrt(math.pi/8)},
            "enumeration":enumeration,"summaries":summaries,"nice":nice,"numerical_threads":1,
            "governor_start":gov,"elapsed_seconds":time.monotonic()-started,
            "max_rss_bytes_macos":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "finished_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
    (OUT/"results.json").write_text(json.dumps(result,indent=2)+"\n")
    print("FINISHED",result["elapsed_seconds"],result["max_rss_bytes_macos"],flush=True)


if __name__=="__main__":
    main()
