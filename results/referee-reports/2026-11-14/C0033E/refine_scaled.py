"""Additional local searches minimizing atom-log-scaled margins."""
import json,time,math,resource
from pathlib import Path
import mpmath as mp
from scipy.optimize import minimize
from optimize_collar import build
from mp_core import *

def main():
    start=time.monotonic();out={'runs':[]}
    def save():
        out['seconds']=time.monotonic()-start;out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
        p=Path('data/scaled_optimization.json');t=p.with_suffix('.tmp');t.write_text(json.dumps(out,indent=2)+'\n');t.replace(p)
    for L in (20,60,150,400):
        mp.mp.dps=100+int(10*L/math.log(10));r={'L':L,'evaluations':0,'rejected':0,'best':None,'starts':[]};out['runs'].append(r)
        bounds=[(-4*L,4*L)]*3+[(-math.pi,math.pi),(.12,1),(-.9*L,.9*L)]
        def fun(x):
            r['evaluations']+=1
            if any(v<lo or v>hi for v,(lo,hi) in zip(x,bounds)):
                r['rejected']+=1;return 20+sum(max(lo-v,v-hi,0)**2 for v,(lo,hi) in zip(x,bounds))
            q=build(x,L);ev=evaluate(q)
            if r['best'] is None or ev['scaled']<mp.mpf(r['best']['scaled']):r['best']=strings(dict(**ev,x=list(map(float,x)),coordinates=coordinates(q)),70)
            if ev['margin']<0:save();raise RuntimeError('negative margin')
            if r['evaluations']%100==0:save()
            return float(ev['scaled'])
        for mid in (0,.2*L,-.2*L):
            init=[.75*L,-3*L,0,0,1,mid]
            ans=minimize(fun,init,method='Nelder-Mead',options=dict(maxfev=500,xatol=1e-6,fatol=1e-13))
            r['starts'].append(dict(success=bool(ans.success),evaluations=int(ans.nfev),message=str(ans.message)))
        print(L,r['evaluations'],r['best']['margin'],r['best']['scaled'],flush=True);save()
    save()
if __name__=='__main__':main()
