#!/usr/bin/env python3
"""One-worker exact SAW counts; finite counts are not infinite connective constants."""
import collections, csv, itertools, json, math, os, pathlib, resource, subprocess, time
ROOT=pathlib.Path(__file__).resolve().parents[1]
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
# Address space remains tiny: only finite fibers and polynomial-size graph balls.
assert os.getpriority(os.PRIO_PROCESS,0) >= 10

def ball(neighbors, root, depth):
    vertices=[root]; indices={root:0}; distances=[0]
    for v in vertices:
        if distances[indices[v]]==depth: continue
        for w in neighbors(v):
            if w not in indices:
                indices[w]=len(vertices); vertices.append(w)
                distances.append(distances[indices[v]]+1)
    adjacency=[[indices[w] for w in neighbors(v) if w in indices] for v in vertices]
    for i,a in enumerate(adjacency):
        assert len(a)==len(set(a)) and i not in a
        assert all(i in adjacency[j] for j in a)
    return vertices,adjacency

def python_check(a, depth):
    # Independent breadth-first construction of explicit vertex sequences.
    frontier=[(0,)]
    result=[1]
    for _ in range(depth):
        frontier=[p+(w,) for p in frontier for w in a[p[-1]] if w not in p]
        result.append(len(frontier))
    return result

def run(name,kind,degree,neighbors,root,depth,height=lambda v:0, bridge=False, meta=None):
    started=time.monotonic()
    vertices,a=ball(neighbors,root,depth)
    payload=f'{len(vertices)} 0 {depth}\n'+''.join(f'{height(v)} {len(a[i])} '+ ' '.join(map(str,a[i]))+'\n' for i,v in enumerate(vertices))
    r=subprocess.run([str(ROOT/'code'/'enumerate')],input=payload,text=True,capture_output=True,check=True)
    assert 'nice=10' in r.stderr or int(r.stderr.strip().split('=')[1])>10
    lines=[tuple(map(int,l.split())) for l in r.stdout.splitlines()]
    counts=[x[1] for x in lines]; bridges=[x[2] for x in lines]
    assert counts[:min(9,depth+1)]==python_check(a,min(8,depth))
    assert counts[1]==degree
    if kind=='infinite':
        assert all(counts[n]<=degree*(degree-1)**(n-1) for n in range(1,depth+1))
        for n in range(1,depth+1):
            for m in range(1,depth+1-n): assert counts[n+m]<=counts[n]*counts[m]
        if bridge:
            for n in range(1,depth+1):
                for m in range(1,depth+1-n): assert bridges[n+m]>=bridges[n]*bridges[m]
    result=dict(name=name,kind=kind,degree=degree,depth=depth,vertices=len(vertices),counts=counts,
                bridge_counts=bridges if bridge else None,seconds=time.monotonic()-started,metadata=meta or {})
    with (ROOT/'data'/'enumerations.jsonl').open('a') as f: f.write(json.dumps(result)+'\n')
    print(name, 'c_n=',counts[-1], 'ratio=',counts[-1]/counts[-2] if counts[-2] else None, flush=True)
    return result

def product_finite(m,k):
    return lambda v: tuple({((v[0]+1)%m,v[1]),((v[0]-1)%m,v[1]),(v[0],(v[1]+1)%k),(v[0],(v[1]-1)%k)})
def cylinder(k):
    return lambda v: tuple({(v[0]+1,v[1]),(v[0]-1,v[1]),(v[0],(v[1]+1)%k),(v[0],(v[1]-1)%k)})
def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def inverse(p): return tuple(p.index(i) for i in range(len(p)))
def strip(a,b,mod=None):
    bi=inverse(b)
    def neighbors(v):
        x,p=v
        values=((x,compose(p,a)),(x+1,compose(p,b)),(x-1,compose(p,bi)))
        return tuple(((y%mod if mod else y),q) for y,q in values)
    return neighbors

def free_neighbors(m,cycle=False):
    # Normal words of C_m * C_2, with C_m all-elements or cycle generators.
    gens=[1,m-1] if cycle else list(range(1,m))
    def neighbors(word):
        out=[]
        for k in gens:
            if word and word[-1]>0:
                z=(word[-1]+k)%m
                out.append(word[:-1]+((z,) if z else ()))
            else: out.append(word+(k,))
        out.append(word[:-1] if word and word[-1]==-1 else word+(-1,))
        return out
    return neighbors

def finite_complete(n): return lambda v: tuple(w for w in range(n) if w!=v)

def main():
    (ROOT/'data'/'enumerations.jsonl').write_text('')
    results=[]
    for n in (4,5):
        r=run(f'K{n}','finite',n-1,finite_complete(n),0,n)
        assert r['counts']==[math.factorial(n-1)//math.factorial(n-1-k) for k in range(n)]+[0]
        results.append(r)
    results.append(run('K3,3','finite',3,lambda v:tuple(w for w in range(6) if (v<3)!=(w<3)),0,6))
    results.append(run('octahedral_K2,2,2','finite',4,lambda v:tuple(w for w in range(6) if v//2!=w//2),0,6))
    def petersen(v):
        if v<5: return ((v+1)%5,(v-1)%5,v+5)
        return (5+(v-5+2)%5,5+(v-5-2)%5,v-5)
    results.append(run('Petersen','finite',3,petersen,0,10))
    for m in (3,4,5,6,8):
        results.append(run(f'prism_C{m}_x_K2','finite',3,product_finite(m,2),(0,0),min(2*m,16)))
    for m in (3,4,5,6):
        results.append(run(f'torus_C{m}_x_C3','finite',4,product_finite(m,3),(0,0),min(3*m,14)))
    ladder=run('ladder_Z_x_K2','infinite',3,cylinder(2),(0,0),30,lambda v:v[0],True)
    results.append(ladder)
    large_prism=run('prism_C31_x_K2_cover_check','finite',3,product_finite(31,2),(0,0),30)
    assert large_prism['counts']==ladder['counts']
    results.append(large_prism)
    results.append(run('line_square_Z_pm1_pm2','infinite',4,lambda v:(v-2,v-1,v+1,v+2),0,24,lambda v:v,True))
    def tree_neighbors(w):
        out=[]
        for g in (0,1,2):
            out.append(w[:-1] if w and w[-1]==g else w+(g,))
        return out
    tree=run('universal_cubic_cover_T3','infinite',3,tree_neighbors,(),12)
    assert tree['counts']==[1]+[3*2**(n-1) for n in range(1,13)]
    results.append(tree)
    def honey(v):
        x,y=v; return ((x-1,y),(x+1,y),(x,y+(1 if (x+y)%2==0 else -1)))
    results.append(run('honeycomb','infinite',3,honey,(0,0),22))
    for k in (3,4,5,6):
        results.append(run(f'cylinder_Z_x_C{k}','infinite',4,cylinder(k),(0,0),16,lambda v:v[0],True))
    results.append(run('square_Z2','infinite',4,lambda v:((v[0]+1,v[1]),(v[0]-1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)),(0,0),16,lambda v:v[0],True))
    for q in (3,4,5):
        a=tuple((-i)%q for i in range(q)); b=tuple((i+1)%q for i in range(q)); e=tuple(range(q))
        r=run(f'Z_D{q}_component','infinite',3,strip(a,b),(0,e),23,lambda v:v[0],True,{'a':a,'b':b,'group':'subgroup generated by (0,a),(1,b) in Z x D_q'})
        results.append(r)
        # Voltage cover check: reduction of x modulo L>depth cannot identify vertices on a path.
        short=9; _,ac=ball(strip(a,b,short+1),(0,e),short)
        assert python_check(ac,short)==r['counts'][:short+1]
    for q in (3,4):
        a=(1,0)+tuple(range(2,q)); b=tuple(list(range(1,q))+[0]); e=tuple(range(q))
        results.append(run(f'Z_S{q}_component','infinite',3,strip(a,b),(0,e),23,lambda v:v[0],True,{'a':a,'b':b,'group':'subgroup generated by (0,a),(1,b) in Z x S_q'}))
    # Free product balls are exponential: cap brute force at depth 10, verify all counts by renewal.
    from family import coefficients
    for m in (3,4,5):
        r=run(f'K{m}_free_K2','infinite',m,free_neighbors(m),(),10)
        assert r['counts']==coefficients(m,10)
        results.append(r)
    for m in (4,5,6):
        results.append(run(f'C{m}_free_K2','infinite',3,free_neighbors(m,True),(),10))
    with (ROOT/'data'/'summary.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['graph','kind','degree','n','c_n','ratio_evidence','nth_root_upper_if_infinite','bridge_lower_if_available'])
        for r in results:
            n=r['depth']; c=r['counts']; b=r['bridge_counts']
            w.writerow([r['name'],r['kind'],r['degree'],n,c[n],c[n]/c[n-1] if c[n-1] else '', c[n]**(1/n) if r['kind']=='infinite' else '', b[n]**(1/n) if b and b[n] else ''])
    info=dict(nice=os.getpriority(os.PRIO_PROCESS,0),worker_processes=1,thread_environment=1,checks='independent explicit-path BFS through length 8; submultiplicativity; bridge supermultiplicativity; finite complete graphs; voltage covers; free-product renewal',python_maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,enumerator_child_maxrss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    (ROOT/'data'/'checks.json').write_text(json.dumps(info,indent=2)+'\n')
if __name__=='__main__': main()
