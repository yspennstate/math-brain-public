"""Certify rational roundings of search records, not their binary scores."""
import json,time,resource
from pathlib import Path
from fractions import Fraction
import numpy as np
import sympy as sp
from interval_core import iv,rat,full_certificate

def coords(q):
    return [q[i,i].real for i in range(3)]+[v for i,j in ((0,1),(0,2),(1,2)) for v in (q[i,j].real,q[i,j].imag)]

def main():
    start=time.monotonic();iv.dps=180
    data=json.loads(Path('data/search.json').read_text())
    records=[('best',data['best'])]+[(r['family'],r) for r in data['families']]
    records += [('NM_'+str(r['start']),r) for r in data['optimizations']]
    records += [('DE_'+str(r['epsilon']),r) for r in data['de']]
    out=dict(precision_decimal=iv.dps,denominator=10**24,records=[])
    for name,row in records:
        q=np.array(row['Q']['real'])+1j*np.array(row['Q']['imag'])
        nums=[round(float(z)*10**24) for z in coords(q)]
        den=10**24;rr=[sp.Rational(z,den) for z in nums]
        qq=sp.Matrix([[rr[0],rr[3]+sp.I*rr[4],rr[5]+sp.I*rr[6]],
                      [rr[3]-sp.I*rr[4],rr[1],rr[7]+sp.I*rr[8]],
                      [rr[5]-sp.I*rr[6],rr[7]-sp.I*rr[8],rr[2]]])
        minors={key:[sp.factor(m[:k,:k].det()) for k in range(1,4)] for key,m in [('Q',qq),('I-Q',sp.eye(3)-qq)]}
        if not all(z>0 for v in minors.values() for z in v):
            out['records'].append(dict(name=name,status='rational rounding not strict',numerators=nums));continue
        item=dict(name=name,float_theta=row['theta'],numerators=nums,
                  exact_leading_minors={k:list(map(str,v)) for k,v in minors.items()})
        try:
            item.update(full_certificate([rat(Fraction(z,den)) for z in nums]));item['status']='certified'
        except ArithmeticError as e:item.update(status='not certified',error=str(e))
        out['records'].append(item)
        print(name,item['status'],item.get('margin'),flush=True)
        out['seconds']=time.monotonic()-start
        out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
        Path('data/certificates.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
