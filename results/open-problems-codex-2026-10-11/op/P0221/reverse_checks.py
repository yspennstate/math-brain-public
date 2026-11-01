"""Exhaustive finite checks of the label reassignment used in reverse transfer."""
import itertools, json
from pathlib import Path

def partitions(n):
    blocks=[]
    def go(v):
        if v==n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(v)
            yield from go(v+1)
            b.pop()
        blocks.append([v]); yield from go(v+1); blocks.pop()
    yield from go(0)

checked=0
diagonal=0
examples=[]
for n in range(2,7):
    for blocks in partitions(n):
        owner={v:i for i,B in enumerate(blocks) for v in B}
        edges=[(u,v) for u in range(n) for v in range(n) if u!=v and owner[u]!=owner[v]]
        for M in (2,3,4):
            def component_class(j):
                return ('large',j) if len(blocks[j])>=M else ('small',len(blocks[j]))
            for u,v in edges:
                I,J=owner[u],owner[v]
                for x,y in edges:
                    X,Y=owner[x],owner[y]
                    if component_class(I)!=component_class(X) or component_class(J)!=component_class(Y):
                        continue
                    component_map={I:X,J:Y}
                    for size in range(1,n+1):
                        source=[j for j,B in enumerate(blocks) if len(B)==size and j not in component_map]
                        target=[j for j,B in enumerate(blocks) if len(B)==size and j not in component_map.values()]
                        assert len(source)==len(target)
                        # Large components are fixed; their two forced endpoint assignments
                        # are already identities because each large component is its own class.
                        if size>=M:
                            assert source==target
                        component_map.update(zip(source,target))
                    assert len(set(component_map.values()))==len(blocks)
                    vertex_map={u:x,v:y}
                    for source,target in component_map.items():
                        left=[z for z in blocks[source] if z not in vertex_map]
                        right=[z for z in blocks[target] if z not in vertex_map.values()]
                        assert len(left)==len(right)
                        vertex_map.update(zip(left,right))
                    assert len(vertex_map)==n and set(vertex_map.values())==set(range(n))
                    assert vertex_map[u]==x and vertex_map[v]==y
                    assert all({vertex_map[z] for z in blocks[j]}==set(blocks[component_map[j]])
                               for j in range(len(blocks)))
                    assert all(component_map[j]==j for j,B in enumerate(blocks) if len(B)>=M)
                    checked+=1
                    diagonal+=int(len(blocks[I])==len(blocks[J]) and len(blocks[I])<M)

out={'vertices':'2 through 6','cutoffs':[2,3,4],
     'exact_reassignments_checked':checked,'same_small_class_cases':diagonal,
     'scope':'All partitions and all oriented cross-bundle source/target edges of compatible classes. Whole-bundle preservation implies containment for every physical forest refining those bundles.'}
Path(__file__).with_name('reverse_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
