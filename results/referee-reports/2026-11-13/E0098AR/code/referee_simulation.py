"""Independent matrix experiment. Does not import/read claim_files/code or data."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import csv
import json
import math
import resource
import time
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.stats import kstest
from threadpoolctl import threadpool_info, threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
RATE = math.sqrt(2 / math.pi)

def governor():
    p = Path.home() / ".claude/compute/compute_state.json"
    if p.exists():
        state = json.loads(p.read_text())
        if state.get("status") == "distress":
            raise RuntimeError("compute governor distress: stop and preserve flushed samples")

def matrix(rng, n, ensemble):
    ii, jj = np.triu_indices(n, 1)
    a = np.empty((n, n), dtype=np.float64, order="F")
    if ensemble == "GOE":
        x = rng.normal(size=len(ii))
        diag = rng.normal(scale=math.sqrt(2), size=n)
    else:
        x = rng.integers(0, 2, size=len(ii)) * 2 - 1
        diag = rng.integers(0, 2, size=n) * 2 - 1
    a[ii, jj] = x
    a[jj, ii] = x
    a[np.diag_indices(n)] = diag
    a /= math.sqrt(n)
    return a

def summarize(rows, out):
    keys = sorted(set((r["ensemble"], r["n"], r["index"]) for r in rows))
    summaries = []
    for ensemble, n, index in keys:
        group = [r for r in rows if (r["ensemble"], r["n"], r["index"]) == (ensemble,n,index)]
        x = np.array([r["scaled_min"] for r in group])
        m = len(x)
        test = kstest(x, "expon", args=(0, 1 / RATE), method="exact")
        s = dict(ensemble=ensemble, n=n, index=index, samples=m,
                 mean=float(x.mean()), mean_se=float(x.std(ddof=1)/math.sqrt(m)),
                 median=float(np.median(x)), ks=float(test.statistic), p=float(test.pvalue),
                 dkw95=math.sqrt(math.log(40)/(2*m)),
                 floating_zero=sum(r["floating_zero"] for r in group),
                 below_1e_12=sum(r["min_abs"] < 1e-12 for r in group))
        for t in (0.5, 1., 2.):
            counts = np.array([r["count_" + str(t)] for r in group])
            s["cdf_" + str(t)] = float(np.mean(x <= t))
            s["count_mean_" + str(t)] = float(counts.mean())
            s["count_factorial2_" + str(t)] = float(np.mean(counts*(counts-1)))
        summaries.append(s)
    with (out / "summary.csv").open("w") as f:
        w=csv.DictWriter(f, fieldnames=list(summaries[0])); w.writeheader(); w.writerows(summaries)
    return summaries

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--spec", default="128:1200,512:600,1024:250,2000:120")
    p.add_argument("--seed", type=int, default=918273645)
    args = p.parse_args()
    governor()
    start = time.monotonic()
    out = ROOT / "data"
    out.mkdir(exist_ok=True)
    rows = []
    fields = ["ensemble", "n", "matrix", "index", "j", "lambda", "min_abs", "scaled_min",
              "floating_zero", "residual", "norm_error", "count_0.5", "count_1.0", "count_2.0"]
    rng = np.random.default_rng(args.seed)
    with threadpool_limits(limits=1), (out / "samples.csv").open("x") as f:
        writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader()
        for n, m in (map(int,s.split(":")) for s in args.spec.split(",")):
            for ensemble in ("GOE", "Rademacher"):
                begin = time.monotonic()
                for trial in range(m):
                    if trial % 10 == 0:
                        governor()
                        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 3_800_000_000
                    a = matrix(rng,n,ensemble)
                    for index, j in (("lower",0), ("bulk",n//2), ("upper",n-1)):
                        lam, u = eigh(a, subset_by_index=(j,j), driver="evr", check_finite=False)
                        v = u[:,0]
                        minimum = float(np.min(np.abs(v)))
                        residual = float(np.linalg.norm(np.einsum("ij,j->i", a, v)-lam[0]*v))
                        norm_error = float(abs(np.linalg.norm(v)-1))
                        assert residual < 1e-10 and norm_error < 1e-12
                        scaled = n**1.5*np.abs(v)
                        row = dict(ensemble=ensemble,n=n,matrix=trial,index=index,j=j+1,
                                   lambda_=float(lam[0]),min_abs=minimum,scaled_min=float(scaled.min()),
                                   floating_zero=int(minimum==0),residual=residual,norm_error=norm_error)
                        row["lambda"] = row.pop("lambda_")
                        for t in (0.5,1.,2.): row["count_"+str(t)] = int(np.sum(scaled<=t))
                        rows.append(row); writer.writerow(row)
                    f.flush()
                print(ensemble,n,m,"seconds",round(time.monotonic()-begin,2),flush=True)
        meta = dict(seed=args.seed,spec=args.spec,rate=RATE,threads=threadpool_info(),
                    numpy=np.__version__,scipy=scipy.__version__,seconds=time.monotonic()-start,
                    rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                    max_residual=max(r["residual"] for r in rows),
                    max_norm_error=max(r["norm_error"] for r in rows),
                    matrices=len(rows)//3,selected_eigenvectors=len(rows),
                    priority="inherited from supplied launch.sh: nice -n 10; sandbox denies priority inspection")
        (out/"metadata.json").write_text(json.dumps(meta,indent=2)+"\n")
    summaries = summarize(rows,out)
    print(json.dumps(meta),flush=True)
    print("summary groups",len(summaries),flush=True)

if __name__ == "__main__": main()
