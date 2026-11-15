"""Check Nyström K entries via the independent Bessel arc formulas (136,138)."""
import json, math
from measure_operator import ROOT, matrix, J1
import numpy as np
from scipy.special import ive, i0e

rows=[]
for rho in (.4,.6,.8,.95):
    A,_,_,x,wx,jt=matrix(rho,256,20,192,False)
    idx=[int(np.argmin(abs(x-t))) for t in (.1,.5,1,2)]
    for i,j in zip(idx,idx[::-1]):
        xx,yy=float(x[i]),float(x[j])
        d=1-rho*rho
        a=2*rho*xx*yy/d
        m=np.arange(1,int(math.ceil(10*math.sqrt(max(a,1))+40))+1,dtype=float)
        ratio=ive(m,a)/i0e(a)
        b=1/3
        sb=np.sin(math.pi*b*m)
        k=b*b+float(np.sum(2*ratio*sb*sb/(math.pi*m)**2))
        P=b+float(np.sum(ratio*np.sin(2*math.pi*b*m)/(math.pi*m)))
        tau=4*P-3*k
        theta=J1/2*a*math.exp(-2*a)/float(i0e(a))
        R0=math.exp(-rho*rho/d*(xx*xx+yy*yy)+a)*float(i0e(a))/d
        bessel=R0*(tau-4*theta)
        nystrom=float(A[i,j])*math.sqrt(float(jt[i]*jt[j]))/(2*math.sqrt(float(wx[i]*wx[j]))) * math.exp((xx*xx+yy*yy)/2)
        row={'rho':rho,'x':xx,'y':yy,'a':a,'nystrom_K':nystrom,
             'Bessel_arc_K':bessel,'absolute_difference':abs(nystrom-bessel),
             'relative_difference':abs(nystrom-bessel)/abs(bessel)}
        rows.append(row)
        if not math.isclose(nystrom,bessel,rel_tol=2e-11,abs_tol=2e-12):
            raise AssertionError(row)
(ROOT/'logs/independent_kernel_controls.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('PASS independent Bessel K control:',len(rows),'cases; maximum relative difference',max(r['relative_difference'] for r in rows))
