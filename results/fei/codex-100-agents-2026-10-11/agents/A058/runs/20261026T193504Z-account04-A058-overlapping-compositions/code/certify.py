import json,time,hashlib
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[1]; S=1<<100; M=48
def ceildiv(a,b):return -((-a)//b)
def qinterval(x): return (x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[1],a[1]-b[0])
def scale(a,q):
    assert q>=0
    return (a[0]*q.numerator//q.denominator,ceildiv(a[1]*q.numerator,q.denominator))
def mulpos(a,b):return (a[0]*b[0]//S,ceildiv(a[1]*b[1],S))
def ln_unit(x):
    assert 1<=x<=2
    z=qinterval((x-1)/(x+1)); z2=mulpos(z,z); power=z; total=(0,0)
    for j in range(M):
        total=add(total,(power[0]//(2*j+1),ceildiv(power[1],2*j+1)))
        power=mulpos(power,z2)
    # Exact remainder: 2 sum_(j>=M) z^(2j+1)/(2j+1)
    # <=(9/4)*3^(-(2M+1))/(2M+1) <3*3^(-(2M+1)).
    tail=ceildiv(3*S,3**(2*M+1))
    return (2*total[0],2*total[1]+tail)
L2=ln_unit(Q(2))
def log2(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(Q(2)**e)
    if y<1:e-=1;y*=2
    if y>=2:e+=1;y/=2
    if y==1:return (e*S,e*S)
    a=ln_unit(y)
    return (e*S+a[0]*S//L2[1],e*S+ceildiv(a[1]*S,L2[0]))
def entropy(ps):
    result=(0,0)
    for p in ps:
        assert 0<=p<=1
        if p:
            a=log2(p);result=add(result,scale((-a[1],-a[0]),p))
    return result
def walsh(a):
    a=a[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a
def profile(a):
    N=len(a);w=walsh(a)
    ps=[Q(t*t,N*N) for t in w]
    assert sum(ps)==1
    return entropy(ps),sum(p*j.bit_count() for j,p in enumerate(ps))
def display(a):return [str(Q(x,S)) for x in a]
start=time.monotonic();p=Q(5,8); H,I=profile([-1]*5+[1]*3);rows=[]
for d in range(13):
    rows.append({'depth':d,'variables':3*(1<<d),'p_sha256':hashlib.sha256(str(p).encode()).hexdigest(),'p_denominator_bits':p.denominator.bit_length(),'H_interval':display(H),'I_interval':display(qinterval(I)),'excess_interval':display(sub(H,qinterval(6*I)))})
    if d==12:break
    v=4*p*(1-p);m=1-2*p*p
    H=add(entropy([m*m,p*p*v,p*p*v,v*v/4]),scale(sub(H,entropy([(1-2*p)**2,v])),2*p))
    I=2*p*I;p=1-p*p
excess=sub(H,qinterval(6*I))
assert excess[0]*100>139*S
assert excess[1]*5<7*S
# independent physical truth table check of recurrence, all Boolean leaves of1bit.
small=0
for a in ([1,1],[1,-1],[-1,1],[-1,-1]):
    pp=Q(a.count(-1),2);hh,ii=profile(list(a));vv=4*pp*(1-pp);mm=1-2*pp*pp
    actual=[1 if x==-1 and y==-1 else -1 for y in a for x in a]
    ha,ia=profile(actual)
    if vv:
        predicted=add(entropy([mm*mm,pp*pp*vv,pp*pp*vv,vv*vv/4]),scale(sub(hh,entropy([(1-2*pp)**2,vv])),2*pp))
        assert predicted[0]<=ha[1] and ha[0]<=predicted[1]
    else:assert ha==(0,0)
    assert ia==2*pp*ii;small+=1
out={'status':'PASS','precision_bits':100,'atanh_terms':48,'levels':rows,'H_approx':sum(H)/(2*S),'I_approx':float(I),'excess_approx':sum(excess)/(2*S),'certified_excess_bounds':['139/100','7/5'],'same_original_reserve_lower_bound':'9/8 E + 3/5 delta','small_boundary_recurrence_checks':small,'elapsed_s':time.monotonic()-start}
(root/'out'/'CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='levels'}))
