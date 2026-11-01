"""Small deterministic check; all receipts remain in this worker folder.

The gamma formula is compared with direct quadrature in the original y
coordinate. Neither calculation is a formal proof or an independent referee.
"""
import argparse
import ctypes
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent


class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', ctypes.c_ulong), ('load', ctypes.c_ulong),
                ('total_physical', ctypes.c_ulonglong), ('available_physical', ctypes.c_ulonglong),
                ('total_pagefile', ctypes.c_ulonglong), ('available_pagefile', ctypes.c_ulonglong),
                ('total_virtual', ctypes.c_ulonglong), ('available_virtual', ctypes.c_ulonglong),
                ('available_extended_virtual', ctypes.c_ulonglong)]


def system_times():
    values = [ctypes.c_ulonglong() for _ in range(3)]
    if not ctypes.windll.kernel32.GetSystemTimes(*(ctypes.byref(v) for v in values)):
        raise OSError('GetSystemTimes failed')
    return tuple(v.value for v in values)


def resource_probe():
    status = MemoryStatus()
    status.length = ctypes.sizeof(status)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
        raise OSError('GlobalMemoryStatusEx failed')
    before = system_times()
    time.sleep(0.25)
    after = system_times()
    idle, kernel, user = [b-a for a,b in zip(before, after)]
    total = kernel + user
    busy = (total-idle)/total if total else 1.0
    governor_path=Path('~/.claude/compute/compute_state.json')
    governor={}
    if governor_path.is_file():
        data=json.loads(governor_path.read_text(encoding='utf-8-sig'))
        governor={name:data.get(name) for name in ('status','mode','cpu_pct','mem_avail_mb','commit_avail_mb','disk_free_gb')}
        governor['state_age_seconds']=time.time()-governor_path.stat().st_mtime
        governor['hung_window_count']=len(data.get('hung_windows') or [])
    governor_ok=(governor.get('state_age_seconds',float('inf'))>=0
                 and governor.get('state_age_seconds',float('inf'))<=60
                 and governor.get('status')!='distress'
                 and governor.get('hung_window_count',1)==0
                 and (governor.get('commit_avail_mb') or 0)>=16*1024
                 and (governor.get('mem_avail_mb') or 0)>=8*1024
                 and (governor.get('disk_free_gb') or 0)>=3)
    return {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
            'available_physical_bytes': status.available_physical, 'cpu_busy_fraction': busy,
            'governor_local':governor,
            'limits': {'minimum_available_physical_bytes': 8*1024**3, 'minimum_commit_headroom_mb':16*1024,
                       'maximum_governor_age_seconds':60, 'maximum_cpu_busy_fraction': .80,
                       'max_quadrature_subintervals': 8192, 'single_thread': True, 'no_gpu': True},
            'admit': governor_ok and status.available_physical >= 8*1024**3 and busy <= .80}


def direct_moments(p, intervals=8192):
    # y^p <= 60; omitted tails are exponentially tiny for the displayed p.
    upper = 60.0**(1.0/p)
    step = upper/intervals
    exponents = (0, 2, p, 2*p, 2*p-2)
    sums = [[] for _ in exponents]
    for i in range(intervals+1):
        y = i*step
        weight = 1 if i in (0, intervals) else (4 if i % 2 else 2)
        density = math.exp(-(y**p))
        for terms, exponent in zip(sums, exponents):
            terms.append(weight*density*(y**exponent))
    integrals = [math.fsum(terms)*step/3 for terms in sums]
    normalizer = integrals[0]
    return [value/normalizer for value in integrals[1:]]


def gamma_energy(p):
    a = 1.0/p
    return math.exp(2*math.log(p)-math.log1p(a)+math.lgamma(3*a)
                    +math.lgamma(2-a)-2*math.lgamma(a))


def simpson(fn, lo, hi, intervals=8192):
    step=(hi-lo)/intervals
    terms=[]
    for i in range(intervals+1):
        weight=1 if i in (0,intervals) else (4 if i%2 else 2)
        terms.append(weight*fn(lo+i*step))
    return math.fsum(terms)*step/3


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--scalar-only', action='store_true', help='No quadrature if an official gate defers it.')
    args=parser.parse_args()
    started=time.monotonic()
    gate=resource_probe()
    (ROOT/'RESOURCE_PROBE.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
    if not gate['admit']:
        receipt={'command':'python -B -X utf8 verify_obstruction.py', 'resource_probe':gate,
                 'deferred':True, 'quadrature_executed':False, 'rows':[],
                 'note':'No experiment ran because the fresh local resource probe did not admit it.'}
        (ROOT/'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
        print(json.dumps(receipt, indent=2))
        return
    rows=[]
    intervals=4096 if gate['governor_local'].get('mode')=='throttle' else 8192
    for p in (2,4,8,16,32,64,128,256,512,1024,1000000):
        dp=gamma_energy(p)
        row={'p':p, 'input_energy':1, 'conditional_gradient_energy':dp, 'D_p_over_p':dp/p,
             'conditional_mean_variance':1/(p+1), 'expected_conditional_variance':p/(p+1)}
        if gate['admit'] and not args.scalar_only and p in (2,4,8,16):
            y2,yp,y2p,y2p_minus2=direct_moments(p,intervals=intervals)
            direct=p*p*y2*y2p_minus2/(1+1/p)
            row.update(quadrature_energy=direct, relative_energy_error=abs(direct/dp-1),
                       quadrature_mean_X=1+yp, quadrature_var_X=1+y2p-yp*yp,
                       var_X_absolute_error=abs(y2p-yp*yp-1/p),
                       energy_inequality_with_C1_accepts=direct<=1,
                       mean_zero_covariance_XY='exact odd symmetry')
            assert row['relative_energy_error'] < 2e-9, row
            assert row['var_X_absolute_error'] < 2e-9, row
        rows.append(row)
    assert abs(rows[0]['conditional_gradient_energy']-2/3) < 1e-12
    assert abs(rows[-1]['D_p_over_p']-1/3) < 1e-5
    receipt={'command':'python -B -X utf8 verify_obstruction.py'+(' --scalar-only' if args.scalar_only else ''),
             'elapsed_seconds':time.monotonic()-started, 'resource_probe':gate,
             'quadrature_executed':gate['admit'] and not args.scalar_only,'quadrature_intervals':intervals,
             'verification_kind':'numerical cross-check, not a proof or independent review', 'rows':rows}
    ball_rows=[]
    for n in (2,4,8,16,32,64,128,1024):
        d=n/2
        t=d/(d+2)
        var_f=2*n*(n+2)/(n+4)
        summed_conditional_variance=(1-t)*var_f
        ratio=var_f/summed_conditional_variance
        assert abs(ratio-(n+4)/4) <= 1e-10*ratio
        ball_rows.append({'n':n, 'quadratic_block_correlation_magnitude':t,
                          'variance_f':var_f, 'summed_conditional_variance':summed_conditional_variance,
                          'necessary_conditional_comparison_factor':ratio,
                          'full_gradient_energy':4*n, 'global_Poincare_ratio':var_f/(4*n)})
    receipt['ball_rows']=ball_rows
    if not args.scalar_only:
        disk_var=simpson(lambda r:r**5/4,0,2,intervals=intervals)
        disk_energy=simpson(lambda r:2*r**3,0,2,intervals=intervals)
        disk_conditional_sum=2*simpson(lambda th:256/(45*math.pi)*math.cos(th)**6,0,math.pi/2,intervals=intervals)
        disk_ratio=disk_var/disk_conditional_sum
        assert abs(disk_ratio-1.5) < 1e-10
        assert abs(disk_energy-8) < 1e-10
        receipt['disk_independent_quadrature']={'var_f':disk_var,'full_gradient_energy':disk_energy,
             'summed_conditional_variance':disk_conditional_sum,'comparison_factor':disk_ratio,
             'method':'Direct radial and angular integrals for the radius-two uniform disk; no gamma formula used.'}
    receipt['elapsed_seconds']=time.monotonic()-started
    (ROOT/'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    print(json.dumps(receipt, indent=2))


if __name__=='__main__':
    main()
