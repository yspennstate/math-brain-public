"""NUMERICAL timing only; discovery prototype benchmark."""
import json,time
from fractions import Fraction as F
from exact_bernstein import data,normal,controls,degree,bernstein_min

if __name__=='__main__':
    t=time.monotonic();p,gs=data();print('construct',time.monotonic()-t,flush=True)
    box=[tuple(map(F,x)) for x in json.load(open('STRAT11/remaining_open_boxes.json'))['boxes'][0]['box']]
    t=time.monotonic();tr,d=normal(p,box);print('normal',time.monotonic()-t,len(tr),flush=True)
    t=time.monotonic();a,den=controls({m:float(c/d) for m,c in tr.items()},degree(p),False);print('float tensor',time.monotonic()-t,a.min(),flush=True)
    t=time.monotonic();a,den=controls(tr,degree(p));print('exact tensor',time.monotonic()-t,'positive',a.min()>0,flush=True)
