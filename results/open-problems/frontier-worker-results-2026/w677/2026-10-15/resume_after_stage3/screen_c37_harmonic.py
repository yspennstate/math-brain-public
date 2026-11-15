"""Separate Monte Carlo implementation using site harmonic exit weights.

One bounded cell per call. All reported error bars are descriptive. No rigorous
contraction certificate is produced. Original direct-exit scripts stay frozen.
"""
import argparse, json, math, random, time, hashlib
from pathlib import Path
from datetime import datetime

root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--height',type=int,required=True)
parser.add_argument('--trials',type=int,default=10000)
parser.add_argument('--seed',type=int,required=True)
args=parser.parse_args()
L=args.height
assert 1<=L<=8 and 2<=args.trials<=100000
N=(4**(L+1)-1)//3
levels=[0]*N
for v in range(1,N): levels[v]=levels[(v-1)//4]+1
h=[(4**(L+1-j)-1)/(4**(L+2)-1) for j in range(L+1)]
spine={0}; leaf=0
for _ in range(L): leaf=4*leaf+1; spine.add(leaf)
output=root/f'C37_HARMONIC_H{L}_S{args.seed}.json'
if output.exists(): raise SystemExit('Output exists; inspect before rerunning.')
rng=random.Random(args.seed)
start=time.monotonic()
data=dict(at=datetime.now().astimezone().isoformat(),status='running',height=L,sites=N,seed=args.seed,
    requested_trials=args.trials,arithmetic='float Monte Carlo; no rigorous enclosures',cells=[],
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
def save():
    data['seconds']=time.monotonic()-start
    output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
for mode in ('top','bottom','root'):
    n=0; sx=sy=sxx=syy=sxy=0.
    cell=dict(mode=mode,trials=0);data['cells'].append(cell)
    for trial in range(args.trials):
        awake={0} if mode=='top' else set(spine)
        queue=[0,0] if mode=='top' else [leaf]
        x=2*h[0] if mode=='top' else (h[L] if mode=='bottom' else 0.)
        cursor=0
        while cursor<len(queue):
            v=queue[cursor];cursor+=1
            while True:
                choice=rng.randrange(4) if mode=='root' and v==0 else rng.randrange(5)-1
                if choice==-1:
                    if v==0: break
                    v=(v-1)//4
                else:
                    v=4*v+1+choice
                    if v>=N: break
                if v not in awake:
                    awake.add(v);queue.append(v)
                    if mode!='root': x+=h[levels[v]]
        y=len(queue)-x
        n+=1;sx+=x;sy+=y;sxx+=x*x;syy+=y*y;sxy+=x*y
        if n%100==0 or n==args.trials:
            mx,my=sx/n,sy/n
            vx=max(0.,(sxx-n*mx*mx)/(n-1));vy=max(0.,(syy-n*my*my)/(n-1))
            cv=(sxy-n*mx*my)/(n-1)
            cell.update(trials=n,means=[mx,my],variances=[vx,vy],covariance=cv,
                standard_errors=[math.sqrt(vx/n),math.sqrt(vy/n)])
            save()
            if time.monotonic()-start>150:
                data['status']='budget_checkpoint';save();raise SystemExit('Budget checkpoint saved.')
    print(L,mode,'means',cell['means'],flush=True)
top,bottom,_=data['cells']
ut,dt=top['means'];ub,db=bottom['means']
rho=math.sqrt(dt*ub)+math.sqrt(ut*db)
var=0.
for cell,(a,b) in zip((top,bottom),[(.5*math.sqrt(db/ut),.5*math.sqrt(ub/dt)),(.5*math.sqrt(dt/ub),.5*math.sqrt(ut/db))]):
    var+=(a*a*cell['variances'][0]+b*b*cell['variances'][1]+2*a*b*cell['covariance'])/cell['trials']
data.update(status='complete',bulk_minimum_estimate=rho,bulk_delta_standard_error=math.sqrt(max(0.,var)))
save()
print('rho',rho,'delta_SE',data['bulk_delta_standard_error'],flush=True)
