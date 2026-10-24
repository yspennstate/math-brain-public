from itertools import product
import networkx as nx

MOD=3

def reconstruct_x(w,r):
    x=[r%3]
    for wi in w:
        x.append((wi-1-x[-1])%3)
    return x

def cycle_colors(w):
    l=len(w)
    return [ (w[i-1]+w[i])%3 for i in range(l) ]

def valid_transparent_cycle_word(w,r,s):
    l=len(w)
    if l<4: return False
    x=reconstruct_x(w,r)
    if x[-1]%3 != r%3: return False
    c=cycle_colors(w)
    if c[0] != 0: return False
    if c[1] == s%3 or c[-1] == s%3: return False
    for i in range(1,l-1):
        if c[i] == c[i+1]: return False
    return True

def find_word(l,r,s):
    for w in product(range(3), repeat=l):
        if valid_transparent_cycle_word(w,r,s):
            return tuple(w)
    return None

def negate_word(w):
    return tuple((-a)%3 for a in w)

def extend6(w):
    w=list(w); l=len(w)
    if l%2==0:
        e,o=w[-2],w[-1]
        extra=[e+1,o+1,e+2,o+2,e,o]
    else:
        e,o=w[-1],w[-2]
        extra=[o+1,e+1,o+2,e+2,o,e]
    return tuple(w+[z%3 for z in extra])

rep_pairs=[(0,0),(0,1),(0,2),(1,0),(1,1)]
base_table={}
for l in (4,6,8):
    for s in (0,1):
        base_table[(l,0,s)]=find_word(l,0,s)
for l in (5,7,9):
    for r,s in rep_pairs:
        base_table[(l,r,s)]=find_word(l,r,s)
assert all(w is not None for w in base_table.values())

all_base={}
for l in range(4,10):
    for r in range(3):
        for s in range(3):
            w=find_word(l,r,s)
            assert w is not None
            all_base[(l,r,s)]=w

even_r_independence=True
for l in (4,6,8):
    for s in range(3):
        w=all_base[(l,0,s)]
        even_r_independence &= all(valid_transparent_cycle_word(w,r,s) for r in range(3))
odd_negation_symmetry=True
for l in (5,7,9):
    for r in range(3):
        for s in range(3):
            w=all_base[(l,r,s)]
            odd_negation_symmetry &= valid_transparent_cycle_word(negate_word(w),(2-r)%3,(-s)%3)
assert even_r_independence and odd_negation_symmetry

extension_failures=[]
for l0 in range(4,10):
    for r in range(3):
        for s in range(3):
            w=all_base[(l0,r,s)]
            for _ in range(9):
                w=extend6(w)
                if not valid_transparent_cycle_word(w,r,s):
                    extension_failures.append((l0,r,s,len(w),w)); break
assert not extension_failures

def triangle_Ts(r,s):
    Ts=set()
    for x,y in product(range(3), repeat=2):
        w0=(1+r+x)%3; w1=(1+x+y)%3; w2=(1+y+r)%3
        cu=(w0+w1)%3; cv=(w1+w2)%3; T=(w0+w2)%3
        if len({s%3,cu,cv})==3:
            Ts.add(T)
    return Ts
triangle_table={(r,s):triangle_Ts(r,s) for r in range(3) for s in range(3)}
for r in range(3):
    for s in range(3):
        expected={0,1,2} if s==(r-1)%3 else set()
        assert triangle_table[(r,s)]==expected

def triangle_xy(r,s,T):
    for x,y in product(range(3), repeat=2):
        w0=(1+r+x)%3; w1=(1+x+y)%3; w2=(1+y+r)%3
        cu=(w0+w1)%3; cv=(w1+w2)%3
        if (w0+w2)%3==T%3 and len({s%3,cu,cv})==3:
            return x,y
    return None

def two_triangle_core(k):
    G=nx.Graph(); rho={}
    if k==0:
        a=0; rho[a]=0; s=(rho[a]-1)%3
        left=(1,2); right=(3,4)
        G.add_edges_from([(a,left[0]),(left[0],left[1]),(left[1],a),
                          (a,right[0]),(right[0],right[1]),(right[1],a)])
        T1=0; T2=s
        xy1=triangle_xy(rho[a],s,T1); xy2=triangle_xy(rho[a],s,T2)
        assert xy1 and xy2
        rho[left[0]],rho[left[1]]=xy1
        rho[right[0]],rho[right[1]]=xy2
    else:
        path=list(range(k+1)); nxt=k+1
        for i,p in enumerate(path): rho[p]=i%3
        G.add_edges_from((path[i],path[i+1]) for i in range(k))
        left=(nxt,nxt+1); nxt+=2; right=(nxt,nxt+1)
        G.add_edges_from([(path[0],left[0]),(left[0],left[1]),(left[1],path[0]),
                          (path[-1],right[0]),(right[0],right[1]),(right[1],path[-1])])
        s0=(rho[path[0]]-1)%3; sk=(rho[path[-1]]-1)%3
        q0=(1+rho[path[0]]+rho[path[1]])%3
        qk=(1+rho[path[-2]]+rho[path[-1]])%3
        T0=(s0-q0)%3; Tk=(sk-qk)%3
        xy1=triangle_xy(rho[path[0]],s0,T0); xy2=triangle_xy(rho[path[-1]],sk,Tk)
        assert xy1 and xy2
        rho[left[0]],rho[left[1]]=xy1
        rho[right[0]],rho[right[1]]=xy2
    return G,rho

def is_proper_integer(G,rho):
    sig={v:G.degree(v)*(1+rho[v])+sum(rho[u] for u in G.neighbors(v)) for v in G.nodes()}
    return all(sig[u]!=sig[v] for u,v in G.edges())

two_triangle_fail=[]
for k in range(0,31):
    G,rho=two_triangle_core(k)
    if not is_proper_integer(G,rho) or max(rho.values())>2:
        two_triangle_fail.append(k)
assert not two_triangle_fail

def is_cactus(G):
    if not nx.is_connected(G): return False
    for edges in nx.biconnected_component_edges(G):
        E=list(edges)
        if len(E)<=1: continue
        verts=set()
        for u,v in E: verts.add(u); verts.add(v)
        if len(E)!=len(verts): return False
        deg={v:0 for v in verts}
        for u,v in E: deg[u]+=1; deg[v]+=1
        if any(d!=2 for d in deg.values()): return False
    return True

def exact_012_witness(G):
    nodes=list(G.nodes())
    for vals in product(range(3), repeat=len(nodes)):
        rho=dict(zip(nodes,vals))
        if is_proper_integer(G,rho): return vals
    return None

atlas_counts={}; atlas_fail=[]
for G0 in nx.graph_atlas_g():
    n=len(G0)
    if n<1 or n>7 or not nx.is_connected(G0): continue
    if G0.number_of_edges()-n+1 !=2: continue
    if not is_cactus(G0): continue
    atlas_counts[n]=atlas_counts.get(n,0)+1
    if exact_012_witness(G0) is None:
        atlas_fail.append(nx.to_graph6_bytes(G0,header=False).decode().strip())
assert not atlas_fail

print('MODEL_NOTE=checker is exact finite validation only; theorem is the written proof')
print('representative_base_word_count=',len(base_table))
for key in sorted(base_table): print('base',key,'=', ''.join(map(str,base_table[key])))
print('all_l4_to_l9_parameter_triples=',len(all_base))
print('even_r_independence=',even_r_independence)
print('odd_negation_symmetry=',odd_negation_symmetry)
print('six_extension_failures=',extension_failures)
print('six_extension_verified_through_max_length=',9+9*6)
print('triangle_interface=',{str(k):sorted(v) for k,v in triangle_table.items()})
print('two_triangle_path_k_checked=0..30')
print('two_triangle_failures=',two_triangle_fail)
print('atlas_bicyclic_cactus_counts=',atlas_counts)
print('atlas_bicyclic_cactus_failures=',atlas_fail)
print('VERDICT=PASS')
