"""Exact integer polynomial attempt, checkpointed one transform per command.

No bound is certified unless the final Bernstein coefficients are nonnegative.
Estimated peak memory below 500MB, one CPU, no downloaded code.
"""
import argparse,ctypes,itertools,json,math,pathlib,time
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parent

def memory_check():
    class Mem(ctypes.Structure):
        _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong)]+[(n,ctypes.c_ulonglong) for n in ['total_phys','avail_phys','total_page','avail_page','total_virtual','avail_virtual','extended']]
    m=Mem();m.length=ctypes.sizeof(m);assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    print('Free physical bytes',m.avail_phys,flush=True);assert m.avail_phys>=2*1024**3

def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def scale(p,v):return {k:x*v for k,x in p.items() if x*v}
def mul(a,b):
    out={}
    for ka,va in a.items():
        for kb,vb in b.items():
            key=tuple(x+y for x,y in zip(ka,kb));out[key]=out.get(key,0)+va*vb
    return {k:v for k,v in out.items() if v}
def powr(p,n,dim):
    out={(0,)*dim:1}
    for _ in range(n):out=mul(out,p)
    return out
def ypoly(c0,c1):return {(0,0):c0,(1,0):c1}
def zpoly(c0,c1):return {(0,0):c0,(0,1):c1}
def lift(p,t,s):return {(t,s,y,z):v for (y,z),v in p.items() if v}
def liftD(p):return {(w,w,y,z):v for (w,y,z),v in p.items() if v}
def save(phase,poly,meta):
    path=ROOT/f'fourth_poly_{phase}.json'
    meta=dict(meta);meta['phase']=phase;meta['terms']=len(poly);meta['poly']=[[list(k),v] for k,v in sorted(poly.items())]
    path.write_text(json.dumps(meta,separators=(',',':')),encoding='utf-8')
    print('Saved',phase,'terms',len(poly),'negative',sum(v<0 for v in poly.values()),'bytes',path.stat().st_size,flush=True)
def load(phase):
    data=json.loads((ROOT/f'fourth_poly_{phase}.json').read_text(encoding='utf-8'));poly={tuple(k):v for k,v in data.pop('poly')};return poly,data

def raw():
    started=time.monotonic();A=99;B=140;K=12*B*B
    a=[ypoly(-2,0),ypoly(-2,3),ypoly(4,-3)]
    b=[zpoly(-2,0),zpoly(-2,3),zpoly(4,-3)]
    Qy=add(*(mul(v,v) for v in a));Qz=add(*(mul(v,v) for v in b))
    S=[];Ns=[]
    for j,rr in enumerate(itertools.permutations(b)):
        c=add(*(mul(a[i],rr[i]) for i in range(3)))
        l21=add(*(mul(mul(a[i],a[i]),rr[i]) for i in range(3)))
        l12=add(*(mul(a[i],mul(rr[i],rr[i])) for i in range(3)))
        base={(0,0,0):K}
        base.update({(1,y,z):A*A*v for (y,z),v in c.items()})
        S.append(powr(base,3,3))
        N=add(lift(scale(Qy,24*A*A*B*B),2,0),lift(scale(Qz,24*A*A*B*B),0,2),lift(scale(c,48*A*A*B*B),1,1),lift(scale(l21,24*A**3*B),2,1),lift(scale(l12,24*A**3*B),1,2),lift(scale(mul(Qy,Qz),A**4),2,2))
        Ns.append(N)
    D={(0,0,0):1}
    for j,factor in enumerate(S):
        D=mul(D,factor);print('Denominator factor',j+1,'terms',len(D),'seconds',round(time.monotonic()-started,2),flush=True)
        assert time.monotonic()-started<480
    rhs=add(lift(scale(mul(Qy,Qy),2*A**8),4,0),lift(scale(mul(Qz,Qz),2*A**8),0,4),lift(scale(mul(Qy,Qz),3*A**4*B**4),2,2))
    P=mul(rhs,liftD(D))
    for j,N in enumerate(Ns):
        dm={(0,0,0):1}
        for k,factor in enumerate(S):
            if k!=j:dm=mul(dm,factor)
        P=add(P,scale(mul(mul(N,N),liftD(dm)),-A**4*B*B))
        print('Numerator orientation',j+1,'terms',len(P),'seconds',round(time.monotonic()-started,2),flush=True)
        assert time.monotonic()-started<480
    assert all(t>=2 and s>=2 for t,s,y,z in P), 'Expected exact t^2 s^2 divisibility failed'
    P={(t-2,s-2,y,z):v for (t,s,y,z),v in P.items()}
    content=math.gcd(*P.values());P={k:v//content for k,v in P.items()}
    degrees=[max(k[i] for k in P) for i in range(4)];dense_count=math.prod(n+1 for n in degrees)
    estimated_bytes=dense_count*400
    assert estimated_bytes<500*1024**2
    meta={'status':'attempt; positivity not yet established','lambda':'99/140','C':'3/2','variables':['t','s','y','z'],'degrees':degrees,'content_divided_out':str(content),'dense_coefficient_count':dense_count,'estimated_memory_bytes':estimated_bytes,'arithmetic':'arbitrary-precision integers; positive common denominators cleared','raw_wall_seconds':time.monotonic()-started}
    save('raw',P,meta)

def transform(phase):
    index=int(phase[-1]);previous='raw' if index==1 else f'bern{index-1}'
    poly,meta=load(previous);axis=[2,3,0,1][index-1];degree=meta['degrees'][axis]
    L=math.lcm(*(math.comb(degree,i) for i in range(degree+1)));out={};started=time.monotonic()
    for key,v in poly.items():
        i=key[axis]
        for j in range(i,degree+1):
            kk=list(key);kk[axis]=j;kk=tuple(kk)
            out[kk]=out.get(kk,0)+v*math.comb(j,i)*(L//math.comb(degree,i))
    out={k:v for k,v in out.items() if v};assert time.monotonic()-started<480
    content=math.gcd(*out.values());out={k:v//content for k,v in out.items()}
    meta['transformed_axes']=meta.get('transformed_axes',[])+[axis]
    meta['transform_wall_seconds']=time.monotonic()-started
    if index==4:
        meta['status']='PASS: exact tensor-product Bernstein nonnegativity on the full unit hypercube' if all(v>=0 for v in out.values()) else 'INCOMPLETE: negative Bernstein coefficients; no bound established'
        meta['negative_coefficient_count']=sum(v<0 for v in out.values())
    save(phase,out,meta)
    print(meta['status'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--phase',choices=['raw','bern1','bern2','bern3','bern4'],required=True);a=p.parse_args()
    memory_check()
    if a.phase=='raw':raw()
    else:transform(a.phase)
