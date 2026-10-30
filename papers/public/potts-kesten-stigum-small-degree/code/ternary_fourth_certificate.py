"""Bernstein certificates for the fourth-moment fusion bounds (F) and (F1)."""
import argparse,itertools,json,math,pathlib,time,hashlib
from fractions import Fraction as F
from fourth_polynomial_certificate import memory_check,add,scale,mul,powr,ypoly,zpoly,lift,liftD
ROOT=pathlib.Path(__file__).resolve().parent
def save(mode,phase,poly,meta):
    obj=dict(meta);obj.update({'mode':mode,'phase':phase,'terms':len(poly),'poly':[[list(k),v] for k,v in sorted(poly.items())]})
    path=ROOT/f'ternary_fourth_{mode}_{phase}.json';path.write_text(json.dumps(obj,separators=(',',':')),encoding='utf-8')
    print('Saved',mode,phase,'terms',len(poly),'negative',sum(v<0 for v in poly.values()),'bytes',path.stat().st_size,flush=True)
def load(mode,phase):
    meta=json.loads((ROOT/f'ternary_fourth_{mode}_{phase}.json').read_text(encoding='utf-8'));return {tuple(k):v for k,v in meta.pop('poly')},meta
def parameters(mode):
    if mode=='prefix':return 2887,5000,F(3,5),F(1),F(1)
    A=99;B=140;return A,B,5*F(A,B)**4,F(B,A),F(2887,5000)*F(B,A)
def raw(mode):
    start=time.monotonic();A,B,C,L,R=parameters(mode);p,q=C.numerator,C.denominator;K=12*B*B
    aa=[ypoly(-2,0),ypoly(-2,3),ypoly(4,-3)];bb=[zpoly(-2,0),zpoly(-2,3),zpoly(4,-3)]
    Qy=add(*(mul(v,v) for v in aa));Qz=add(*(mul(v,v) for v in bb));S=[];Ns=[]
    for rr in itertools.permutations(bb):
        c=add(*(mul(aa[i],rr[i]) for i in range(3)))
        l21=add(*(mul(mul(aa[i],aa[i]),rr[i]) for i in range(3)));l12=add(*(mul(aa[i],mul(rr[i],rr[i])) for i in range(3)))
        base={(0,0,0):K};base.update({(1,y,z):A*A*v for (y,z),v in c.items()});S.append(powr(base,3,3))
        N=add(lift(scale(Qy,24*A*A*B*B),2,0),lift(scale(Qz,24*A*A*B*B),0,2),lift(scale(c,48*A*A*B*B),1,1),lift(scale(l21,24*A**3*B),2,1),lift(scale(l12,24*A**3*B),1,2),lift(scale(mul(Qy,Qz),A**4),2,2));Ns.append(N)
    D={(0,0,0):1}
    for factor in S:D=mul(D,factor)
    rhs=add(lift(scale(mul(Qy,Qy),2*q*A**8),4,0),lift(scale(mul(Qz,Qz),2*q*A**8),0,4),lift(scale(mul(Qy,Qz),2*p*A**4*B**4),2,2))
    P=mul(rhs,liftD(D))
    for j,N in enumerate(Ns):
        dm={(0,0,0):1}
        for k,factor in enumerate(S):
            if k!=j:dm=mul(dm,factor)
        P=add(P,scale(mul(mul(N,N),liftD(dm)),-q*A**4*B*B));assert time.monotonic()-start<480
    assert all(t>=2 and s>=2 for t,s,y,z in P)
    P={(t-2,s-2,y,z):v for (t,s,y,z),v in P.items()};degrees=[max(k[i] for k in P) for i in range(4)]
    # Exact positive denominator-clearing for H(L*t,R*s,y,z).
    P={k:v*L.numerator**k[0]*L.denominator**(degrees[0]-k[0])*R.numerator**k[1]*R.denominator**(degrees[1]-k[1]) for k,v in P.items()}
    content=math.gcd(*P.values());P={k:v//content for k,v in P.items()}
    estimate=math.prod(d+1 for d in degrees)*600;assert estimate<500*1024**2
    meta={'status':'raw polynomial, before the Bernstein transforms','lambda_common':str(F(A,B)),'C_edge_scaled':str(C),'raw_domain_t_upper':str(L),'raw_domain_s_upper':str(R),'degrees':degrees,'estimated_memory_bytes':estimate,'arithmetic':'arbitrary-precision integers, exact rational domain rescaling','wall_raw_seconds':time.monotonic()-start,'raw_gcd_divided_out':str(content),'inequality':'edge-scaled two-child prefix with C=3/5' if mode=='prefix' else 'root-scaled generic fusion U_out<=U_left+U_right+5*m_left*m_right, left arbitrary and right min coordinate >=(1-2887/5000)/3'}
    save(mode,'raw',P,meta)
def transform(mode,phase):
    index=int(phase[-1]);poly,meta=load(mode,'raw' if index==1 else f'bern{index-1}');axis=[2,3,0,1][index-1];degree=meta['degrees'][axis]
    L=math.lcm(*(math.comb(degree,i) for i in range(degree+1)));out={};start=time.monotonic()
    for key,v in poly.items():
        i=key[axis]
        for j in range(i,degree+1):
            kk=list(key);kk[axis]=j;kk=tuple(kk);out[kk]=out.get(kk,0)+v*math.comb(j,i)*(L//math.comb(degree,i))
    out={k:v for k,v in out.items() if v};content=math.gcd(*out.values());out={k:v//content for k,v in out.items()};assert time.monotonic()-start<480
    meta['transformed_axes']=meta.get('transformed_axes',[])+[axis];meta['wall_transform_seconds']=time.monotonic()-start
    if index==4:
        meta['status']='PASS: exact Bernstein nonnegativity over the specified full parameter rectangle' if all(v>=0 for v in out.values()) else 'INCOMPLETE: negative coefficients; no inequality established'
        meta['negative_coefficients']=sum(v<0 for v in out.values())
    save(mode,phase,out,meta);print(meta['status'],flush=True)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['prefix','merge'],required=True);parser.add_argument('--phase',choices=['raw','bern1','bern2','bern3','bern4'],required=True);args=parser.parse_args()
    original=json.loads((ROOT/'fourth_polynomial_independent_check.json').read_text(encoding='utf-8'))['sha256']['fourth_polynomial_certificate.py'];assert hashlib.sha256((ROOT/'fourth_polynomial_certificate.py').read_bytes()).hexdigest()==original
    memory_check()
    if args.phase=='raw':raw(args.mode)
    else:transform(args.mode,args.phase)
