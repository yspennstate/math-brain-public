"""Verify L3's formula with an independent exact linear-system solve."""
import json
import time
from fractions import Fraction as F
from pathlib import Path

start = time.perf_counter()
rows = []
for r in range(0, 8):
    positions = list(range(-r, r+1))
    size = len(positions)
    matrix = [[F(int(i==j)) for j in range(size)] + [F(1)] for i in range(size)]
    for i,x in enumerate(positions):
        p = F(1,2) if x==0 else (F(1,4) if x>0 else F(3,4))
        for y,prob in ((x+1,p),(x-1,1-p)):
            if -r<=y<=r:
                matrix[i][y+r] -= prob
    for column in range(size):
        pivot = next(i for i in range(column,size) if matrix[i][column])
        matrix[column],matrix[pivot] = matrix[pivot],matrix[column]
        scale = matrix[column][column]
        matrix[column] = [v/scale for v in matrix[column]]
        for i in range(size):
            if i!=column and matrix[i][column]:
                scale = matrix[i][column]
                matrix[i] = [a-scale*b for a,b in zip(matrix[i],matrix[column])]
    exact = matrix[r][-1]
    formula = F(3,2)*(3**(r+1)-1)-2*(r+1)
    assert exact==formula,(r,exact,formula)
    rows.append({"radius":r,"mean_exit_time":str(exact)})
partial = [sum(F(1,2**r)*(F(3,2)*(3**(r+1)-1)-2*(r+1)) for r in range(1,n+1)) for n in (2,4,6,8,10,12)]
assert time.perf_counter()-start<60,"compute gate expired"
result = {"command":"python -B -X utf8 verify_countermodel.py", "exact_linear_systems_checked":len(rows), "failed":0, "elapsed_seconds":round(time.perf_counter()-start,6), "rows":rows,"truncated_mixture_means":[{"max_radius":n,"value":str(v)} for n,v in zip((2,4,6,8,10,12),partial)], "limitation":"Divergence follows from the written geometric-growth proof; finite checks alone do not prove it. This countermodel omits C0041's iid, transience and dimension assumptions."}
Path(__file__).with_name("countermodel_checks.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
