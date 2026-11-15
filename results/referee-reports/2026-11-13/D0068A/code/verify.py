"""Independent breadth-first path enumeration, fixtures, and data audit."""
import csv
import hashlib
import itertools
import json
import math
import os
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
KNOWN = [1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100, 120292, 324932]

def graph_from_file(path):
    lines = path.read_text().splitlines()
    radius, p, seed = lines[1].split()
    radius = int(radius)
    side = 2*radius+1
    bits = ''.join(lines[2:])
    assert len(bits) == 2*side*side
    adj = [[] for _ in range(side*side)]
    for y in range(side):
        for x in range(side):
            v = y*side+x
            if bits[2*v] == '1':
                assert x+1 < side
                adj[v].append(v+1); adj[v+1].append(v)
            if bits[2*v+1] == '1':
                assert y+1 < side
                adj[v].append(v+side); adj[v+side].append(v)
    assert all(len(set(ns)) == len(ns) <= 4 for ns in adj)
    return radius, float(p), int(seed), adj

def breadth_first(adj, root, nmax):
    frontier = [(root,)]
    counts = [1]
    for _ in range(nmax):
        following = []
        for path in frontier:
            for w in adj[path[-1]]:
                if w not in path:
                    following.append(path+(w,))
        counts.append(len(following))
        frontier = following
    return counts

def square_graph(radius):
    return {(x,y): [(a,b) for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1))
                    if abs(a)<=radius and abs(b)<=radius]
            for x in range(-radius,radius+1) for y in range(-radius,radius+1)}

def check_diamond_formula():
    checked = 0
    for bs in itertools.product((0,1), repeat=7):
        # n<=12 only reaches cell 6; the finite right boundary cannot matter.
        adj = {}
        def edge(a,b):
            adj.setdefault(a,[]).append(b); adj.setdefault(b,[]).append(a)
        for k,b in enumerate(bs):
            a=(k,k); z=(k+1,k+1); h=(k+1,k)
            edge(a,h);edge(h,z)
            if b:
                t=(k,k+1);edge(a,t);edge(t,z)
        counts = breadth_first(adj,(0,0),12)
        for n,c in enumerate(counts):
            m=n//2; expected=2**sum(bs[:m])
            if n%2: expected*=1+bs[m]+(bs[m-1] if m else 0)
            assert c==expected, (bs,n,c,expected)
            checked+=1
    return checked

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    report = {'nice': os.getpriority(os.PRIO_PROCESS,0)}
    assert breadth_first(square_graph(12),(0,0),12)==KNOWN
    report['full_lattice_fixture_nmax']=12
    report['diamond_formula_comparisons']=check_diamond_formula()
    rows = list(csv.DictReader((DATA/'counts.csv').open()))
    metas = list(csv.DictReader((DATA/'samples.csv').open()))
    assert len(metas)==27, 'Enumeration not finished'
    groups = {}
    for row in rows:
        key = (round(float(row['p']),2),int(row['sample']),int(row['root']))
        groups.setdefault(key,[]).append(row)
    assert len(groups)==27
    comparisons=0
    hashes={}
    for path in sorted(DATA.glob('*_edges.txt')):
        hashes[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
        radius,p,seed,adj=graph_from_file(path)
        sample=int(path.stem.split('_s')[1].split('_')[0])
        origin=radius*(2*radius+1)+radius
        component={origin}; q=deque([origin])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in component:component.add(w);q.append(w)
        side=2*radius+1
        assert {0,side-1} <= {v%side for v in component}
        assert {0,side-1} <= {v//side for v in component}
        for root in range(3):
            rs=sorted(groups[(p,sample,root)],key=lambda r:int(r['n']))
            expected_nmax={.6:28,.75:24,.9:21}[p]
            assert [int(r['n']) for r in rs] == list(range(expected_nmax+1))
            x,y=int(rs[0]['x']),int(rs[0]['y'])
            start=(y+radius)*side+x+radius
            assert start in component
            assert radius-max(abs(x),abs(y))>expected_nmax
            assert all(int(r['seed'])==seed for r in rs)
            exact=breadth_first(adj,start,10)
            got=[int(r['count']) for r in rs]
            assert got[:11]==exact,(p,sample,root,got[:11],exact)
            assert got[1]==len(adj[start])
            assert got[2]==sum(len(adj[w])-1 for w in adj[start])
            for n,c in enumerate(got):
                assert c>=1
                if n:
                    assert c<=4*3**(n-1)<2**64
                    assert abs(float(rs[n]['nth_root'])-math.exp(math.log(c)/n))<1e-12
                if n>1: assert c<=3*got[n-1]
            comparisons+=11
    report.update({'sample_graphs':len(hashes),'roots':len(groups),
                   'breadth_first_comparisons':comparisons,'edge_sha256':hashes,
                   'passed':True})
    (DATA/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
