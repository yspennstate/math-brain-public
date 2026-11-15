#!/usr/bin/env python3
"""Replay only the literature certificates needed for regular trees.

This is an audit of the cited preprint, not a new proof or population dynamics.
The Poisson-only interval case 2 and grid cases 0..26 are deliberately omitted.
"""
import hashlib
import json
import os
from pathlib import Path
import resource
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'code' / 'literature_verification'
OUT = ROOT / 'data' / 'literature_checks'


def main():
    assert not sys.flags.optimize
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    OUT.mkdir(exist_ok=True)
    (OUT / 'tmp').mkdir(exist_ok=True)
    env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
               MKL_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1',
               PYTHONDONTWRITEBYTECODE='1', TMPDIR=str(OUT / 'tmp'),
               CLANG_MODULE_CACHE_PATH=str(OUT / 'tmp' / 'clang'))
    records = []

    def run(name, args, expectation=None, timeout=600):
        print('Starting', name, flush=True)
        started = time.monotonic()
        result = {'name': name, 'command': args, 'nice': os.getpriority(os.PRIO_PROCESS, 0)}
        with (OUT / (name + '.stdout.txt')).open('w') as stdout, \
                (OUT / (name + '.stderr.txt')).open('w') as stderr:
            try:
                p = subprocess.run(args, cwd=ROOT, env=env, stdout=stdout,
                                   stderr=stderr, timeout=timeout)
                result['exit_code'] = p.returncode
            except subprocess.TimeoutExpired:
                result['exit_code'] = None
                result['timeout'] = True
        result['seconds'] = time.monotonic() - started
        result['child_peak_rss_bytes_cumulative'] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        out = (OUT / (name + '.stdout.txt')).read_text()
        err = (OUT / (name + '.stderr.txt')).read_text()
        result['passed'] = result['exit_code'] == 0
        if expectation is not None:
            result['expected'] = expectation
            if name.startswith('interval_'):
                case = name.rsplit('_', 1)[1]
                result['passed'] &= out == '' and bool(re.fullmatch(
                    rf'{case},23: {expectation}', err.splitlines()[-1]))
                result['passed'] &= all(re.fullmatch(rf'{case},\d+: \d+', s)
                                        for s in err.splitlines())
            else:
                result['passed'] &= out == expectation
        if name == 'pair':
            result['passed'] &= out == '' and err == ''
        result['passed'] &= 'runtime error:' not in err
        result['passed'] &= 'UndefinedBehaviorSanitizer' not in err
        records.append(result)
        (OUT / 'summary.json').write_text(json.dumps(records, indent=2) + '\n')
        print(json.dumps(result), flush=True)
        return result['passed']

    expected = {
        'pair.py': 'ab775c3a63fb1d2713bfe058af2dece4ceda99627c17ce18f51f817b69410bba',
        'interval.cpp': '76d1443b1194597ee77749e8030c825f2b9aae46b5c172d9eccf0745078c28e3',
        'grid.cpp': '03c92321efedd0db53b1e91372918dfcd68d459db0223cb160c39df3bd645283',
    }
    for filename, digest in expected.items():
        assert hashlib.sha256((SOURCE / filename).read_bytes()).hexdigest() == digest
    run('python_version', [sys.executable, '--version'])
    run('compiler_version', ['/usr/bin/clang++', '--version'])
    if not run('pair', [sys.executable, '-B', str(SOURCE / 'pair.py')]):
        return 1
    # Sanitizer is enabled for both interval and finite-grid executions.
    for name in ['interval', 'grid']:
        if not run('compile_' + name, ['/usr/bin/clang++', '-std=c++17', '-O2',
                   '-UNDEBUG', '-fsanitize=undefined', '-fno-sanitize-recover=undefined',
                   str(SOURCE / (name + '.cpp')), '-o', str(OUT / name)]):
            return 1
    for case, count in [('0', '414080'), ('1', '756096')]:
        if not run('interval_' + case, [str(OUT / 'interval'), case], count):
            return 1
    if not run('grid_regular', [str(OUT / 'grid'), '-1'], '-1 162\n'):
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
