"""Reproduce every full-state curve, sequentially, at nice >= 10."""
import os
from pathlib import Path
import subprocess


def main():
    if os.getpriority(os.PRIO_PROCESS,0)<10:
        os.setpriority(os.PRIO_PROCESS,0,10)
    for n in range(5,12):
        for model in ['base','double']:
            print(n,model,flush=True)
            with open(f'data/walk_n{n}_{model}.stderr','w') as err:
                subprocess.run(['code/exact_walk',str(n),model,'5000',
                                f'data/walk_n{n}_{model}.csv'],stderr=err,check=True)


if __name__=='__main__':main()
