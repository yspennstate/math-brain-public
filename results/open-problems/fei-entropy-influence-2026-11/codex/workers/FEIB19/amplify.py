"""Exact scalar AND-of-copies amplification of all coordinate orbits."""
import json,math,time,os,resource
import mpmath as mp
from large import Stable,ln2
def run():
    pm=json.load(open('pm.json'))['data']['rows'];rows=[]
    for z in pm[:10]:
        depth=z['depth']
        for w in list(range(2,41))+[50,64,100,200,1000]:
            vals=[]
            for st in z['states']:
                d=mp.mpf(57)**st['core']/mp.mpf(256)**depth
                a=Stable();a.n=z['n'];a.ld=a.lc=mp.log(d);a.TL=mp.mpf(st['F']);a.TE=mp.mpf(st['E']);a.step(w,'AND');r=a.row('');r['core']=st['core'];vals.append(r)
            r=min(vals,key=lambda x:x['F']);rows.append(dict(depth=depth,w=w,n=r['n'],F=r['F'],E=min(v['E'] for v in vals),core=r['core']))
    return rows
if __name__=='__main__':
    start=time.time();rows=run();out=dict(seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,data=rows)
    json.dump(out,open('amplify.json','w'),indent=2);print(json.dumps(sorted(rows,key=lambda r:r['F'],reverse=True)[:15],indent=2))
