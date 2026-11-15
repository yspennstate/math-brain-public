"""Full-orientation rational Bayes control, independent of author programs."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
from collections import defaultdict
from hashlib import sha256
import json
ROOT=Path(__file__).resolve().parents[1]
N=6;S=2**32;eta=F(89,218)
orbits=[(a,b,N-a-b) for a in range(N+1) for b in range(a,N+1) if N-a-b>=b]
ids={p:i for i,p in enumerate(orbits)};pure=ids[(0,0,N)]
orient=[sorted(set(permutations(p))) for p in orbits]
bary_cases=0
def split(p):
    global bary_cases
    u=[N*x for x in p];f=[x.numerator//x.denominator for x in u]
    r=[x-y for x,y in zip(u,f)]; missing=N-sum(f);rows=[]
    assert missing in (0,1,2)
    if missing==0:rows=[(tuple(f),F(1))]
    for k in range(3):
        if missing==1:
            q=f.copy();q[k]+=1;rows.append((tuple(q),r[k]))
        if missing==2:
            q=[v+1 for v in f];q[k]-=1;rows.append((tuple(q),1-r[k]))
    assert all(w>=0 and sum(q)==N and min(q)>=0 for q,w in rows)
    assert sum(w for q,w in rows)==1
    assert all(sum(w*q[k]/N for q,w in rows)==p[k] for k in range(3))
    bary_cases+=1
    out=defaultdict(F)
    for q,w in rows:
        if w:out[ids[tuple(sorted(q))]]+=w
    return dict(out)
def unit_row(i,j,full=True):
    out=defaultdict(F); zeros=0
    left=orient[i] if full else [orbits[i]]
    for a in left:
        for b in orient[j]:
            products=[F(a[k]*b[k],N*N) for k in range(3)]
            dot=sum(products)
            if not dot: zeros+=1;continue
            density=3*dot/(len(left)*len(orient[j]))
            for dest,w in split([z/dot for z in products]).items():out[dest]+=density*w
    assert sum(out.values())==1 and all(v>=0 for v in out.values())
    return dict(out),zeros
unit={};zero_pairs=0
for i in range(7):
    for j in range(7):
        row,z=unit_row(i,j);simple,_=unit_row(i,j,False)
        assert row==simple
        assert all((v*(108*N*N)).denominator==1 for v in row.values())
        unit[i,j]=row;zero_pairs+=z
assert zero_pairs==36
edges={}
for strength in [F(0),F(1),eta,F(53,237)]:
    rows=[]
    for a in orbits:
        row=split([F(1,3)+strength*(F(k,N)-F(1,3)) for k in a])
        assert all((w*3*strength.denominator).denominator==1 for w in row.values())
        rows.append(row)
    edges[str(strength)]=rows

def round_law(raw):
    m=[v.numerator//v.denominator for v in raw]
    reveal=S-sum(m);assert reveal>=0
    m[pure]+=reveal;assert sum(m)==S
    return m,reveal
def edge(m):
    raw=[F(0)]*7
    for i in range(7):
        for k,w in edges[str(eta)][i].items():raw[k]+=m[i]*w
    return round_law(raw)
def fuse(left,right):
    raw=[F(0)]*7
    for i in range(7):
        for j in range(7):
            if left[i] and right[j]:
                for k,w in unit[i,j].items():raw[k]+=F(left[i]*right[j],S)*w
    return round_law(raw)
def signal(m):return sum(F(mass*(3*sum(v*v for v in p)-N*N),S*3*N*N) for mass,p in zip(m,orbits))
mass=[0]*7;mass[pure]=S;trajectory=[]
for depth in range(1,5):
    e,r0=edge(mass);g2,r1=fuse(e,e);g4,r2=fuse(g2,g2);mass,r3=fuse(g2,g4)
    trajectory.append({'depth':depth,'mass':mass,'revealed':[r0,r1,r2,r3],'signal':str(signal(mass))})

# Direct six-child leaf observation calculation at depth1, independent of
# any fusion or grid routine. Aggregate color-count likelihoods exactly.
true_signal=F(0);true_probability=F(0)
for a in range(7):
    for b in range(7-a):
        counts=(a,b,6-a-b)
        likelihood=[]
        for root in range(3):
            value=F(1)
            for k,count in enumerate(counts):value*=((1+2*eta)/3 if k==root else (1-eta)/3)**count
            likelihood.append(value)
        total=sum(likelihood)
        if not total:continue
        combinations=factorial(6)
        for v in counts:combinations//=factorial(v)
        probability=total*combinations/3
        posterior=[v/total for v in likelihood]
        true_probability+=probability
        true_signal+=probability*sum((v-F(1,3))**2 for v in posterior)
assert true_probability==1 and F(trajectory[0]['signal'])>=true_signal

native=[]
for row in trajectory:
    p=ROOT/f"checks/t067_d6_N6_own_depth_{row['depth']:03}.txt"
    if p.exists():
        fields=p.read_text().splitlines()
        assert int(fields[0])==row['depth'] and F(fields[1])==F(row['signal'])
        assert list(map(int,fields[2:]))==row['mass']
        rfile=ROOT/f"checks/t067_d6_N6_own_revealed_{row['depth']:03}.txt"
        assert [F(x)*S for x in rfile.read_text().splitlines()]==row['revealed']
        native.append({'depth':row['depth'],'file':str(p),'sha256':sha256(p.read_bytes()).hexdigest(),'all7_masses_signal_and4_reveals':'match'})
edge_dump=ROOT/'checks/t067_d6_N6_own_edge.tsv'
unit_dump=ROOT/'checks/t067_d6_N6_own_merge.tsv'
if edge_dump.exists():
    got=defaultdict(lambda:defaultdict(F))
    for line in edge_dump.read_text().splitlines():
        i,k,num,den=map(int,line.split());got[i][k]+=F(num,den)
    assert all(dict(got[i])==edges[str(eta)][i] for i in range(7))
if unit_dump.exists():
    got=defaultdict(lambda:defaultdict(F))
    for line in unit_dump.read_text().splitlines():
        i,j,k,num,den=map(int,line.split());got[i,j][k]+=F(num,den)
    assert all(dict(got[i,j])==unit[i,j] for i in range(7) for j in range(7))
result={'status':'exact Bayes and grid controls PASS','ordered_unit_rows':49,'both_orientation_methods_agree':True,'excluded_zero_point_pairs':zero_pairs,'edge_rows_checked':28,'barycenter_controls':bary_cases,'scale':S,'eta':str(eta),'trajectories':trajectory,'true_depth1_signal':str(true_signal),'rounded_depth1_upper':trajectory[0]['signal'],'native_trajectories_compared':native,'native_all7_edge_and49_unit_rows_compared':edge_dump.exists() and unit_dump.exists(),'source':'independent Fraction Bayes calculation; no author source imported'}
(ROOT/'checks/t067_universal_control_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','ordered_unit_rows','excluded_zero_point_pairs','edge_rows_checked','barycenter_controls']}))
