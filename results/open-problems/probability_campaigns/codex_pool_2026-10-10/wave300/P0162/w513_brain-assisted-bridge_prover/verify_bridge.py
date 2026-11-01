"""Independent truth-table/Walsh checks of exact FEI bridge deductions.

No stores are opened. One process; <=2048 truth-table values; bounded run.
Exact integer Walsh coefficients, then double precision entropy: these are
arithmetic checks, not a formal proof or an audit of the general conjecture.
"""
import ctypes
import datetime
import json
import math
import pathlib
import time

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
gate=dict(timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
          max_seconds=30,max_table_size=2048,exhaustive_dimension=3,bent_m_max=10,
          processes=1,gpu=False,background=False)
class Memory(ctypes.Structure):
    _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong)]+[(name,ctypes.c_ulonglong) for name in
        ('total_phys','avail_phys','total_page','avail_page','total_virtual','avail_virtual','avail_extended')]
memory=Memory(); memory.length=ctypes.sizeof(memory)
if hasattr(ctypes,'windll'):
    ok=ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory))
    gate.update(memory_query_ok=bool(ok),available_memory=memory.avail_phys)
    if not ok or memory.avail_phys<64*1024*1024:
        gate['allowed']=False
        (root/'compute_gate.json').write_text(json.dumps(gate,indent=2),encoding='utf-8')
        raise SystemExit('Fresh memory gate failed; experiment not run.')
gate['allowed']=True
(root/'compute_gate.json').write_text(json.dumps(gate,indent=2),encoding='utf-8')

def guard():
    if time.perf_counter()-start>gate['max_seconds']:
        raise RuntimeError('Bounded compute time exhausted')

def walsh(values):
    assert len(values)<=gate['max_table_size']
    w=list(values); step=1
    while step<len(w):
        for base in range(0,len(w),2*step):
            for j in range(base,base+step):
                a,b=w[j],w[j+step]
                w[j],w[j+step]=a+b,a-b
        step*=2
    return [x/len(w) for x in w]

def entropy(p):
    return math.fsum(-x*math.log2(x) for x in p if x>0)

def binary(q):
    if q<=0 or q>=1: return 0.0
    return -q*math.log2(q)-(1-q)*math.log1p(-q)/math.log(2)

def split(values,i):
    plus=[];minus=[]
    for x in range(len(values)):
        (minus if (x>>i)&1 else plus).append(values[x])
    return plus,minus

def check(values,i):
    f=walsh(values);g,h=split(values,i);a,b=walsh(g),walsh(h)
    p,q=[x*x for x in a],[x*x for x in b]
    r=[(x+y)/2 for x,y in zip(p,q)]
    js=entropy(r)-(entropy(p)+entropy(q))/2
    cond=math.fsum(weight*binary((x-y)**2/(4*weight)) for weight,x,y in zip(r,a,b) if weight>0)
    influence=math.fsum((x-y)**2/4 for x,y in zip(a,b))
    delta=entropy([x*x for x in f])-(entropy(p)+entropy(q))/2
    residual=abs(delta-js-cond)
    assert residual<2e-11,(delta,js,cond)
    assert js>=-2e-11
    assert js<=2/math.log(2)*influence+2e-11
    assert cond<=binary(influence)+2e-11
    return dict(delta=delta,js=js,conditional_entropy=cond,influence=influence,
                ratio=delta/influence if influence else None,residual=residual,
                entropy=entropy([x*x for x in f]))

report=dict(command='python -X utf8 ~/brain_workers/w513/verify_bridge.py',gate=gate,
            floating_point_only=True,formal_check=False)
# f(x,z)=x for z=+1, 1 for z=-1; bit=0 means +1.
report['disjoint_witness']=check([1,-1,1,1],1)
assert report['disjoint_witness']['delta']==2
assert report['disjoint_witness']['conditional_entropy']==1
assert report['disjoint_witness']['js']==1
report['discarded_identity_error_bits']=1
report['corrected_identity_error_bits']=report['disjoint_witness']['residual']
max_residual=0;count=0
for mask in range(256):
    guard()
    values=[1 if (mask>>x)&1 else -1 for x in range(8)]
    for i in range(3):
        r=check(values,i);max_residual=max(max_residual,r['residual']);count+=1
report['exhaustive']=dict(functions=256,coordinate_checks=count,max_residual=max_residual)
report['rare_switch']=[]
for m in (2,4,6,8,10):
    guard()
    n=1<<m
    g=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2)) for x in range(n)]
    h=list(g);h[0]=-h[0]
    coeff=walsh(g)
    assert all(abs(abs(x)-1/math.sqrt(n))<1e-15 for x in coeff)
    r=check(g+h,m)
    assert r['influence']==1/n
    assert r['ratio']>=m-1-1e-11
    r.update(m=m,N=n,proved_lower_ratio=m-1)
    report['rare_switch'].append(r)
guard()
# A genuinely Boolean nine-bit composition, not a precomputed spectral table.
m=2;gadget_width=3;alpha=0.5
composed=[]
for value in range(1<<9):
    out=[]
    for block in range(3):
        ones=sum((value>>(3*block+j))&1 for j in range(3))
        out.append(1 if ones<=1 else -1)
    x0,x1=(int(out[j]==-1) for j in (0,1))
    g=(-1)**(x0*x1)
    if out[2]==-1 and x0==x1==0: g=-g
    composed.append(g)
v=6
physical_influences=[sum(composed[x]!=composed[x^(1<<i)] for x in range(len(composed)))/len(composed) for i in range(9)]
assert max(physical_influences)<=alpha
r=check(composed,v)
assert r['influence']==alpha/(1<<m)
assert r['ratio']>=alpha*m-1e-11
outer=[1,1,1,-1,-1,1,1,-1]
outer_coeff=walsh(outer)
outer_H=entropy([x*x for x in outer_coeff])
outer_I=math.fsum(s.bit_count()*a*a for s,a in enumerate(outer_coeff))
composed_I=math.fsum(physical_influences)
assert abs(r['entropy']-(outer_H+outer_I*2))<2e-11
assert composed_I==outer_I*1.5
assert r['entropy']<=4*composed_I
r.update(m=m,gadget_width=gadget_width,alpha=alpha,physical_influences=physical_influences,
         proved_lower_ratio=alpha*m,physical_bits=9,total_influence=composed_I,
         entropy_over_total_influence=r['entropy']/composed_I,
         composition_entropy_residual=abs(r['entropy']-outer_H-outer_I*2))
report['composed_small_influence_witness']=r
# This is a closed-form lower-sector calculation, not an enumeration of 2^m bits.
report['small_influence_lower_sector']=[]
for m in (2,4,8,16,32):
    N=1<<m;eps=1/math.sqrt(N)
    B=0.0
    for sigma,count in ((1,(N+math.isqrt(N))//2),(-1,(N-math.isqrt(N))//2)):
        A=sigma*eps-eps*eps;deriv=alpha*eps*eps
        R=A*A+deriv*deriv;q=deriv*deriv/R
        B+=count*R*binary(q)
    ratio=B/(alpha/N)
    assert ratio>=alpha*m-1e-10
    report['small_influence_lower_sector'].append(dict(m=m,alpha=alpha,partial_B=B,
          selector_influence=alpha/N,partial_B_over_influence=ratio,proved_lower_ratio=alpha*m))
report['elapsed_s']=time.perf_counter()-start
(root/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
