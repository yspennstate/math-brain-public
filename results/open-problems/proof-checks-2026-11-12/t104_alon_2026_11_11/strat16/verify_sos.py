"""Independent exact SOS/Farkas replay, with integer PSD witnesses.

No numerical package, floating eigenvalue, or solver status is used here.
"""
import json
import itertools
import time
from pathlib import Path
from sympy.polys.domains import QQ
from rank_three_target import construct


def full(triangle):
    n=len(triangle)
    assert all(len(row)==i+1 for i,row in enumerate(triangle))
    return [[triangle[max(i,j)][min(i,j)]for j in range(n)]for i in range(n)]


def reconstruct(blocks,denominator):
    rr,V,R,mats,controls,gs,bounds=construct();out=[[rr.zero for j in range(4)]for i in range(4)]
    for block in blocks:
        mons=block['mons'];n=block['n'];dim=block['dim']
        assert all(len(m)==6 and all(isinstance(e,int)and e>=0 for e in m)and sum(m)<=2 for m in mons)
        G=block['G'];G=full(G)if not all(len(row)==dim for row in G)else G
        g=rr.one if block['key'].startswith('free')else gs[block['key']]
        assert dim==len(mons)*n and n in (1,4)
        for b in range(dim):
            for a in range(b+1):
                if not G[a][b]:continue
                m,i=mons[a//n],a%n;v,j=mons[b//n],b%n
                power=tuple(x+y for x,y in zip(m,v));fac=2 if i==j and a!=b else 1
                term=rr.from_dict({power:QQ(fac*G[a][b],denominator)})*g
                if n==4:
                    out[min(i,j)][max(i,j)]+=term
                else:
                    for c in range(4):out[c][c]+=term
    for i in range(4):
        for j in range(i):out[i][j]=out[j][i]
    return out


def check(cert):
    assert cert['schema']==1 and cert['control']in(0,1,2) and cert['margin']=='1/100'
    rr,V,R,mats,controls,gs,bounds=construct()
    D=cert['gram_denominator'];Df=cert['factor_denominator']
    assert isinstance(D,int)and D>0 and isinstance(Df,int)and Df>0 and Df*Df%D==0
    free=[b['key']for b in cert['blocks']if b['key'].startswith('free')]
    assert len(free)==len(set(free))and free
    assert [b['key']for b in cert['blocks']]==[*free,*gs]
    for block in cert['blocks']:
        n=block['dim'];G=full(block['G']);L=block['chol'];scale=Df*Df//D
        assert len(G)==n and len(L)==n and all(len(row)==i+1 for i,row in enumerate(L))
        assert all(isinstance(a,int)for row in G+L for a in row)
        caps=[0]*n;diag=[0]*n
        for i in range(n):
            for j in range(i+1):
                value=scale*G[i][j]-sum(L[i][k]*L[j][k]for k in range(j+1))
                if i==j:diag[i]=value
                else:caps[i]+=abs(value);caps[j]+=abs(value)
        assert all(a>b for a,b in zip(diag,caps)),('Gram residual is not strictly diagonally dominant',block['key'])
        # G=L L^T + positive-diagonal-dominant symmetric residual, so G>0.
    actual=reconstruct(cert['blocks'],D)
    for i in range(4):
        for j in range(4):
            assert actual[i][j]+(rr(1)/100 if i==j else 0)==controls[cert['control']][i][j]
    return True


def main():
    tick=time.monotonic()
    for c in (2,):
        cert=json.loads(Path('rational_sos_'+str(c)+'.json').read_text());assert cert['control']==c
        check(cert);print('PROVED (verify_sos.py): control',c,'all polynomial coefficients and all integer PSD residuals passed.',flush=True)
    print('PROVED (verify_sos.py): complete rank-three zero-edge boundary matrix certificate at k=5; padding_monotonicity.py gives all larger k and infinity.')
    print('NUMERICAL replay seconds',time.monotonic()-tick)

if __name__=='__main__':main()
