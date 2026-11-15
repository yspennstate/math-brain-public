"""Independent first Euler-error equation in the original nonlinear profile.

OMP_NUM_THREADS=1 nice -n 15 python3 recheck.py > recheck_output.txt 2>&1
Earlier modules are imported read-only; none of their main functions runs.
"""
import importlib.util
import json
import os
from pathlib import Path
import resource
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path('~')


def load(relative, name):
    spec = importlib.util.spec_from_file_location(name, ROOT/relative)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


r5 = load('codex_op_1114r5/briefs/T245/verify.py', 'r5_readonly')
raw, q = r5.old, r5.q
add, sc, err = q.add, q.sc, q.error


def main():
    start = time.monotonic()
    assert Path.cwd() == Path(__file__).resolve().parent
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    grid, dt, final = int(os.environ.get('T245_GRID', '64')), .002, .4
    size = 4*(grid+1)+1

    def physical(state):
        cs = [state[4*j:4*j+4] for j in range(grid+1)]
        st = raw.profile_state(cs, 1., 1., state[-1], q.TWO)
        gg = [sc(q.outer(v[:2], q.mv(u, st['g'])), -1.)
              for u, v in zip(st['us'], st['vs'])]
        return tuple(x for mat in gg for x in mat)+(-st['h'],)

    def derivative(state, direction):
        eps = 2e-5/max(1., max(abs(x) for x in direction))
        plus = physical(add(state, sc(direction, eps)))
        minus = physical(add(state, sc(direction, -eps)))
        return sc(add(plus, sc(minus, -1.)), 1/(2*eps))

    def coupled(state):
        path, tangent = state[:size], state[size:]
        flow = physical(path)
        # This does not use J, its transport, the Gram BVP, or endpoint forcing.
        zdot = add(derivative(path, tangent), sc(derivative(path, flow), -.5))
        return (*flow, *zdot)

    state = (0.,)*(2*size)
    for _ in range(round(final/dt)):
        state = q.rk4(state, dt, coupled)
    path, tangent = state[:size], state[size:]

    def observations(y):
        cs = [y[4*j:4*j+4] for j in range(grid+1)]
        st = raw.profile_state(cs, 1., 1., y[-1], q.TWO)
        return (*st['Q'], y[-1], *st['M'], st['B'])

    eps = 2e-5
    measured = sc(add(observations(add(path, sc(tangent, eps))),
                      sc(observations(add(path, sc(tangent, -eps))), -1)), 1/(2*eps))
    ref = r5.correction_run(1., 1., q.TWO, final=final, grid=grid, dt=dt)
    predicted = (*ref['p'], ref['beta'], *ref['m'], ref['bcor'])
    difference = err(measured, predicted)
    path_difference = err(observations(path), (*ref['P'], ref['b'], *ref['M'], ref['B']))
    print('Grid', grid, 'sensitivity error', difference, 'path error', path_difference, flush=True)
    assert difference < 2e-7
    assert path_difference < 2e-6
    exact = r5.exact_prior_recheck()
    result = dict(independent_original_profile_sensitivity=list(measured),
                  endpoint_memory_prediction=list(predicted),
                  maximum_sensitivity_error=difference,
                  maximum_flow_observation_error=path_difference,
                  exact_benchmark=exact,
                  seconds=time.monotonic()-start,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  priority=os.getpriority(os.PRIO_PROCESS, 0))
    assert result['seconds'] < 1200 and result['peak_rss_bytes'] < 1_000_000_000
    Path('recheck_data.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    print('Independent recheck passed.')


if __name__ == '__main__':
    main()
