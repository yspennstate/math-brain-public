"""Exact integer raw moments then Decimal centering independently check MC summaries."""
from common import log
import csv,json,decimal
from decimal import Decimal as D
decimal.getcontext().prec=80
summary=json.load(open('mc_summary.json'));results=[]
for filename in sorted(set(row['file'] for row in summary)):
    sums=[[0]*4 for k in range(3)];R=0
    with open(filename) as f:
        for row in csv.DictReader(f):
            R+=1
            for k,name in enumerate(('S','C','QC')):
                x=int(row[name]);power=1
                for r in range(4):power*=x;sums[k][r]+=power
    for k,name in enumerate(('S','C','QC')):
        raw=[D(v)/R for v in sums[k]];mu=raw[0];v=raw[1]-mu**2;c3=raw[2]-3*mu*raw[1]+2*mu**3;c4=raw[3]-4*mu*raw[2]+6*mu**2*raw[1]-3*mu**4
        vals=[mu,v,c3/(v*v.sqrt()),c4/v**2]
        ref=next(r for r in summary if r['file']==filename and r['index']==name)
        keys=('mean','variance','skewness','kurtosis');err=max(abs(float(val)-ref[key])/max(1,abs(float(val))) for key,val in zip(keys,vals))
        assert err<1e-11,(filename,name,err)
        results.append({'file':filename,'index':name,'max_relative_disagreement':err})
with open('mc_verification.json','w') as f:json.dump(results,f,indent=2)
log('All Monte Carlo summaries independently checked by exact integer raw sums and Decimal-80 centering: worst relative disagreement '+str(max(r['max_relative_disagreement'] for r in results)))
