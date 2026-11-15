"""Direct finite-n sums checking the asymptotic local-cycle calculation."""
import json
from pathlib import Path

rows=[]
for d in [2,3,4,6,9]:
    A=(2*d*d-1)/(2*(d-1)**2)
    b=1/d+A/d**2
    C1=(2*d-1)/(2*d*(d-1)**2)
    C2=(2*d-1)*(2*d*d-2*d+1)/(2*d*d*(d-1)**5)
    for n in [20,40,80,160,320,640]:
        p=1/(d*n)+b/n**2
        term=d*(n-1)*(n-2)*p**3/2
        total=2*term
        for k in range(4,n+1):
            term *= (n-k+1)*p
            total += (k-1)*term
        rows.append({'d':d,'n':n,'p':p,'weighted_cycle_mean':total,
                     'C1':C1,'C2':C2,
                     'scaled_remainder':n**3*(total-C1/n-C2/n**2)})
root=Path(__file__).resolve().parents[1]
(root/'data'/'cycle_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
for d in [2,3,4,6,9]:
    group=[a for a in rows if a['d']==d]
    print(d,[(a['n'],round(a['scaled_remainder'],5)) for a in group])
