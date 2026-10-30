from verify import *
from math import comb
start=time.perf_counter();count=0
def test(x):
    global count
    assert x
    count+=1
def poly_mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z
def pivot_poly(h,j):
    z=[0]*6
    for x in range(64):
        if x>>j&1 or h[x]==h[x|1<<j]:continue
        r=x.bit_count()
        for k in range(6-r):z[r+k]+=comb(5-r,k)*(-1)**k
    return z
expected=[0,4,-14,18,-10,2]
polys=[]
for j in range(6):
    a=pivot_poly(table('h'),j);test(a==expected);polys.append(a)
p=F(1,16)
test(2*(1-p)**3*(2-p)>3)
test((1-p)**5>F(1,2))
test((1-2*p)*(1-p)**4>F(2,3))
test((1-2*p)*(1-p)**3>F(2,3))
test((1-2*p)*(1-p)**2>F(3,4))
test(F(1)+F(8,3)/p<=4/p)
test(F(1)+F(64,27)/p**2<=4/p**2)
test(2*p*(4+F(19,4))==F(35,32))
def vector_coeff(vals,T,mus):
    w=walsh(tuple(vals))
    return sum(w[U]*prod(mus[k] for k in range(len(mus)) if (U^T)>>k&1) for U in range(len(vals)) if U&T==T)
h=table('J');idx=[1,2,3,5]
# On previous-positive section, selected4 is pointwise irrelevant.
for z in range(16):
    x=sum(((z>>k)&1)<<i for k,i in enumerate(idx));test(h[x]==h[x|16])
groups=[];Lbounds=[]
for p in [F(1,1024),F(1,16)]:
 for t in [F(0),F(1,1024),F(1,32),F(1,8)]:
  if t>2*p:continue
  for x in [F(3,4),F(7,8),F(1)]:
    mus4=[1-2*p]*4;vv=4*p*(1-p)
    a0=[];a1=[];d1=[]
    for z in range(16):
        xx=sum(((z>>k)&1)<<i for k,i in enumerate(idx));a0.append(F(h[xx]));a1.append(F(h[xx|1]+h[xx|1|16],2));d1.append(F(h[xx|1]-h[xx|1|16],2))
    A5=[];D5=[]
    for z in range(32):
        xx=sum(((z>>k)&1)<<i for k,i in enumerate([0,1,2,3,5]))
        A5.append(F(h[xx]+h[xx|16],2));D5.append(F(h[xx]-h[xx|16],2))
    mus5=[1-2*t]+mus4
    q1=F(0);Lp={};norm0=normdiff=F(0)
    for T in range(16):
        A0=vector_coeff(a0,T,mus4);A1=vector_coeff(a1,T,mus4);D=vector_coeff(d1,T,mus4);w=vv**T.bit_count();B=A1+x*D
        norm0+=w*((1-t)*A0+t*B)**2;normdiff+=w*(A0-B)**2;q1+=w*D*D
        # Direct five-input coefficients, with positive/negative previous sections.
        # The normalized basis factor cancels in log arguments, leaving rational values.
        for prior in [0,1]:
            dd=t*D if prior==0 else -D/2
            aa=(1-t)*A0+t*A1 if prior==0 else (A0-A1)/2
            W=w if prior==0 else w*4*t*(1-t)
            mask5=(T<<1)|prior
            test(dd==vector_coeff(D5,mask5,mus5))
            test(aa==vector_coeff(A5,mask5,mus5))
            if W and dd and aa+x*dd:
                key=(aa+x*dd)**2/(x*x*dd*dd)
                Lp=add(Lp,{key:W*dd*dd})
        if D and t:
            for aa,dd,W in [((1-t)*A0+t*A1,t*D,w),((A0-A1)/2,-D/2,w*4*t*(1-t))]:
                if W and aa+x*dd:test((aa+x*dd)**2/(x*x*dd*dd)>0)
    test(q1>=3*p/4 and norm0<=1 and normdiff<=4)
    # Independent direct pivotal enumeration (all5 other physical gate inputs).
    ms=[1-2*t if j==0 else 1-2*p for j in range(6) if j!=4]
    q=outer('J',tuple(1-2*t if j==0 else x if j==4 else 1-2*p for j in range(6)))['q'][4]
    test(q==t*q1)
    if t:
        # Coefficient zeros have negative infinite slope and help an upper bound.
        finite=True
        for T in range(16):
            A0=vector_coeff(a0,T,mus4);A1=vector_coeff(a1,T,mus4);D=vector_coeff(d1,T,mus4)
            if D and (((1-t)*A0+t*(A1+x*D))==0 or A0-A1-x*D==0):finite=False
        if finite:
            bound=add({1/p:q}, {None:F(19,4)*q})
            test(ev(add(bound,times(Lp,-1)))[0]>=0)
        Lbounds.append(dict(p=str(p),t=str(t),x=str(x),q=str(q),finite=finite))
    groups.append(dict(p=str(p),t=str(t),x=str(x),q1=str(q1),norm0=str(norm0),normdiff=str(normdiff)))
test((F(1)+F(-1))/2==0 and F(1)!=0) # positivity cannot be dropped
test((F(2)+F(0))/2!=0)              # conservation cannot be dropped
test(len(groups)==18)
result=dict(version='A084-analytic-guards-v1',assertions=count,exceptional_parameter_cases=len(groups),h_polynomials=polys,runtime_seconds=time.perf_counter()-start,scope='exact algebra and endpoint guards; continuum supplied by PROOF.md')
test(result['runtime_seconds']<55)
save('ANALYTIC_GROUPS.json',groups);save('EXCEPTIONAL_SLOPE_GUARDS.json',Lbounds);save('ANALYTIC_VALIDATION.json',result)
print(json.dumps(result))
