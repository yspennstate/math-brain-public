"""Two rational face boxes containing the two types of limit charts."""
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path
from corner_boxes import corner_record,permutations


def build():
    scale=10**12
    n=isqrt(5*scale*scale)
    lo,hi=F(n,scale),F(n+1,scale)
    assert lo*lo<=5<=hi*hi
    e=F(1,10**8)
    boxes=[[(4-e,F(4)),(F(-1),-1+e),(-hi-e,-lo+e),(F(-1),-1+e),(-hi-e,-lo+e),(lo-e,hi+e)],
           [(F(3,2)-e,F(3,2)+e),(F(-1),-1+e),(-hi-e,-lo+e),(F(-1),-1+e),(lo/2-e,hi/2+e),(lo/2-e,hi/2+e)]]
    out=[]
    for b in boxes:
        rec=corner_record(b);assert rec is not None
        out.append(dict(box=[[str(a),str(c)] for a,c in b],certificate=rec))
    # All fifteen permutations represent distinct labeled limit gap matrices.
    matrices=[]
    for perm in permutations():
        U=[0]*5;W=[0]*5
        for j,i in enumerate(perm):U[i]=[-4,1,1,1,1][j];W[i]=[0,1,-1,-1,1][j]
        matrices.append(tuple(F(U[i]*U[j],20)+F(W[i]*W[j],4) for i in range(5) for j in range(5)))
    assert len(set(matrices))==15
    return dict(label='PROVED by verify_corner_faces.py',sqrt5_enclosure=[str(lo),str(hi)],
                boxes=out,corner_permutations=permutations(),
                conclusion='Nonnegative T on feasible parts of each closed box; strictly positive on connected graphs. The boxes include disconnected equality points.')


if __name__=='__main__':
    data=build();Path('corner_face_boxes.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PROVED: two rational face boxes include the limit charts, via the corner theorem.')
