"""Parameter screen only: binary64 diagnostics are not FPP bounds."""
from pathlib import Path
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse,json,time,math,ctypes,hashlib
from datetime import datetime,timezone
from measure_height_renewal import matrices
from height_profiles import profiles,scalar_total_float,scalar_short_float
from measure_chord5 import available_memory
ROOT=Path(__file__).resolve().parents[1]
BASE={18:.080091928276,19:.077847718913,20:.075782388230,21:.073873348622}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--d',type=int,nargs='+',required=True)
    parser.add_argument('--cutoff',type=int,default=21)
    parser.add_argument('--delta',type=float,default=.000008)
    parser.add_argument('--iterations',type=int,default=100)
    args=parser.parse_args()
    assert 1<=args.cutoff<=21 and 1<=args.iterations<=100
    assert all(d in BASE for d in args.d)
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    free=available_memory()
    if free is None or free<2*1024**3:raise SystemExit('WAIT: memory admission unavailable or under 2GB.')
    import numpy as np
    graph_path=ROOT/'scripts/height_renewal_graph.json'
    graph=json.loads(graph_path.read_text(encoding='utf-8'))
    params=json.loads((ROOT/'scripts/hybrid2_certificate_parameters.json').read_text(encoding='utf-8'))
    points={row['d']:row for row in params['rows']}
    words=profiles(args.cutoff)
    suffixes={word[k:] for word,h in words for k in range(1,len(word)+1)}
    n=len(graph['states']);estimate=len(suffixes)*n*8+256000000
    assert estimate<10**9
    for d in args.d:
        free=available_memory()
        if free is None or free<2*1024**3:raise SystemExit('WAIT: less than2GB before next dimension.')
        start=time.monotonic();point=points[d]
        z=point['z_n']/point['z_d'];old_s=point['s_n']/point['s_d']
        old_ratio=math.sqrt(d)*math.log(z)/old_s
        assert BASE[d]<=old_ratio<BASE[d]+2e-12
        target=old_ratio+args.delta;s=math.sqrt(d)*math.log(z)/target;a=s+1
        ops=matrices(graph,d,a,z)
        w=np.array([(a/(a+state[6]))**(state[7]+1) for state in graph['states']])
        ids=np.where([state[1][-1][1]==1 for state in graph['states']])[0]
        total=scalar_total_float(d,a,z);short=scalar_short_float(words,d,a,z);tail=total-short
        assert math.isfinite(tail) and tail>0
        def apply(v):
            full=np.zeros(n);full[ids]=v;cache={():full}
            def value(suffix):
                if suffix not in cache:cache[suffix]=ops[(0,suffix[0])]@value(suffix[1:])
                return cache[suffix]
            acc=np.zeros(n)
            for word,height in words:acc+=value(word[1:])
            result=(ops[(1,1)]@acc)[ids]
            result+=tail*float(np.max(v/w[ids]))*w[ids]
            assert np.isfinite(result).all() and (result>0).all()
            return result
        v=w[ids].copy()
        for iteration in range(args.iterations):
            new=(v+apply(v))*.5;new/=np.max(new/w[ids])
            diff=float(np.max(np.abs(new-v)));v=new
            if diff<2e-12 or time.monotonic()-start>150:break
        ratios=apply(v)/v
        result=dict(at=datetime.now(timezone.utc).isoformat(),kind='numerical evidence',target='2',d=d,
                    cutoff=args.cutoff,s=s,z=z,baseline_floor=BASE[d],baseline_ratio_float=old_ratio,
                    candidate_ratio_float=target,delta_from_baseline_ratio=args.delta,
                    rho_lower_float=float(ratios.min()),rho_upper_float=float(ratios.max()),
                    scalar_total_float=total,scalar_tail_float=tail,states=n,boundary_ids=ids.tolist(),
                    vector=v.tolist(),profiles=len(words),suffixes=len(suffixes),iterations=iteration+1,
                    available_physical_bytes=free,estimated_peak_bytes=estimate,cores=1,priority='below normal',
                    elapsed_seconds=time.monotonic()-start,
                    graph_sha256=hashlib.sha256(graph_path.read_bytes()).hexdigest(),
                    scope='Floating screen of encoded operator; neither outward-rounded certificate nor FPP theorem. Scalar closed form is used only as a numerical diagnostic.')
        dest=ROOT/f'logs/renewal_dimension_screen_d{d}_K{args.cutoff}.json'
        dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(f"d={d} target={target:.12f} s={s:.9f} z={z:.9f} rho=[{ratios.min():.12f},{ratios.max():.12f}] seconds={result['elapsed_seconds']:.1f} NUMERICAL_ONLY",flush=True)
if __name__=='__main__':main()
