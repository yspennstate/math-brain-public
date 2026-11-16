"""Exact coefficient-matrix proof that k=6 is the hardest isolate endpoint."""
import json
from pathlib import Path
from algebra44 import variables,pair
from boundary44 import inspect
from inherited17.memory_guard import install

JOBS=[('star','star',1,1),('star','path',1,1),('path','path',1,1),
      ('star','rank',1,0),('star','rank',1,1),('path','rank',1,0),('path','rank',1,1),
      ('rank','rank',0,0),('rank','rank',0,1),('rank','rank',1,1)]

def main():
    install(850_000_000);rr,*_=variables();records=[]
    for left,right,i,j in JOBS:
        M,*_=pair(rr,left,right,i,j)
        def coeff(p,hp):return rr.from_dict({e[:-1]+(0,):c for e,c in p.items()if e[-1]==hp})
        A=[[[coeff(p,hp)for p in row]for row in M]for hp in (0,1,2)]
        # M(k-6)/k^2=A2+(A1-12A2)r+(A0-6A1+36A2)r^2.
        # Its derivative is affine in r=1/k. At r=0,1/6 its negatives
        # are respectively 12A2-A1 and A1-A0/3. Denominators are positive.
        for ep in (0,1):
            B=[[12*A[2][a][b]-A[1][a][b]if ep==0 else A[1][a][b]-A[0][a][b]/3 for b in range(len(M))]for a in range(len(M))]
            count,bad=inspect(B);assert not bad
            records.append(dict(left=left,right=right,endpoints=[i,j],inverse_k_endpoint=ep,matrices=count,failed=0))
    Path('padding44_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (padding44.py): every connected endpoint pair is minimized at k=6, including k=infinity.')

if __name__=='__main__':main()
