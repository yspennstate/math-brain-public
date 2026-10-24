import json,itertools,math,time
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def save(key,statement,data):
    data.update(problem_id=key,audit_status='PENDING w347',command='python -B -X utf8 checks/batch_one.py')
    (root/'checks'/f'{key}_receipt.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    with (root/'results.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'row':'S1.O.w331.'+key,'problem_id':key,'label':'proof of special case/reduction; exact or numerical controls','statement':statement,'proof_path':str(root/'proofs'/f'{key}.md'),'measurement':data,'audit_status':'PENDING w347'})+'\n')
    print(json.dumps(data),flush=True)
start=time.perf_counter(); errors=[]
for a in [.1,1,3]:
    for x in [.01,.1,.5,1,2,10,100]: errors.append(abs(math.exp(-a/(2*x))**2-math.exp(-a/x)))
assert max(errors)<1e-14
save('P0355','Strict-discount zero-mark binary Frechet fixed points are nonendogenous; a finite-r-moment contraction gives an endogenous sufficient condition whose parameter range excludes these heavy tails.',{'fixed_point_values_checked':len(errors),'max_fixed_point_error':max(errors),'finite_half_moment_a1':math.gamma(.5),'half_moment_contraction':2*.5**.5,'second_moment_contraction':2*.5**2,'second_moment':'infinite','elapsed_seconds':time.perf_counter()-start})
start=time.perf_counter(); moments=[]
for k in range(1,5):
    atomic=F(1,6)+F(2,3)*F(1,2)**k; uniform=F(1,k+1); moments.append({'order':k,'uniform':str(uniform),'three_atom':str(atomic)})
    if k<=3: assert atomic==uniform
    else: assert atomic!=uniform
save('C0075','All normalised moment measures suffice for weak convergence of random probability measures; their mass is one. First three moment measures do not determine the random-measure law.',{'moment_controls':moments,'fourth_moment_gap':str(F(5,24)-F(1,5)),'normalised_moment_mass':1,'elapsed_seconds':time.perf_counter()-start})
start=time.perf_counter(); grids=[]
for height,width in [(2,2),(2,3),(3,3)]:
    n=height*width; neighbours=[]
    for v in range(n):
        r,c=divmod(v,width); neighbours.append([rr*width+cc for rr,cc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] if 0<=rr<height and 0<=cc<width])
    distances=Counter(); two=0
    for labels in itertools.permutations(range(n)):
        peaks=[v for v in range(n) if all(labels[v]>labels[w] for w in neighbours[v])]
        if len(peaks)==2:
            two+=1; a,b=peaks; ar,ac=divmod(a,width); br,bc=divmod(b,width); distances[abs(ar-br)+abs(ac-bc)]+=1
    assert sum(distances.values())==two and 1 not in distances
    if n==4: assert two==8
    grids.append({'grid':[height,width],'permutations':math.factorial(n),'two_peak_count':two,'graph_distance_counts':dict(sorted(distances.items()))})
save('P0029','A nonempty independent vertex set is exactly an attainable peak set on a finite connected graph; both near and far two-peak pairs occur on square grids.',{'exact_grid_counts':grids,'elapsed_seconds':time.perf_counter()-start})
