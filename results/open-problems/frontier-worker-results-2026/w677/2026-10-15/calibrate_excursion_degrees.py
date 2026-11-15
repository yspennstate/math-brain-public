"""Critical-degree calibration for C29; known full phases, no new theorem.

d=2 is recurrent and d=5 transient by HJJ. A lower family's d=2 phase need
not match the full model. Finite-height growth at d=5 remains possible.
"""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,hashlib,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from simulate_depth_dependent_excursions import leaf,resources,atomic_json,metrics,sample_variable,save_population
BASE=Path(__file__).resolve().parent

def budget_at(level,degree):
    power,cap=degree+1,1
    while power<(level+2)**2:
        power*=degree+1
        cap+=1
    return cap

def sample_degree(n,p,incap,outcap,previous,rng,degree):
    beta,q=p/(1-p),(1-p)/degree
    children=previous[rng.integers(len(previous),size=(n,degree))]
    assert children.shape[2]==outcap
    entries=np.zeros((n,degree),dtype=np.int16)
    returned=np.zeros(n,dtype=np.int64)
    answers=[]
    for seed in range(incap):
        pending=np.full(n,2 if seed==0 else 1,dtype=np.int64)
        for _wave in range(degree*outcap+2):
            codes=np.sum((entries==outcap)*(1<<np.arange(degree)),axis=1)
            old=pending
            pending=np.zeros(n,dtype=np.int64)
            for code in range(1<<degree):
                rows=np.flatnonzero((codes==code)&(old>0))
                if not len(rows):
                    continue
                if code==(1<<degree)-1:
                    returned[rows]+=rng.binomial(old[rows],beta)
                    continue
                eligible=[j for j in range(degree) if not code>>j&1]
                denominator=1-(degree-len(eligible))*q*beta
                ups=rng.binomial(old[rows],p/denominator)
                returned[rows]+=ups
                remaining=old[rows]-ups
                for slot,child in enumerate(eligible):
                    chance=q/(denominator-p-slot*q)
                    assert -1e-12<=chance<=1+1e-12
                    down=rng.binomial(remaining,min(1,max(0,chance)))
                    remaining-=down
                    before=entries[rows,child].astype(np.int64)
                    admitted=np.minimum(outcap-before,down)
                    after=before+admitted
                    a=np.where(before==0,0,children[rows,child,np.maximum(0,before-1)])
                    b=np.where(after==0,0,children[rows,child,np.maximum(0,after-1)])
                    pending[rows]+=b-a+rng.binomial(down-admitted,beta)
                    entries[rows,child]=after
            if not np.any(pending):
                break
        assert not np.any(pending)
        answers.append(returned.copy())
    values=np.column_stack(answers)
    assert np.all(np.diff(values,axis=1)>=0)
    return values

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--degrees',default='2,5')
    parser.add_argument('--depths',default='20,64')
    parser.add_argument('--runs',type=int,default=3)
    parser.add_argument('--samples',type=int,default=2000)
    parser.add_argument('--seconds',type=float,default=180)
    args=parser.parse_args()
    degrees=[int(x) for x in args.degrees.split(',')]
    horizons=[int(x) for x in args.depths.split(',')]
    assert all(d in (2,3,5) for d in degrees) and all(1<=h<=128 for h in horizons)
    assert args.samples>=1000 and 1<=args.runs<=6 and 0<args.seconds<=300
    memory=args.samples*(2000+max(degrees)*max(budget_at(max(horizons),d) for d in degrees)*250)
    assert memory<800000000
    guard=resources()
    if guard['free_ram_bytes']<2*2**30:
        print(json.dumps({'waiting_for_memory':True,**guard}))
        return
    # Real degree3 prefix compatibility with the production C29 operator.
    pool=np.sort(np.random.default_rng(3150).integers(0,5,size=(500,3)),axis=1)
    a=sample_degree(1000,.25,2,3,pool,np.random.default_rng(3151),3)
    b=sample_variable(1000,.25,2,3,pool,np.random.default_rng(3151))
    assert np.array_equal(a,b)
    digest=hashlib.sha256(Path(__file__).read_bytes()+(BASE/'simulate_depth_dependent_excursions.py').read_bytes()).hexdigest()
    base=BASE/'computations'/f'c29_degree_calibration_M{args.samples}_src{digest[:10]}'
    base.mkdir(exist_ok=True)
    atomic_json(base/'calibration_protocol.json',{'source_sha256':digest,'degrees':degrees,'horizons':horizons,
        'samples':args.samples,'replicates':args.runs,'degree3_rng_prefix':'bit-identical',
        'memory_budget_bytes':memory,'resources':guard,'known_full_phases':{'2':'recurrent','5':'transient'},
        'primary_source':'HJJ arXiv:1404.6238 Theorem1',
        'scope':'Numerical calibration only; no finite-height classifier is expected to certify the phase, and a lower model need not inherit d2 recurrence.'})
    start=time.monotonic()
    steps,done=0,0
    for degree in degrees:
        p=Fraction(1,degree+1)
        for horizon in horizons:
            for rep in range(args.runs):
                directory=base/f'd{degree}_H{horizon:03d}_rep{rep:02d}'
                directory.mkdir(exist_ok=True)
                if (directory/'population.npz').exists():
                    with np.load(directory/'population.npz',allow_pickle=False) as saved:
                        values=saved['values']
                        level=int(saved['absolute_level'])
                else:
                    if time.monotonic()-start>=args.seconds:
                        print(json.dumps({'directory':str(base),'steps':steps,'completed':done,'checkpointed':True}))
                        return
                    level=horizon
                    rng=np.random.default_rng(np.random.SeedSequence([6773100,degree,horizon,rep,level]))
                    values=leaf(args.samples,float(p),budget_at(level,degree),rng)
                    save_population(directory,values,level)
                    steps+=1
                while level>0 and time.monotonic()-start<args.seconds:
                    assert int(np.max(values))<10**11,'Count guard; retain previous checkpoint'
                    rng=np.random.default_rng(np.random.SeedSequence([6773100,degree,horizon,rep,level-1]))
                    values=sample_degree(args.samples,float(p),budget_at(level-1,degree),budget_at(level,degree),values,rng,degree)
                    level-=1
                    target=directory/'population.npz'
                    part=directory/'population.npz.part'
                    with part.open('wb') as stream:
                        np.savez(stream,values=values,absolute_level=np.int64(level))
                    part.replace(target)
                    steps+=1
                if level==0:
                    row=metrics(values,p,horizon,0,rep)
                    row.update({'degree':degree,'normalized_mean':row['mean_R1']/horizon,
                                'all_active_mean_upper_bound':(horizon+2)/degree,
                                'known_full_phase':'recurrent' if degree==2 else 'transient' if degree==5 else 'open'})
                    atomic_json(directory/'root_summary.json',row)
                    done+=1
                else:
                    print(json.dumps({'directory':str(base),'steps':steps,'completed':done,'checkpointed':True}))
                    return
    print(json.dumps({'directory':str(base),'steps':steps,'completed':done,'requested_jobs_complete':True}))

if __name__=='__main__':
    main()
