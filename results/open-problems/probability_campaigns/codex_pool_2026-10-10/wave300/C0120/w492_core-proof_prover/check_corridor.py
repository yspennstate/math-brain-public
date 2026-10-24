"""Bounded CPU-only consistency checks; numeric integration is not a proof."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import shutil
import time

ROOT = Path(__file__).resolve().parent

def phi(x: float) -> float:
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)

def cdf(x: float) -> float:
    return math.erfc(-x/math.sqrt(2))/2

def moment_integrals(m: int, panels: int, deadline: float) -> tuple[float,float,float]:
    lo, hi = -8.0, math.sqrt(2*math.log(m))+8.0
    step = (hi-lo)/panels
    moments = [0.0,0.0,0.0]
    for i in range(panels+1):
        if i % 1024 == 0 and time.monotonic()>deadline:
            raise RuntimeError('fresh compute gate wall budget exceeded')
        x=lo+i*step
        p=cdf(x)
        density=0.0 if p==0 else m*phi(x)*math.exp((m-1)*math.log(p))
        weight=1 if i in (0,panels) else 4 if i%2 else 2
        weighted=weight*density
        moments[0]+=weighted
        moments[1]+=weighted*x
        moments[2]+=weighted*x*x
    mass,mean,second=(value*step/3 for value in moments)
    return mass,mean,second-mean*mean

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--panels',type=int,default=8192)
    p.add_argument('--seconds',type=float,default=30)
    args=p.parse_args()
    if args.panels<256 or args.panels>16384 or args.panels%2:
        p.error('panels must be even and in [256,16384]')
    if not 0<args.seconds<=30:
        p.error('seconds must be in (0,30]')
    start=time.monotonic()
    free=shutil.disk_usage(ROOT).free
    gate={'cpu_only':True,'concurrency':1,'gpu':False,'training':False,
          'wall_budget_seconds':args.seconds,'max_panels':16384,
          'max_grid_points':7*(args.panels+args.panels//2+2),'free_disk_bytes':free,
          'output_budget_bytes':30000,'purpose':'one-dimensional L4 consistency checks'}
    if free<1048576:
        raise RuntimeError('fresh compute gate: less than 1 MiB disk headroom')
    (ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2),encoding='utf-8')
    c=(1-math.exp(-math.exp(-1.5)*math.log(2)/10))/4
    rows=[]
    for m in (8,16,32,64,128,256,1024):
        mass,mean,var=moment_integrals(m,args.panels,start+args.seconds)
        mass2,mean2,var2=moment_integrals(m,args.panels//2,start+args.seconds)
        row={'m':m,'mass':mass,'mean':mean,'variance_max':var,
             'variance_half_panels':var2,'refinement_difference':abs(var-var2),
             'rigorous_lower_formula':c/math.log(2*m),
             'rigorous_upper_formula':2/math.log(m),
             'corridor_n_equals_m_variance':1+(m-1)*var,
             'poincare_bound_n':m,'variance_times_log_m':var*math.log(m),
             'status':'numerical consistency only'}
        assert abs(mass-1)<1e-7
        assert c/math.log(2*m)<var<2/math.log(m)
        assert abs(var-var2)<1e-6
        rows.append(row)
        print(json.dumps(row),flush=True)
        (ROOT/'corridor_checks.jsonl').open('a',encoding='utf-8').write(json.dumps(row)+'\n')
    receipt={'command':'python -X utf8 check_corridor.py --panels 8192 --seconds 30',
             'rows':rows,'checks_passed':len(rows)*3,
             'elapsed_seconds':time.monotonic()-start,'lower_constant':c,
             'warning':'No rigorous quadrature error certificate; no open-target data or exponent claim.'}
    (ROOT/'CHECK_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    print(json.dumps({'checks_passed':receipt['checks_passed'],'elapsed_seconds':receipt['elapsed_seconds']}))

if __name__=='__main__':
    main()
