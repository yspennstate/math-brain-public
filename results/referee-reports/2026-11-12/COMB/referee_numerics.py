"""Deterministic killed-kernel moments and summaries, independently of the authors.

The finite domain is exactly the rectangle used by referee_sim.c. Teeth crossing
its top are killed, never reflected or renormalized there.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[name] = "1"
import csv
import json
import math
import time
import numpy as np
from scipy.sparse import csr_matrix

MASK = (1 << 64)-1


def mix(z):
    z &= MASK
    z = ((z ^ (z >> 30))*0xbf58476d1ce4e5b9) & MASK
    z = ((z ^ (z >> 27))*0x94d049bb133111eb) & MASK
    return z ^ (z >> 31)


def height(x,p):
    seed = 18444453+p*1000003
    h = mix(seed ^ mix(x + 0x6a09e667f3bcc909))
    u = ((h >> 11)+0.5)*2.0**-53
    return min(100000001,math.floor(u**-3.0))


def killed_moments(N,p):
    radius, ceiling = 4*N,math.floor((4*N)**1.5)
    actual = {x:height(x,p) for x in range(-radius,radius+1)}
    states = [(x,y) for x in actual for y in range(min(actual[x],ceiling)+1)]
    ix = {v:i for i,v in enumerate(states)}
    rows,cols,values = [],[],[]
    for v,i in ix.items():
        x,y = v
        neighbors = [(x-1,0),(x+1,0),(x,1)] if y == 0 else [(x,y-1)] + ([(x,y+1)] if y<actual[x] else [])
        for w in neighbors:
            if w in ix:
                rows.append(ix[w]);cols.append(i);values.append(1.0/len(neighbors))
    PT = csr_matrix((values,(rows,cols)),shape=(len(ix),len(ix)))
    backbone = np.array([ix[x,0] for x in range(-N,N+1)])
    B = len(backbone)
    prob = np.zeros((len(ix),B))
    prob[backbone,np.arange(B)] = 1.0
    length = N**3
    prefix = np.zeros((length+1,B))
    for k in range(1,length+1):
        prob = PT @ prob
        prefix[k] = prefix[k-1]+(prob[backbone]**2).sum(axis=0)
    origin = prob[:,N].copy()
    first, cross = 0.0,0.0
    for n in range(length,2*length+1):
        if n>length:
            origin = PT @ origin
        earlier = origin[backbone]**2
        first += earlier.sum()
        cross += earlier @ prefix[2*length-n]
    second = first+2*cross
    return dict(N=N,profile=p,states=len(ix),mean=first,second=second,
                second_over_mean_squared=second/first**2,
                second_over_mean=second/first,
                ratio_over_logN=second/(first**2*math.log(N)))


def read_csv(path):
    with open(path) as f:
        return list(csv.DictReader(line for line in f if not line.startswith("#")))


def main():
    start = time.monotonic()
    result = {"constants":{"cl":1,"cu":2,"b":4},"deterministic_moments":[]}
    sampled = read_csv("moments_critical.csv")
    for N in (4,8,16):
        for p in range(6):
            r = killed_moments(N,p)
            mc = next(z for z in sampled if int(z["N"])==N and int(z["profile"])==p)
            r["MC_mean_z"] = (float(mc["mean"])-r["mean"])/float(mc["mean_se"])
            r["MC_second_z"] = (float(mc["second"])-r["second"])/float(mc["second_se"])
            result["deterministic_moments"].append(r)
            print(json.dumps(r),flush=True)
            if time.monotonic()-start > 230:
                raise RuntimeError("time budget")
    result["long_run_summary"] = []
    for label in ("subcritical","critical","supercritical"):
        data = read_csv("simulation_"+label+".csv")
        for t in (100000,1000000,10000000,100000000):
            selected = [r for r in data if int(r["time"])==t]
            allc = [int(r["all_collisions"]) for r in selected]
            back = [int(r["backbone_collisions"]) for r in selected]
            result["long_run_summary"].append(dict(regime=label,time=t,all_by_profile=allc,
                backbone_by_profile=back,mean_all=float(np.mean(allc)),mean_backbone=float(np.mean(back))))
    result["sampled_moment_summary"] = []
    for N in (4,8,16,32,64):
        selected = [r for r in sampled if int(r["N"])==N]
        mean = float(np.mean([float(r["mean"]) for r in selected]))
        second = float(np.mean([float(r["second"]) for r in selected]))
        result["sampled_moment_summary"].append(dict(N=N,mean=mean,second=second,
            pooled_ratio=second/mean**2,pooled_ratio_over_logN=second/(mean**2*math.log(N)),
            mean_quenched_ratio=float(np.mean([float(r["second_over_mean_squared"]) for r in selected])),
            probability_positive=float(np.mean([float(r["prob_positive"]) for r in selected]))))
    result["elapsed_seconds"] = time.monotonic()-start
    with open("numerical_checks.json","w") as f:
        json.dump(result,f,indent=2)
        f.write("\n")
    print("elapsed_seconds",result["elapsed_seconds"])


if __name__ == "__main__":
    main()
