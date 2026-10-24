from collections import deque
from math import sin,pi,asin,sqrt
import json

def run(H,n):
    heights={(0,0):n-H}; u={}; last={}; q=deque([(0,0)]); queued={(0,0)}; tick=0
    while q:
        x=q.popleft(); queued.remove(x); z=heights.get(x,-H)//4
        if z<=0: continue
        heights[x]-=4*z; u[x]=u.get(x,0)+z; tick+=z; last[x]=tick
        for y in [(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]-1),(x[0],x[1]+1)]:
            heights[y]=heights.get(y,-H)+z
            if heights[y]>=4 and y not in queued: q.append(y); queued.add(y)
    def neighbours(x): return [(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]-1),(x[0],x[1]+1)]
    assert sum(v+H for v in heights.values())==n
    for x,v in heights.items():
        assert v<=3
        assert v==-H+n*(x==(0,0))-4*u.get(x,0)+sum(u.get(y,0) for y in neighbours(x))
    for x,v in u.items():
        assert heights[x]>=sum(last.get(y,0)>last[x] for y in neighbours(x))
        assert all(u.get((sx*x[0],sy*x[1]),0)==v and u.get((sx*x[1],sy*x[0]),0)==v for sx in [-1,1] for sy in [-1,1])
        if x[0]>0: assert v<=u.get((x[0]-1,x[1]),0)
        if x[1]>0: assert v<=u.get((x[0],x[1]-1),0)
    boxchecks=0
    for r in range(1,12):
        A={(x,y) for x in range(-r,r+1) for y in range(-r,r+1)}
        if A<=u.keys():
            E=sum(y in A for x in A for y in neighbours(x))//2
            assert sum(heights[x] for x in A)>=E; boxchecks+=1
    weights={x:1+(x[0]*7+x[1]*11)%13 for x in u}
    lhs=sum(heights[x]*w for x,w in weights.items())
    rhs=sum(min(w,weights.get(y,0)) for x,w in weights.items() for y in [(x[0]+1,x[1]),(x[0],x[1]+1)])
    assert lhs>=rhs
    return dict(H=H,n=n,fired=len(u),firings=tick,box_checks=boxchecks,weighted_margin=lhs-rhs)
results=[run(H,n) for H in range(-2,4) for n in [128,1024,4096]]
angles=[]
for k in range(2,104):
    margin=k*sin(pi/(2*k))-1
    assert margin>0
    angles.append(margin)
c=(20+8*sqrt(3))/13
assert 2<c<8/3
assert abs((2-3*c/4)*(1-c/4)-(1-sqrt(3)*c/4)**2)<1e-14
out={'runs':results,'min_corner_contradiction_margin_k_2_to_103':min(angles),'H0_side_lower_bound':2*pi/asin(1/3),'matrix_c':c}
open('independent_checks.json','w',encoding='utf-8').write(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
