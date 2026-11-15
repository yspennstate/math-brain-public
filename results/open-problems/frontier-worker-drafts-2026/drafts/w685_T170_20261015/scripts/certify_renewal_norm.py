"""Independent polynomial-integral check of the scalar boundary norm."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
from functools import lru_cache
from datetime import datetime, timezone
import json, hashlib, time, ctypes

ROOT=Path(__file__).resolve().parents[1]

def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    start=time.monotonic()
    graph_path=ROOT/'scripts/height_renewal_graph.json'
    graph=json.loads(graph_path.read_text(encoding='utf-8'))
    point=json.loads((ROOT/'logs/height_bridge_tail_certificate.json').read_text(encoding='utf-8'))
    a=Q(int(point['s']['n']),int(point['s']['d']))+1
    d=21
    states=graph['states']
    w=[(a/(a+state[6]))**(state[7]+1) for state in states]

    @lru_cache(None)
    def block(c0,c1,E,O,I,p,q):
        # Expand both Gamma(2) survival polynomials independently of
        # the production code's two-by-two matrix multiplication.
        x,y=a+c0+I+E,a+c1+E+O
        val=Q(0)
        for even in ((-1,0,1) if E else (-1,)):
            for odd in ((-1,1,2) if O else (-1,)):
                if int(odd==2)!=q:
                    continue
                e0=p+int(even==0)
                e1=int(even==1)+int(odd==1)
                val+=Q(factorial(e0)*factorial(e1),1)/(x**(e0+1)*y**(e1+1))
        return a*a**(p-q)*val

    checks=0
    largest=Q(0)
    for i,both in enumerate(graph['rows']):
        for mark in (0,1):
            for sign in (-1,1):
                total=Q(0)
                for j,sgn,r,final,c0,c1,E,O,I,p,q in both[mark]:
                    if sgn!=sign:
                        continue
                    assert I==states[i][6] and p==states[i][7]
                    assert states[j][6]==(O if final else I)
                    factor=block(c0,c1,E,O,I,p,q) if final else 1/a
                    total+=(1 if r==0 else d-r)*factor*w[j]
                ratio=total/((Q(d,1)/a)*w[i])
                largest=max(largest,ratio)
                assert ratio<=1,(i,mark,sign,ratio)
                checks+=1
    out=dict(at=datetime.now(timezone.utc).isoformat(), d=d, states=len(states), checks=checks,
             graph_sha256=hashlib.sha256(graph_path.read_bytes()).hexdigest(),
             point_sha256=hashlib.sha256((ROOT/'logs/height_bridge_tail_certificate.json').read_bytes()).hexdigest(),
             exact_largest_ratio={'n':str(largest.numerator),'d':str(largest.denominator)},
             block_integrals=block.cache_info().currsize,
             method='positive polynomial expansion, factorial integrals, and rational sign-row norm inequalities',
             seconds=time.monotonic()-start,
             scope='finite encoded operator norm at the saved rational point only; graph semantics and full FPP argument need review')
    (ROOT/'logs/height_renewal_norm_certificate.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS exact renewal norm',checks,'rows; largest ratio',float(largest),'seconds',out['seconds'],flush=True)

if __name__=='__main__':
    main()
