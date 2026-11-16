"""NUMERICAL discovery conversion; the separate integer replay is the proof."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import json,math,sys
from pathlib import Path
import numpy as np
from sympy.polys.domains import QQ
from rank3_target55 import target
from inherited20.inherited19.inherited18.inherited17.memory_guard import install,peak_bytes

def main():
    install(450_000_000);rr,M,gs=target();meta=json.loads(Path('rank3_discovery_meta.json').read_text());blocks=meta['blocks'];arr=np.load('rank3_discovery.npz');D=10**10
    Gs=[[[int(round(float(x)*D))for x in row]for row in arr['arr_'+str(b)]]for b in range(len(blocks))]
    actual=[[rr.zero for j in range(4)]for i in range(4)];maps={};basis={};scalar_maps={}
    # All matrix blocks use the same monomial sets in each output coordinate.
    for bi,(block,G)in enumerate(zip(blocks,Gs)):
        n=block['n'];dim=block['dim'];g=rr.one if block['key'].startswith('free')else gs[block['key']]
        for v in range(dim):
            for u in range(v+1):
                power=tuple(a+b for a,b in zip(block['mons'][u//n],block['mons'][v//n]));i,j=sorted((u%n,v%n));fac=2 if i==j and u!=v else 1
                pol=rr.from_dict({power:QQ.one})*g
                if n==4:
                    actual[i][j]+=pol*QQ(fac*G[u][v],D)
                    maps.setdefault((i,j,block['key'],power),(bi,u,v,fac))
                else:
                    scalar_maps.setdefault((block['key'],power),(bi,u,v,fac))
                    for a in range(4):actual[a][a]+=pol*QQ(fac*G[u][v],D)
    # Sparse exact elimination on scalar polynomial generators, at most 210 rows.
    for i,j,key,power in maps:
        if (i,j)!=(0,0):continue
        origin=(key,power);p=rr.from_dict({power:QQ.one})*(rr.one if key.startswith('free')else gs[key]);rep={origin:QQ.one}
        while p:
            e=max(p);c=p[e]
            if e not in basis:
                basis[e]=(p/c,{key0:v/c for key0,v in rep.items()});break
            bp,br=basis[e];p-=c*bp
            for key0,v in br.items():
                rep[key0]=rep.get(key0,QQ.zero)-c*v
                if not rep[key0]:del rep[key0]
    print('scalar exact basis rank',len(basis),flush=True)
    def reduce_poly(p):
        remainder=rr.zero
        while p:
            e=max(p);c=p[e]
            if e in basis:p-=c*basis[e][0]
            else:
                term=rr.from_dict({e:c});remainder+=term;p-=term
        return remainder
    quotient={}
    for key,power in scalar_maps:
        origin=(key,power);pol=rr.from_dict({power:QQ.one})*gs[key];p=reduce_poly(pol);rep={origin:QQ.one}
        while p:
            e=max(p);c=p[e]
            if e not in quotient:
                quotient[e]=(p/c,{kk:vv/c for kk,vv in rep.items()});break
            bp,br=quotient[e];p-=c*bp
            for kk,vv in br.items():rep[kk]=rep.get(kk,QQ.zero)-c*vv
    rems=[reduce_poly(M[i][i]-actual[i][i])for i in range(4)]
    assert all(p==rems[0]for p in rems), 'scalar quotient differs across diagonals'
    p=rems[0];rep={};corrections=[]
    while p:
        e=max(p);c=p[e];assert e in quotient
        bp,br=quotient[e];p-=c*bp
        for kk,vv in br.items():rep[kk]=rep.get(kk,QQ.zero)+c*vv
    for (key,power),co in rep.items():
        bi,u,v,fac=scalar_maps[key,power];corrections.append((bi,u,v,co/fac))
        pol=rr.from_dict({power:QQ.one})*gs[key]
        for i in range(4):actual[i][i]+=co*pol
    print('scalar quotient rank',len(quotient),flush=True)
    for i in range(4):
        for j in range(i,4):
            p=M[i][j]-actual[i][j];rep={}
            while p:
                e=max(p);c=p[e];assert e in basis,('unspanned exact residual',i,j,e)
                bp,br=basis[e];p-=c*bp
                for key0,v in br.items():rep[key0]=rep.get(key0,QQ.zero)+c*v
            for (key,power),co in rep.items():
                bi,u,v,fac=maps[i,j,key,power];corrections.append((bi,u,v,co/fac))
    den=D
    for bi,u,v,co in corrections:den=math.lcm(den,int(co.denominator))
    ints=[[[x*(den//D)for x in row]for row in G]for G in Gs]
    for bi,u,v,co in corrections:
        val=int(co*den);ints[bi][u][v]+=val
        if u!=v:ints[bi][v][u]+=val
    Df=den*10**4;certblocks=[]
    for block,G in zip(blocks,ints):
        vals=np.array([[float(QQ(x,den))for x in row]for row in G]);L=np.linalg.cholesky(vals-np.eye(block['dim'])/100)
        LL=[[int(round(float(L[i,j])*Df))for j in range(i+1)]for i in range(block['dim'])]
        certblocks.append(dict(**block,G=[[G[i][j]for j in range(i+1)]for i in range(block['dim'])],chol=LL))
    cert=dict(schema=1,margin='1/5',gamma=4,gram_denominator=den,factor_denominator=Df,blocks=certblocks)
    Path('rank3_sos55.json').write_text(json.dumps(cert,separators=(',',':'))+'\n')
    print('wrote exact candidate',len(corrections),'corrections','denominator',den,'peak',peak_bytes(),flush=True)
if __name__=='__main__':main()
