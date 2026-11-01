from itertools import permutations
from math import factorial

# Independent P14 audit of HARD10-N9-DENSE-UNIT-PAIR-20260916-01.
# This does not reuse HARD10's forest recurrence.  It independently checks
# Burnside graph counts / edge-histogram coverage arithmetic and brute-forces
# all 2^19 edge subsets of HARD10's reported minimum-positive-gap graph.

def burnside_graphs(n):
    edges=[(i,j) for j in range(1,n) for i in range(j)]
    idx={e:k for k,e in enumerate(edges)}
    idx.update({(j,i):k for k,(i,j) in enumerate(edges)})
    total=0
    for p in permutations(range(n)):
        seen=[False]*len(edges); orbits=0
        for k,(i,j) in enumerate(edges):
            if seen[k]: continue
            orbits+=1; cur=k
            while not seen[cur]:
                seen[cur]=True
                a,b=edges[cur]
                cur=idx[(p[a],p[b])]
        total += 1<<orbits
    assert total%factorial(n)==0
    return total//factorial(n)

hist=[1,1,2,5,11,25,63,148,345,771,1637,3252,5995,10120,15615,21933,27987,32403,34040,32403,27987,21933,15615,10120,5995,3252,1637,771,345,148,63,25,11,5,2,1,1]
print('hist_sum=',sum(hist))
print('hist_sym=',all(hist[i]==hist[36-i] for i in range(37)))
print('dense_19_36=',sum(hist[19:]))
pair_checks=sum(hist[m]*m*(m-1)//2 for m in range(19,37))
print('dense_pair_checks=',pair_checks)
assert pair_checks==25304635
assert sum(hist)==274668 and sum(hist[19:])==120314 and all(hist[i]==hist[36-i] for i in range(37))
print('Burnside_U9=',burnside_graphs(9))
assert burnside_graphs(8)==12346
assert burnside_graphs(9)==274668

# Decode the graph6 serialization used by HARD10 (n<=62, pair order j then i).
def decode_g6(s):
    n=ord(s[0])-63
    bits=[]
    for ch in s[1:]:
        v=ord(ch)-63
        bits += [(v>>(5-b))&1 for b in range(6)]
    edges=[]; k=0
    for j in range(1,n):
        for i in range(j):
            if bits[k]: edges.append((i,j))
            k+=1
    return n,edges

def forest_counts(n,edges,eidx,fidx):
    m=len(edges); Z=Ze=Zf=Zef=0
    for mask in range(1<<m):
        parent=list(range(n))
        def find(a):
            while parent[a]!=a:
                parent[a]=parent[parent[a]]; a=parent[a]
            return a
        ok=True
        for k,(u,v) in enumerate(edges):
            if (mask>>k)&1:
                ru,rv=find(u),find(v)
                if ru==rv: ok=False; break
                parent[ru]=rv
        if not ok: continue
        Z+=1
        he=(mask>>eidx)&1; hf=(mask>>fidx)&1
        Ze+=he; Zf+=hf; Zef+=he&hf
    return Z,Ze,Zf,Zef,Ze*Zf-Z*Zef

n,edges=decode_g6('HGC[~Nf')
print('min_graph_n=',n,'m=',len(edges),'edges=',edges)
res=forest_counts(n,edges,0,1)
print('min_graph Z Ze Zf Zef delta=',res)
assert res[-1]==4464
print('AUDIT PASS: HARD10 n=9 coverage arithmetic and min-gap witness independently verified')
