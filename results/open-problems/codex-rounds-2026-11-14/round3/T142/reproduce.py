#!/usr/bin/env python3
"""Rebuild and reproduce the exact enumeration and its audits, sequentially."""
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, 'launch under nice -n 15'
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[name] = '1'
subprocess.run(['clang', '-std=c11', '-O3', '-Wall', '-Wextra', '-Wconversion',
                'quadratic_stream.c', '-o', 'quadratic_stream'], check=True, timeout=120)
for mode, limit in [('bits', '16'), ('dp', '10')]:
    with open(f'stream_{mode}.jsonl', 'w') as data, open(f'stream_{mode}.txt', 'w') as log:
        subprocess.run(['./quadratic_stream', mode, limit], stdout=data, stderr=log,
                       check=True, timeout=1100)
with open('probe.txt', 'w') as f:
    subprocess.run(['./quadratic_stream', 'probe'], stdout=f, check=True, timeout=120)
with open('audit.txt', 'w') as f:
    subprocess.run([sys.executable, 'audit_stream.py'], stdout=f, check=True, timeout=120)
print((ROOT / 'probe.txt').read_text(), end='')
print((ROOT / 'audit.txt').read_text(), end='')
