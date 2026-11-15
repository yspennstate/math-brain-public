#!/usr/bin/env python3
"""Bounded compiler/checker runner; compare exact independent census."""
import csv
import json
import os
import resource
import subprocess
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
os.environ['TMPDIR'] = os.getcwd()
resource.setrlimit(resource.RLIMIT_CPU, (1140, resource.getrlimit(resource.RLIMIT_CPU)[1]))
t = time.monotonic()
subprocess.run(['clang++', '-O2', '-std=c++17', 'independent_check.cpp', '-o', 'independent_check'],
               check=True, timeout=90)
subprocess.run(['./independent_check'], check=True, timeout=1000)
expected = json.load(open('obstructions.json'))['rows']
actual = [{k: int(v) for k, v in row.items()} for row in csv.DictReader(open('independent_counts.csv'))]
assert actual == expected, (actual, expected)
usage = resource.getrusage(resource.RUSAGE_CHILDREN)
assert usage.ru_maxrss < 1024**3
print('PASS: all independent counts match obstructions.json')
print('peak_child_rss_bytes', usage.ru_maxrss)
print('seconds', round(time.monotonic()-t, 3))
