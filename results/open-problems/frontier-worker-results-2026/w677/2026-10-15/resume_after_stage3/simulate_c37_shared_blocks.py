"""Finite-site shared-discovery upper-block screening, one bounded cell per call.

Only numerical evidence.  No independent-activation approximation, particle cap,
path truncation, or copied discovery within a block.  No theorem about the
ordinary infinite model follows from these finite-block measurements.
"""
import argparse, json, math, random, time, hashlib
from pathlib import Path
from datetime import datetime

ROOT=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--height',type=int,required=True)
    parser.add_argument('--trials',type=int,default=2000)
    parser.add_argument('--seed',type=int,default=37715)
    parser.add_argument('--seconds',type=float,default=150)
    args=parser.parse_args()
    assert 1<=args.height<=8 and 2<=args.trials<=100000
    d=4; L=args.height; N=(d**(L+1)-1)//(d-1)
    assert N<100000
    rng=random.Random(args.seed)
    start=time.monotonic()
    output=ROOT/f'C37_MC_H{L}_S{args.seed}.json'
    if output.exists(): raise SystemExit('Output exists; inspect before choosing a new cell.')
    spine={0}; leaf=0
    for _ in range(L): leaf=4*leaf+1; spine.add(leaf)
    result=dict(at=datetime.now().astimezone().isoformat(),status='running',height=L,sites=N,
        requested_trials=args.trials,seed=args.seed,cells=[],
        arithmetic='float Monte Carlo; descriptive standard errors, not rigorous bounds',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    def save():
        result['seconds']=time.monotonic()-start
        output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for mode in ('top','bottom','root'):
        sums=[0.,0.]; sq=[0.,0.]; cross=0.
        cell=dict(mode=mode,trials=0)
        result['cells'].append(cell)
        for trial in range(args.trials):
            awake={0} if mode=='top' else set(spine)
            queue=[0,0] if mode=='top' else [leaf]
            up=down=0
            cursor=0
            while cursor<len(queue):
                v=queue[cursor]; cursor+=1
                while True:
                    # Ordinary 5-neighbour walk, except degree four at global root.
                    pick=rng.randrange(4) if mode=='root' and v==0 else rng.randrange(5)-1
                    if pick==-1:
                        if v==0: up+=1; break
                        v=(v-1)//4
                    else:
                        v=4*v+1+pick
                        if v>=N: down+=1; break
                    if v not in awake: awake.add(v); queue.append(v)
            assert up+down==len(queue)
            for i,x in enumerate((up,down)): sums[i]+=x; sq[i]+=x*x
            cross+=up*down
            n=trial+1
            if n%100==0 or n==args.trials:
                means=[s/n for s in sums]
                variances=[max(0,(sq[i]-n*means[i]**2)/(n-1)) for i in range(2)]
                cov=(cross-n*means[0]*means[1])/(n-1)
                cell.update(trials=n,means=means,variances=variances,covariance=cov,
                    standard_errors=[math.sqrt(v/n) for v in variances])
                save()
                if time.monotonic()-start>args.seconds:
                    result['status']='budget_checkpoint';save();print('Budget checkpoint',output.name,flush=True);return
        print('Completed',L,mode,'means',cell['means'],flush=True)
    top,bottom,_=result['cells']
    ut,dt=top['means'];ub,db=bottom['means']
    if min(ut,dt,ub,db)>0:
        rho=math.sqrt(dt*ub)+math.sqrt(ut*db)
        gradients=[(.5*math.sqrt(db/ut),.5*math.sqrt(ub/dt)),
                   (.5*math.sqrt(dt/ub),.5*math.sqrt(ut/db))]
        variance=0
        for cell,(g0,g1) in zip((top,bottom),gradients):
            variance+=(g0*g0*cell['variances'][0]+g1*g1*cell['variances'][1]+2*g0*g1*cell['covariance'])/cell['trials']
        result['bulk_minimum_estimate']=rho
        result['bulk_delta_standard_error']=math.sqrt(max(0,variance))
    result['status']='complete';save()
    print(json.dumps({k:result[k] for k in ('height','bulk_minimum_estimate','bulk_delta_standard_error','seconds') if k in result}),flush=True)

if __name__=='__main__': main()
