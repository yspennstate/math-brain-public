"""Exact finite-law checks of algebra used in the stronger local argument."""
from fractions import Fraction as F
from itertools import permutations,product
import json,pathlib
def orbit(v):
    o=sorted(set(permutations(v)));return [(p,F(1,len(o))) for p in o]
def mix(parts):return [(p,w*mass) for w,law in parts for p,mass in law]
def moments(law):
    return tuple(sum(w*(sum(v*v for v in a) if k==2 else sum(v*v for v in a)**2 if k==4 else sum(v**3 for v in a)) for a,w in law) for k in [2,4,3])
def main():
    laws=[orbit((F(2,5),F(-1,5),F(-1,5))),orbit((F(-1),F(1,2),F(1,2))),orbit((F(3,4),F(1,4),F(-1)))]
    laws.append(mix([(F(2,3),laws[0]),(F(1,3),laws[1])]))
    count=0
    for left,right in product(laws,laws):
        m,V,T=moments(left);n,W,H=moments(right);lc=nc2=0
        for (a,wa),(b,wb) in product(left,right):
            A=sum(v*v for v in a);B=sum(v*v for v in b);c=sum(a[i]*b[i] for i in range(3));U=sum(a[i]**2*b[i]**2 for i in range(3))
            assert U-c*c/3==A*B/6
            L=sum(a[i]**2*b[i]+a[i]*b[i]**2 for i in range(3));N=A+B+2*c+2*L+A*B/6
            vec=[a[i]+b[i]+a[i]*b[i]-c/3 for i in range(3)];assert N==sum(v*v for v in vec)
            lc+=wa*wb*L*c;nc2+=wa*wb*N*c*c
        assert lc==(n*T+m*H)/2
        assert nc2==(n*V+m*W)/2+3*T*H+(V*H+T*W)/2+V*W/12
        count+=1
    report={'status':'PASS','pairs_of_independent_symmetric_laws':count,'arithmetic':'exact Fractions','scope':'direct componentwise checks of projected-product identity, N norm, E Lc and E Nc^2; general proof uses third/fourth tensor tables'}
    pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report),flush=True)
if __name__=='__main__':main()
