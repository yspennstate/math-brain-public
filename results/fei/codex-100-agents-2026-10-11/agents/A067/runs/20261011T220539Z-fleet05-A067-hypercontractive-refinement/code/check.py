"""Frozen A067 exact checks, Python standard library only."""
import argparse
import json
import time
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for base in range(0, len(a), 2*step):
            for j in range(base, base+step):
                u, v = a[j], a[j+step]
                a[j], a[j+step] = u+v, u-v
        step *= 2
    return a

def upper_degrees(a, n):
    d = [s.bit_count() if x else -1 for s,x in enumerate(a)]
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not (s & bit):
                d[s] = max(d[s], d[s | bit])
    return d

def check_table(values, n, direct=False):
    size = 1 << n
    a = fwht(values)
    d = upper_degrees(a,n)
    assertions = 0
    assert sum(x*x for x in a) == size*size
    assertions += 1
    for s in range(1,size):
        if a[s]:
            # a_s/2^n must be a multiple of 2^(1-d_s).
            assert a[s] % (1 << (n+1-d[s])) == 0
            assert abs(a[s]) >= 1 << (n+1-d[s])
            assertions += 2
    influence_num = sum(s.bit_count()*x*x for s,x in enumerate(a))
    physical_num = sum(values[x] != values[x ^ (1<<i)]
                       for x in range(size) for i in range(n))
    assert influence_num == physical_num*size
    assertions += 1
    v_num = size*size-a[0]*a[0]
    u_num = sum(x*x*(d[s]-s.bit_count()) for s,x in enumerate(a) if s and x)
    local_num = sum(2*x*x*(d[s]-1) for s,x in enumerate(a) if s and x)
    assert local_num == 2*influence_num-2*v_num+2*u_num
    assertions += 1
    if direct:
        # Independent direct character sum, no butterfly transform.
        for s in range(size):
            b = sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(values))
            assert b == a[s]
            assertions += 1
    return assertions

def exhaustive(ns, limit):
    started = time.perf_counter()
    count = assertions = 0
    histogram = {}
    complete = True
    for n in ns:
        size = 1 << n
        for table in range(1 << size):
            values = [1 if (table >> x)&1 else -1 for x in range(size)]
            assertions += check_table(values,n,direct=n<=3)
            count += 1
            if time.perf_counter()-started > limit:
                complete = False
                break
        histogram[str(n)] = (table+1)
        if not complete:
            break
    return {"complete":complete,"cases":count,"assertions":assertions,
            "per_dimension":histogram,"elapsed_seconds":time.perf_counter()-started,
            "arithmetic":"integers; no numeric logarithms"}

def families(limit):
    started = time.perf_counter()
    rows=[]
    assertions=0
    for n in range(2,13):
        size=1<<n
        p=Q(1,size)
        for kind in ('point_defect','dictator_surgery'):
            values=[1 for _ in range(size)] if kind=='point_defect' else [1 if not (x&1) else -1 for x in range(size)]
            values[0] = -1
            assertions += check_table(values,n)
            a=fwht(values)
            d=upper_degrees(a,n)
            q=[Q(x*x,size*size) for x in a]
            inf=sum(s.bit_count()*v for s,v in enumerate(q))
            u=sum(v*(d[s]-s.bit_count()) for s,v in enumerate(q) if s and v)
            if kind=='point_defect':
                assert a[0]==size-2 and all(x==-2 for x in a[1:])
                assert inf==2*n*p and u==2*n*p-4*n*p*p and u<=inf
            else:
                assert a[1]==size-2 and all(x==-2 for s,x in enumerate(a) if s!=1)
                assert inf==1+(2*n-4)*p
                assert u==n-1-(2*n-4)*p-4*n*p*p
            assertions+=3
            rows.append({"n":n,"family":kind,"I":str(inf),"U":str(u),"U_over_I":str(u/inf)})
    # All physical truth tables on each explicit tensor; every character anchor.
    tensor_rows=[]
    for n in range(2,9):
        total=n+3
        size=1<<total
        values=[]
        for x in range(size):
            z=x&7
            majority=1 if z.bit_count()<=1 else -1
            defect=-1 if (x>>3)==0 else 1
            values.append(majority*defect)
        assertions+=check_table(values,total)
        a=fwht(values)
        influence=Q(sum(s.bit_count()*v*v for s,v in enumerate(a)),size*size)
        assert influence==Q(3,2)+Q(2*n,1<<n)
        assertions+=1
        minimum=None
        for anchor in range(size):
            shifted=[a[s^anchor] for s in range(size)]
            d=upper_degrees(shifted,total)
            local=Q(sum(2*v*v*(d[s]-1) for s,v in enumerate(shifted) if s and v),size*size)
            # E_anchor has an additional nonnegative bias contribution.
            assert local>=Q(3*n,2)
            assertions+=1
            minimum=local if minimum is None else min(minimum,local)
        tensor_rows.append({"n":n,"anchors":size,"I":str(influence),"minimum_local_envelope":str(minimum),"lower_bound":str(Q(3*n,2))})
        if time.perf_counter()-started>limit:
            raise RuntimeError('frozen runtime exceeded')
    return {"complete":True,"rows":rows,"tensor_rows":tensor_rows,"assertions":assertions,
            "elapsed_seconds":time.perf_counter()-started,"arithmetic":"integer Walsh and exact Fraction"}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['pilot','n4','families'])
    args=parser.parse_args()
    if args.mode=='pilot':
        result=exhaustive([0,1,2,3],60)
    elif args.mode=='n4':
        result=exhaustive([4],60)
    else:
        result=families(60)
    out=ROOT/'out'/('check_'+args.mode+'.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','tensor_rows']},indent=2))
    if not result['complete']:
        raise SystemExit(2)

if __name__=='__main__':
    main()
