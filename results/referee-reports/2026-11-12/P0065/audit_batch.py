"""Serial bounded audit runner: this driver plus exactly one numerical child.

Each child has a 280-second alarm; the whole driver also has one. No parallelism.
"""
import os
import signal
signal.alarm(280)
import subprocess
import sys

for law in ('12','24','123','geom'):
    for seed in (101,102,103,104):
        target=f'pool_{law}_{seed}.json'
        if os.path.exists(target):
            continue
        subprocess.run([sys.executable,'audit_pool.py',law,str(seed)],check=True,timeout=279)
for seed in (201,202,203,204):
    if os.path.exists(f'ray_{seed}.json'):
        continue
    subprocess.run([sys.executable,'audit_ray.py',str(seed)],check=True,timeout=279)
