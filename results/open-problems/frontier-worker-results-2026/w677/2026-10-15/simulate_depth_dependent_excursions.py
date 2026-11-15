"""C29: ordinary retained excursions with logarithmic absolute-depth entry caps.

Numerical hierarchical sampling only. Conditional sampling errors omit inherited
population error. Every chunk checkpoints and exits; no work survives the call.
"""
import os
for thread_option in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[thread_option] = '1'
import argparse
import ctypes
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import shutil
import time
import numpy as np

BASE = Path(__file__).resolve().parent

def cap_at(level):
    """Smallest positive K with 4**K >= (level+2)**2; no logarithmic rounding."""
    power, cap = 4, 1
    while power < (level+2)**2:
        power *= 4
        cap += 1
    return cap

def resources():
    class MemoryStatus(ctypes.Structure):
        _fields_ = [('length',ctypes.c_ulong),('load',ctypes.c_ulong)] + [
            (name,ctypes.c_ulonglong) for name in
            ('total_phys','avail_phys','total_page','avail_page','total_virtual','avail_virtual','extended')]
    value = MemoryStatus()
    value.length = ctypes.sizeof(value)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(value)):
        raise OSError('GlobalMemoryStatusEx failed')
    return {'free_ram_bytes':value.avail_phys,'free_disk_bytes':shutil.disk_usage(BASE).free}

def atomic_json(path, value):
    part = Path(str(path)+'.part')
    part.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    part.replace(path)

def leaf(n,p,input_cap,rng):
    bits = rng.binomial(1,p/(1-p),size=(n,input_cap+1))
    return bits[:,:1]+np.cumsum(bits[:,1:],axis=1)

def sample_variable(n,p,input_cap,child_cap,previous,rng):
    beta, q = p/(1-p),(1-p)/3
    if previous is None:
        bits = rng.binomial(1,beta,size=(n,3,child_cap+1))
        children = bits[:,:,:1]+np.cumsum(bits[:,:,1:],axis=2)
    else:
        assert previous.shape[1] == child_cap
        children = previous[rng.integers(len(previous),size=(n,3))]
    assert np.all(np.diff(children,axis=2)>=0)
    entries = np.zeros((n,3),dtype=np.int16)
    returned = np.zeros(n,dtype=np.int64)
    answers = []
    for seed in range(input_cap):
        pending = np.full(n,2 if seed==0 else 1,dtype=np.int64)
        for _wave in range(3*child_cap+2):
            codes = np.sum((entries==child_cap)*np.array([1,2,4]),axis=1)
            old = pending
            pending = np.zeros(n,dtype=np.int64)
            for code in range(8):
                rows = np.flatnonzero((codes==code)&(old>0))
                if not len(rows):
                    continue
                if code==7:
                    returned[rows] += rng.binomial(old[rows],beta)
                    continue
                eligible = [j for j in range(3) if not code>>j&1]
                denominator = 1-(3-len(eligible))*q*beta
                ups = rng.binomial(old[rows],p/denominator)
                returned[rows] += ups
                remaining = old[rows]-ups
                for slot,child in enumerate(eligible):
                    probability = q/(denominator-p-slot*q)
                    assert -1e-12<=probability<=1+1e-12
                    down = rng.binomial(remaining,min(1,max(0,probability)))
                    remaining -= down
                    before = entries[rows,child].astype(np.int64)
                    admitted = np.minimum(child_cap-before,down)
                    after = before+admitted
                    old_value = np.where(before==0,0,children[rows,child,np.maximum(0,before-1)])
                    new_value = np.where(after==0,0,children[rows,child,np.maximum(0,after-1)])
                    increment = new_value-old_value
                    assert np.all(increment>=0)
                    pending[rows] += increment+rng.binomial(down-admitted,beta)
                    entries[rows,child] = after
            if not np.any(pending):
                break
        assert not np.any(pending),'Finite quota wave bound failed'
        answers.append(returned.copy())
    values = np.column_stack(answers)
    assert np.all(np.diff(values,axis=1)>=0)
    assert int(np.max(values))<=input_cap+1+3*int(np.max(children))
    return values

def metrics(values,p,horizon,absolute_level,rep):
    first = values[:,0]
    pgf = np.power(.5,first.astype(float))
    tails = {}
    for cutoff in (5,10,20,40,80,160):
        chance = float(np.mean(first>=cutoff))
        tails[str(cutoff)] = {'estimate':chance,'se_conditional_only':math.sqrt(chance*(1-chance)/len(first))}
    return {'status':'numerical evidence','p':str(p),'horizon':horizon,'absolute_level':absolute_level,
            'replicate':rep,'samples':len(first),'input_cap':values.shape[1],
            'mean_R1':float(np.mean(first)),'median_R1':float(np.median(first)),
            'max_Rcap':int(np.max(values)),'pgf_half_R1':float(np.mean(pgf)),
            'pgf_se_conditional_only':float(np.std(pgf,ddof=1)/math.sqrt(len(first))),
            'prob_zero':float(np.mean(first==0)),'tails':tails,
            'error_scope':'Conditional error bars exclude inherited population bias; no phase threshold or recurrence bound.'}

def seed_for(p,horizon,rep,level):
    return np.random.default_rng(np.random.SeedSequence([6772900,p.numerator,p.denominator,horizon,rep,level]))

def save_population(directory,values,level):
    target = directory/'population.npz'
    part = directory/'population.npz.part'
    with part.open('wb') as stream:
        np.savez(stream,values=values,absolute_level=np.int64(level))
    part.replace(target)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ps',default='1/4,6/25')
    parser.add_argument('--depths',default='20,32,64')
    parser.add_argument('--runs',type=int,default=3)
    parser.add_argument('--samples',type=int,default=4000)
    parser.add_argument('--seconds',type=float,default=180)
    args = parser.parse_args()
    probabilities = [Fraction(x) for x in args.ps.split(',')]
    horizons = [int(x) for x in args.depths.split(',')]
    assert all(0<=p<Fraction(1,2) for p in probabilities)
    assert all(1<=h<=128 for h in horizons)
    assert 1<=args.runs<=16 and args.samples>=1000 and 0<args.seconds<=300
    max_cap = cap_at(max(horizons))
    budget = args.samples*(1400+350*max_cap)
    assert budget<800_000_000
    guard = resources()
    if guard['free_ram_bytes']<2*2**30 or guard['free_disk_bytes']<2**30:
        print(json.dumps({'waiting_for_resources':True,**guard}))
        return
    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    base = BASE/'computations'/f'c29_log_caps_M{args.samples}_src{digest[:10]}'
    base.mkdir(exist_ok=True)
    started = time.monotonic()
    completed,steps,total_jobs = 0,0,len(probabilities)*len(horizons)*args.runs
    for p in probabilities:
        for horizon in horizons:
            for rep in range(args.runs):
                directory = base/f'p{p.numerator}_{p.denominator}_H{horizon:03d}_rep{rep:02d}'
                directory.mkdir(exist_ok=True)
                config = {'p':str(p),'horizon':horizon,'replicate':rep,'samples':args.samples,
                          'source_sha256':digest,'numpy_version':np.__version__,'budget_bytes':budget,
                          'caps':[cap_at(j) for j in range(horizon+1)],
                          'model':'ordinary retained excursions, absolute-depth logarithmic waking-entry caps',
                          'resources_before_chunk':guard}
                configuration = directory/'configuration.json'
                if not configuration.exists():
                    atomic_json(configuration,config)
                history_file = directory/'history.json'
                history = json.loads(history_file.read_text(encoding='utf-8')) if history_file.exists() else []
                if (directory/'population.npz').exists():
                    with np.load(directory/'population.npz',allow_pickle=False) as checkpoint:
                        values = checkpoint['values']
                        level = int(checkpoint['absolute_level'])
                else:
                    if time.monotonic()-started>=args.seconds:
                        print(json.dumps({'directory':str(base),'steps':steps,'completed_jobs':completed,'total_jobs':total_jobs,'checkpointed':True}))
                        return
                    level = horizon
                    values = leaf(args.samples,float(p),cap_at(level),seed_for(p,horizon,rep,level))
                    save_population(directory,values,level)
                    steps += 1
                if not history or history[-1]['absolute_level']!=level:
                    history.append(metrics(values,p,horizon,level,rep))
                    atomic_json(history_file,history)
                while level>0 and time.monotonic()-started<args.seconds:
                    if int(np.max(values))>=10**11:
                        atomic_json(directory/'size_guard.json',{'absolute_level':level,'reason':'Retain checkpoint before large counts; no completion or phase claim.'})
                        print(json.dumps({'directory':str(directory),'status':'size_guard','completed_jobs':completed}))
                        return
                    parent_level = level-1
                    values = sample_variable(args.samples,float(p),cap_at(parent_level),cap_at(level),values,
                                             seed_for(p,horizon,rep,parent_level))
                    level = parent_level
                    save_population(directory,values,level)
                    history.append(metrics(values,p,horizon,level,rep))
                    atomic_json(history_file,history)
                    steps += 1
                if level==0:
                    atomic_json(directory/'root_summary.json',history[-1])
                    completed += 1
                else:
                    print(json.dumps({'directory':str(base),'steps':steps,'completed_jobs':completed,'total_jobs':total_jobs,'checkpointed':True}))
                    return
    print(json.dumps({'directory':str(base),'steps':steps,'completed_jobs':completed,'total_jobs':total_jobs,'requested_jobs_complete':True}))

if __name__=='__main__':
    main()
