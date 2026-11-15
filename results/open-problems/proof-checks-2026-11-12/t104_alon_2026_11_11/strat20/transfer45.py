"""Exact transfer comparisons. Coefficient matrices are checked over QQ."""
import sys,json
from pathlib import Path
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited19'/'inherited18'))
from algebra44 import block
from boundary44 import inspect
from inherited17.memory_guard import install

def construct(kind,ep,oldk,oldtrace,oldh,dd,tmax,margin=0):
    rr,*_=ring('x,y,z,a,b,c,t',QQ);t=rr.gens[-1]*tmax
    D,tr,sq,Q,B,H,Y,*_=block(rr,kind,0,ep)
    # Multiply by D^2: new mass numerator is (tr+(4-t)D)/2.
    mass=(tr+(4-t)*D)/2;oldmass=(oldtrace+4-t)/2
    def Xnum(k,mass,hn):
        return (mass-D)*(2*(k+1)*(k-2)*D-4*k*mass+2*(k+2)*hn)/(k*k)
    oldX=(oldmass-1)*(2*(oldk+1)*(oldk-2)-4*oldk*oldmass+2*(oldk+2)*(oldh-dd))/(oldk*oldk)
    const=2*(D*tr-sq)-oldX*D*D+(QQ(4,7)-QQ(4,oldk))*dd*D*D-margin*D*D
    # X is affine in h: scalar part uses 4/5-d, matrix part H/D.
    scalarX=Xnum(7,mass,(QQ(4,5)-dd)*D)
    M=[[ (const+scalarX)*Q[i][j]+QQ(18,7)*B[i][j]-Y[i][j]+(mass-D)*QQ(18,49)*H[i][j] for j in range(len(Q))] for i in range(len(Q))]
    return rr,M

def controls(rr,M):
    # Bernstein degree 2 in t/tmax, keeping all other gap monomials.
    def term(p,j):return rr.from_dict({e[:-1]+(0,):c for e,c in p.items() if e[-1]==j})
    A=[[[term(p,j) for p in row] for row in M] for j in range(3)]
    return [A[0],[[A[0][i][j]+A[1][i][j]/2 for j in range(len(M))] for i in range(len(M))],[[sum(A[a][i][j] for a in range(3)) for j in range(len(M))] for i in range(len(M))]]

def main():
    install(850_000_000);records=[]
    jobs=[('rank',ep,5,1,QQ(13,10),3) for ep in (0,1)]
    jobs += [(kind,1,5,1,QQ(13,10),2) for kind in ('star','path')]
    for kind,ep,ok,ot,oh,tm in jobs:
        for dd in (QQ.zero,QQ(3,10)):
            rr,M=construct(kind,ep,ok,ot,oh,dd,tm,QQ(1,100))
            failures=[];counts=[]
            for i,A in enumerate(controls(rr,M)):
                count,bad=inspect(A);counts.append(count);failures.extend((i,e,a) for e,a in bad)
            rec=dict(kind=kind,endpoint=ep,oldk=ok,tau5_max=tm,d5=str(dd),margin='1/100',counts=counts,failed=len(failures))
            print(rec,flush=True)
            if failures:print('first failure',failures[:1],flush=True)
            records.append(rec)
    Path('transfer45_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    assert all(r['failed']==0 for r in records)
    print('PROVED (transfer45.py): four-rank endpoints with every five-part, and four-trees with rank(A5)<=3, transfer from edge+five, with increment >=1/100 at k=7.')
if __name__=='__main__':main()
