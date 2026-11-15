"""Exact comparison with the proved tied edge/five theorem."""
import json
from pathlib import Path
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited20'))
from inherited20.transfer45 import controls
from algebra55 import block,FIVE
from inherited20.inherited19.inherited18.boundary44 import inspect
from inherited20.inherited19.inherited18.inherited17.memory_guard import install

def construct(kind,ep,dd,tmax,margin=QQ(1,100)):
    rr,*_=ring('a,b,c,d,t',QQ);t=rr.gens[-1]*tmax
    D,tr,sq,Q,B,H,Y,*_=block(rr,kind,ep)
    mass=(tr+(4-t)*D)/2;oldmass=(5-t)/2
    oldX=(oldmass-1)*(2*6*3-20*oldmass+14*(QQ(13,10)-dd))/25
    const=2*(D*tr-sq)-oldX*D*D-QQ(3,10)*dd*D*D-margin*D*D
    scalar=(mass-D)*(108*D-32*mass+20*(QQ(4,5)-dd)*D)/64
    M=[[(const+scalar)*Q[i][j]+QQ(5,2)*B[i][j]-Y[i][j]+(mass-D)*QQ(5,16)*H[i][j] for j in range(len(Q))]for i in range(len(Q))]
    return rr,M

def main():
    install(850_000_000);records=[]
    for kind,ep,tm in [('rank',0,3),('rank',1,3)]+[(kind,1,2)for kind in FIVE]:
        for dd in (QQ.zero,QQ(3,10)):
            rr,M=construct(kind,ep,dd,tm);counts=[];bad=[]
            for j,A in enumerate(controls(rr,M)):
                n,fail=inspect(A);counts.append(n);bad.extend((j,e)for e,a in fail)
            rec=dict(kind=kind,endpoint=ep,tau_other_max=tm,d_other=str(dd),margin='1/100',counts=counts,failed=len(bad));records.append(rec)
            print(rec,'first',bad[:1],flush=True)
    Path('transfer55_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    assert all(r['failed']==0 for r in records)
    print('PROVED (transfer55.py): rank-two endpoints against every five-part and trees against rank-at-most-three five-parts, increment >=1/100 at k=8.')
if __name__=='__main__':main()
