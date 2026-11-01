# control: does {exists 2-cycle in [0,1]} == {f'(p) < -1} for m=2 QSOs?  and does
# a repelling fixed point really give a NON-convergent orbit (simulate)?
import math, random
def f(A,B,C,x): return A*x*x + 2*B*x*(1-x) + C*(1-x)**2
def fp(A,B,C,x): return 2*A*x + 2*B*(1-2*x) - 2*C*(1-x)
def fixed_point(A,B,C):
    a=A-2*B+C; b=2*B-2*C-1.0; c=C
    if abs(a)<1e-14: return -c/b
    d=b*b-4*a*c
    if d<0: return None
    s=math.sqrt(d)
    for r in ((-b+s)/(2*a),(-b-s)/(2*a)):
        if -1e-12<=r<=1+1e-12: return r
    return None
random.seed(1)
bad=0; n=0; disagree=[]
for _ in range(200000):
    A,B,C=[random.random() for _ in range(3)]
    p=fixed_point(A,B,C)
    if p is None: continue
    n+=1
    slope=fp(A,B,C,p)
    # look for 2-cycle: iterate from many starts, check non-convergence
    nonconv=False
    for x0 in (0.0,0.25,0.5,0.75,1.0):
        x=x0
        for _ in range(4000): x=f(A,B,C,x)
        y=x
        for _ in range(2): y=f(A,B,C,y)
        if abs(y-x)>1e-7: nonconv=True; break
    if nonconv != (slope < -1-1e-9):
        bad+=1
        if len(disagree)<6: disagree.append((A,B,C,p,slope,nonconv))
print("tested",n,"disagreements",bad)
for d in disagree: print(d)
