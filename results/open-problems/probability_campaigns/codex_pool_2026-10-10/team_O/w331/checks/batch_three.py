import json,itertools,time,math
from fractions import Fraction as F
from collections import deque
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def save(key,statement,data):
    data.update(problem_id=key,audit_status='PENDING w347',command='python -B -X utf8 checks/batch_three.py')
    (root/'checks'/f'{key}_receipt.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    with (root/'results.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'row':'S1.O.w331.'+key,'problem_id':key,'label':'proof of special case/obstruction; exact finite controls','statement':statement,'proof_path':str(root/'proofs'/f'{key}.md'),'measurement':data,'audit_status':'PENDING w347'})+'\n')
    print(json.dumps(data),flush=True)
def min_closure(costs,m):
    n=len(costs); source=n;sink=n+1; graph=[[] for _ in range(n+2)]; infinity=1+sum(abs(x) for x in costs)
    def edge(a,b,cap):
        graph[a].append([b,len(graph[b]),cap]);graph[b].append([a,len(graph[a])-1,0])
    negative=0
    for a,c in enumerate(costs):
        if c<0: edge(source,a,-c);negative-=c
        elif c>0: edge(a,sink,c)
        for bit in range(m):
            if not (a>>bit)&1: edge(a,a|(1<<bit),infinity)
    flow=0
    while True:
        level=[-1]*(n+2);level[source]=0;q=deque([source])
        while q:
            a=q.popleft()
            for b,rev,cap in graph[a]:
                if cap and level[b]<0:level[b]=level[a]+1;q.append(b)
        if level[sink]<0:break
        index=[0]*(n+2)
        def send(a,amount):
            if a==sink:return amount
            while index[a]<len(graph[a]):
                e=graph[a][index[a]];b,rev,cap=e
                if cap and level[b]==level[a]+1:
                    take=send(b,min(amount,cap))
                    if take:e[2]-=take;graph[b][rev][2]+=take;return take
                index[a]+=1
            return 0
        while True:
            amount=send(source,infinity)
            if not amount:break
            flow+=amount
    reached={source};q=deque([source])
    while q:
        a=q.popleft()
        for b,rev,cap in graph[a]:
            if cap and b not in reached:reached.add(b);q.append(b)
    witness=[a for a in range(n) if a in reached]
    minimum=flow-negative
    assert sum(costs[a] for a in witness)==minimum
    assert all((a|(1<<bit)) in witness for a in witness for bit in range(m) if not (a>>bit)&1)
    return minimum,witness
start=time.perf_counter()
graphs={'tree':(4,[(0,1),(1,2),(2,3)]),'triangle':(3,[(0,1),(1,2),(2,0)]),'cactus_two_triangles':(5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]),'theta_K23':(5,[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]),'K4':(4,list(itertools.combinations(range(4),2)))}
pvalues=[F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)];qvalues=[F(1,10),F(1,4),F(1,2),F(3,4),F(9,10),F(1)]
summaries=[];brute_checks=0;violations=[]
for name,(vertices,edges) in graphs.items():
    m=len(edges);counts=[];ranks=[]
    for mask in range(1<<m):
        parent=list(range(vertices))
        def find(v):
            while parent[v]!=v:v=parent[v]
            return v
        for bit,(a,b) in enumerate(edges):
            if (mask>>bit)&1:parent[find(a)]=find(b)
        counts.append(len({find(v) for v in range(vertices)}));ranks.append(mask.bit_count())
    for p in pvalues:
        for qval in qvalues:
            weights=[p.numerator**k*(p.denominator-p.numerator)**(m-k)*qval.numerator**comp*qval.denominator**(vertices-comp) for k,comp in zip(ranks,counts)]
            Z=sum(weights); Z1=sum(k*w for k,w in zip(ranks,weights)); costs=[w*(k*Z-Z1) for k,w in zip(ranks,weights)]
            assert sum(costs)==0
            minimum,witness=min_closure(costs,m)
            if name=='triangle':
                brute=0
                for event in range(1<<(1<<m)):
                    members=[a for a in range(1<<m) if (event>>a)&1]
                    if all((event>>(a|(1<<bit)))&1 for a in members for bit in range(m) if not (a>>bit)&1):
                        brute=min(brute,sum(costs[a] for a in members));brute_checks+=1
                assert brute==minimum
            if minimum<0:violations.append({'graph':name,'p':str(p),'q':str(qval),'minimum':minimum,'event':witness})
    summaries.append({'graph':name,'edge_configurations':1<<m,'parameter_pairs':len(pvalues)*len(qvalues)})
# Explicit witness that the algorithm detects a decreasing increasing-event derivative.
assert min_closure([1,-1],1)[0]==-1
assert not violations,violations
save('C0146','Finite free-boundary cactus FK graphs admit a simultaneous monotone p coupling for every q>0. Exact minimum-cut tests find no increasing-event derivative violation on the sampled theta and K4 parameters; arbitrary graphs and q=0 remain open here.',{'q_values':[str(q) for q in qvalues],'p_values':[str(p) for p in pvalues],'graph_controls':summaries,'all_upset_parameter_checks':sum(s['parameter_pairs'] for s in summaries),'triangle_brute_upset_evaluations':brute_checks,'negative_control_detected':True,'violations':violations,'elapsed_seconds':time.perf_counter()-start})
start=time.perf_counter();intervals=[(F(0),F(1))];deleted=0
for depth in range(1,11):
    next_intervals=[]
    for a,b in intervals:
        left=a+(b-a)/3;right=a+2*(b-a)/3;assert not (left<=F(1,4)<=right);deleted+=1
        next_intervals.extend([(a,left),(right,b)])
    intervals=next_intervals
assert F(1,4)==F(2,9)/(1-F(1,9))
save('P0021','Deleting all complementary-component boundaries from a planar zero-area connected compact set need not leave a totally disconnected set: the Sierpinski carpet retains the open line x=1/4.',{'cantor_deletion_stages':10,'closed_gap_projections_checked':deleted,'ternary_witness_exact':str(F(2,9)/(1-F(1,9))),'carpet_area_upper_bound_stage100':float(F(8,9)**100),'elapsed_seconds':time.perf_counter()-start})
