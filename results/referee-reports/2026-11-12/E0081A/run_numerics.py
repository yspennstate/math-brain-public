#!/usr/bin/env python3
"""Reproduce simulations serially. Each seed defines independent trial streams."""
import csv
import json
import math
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'


def governor():
    path=Path.home()/'.claude/compute/compute_state.json'
    if path.exists():
        state=json.loads(path.read_text())
        if state.get('status')=='distress':
            raise RuntimeError('Compute governor reports distress; stop simulation.')


def run(args):
    governor()
    r=subprocess.run([str(ROOT/'simulate'),*map(str,args)],check=True,text=True,capture_output=True)
    return list(csv.DictReader(r.stdout.splitlines()))[0]


def main():
    DATA.mkdir(exist_ok=True)
    # The complete serial run uses roughly three billion simulated steps.
    cases=[(8,2,200000),(12,2,200000),(100,10,30000),(200,14,30000),
           (500,22,20000),(1000,30,20000),(2000,44,20000),
           (10000,100,8000),(100000,316,1000),(1000000,1000,200)]
    with (DATA/'monte_carlo.csv').open('w') as f:
        writer=None
        for i,(n,a,reps) in enumerate(cases):
            row=run(['wait',n,a,reps,810000+i])
            if writer is None:
                writer=csv.DictWriter(f,fieldnames=list(row));writer.writeheader()
            writer.writerow(row);f.flush();print(row,flush=True)
    with (DATA/'record_range.csv').open('w') as f:
        writer=None
        for i,(m,reps) in enumerate([(100,30000),(1000,20000),(10000,10000),(100000,2000)]):
            row=run(['range',m,reps,820000+i])
            if writer is None:
                writer=csv.DictWriter(f,fieldnames=list(row));writer.writeheader()
            writer.writerow(row);f.flush();print(row,flush=True)


if __name__=='__main__':main()
