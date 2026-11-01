from fractions import Fraction as F
import json
import math
import pathlib
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
N=B=0
blocks=[]
for j in range(8):
    length=2**(2**j)
    N+=length
    if j%2:
        B+=length
    fraction=F(B,N)
    blocks.append({'block':j,'length':str(length),'total_levels':str(N),'two_child_fraction':float(fraction),'root_growth_at_block_end':2**float(fraction)})
early=[1]
level_counts=[]
for j in range(3):
    level_counts.extend([1 if j%2==0 else 2]*(2**(2**j)))
for b in level_counts[:10]:
    early.append(early[-1]*b)
assert early[1]==early[2]==1 and early[3]==2
assert early[3]>early[1]*early[2]
counts=[0]*11
seen={(0,0)}
steps=((1,0),(-1,0),(0,1),(0,-1))
def visit(x,y,depth):
    counts[depth]+=1
    if depth==10:
        return
    for dx,dy in steps:
        position=(x+dx,y+dy)
        if position not in seen:
            seen.add(position)
            visit(*position,depth+1)
            seen.remove(position)
visit(0,0,0)
submultiplicative_cases=0
for n in range(1,11):
    assert 2**n<=counts[n]<=4*3**(n-1)
    for m in range(1,11-n):
        assert counts[n+m]<=counts[n]*counts[m]
        submultiplicative_cases+=1
measurement={'command':'python -X utf8 check_p0004.py','tree_early_counts':early,'tree_block_end_cases':blocks,'lattice_counts_through_10':counts,'exact_lattice_submultiplicativity_checks':submultiplicative_cases,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS'}
(root/'p0004_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
tree_statement='There is an infinite connected tree of maximum degree three whose rooted self-avoiding-walk counts c_n satisfy liminf c_n^(1/n)=1 and limsup c_n^(1/n)=2. Use successive level-block lengths 2^(2^j), with one child in even blocks and two in odd blocks. Rooted scalar submultiplicativity already fails at c_1=c_2=1,c_3=2. This refutes a generic bounded-degree existence route, but the example is not a stationary iid percolation cluster of Z^2.'
tree_proof=(root/'P0004_proof.md').read_text(encoding='utf-8').split('Let c_n(o)',1)[1].split('\n\nAt the p=1 boundary',1)[0]
tree=entry('p0004-nonstationary-tree','probability.percolation','bounded-degree-tree-without-rooted-connective-limit','lemma','Bounded degree alone does not give a connective limit',tree_statement,'Let c_n(o)'+tree_proof,['Infinite spherically symmetric rooted tree','Nonstationary alternating branching blocks','Rooted self-avoiding-walk counts'])
lattice_statement='For the p=1 bond-percolation configuration on Z^2, let c_n(v) count length-n self-avoiding walks from v. Translation invariance and prefix splitting give c_{n+m}(0)<=c_n(0)*c_m(0). Thus c_n(v)^(1/n) has a common limit in [2,3] by Fekete subadditivity, independent of v. This boundary result does not prove the quenched limit for p in (p_c,1).'
lattice=entry('p0004-full-lattice-boundary','probability.percolation','full-square-lattice-connective-limit-submultiplicativity-boundary','lemma','Translation invariance proves the full-lattice boundary limit',lattice_statement,'Translate each prefix endpoint to zero; the permitted suffixes inject into all length-m origin walks. This gives scalar submultiplicativity. Fekete applied to log c_n gives the limit. There are 2^n monotone northeast walks and at most 4*3^(n-1) walks without immediate reversal, giving the bounds. Translation preserves the counts.',['p=1 on the square lattice','Finite-length self-avoiding walks'])
relations=[edge_to_problem('P0004',tree['key'],'the example is not a stationary iid percolation cluster of Z^2','analogous_to'),edge_to_attempt('P0004',tree['key'],'Rooted scalar submultiplicativity already fails','No stationary scalar subadditive process or liminf lower bound was obtained','semantic_association'),edge_to_problem('P0004',lattice['key'],'This boundary result does not prove the quenched limit')]
emit(9,'P0004',[tree,lattice],relations,'P0004_proof.md','p0004_measurement.json')
print(json.dumps(measurement),flush=True)
