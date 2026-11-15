"""PROVED: finite rational search for endpoints outside the new moment tests."""
import json
import random
from fractions import Fraction as F
from moment_bounds import value, vertices
from rational_rays import frame_data,cell_bound
from directional_bounds import vector_from_record,lower_value

rng=random.Random(13110343)
base=json.load(open('strong_moment_cells.json'))
extra=json.load(open('enhanced_moment_cells.json'))
directional=json.load(open('directional_moment_cells.json'))
directional=[(c,vector_from_record(c))for c in directional]
old_cells=json.load(open('STRAT5/weight_moment_cells.json'))
verts=vertices()
counts=dict(tested=0,old_uncovered=0,new_covered=0)
witnesses=[]
residual=[]
for trial in range(8000):
    zz=[rng.randrange(5) for _ in range(4)]
    if not any(zz):continue
    U=[sum(((5-j) if i<j else -j)*zz[j-1] for j in range(1,5))for i in range(5)]
    xi=[rng.randrange(-4,5)for _ in range(3)]
    if not any(xi):continue
    W=[sum((U[4]-U[j+1])*xi[j]for j in range(3))]
    W += [(U[0]-U[4])*xi[j]for j in range(3)]
    W += [sum((U[j+1]-U[0])*xi[j]for j in range(3))]
    r=F(rng.randrange(3,21),20)
    data=frame_data(U,W,r)
    counts['tested']+=1
    a,lam=data['a'],data['lam']
    if lam<=a or a<=F(443,1000):continue
    if r==1 and a<=F(11,20):continue
    if any(F(c['rlo'])<=r<=F(c['rhi']) and a<=F(c['ahi']) for c in old_cells):continue
    A,B,C=data['moments']
    cr=max(F(0),1-7*r)*(9+r)/24
    old_moment=value(data['moments'],a,r,0,0,0,0,0)-a*cr*C
    if old_moment>=0:continue
    DD=34+52*r-22*r*r+max(F(0),1-7*r)*(9+r)/2
    if a<=14*(1+r)/DD:continue
    K=A+B+2*C
    fm=A+r*B+(1+r)*C
    ZN=a*fm*fm/(1+r)-lam*(2-K)/5
    ZJ=a*fm*fm/(1+r)-lam*(4-K)/5
    old_weight=value(data['moments'],a,r,0,0,0,0,0)
    if r>=F(3,5):
        old_weight+=(5*r/3-1)*max(F(0),ZN)+(1+r)*max(F(0),ZJ)
        if old_weight>=0:continue
    counts['old_uncovered']+=1
    eligible=[(i,cell_bound(c,data['moments'],a,r)) for i,c in enumerate(base)
              if F(c['rlo'])<=r<=F(c['rhi'])]
    eligible += [(-1,cell_bound(c,data['moments'],a,r))for c in extra
                 if F(c['rlo'])<=r<=F(c['rhi'])]
    eligible += [(-2,lower_value(data['moments'],a,r,vector))for c,vector in directional
                 if F(c['rlo'])<=r<=F(c['rhi'])]
    if not eligible:continue
    index,bound=max(eligible,key=lambda q:q[1])
    if bound>=0:
        counts['new_covered']+=1
        if len(witnesses)<10:
            assert data['T']/a>=bound
            witnesses.append(dict(U=U,W=W,r=str(r),a=str(a),T=str(data['T']),
                cell=index,bound=str(bound),old_moment=str(old_moment),old_weight=str(old_weight)))
    else:
        residual.append(dict(U=U,W=W,r=str(r),a=str(a),T=str(data['T']),bound=str(bound)))
with open('residual_rays.json','w') as out:
    json.dump(dict(counts=counts,residual=residual),out,indent=2)
print('PROVED: finite exact search counts',counts,'with',len(residual),'endpoints outside all new moment cells.')
print('PROVED: these counts describe the finite search only; they make no global coverage claim.')
