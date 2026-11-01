from collections import deque
import json
from pathlib import Path

root=Path(__file__).resolve().parent
checks=[]
for L in [3,4,5,10]:
    vertex=lambda x,y:(x%L)*L+(y%L)
    edges=[]
    dual=[]
    selected=set()
    for x in range(L):
        for y in range(L):
            i=len(edges)
            edges.append((vertex(x,y),vertex(x+1,y)))
            dual.append((vertex(x,y-1),vertex(x,y),(0,1)))
            if x<L-1:
                selected.add(i)
            i=len(edges)
            edges.append((vertex(x,y),vertex(x,y+1)))
            dual.append((vertex(x-1,y),vertex(x,y),(1,0)))
            if x==0 and y<L-1:
                selected.add(i)
    assert len(selected)==L*L-1
    parent=list(range(L*L))
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for i in selected:
        a,b=map(find,edges[i])
        assert a!=b
        parent[a]=b
    assert len({find(i) for i in range(L*L)})==1
    adjacency=[[] for _ in range(L*L)]
    active=set(range(len(dual)))-selected
    for i in active:
        u,v,(dx,dy)=dual[i]
        adjacency[u].append((v,(dx,dy),i))
        adjacency[v].append((u,(-dx,-dy),i))
    degrees=[len(xs) for xs in adjacency]
    todo=deque(i for i,d in enumerate(degrees) if d<=1)
    while todo:
        u=todo.popleft()
        for v,step,i in adjacency[u]:
            if i in active:
                active.remove(i)
                degrees[u]-=1
                degrees[v]-=1
                if degrees[v]==1:
                    todo.append(v)
    branch=[i for i,d in enumerate(degrees) if d>2]
    assert len(branch)==1 and degrees[branch[0]]==4
    s=branch[0]
    loops=[]
    seen=set()
    for first,step,e in adjacency[s]:
        if e not in active or e in seen:
            continue
        trail=[e]
        current,total,last_edge=first,step,e
        while current!=s:
            options=[(v,delta,i) for v,delta,i in adjacency[current] if i in active and i!=last_edge]
            assert len(options)==1
            nxt,delta,nxt_edge=options[0]
            trail.append(nxt_edge)
            total=(total[0]+delta[0],total[1]+delta[1])
            current,last_edge=nxt,nxt_edge
        assert len(trail)==len(set(trail))
        assert all(c%L==0 for c in total)
        winding=tuple(c//L for c in total)
        seen.update(trail)
        loops.append((set(trail),winding))
    assert len(loops)==2 and not loops[0][0]&loops[1][0]
    u,v=[item[1] for item in loops]
    canonical=lambda w:w if w[0]>0 or (w[0]==0 and w[1]>0) else (-w[0],-w[1])
    classes={canonical(u),canonical(v),canonical((u[0]+v[0],u[1]+v[1])),canonical((u[0]-v[0],u[1]-v[1]))}
    assert classes=={(1,0),(0,1),(1,1),(1,-1)}
    checks.append({'side':L,'tree_edges':len(selected),'core_edges':len(active),'distinct_trail_homotopy_classes_up_to_reversal':sorted(classes)})
receipt={'command':'python -X utf8 verify_torus_comb.py','exact_witness_checks':len(checks),'cases':checks,'violations':0,'scope':'literal edge-simple trails; intended source cycle convention needs independent review'}
(root/'p0133_comb_measurements.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
