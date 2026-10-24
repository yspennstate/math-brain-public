import csv, glob
from fractions import Fraction
rows=[]
for f in ["rr_lp_results.csv"]+sorted(glob.glob("rr_lp_results_W*.csv")):
    try:
        for r in csv.reader(open(f)):
            if r: rows.append(r)
    except FileNotFoundError: pass
seen=set(); uniq=[]
for r in rows:
    k=(r[0],r[1])
    if k in seen: continue
    seen.add(k); uniq.append(r)
uniq.sort(key=lambda r:(int(r[0]),int(r[1])))
print(open("table_headers.txt",encoding="utf-8").read().split(chr(10))[1])
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in uniq:
    d,n,seed,mu2,t2,diam,meand,best,rb,F,ub,ratio,lim,secs=r
    print(f"| {d} | {n} | {float(mu2):.4f} | {float(t2):.4f} | {diam} | {float(meand):.2f} | {float(best):.4f} | {rb} | {float(F):.4f} | {float(ub):.4f} | {float(ratio):.3f} | {float(lim):.3f} |")
print()
print(open("table_headers.txt",encoding="utf-8").read().split(chr(10))[3])
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
try:
    for r in csv.reader(open("rr_dual_large_results.csv")):
        if not r: continue
        d,n,mu2,t2,diam,meand,best,rb,bb,ub,ratio,lim,secs=r
        print(f"| {d} | {n} | {float(mu2):.4f} | {float(t2):.4f} | {diam} | {float(meand):.2f} | {float(best):.4f} | {rb} | {bb} | {float(ub):.4f} | {float(ratio):.3f} | {float(lim):.3f} |")
except FileNotFoundError: pass
print()
try:
    print(open("table_headers.txt",encoding="utf-8").read().split(chr(10))[5])
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in csv.reader(open("lps_results.csv")):
        if not r: continue
        p,q,n,d,simple,mu2,tsp,t2,diam,meand,best,rb,bb,ub,ratio,lim,secs=r
        print(f"| {p} | {q} | {n} | {d} | {simple} | {float(mu2):.4f} | {float(tsp):.4f} | {float(t2):.4f} | {diam} | {float(meand):.2f} | {float(best):.4f} | {rb} | {bb} | {float(ub):.4f} | {float(ratio):.3f} | {float(lim):.3f} |")
except FileNotFoundError: pass
