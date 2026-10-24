"""Finite polygon checks; no claim of exhaustive variation optimization."""
from pathlib import Path
import json, math, random

random.seed(139)

def wedge(x, y):
    return x[0]*y[1]-x[1]*y[0]

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def sub(x, y):
    return (x[0]-y[0], x[1]-y[1])

def norm(x):
    return math.hypot(*x)

def area_prefix(points):
    a=[0.0]
    for x,y in zip(points,points[1:]):
        a.append(a[-1]+0.5*wedge(x,y))
    return a

def inc_area(points, areas, s, t):
    return areas[t]-areas[s]-0.5*wedge(points[s],points[t])

# A backbone alternates straight movements and intervals of enhanced stationarity.
# Each loop is a based polygonal circle; varying signs exercise area cancellation.
N=12
steps=32
y=[(0.0,0.0)]
e=[(0.0,0.0)]
B=[0.0]
owners=[-1]
loops=[]
total=0.0
for i in range(N):
    base=add(y[-1],(0.15, random.uniform(-0.1,0.1)))
    y.append(base);e.append((0.0,0.0));B.append(total);owners.append(-1)
    r=2.0**(-i-1)
    sign=(-1)**i
    points=[(r*(math.cos(2*math.pi*k/steps)-1),sign*r*math.sin(2*math.pi*k/steps)) for k in range(steps+1)]
    points[0]=points[-1]=(0.0,0.0)
    pref=area_prefix(points)
    start=len(y)-1
    for k in range(1,steps+1):
        y.append(base);e.append(points[k]);B.append(total+pref[k]);owners.append(i)
    total+=pref[-1]
    loops.append({'start':start,'end':len(y)-1,'c':pref[-1], 'r':r})

Ay=area_prefix(y)
full=[add(a,b) for a,b in zip(y,e)]
formula=[a+b+0.5*wedge(v,w) for a,b,v,w in zip(Ay,B,y,e)]
direct=area_prefix(full)
global_error=max(abs(a-b) for a,b in zip(formula,direct))
increment_error=0.0
for _ in range(5000):
    s,t=sorted(random.sample(range(len(y)),2))
    rhs=inc_area(y,Ay,s,t)+B[t]-B[s]+0.5*wedge(sub(y[t],y[s]),add(e[t],e[s]))-0.5*wedge(e[s],e[t])
    increment_error=max(increment_error,abs(rhs-inc_area(full,direct,s,t)))

p=2.5
q=p/2
variation=[]
for cutoff in (0,1,3,6,9,11,12):
    short=[add(a,b) if 0<=owner<cutoff else a for a,b,owner in zip(y,e,owners)]
    short_area=area_prefix(short)
    best1=best2=0.0
    for _ in range(1000):
        P=sorted({0,len(y)-1,*random.sample(range(1,len(y)-1),random.randrange(1,80))})
        d1=sum(norm(sub(sub(full[t],full[s]),sub(short[t],short[s])))**p for s,t in zip(P,P[1:]))**(1/p)
        d2=sum(abs(inc_area(full,direct,s,t)-inc_area(short,short_area,s,t))**q for s,t in zip(P,P[1:]))**(1/q)
        best1=max(best1,d1);best2=max(best2,d2)
    # Conservative loop gauge bound from total polygon length: L* <= 2 length.
    eps=sum((4*math.pi*l['r'])**p for l in loops[cutoff:])**(1/p)
    alpha=sum(abs(l['c']) for l in loops[cutoff:])
    E=sum((4*math.pi*l['r'])**p for l in loops)**(1/p)
    # V bound from total variation of backbone, same conservative factor 2.
    V=2*sum(norm(sub(v,u)) for u,v in zip(y,y[1:]))
    rhs=eps**2+(V+E)*eps+alpha
    variation.append({'cutoff':cutoff,'sampled_first_difference':best1,'sampled_area_difference':best2,'eps_upper_bound':eps,'absolute_area_tail':alpha,'bound_expression':rhs})
    assert best1<=10*eps+1e-12
    assert best2<=10*rhs+1e-12

obstruction=[]
for m in (1,4,16,64,256,1024):
    r=m**(-0.5)
    obstruction.append({'m':m,'sup_norm':2*r,'area_exact':'pi','area_float':math.pi,'pvar_upper_bound':((2*math.pi)**p+2**(2*p))**(1/p)*m**(1/p-0.5)})

result={'seed':139,'polygon_loops':N,'polygon_steps_per_loop':steps,'random_increment_checks':5000,'global_coordinate_max_error':global_error,'increment_formula_max_error':increment_error,'partitions_per_cutoff':1000,'p':p,'truncation_checks':variation,'circle_obstruction':obstruction,'qualification':'Sampled partition checks supplement the analytic proof; they do not optimize p-variation.'}
assert global_error<1e-11 and increment_error<1e-11
Path('numerical_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
