"""Independent full-orientation Fraction control of our native grid6 evaluator."""
from fractions import Fraction as F
from itertools import permutations
from collections import defaultdict
from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parent
N=6; S=2**32; eta=F(53,237)
orbits=[(x,y,N-x-y) for x in range(N+1) for y in range(x,N+1) if N-x-y>=y]
ids={v:i for i,v in enumerate(orbits)}
orient=[sorted(set(permutations(v))) for v in orbits]

def row(i,j,first):
    answer=defaultdict(F)
    for a in orient[i]:
        for b in orient[j]:
            p=[F(v,N) for v in a]; r=[F(v,N) for v in b]
            z=[((1-eta+3*eta*p[k]) if first else 3*p[k])*(1-eta+3*eta*r[k]) for k in range(3)]
            c=sum(z); posterior=[v/c for v in z]
            floors=[int(N*v) for v in posterior]; residual=[N*posterior[k]-floors[k] for k in range(3)]
            missing=N-sum(floors)
            vertices=[]
            if missing==0: vertices=[(floors,F(1))]
            elif missing==1:
                vertices=[([floors[k]+int(k==h) for k in range(3)],residual[h]) for h in range(3)]
            elif missing==2:
                vertices=[([floors[k]+int(k!=h) for k in range(3)],1-residual[h]) for h in range(3)]
            else: raise AssertionError(missing)
            for vertex,w in vertices:
                answer[ids[tuple(sorted(vertex))]]+=c*w/(3*len(orient[i])*len(orient[j]))
    answer={k:v for k,v in answer.items() if v}
    assert sum(answer.values())==1
    return answer

tables={}; count=0
for first,name in [(True,'prefix'),(False,'merge')]:
    dumped=defaultdict(dict)
    for line in (ROOT/f't067_band20_N6_own_{name}.tsv').read_text().splitlines():
        i,j,k,num,den=map(int,line.split()); dumped[i,j][k]=F(num,den)
    table={}
    for i in range(len(orbits)):
        for j in range(i if first else 0,len(orbits)):
            actual=row(i,j,first)
            assert actual==dumped[i,j],(name,i,j)
            table[i,j]=actual; count+=1
    tables[first]=table

def stage(left,right,first):
    mass=[F(0)]*len(orbits)
    for i in range(len(orbits)):
        for j in range(len(orbits)):
            key=tuple(sorted((i,j))) if first else (i,j)
            for k,w in tables[first][key].items():mass[k]+=F(left[i]*right[j],S*S)*w
    rounded=[int(v*S) for v in mass]
    revealed=S-sum(rounded); rounded[ids[(0,0,N)]]+=revealed
    return rounded,F(revealed,S)

child=[0]*len(orbits);child[ids[(0,0,N)]]=S
receipts=[]
for depth in range(1,5):
    old=child; child,r=stage(old,old,True);reveals=[r]
    for _ in range(19):child,r=stage(child,old,False);reveals.append(r)
    signal=sum(F(child[k],S)*(sum(F(v,N)**2 for v in o)-F(1,3)) for k,o in enumerate(orbits))
    native=(ROOT/f't067_band20_N6_own_depth_{depth:03}.txt').read_text().splitlines()
    assert int(native[0])==depth and F(native[1])==signal and list(map(int,native[2:]))==child
    native_reveals=[F(v) for v in (ROOT/f't067_band20_N6_own_revealed_{depth:03}.txt').read_text().splitlines()]
    assert native_reveals==reveals
    receipts.append({'depth':depth,'signal':str(signal),'all_masses':child,'revealed':[str(v) for v in reveals]})
out={'status':'PASS','method':'Fraction; enumerate BOTH independent orbit orientations; exact barycentric weights and all ordered child pairs','transition_rows':count,'depths':receipts,'native_sha256':hashlib.sha256((ROOT/'t067_band20_own.cs').read_bytes()).hexdigest()}
(ROOT/'t067_band20_control_own.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all77 full-orientation rows and all4 depths, masses, signals and80 stage-reveals match')
