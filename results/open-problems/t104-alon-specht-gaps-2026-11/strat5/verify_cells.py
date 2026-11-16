"""PROVED: standard-library rational replay of every moment cell."""
import itertools,json
from fractions import Fraction as F

def det(m):
    if not m:return F(1)
    return sum((-1)**j*m[0][j]*det([row[:j]+row[j+1:] for row in m[1:]]) for j in range(len(m)))
ineq=[([-1,0,0],-F(7,30)),([0,-1,0],-F(7,30)),([1,0,0],F(13,20)),([0,1,0],F(13,20)),
      ([0,0,-1],F(0)),([0,0,1],F(3,10)),([1,0,1],F(4,5)),([0,1,1],F(4,5)),
      ([1,1,2],F(7,5)),([-1,-1,2],F(0)),([-1,0,-1],-F(1,4)),([0,-1,-1],-F(1,4))]
vertices=set()
for indices in itertools.combinations(range(len(ineq)),3):
    mat=[list(map(F,ineq[i][0])) for i in indices]
    dd=det(mat)
    if not dd:continue
    rhs=[ineq[i][1] for i in indices]
    sol=[]
    for j in range(3):
        copy=[row[:] for row in mat]
        for i in range(3):copy[i][j]=rhs[i]
        sol.append(det(copy)/dd)
    if all(sum(F(x)*y for x,y in zip(row,sol))<=rhs for row,rhs in ineq):vertices.add(tuple(sol))
assert vertices==set(tuple(map(F,v)) for v in json.load(open('moment_vertices.json')))

def value(v,a,r,tn,tj,t):
    A,B,C=v
    fm=A+r*B+(1+r)*C
    k=A+B+2*C
    f=fm-(1+r)/5
    base=F(14,9)*f+a*(2*(1+r)*f/9+F(4,3)*(1+r*r)-F(14,3)*(A+r*r*B)-4*(1+r*r+r/3)*C)
    tangent=a*(2*t*fm-(1+r)*t*t)
    ldiv5=(2+a*(1+r))/20
    return base+tn*(tangent-ldiv5*(2-k))+tj*(tangent-ldiv5*(4-k))

def minimum(v,alo,ahi,rlo,rhi,tn,tj,t):
    vals=[]
    for a in (alo,ahi):
        c0=value(v,a,F(0),tn,tj,t)
        plus,minus=value(v,a,F(1),tn,tj,t),value(v,a,F(-1),tn,tj,t)
        c1=(plus-minus)/2
        c2=(plus+minus)/2-c0
        test=[rlo,rhi]
        if c2>0:
            point=-c1/(2*c2)
            if rlo<=point<=rhi:test.append(point)
        vals.extend(c0+c1*x+c2*x*x for x in test)
    return min(vals)

cells=json.load(open('weight_moment_cells.json'))
previous=F(3,5)
for rec in cells:
    rlo,rhi,alo,ahi,tn,tj,t,claimed=map(lambda k:F(rec[k]),['rlo','rhi','alo','ahi','theta_n','theta_j','tangent','margin'])
    assert rlo==previous and rhi>rlo and alo==F(4,11) and ahi>alo
    assert 0<=tn<=5*rlo/3-1 and 0<=tj<=1+rlo
    margin=min(minimum(v,alo,ahi,rlo,rhi,tn,tj,t) for v in vertices)
    assert margin==claimed and margin>=0
    previous=rhi
assert previous==1
print('PROVED: independently enumerated',len(vertices),'rational moment vertices.')
print('PROVED:',len(cells),'adjacent cells cover ratios [3/5,1]; every multiplier and lower bound checked exactly.')
for lower,upper in [(F(3,5),F(7,10)),(F(7,10),F(4,5)),(F(4,5),F(9,10)),(F(9,10),F(19,20)),(F(19,20),F(99,100)),(F(99,100),F(1))]:
    cap=min(F(c['ahi']) for c in cells if F(c['rlo'])<upper and F(c['rhi'])>lower)
    print('PROVED: r in ['+str(lower)+','+str(upper)+'] and a<='+str(cap)+' is covered.')

def moment_value(v,r,low):
    ans=value(v,F(443,1000),r,F(0),F(0),F(0))
    if low:ans-=F(443,1000)*(1-7*r)*(9+r)*v[2]/24
    return ans
for low,rlo,rhi in [(True,F(3,25),F(1,7)),(False,F(1,7),F(1))]:
    for v in vertices:
        c0=moment_value(v,F(0),low)
        plus,minus=moment_value(v,F(1),low),moment_value(v,F(-1),low)
        c1=(plus-minus)/2
        c2=(plus+minus)/2-c0
        tests=[rlo,rhi]
        if c2>0 and rlo<=-c1/(2*c2)<=rhi:tests.append(-c1/(2*c2))
        assert min(c0+c1*x+c2*x*x for x in tests)>=0
print('PROVED: the moment region covers a<=443/1000 for every r in [3/25,1].')
