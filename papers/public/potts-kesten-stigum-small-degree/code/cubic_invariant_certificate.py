"""Attempt an all-domain sufficient inequality for nonnegative cubic invariance."""
import argparse,itertools,json,math,pathlib,time
from fractions import Fraction as F
from fourth_polynomial_certificate import memory_check,add,scale,mul,powr,ypoly,zpoly,lift,liftD
ROOT=pathlib.Path(__file__).resolve().parent

def save(domain,phase,poly,meta):
    result=dict(meta);result.update({'domain':domain,'phase':phase,'terms':len(poly),'poly':[[list(k),v] for k,v in sorted(poly.items())]})
    target=ROOT/f'cubic_invariant_{domain}_{phase}.json';target.write_text(json.dumps(result,separators=(',',':')),encoding='utf-8')
    print('Saved',domain,phase,'terms',len(poly),'negative',sum(v<0 for v in poly.values()),flush=True)

def load(domain,phase):
    meta=json.loads(ROOT.joinpath(f'cubic_invariant_{domain}_{phase}.json').read_text(encoding='utf-8'))
    return {tuple(k):v for k,v in meta.pop('poly')},meta

def raw(domain):
    start=time.monotonic();A=99;B=140
    L=F(B,A);R=L if domain=='full' else L*F(2887,5000)
    aa=[ypoly(-2,0),ypoly(-2,3),ypoly(4,-3)];bb=[zpoly(-2,0),zpoly(-2,3),zpoly(4,-3)]
    Qy=add(*(mul(v,v) for v in aa));Qz=add(*(mul(v,v) for v in bb))
    Ty=add(*(powr(v,3,2) for v in aa));Tz=add(*(powr(v,3,2) for v in bb))
    factors=[];Ws=[]
    for rr in itertools.permutations(bb):
        c=add(*(mul(aa[i],rr[i]) for i in range(3)))
        base={(0,0,0):12*B*B};base.update({(1,y,z):A*A*v for (y,z),v in c.items()});factors.append(powr(base,2,3))
        vs=[add(lift(scale(aa[i],6*A*B),1,0),lift(scale(rr[i],6*A*B),0,1),
                lift(scale(mul(aa[i],rr[i]),3*A*A),1,1),lift(scale(c,-A*A),1,1)) for i in range(3)]
        assert not add(*vs);Ws.append(add(*(powr(v,3,4) for v in vs)))
    D={(0,0,0):1}
    for factor in factors:D=mul(D,factor)
    rhs=add(lift(scale(Ty,-72*A**3*B*B),3,0),lift(scale(Tz,-72*A**3*B*B),0,3),
            lift(scale(mul(Ty,Qz),3*A**5),3,2),lift(scale(mul(Qy,Tz),3*A**5),2,3))
    P=mul(rhs,liftD(D))
    for j,W in enumerate(Ws):
        dm={(0,0,0):1}
        for k,factor in enumerate(factors):
            if j!=k:dm=mul(dm,factor)
        P=add(P,scale(mul(W,liftD(dm)),8*B**3));assert time.monotonic()-start<480
    assert all(t>=2 and s>=2 for t,s,y,z in P)
    P={(t-2,s-2,y,z):v for (t,s,y,z),v in P.items()};deg=[max(k[i] for k in P) for i in range(4)]
    P={k:v*L.numerator**k[0]*L.denominator**(deg[0]-k[0])*R.numerator**k[1]*R.denominator**(deg[1]-k[1]) for k,v in P.items()}
    content=math.gcd(*P.values());P={k:v//content for k,v in P.items()}
    estimate=math.prod(n+1 for n in deg)*600;assert estimate<500*1024**2
    meta={'status':'attempt; no universal inequality established','lambda_common':'99/140','raw_domain_t_upper':str(L),'raw_domain_s_upper':str(R),
          'degrees':deg,'raw_gcd_divided_out':str(content),'estimated_memory_bytes':estimate,
          'target':'T_out >= (1-M_right/6)*T_left+(1-M_left/6)*T_right',
          'normalization':'P/(576*B^5*product Snum^2) is target gap before t^2s^2 division and radial rescaling',
          'raw_wall_seconds':time.monotonic()-start}
    save(domain,'raw',P,meta)

def transform(domain,phase):
    number=int(phase[-1]);poly,meta=load(domain,'raw' if number==1 else f'bern{number-1}')
    axis=[2,3,0,1][number-1];n=meta['degrees'][axis];den=math.lcm(*(math.comb(n,i) for i in range(n+1)));out={}
    for key,v in poly.items():
        for j in range(key[axis],n+1):
            kk=list(key);kk[axis]=j;kk=tuple(kk)
            out[kk]=out.get(kk,0)+v*math.comb(j,key[axis])*(den//math.comb(n,key[axis]))
    out={k:v for k,v in out.items() if v};g=math.gcd(*out.values());out={k:v//g for k,v in out.items()}
    meta['transformed_axes']=meta.get('transformed_axes',[])+[axis]
    if number==4:
        meta['status']='PASS all Bernstein coefficients nonnegative' if all(v>=0 for v in out.values()) else 'INCOMPLETE negative coefficients; no all-domain proof'
        meta['negative_coefficients']=sum(v<0 for v in out.values())
    save(domain,phase,out,meta);print(meta['status'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--domain',choices=['full','eta'],required=True);p.add_argument('--phase',choices=['raw','bern1','bern2','bern3','bern4'],required=True)
    a=p.parse_args();memory_check()
    if a.phase=='raw':raw(a.domain)
    else:transform(a.domain,a.phase)
