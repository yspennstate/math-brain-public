"""Exact signed cubic fusion bound (C) on the four-parameter box."""
import argparse,itertools,json,math,pathlib,time
from fractions import Fraction as F
from fourth_polynomial_certificate import memory_check,add,scale,mul,powr,ypoly,zpoly,lift,liftD
ROOT=pathlib.Path(__file__).resolve().parent
def save(mode,phase,poly,meta):
    obj=dict(meta);obj.update({'mode':mode,'phase':phase,'terms':len(poly),'poly':[[list(k),v] for k,v in sorted(poly.items())]})
    path=ROOT/f'ternary_cubic_{mode}_{phase}.json';path.write_text(json.dumps(obj,separators=(',',':')),encoding='utf-8')
    print('Saved cubic',mode,phase,'terms',len(poly),'negative',sum(v<0 for v in poly.values()),'bytes',path.stat().st_size,flush=True)
def load(mode,phase):
    meta=json.loads((ROOT/f'ternary_cubic_{mode}_{phase}.json').read_text(encoding='utf-8'));return {tuple(k):v for k,v in meta.pop('poly')},meta
def raw(mode):
    start=time.monotonic();A=99;B=140;eta=F(2887,5000);C=F(5,3);p,q=C.numerator,C.denominator;L=F(B,A);R=eta*L
    aa=[ypoly(-2,0),ypoly(-2,3),ypoly(4,-3)];bb=[zpoly(-2,0),zpoly(-2,3),zpoly(4,-3)]
    Qy=add(*(mul(v,v) for v in aa));Qz=add(*(mul(v,v) for v in bb));Ty=add(*(powr(v,3,2) for v in aa));Tz=add(*(powr(v,3,2) for v in bb))
    S=[];Ws=[]
    for rr in itertools.permutations(bb):
        c=add(*(mul(aa[i],rr[i]) for i in range(3)));base={(0,0,0):12*B*B};base.update({(1,y,z):A*A*v for (y,z),v in c.items()});S.append(powr(base,2,3))
        vs=[]
        for i in range(3):
            vs.append(add(lift(scale(aa[i],6*A*B),1,0),lift(scale(rr[i],6*A*B),0,1),lift(scale(mul(aa[i],rr[i]),3*A*A),1,1),lift(scale(c,-A*A),1,1)))
        assert not add(*vs)
        Ws.append(add(*(powr(v,3,4) for v in vs)))
    D={(0,0,0):1}
    for f in S:D=mul(D,f)
    sign=1 if mode=='upper' else -1
    rhs=add(lift(scale(Ty,sign*18*q*A**3*B),3,0),lift(scale(Tz,sign*18*q*A**3*B),0,3),lift(scale(mul(Qy,Qz),9*p*A**4),2,2));P=mul(rhs,liftD(D))
    for j,W in enumerate(Ws):
        dm={(0,0,0):1}
        for k,factor in enumerate(S):
            if k!=j:dm=mul(dm,factor)
        P=add(P,scale(mul(W,liftD(dm)),-sign*2*q*B*B));assert time.monotonic()-start<480
    assert all(t>=2 and s>=2 for t,s,y,z in P)
    P={(t-2,s-2,y,z):v for (t,s,y,z),v in P.items()};degrees=[max(k[i] for k in P) for i in range(4)]
    P={k:v*L.numerator**k[0]*L.denominator**(degrees[0]-k[0])*R.numerator**k[1]*R.denominator**(degrees[1]-k[1]) for k,v in P.items()}
    content=math.gcd(*P.values());P={k:v//content for k,v in P.items()};estimate=math.prod(d+1 for d in degrees)*600;assert estimate<500*1024**2
    meta={'status':'raw polynomial, before the Bernstein transforms','lambda_common':'99/140','eta':str(eta),'C_cubic':str(C),'raw_domain_t_upper':str(L),'raw_domain_s_upper':str(R),'degrees':degrees,'raw_gcd_divided_out':str(content),'estimated_memory_bytes':estimate,'arithmetic':'exact integers with rational domain rescaling','raw_wall_seconds':time.monotonic()-start,'inequality':'K3<=Tleft+Tright+C*mleft*mright' if mode=='upper' else 'K3>=Tleft+Tright-C*mleft*mright','normalization':'P/(144*q*B^4*product Snum^2) is the signed target gap before t^2s^2 division and domain rescaling'}
    save(mode,'raw',P,meta)
def transform(mode,phase):
    index=int(phase[-1]);poly,meta=load(mode,'raw' if index==1 else f'bern{index-1}');axis=[2,3,0,1][index-1];degree=meta['degrees'][axis];L=math.lcm(*(math.comb(degree,i) for i in range(degree+1)));out={};start=time.monotonic()
    for key,v in poly.items():
        i=key[axis]
        for j in range(i,degree+1):
            kk=list(key);kk[axis]=j;kk=tuple(kk);out[kk]=out.get(kk,0)+v*math.comb(j,i)*(L//math.comb(degree,i))
    out={k:v for k,v in out.items() if v};content=math.gcd(*out.values());out={k:v//content for k,v in out.items()};assert time.monotonic()-start<480
    meta['transformed_axes']=meta.get('transformed_axes',[])+[axis];meta['wall_transform_seconds']=time.monotonic()-start
    if index==4:
        meta['status']='PASS: all cubic-gap Bernstein coefficients nonnegative on the full box' if all(v>=0 for v in out.values()) else 'INCOMPLETE: negative Bernstein coefficients; no cubic bound certified'
        meta['negative_coefficients']=sum(v<0 for v in out.values())
    save(mode,phase,out,meta);print(meta['status'],flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['upper','lower'],required=True);p.add_argument('--phase',choices=['raw','bern1','bern2','bern3','bern4'],required=True);a=p.parse_args();memory_check()
    if a.phase=='raw':raw(a.mode)
    else:transform(a.mode,a.phase)
