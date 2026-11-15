"""Independent exact direction-word check for the delayed 3/5-chord transfer."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from datetime import datetime,timezone
import json

ROOT=Path(__file__).resolve().parents[1]
graph=json.loads((ROOT/'scripts/chord5_graph.json').read_text())
states=[(tuple(tuple(v) for v in word),tuple(c)) for word,c in graph['states']]
index={state:i for i,state in enumerate(states)}
D=3;Z=Q(7,3);S=Q(17,2)
directions=[(axis,sign) for axis in range(D) for sign in (-1,1)]
def canon(word):
    mapping={};out=[]
    for axis,sign in word:
        if axis not in mapping:mapping[axis]=len(mapping)
        out.append((mapping[axis],sign))
    return tuple(out)
def norm(word):
    vec=[0]*D
    for axis,sign in word:vec[axis]+=sign
    return sum(abs(a) for a in vec)
def chord_intervals(word):
    out=[]
    for length in (3,5):
        for start in range(len(word)-length+1):
            if norm(word[start:start+length])==1:out.append((start,start+length))
    return out

hist={k:Counter() for k in range(4,8)}
numwords={k:0 for k in range(4,8)}
seed=Counter();simple_count=0
def visit(word):
    global simple_count
    k=len(word)
    if k>=4:
        chords=chord_intervals(word)
        counts=[0]*k
        for start,end in chords:
            for edge in range(start,end):counts[edge]+=1
        height=sum(sign for axis,sign in word)
        hist[k][(height,tuple(sorted(counts[:k-4])))]+=1
        numwords[k]+=1
        state=(canon(word[-4:]),tuple(counts[-4:]))
        assert state in index
        if k==4:seed[(index[state],height)]+=1
        if k==7:
            positions=[(0,)*D]
            for axis,sign in word:
                point=list(positions[-1]);point[axis]+=sign;positions.append(tuple(point))
            if len(set(positions))==len(positions):
                path_edges={frozenset((a,b)) for a,b in zip(positions,positions[1:])}
                shortcut_edges=[frozenset((positions[start],positions[end])) for start,end in chords]
                assert len(set(shortcut_edges))==len(shortcut_edges)
                assert all(e not in path_edges for e in shortcut_edges)
                simple_count+=1
    if k==7:return
    for step in directions:
        if word and step==(word[-1][0],-word[-1][1]):continue
        if k>=3 and norm(word[-3:]+(step,))==0:continue
        visit(word+(step,))
visit(())

vec={}
for (i,height),n in seed.items():vec[i]=vec.get(i,Q(0))+n*Z**height
checks=[]
for k in range(4,8):
    direct=Q(0)
    for (height,counts),n in hist[k].items():
        term=n*Z**height
        for c in counts:term/=S+1+c
        direct+=term
    assert direct==sum(vec.values(),Q(0)),(k,'direct word sum does not match matrix')
    checks.append(dict(d=D,length=k,words=numwords[k],status='PASS exact equality',weight_n=str(direct.numerator),weight_d=str(direct.denominator)))
    print('PASS length',k,'words',numwords[k],flush=True)
    newvec={}
    for i,value in vec.items():
        for j,sign,new_axis_r,coverage in graph['rows'][i]:
            multiplicity=1 if new_axis_r==0 else max(0,D-new_axis_r)
            if multiplicity:
                newvec[j]=newvec.get(j,Q(0))+value*multiplicity*Z**sign/(S+1+coverage)
    vec=newvec
print('PASS distinct off-path 3/5-chords on',simple_count,'vertex-simple length-seven words.',flush=True)
(ROOT/'logs/chord5_transfer_validation.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),checks=checks,simple_path_samples=simple_count,role='independent finite check, not a replacement for the general proof'),indent=2)+'\n',encoding='utf-8')
