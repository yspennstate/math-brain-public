from pathlib import Path
from fractions import Fraction as F
import json, time
B=Path(__file__).resolve().parents[1]; start=time.monotonic(); w=4; r=16; checks=0
def ck(x):
    global checks
    checks+=1
    assert x,checks
# The actual positive-prime weights are lambda_(transversal,D)=t_D/w^r.
# Summing the w^(r-1) transversals containing any specified X coordinate gives
# total/w; every Y coordinate in D sees exactly t_D. These are all packing rows.
rows=[]
for ell in range(r):
    t=[F(3,4) if D==ell else F(1,4*(r-1)) for D in range(r)]
    ck(sum(t)==1);ck(all(0<x<=1 for x in t));ck(sum(t)/w<=1)
    ck(all(F(w**(r-1))*x/F(w**r)==x/w for x in t))
    rows.append(t)
good=[D for D in range(r) if all(t[D]<=F(2*w,r) for t in rows)]
ck(not good)
# Each individual vector has at least half good clauses; their intersection is empty.
ck(all(sum(x<=F(2*w,r) for x in t)>=r//2 for t in rows))
out={'status':'PASS','checks':checks,'seconds':time.monotonic()-start,'w':w,'r':r,'positive_references':r,'lambda_formula':'t_(ell,D)/w^r for every X transversal','special_clause_mass':'3/4','other_clause_mass':'1/60','sum_lambda_per_reference':'1','X_packing_row':'1/4','max_Y_packing_row':'3/4','single_reference_threshold':'1/2','common_good_clauses_using_invalid_L_independent_threshold':good,'scope':'Exact actual-prime feasible-weight boundary control only; no full queue cost evaluated and no successful unrestricted-mixture claim'}
(B/'out/BOUNDARY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(out))
