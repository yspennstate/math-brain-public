"""Finite-depth ordinary-excursion candidates. Numerical evidence only.

One resident, joint persistent responses to K incoming seeds, K waking-producing
entries per child. Later entries retain return excursions but suppress waking.
Conditional pool errors do not control inherited population bias. One CPU.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import ctypes
import hashlib
import json
import math
import shutil
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent


def resources():
    class Memory(ctypes.Structure):
        _fields_ = [('length', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [
            (name, ctypes.c_ulonglong) for name in
            ('total', 'available', 'page', 'available_page', 'virtual',
             'available_virtual', 'extended')]
    memory = Memory()
    memory.length = ctypes.sizeof(memory)
    assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory))
    return {'free_ram_bytes': int(memory.available),
            'free_disk_bytes': shutil.disk_usage(ROOT).free}


def atomic_json(path, value):
    part = path.with_suffix('.json.part')
    part.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    part.replace(path)


def sample_joint(n, p, cap, previous, rng):
    """Return joint R(1),...,R(cap), conditional on the supplied child pool."""
    beta = p / (1-p)
    q = (1-p) / 3
    if previous is None:
        # A leaf's resident contributes once; every new incoming frog contributes
        # an independent first-parent hit. Descendant waking is suppressed.
        leaf = rng.binomial(1, beta, size=(n, 3, cap+1))
        children = leaf[:, :, :1] + np.cumsum(leaf[:, :, 1:], axis=2)
    else:
        children = previous[rng.integers(len(previous), size=(n, 3))]
    assert np.all(np.diff(children, axis=2) >= 0)
    entries = np.zeros((n, 3), dtype=np.int16)
    returned = np.zeros(n, dtype=np.int64)
    answers = []
    for seed in range(cap):
        pending = np.full(n, 2 if seed == 0 else 1, dtype=np.int64)
        for _wave in range(3*cap+2):
            codes = np.sum((entries == cap) * np.array([1, 2, 4]), axis=1)
            old = pending
            pending = np.zeros(n, dtype=np.int64)
            for code in range(8):
                rows = np.flatnonzero((codes == code) & (old > 0))
                if not len(rows):
                    continue
                if code == 7:
                    returned[rows] += rng.binomial(old[rows], beta)
                    continue
                eligible = [i for i in range(3) if not code >> i & 1]
                denominator = 1 - (3-len(eligible))*q*beta
                ups = rng.binomial(old[rows], p/denominator)
                returned[rows] += ups
                remaining = old[rows] - ups
                for slot, child in enumerate(eligible):
                    probability = q / (denominator-p-slot*q)
                    assert -1e-12 <= probability <= 1+1e-12
                    down = rng.binomial(remaining, min(1, max(0, probability)))
                    remaining -= down
                    before = entries[rows, child].astype(np.int64)
                    admitted = np.minimum(cap-before, down)
                    after = before + admitted
                    old_value = np.where(before == 0, 0,
                        children[rows, child, np.maximum(0, before-1)])
                    new_value = np.where(after == 0, 0,
                        children[rows, child, np.maximum(0, after-1)])
                    increment = new_value-old_value
                    assert np.all(increment >= 0)
                    pending[rows] += increment + rng.binomial(down-admitted, beta)
                    entries[rows, child] = after
            if not np.any(pending):
                break
        assert not np.any(pending), 'Finite quota consumption bound failed'
        answers.append(returned.copy())
    values = np.column_stack(answers)
    assert np.all(np.diff(values, axis=1) >= 0)
    return values


def metrics(values, p, cap, height):
    first = values[:, 0]
    pgf = np.power(.5, first.astype(float))
    return {'status': 'numerical evidence', 'p': str(p), 'cap': cap,
            'height': height, 'samples': len(values),
            'mean_R1': float(np.mean(first)), 'maximum_Rcap': int(np.max(values)),
            'pgf_half_R1': float(np.mean(pgf)),
            'se_conditional_only': float(np.std(pgf)/math.sqrt(len(values))),
            'prob_zero_R1': float(np.mean(first == 0)),
            'scope': 'Empirical child law. Conditional errors omit inherited '
                     'population bias; no critical drift or recurrence bound.'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--p', default='1/4')
    ap.add_argument('--cap', type=int, default=2)
    ap.add_argument('--samples', type=int, default=20000)
    ap.add_argument('--depth', type=int, default=32)
    ap.add_argument('--seed', type=int, default=6772500)
    ap.add_argument('--seconds', type=float, default=22)
    args = ap.parse_args()
    p = Fraction(args.p)
    assert 0 <= p < Fraction(1, 2) and 1 <= args.cap <= 16
    assert 1 <= args.depth <= 128 and 1000 <= args.samples
    required = args.samples*(1200+args.cap*200)
    assert required < 800000000
    guard = resources()
    if guard['free_ram_bytes'] < 2*2**30:
        print(json.dumps({'waiting_for_memory': True, **guard}))
        return
    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    directory = ROOT / ('computations/c25_cap%d_p%d_%d_M%d_seed%d_src%s' % (
        args.cap, p.numerator, p.denominator, args.samples, args.seed, digest[:10]))
    directory.mkdir(exist_ok=True)
    config = {'source_sha256': digest, 'p': str(p), 'cap': args.cap,
              'samples': args.samples, 'seed': args.seed,
              'memory_budget_bytes': required,
              'model': 'ordinary joint returns; later-entry waking suppressed',
              'resident_count': 1}
    cf = directory/'configuration.json'
    if cf.exists():
        assert json.loads(cf.read_text(encoding='utf-8')) == config
    else:
        atomic_json(cf, config)
    # Derive durable progress from populations, not an older checkpoint.
    height = 0
    while (directory/f'height_{height+1:03d}.npy').exists():
        height += 1
    previous = None if height == 0 else np.load(directory/f'height_{height:03d}.npy')
    start = time.monotonic()
    count = 0
    last = None
    while height < args.depth:
        if previous is not None and int(np.max(previous)) >= 10**12:
            atomic_json(directory/'size_guard.json', {'height': height,
                        'reason': 'Stop before integer or support growth risk'})
            break
        height += 1
        rng = np.random.default_rng(args.seed + 1000003*height)
        values = sample_joint(args.samples, float(p), args.cap, previous, rng)
        assert int(np.max(values)) <= (3**(height+1)-1)//2 + args.cap
        target = directory/f'height_{height:03d}.npy'
        part = target.with_suffix('.npy.part')
        with part.open('wb') as stream:
            np.save(stream, values)
        part.replace(target)
        last = metrics(values, p, args.cap, height)
        atomic_json(directory/f'height_{height:03d}_summary.json', last)
        atomic_json(directory/'summary.json', last)
        atomic_json(directory/'checkpoint.json', {'next_height': height+1,
            'complete': height >= args.depth, 'at': datetime.now(timezone.utc).isoformat()})
        previous = values
        count += 1
        if time.monotonic()-start >= args.seconds:
            break
    if last is None and (directory/'summary.json').exists():
        last = json.loads((directory/'summary.json').read_text(encoding='utf-8'))
    print(json.dumps({'directory': str(directory), 'heights_this_chunk': count,
                      'resources': guard, 'last': last}))


if __name__ == '__main__':
    main()
