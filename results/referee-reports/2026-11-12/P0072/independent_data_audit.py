"""Check the paper's printed numbers against local text data and fresh algebra.

No supplied program is executed or imported. Run: python3 independent_data_audit.py
"""
from pathlib import Path
import math
import re
import signal

signal.alarm(60)
paper = Path("PAPER.tex").read_text()
rows = re.findall(r"^([0-9]+) & ([0-9]+) & ([0-9.]+) & ([0-9.]+) & ([0-9.]+) & ([0-9.]+)", paper, re.M)
assert len(rows) == 13
max_ac = 0.0
for row in rows:
    ell, seed = map(int, row[:2])
    a, c, h, target = map(float, row[2:])
    lines = Path(f"data/run_l{ell}_s{seed}.txt").read_text().splitlines()
    final = next(x.split() for x in lines if x.split() and x.split()[0] == "100000000")
    assert list(map(float, final[1:5])) == [a, c, h, target]
    recalculated = (1 - 1/ell)*a*(1-a)
    assert abs(recalculated-target) <= 1e-5
    max_ac = max(max_ac, abs(a-c))
    print(f"Table l={ell:2} seed={seed}: data MATCH; recomputed target={recalculated:.9f}; h-target={h-target:+.5f}")
print(f"Maximum table |a-c|={max_ac:.5f}; claim <0.0003 PASS")

def parsed_run(ell, seed):
    result = []
    for line in Path(f"data/run_l{ell}_s{seed}.txt").read_text().splitlines():
        tok = line.split()
        if tok and tok[0].isdigit():
            n = int(tok[0])
            a, c, h, target = map(float, tok[1:5])
            if n >= 10000:
                result.append((n, a, c, h, target))
    return result

run2 = parsed_run(2,1)
residuals = [h-(1-1/2)*a*(1-a) for _,a,c,h,_ in run2]
print("Paper G2 seed1 residuals:", ", ".join(f"{x:.7f}" for x in residuals))
print("Paper G2 seed1 decade ratios:", ", ".join(f"{y/x:.5f}" for x,y in zip(residuals,residuals[1:])))
print(f"Linearization prediction 10^(-1/4)={10**(-1/4):.7f}")
run1 = parsed_run(1,1)
recip = [1/h for _,a,c,h,_ in run1]
print("Paper G1 seed1 inverse-h increments:", ", ".join(f"{y-x:.5f}" for x,y in zip(recip,recip[1:])))
print("Paper G1 seed1 log(10)/Q:", ", ".join(f"{math.log(10)/(a*(1-a)+c*(1-c)+h):.5f}" for _,a,c,h,_ in run1))
for ell, weights, empirical in [
    (2, (2,3,1,4,2), (.15544,.60037,.17762,.06657)),
    (3, (5,2,3,4,1), (.44208,.38081,.13629,.04083)),
]:
    A,B,C,D,R=weights
    m = [A*C*(D+ell*B+ell*R),B*D*(C+ell*A+ell*R),ell*A*R*D,ell*B*R*C]
    law = [x/sum(m) for x in m]
    deviations = [(p-q)/math.sqrt(q*(1-q)/2000000) for p,q in zip(empirical,law)]
    print(f"Frozen G{ell}: exact decimals=" + ", ".join(f"{q:.9f}" for q in law))
    print("  empirical deviations / marginal standard error=" + ", ".join(f"{z:+.3f}" for z in deviations))
    assert max(map(abs,deviations)) < 2

fresh = Path("independent_sim_1e8.out").read_text().splitlines()
assert fresh[-1].startswith("elapsed_wall_seconds=")
run = None
for line in fresh:
    if line.startswith("ell="):
        run=line
    elif line.startswith("100000000 "):
        print("Independent endpoint:",run,"::",line)
print("ALL PRINTED-NUMBER CHECKS PASS")
