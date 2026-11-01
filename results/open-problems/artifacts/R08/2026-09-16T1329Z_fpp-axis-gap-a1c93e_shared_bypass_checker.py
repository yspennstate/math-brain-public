from fractions import Fraction
import heapq

def build(m, eps):
    L=m+1
    H=Fraction(10*L+10,1)+eps
    verts=[(x,y) for x in range(L+1) for y in (0,1)]
    adj={v:[] for v in verts}
    def add(a,b,w):
        # nearest-neighbor square-lattice edge
        assert abs(a[0]-b[0])+abs(a[1]-b[1])==1
        assert w>0
        adj[a].append((b,w))
        adj[b].append((a,w))
    for x in range(L):
        add((x,0),(x+1,0),Fraction(1))
        add((x,1),(x+1,1),Fraction(1))
    add((0,0),(0,1),eps/Fraction(2))
    add((L,0),(L,1),eps/Fraction(2))
    for x in range(1,L):
        add((x,0),(x,1),H)
    marked=[((x,0),(x+1,0)) for x in range(m)]
    return adj,(0,0),(L,0),marked,Fraction(L),Fraction(L)+eps

def shortest(adj,s,t,deleted=None):
    # exact Dijkstra + exact count of shortest paths
    inf=None
    dist={v:inf for v in adj}
    count={v:0 for v in adj}
    dist[s]=Fraction(0); count[s]=1
    pq=[(Fraction(0),s)]
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]: continue
        for v,w in adj[u]:
            if deleted is not None and frozenset((u,v))==deleted:
                continue
            nd=d+w
            if dist[v] is None or nd<dist[v]:
                dist[v]=nd
                count[v]=count[u]
                heapq.heappush(pq,(nd,v))
            elif nd==dist[v]:
                count[v]+=count[u]
    return dist[t],count[t]

def run():
    eps_list=[Fraction(1,7),Fraction(2,5),Fraction(3,2),Fraction(17,13)]
    cases=0
    for m in range(1,21):
        for eps in eps_list:
            adj,s,t,marked,base,bypass=build(m,eps)
            d,c=shortest(adj,s,t)
            assert d==base,(m,eps,d,base)
            assert c==1,(m,eps,c)
            for e in marked:
                dd,cc=shortest(adj,s,t,frozenset(e))
                assert dd==bypass,(m,eps,e,dd,bypass)
                assert cc==1,(m,eps,e,cc)
            cases+=1
    print("R08-X001 exact shared-bypass checker")
    print("cases",cases)
    print("m range 1..20")
    print("eps",",".join(map(str,eps_list)))
    print("all graphs: finite nearest-neighbor subgraphs of Z^2, all weights positive rationals")
    print("baseline: unique shortest path cost L=m+1")
    print("each of first m bottom edges deleted: unique shortest path cost L+eps")
    print("deletion margin for every marked edge: exactly eps")
    print("PASS")

if __name__=="__main__":
    run()
