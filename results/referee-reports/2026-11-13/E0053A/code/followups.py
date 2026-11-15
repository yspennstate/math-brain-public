#!/usr/bin/env python3
"""Run follow-up batches sequentially after the main batch has finished."""
import os,pathlib,subprocess,sys,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
while not (ROOT/'data/large_complete.json').exists():time.sleep(1)
for mode in ['deep','sa']:
    with (ROOT/f'data/{mode}_progress.log').open('a') as f:
        subprocess.run([sys.executable,str(ROOT/'code/experiments.py'),mode],cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,check=True)
    print(mode,'finished',time.strftime('%Y-%m-%dT%H:%M:%S%z'),flush=True)
